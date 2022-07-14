const moviesInput = document.querySelector("#movies");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
const titlesList = document.querySelector(".titles-list");

const url = "";
moviesInput.addEventListener("input", async function (e) {
  titlesList.innerHTML = "Available titles:"
  e.preventDefault();
  const fd = new FormData();
  fd.append("csrfmiddlewaretoken", csrf[0].value);
  fd.append("title", moviesInput.value);
  let resp = await fetch(url, { method: "POST", body: fd });
  resp = await resp.json();
  console.log(resp["status"]);
  console.log(resp);
  console.log(resp["titles"]);
  resp["titles"].forEach((element) => {
    const li = document.createElement('li');
    li.appendChild(document.createTextNode(element));
    titlesList.appendChild(li);
  });
});
