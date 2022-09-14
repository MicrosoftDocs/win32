---
description: Provides events for Microsoft Windows HTTP Services (WinHTTP).
ms.assetid: 0721d7f9-2e84-41a9-be52-89c8d638eb90
title: IWinHttpRequestEvents interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWinHttpRequestEvents
api_type: 
- COM
api_location: 
- HttpRequest.idl
---

# IWinHttpRequestEvents interface

The **IWinHttpRequestEvents** interface provides events for [Microsoft Windows HTTP Services (WinHTTP)](about-winhttp.md). It uses only event methods.

## Members

The **IWinHttpRequestEvents** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWinHttpRequestEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWinHttpRequestEvents** interface has these methods.



| Method                                                                           | Description                                                          |
|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------|
| [**OnError**](iwinhttprequestevents-onerror.md)                                 | Occurs when there is a run-time error in the application.<br/> |
| [**OnResponseDataAvailable**](iwinhttprequestevents-onresponsedataavailable.md) | Occurs when data is available from the response.<br/>          |
| [**OnResponseFinished**](iwinhttprequestevents-onresponsefinished.md)           | Occurs when the response data is complete.<br/>                |
| [**OnResponseStart**](iwinhttprequestevents-onresponsestart.md)                 | Occurs when the response data starts to be received.<br/>      |



 

## Remarks

The following procedure describes how to register for notifications.

1.  Get an [IConnectionPointContainer](/windows/win32/api/ocidl/nn-ocidl-iconnectionpointcontainer) interface by calling **QueryInterface** on an [**IWinHttpRequest**](iwinhttprequest-interface.md) object.
2.  Call [FindConnectionPoint](/windows/win32/api/ocidl/nf-ocidl-iconnectionpointcontainer-findconnectionpoint) on the returned interface and pass **IID\_IWinHttpRequestEvents** to *riid*.
3.  Call [Advise](/windows/win32/api/ocidl/nf-ocidl-iconnectionpoint-advise) on the returned connection point and pass a pointer to an **IUnknown** interface on an object that implements **IWinHttpRequestEvents** to *pUnk*.

Notifications can be terminated by calling [Unadvise](/windows/win32/api/ocidl/nf-ocidl-iconnectionpoint-unadvise) on the connection point returned in step 2.

To view some code that registers for COM notifications, see the Client section of the [COM Connection Points](/archive/msdn-magazine/2007/september/clr-inside-out-com-connection-points) article.

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

[**IWinHttpRequest**](iwinhttprequest-interface.md)
</dt> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

