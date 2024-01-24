---
description: Occurs when data is available from the response.
ms.assetid: 62d02e3b-466a-4d3d-994b-0a1ae12049e1
title: IWinHttpRequestEvents::OnResponseDataAvailable event
ms.topic: reference
ms.date: 05/31/2018
---

# IWinHttpRequestEvents::OnResponseDataAvailable event

The **OnResponseDataAvailable** event occurs when data is available from the response.

## Syntax


```C++
void OnResponseDataAvailable(
  [in] SAFEARRAY(unsigned char) *Data
);
```



## Parameters

<dl> <dt>

*Data* \[in\]
</dt> <dd>

A zero-based array of bytes that receives the response data received by Microsoft Windows HTTP Services (WinHTTP) up to the point that this event occurs. This is a **VARIANT** of type VT\_ARRAY \| VT\_UI1.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Because data is in bytes, it must be converted to wide characters when placed in a wide character (Unicode) string.

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

 

 




