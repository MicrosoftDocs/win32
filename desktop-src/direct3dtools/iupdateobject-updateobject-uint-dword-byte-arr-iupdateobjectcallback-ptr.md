---
Description: A request to update the initial state of an object; for example, a texture or shader.
MS-HAID: vspixengine.IUpdateObject\_UpdateObject\_UINT\_DWORD\_BYTE\_arr\_IUpdateObjectCallback\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IUpdateObject::UpdateObject method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iupdateobject_updateobject_uint_dword_byte_arr_iupdateobjectcallback_ptr"></span>IUpdateObject::UpdateObject method

A request to update the initial state of an object; for example, a texture or shader.

## Syntax


```C++
);
```

## Parameters

*objectAddress*   
The ID of the object to be updated.

*size*   
The size of the update payload in bytes.

*count1\_buffer*   
The update payload.

*pCallback*   
The address of a function used to notify the host that the object was updated.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IUpdateObject**](https://msdn.microsoft.com/library/windows/desktop/mt432822)

 

 



