---
description: Creates a binary object and adds it as a child object. Deprecated.
ms.assetid: 6164951d-dd87-4318-ac08-b97c22f58d45
title: IDirectXFileData::AddBinaryObject method (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileData.AddBinaryObject
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
---

# IDirectXFileData::AddBinaryObject method

Creates a binary object and adds it as a child object. Deprecated.

## Syntax


```C++
HRESULT AddBinaryObject(
  [in]       LPCSTR szName,
  [in] const GUID   *pguid,
  [in]       LPCSTR szMimeType,
  [in]       LPVOID pvData,
  [in]       DWORD  cbSize
);
```



## Parameters

<dl> <dt>

*szName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to the name of the object. Specify **NULL** if the object does not need a name.

</dd> <dt>

*pguid* \[in\]
</dt> <dd>

Type: **const [**GUID**](guid.md)\***

Pointer to the GUID representing the object. Specify **NULL** if the object does not need a GUID.

</dd> <dt>

*szMimeType* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to the object's MIME type.

</dd> <dt>

*pvData* \[in\]
</dt> <dd>

Type: **[**LPVOID**](../winprog/windows-data-types.md)**

Pointer to the object's data.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Size of the buffer pointed to by pvData, in bytes.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values.DXFILEERR\_BADALLOC DXFILEERR\_BADVALUE

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileData](idirectxfiledata.md)
</dt> <dt>

[**IDirectXFileBinary::GetMimeType**](idirectxfilebinary--getmimetype.md)
</dt> </dl>

 

 
