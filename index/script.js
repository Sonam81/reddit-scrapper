async function fetchData(subreddit) {

//    Build fetch url and pass to the API for response
    fetch_url = 'http://127.0.0.1:8000/subreddit/' + subreddit
    const res=await fetch (fetch_url);
    const record=await res.json();
    news_list_ul = document.getElementById('news_list');
    news_list_ul.innerHTML = "";

    for (i = 0; i < record.posts.length; i++) {
        li = document.createElement('li')
        a = document.createElement('a');
        a.setAttribute('href', record.posts[i].permalink);
        a.setAttribute('target', '_blank');
        a.textContent = record.posts[i].title;
        li.appendChild(a);
        news_list_ul.appendChild(li);
    }
}
fetchData(subreddit='worldnews');


//var a = document.createElement("a");
//var ulist = document.getElementById("list1");
//var newItem = document.createElement("li");
//
//a.textContent = "...ooo";
//a.setAttribute('href', "http://www.msn.com");
//newItem.appendChild(a);
//ulist.appendChild(newItem);
