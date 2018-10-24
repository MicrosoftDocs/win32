---
Description: A callback function used to notify the host of information about events in the event list.
MS-HAID: vspixengine.IFrameEventsCallback\_ResultCallback\_DWORD\_DWORD\_DWORD\_DWORD\_VARIANT\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IFrameEventsCallback::ResultCallback method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iframeeventscallback_resultcallback_dword_dword_dword_dword_variant_arr"></span>IFrameEventsCallback::ResultCallback method

A callback function used to notify the host of information about events in the event list.

## Syntax


```C++
);
```

## Parameters

*frameNumber*   
The frame number associated with the events.

*numElements*   
The total number of fields in all columns of all events.

*numRows*   
The number of events in the result.

*numColumns*   
The number of columns (fields) in each row.

*count1\_pRowData*   
Information about the events; one item for each field of each event.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IFrameEventsCallback**](https://msdn.microsoft.com/library/windows/desktop/mt422672)

 

 



