---
title: CardWriteFile function
description: Writes data in a buffer to a file on a smart card. This function overwrites any data currently in the file.
ms.assetid: 6e3cabc0-b55b-436a-ac2e-b96354e5666a
keywords:
- CardWriteFile function Security
topic_type:
- apiref
api_name:
- CardWriteFile
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

# CardWriteFile function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardWriteFile** function, defined by a smart card module, writes data in a buffer to a file on a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly). This function overwrites any data currently in the file.

## Syntax


```C++
DWORD WINAPI CardWriteFile(
  _In_ PCARD_DATA pCardData,
  _In_ LPSTR      pszDirectoryName,
  _In_ LPSTR      pszFileName,
  _In_ DWORD      dwFlags,
  _In_ PBYTE      pbData,
  _In_ DWORD      cbData
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

A pointer to a null-terminated string that contains the name of the directory that contains the file to which to write. The function fails if the specified directory does not exist.

</dd> <dt>

*pszFileName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the file to which to write. The function fails if the specified file does not exist.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> <dt>

*pbData* \[in\]
</dt> <dd>

A pointer to a buffer that contains the data to be written to the file.

</dd> <dt>

*cbData* \[in\]
</dt> <dd>

The size, in bytes, of the *pbData* buffer.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                        | Description                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_FILE\_NOT\_FOUND**</dt> <dt>2148532260 (0x80100024)</dt> </dl>   | The file specified by the *pszDirectoryName* and *pszFileName* parameters does not exist.<br/> |
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>2148532228 (0x80100004)</dt> </dl> | The *dwFlags* parameter contains a value other than zero.<br/>                                 |



 

## Remarks

When a smart card file is overwritten and the allocated size of the file changes, the available storage of the smart card might become fragmented, resulting in significant loss of useful space. This is because it is usually not possible to implement a memory manager for card storage. For this reason, implementations might choose not to shrink a file if its size has been decreased. Users of this function should be aware that the size of a file might exceed the size of the data contained in that file.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[**CardReadFile**](cardreadfile.md)
</dt> </dl>

 

 





