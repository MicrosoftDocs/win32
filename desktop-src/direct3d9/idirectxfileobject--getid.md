---
Description: Retrieves a pointer to the GUID that identifies a DirectX file object. Deprecated.
ms.assetid: 74c7a1d9-85e4-43eb-bcd8-1f3ddd713e9f
title: IDirectXFileObject::GetId method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IDirectXFileObject::GetId method

Retrieves a pointer to the GUID that identifies a DirectX file object. Deprecated.

## Syntax


```C++
HRESULT GetId(
  [out, retval] 
            LPGUID pGuid
);
```



## Parameters

<dl> <dt>

*pGuid* \[out, retval\]
</dt> <dd>

Type: **LPGUID**

Pointer to a GUID to receive the object's ID. The function will set the GUID to a **NULL** GUID if the object does not have an ID.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be DXFILEERR\_BADVALUE.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileObject](idirectxfileobject.md)
</dt> </dl>

 

 




