---
Description: Retrieves the enumeration object in this file data object.
ms.assetid: 383560e2-1888-4e37-9883-2ddbcb101cf6
title: ID3DXFileData::GetEnum method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXFileData::GetEnum method

Retrieves the enumeration object in this file data object.

## Syntax


```C++
HRESULT GetEnum(
  [in] ID3DXFileEnumObject **ppObj
);
```



## Parameters

<dl> <dt>

*ppObj* \[in\]
</dt> <dd>

Type: **[**ID3DXFileEnumObject**](id3dxfileenumobject.md)\*\***

Address of a pointer to receive the enumeration object in this file data object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DXFERR\_BADVALUE.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileData](id3dxfiledata.md)
</dt> </dl>

 

 




