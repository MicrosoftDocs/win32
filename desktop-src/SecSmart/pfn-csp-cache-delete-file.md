---
title: PFN\_CSP\_CACHE\_DELETE\_FILE function pointer
description: Points to a function that deletes a file from the cache of the Microsoft Base Smart Card Cryptographic Service Provider.
ms.assetid: 8d9f3ec2-32aa-4939-ae55-5ca29d0ca9af
keywords:
- PFN_CSP_CACHE_DELETE_FILE function pointer Security
topic_type:
- apiref
api_name:
- PFN_CSP_CACHE_DELETE_FILE
api_location:
- Cardmod.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PFN\_CSP\_CACHE\_DELETE\_FILE function pointer

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **PFN\_CSP\_CACHE\_DELETE\_FILE** function pointer points to a function that deletes a file from the cache of the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md).

## Syntax


```C++
typedef DWORD ( WINAPI *PFN_CSP_CACHE_DELETE_FILE)(
  _In_ PVOID  pvCacheContext,
  _In_ LPWSTR wszTag,
  _In_ DWORD  dwFlags
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

A pointer to a null-terminated wide character string that contains the name of the cached file to delete. This name was supplied when the file was cached by using the [**PFN\_CSP\_CACHE\_ADD\_FILE**](pfn-csp-cache-add-file.md) function pointer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero value.

## Remarks

This function pointer is passed to a card module in a [**CARD\_DATA**](card-data.md) structure when the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) calls the [**CardAcquireContext**](cardacquirecontext.md) function.

To improve performance by avoiding redundant read/write activity to the card, files on the card that are used only internally by the smart card module can take advantage of caching provided by the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md). This function is used to delete a file from the cache.

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

[**PFN\_CSP\_CACHE\_ADD\_FILE**](pfn-csp-cache-add-file.md)
</dt> </dl>

 

 





