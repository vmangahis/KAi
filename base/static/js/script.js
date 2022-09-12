document.addEventListener("DOMContentLoaded", (event) => {
    let window_location = window.location.pathname.split('/')[1];
    console.log(window_location);
    if(window_location == 'readlist')
    {
        document.getElementById('readlist-button').classList.add('mode-choice');
        document.getElementById('watchlist-button').classList.remove('mode-choice');
    }
    else if(window_location == 'watchlist'){
        document.getElementById('watchlist-button').classList.add('mode-choice');
        document.getElementById('readlist-button').classList.remove('mode-choice');
    }
    document.querySelectorAll('#watchlist-button, #readlist-button').forEach(ell => {
        ell.addEventListener('click', (e) => {

            let url = "";
            let list_type = "";
            if(e.target.id == 'watchlist-button')
            {
                document.getElementById('watchlist-button').classList.add('mode-choice');
                document.getElementById('readlist-button').classList.remove('mode-choice');
                url = "/watchlist/" + document.getElementById('user_id').textContent;
                list_type = "watchlist";
                
            }
    
            else if(e.target.id == 'readlist-button')
            {   
                document.getElementById('readlist-button').classList.add('mode-choice');
                document.getElementById('watchlist-button').classList.remove('mode-choice');
                url = "/readlist/" + document.getElementById('user_id').textContent;
                list_type = "readlist";
            }
            
            
            fetch(url , 
                {
                    method: "POST",
                    credentials: 'same-origin',
                    body: JSON.stringify({
                        'queryType': list_type
                    })
                    
                })
                .then((res) => res.json())
                .then((data) => {
                    var final = data;
                    var tag = "";
                    console.log(final);
                    final.forEach(elemen => {
                        console.log(elemen.genre);
                    })
                    final.forEach(elem => {
                        if(list_type == "watchlist")
                        {
                            tag+=`<div class = "list-card text-light"><a href="http://${window.location.host}/anime/${elem.id}"><img src="https://via.placeholder.com/300x500" alt="${elem.fields.title}" class="list-card-image" />
                            </a><div class="title-info-text">
                            <h5 class="text-start">${elem.fields.title}</h5><p class="text-start">GenrePlaceHolder</p></div></div>`;
                        }

                        else if(list_type == "readlist")
                        {
                            tag+=`<div class = "list-card text-light"><a href="http://${window.location.host}/manga/${elem.id}"><img src="https://via.placeholder.com/300x500" alt="${elem.fields.title}" class="list-card-image" />
                            </a><div class="title-info-text">
                            <h5 class="text-start">${elem.fields.title}</h5><p class="text-start">GenrePlaceHolder</p></div></div>`;
                        }
                        
                    })
                    document.getElementById('watchlist-card-container').innerHTML = tag;
                })
                .catch((error) => {
                    console.error(error);
                })
        })
    });    

});

