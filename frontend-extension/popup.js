document
.getElementById("scanBtn")
.addEventListener("click", async ()=>{

    const [tab] =
      await chrome.tabs.query({
        active:true,
        currentWindow:true
      });

    chrome.tabs.sendMessage(
      tab.id,
      {
        action:"getJobText"
      },

      async(response)=>{

        const api =
          await fetch(
            "http://127.0.0.1:8000/analyze",
            {
              method:"POST",

              headers:{
                "Content-Type":
                "application/json"
              },

              body:JSON.stringify({
                text:response.text
              })
            }
          );

        const data =
          await api.json();

        document
        .getElementById("results")
        .innerHTML =

`Match Score:
${data.score}%

Matched:
${data.matched.join(", ")}

Missing:
${data.missing.join(", ")}
`;
      }
    );
});