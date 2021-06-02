---
description: Gets the level of a hash identification rule that matches the specified hash.
ms.assetid: 1592c8da-31c0-45fb-b832-d439dd53c277
title: SaferiSearchMatchingHashRules function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SaferiSearchMatchingHashRules
api_type: 
- DllExport
api_location: 
- Advapi32.dll
- Ext-MS-Win-AdvAPI32-safer-l1-1-0.dll
---

# SaferiSearchMatchingHashRules function

Gets the level of a hash identification rule that matches the specified hash.

This function has no associated import library and is not declared in a public header. You must define a function pointer with the signature of this function, and you must use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Advapi32.dll.

We recommend using the [**SaferIdentifyLevel**](/windows/win32/api/winsafer/nf-winsafer-saferidentifylevel) function to evaluate software restriction policies.

## Syntax


```C++
BOOL WINAPI SaferiSearchMatchingHashRules(
  _In_opt_ ALG_ID HashAlgorithm,
  _In_     PBYTE  pHashBytes,
  _In_     DWORD  dwHashSize,
  _In_opt_ DWORD  dwOriginalImageSize,
  _Out_    PDWORD pdwFoundLevel,
           PDWORD pdwSaferFlags
);
```



## Parameters

<dl> <dt>

*HashAlgorithm* \[in, optional\]
</dt> <dd>

The identifier of the algorithm used to create the hash.

</dd> <dt>

*pHashBytes* \[in\]
</dt> <dd>

A pointer to an array of bytes that contains the hash.

</dd> <dt>

*dwHashSize* \[in\]
</dt> <dd>

The size, in bytes, of the *pHashBytes* array.

</dd> <dt>

*dwOriginalImageSize* \[in, optional\]
</dt> <dd>

The size, in bytes, of the original image from which the hash was computed.

</dd> <dt>

*pdwFoundLevel* \[out\]
</dt> <dd>

A pointer to the level identifier for the matching hash identification rule.

</dd> <dt>

*pdwSaferFlags* 
</dt> <dd>

Reserved. Set this value to zero.

</dd> </dl>

## Return value

**TRUE** if the function is successful; otherwise, **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |



 

 
