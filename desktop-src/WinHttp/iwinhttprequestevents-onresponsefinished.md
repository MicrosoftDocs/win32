---
description: Occurs when the response data is complete.
ms.assetid: 0df2031e-826f-436e-a689-201fa8b5c38f
title: IWinHttpRequestEvents::OnResponseFinished event
ms.topic: reference
ms.date: 05/31/2018
---

# IWinHttpRequestEvents::OnResponseFinished event

The **OnResponseFinished** event occurs when the response data is complete.

## Syntax


```C++
void OnResponseFinished();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

This event signals that all of the response data that pertains to the most recent request has been received. [**OnResponseDataAvailable**](iwinhttprequestevents-onresponsedataavailable.md) does not occur again until the next request.

> [!Note]  
> For Windows XP and Windows 2000, see the [Run-Time Requirements](winhttp-start-page.md) section of the WinHTTP Start Page.

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>            |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>         |
| Redistributable<br/>          | WinHTTP 5.0 and Internet Explorer 5.01 or later on Windows XP and Windows 2000.<br/> |
| IDL<br/>                      | <dl> <dt>HttpRequest.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWinHttpRequestEvents**](iwinhttprequestevents-interface.md)
</dt> <dt>

[**WinHttpRequest**](winhttprequest.md)
</dt> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

 




