---
description: Retrieves the data object that has the specified GUID. Deprecated.
ms.assetid: dd079b5c-18e1-4252-aabd-498c24910a08
title: IDirectXFileEnumObject::GetDataObjectById method (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileEnumObject.GetDataObjectById
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
---

# IDirectXFileEnumObject::GetDataObjectById method

Retrieves the data object that has the specified GUID. Deprecated.

## Syntax


```C++
HRESULT GetDataObjectById(
  [in]  REFGUID           rguid,
  [out] LPDIRECTXFILEDATA *ppDataObj
);
```



## Parameters

<dl> <dt>

*rguid* \[in\]
</dt> <dd>

Type: **[REFGUID](/openspecs/windows_protocols/ms-oaut/6e7d7108-c213-40bc-8294-ac13fe68fd50)**

Reference to the requested GUID.

</dd> <dt>

*ppDataObj* \[out\]
</dt> <dd>

Type: **[**LPDIRECTXFILEDATA**](idirectxfiledata.md)\***

Address of a pointer to an [**IDirectXFileData**](idirectxfiledata.md) interface, representing the returned file data object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values: DXFILEERR\_BADVALUE, DXFILEERR\_NOTFOUND.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileEnumObject](idirectxfileenumobject.md)
</dt> </dl>

 

 
