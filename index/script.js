async function fetchData() {
    const res=await fetch ('http://127.0.0.1:8000/subreddit/pics');
    const record=await res.json();
    news_list_ul = document.getElementById('news_list');
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
fetchData();


//var a = document.createElement("a");
//var ulist = document.getElementById("list1");
//var newItem = document.createElement("li");
//
//a.textContent = "...ooo";
//a.setAttribute('href', "http://www.msn.com");
//newItem.appendChild(a);
//ulist.appendChild(newItem);
