---
Description: 'Refreshes the current document without sending a 'Pragma:no-cache' HTTP header to the server.'
ms.assetid: '66f94cc9-9407-4844-a100-8144fc6f45ce'
title: 'IWebApplicationHost::Refresh method'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWebApplicationHost::Refresh method

Refreshes the current document without sending a 'Pragma:no-cache' HTTP header to the server.

## Syntax


```C++
HRESULT Refresh();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Use this method when the currently executing code is outside of the activation path. If the code is executing inside the activation path, use [**IWebApplicationActivation::CancelPendingActivation**](/previous-versions/windows/desktop/api/WebApplication/nf-webapplication-iwebapplicationactivation-cancelpendingactivation) instead.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                          |
| IDL<br/>                      | <dl> <dt>Webapplication.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWebApplicationHost**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationhost)
</dt> </dl>

 

 




