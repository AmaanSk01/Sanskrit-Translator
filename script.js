function translateText() {
    let text = document.getElementById("text-input").value;
    let file = document.getElementById("file-upload").files[0];
    let language = document.getElementById("language-select").value;

    let formData = new FormData();
    if (file) {
        formData.append("file", file);
        formData.append("language", language); // File input needs selected language
    } else {
        formData.append("text", text);
        formData.append("language", "san"); // Manual input should always translate to Sanskrit
    }

    fetch("/translate", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("translated-text").innerText = data.translated_text;
    });
}

function downloadText() {
    let text = document.getElementById("translated-text").innerText;
    let blob = new Blob([text], { type: "text/plain" });
    let link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "translated_text.txt";
    link.click();
}
