---
Description: Requests a list of pixel history results in the specified pixel, render tartget /UAV, and frame.
MS-HAID: vspixengine.IPixelHistoryRequest\_RequestAsync\_DWORD\_Point2D\_DWORD\_IPixelHistoryCallback\_ptr\_DWORD\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixelHistoryRequest::RequestAsync method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixelhistoryrequest_requestasync_dword_point2d_dword_ipixelhistorycallback_ptr_dword_dword"></span>IPixelHistoryRequest::RequestAsync method

Requests a list of pixel history results in the specified pixel, render tartget /UAV, and frame.

## Syntax


```C++
);
```

## Parameters

*frameNumber*   
The specified frame.

*pixel*   
The specified pixel.

*renderTargetPtr*   
The specified render target.

*requestCallback*   
The address of a callback used to notifify the host of results.

*requestCookie*   
A cookie that uniquely identifies the request, and can be used to signal for it to be cancelled.

*progressIntervalMsecs*   
Not used.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixelHistoryRequest**](https://msdn.microsoft.com/library/windows/desktop/mt432740)

 

 



