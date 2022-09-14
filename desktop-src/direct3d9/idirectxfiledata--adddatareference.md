---
description: Creates and adds a data reference object as a child object. Deprecated.
ms.assetid: 71a770a2-1502-4b93-b368-990c3318bd33
title: IDirectXFileData::AddDataReference method (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileData.AddDataReference
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
---

# IDirectXFileData::AddDataReference method

Creates and adds a data reference object as a child object. Deprecated.

## Syntax


```C++
HRESULT AddDataReference(
  [in]       LPCSTR szRef,
  [in] const GUID   *pguidRef
);
```



## Parameters

<dl> <dt>

*szRef* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to the name of the referenced data object. This parameter can be **NULL** if pguidRef provides a reference to the GUID.

</dd> <dt>

*pguidRef* \[in\]
</dt> <dd>

Type: **const [**GUID**](guid.md)\***

Pointer to the GUID representing the data. This parameter can be **NULL** if szRef provides a reference to the name.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values.DXFILEERR\_BADALLOC DXFILEERR\_BADVALUE

## Remarks

For this method to succeed, either the szRef or pguidRef parameter must be non-**NULL**.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileData](idirectxfiledata.md)
</dt> </dl>

 

 
