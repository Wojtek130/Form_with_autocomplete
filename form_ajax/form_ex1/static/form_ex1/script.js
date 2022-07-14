console.log("world2222");
const form = document.querySelector("#p-form");
// console.log(form);

const login = document.querySelector("#id_login");
const password = document.querySelector("#id_password");
const password_conf = document.querySelector("#id_password_conf");
const birth_date = document.querySelector("#id_birth_date");
const csrf = document.getElementsByName("csrfmiddlewaretoken");

const url = "";
console.log("whatever");

form.addEventListener("submit", async function (e) {
  e.preventDefault();
  $(".control").html("");
  const fd = new FormData();
  fd.append("csrfmiddlewaretoken", csrf[0].value);
  fd.append("login", login.value);
  fd.append("password", password.value);
  fd.append("password_conf", password_conf.value);
  fd.append("birth_date", birth_date.value);
  console.log("in the script");
  // try {
  //   let resp = await fetch(url, { method: "POST", body: fd });
  //   resp = await resp.json();
  //   console.log(resp, "!!!");
  //   if (resp["status"] === "error") {
  //     console.log("right place");
  //     const errors = resp["mes"];
  //     const controlList = document.querySelector(".control");
  //     errors.forEach((element) => {
  //       const li = document.createElement('li');
  //       li.appendChild(document.createTextNode(element));
  //       controlList.appendChild(li);
  //     });
  //   } else {
  //     setTimeout(() => {
  //       login.value = "";
  //       password.value = "";
  //       password_conf.value = "";
  //       password.value = "";
  //       birth_date.value = "2000-01-01";
  //     }, 2500);
  //   }
  // } catch (err) {
  //   console.error(err);
  // }

  $.ajax({
    type: "POST",
    url: url,
    data: fd,
    success: function (response) {
      console.log("jq1");
      console.log(response);
      if (response["status"] === "error") {
        let err_html = "";
        const errors = response["mes"];
        errors.forEach((element) => {
          err_html += `<li>${element}</li>`;
        });
        $(".control").html(err_html);
      } else {
      console.log("jq2");

        setTimeout(() => {
          login.value = "";
          password.value = "";
          password_conf.value = "";
          password.value = "";
          birth_date.value = "2000-01-01";
        }, 2500);
      }
    },
    error: function (err) {
      console.log(
        "ajacx------------------------------------------------------"
      );
      console.log(err);
    },
    cache: false,
    contentType: false,
    processData: false,
  });
});
