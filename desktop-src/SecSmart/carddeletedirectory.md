---
title: CardDeleteDirectory function
description: Deletes a directory from a smart card. The directory must be empty, and the caller must have permission to delete that directory.
ms.assetid: 'c5a4e77d-fa0e-4808-8f62-e099aa3b3ecf'
keywords: ["CardDeleteDirectory function Security"]
topic_type:
- apiref
api_name:
- CardDeleteDirectory
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CardDeleteDirectory function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardDeleteDirectory** function, defined by a smart card module, deletes a directory from a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly). The directory must be empty, and the caller must have permission to delete that directory.

## Syntax


```C++
DWORD WINAPI CardDeleteDirectory(
  _In_ PCARD_DATA pCardData,
  _In_ LPSTR      pszDirectoryName
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

A pointer to a null-terminated string that contains the name of the directory to delete.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                         | Description                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_W\_SECURITY\_VIOLATION**</dt> <dt>2148532330 (0x8010006A)</dt> </dl> | The caller did not authenticate to the smart card before calling this function.<br/> |



 

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
</dt> <dt>

[**CardCreateDirectory**](cardcreatedirectory.md)
</dt> </dl>

 

 





