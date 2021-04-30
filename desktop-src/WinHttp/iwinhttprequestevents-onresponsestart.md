---
description: Occurs when the response data starts to be received.
ms.assetid: 7245725b-40dd-4282-b681-f0b2c191db94
title: IWinHttpRequestEvents::OnResponseStart event
ms.topic: reference
ms.date: 05/31/2018
---

# IWinHttpRequestEvents::OnResponseStart event

The **OnResponseStart** event occurs when the response data starts to be received.

## Syntax


```C++
void OnResponseStart(
  [in] long Status,
  [in] BSTR ContentType
);
```



## Parameters

<dl> <dt>

*Status* \[in\]
</dt> <dd>

Receives the standard status code returned with the response data. Status codes are defined in [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt).

</dd> <dt>

*ContentType* \[in\]
</dt> <dd>

Specifies the type of content received, such as "text/html" or "image/gif".

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

For this event to occur, use [**Open**](iwinhttprequest-open.md) to send an HTTP connection in asynchronous mode and use [**Send**](iwinhttprequest-send.md) to send a data request to an Internet server.

This is the first WinHTTP event to occur after the [**Send**](iwinhttprequest-send.md).

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

 

 




