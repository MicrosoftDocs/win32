---
description: Retrieves the Multipurpose Internet Mail Extensions (MIME) type for the binary data. Deprecated.
ms.assetid: 57c42ace-4313-40d8-9992-eaf12edf3a30
title: IDirectXFileBinary::GetMimeType method (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileBinary.GetMimeType
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
---

# IDirectXFileBinary::GetMimeType method

Retrieves the Multipurpose Internet Mail Extensions (MIME) type for the binary data. Deprecated.

## Syntax


```C++
HRESULT GetMimeType(
  [out] LPCSTR *pszMimeType
);
```



## Parameters

<dl> <dt>

*pszMimeType* \[out\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)\***

Address of a pointer to receive the MIME type string.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be DXFILEERR\_BADVALUE.

## Remarks

When there is no MIME type specified in a DirectX file for a binary object, the function will set pszMimeType to **NULL**.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileBinary](idirectxfilebinary.md)
</dt> </dl>

 

 
