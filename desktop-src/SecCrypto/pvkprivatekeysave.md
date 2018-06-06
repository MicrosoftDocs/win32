---
Description: Saves a private key and its corresponding public key to a specified file.
ms.assetid: 491a128a-b4aa-4cca-a835-d0e8d7df6720
title: PvkPrivateKeySave function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PvkPrivateKeySave function

> \[!Important\]  
> This API is deprecated. Microsoft may remove this API in future releases.

 

The **PvkPrivateKeySave** function saves a [*private key*](security.p_gly#-security-private-key-gly) and its corresponding [*public key*](security.p_gly#-security-public-key-gly) to a specified file.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions to dynamically link to Mssign32.dll.

 

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

A handle to a [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP).

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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



 

 




