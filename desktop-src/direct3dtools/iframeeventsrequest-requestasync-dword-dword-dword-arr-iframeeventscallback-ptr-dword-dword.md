---
Description: An asynchronous request to get specified information about a single specified frame.
MS-HAID: vspixengine.IFrameEventsRequest\_RequestAsync\_DWORD\_DWORD\_DWORD\_arr\_IFrameEventsCallback\_ptr\_DWORD\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IFrameEventsRequest::RequestAsync method
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iframeeventsrequest_requestasync_dword_dword_dword_arr_iframeeventscallback_ptr_dword_dword"></span>IFrameEventsRequest::RequestAsync method

An asynchronous request to get specified information about a single specified frame.

## Syntax


```C++
);
```

## Parameters

*frameNumber*   
The specified frame.

*numColumns*   
The specified columns (fields).

*count1\_columns*   
The address of callback used to notify the host of results.

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

[**IFrameEventsRequest**](https://msdn.microsoft.com/library/windows/desktop/mt422675)

 

 



