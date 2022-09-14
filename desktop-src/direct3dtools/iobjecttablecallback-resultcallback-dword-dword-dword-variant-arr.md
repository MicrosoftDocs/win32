---
description: A callback function used to notify the host of object table information.
MS-HAID: vspixengine.IObjectTableCallback\_ResultCallback\_DWORD\_DWORD\_DWORD\_VARIANT\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IObjectTableCallback::ResultCallback method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: AAD02864-AE08-406B-A0E9-2228DC9A73E7
api_name: 
 - IObjectTableCallback.ResultCallback
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iobjecttablecallback_resultcallback_dword_dword_dword_variant_arr"></span>IObjectTableCallback::ResultCallback method

A callback function used to notify the host of object table information.

## Syntax


```C++
HRESULT ResultCallback(
   DWORD      numElements,
   DWORD      numRows,
   DWORD      numColumns,
   VARIANT [] count0_pRowData
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

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IObjectTableCallback**](/windows/desktop/direct3dtools/iobjecttablecallback)

 

 
