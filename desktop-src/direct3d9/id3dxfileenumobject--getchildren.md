---
Description: Retrieves the number of child objects in this file data object.
ms.assetid: 4409819f-a346-40b1-8e12-86e8128ece47
title: ID3DXFileEnumObjectGetChildren method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**SIZE\_T**](winprog.windows_data_types)\***

Address of a pointer to receive the number of child objects in this file data object.

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

[ID3DXFileEnumObject](id3dxfileenumobject.md)
</dt> </dl>

 

 




