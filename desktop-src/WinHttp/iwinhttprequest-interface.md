---
description: The IWinHttpRequest interface provides all of the nonevent methods for Microsoft Windows HTTP Services (WinHTTP).
ms.assetid: 6417b3b5-b74a-4c7b-acf9-87e2e814a4df
title: IWinHttpRequest interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWinHttpRequest
api_type: 
- COM
api_location: 
- Winhttp.dll
---

# IWinHttpRequest interface

The **IWinHttpRequest** interface provides all of the nonevent methods for [Microsoft Windows HTTP Services (WinHTTP)](about-winhttp.md).

## Members

The **IWinHttpRequest** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWinHttpRequest** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWinHttpRequest** interface has these methods.



| Method                                                                 | Description                                                                                                                             |
|:-----------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| [**Abort**](iwinhttprequest-abort.md)                                 | Aborts a [WinHTTP](about-winhttp.md) [**Send**](iwinhttprequest-send.md) method.<br/>                                           |
| [**GetAllResponseHeaders**](iwinhttprequest-getallresponseheaders.md) | Retrieves all HTTP response headers.<br/>                                                                                         |
| [**GetResponseHeader**](iwinhttprequest-getresponseheader.md)         | Retrieves the HTTP response headers.<br/>                                                                                         |
| [**Open**](iwinhttprequest-open.md)                                   | Opens an HTTP connection to an HTTP resource.<br/>                                                                                |
| [**Send**](iwinhttprequest-send.md)                                   | Sends an HTTP request to an HTTP server.<br/>                                                                                     |
| [**SetAutoLogonPolicy**](iwinhttprequest-setautologonpolicy.md)       | Sets the current [Automatic Logon Policy](authentication-in-winhttp.md).<br/>                             |
| [**SetClientCertificate**](iwinhttprequest-setclientcertificate.md)   | Selects a client certificate to send to a Secure Hypertext Transfer Protocol (HTTPS) server.<br/>                                 |
| [**SetCredentials**](iwinhttprequest-setcredentials.md)               | Sets credentials to be used with an HTTP server, either a proxy server or an originating server.<br/>                             |
| [**SetProxy**](iwinhttprequest-setproxy.md)                           | Sets proxy server information.<br/>                                                                                               |
| [**SetRequestHeader**](iwinhttprequest-setrequestheader.md)           | Adds, changes, or deletes an HTTP request header.<br/>                                                                            |
| [**SetTimeouts**](iwinhttprequest-settimeouts.md)                     | Specifies the individual time-out components of a send/receive operation, in milliseconds.<br/>                                   |
| [**WaitForResponse**](iwinhttprequest-waitforresponse.md)             | Waits for an asynchronous [**Send**](iwinhttprequest-send.md) method to complete, with optional time-out value, in seconds.<br/> |



 

### Properties

The **IWinHttpRequest** interface has these properties.



| Property                                                            | Access type           | Description                                                           |
|:--------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------|
| [**Option**](iwinhttprequest-option.md)<br/>                 | Read/write<br/> | A WinHTTP option value.<br/>                                    |
| [**ResponseBody**](iwinhttprequest-responsebody.md)<br/>     | Read-only<br/>  | The response entity body as an array of unsigned bytes.<br/>    |
| [**ResponseStream**](iwinhttprequest-responsestream.md)<br/> | Read-only<br/>  | The response entity body as an [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream).<br/> |
| [**ResponseText**](iwinhttprequest-responsetext.md)<br/>     | Read-only<br/>  | The response entity body.<br/>                                  |
| [**Status**](iwinhttprequest-status.md)<br/>                 | Read-only<br/>  | The HTTP status code from the last response.<br/>               |
| [**StatusText**](iwinhttprequest-statustext.md)<br/>         | Read-only<br/>  | The HTTP status text.<br/>                                      |



 

## Remarks

The **IWinHttpRequest** interface defined in httprequest.idl is implemented by a class with id of **CLSID\_WinHttpRequest**. An application obtain this interface by calling [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) with a class id of **CLSID\_WinHttpRequest** and an interface id of **IID\_IWinHttpRequest**.

> [!Note]  
> For Windows XP and Windows 2000, see the [Run-Time Requirements](winhttp-start-page.md) section of the WinHttp start page.

 

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

[**IWinHttpRequestEvents**](iwinhttprequestevents-interface.md)
</dt> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

