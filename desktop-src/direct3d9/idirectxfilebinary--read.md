---
Description: Reads the binary data. Deprecated.
ms.assetid: 530552c5-bf05-4e86-836d-d25161832c6d
title: IDirectXFileBinary::Read method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileBinary.Read
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
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

Type: **[**LPVOID**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Pointer to the buffer that receives the data that has been read.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Size of the buffer pointed to by pvData, in bytes.

</dd> <dt>

*pcbRead* \[out\]
</dt> <dd>

Type: **[**LPDWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Pointer to the number of bytes actually read.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

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

 

 




