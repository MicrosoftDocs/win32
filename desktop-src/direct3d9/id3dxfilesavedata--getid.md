---
description: Retrieves the GUID of this ID3DXFileSaveData file data node.
ms.assetid: 79413eb4-4889-4148-b1a1-58a0b780403c
title: ID3DXFileSaveData::GetId method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileSaveData.GetId
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileSaveData::GetId method

Retrieves the GUID of this [**ID3DXFileSaveData**](id3dxfilesavedata.md) file data node.

## Syntax


```C++
HRESULT GetId(
  [out] 
            LPGUID pId
);
```



## Parameters

<dl> <dt>

*pId* \[out\]
</dt> <dd>

Type: **LPGUID**

Pointer to a GUID to receive the ID of this file data node. If the object has no ID, the returned parameter value will be GUID\_NULL.

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

[ID3DXFileSaveData](id3dxfilesavedata.md)
</dt> </dl>

 

 




