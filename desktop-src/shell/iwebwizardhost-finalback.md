---
Description: Navigates to the client-side page immediately preceding the page hosting the server-side HTML pages.
title: WebWizardHost.FinalBack method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WebWizardHost.FinalBack method

Navigates to the client-side page immediately preceding the page hosting the server-side HTML pages.

## Syntax


```JScript
iRetVal = WebWizardHost.FinalBack()
```



## Parameters

This method has no parameters.

## Remarks

When the wizard displays the first server-side page and the user clicks the **Back** button, the server invokes **FinalBack** when notified of that event by the client's event handler.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl> |



 

 




