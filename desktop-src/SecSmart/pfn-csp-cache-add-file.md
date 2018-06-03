---
title: PFN\_CSP\_CACHE\_ADD\_FILE function pointer
description: Points to a function that adds a file to the data cached by the Microsoft Base Smart Card Cryptographic Service Provider.
ms.assetid: d578eef9-ddd6-48a4-af10-35c772bdc427
keywords:
- PFN_CSP_CACHE_ADD_FILE function pointer Security
topic_type:
- apiref
api_name:
- PFN_CSP_CACHE_ADD_FILE
api_location:
- Cardmod.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PFN\_CSP\_CACHE\_ADD\_FILE function pointer

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **PFN\_CSP\_CACHE\_ADD\_FILE** function pointer points to a function that adds a file to the data cached by the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md).

## Syntax


```C++
typedef DWORD ( WINAPI *PFN_CSP_CACHE_ADD_FILE)(
  _In_ PVOID  pvCacheContext,
  _In_ LPWSTR wszTag,
  _In_ DWORD  dwFlags,
  _In_ PBYTE  pbData,
  _In_ DWORD  cbData
);
```



## Parameters

<dl> <dt>

*pvCacheContext* \[in\]
</dt> <dd>

A context value supplied by the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md). This value must be set to the value of the **pvCacheContext** member of the corresponding [**CARD\_DATA**](card-data.md) structure.

</dd> <dt>

*wszTag* \[in\]
</dt> <dd>

A pointer to a null-terminated wide character string that contains the name of the file to cache. This name is used in subsequent calls using the [**PFN\_CSP\_CACHE\_LOOKUP\_FILE**](pfn-csp-cache-lookup-file.md) and [**PFN\_CSP\_CACHE\_DELETE\_FILE**](pfn-csp-cache-delete-file.md) function pointers.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> <dt>

*pbData* \[in\]
</dt> <dd>

A pointer to a buffer that contains the data to be cached. the smart card module allocates memory for this buffer by using the [**PFN\_CSP\_ALLOC**](pfn-csp-alloc.md) function pointer.

When memory for this buffer is no longer required, the smart card module must free it by using the [**PFN\_CSP\_FREE**](pfn-csp-free.md) function pointer.

</dd> <dt>

*cbData* \[in\]
</dt> <dd>

The size, in bytes, of the data contained in the *pbData* buffer.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero value.

## Remarks

This function pointer is passed to a card module in a [**CARD\_DATA**](card-data.md) structure when the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) calls the [**CardAcquireContext**](cardacquirecontext.md) function.

To improve performance by avoiding redundant read/write activity to the card, files on the card that are used only internally by the smart card module can take advantage of caching provided by the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md). This function is used to add a file to the cache.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[**PFN\_CSP\_ALLOC**](pfn-csp-alloc.md)
</dt> <dt>

[**PFN\_CSP\_FREE**](pfn-csp-free.md)
</dt> </dl>

 

 





