---
description: Retrieves the template ID in this file data object.
ms.assetid: abc53dda-d3ed-461b-b3d8-a64845c44c81
title: ID3DXFileData::GetType method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileData.GetType
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileData::GetType method

Retrieves the template ID in this file data object.

## Syntax


```C++
HRESULT GetType(
  [in] const GUID *pType
);
```



## Parameters

<dl> <dt>

*pType* \[in\]
</dt> <dd>

Type: **const [**GUID**](guid.md)\***

Pointer to the GUID representing the template in this file data object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DXFERR\_BADVALUE.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileData](id3dxfiledata.md)
</dt> </dl>

 

 




