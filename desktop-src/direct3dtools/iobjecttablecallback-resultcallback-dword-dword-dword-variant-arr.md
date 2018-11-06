---
Description: A callback function used to notify the host of object table information.
MS-HAID: vspixengine.IObjectTableCallback\_ResultCallback\_DWORD\_DWORD\_DWORD\_VARIANT\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IObjectTableCallback::ResultCallback method
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iobjecttablecallback_resultcallback_dword_dword_dword_variant_arr"></span>IObjectTableCallback::ResultCallback method

A callback function used to notify the host of object table information.

## Syntax


```C++
);
```

## Parameters

*numElements*   
The total number of fields in all columns of all objects.

*numRows*   
The number of objects being transferred.

*numColumns*   
The number of columns (fields) of information being transferred for each object.

*count0\_pRowData*   
Information about the objects; one item for each field of each object.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IObjectTableCallback**](https://msdn.microsoft.com/library/windows/desktop/mt422696)

 

 



