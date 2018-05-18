---
title: CardCreateFile function
description: Creates a file in the specified directory of a smart card.
ms.assetid: '030a7102-0e5c-43c8-a0ef-3688655dc75d'
keywords: ["CardCreateFile function Security"]
topic_type:
- apiref
api_name:
- CardCreateFile
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CardCreateFile function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardCreateFile** function, defined by a smart card module, creates a file in the specified directory of a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardCreateFile(
  _In_ PCARD_DATA                 pCardData,
  _In_ LPSTR                      pszDirectoryName,
  _In_ LPSTR                      pszFileName,
  _In_ DWORD                      cbInitialCreationSize,
  _In_ CARD_FILE_ACCESS_CONDITION AccessCondition
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to the [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pszDirectoryName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains a directory name. The **CardCreateFile** function creates the new file in this directory. The function fails if the specified directory does not exist.

</dd> <dt>

*pszFileName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the file to create.

</dd> <dt>

*cbInitialCreationSize* \[in\]
</dt> <dd>

The size, in bytes, of the new file.

</dd> <dt>

*AccessCondition* \[in\]
</dt> <dd>

A member of the [**CARD\_FILE\_ACCESS\_CONDITION**](https://msdn.microsoft.com/library/windows/desktop/aa375998) enumeration that specifies access control permissions for the new file.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                  | Description                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_FILE\_EXISTS**</dt> <dt>128 (0x80)</dt> </dl> | A file with the same name as the value of the *pszFileName* parameter already exists.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> </dl>

 

 





