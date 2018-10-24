---
Description: A callback function used to notify the host of which frames were captured.
MS-HAID: vspixengine.IFrameListCallback\_ResultCallback\_DWORD\_DWORD\_arr\_DWORD\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IFrameListCallback::ResultCallback method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iframelistcallback_resultcallback_dword_dword_arr_dword_arr"></span>IFrameListCallback::ResultCallback method

A callback function used to notify the host of which frames were captured.

## Syntax


```C++
);
```

## Parameters

*numFrames*   
The number of frames captured.

*count0\_frameNumbers*   
The frame numbers of the captured frames.

*count0\_frameEventIDs*   
The final event associated with each frame.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IFrameListCallback**](https://msdn.microsoft.com/library/windows/desktop/mt422678)

 

 



