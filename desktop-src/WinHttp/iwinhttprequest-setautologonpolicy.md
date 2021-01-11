---
description: Sets the current Automatic Logon Policy.
ms.assetid: bc8e8c9c-574e-4392-b336-2c06947022ee
title: IWinHttpRequest::SetAutoLogonPolicy method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWinHttpRequest.SetAutoLogonPolicy
- WinHttpRequest.SetAutoLogonPolicy
api_type: 
- COM
api_location: 
- Winhttp.dll
---

# IWinHttpRequest::SetAutoLogonPolicy method

The **SetAutoLogonPolicy** method sets the current [Automatic Logon Policy](authentication-in-winhttp.md).

## Syntax


```C++
HRESULT SetAutoLogonPolicy(
  [in] WinHttpRequestAutoLogonPolicy AutoLogonPolicy
);
```



## Parameters

<dl> <dt>

*AutoLogonPolicy* \[in\]
</dt> <dd>

Specifies the current automatic logon policy.

</dd> </dl>

## Return value

The return value is **S\_OK** on success or an error value otherwise.

## Remarks

The default policy is [**AutoLogonPolicy\_OnlyIfBypassProxy**](winhttprequestautologonpolicy.md).

Call **SetAutoLogonPolicy** to set the automatic logon policy before calling [**Send**](iwinhttprequest-send.md) to send the request.

> [!Note]  
> For Windows XP and Windows 2000, see the [Run-Time Requirements](winhttp-start-page.md) section of the WinHTTP Start Page.

 

## Examples

The following scripting example shows how to set the automatic logon policy to never use NTLM or Negotiate authentication automatically.


```JScript
// Instantiate a WinHttpRequest object.
var HttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
    
// Open an HTTP connection.
HttpReq.Open("GET", "https://www.fabrikam.com/", false);
    
// Do not automatically send user credentials.
HttpReq.SetAutoLogonPolicy(2);

// Send the HTTP Request.
HttpReq.Send();
```



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

[Authentication in WinHTTP](authentication-in-winhttp.md)
</dt> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

 




