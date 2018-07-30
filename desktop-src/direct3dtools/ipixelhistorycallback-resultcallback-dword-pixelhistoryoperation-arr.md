---
Description: A callback that notifies the host of pixel history request results.
MS-HAID: vspixengine.IPixelHistoryCallback\_ResultCallback\_DWORD\_PixelHistoryOperation\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixelHistoryCallback::ResultCallback method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.ipixelhistorycallback_resultcallback_dword_pixelhistoryoperation_arr"></span>IPixelHistoryCallback::ResultCallback method

A callback that notifies the host of pixel history request results.

## Syntax


```C++
);
```

## Parameters

*count*   
The number of results.

*count0\_pixelHistoryOperation*   
The results.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixelHistoryCallback**](https://msdn.microsoft.com/library/windows/desktop/mt432735)

 

 



