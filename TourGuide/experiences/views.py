from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.

def search(request):
    if request.method == 'GET':
        destination = request.GET['destination']
        category = request.GET['category']

        # Retrieve Airbnb tours
        airbnb_url = f'https://www.airbnb.com/api/v2/explore_tabs?version=1.3.9&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid=18&guidebooks_per_grid=20&auto_ib=false&fetch_filters=true&has_zero_guest_treatment=false&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=false&query_understanding_enabled=true&show_groupings=true&supports_for_you_v3=true&timezone_offset=-240&client_session_id=f9079a9c-7f5c-4c43-8c0f-d1f6e49c6a3a&metadata_only=false&is_standard_search=true&refinement_paths%5B%5D=%2Ftours&selected_tab_id=tours&place_id=ChIJE9on3F3HwoAR9AhGJW_fL-I&query={destination}'
        airbnb_response = requests.get(airbnb_url).json()
        airbnb_tours = [x for x in airbnb_response['explore_tabs'][0]['sections'][0]['listings'] if category in x['subcategory']]

        # Retrieve TripAdvisor tours
        tripadvisor_url = f'https://www.tripadvisor.com/api/partner/2.0/location/{destination}/tours?limit=30'
        tripadvisor_response = requests.get(tripadvisor_url).json()
        tripadvisor_tours = [x for x in tripadvisor_response['data'] if category in x['category']]

        # return HttpResponse(template.render(context, request))
        return render(request, 'templates/index.html', {'airbnb_tours': airbnb_tours, 'tripadvisor_tours': tripadvisor_tours})
    else:
        return render(request, 'index.html')