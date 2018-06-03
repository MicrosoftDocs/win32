---
title: CardCreateDirectory function
description: Creates a subdirectory of the root directory in the file system on a smart card.
ms.assetid: e5f067e1-fdd7-4a83-993e-ffbca22c1a38
keywords:
- CardCreateDirectory function Security
topic_type:
- apiref
api_name:
- CardCreateDirectory
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CardCreateDirectory function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardCreateDirectory** function, defined by a smart card module, creates a subdirectory of the root directory in the file system on a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardCreateDirectory(
  _In_ PCARD_DATA                      pCardData,
  _In_ LPSTR                           pszDirectory,
  _In_ CARD_DIRECTORY_ACCESS_CONDITION AccessCondition
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to the [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pszDirectory* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the new directory. The string must contain eight or fewer ANSI characters.

</dd> <dt>

*AccessCondition* \[in\]
</dt> <dd>

A member of the [**CARD\_DIRECTORY\_ACCESS\_CONDITION**](https://msdn.microsoft.com/library/windows/desktop/aa375997) enumeration that specifies access control permissions for the new directory.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                         | Description                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_FILE\_EXISTS**</dt> <dt>128 (0x80)</dt> </dl>                        | A directory with the same name as the value of the *pszDirectory* parameter already exists, or there is not enough memory on the smart card to create the new directory.<br/> |
| <dl> <dt>**SCARD\_W\_SECURITY\_VIOLATION**</dt> <dt>2148532330 (0x8010006A)</dt> </dl> | The caller did not authenticate to the smart card before calling this function.<br/>                                                                                          |
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>2148532228 (0x80100004)</dt> </dl>  | The value of the *AccessCondition* parameter is not a valid value of the [**CARD\_DIRECTORY\_ACCESS\_CONDITION**](https://msdn.microsoft.com/library/windows/desktop/aa375997) enumeration.<br/> |



 

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
</dt> </dl>

 

 





