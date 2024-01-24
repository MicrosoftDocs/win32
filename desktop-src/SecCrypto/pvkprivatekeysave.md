---
description: Saves a private key and its corresponding public key to a specified file.
ms.assetid: 491a128a-b4aa-4cca-a835-d0e8d7df6720
title: PvkPrivateKeySave function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PvkPrivateKeySave
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# PvkPrivateKeySave function

> [!IMPORTANT]
> This API is deprecated. Microsoft may remove this API in future releases.

 

The **PvkPrivateKeySave** function saves a [*private key*](../secgloss/p-gly.md) and its corresponding [*public key*](../secgloss/p-gly.md) to a specified file.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
BOOL WINAPI PvkPrivateKeySave(
  _In_ HCRYPTPROV hCryptProv,
  _In_ HANDLE     hFile,
  _In_ DWORD      dwKeySpec,
  _In_ HWND       hwndOwner,
  _In_ LPCWSTR    pwszKeyName,
  _In_ DWORD      dwFlags
);
```



## Parameters

<dl> <dt>

*hCryptProv* \[in\]
</dt> <dd>

A handle to a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).

</dd> <dt>

*hFile* \[in\]
</dt> <dd>

A handle to a file created with initial read/write permission and subsequent read-only permission.

</dd> <dt>

*dwKeySpec* \[in\]
</dt> <dd>

A long integer for the type of key. Possible values include **AT\_KEYEXCHANGE** or **AT\_SIGNATURE**.

</dd> <dt>

*hwndOwner* \[in\]
</dt> <dd>

If a password is required to encrypt the private key, this parameter is a handle to the parent of the dialog box; otherwise, it is **NULL**.

</dd> <dt>

*pwszKeyName* \[in\]
</dt> <dd>

A pointer to a null-terminated string for the name of the key to be saved.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

A **DWORD** value that specifies additional options for the function. For more information, see the *dwFlags* parameter in [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey).

</dd> </dl>

## Return value

Upon success, this function returns **TRUE**. The **PvkPrivateKeySave** function returns **FALSE** if it fails.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



 

 
