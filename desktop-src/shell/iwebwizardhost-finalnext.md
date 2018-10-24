---
Description: Navigates to the client-side wizard page that follows the page that hosts the server-side HTML pages, or finishes the wizard if there are no further client-side pages.
title: WebWizardHost.FinalNext method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WebWizardHost.FinalNext
api_type: 
- COM
api_location: 
- Shldisp.h
---

# WebWizardHost.FinalNext method

Navigates to the client-side wizard page that follows the page that hosts the server-side HTML pages, or finishes the wizard if there are no further client-side pages.

## Syntax


```JScript
iRetVal = WebWizardHost.FinalNext()
```



## Parameters

This method has no parameters.

## Remarks

When the wizard is displaying the last server-side HTML page and the user clicks the **Next** or **Finish** button, the server invokes **FinalNext** in that button's event handler.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl> |



 

 




