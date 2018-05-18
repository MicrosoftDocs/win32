---
title: CardGetFileInfo function
description: Gets the size and access permissions of a smart card file.
ms.assetid: '964b6fb3-c7cc-4a9c-a784-3a1297e23bef'
keywords: ["CardGetFileInfo function Security"]
topic_type:
- apiref
api_name:
- CardGetFileInfo
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CardGetFileInfo function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardGetFileInfo** function, defined by a smart card module, gets the size and access permissions of a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly) file.

## Syntax


```C++
DWORD WINAPI CardGetFileInfo(
  _In_    PCARD_DATA      pCardData,
  _In_    LPSTR           pszDirectoryName,
  _In_    LPSTR           pszFileName,
  _Inout_ PCARD_FILE_INFO pCardFileInfo
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

A pointer to a null-terminated string that contains the name of the directory that contains the file. The function fails if the specified directory does not exist. Set the value of this parameter to **NULL** if the file is in the **ROOT** directory.

</dd> <dt>

*pszFileName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the file. The function fails if the specified file does not exist.

</dd> <dt>

*pCardFileInfo* \[in, out\]
</dt> <dd>

On input, this parameter contains a pointer to a [**CARD\_FILE\_INFO**](card-file-info.md) structure.

On output, the [**CARD\_FILE\_INFO**](card-file-info.md) structure contains the size and access permissions of the file specified by the *pszFileName* parameter.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero value.

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

[**CARD\_FILE\_INFO**](card-file-info.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> </dl>

 

 





