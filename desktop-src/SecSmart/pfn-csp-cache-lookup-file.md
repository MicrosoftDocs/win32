---
title: PFN\_CSP\_CACHE\_LOOKUP\_FILE function pointer
description: Points to a function that reads a file that was cached by the Microsoft Base Smart Card Cryptographic Service Provider as the result of a previous call that used the PFN\_CSP\_CACHE\_ADD\_FILE function pointer.
ms.assetid: '57868c11-94ee-4791-a115-28a4d2259241'
keywords: ["PFN_CSP_CACHE_LOOKUP_FILE function pointer Security"]
topic_type:
- apiref
api_name:
- PFN_CSP_CACHE_LOOKUP_FILE
api_location:
- Cardmod.h
api_type:
- UserDefined
---

# PFN\_CSP\_CACHE\_LOOKUP\_FILE function pointer

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **PFN\_CSP\_CACHE\_LOOKUP\_FILE** function pointer points to a function that reads a file that was cached by the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) as the result of a previous call that used the [**PFN\_CSP\_CACHE\_ADD\_FILE**](pfn-csp-cache-add-file.md) function pointer.

## Syntax


```C++
typedef DWORD ( WINAPI *PFN_CSP_CACHE_LOOKUP_FILE)(
  _In_  PVOID  pvCacheContext,
  _In_  LPWSTR wszTag,
  _In_  DWORD  dwFlags,
  _Out_ PBYTE  *ppbData,
  _Out_ PDWORD pcbData
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

A pointer to a null-terminated wide character string that contains the name of the cached file to read. This name was supplied when the file was cached by using the [**PFN\_CSP\_CACHE\_ADD\_FILE**](pfn-csp-cache-add-file.md) function pointer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> <dt>

*ppbData* \[out\]
</dt> <dd>

A pointer to a buffer that receives the data from the cached file.

When memory for this buffer is no longer required, the smart card module must free it by using the [**PFN\_CSP\_FREE**](pfn-csp-free.md) function pointer.

</dd> <dt>

*pcbData* \[out\]
</dt> <dd>

A pointer to a **DWORD** that receives the size, in bytes, of the data contained in the *ppbData* buffer.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero value.

## Remarks

This function pointer is passed to a card module in a [**CARD\_DATA**](card-data.md) structure when the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) calls the [**CardAcquireContext**](cardacquirecontext.md) function.

To improve performance by avoiding redundant read/write activity to the card, files on the card that are used only internally by the smart card module can take advantage of caching provided by the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md). This function is used to find a file in the cache.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[**PFN\_CSP\_CACHE\_ADD\_FILE**](pfn-csp-cache-add-file.md)
</dt> <dt>

[**PFN\_CSP\_FREE**](pfn-csp-free.md)
</dt> </dl>

 

 





