function initMap() {
    // LOCATIONS
    const subClub = { lat: 55.85802559710552, lng: -4.25716789944254 };

    


    // MAP CENTRED AT LOCATION
    const map = new google.maps.Map(
        document.getElementById("map"),
        {
            zoom: 18,
            center: subClub,
        }
    );

    // MAP MARKER POSITIONED AT LOCATION
    const marker = new google.maps.Marker({
        position: subClub,
        map,
    });
}