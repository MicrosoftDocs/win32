---
description: Selects a client certificate to send to a Secure Hypertext Transfer Protocol (HTTPS) server.
ms.assetid: e76f1e76-5efe-46f2-9a21-064aa06fb3a8
title: IWinHttpRequest::SetClientCertificate method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWinHttpRequest.SetClientCertificate
- WinHttpRequest.SetClientCertificate
api_type: 
- COM
api_location: 
- Winhttp.dll
---

# IWinHttpRequest::SetClientCertificate method

The **SetClientCertificate** method selects a client certificate to send to a Secure Hypertext Transfer Protocol (HTTPS) server.

## Syntax


```C++
HRESULT SetClientCertificate(
  [in] BSTR ClientCertificate
);
```



## Parameters

<dl> <dt>

*ClientCertificate* \[in\]
</dt> <dd>

Specifies the location, [*certificate store*](glossary.md), and subject of a client certificate.

</dd> </dl>

## Return value

The return value is **S\_OK** on success or an error value otherwise.

## Remarks

The string specified in the *ClientCertificate* parameter consists of the certificate location, certificate store, and subject name delimited by backslashes. For more information about the components of the certificate string, see [Client Certificates](ssl-in-winhttp.md).

The certificate store name and location are optional. However, if you specify a certificate store, you must also specify the location of that certificate store. The default location is CURRENT\_USER and the default certificate store is "MY". A blank subject indicates that the first certificate in the certificate store should be used.

Call **SetClientCertificate** to select a certificate before calling [**Send**](iwinhttprequest-send.md) to send the request.

Microsoft Windows HTTP Services (WinHTTP) does not provide client certificates to proxy servers that request certificates for authentication.

> [!Note]  
> For Windows XP and Windows 2000, see the [Run-Time Requirements](winhttp-start-page.md) section of the WinHTTP Start Page.

 

## Examples

The following scripting example shows how to select a client certificate to send with a request. A certificate with the subject "My Middle-Tier Certificate" is chosen from the "Personal" certificate store in the registry under **HKEY\_LOCAL\_MACHINE**. Because this code example is specific to Microsoft JScript, which uses the backslash as an escape character, two adjacent backslashes are required to delimit components of the certificate string.


```JScript
// Instantiate a WinHttpRequest object.
var HttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
    
// Open an HTTP connection.
HttpReq.Open("GET", "https://www.fabrikam.com/", false);
    
// Select a client certificate.
HttpReq.SetClientCertificate(
            "LOCAL_MACHINE\\Personal\\My Middle-Tier Certificate");

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

[SSL in WinHTTP](ssl-in-winhttp.md)
</dt> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

 




