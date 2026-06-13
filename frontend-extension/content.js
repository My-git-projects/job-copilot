chrome.runtime.onMessage.addListener(
    (request,sender,sendResponse)=>{
  
      if(request.action==="getJobText"){
  
        sendResponse({
          text: document.body.innerText
        });
  
      }
  
      return true;
  });