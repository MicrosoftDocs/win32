---
title: IsColorProfileValid function
description: The IsColorProfileValid function allows an application to determine whether the specified profile is a valid International Color Consortium (ICC) profile or a valid Windows Color System (WCS) profile handle that can be used for color management.
ms.assetid: 6b8075ae-301c-4b22-8bed-b4bb154ccc9e
keywords:
- IsColorProfileValid function Windows Color System
topic_type:
- apiref
api_name:
- IsColorProfileValid
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IsColorProfileValid function

The **IsColorProfileValid** function allows an application to determine whether the specified profile is a valid International Color Consortium (ICC) profile or a valid Windows Color System (WCS) profile handle that can be used for color management. WCS profile validation does not invoke the underlying device models, but instead simply validates against the XML schema and the schema element range limits.

## Syntax


```C++
BOOL WINAPI IsColorProfileValid(
   HPROFILE hProfile,
   PBOOL    pbValid
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the profile to be validated. The function determines whether the HPROFILE contains ICC or WCS profile information.

</dd> <dt>

*pbValid* 
</dt> <dd>

Pointer to a variable that is set to **TRUE** on return if the operation succeeds and the profile is a valid ICC or WCS profile. If the operation fails or the profile is not valid the variable is **FALSE**.

</dd> </dl>

## Return value

If this function succeeds and the profile is valid, the return value is **TRUE**.

If this function fails (or succeeds and the profile is not valid), the return value is **FALSE**. For extended error information, call **GetLastError**.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





