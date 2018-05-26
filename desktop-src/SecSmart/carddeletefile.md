---
title: CardDeleteFile function
description: Deletes a file from a smart card.
ms.assetid: ea55bc59-c239-45a1-8a46-e0cfc3842695
keywords:
- CardDeleteFile function Security
topic_type:
- apiref
api_name:
- CardDeleteFile
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

# CardDeleteFile function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardDeleteFile** function, defined by a smart card module, deletes a file from a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardDeleteFile(
  _In_ PCARD_DATA pCardData,
  _In_ LPSTR      pszDirectoryName,
  _In_ LPSTR      pszFileName,
  _In_ DWORD      dwFlags
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

A pointer to a null-terminated string that contains the name of the directory that contains the file to delete.

</dd> <dt>

*pszFileName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the file to delete. If the specified file does not exist, the return value of this function should indicate that the file does not exist.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                         | Description                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_FILE\_NOT\_FOUND**</dt> <dt>2148532260 (0x80100024)</dt> </dl>    | The file specified by the *pszDirectoryName* and *pszFileName* parameters does not exist.<br/> |
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>2148532228 (0x80100004)</dt> </dl>  | The *dwFlags* parameter contains a value that is not valid.<br/>                               |
| <dl> <dt>**SCARD\_W\_SECURITY\_VIOLATION**</dt> <dt>2148532330 (0x8010006A)</dt> </dl> | The caller did not authenticate to the smart card before calling this function.<br/>           |



 

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

[**CardCreateFile**](cardcreatefile.md)
</dt> </dl>

 

 





