/**
 * @author <code@tythos.net>
 */

function onWindowLoad(event) {
    console.log("window loaded:", event);
    let div = window.document.createElement("div");
    div.textContent = "Window loaded.";
    window.document.body.appendChild(div);
}

window.addEventListener("load", onWindowLoad);
