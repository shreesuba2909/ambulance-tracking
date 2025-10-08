def find_nearest_hospitals(lat, lng, radius):
    hospitals = []
    try:
        places = gmaps.places_nearby(location=(lat, lng), radius=radius, type='hospital')
        
        # Process the initial set of results
        if 'results' in places:
            for place in places['results']:
                name = place['name']
                address = place.get('vicinity', 'N/A')
                hospital_lat = place['geometry']['location']['lat']
                hospital_lng = place['geometry']['location']['lng']
                

                hospitals.append((name, address, hospital_lat, hospital_lng))

        # Check for next page of results
        while 'next_page_token' in places:
         
            places = gmaps.places_nearby(page_token=places['next_page_token'])
            if 'results' in places:
                for place in places['results']:
                    name = place['name']
                    address = place.get('vicinity', 'N/A')
                    hospital_lat = place['geometry']['location']['lat']
                    hospital_lng = place['geometry']['location']['lng']
                    

                    hospitals.append((name, address, hospital_lat, hospital_lng))

    except Exception as e:
        print(f"An error occurred while finding hospitals: {e}")

    return hospitals