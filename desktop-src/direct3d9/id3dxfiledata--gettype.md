---
Description: Retrieves the template ID in this file data object.
ms.assetid: abc53dda-d3ed-461b-b3d8-a64845c44c81
title: ID3DXFileDataGetType method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




