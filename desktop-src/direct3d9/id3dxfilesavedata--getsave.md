---
Description: Retrieves a pointer to this ID3DXFileSaveObject file data node.
ms.assetid: 092d1c6f-0a53-4b8e-84ec-bc76f3f647ac
title: ID3DXFileSaveDataGetSave method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DXFERR\_BADVALUE.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileSaveData](id3dxfilesavedata.md)
</dt> </dl>

 

 




