---
description: Retrieves the value of a specified provider property.
ms.assetid: 69235520-acaa-4ec4-9fd6-4b3297e14376
title: SslGetProviderProperty function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslGetProviderProperty
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslGetProviderProperty function

The **SslGetProviderProperty** function retrieves the value of a specified provider property.

## Syntax


```C++
SECURITY_STATUS WINAPI SslGetProviderProperty(
  _In_    NCRYPT_PROV_HANDLE hSslProvider,
  _In_    LPCWSTR            pszProperty,
  _Out_   PBYTE              ppbOutput,
  _Out_   DWORD              *pcbOutput,
  _Inout_ PVOID              *ppEnumState,
  _In_    DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*hSslProvider* \[in\]
</dt> <dd>

The handle of the [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) provider for which to retrieve the property.

</dd> <dt>

*pszProperty* \[in\]
</dt> <dd>

A pointer to a null-terminated Unicode string that contains the name of the property to retrieve.

</dd> <dt>

*ppbOutput* \[out\]
</dt> <dd>

The address of a buffer that receives the property value.

The caller of the function must free this buffer by calling the [**SslFreeBuffer**](sslfreebuffer.md) function.

</dd> <dt>

*pcbOutput* \[out\]
</dt> <dd>

The size, in bytes, of the *pbOutput* buffer.

</dd> <dt>

*ppEnumState* \[in, out\]
</dt> <dd>

The address of a **VOID** pointer that receives enumeration state information that is used in subsequent calls to this function. This information only has meaning to the SSL provider and is opaque to the caller. The SSL provider uses this information to determine which item is next in the enumeration. If the variable pointed to by this parameter contains **NULL**, the enumeration is started from the beginning.

The caller of the function must free this memory by calling the [**SslFreeBuffer**](sslfreebuffer.md) function.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                       | Description                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>**NTE\_NO\_MEMORY**</dt> <dt>0x8009000EL</dt> </dl>         | Not enough memory is available to allocate necessary buffers.<br/> |
| <dl> <dt>**NTE\_INVALID\_HANDLE**</dt> <dt>0x80090026L</dt> </dl>    | The *hSslProvider* handle is not valid.<br/>                       |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | One of the supplied parameters is not valid.<br/>                  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

