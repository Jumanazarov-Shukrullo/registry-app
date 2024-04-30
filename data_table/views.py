from datetime import datetime

from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Table


def index(request):
    # Retrieve all items from the Table model
    all_items = Table.objects.all()

    # Search functionality
    query = request.GET.get('q')
    if query:
        query = query.strip()
        # Parse the search query into a valid date object
        try:
            parsed_date = datetime.strptime(query, '%Y-%m-%d').date()
        except ValueError:
            try:
                parsed_date = datetime.strptime(query, '%B %d, %Y').date()
            except ValueError:
                try:
                    parsed_date = datetime.strptime(query, '%b. %d, %Y').date()
                except ValueError:
                    parsed_date = None
        # If parsed_date is not None, format it to match the format of dates stored in the database
        if parsed_date:
            formatted_date = parsed_date.strftime('%Y-%m-%d')
            all_items = all_items.filter(
                Q(fullname__icontains=query) |
                Q(date_of_registration__icontains=formatted_date) |
                Q(abbreviated_name__icontains=query) |
                Q(licence_number__icontains=query) |
                Q(inn__icontains=query) |
                Q(status__icontains=query) |
                Q(deadline__icontains=formatted_date) |  # Search in the deadline field
                Q(address__icontains=query) |
                Q(termination_date__icontains=formatted_date)
            )
        else:
            # If parsed_date is None, perform regular search without date filtering
            all_items = all_items.filter(
                Q(fullname__icontains=query) |
                Q(date_of_registration__icontains=query) |
                Q(abbreviated_name__icontains=query) |
                Q(licence_number__icontains=query) |
                Q(inn__icontains=query) |
                Q(status__icontains=query) |
                Q(deadline__icontains=query) |
                Q(address__icontains=query) |
                Q(termination_date__icontains=query)
            )
    paginator = Paginator(all_items, 50)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Count the number of items returned by the query
    num_rows_rendered = all_items.count()
    # Pass the items, pagination, and search query to the template for rendering
    return render(request, 'index.html', {'page_obj': page_obj, 'query': query, 'num_rows_rendered': num_rows_rendered})
