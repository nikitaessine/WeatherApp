 // js code to call python functions
 async function display_weather(){
    let place = document.getElementById("location").value;

    //call function get_weather from python code
    let res = await eel.get_weather(place)();
    document.getElementById('info').innerHTML = res;
}

jQuery("#show").on('click', function(){
    //by pressing button weather displays
    display_weather();
});