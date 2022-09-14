---
description: Updates the initial state of an object; for example, a texture or shader.
MS-HAID: vspixengine.IPixEngine4\_UpdateObject\_UINT\_DWORD\_BYTE\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine4::UpdateObject method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 90B1DE4F-7DF5-44C9-9A57-1BFB6825EB58
api_name: 
 - IPixEngine4.UpdateObject
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixengine4_updateobject_uint_dword_byte_arr"></span>IPixEngine4::UpdateObject method

Updates the initial state of an object; for example, a texture or shader.

## Syntax


```C++
HRESULT UpdateObject(
   UINT    objectAddress,
   DWORD   size,
   BYTE [] count1_buffer
);
```

## Parameters

*objectAddress*   
The ID of the object to be updated.

*size*   
The size of the update payload in bytes.

*count1\_buffer*   
The update payload.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixEngine4**](/windows/desktop/direct3dtools/ipixengine4)

 

 
