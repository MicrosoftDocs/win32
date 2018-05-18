---
Description: 'Creates a temporary container in the cryptographic service provider (CSP) and loads a private key from memory into the container.'
ms.assetid: '9388b49b-fad4-4499-a391-fe58ed672552'
title: PvkPrivateKeyAcquireContextFromMemory function
---

# PvkPrivateKeyAcquireContextFromMemory function

> \[!Important\]  
> This API is deprecated. Microsoft may remove this API in future releases.

 

The **PvkPrivateKeyAcquireContextFromMemory** function creates a temporary container in the [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) and loads a [*private key*](security.p_gly#-security-private-key-gly) from memory into the container.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
BOOL WINAPI PvkPrivateKeyAcquireContextFromMemory(
  _In_        LPCWSTR    pwszProvName,
  _In_        DWORD      dwProvType,
  _In_        BYTE       *pbData,
  _In_        DWORD      cbData,
  _In_        HWND       hwndOwner,
  _In_        LPCWSTR    pwszKeyName,
  _Inout_opt_ DWORD      *pdwKeySpec,
  _Out_       HCRYPTPROV *phCryptProv,
  _Out_       LPTSTR     *ppwszTmpContainer
);
```



## Parameters

<dl> <dt>

*pwszProvName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the CSP whose type is requested in *dwProvType*.

</dd> <dt>

*dwProvType* \[in\]
</dt> <dd>

A **DWORD** value for the CSP type. For more information about CSP types, see [Cryptographic Provider Types](cryptographic-provider-types.md).

</dd> <dt>

*pbData* \[in\]
</dt> <dd>

A pointer to a buffer to receive the context data. The caller must provide this resource.

</dd> <dt>

*cbData* \[in\]
</dt> <dd>

A **DWORD** value that specifies the size, in bytes, of the *pbData* buffer. The caller must provide this value.

</dd> <dt>

*hwndOwner* \[in\]
</dt> <dd>

If a password is required to decrypt the context data pointed to by the *pbData* parameter, this parameter is a handle to the parent of the dialog box; otherwise, it is **NULL**.

</dd> <dt>

*pwszKeyName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the key to retrieve.

</dd> <dt>

*pdwKeySpec* \[in, out, optional\]
</dt> <dd>

A pointer to a **DWORD** value that specifies the type of key. Possible values include **AT\_KEYEXCHANGE** or **AT\_SIGNATURE**.

</dd> <dt>

*phCryptProv* \[out\]
</dt> <dd>

A pointer to a handle for the CSP.

</dd> <dt>

*ppwszTmpContainer* \[out\]
</dt> <dd>

The address of a pointer to a null-terminated string for the temporary container name. The **PvkPrivateKeyAcquireContextFromMemory** function provides the buffer for this string and initializes it. When calling **PvkPrivateKeyAcquireContextFromMemory**, the address should point to a **NULL** value.

</dd> </dl>

## Return value

Upon success, this function returns **TRUE**. The **PvkPrivateKeyAcquireContextFromMemory** function returns **FALSE** if it fails.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



 

 




