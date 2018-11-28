---
Description: Gets information about which columns (types of object data) are supported by the object table.
MS-HAID: vspixengine.IObjectTableCallback\_GetSupportedColumns\_DWORD\_ObjectTableColumnID\_arr\_BSTR\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IObjectTableCallback::GetSupportedColumns method
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 148AB80D-9833-4B57-9F34-CEDFFF8E905A
api_name: 
 - IObjectTableCallback.GetSupportedColumns
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.iobjecttablecallback_getsupportedcolumns_dword_objecttablecolumnid_arr_bstr_arr"></span>IObjectTableCallback::GetSupportedColumns method

Gets information about which columns (types of object data) are supported by the object table.

## Syntax


```C++
);
```

## Parameters

*numColumns*   
The number of columns supported by the object table.

*count0\_pIDs*   
The IDs of each column supported by the object table.

*count0\_pBstrNames*   
The names of each column, as a COM string, supported by the object table.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IObjectTableCallback**](https://msdn.microsoft.com/library/windows/desktop/mt422696)

 

 



