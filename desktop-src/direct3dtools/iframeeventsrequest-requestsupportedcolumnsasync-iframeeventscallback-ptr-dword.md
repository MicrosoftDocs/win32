---
Description: An asynchronous request to get information about what columns (fields) this frame events request type supports.
MS-HAID: vspixengine.IFrameEventsRequest\_RequestSupportedColumnsAsync\_IFrameEventsCallback\_ptr\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IFrameEventsRequest::RequestSupportedColumnsAsync method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iframeeventsrequest_requestsupportedcolumnsasync_iframeeventscallback_ptr_dword"></span>IFrameEventsRequest::RequestSupportedColumnsAsync method

An asynchronous request to get information about what columns (fields) this frame events request type supports.

## Syntax


```C++
);
```

## Parameters

*requestCallback*   
The address of callback used to notify the host of results.

*progressIntervalMsecs*   
Not used.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IFrameEventsRequest**](https://msdn.microsoft.com/library/windows/desktop/mt422675)

 

 



