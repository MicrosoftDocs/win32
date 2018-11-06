---
Description: A callback function used to notify the host of graphics log summary information.
MS-HAID: vspixengine.ISummaryCallback\_ResultCallback\_DWORD\_SummaryItem\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ISummaryCallback::ResultCallback method
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.isummarycallback_resultcallback_dword_summaryitem_arr"></span>ISummaryCallback::ResultCallback method

A callback function used to notify the host of graphics log summary information.

## Syntax


```C++
);
```

## Parameters

*count*   
The number of summary information items returned.

*count0\_summaryItem*   
The summary information items (key-value pairs).

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**ISummaryCallback**](https://msdn.microsoft.com/library/windows/desktop/mt432809)

 

 



