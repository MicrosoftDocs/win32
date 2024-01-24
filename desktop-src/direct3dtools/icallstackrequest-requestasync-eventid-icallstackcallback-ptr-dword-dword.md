---
description: An asynchronous request to get the call stack RVAs (relative virtual addresses) of the specified event.
MS-HAID: vspixengine.ICallStackRequest\_RequestAsync\_EventID\_ICallStackCallback\_ptr\_DWORD\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ICallStackRequest::RequestAsync method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 1951716F-5382-41EE-90BB-A9053DB38A78
api_name: 
 - ICallStackRequest.RequestAsync
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.icallstackrequest_requestasync_eventid_icallstackcallback_ptr_dword_dword"></span>ICallStackRequest::RequestAsync method

An asynchronous request to get the call stack RVAs (relative virtual addresses) of the specified event.

## Syntax


```C++
HRESULT RequestAsync(
   EventID              eventID,
   ICallStackCallback * requestCallback,
   DWORD                requestCookie,
   DWORD                progressIntervalMsecs
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

[**ICallStackRequest**](/windows/desktop/direct3dtools/icallstackrequest)

 

 
