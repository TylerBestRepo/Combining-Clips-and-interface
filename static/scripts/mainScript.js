
let form = document.getElementById('numberSubmitForm');

let submitBtn = document.getElementById('goBtn');
let nextBtn = document.getElementById('genFileBoxes');
let numClips = document.getElementById('numClips');
let locationSpaceDiv = document.getElementById('spaceForLocations');
submitBtn.style.display = 'none';



nextBtn.addEventListener('click', () => generateFileBoxes(numClips.value))

function generateFileBoxes(numClips) {
    console.log(numClips)
    let i = 0;

    while (i < numClips) {
        var input = document.createElement("input");
        input.type = "text";
        input.name = "clip" + i
        input.className = "fileDirectories"; // set the CSS class
        locationSpaceDiv.appendChild(input);// put it into the DOM
        i += 1;
    }
    nextBtn.style.display = 'none';

    numClips.className = 'removeNumClips';

    submitBtn.style.display = 'block';


     
}