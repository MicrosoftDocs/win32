---
title: CardReadFile function
description: Reads the contents of a file into a buffer.
ms.assetid: 508a57da-75d8-4636-aaba-21b585df9f25
keywords:
- CardReadFile function Security
topic_type:
- apiref
api_name:
- CardReadFile
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CardReadFile function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardReadFile** function, defined by a smart card module, reads the contents of a file into a buffer.

## Syntax


```C++
DWORD WINAPI CardReadFile(
  _In_    PCARD_DATA pCardData,
  _In_    LPSTR      pszDirectoryName,
  _In_    LPSTR      pszFileName,
  _In_    DWORD      dwFlags,
  _Out_   PBYTE      *ppbData,
  _Inout_ PDWORD     pcbData
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pszDirectoryName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the directory that contains the file to read.

</dd> <dt>

*pszFileName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the file to read.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> <dt>

*ppbData* \[out\]
</dt> <dd>

On output, this parameter contains the address of a pointer to a buffer that contains the contents of the file specified by the *pszFileName* parameter. Memory for this buffer is allocated by the smart card module and freed by the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md).

</dd> <dt>

*pcbData* \[in, out\]
</dt> <dd>

If the caller of this function specifies a value for this parameter, that value specifies the number of bytes to be read from the file. If the caller does not specify a value for this parameter on input, the entire file is read.

On output, this parameter contains a pointer to a value that specifies the size, in bytes, of the *ppbData* buffer.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                      | Description                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_FILE\_NOT\_FOUND**</dt> <dt>2148532260 (0x80100024)</dt> </dl> | The file specified by the *pszDirectoryName* and *pszFileName* parameters does not exist.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> </dl>

 

 





