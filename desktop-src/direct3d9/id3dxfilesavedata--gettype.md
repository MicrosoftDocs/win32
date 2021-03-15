---
description: Retrieves the template ID of this file data node.
ms.assetid: ff0662da-b4f8-4ed2-81d4-6771e91da262
title: ID3DXFileSaveData::GetType method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileSaveData.GetType
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileSaveData::GetType method

Retrieves the template ID of this file data node.

## Syntax


```C++
HRESULT GetType(
  [in] GUID *type
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

Type: **[**GUID**](guid.md)\***

Pointer to the GUID representing the template in this file data node.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DXFERR\_BADOBJECT, D3DXFERR\_BADVALUE.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileSaveData](id3dxfilesavedata.md)
</dt> </dl>

 

 




