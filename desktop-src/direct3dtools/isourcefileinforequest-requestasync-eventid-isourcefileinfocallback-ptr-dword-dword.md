---
Description: An asynchronous request to get the source files associated with the callstack of an event.
MS-HAID: vspixengine.ISourceFileInfoRequest\_RequestAsync\_EventID\_ISourceFileInfoCallback\_ptr\_DWORD\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ISourceFileInfoRequest::RequestAsync method
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.isourcefileinforequest_requestasync_eventid_isourcefileinfocallback_ptr_dword_dword"></span>ISourceFileInfoRequest::RequestAsync method

An asynchronous request to get the source files associated with the callstack of an event.

## Syntax


```C++
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

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**ISourceFileInfoRequest**](https://msdn.microsoft.com/library/windows/desktop/mt432804)

 

 



