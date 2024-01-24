---
description: Retrieves the response entity body as an array of unsigned bytes.
ms.assetid: 557913e0-9f19-42fc-bfca-9ed248972b4b
title: IWinHttpRequest::ResponseBody property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWinHttpRequest.ResponseBody
- IWinHttpRequest.get_ResponseBody
- WinHttpRequest.ResponseBody
api_type: 
- COM
api_location: 
- Winhttp.dll
---

# IWinHttpRequest::ResponseBody property

The **ResponseBody** property retrieves the response entity body as an array of unsigned bytes.

This property is read-only.

## Syntax


```C++
HRESULT get_ResponseBody(
  [out, retval] VARIANT *Body
);
```


```JScript

vtResponseBody = WinHttpRequest.ResponseBody
```





## Property value

A **Variant** value that receives the response entity body as an array of unsigned bytes. This array contains the raw data as received directly from the server.

## Error codes

The return value is **S\_OK** on success or an error value otherwise.

## Remarks

This property returns the response data in an array of unsigned bytes. If the response does not have a response body, an empty variant is returned. This property can only be invoked after the [**Send**](iwinhttprequest-send.md) method has been called.

> [!Note]  
> For more information about implementation for Windows XP and Windows 2000, see [Run-Time Requirements](winhttp-start-page.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>            |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>         |
| Redistributable<br/>          | WinHTTP 5.0 and Internet Explorer 5.01 or later on Windows XP and Windows 2000.<br/> |
| IDL<br/>                      | <dl> <dt>HttpRequest.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winhttp.lib</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Winhttp.dll</dt> </dl>     |



## See also

<dl> <dt>

[**IWinHttpRequest**](iwinhttprequest-interface.md)
</dt> <dt>

[**WinHttpRequest**](winhttprequest.md)
</dt> <dt>

[**ResponseStream**](iwinhttprequest-responsestream.md)
</dt> <dt>

[**ResponseText**](iwinhttprequest-responsetext.md)
</dt> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

 




