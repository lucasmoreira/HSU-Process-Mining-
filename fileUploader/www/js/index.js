function onDeviceReady() {
    console.log("Device is ready.");
    document.getElementById("uploadButton").addEventListener("click", uploadFile);
}

document.addEventListener("deviceready", onDeviceReady, false);

function onDeviceReady() {
    document.getElementById("uploadButton").addEventListener("click", uploadFile);
}

function uploadFile() {
    var fileInput = document.getElementById("file");
    var file = fileInput.files[0];
    var serverUrl = "http://127.0.0.1:5000/upload"; // Replace with your Flask server URL

    if (file) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", serverUrl, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    alert("File uploaded successfully.");
                } else {
                    alert("Error uploading file.");
                }
            }
        };

        var formData = new FormData();
        formData.append("file", file);
        xhr.send(formData);
    } else {
        alert("Please select a file to upload.");
    }
}