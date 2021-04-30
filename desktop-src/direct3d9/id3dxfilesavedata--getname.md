---
description: Retrieves the name of this ID3DXFileSaveData file data node.
ms.assetid: ea697d23-42e7-4661-b605-3654f6a31055
title: ID3DXFileSaveData::GetName method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileSaveData.GetName
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFileSaveData::GetName method

Retrieves the name of this [**ID3DXFileSaveData**](id3dxfilesavedata.md) file data node.

## Syntax


```C++
HRESULT GetName(
  [in]      LPSTR  szName,
  [in, out] SIZE_T *puiSize
);
```



## Parameters

<dl> <dt>

*szName* \[in\]
</dt> <dd>

Type: **[**LPSTR**](../winprog/windows-data-types.md)**

Address of a pointer to receive the name of this file data node. If this parameter is **NULL**, then *puiSize* will return the size of the string. If szName points to valid memory, the name of this file data node will be copied into szName up to the number of characters given by *puiSize* .

</dd> <dt>

*puiSize* \[in, out\]
</dt> <dd>

Type: **[**SIZE\_T**](../winprog/windows-data-types.md)\***

Pointer to the size of the string that represents the name of this file data node. This parameter can be **NULL** if szName provides a reference to the name. This parameter will return the size of the string if szName is **NULL**.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DXFERR\_BADVALUE.

## Remarks

For this method to succeed, either *szName* or *puiSize* must be non-**NULL**.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileSaveData](id3dxfilesavedata.md)
</dt> </dl>

 

 
