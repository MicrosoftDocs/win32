---
Description: This topic provides information about using the WinHTTP WinHttpRequest COM object with scripting languages.
ms.assetid: 0bbbf3dc-84b8-41d8-8627-e3d80ddcb783
title: WinHttpRequest object
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/22/2020
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WinHttpRequest
api_type: 
- COM
api_location: 
- Winhttp.dll
---

# WinHttpRequest object

This topic provides information about using the WinHTTP **WinHttpRequest** COM object with scripting languages. For more information, including the C++ API (WinHTTP) please see [About WinHTTP](about-winhttp.md). See [Choosing a WinHTTP Interface](choosing-a-winhttp-interface.md) for a comparison of these interfaces.

## Example

```javascript
// Instantiate a WinHttpRequest object.
var WinHttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
```

```cpp
 IWinHttpRequest *  pIWinHttpRequest = NULL;
 \\..
    hr = CLSIDFromProgID(L"WinHttp.WinHttpRequest.5.1", &clsid);

    if (SUCCEEDED(hr))
    {
        hr = CoCreateInstance(clsid, NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IWinHttpRequest,
                              (void **)&pIWinHttpRequest);
    }
```

Code examples taken from [IWinHttpRequest::Status property](iwinhttprequest-status.md).



## Members

The **WinHttpRequest** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **WinHttpRequest** object has these events.



| Event                                                                            | Description                                                          |
|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------|
| [**OnError**](iwinhttprequestevents-onerror.md)                                 | Occurs when there is a run-time error in the application.<br/> |
| [**OnResponseDataAvailable**](iwinhttprequestevents-onresponsedataavailable.md) | Occurs when data is available from the response.<br/>          |
| [**OnResponseFinished**](iwinhttprequestevents-onresponsefinished.md)           | Occurs when the response data is complete.<br/>                |
| [**OnResponseStart**](iwinhttprequestevents-onresponsestart.md)                 | Occurs when the response data starts to be received.<br/>      |



 

### Methods

The **WinHttpRequest** object has these methods.



| Method                                                                 | Description                                                                                                                                                |
|:-----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Abort**](iwinhttprequest-abort.md)                                 | Aborts a [WinHTTP](about-winhttp.md) [**Send**](iwinhttprequest-send.md) method.<br/>                                                              |
| [**GetAllResponseHeaders**](iwinhttprequest-getallresponseheaders.md) | Retrieves all HTTP response headers.<br/>                                                                                                            |
| [**GetResponseHeader**](iwinhttprequest-getresponseheader.md)         | Retrieves the HTTP response headers.<br/>                                                                                                            |
| [**Open**](iwinhttprequest-open.md)                                   | Opens an HTTP connection to an HTTP resource.<br/>                                                                                                   |
| [**Send**](iwinhttprequest-send.md)                                   | Sends an HTTP request to an HTTP server.<br/>                                                                                                        |
| [**SetAutoLogonPolicy**](iwinhttprequest-setautologonpolicy.md)       | Sets the current [Automatic Logon Policy](authentication-in-winhttp.md).<br/>                                                |
| [**SetClientCertificate**](iwinhttprequest-setclientcertificate.md)   | Selects a client certificate to send to a Secure Hypertext Transfer Protocol (HTTPS) server.<br/>                                                    |
| [**SetCredentials**](iwinhttprequest-setcredentials.md)               | Sets credentials to be used with an HTTP server either an origin or a proxy server.<br/>                                                             |
| [**SetProxy**](iwinhttprequest-setproxy.md)                           | Sets proxy server information.<br/>                                                                                                                  |
| [**SetRequestHeader**](iwinhttprequest-setrequestheader.md)           | Adds, changes, or deletes an HTTP request header.<br/>                                                                                               |
| [**SetTimeouts**](iwinhttprequest-settimeouts.md)                     | Specifies, in milliseconds, the individual time-out components of a send/receive operation.<br/>                                                     |
| [**WaitForResponse**](iwinhttprequest-waitforresponse.md)             | Specifies the wait time, in seconds, for an asynchronous [**Send**](iwinhttprequest-send.md) method to complete, with optional time-out value.<br/> |



 

### Properties

The **WinHttpRequest** object has these properties.



| Property                                                            | Access type           | Description                                                                     |
|:--------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------|
| [**Option**](iwinhttprequest-option.md)<br/>                 | Read/write<br/> | Sets or retrieves a WinHTTP option value.<br/>                            |
| [**ResponseBody**](iwinhttprequest-responsebody.md)<br/>     | Read-only<br/>  | Retrieves the response entity body as an array of unsigned bytes.<br/>    |
| [**ResponseStream**](iwinhttprequest-responsestream.md)<br/> | Read-only<br/>  | Retrieves the response entity body as an [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream).<br/> |
| [**ResponseText**](iwinhttprequest-responsetext.md)<br/>     | Read-only<br/>  | Retrieves the response entity body as text.<br/>                          |
| [**Status**](iwinhttprequest-status.md)<br/>                 | Read-only<br/>  | Retrieves the HTTP status code from the last response.<br/>               |
| [**StatusText**](iwinhttprequest-statustext.md)<br/>         | Read-only<br/>  | Retrieves HTTP status text.<br/>                                          |



 

## Remarks

The **WinHttpRequest** object uses the [**IErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ierrorinfo) interface to provide error data. A description and numerical error value can be obtained with the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object in Microsoft Visual Basic Scripting Edition (VBScript), and the [Error](https://msdn.microsoft.com/library/dww52sbt.aspx) object in Microsoft JScript. The lower 16 bits of an error number correspond to the values found in [**Error Messages**](error-messages.md).

> [!Note]  
> For Windows XP and Windows 2000, see [Run-Time Requirements](winhttp-start-page.md).

 

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

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

