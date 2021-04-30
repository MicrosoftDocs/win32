---
description: Retrieves the number of child objects in this file data object.
ms.assetid: 4409819f-a346-40b1-8e12-86e8128ece47
title: ID3DXFileEnumObject::GetChildren method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileEnumObject.GetChildren
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileEnumObject::GetChildren method

Retrieves the number of child objects in this file data object.

## Syntax


```C++
HRESULT GetChildren(
  [in] SIZE_T *puiChildren
);
```



## Parameters

<dl> <dt>

*puiChildren* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](../winprog/windows-data-types.md)\***

Address of a pointer to receive the number of child objects in this file data object.

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

[ID3DXFileEnumObject](id3dxfileenumobject.md)
</dt> </dl>

 

 
