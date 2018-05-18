---
Description: 'Retrieves the template ID of this file data node.'
ms.assetid: 'ff0662da-b4f8-4ed2-81d4-6771e91da262'
title: 'ID3DXFileSaveData::GetType method'
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

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DXFERR\_BADOBJECT, D3DXFERR\_BADVALUE.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileSaveData](id3dxfilesavedata.md)
</dt> </dl>

 

 




