---
description: Occurs when there is a run-time error in the application.
ms.assetid: d99400a4-3661-4162-bfd6-8c2a27e0f328
title: IWinHttpRequestEvents::OnError event
ms.topic: reference
ms.date: 05/31/2018
---

# IWinHttpRequestEvents::OnError event

The **OnError** event occurs when there is a run-time error in the application.

## Syntax


```C++
void OnError(
  [in] long ErrorNumber,
  [in] BSTR ErrorDescription
);
```



## Parameters

<dl> <dt>

*ErrorNumber* \[in\]
</dt> <dd>

Receives the numerical value of the error. The lower 16 bits of this error number corresponds to one of the errors listed in [**Error Messages**](error-messages.md).

</dd> <dt>

*ErrorDescription* \[in\]
</dt> <dd>

Specifies a short description of the error which occurred.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

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

 

 




