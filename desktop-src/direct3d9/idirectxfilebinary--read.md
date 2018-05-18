---
Description: 'Reads the binary data. Deprecated.'
ms.assetid: '530552c5-bf05-4e86-836d-d25161832c6d'
title: 'IDirectXFileBinary::Read method'
---

# IDirectXFileBinary::Read method

Reads the binary data. Deprecated.

## Syntax


```C++
HRESULT Read(
  [out] LPVOID  pvData,
  [in]  DWORD   cbSize,
  [out] LPDWORD pcbRead
);
```



## Parameters

<dl> <dt>

*pvData* \[out\]
</dt> <dd>

Type: **[**LPVOID**](winprog.windows_data_types)**

Pointer to the buffer that receives the data that has been read.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Size of the buffer pointed to by pvData, in bytes.

</dd> <dt>

*pcbRead* \[out\]
</dt> <dd>

Type: **[**LPDWORD**](winprog.windows_data_types)**

Pointer to the number of bytes actually read.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values: DXFILEERR\_BADVALUE, DXFILEERR\_NOMOREDATA.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileBinary](idirectxfilebinary.md)
</dt> </dl>

 

 




