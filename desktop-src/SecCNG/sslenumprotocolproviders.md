---
description: Returns an array of installed Secure Sockets Layer protocol (SSL) protocol providers.
ms.assetid: a61ddcf5-b7e3-40b2-82fc-1cf87eb963ec
title: SslEnumProtocolProviders function (Sslprovider.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SslEnumProtocolProviders
api_type: 
- DllExport
api_location: 
- Ncrypt.dll
---

# SslEnumProtocolProviders function

The **SslEnumProtocolProviders** function returns an array of installed [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) protocol providers.

## Syntax


```C++
SECURITY_STATUS WINAPI SslEnumProtocolProviders(
  _Out_ DWORD              *pdwProviderCount,
  _Out_ NCryptProviderName **ppProviderList,
  _In_  DWORD              dwFlags
);
```



## Parameters

<dl> <dt>

*pdwProviderCount* \[out\]
</dt> <dd>

A pointer to a **DWORD** value to receive the number of protocol providers returned.

</dd> <dt>

*ppProviderList* \[out\]
</dt> <dd>

A pointer to a buffer that receives the array of [**NCryptProviderName**](/windows/desktop/api/Ncrypt/ns-ncrypt-ncryptprovidername) structures.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value.

Possible return codes include, but are not limited to, the following.



| Return code/value                                                                                                                                                       | Description                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt>**NTE\_BAD\_FLAGS**</dt> <dt>0x80090009L</dt> </dl>         | The *dwFlags* parameter is not zero.<br/>                              |
| <dl> <dt>**NTE\_NO\_MEMORY**</dt> <dt>0x8009000EL</dt> </dl>         | Not enough memory is available to allocate necessary buffers.<br/>     |
| <dl> <dt>**NTE\_INVALID\_PARAMETER**</dt> <dt>0x80090027L</dt> </dl> | The *pdwProviderCount* or *ppProviderList* parameter is **NULL**.<br/> |



 

## Remarks

When you have finished using the array of [**NCryptProviderName**](/windows/desktop/api/Ncrypt/ns-ncrypt-ncryptprovidername) structures, call the [**SslFreeBuffer**](sslfreebuffer.md) function to free the array.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Sslprovider.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ncrypt.dll</dt> </dl>    |



 

