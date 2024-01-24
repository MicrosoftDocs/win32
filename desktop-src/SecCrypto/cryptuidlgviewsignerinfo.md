---
description: 'Displays a dialog box that contains the signer information for a signed message.'
ms.assetid: 'e4552cbb-90f4-46f4-a271-3a91ccd5f806'
title: CryptUIDlgViewSignerInfo function
ms.topic: reference
ms.date: 05/29/2020
---

# CryptUIDlgViewSignerInfo function

\[The **CryptUIDlgViewSignerInfo** function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

The **CryptUIDlgViewSignerInfo** function displays a dialog box that contains the signer information for a signed message.

> [!Note]  
> This function is not declared in a published header file. To use this structure, declare it in the exact format shown.

## Syntax


```C++
);
```



## Parameters

<dl> <dt>

*pcvsi* \[in\]
</dt> <dd>

A pointer to a [**CRYPTUI\_VIEWSIGNERINFO\_STRUCT**](cryptui-viewsignerinfo-struct.md) structure that contains the signer information to display.

</dd> </dl>

## Return value

This function returns a nonzero value on success and zero on failure. For extended error information, call the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function.

Possible error codes returned from [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) include, but are not limited to, the following.



| Return code                                                                                   | Description                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | One or more arguments are not valid.<br/>  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | A memory allocation failure occurred.<br/> |

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                        |
| End of support<br/> | Windows 7 \[desktop apps only\]<br/>                                                       |
| Library<br/>                  | <dl> <dt>Cryptui.lib</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>Cryptui.dll</dt> </dl>      |
| Unicode and ANSI names<br/>   | **CryptUIDlgViewSignerInfoW** (Unicode) and **CryptUIDlgViewSignerInfoA** (ANSI)<br/> |



## See also

<dl> <dt>

[**CRYPTUI\_VIEWSIGNERINFO\_STRUCT**](cryptui-viewsignerinfo-struct.md)
</dt> </dl>
