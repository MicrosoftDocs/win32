---
description: Retrieves a pointer to this ID3DXFileSaveObject file data node.
ms.assetid: 092d1c6f-0a53-4b8e-84ec-bc76f3f647ac
title: ID3DXFileSaveData::GetSave method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileSaveData.GetSave
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileSaveData::GetSave method

Retrieves a pointer to this [**ID3DXFileSaveObject**](id3dxfilesaveobject.md) file data node.

## Syntax


```C++
HRESULT GetSave(
  [out] ID3DXFileSaveObject **ppObj
);
```



## Parameters

<dl> <dt>

*ppObj* \[out\]
</dt> <dd>

Type: **[**ID3DXFileSaveObject**](id3dxfilesaveobject.md)\*\***

Address of a pointer to an [**ID3DXFileSaveObject**](id3dxfilesaveobject.md) interface representing this file data node.

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

 

 




