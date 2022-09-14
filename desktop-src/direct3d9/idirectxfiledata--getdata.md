---
description: Retrieves the data for one of the object's members or the data for all members. Deprecated.
ms.assetid: 2a227705-371e-41f1-af5d-20e652cd07f6
title: IDirectXFileData::GetData method (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileData.GetData
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
---

# IDirectXFileData::GetData method

Retrieves the data for one of the object's members or the data for all members. Deprecated.

## Syntax


```C++
HRESULT GetData(
  [in]  LPCSTR szMember,
  [out] DWORD  *pcbSize,
  [out] void   **ppvData
);
```



## Parameters

<dl> <dt>

*szMember* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to the name of the member for which to retrieve data. Specify **NULL** to retrieve all required members' data.

</dd> <dt>

*pcbSize* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Pointer to receive the ppvData buffer size, in bytes.

</dd> <dt>

*ppvData* \[out\]
</dt> <dd>

Type: **void\*\***

Address of a pointer to the buffer to receive the data associated with szMember. If szMember is **NULL**, ppvData is set to point to a buffer containing all required members' data in a contiguous block of memory.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values: DXFILEERR\_BADARRAYSIZE, DXFILEERR\_BADDataReference, DXFILEERR\_BADVALUE.

## Remarks

This method retrieves the data for required members of a data object but no data for optional (child) members. Use [**IDirectXFileData::GetNextObject**](idirectxfiledata--getnextobject.md) to retrieve child objects.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileData](idirectxfiledata.md)
</dt> <dt>

[**IDirectXFileData::GetNextObject**](idirectxfiledata--getnextobject.md)
</dt> </dl>

 

 
