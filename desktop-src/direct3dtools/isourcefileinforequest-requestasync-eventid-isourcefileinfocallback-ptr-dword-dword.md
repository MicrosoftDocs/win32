---
description: An asynchronous request to get the source files associated with the callstack of an event.
MS-HAID: vspixengine.ISourceFileInfoRequest\_RequestAsync\_EventID\_ISourceFileInfoCallback\_ptr\_DWORD\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ISourceFileInfoRequest::RequestAsync method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 257361ED-7400-4320-8433-59A9A07E69E4
api_name: 
 - ISourceFileInfoRequest.RequestAsync
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.isourcefileinforequest_requestasync_eventid_isourcefileinfocallback_ptr_dword_dword"></span>ISourceFileInfoRequest::RequestAsync method

An asynchronous request to get the source files associated with the callstack of an event.

## Syntax


```C++
HRESULT RequestAsync(
   EventID                   eventID,
   ISourceFileInfoCallback * requestCallback,
   DWORD                     requestCookie,
   DWORD                     progressIntervalMsecs
);
```

## Parameters

*eventID*   
The specified event.

*requestCallback*   
The address of callback used to notify the host of results.

*requestCookie*   
A cookie that uniquely identifies the request, and can be used to signal for it to be cancelled.

*progressIntervalMsecs*   
Not used.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**ISourceFileInfoRequest**](/windows/desktop/direct3dtools/isourcefileinforequest)

 

 
