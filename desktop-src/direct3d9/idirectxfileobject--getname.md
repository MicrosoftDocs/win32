---
description: Retrieves a pointer to a DirectX file object's name. Deprecated.
ms.assetid: feb3faa2-22b9-47ed-8a38-33092821d484
title: IDirectXFileObject::GetName method (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileObject.GetName
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
---

# IDirectXFileObject::GetName method

Retrieves a pointer to a DirectX file object's name. Deprecated.

## Syntax


```C++
HRESULT GetName(
  [out]     LPSTR   pstrNameBuf,
  [in, out] LPDWORD pdwBufLen
);
```



## Parameters

<dl> <dt>

*pstrNameBuf* \[out\]
</dt> <dd>

Type: **[**LPSTR**](../winprog/windows-data-types.md)**

Pointer to the buffer in which the DirectX file object's name will be copied. Set to **NULL** if only the buffer length is needed.

</dd> <dt>

*pdwBufLen* \[in, out\]
</dt> <dd>

Type: **[**LPDWORD**](../winprog/windows-data-types.md)**

Pointer to a DWORD specifying the length of the buffer pointed to by pstrNameBuf. The pdwBufLen parameter value will be modified to the buffer length needed to hold the object's name even if pstrNameBuf is **NULL**. In either case, the function will return DXFILEERR\_BADVALUE if the original value of pdwBufLen is not as large as or larger than the length needed to hold the object's name.

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

[IDirectXFileObject](idirectxfileobject.md)
</dt> </dl>

 

 
