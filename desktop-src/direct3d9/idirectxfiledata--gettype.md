---
Description: 'Retrieves the GUID of the object''s template. Deprecated.'
ms.assetid: 'bb4a4a32-a9e7-4caa-869d-24cfb310d8d1'
title: 'IDirectXFileData::GetType method'
---

# IDirectXFileData::GetType method

Retrieves the GUID of the object's template. Deprecated.

## Syntax


```C++
HRESULT GetType(
  [out, retval] const GUID **ppguid
);
```



## Parameters

<dl> <dt>

*ppguid* \[out, retval\]
</dt> <dd>

Type: **const [**GUID**](guid.md)\*\***

Address of a pointer to receive the GUID of the object's template.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be DXFILEERR\_BADVALUE.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileData](idirectxfiledata.md)
</dt> </dl>

 

 




