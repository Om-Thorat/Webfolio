var welcome = "Welcome.I am Om!I am curious.clumsy.stupid.a bit lazy. and completely crazy. Have fun looking around*"
//var welcome = "Have fun looking around*"
welcome = welcome.split("")
var x = ""
var a = 0
var skip = false
var y = 0
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
function byebye(){
    skip = true
}
console.log("Hey Welcome to the Console!")
console.log("skipped the message?")
console.log("wondering what the whole thing was?")
console.log("dw it said")
console.log(welcome)
async function type(welcome){
for (let i = 0; i < welcome.length; i++){
    x = x + welcome[i]
    await sleep(40)
    document.getElementById('type').innerText = x
    await sleep(40)
    if ([".","!"].includes(welcome[i])){
        await sleep(240)
        x = ""
        a = a + 1
    }
    if (a == 2){
        document.getElementById("bgimg").src = "/static/questionmark.svg"
        document.getElementById("bgimg").style.animationPlayState = 'running'
        //todo = true
    }
    if (a == 3){
        y = 0
        document.getElementById("bgimg").src = ""
    }
    if (welcome[i] == "*" || skip){
        document.getElementById('skip').style.display="none"
        document.getElementById("bgimg").src = ""
        await sleep(600)
        //document.getElementById("type").classList.add("animate__animated")
        //document.getElementById("type").classList.add("animate__fadeOutUps")
        //document.getElementById('blink').style.animationPlayState = 'none'
        document.getElementById("run").style.animationPlayState = "running"
        await sleep(700)
        document.getElementById("page").style.display = "flex"
        document.getElementById("intro").style.display = "none"
        document.getElementById("bg").style.justifyContent = ""
        document.getElementById("page").style.animationPlayState = "running"
        await sleep(2000)
        document.body.style.overflow = ""
        document.body.style.overflowX = "hidden"
}}}
function work(){
    document.getElementById('work').style.animation = "sheesh 3s infinite"
    document.getElementById('home').style.animation = ""
    document.getElementById('stuff').style.animation = ""
    document.getElementById('feed').style.display = ""
    document.getElementById('feed').style.flexDirection = ""
    document.getElementById("feed").innerText = "Hire me so i can add things here"
}
function home(){
    document.getElementById('stuff').style.animation=""
    document.getElementById('work').style.animation = ""
    document.getElementById('home').style.animation = "sheesh 3s infinite"
    document.getElementById('feed').style.display = ""
    document.getElementById('feed').style.flexDirection = ""
    // document.getElementById("feed").innerHTML = `<br>I am Om, Currently doing my bachelors in Computer Science at somewhere</br>
    // <br>Trying to squeeze out every ounce of experience i can before i am kicked off the stage.</br>
    // <br>That's me and this website is my verse in the grand play of the universe.</br>`
    document.getElementById("feed").innerHTML = `<br> Hey I am Om, Currently trying to get a college i'll love to spend the best 4 years of my life at.</br>
    <br>Hopefully i get it 🤞</br>`
}
function stuff(){
    document.getElementById('stuff').style.animation="sheesh 3s infinite"
    document.getElementById('work').style.animation = ""
    document.getElementById('home').style.animation = ""
    // function sus(data)
    // {
    //     document.getElementById('feed').innerHTML =( `</br>${data[1]}<br> by ${data[3]}
    //     <div>
    //     <img class="song" style="width:15vw;
    //     max-width:110px;
    //     padding-top:1%" src=${data[2]}></div>
    //     ${data[0]}<br></br>`)
    //     document.getElementById('stuff').style.animation="sheesh 3s infinite"
    //     document.getElementById('work').style.animation = ""
    //     document.getElementById('home').style.animation = ""}
    // document.getElementById('feed').style.display = "flex"
    // document.getElementById('feed').style.flexDirection = "column-reverse"
    // fetch('/spotifyinfo')
    // .then(response => response.json())
    // .then(data => sus(data))
    document.getElementById('feed').innerHTML = `<img class="song" style="padding:2vw;max-height:20vh" src='/spotify'>`
}
type(welcome)