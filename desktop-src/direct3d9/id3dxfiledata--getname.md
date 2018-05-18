---
Description: 'Retrieves the name of this file data object.'
ms.assetid: '182529cb-144c-4ed8-94bf-6688598e9ea7'
title: 'ID3DXFileData::GetName method'
---

# ID3DXFileData::GetName method

Retrieves the name of this file data object.

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

Type: **[**LPSTR**](winprog.windows_data_types)**

Address of a pointer to receive the name of this file data object. If this parameter is **NULL**, then puiSize will return the size of the string. If szName points to valid memory, the name of this file data object will be copied into szName up to the number of characters given by puiSize.

</dd> <dt>

*puiSize* \[in, out\]
</dt> <dd>

Type: **[**SIZE\_T**](winprog.windows_data_types)\***

Pointer to the size of the string that represents the name of this file data object. This parameter can be **NULL** if szName provides a reference to the name. This parameter will return the size of the string if szName is **NULL**.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DXFERR\_BADVALUE.

## Remarks

For this method to succeed, either szName or *puiSize* must be non-**NULL**.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFileData](id3dxfiledata.md)
</dt> </dl>

 

 




