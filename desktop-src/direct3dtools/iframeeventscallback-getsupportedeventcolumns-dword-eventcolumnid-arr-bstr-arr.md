---
Description: Gets information about which columns (types of event data) are supported by the event list.
MS-HAID: vspixengine.IFrameEventsCallback\_GetSupportedEventColumns\_DWORD\_EventColumnID\_arr\_BSTR\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IFrameEventsCallback::GetSupportedEventColumns method
ms.topic: article
ms.date: 05/31/2018
ms.assetid: F1BFF189-A22C-4058-A427-74653998DD27
api_name: 
 - IFrameEventsCallback.GetSupportedEventColumns
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iframeeventscallback_getsupportedeventcolumns_dword_eventcolumnid_arr_bstr_arr"></span>IFrameEventsCallback::GetSupportedEventColumns method

Gets information about which columns (types of event data) are supported by the event list.

## Syntax


```C++
);
```

## Parameters

*numColumns*   
The number of columns supported by

*count0\_pIDs*   
The IDs of each column supported by the event list.

*count0\_pBstrNames*   
The names of each column, as a COM string, supported by the event list.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IFrameEventsCallback**](https://msdn.microsoft.com/library/windows/desktop/mt422672)

 

 



