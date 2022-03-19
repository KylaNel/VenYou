current_stars = {
    'hygiene_stars':0,
    'vibe_stars':0,
    'safety_stars':0,
}


function setStarsTo(x, star_container_id){
    star_container = document.getElementById(star_container_id);
    stars = star_container.getElementsByClassName('star');
    for( var i = 0; i < x; i++){
        stars[i].setAttribute('class', 'fa fa-star star');
    }
    for( var j = x; i < 5; i++){
        stars[i].setAttribute('class', 'fa fa-star-o star');
    }
}

function updateStars(event){
    pos = event.target.getAttribute('pos');

    rating = event.target.getAttribute('parentId');
    current_stars[rating] = pos;
    setStarsTo(pos, rating);
    updateForm();
}

function clearStars(event){
    rating = event.target.getAttribute('parentId');
    if (rating == null){
        console.log(event.target)
    }
    setStarsTo(current_stars[rating], rating);
}

function hoverStars(event){
    pos = event.target.getAttribute('pos');
    rating = event.target.getAttribute('parentId');
    setStarsTo(pos, rating);
}

function createStars(masterDiv){
    for (var i=0; i<5; i++){
        var newDiv = document.createElement('div');
        var newLink = document.createElement('a');
        newLink.setAttribute("pos",i+1);
        
        newDiv.setAttribute("parentId", masterDiv.getAttribute('id'));
        newLink.setAttribute("parentId", masterDiv.getAttribute('id'));
        newDiv.appendChild(newLink);
        newLink.setAttribute("class", "fa fa-star-o star");
        masterDiv.appendChild(newDiv);
    }
}

function createStarRating(id, labelText){
    var label = document.createElement('h4');
    var area = document.getElementById('star_rating_area');
    area.appendChild(label);
    label.innerHTML = labelText;

    var newRating = document.createElement('div');
    newRating.setAttribute('class', 'rating')
    newRating.setAttribute('id', id);
    area.appendChild(newRating);
    createStars(newRating);
}


$(function(){

    createStarRating('hygiene_stars', 'Hygiene score: ');
    createStarRating('vibe_stars', 'Vibe score: ');
    createStarRating('safety_stars', 'Safety score: ');
    updateForm();

    $('.star').click(updateStars);
    $('.rating div').mouseleave(clearStars);
    $('.star').mouseover(hoverStars);
})


function addStarsToForm(){
    console.log('yikes');
    alert();
    return false;
}

function updateForm(){
    rate_form = document.forms['rate'];
    rate_form['hygiene_score'].value = current_stars['hygiene_stars'];
    rate_form['vibe_score'].value = current_stars['vibe_stars'];
    rate_form['safety_score'].value = current_stars['safety_stars'];
}