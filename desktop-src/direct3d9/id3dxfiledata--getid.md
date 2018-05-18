---
Description: 'Retrieves the GUID of this file data object.'
ms.assetid: '79bf56b5-5900-4427-8092-3a1df86f8a57'
title: 'ID3DXFileData::GetId method'
---

# ID3DXFileData::GetId method

Retrieves the GUID of this file data object.

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

Pointer to a GUID to receive the ID of this file data object. If the file data object has no ID, the returned parameter value will be GUID\_NULL.

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

 

 




