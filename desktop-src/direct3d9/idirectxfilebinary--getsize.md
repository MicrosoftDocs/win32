---
Description: Retrieves the size of the binary data. Deprecated.
ms.assetid: 99a74043-ce87-4545-961f-dade54e77735
title: IDirectXFileBinaryGetSize method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDirectXFileBinary::GetSize method

Retrieves the size of the binary data. Deprecated.

## Syntax


```C++
HRESULT GetSize(
  [out] DWORD *pcbSize
);
```



## Parameters

<dl> <dt>

*pcbSize* \[out\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)\***

Pointer to the returned size of the binary data, in bytes.

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

[IDirectXFileBinary](idirectxfilebinary.md)
</dt> </dl>

 

 




