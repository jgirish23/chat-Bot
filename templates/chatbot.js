var objDiv = document.getElementById("scroll-container");
objDiv.scrollTop = objDiv.scrollHeight;

let count = 0;
const button_post = document.getElementById("button-addon2");
const text = document.getElementById("user-text");

console.log(text.value);
text.addEventListener("keypress", async (e) => {
  if (e.key === "Enter") {
    console.log("Enter key clicked");
    Handel_post_request(e);
  }
});
button_post.addEventListener("click", async (e) => {
  console.log("button clicked");
  Handel_post_request(e);
});
async function Handel_post_request(e) {
  try {
    const response = await fetch("/chatbot", {
      method: "POST",
      body: JSON.stringify({
        Text: text.value,
        Username: "{{user.username}}",
        Check: 1,
        Text_count: count + 1,
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    });
    // console.log("Completed!!!", response);
    location.reload();
  } catch (err) {
    console.error(`Error: ${err}`);
  }
}
