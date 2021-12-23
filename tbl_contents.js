function scroll_bottom() {
  var objDiv = document.getElementById("contents");
  objDiv.scrollTop = objDiv.scrollHeight;
}


function toggle_show_spoiler() {
  var x = document.getElementsByClassName("spoiler");
  for (let i = 0; i < x.length; i++) {
    toggle_spoiler(x[i])
  }
}



function toggle_show() {
  var x = document.getElementById("toc_frame");
  if (x.style.display == "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function toggle_spoiler(obj) {
  if (obj.style.height == "10px") {
    obj.style.height = "auto";
  } else {
    obj.style.height = "10px";
  }
}

function click_spoiler(event) {
  x = event.target;
  toggle_spoiler(x);
}

window.onload = function () {

    var x = document.getElementsByClassName("spoiler");
    for (let i = 0; i < x.length; i++) {
      x[i].style.height = "10px";
      /*x[i].addEventListener("click", click_spoiler );*/
    }

    var x = document.getElementById("toc_frame");
    x.style.display = "none";

    var toc = "";
    var level = 0;

    document.getElementById("contents").innerHTML =
        document.getElementById("contents").innerHTML.replace(
            /<h([\d])>([^<]+)<\/h([\d])>/gi,
            function (str, openLevel, titleText, closeLevel) {
                if (openLevel != closeLevel) {
                    return str;
                }

                if (openLevel > level) {
                    toc += (new Array(openLevel - level + 1)).join("<ul>");
                } else if (openLevel < level) {
                    toc += (new Array(level - openLevel + 1)).join("</ul>");
                }

                level = parseInt(openLevel);

                var anchor = titleText.replace(/ /g, "_");
                toc += "<li><a href=\"#" + anchor + "\">" + titleText
                    + "</a></li>";

                return "<h" + openLevel + "><a name=\"" + anchor + "\">"
                    + titleText + "</a></h" + closeLevel + ">";
            }
        );

    if (level) {
        toc += (new Array(level + 1)).join("</ul>");
    }

    document.getElementById("toc").innerHTML += toc;
};
