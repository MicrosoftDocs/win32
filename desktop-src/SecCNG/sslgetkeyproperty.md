---
description: Retrieves the value of a named property for a Secure Sockets Layer protocol (SSL) provider key object.
ms.assetid: 01a7e82a-3888-4f96-85a2-e07811f1895e
title: SslGetKeyProperty function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslGetKeyProperty
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslGetKeyProperty function

The **SslGetKeyProperty** function retrieves the value of a named property for a [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) provider key object.

## Syntax


```C++
SECURITY_STATUS WINAPI SslGetKeyProperty(
  _In_  NCRYPT_KEY_HANDLE hKey,
  _In_  LPCWSTR           pszProperty,
  _Out_ PBYTE             ppbOutput,
  _Out_ DWORD             *pcbOutput,
  _In_  DWORD             dwFlags
);
```



## Parameters

<dl> <dt>

*hKey* \[in\]
</dt> <dd>

The handle of the SSL provider.

</dd> <dt>

*pszProperty* \[in\]
</dt> <dd>

A pointer to a null-terminated Unicode string that contains the name of the property to retrieve. This can be one of the predefined [**Key Storage Property Identifiers**](key-storage-property-identifiers.md) or a custom property identifier.

</dd> <dt>

*ppbOutput* \[out\]
</dt> <dd>

A pointer to a buffer that receives the property value. The caller of the function must free this buffer by calling the [**SslFreeBuffer**](sslfreebuffer.md) function.

</dd> <dt>

*pcbOutput* \[out\]
</dt> <dd>

The size, in bytes, of the *pbOutput* buffer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                       | Description                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl>    | One of the provided handles is not valid.<br/>    |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | One of the supplied parameters is not valid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

