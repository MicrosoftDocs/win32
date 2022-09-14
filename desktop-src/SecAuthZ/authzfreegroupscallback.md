---
description: An application-defined function that frees memory allocated by the AuthzComputeGroupsCallback function. AuthzFreeGroupsCallback is a placeholder for the application-defined function name.
ms.assetid: 5563311c-2bd1-4e96-ba0a-5a4225050f77
title: AuthzFreeGroupsCallback callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AuthzFreeGroupsCallback
api_type: 
- UserDefined
api_location: 
---

# AuthzFreeGroupsCallback callback function

The **AuthzFreeGroupsCallback** function is an application-defined function that frees memory allocated by the [**AuthzComputeGroupsCallback**](authzcomputegroupscallback.md) function. **AuthzFreeGroupsCallback** is a placeholder for the application-defined function name.

## Syntax


```C++
void CALLBACK AuthzFreeGroupsCallback(
  _In_ PSID_AND_ATTRIBUTES pSidAttrArray
);
```



## Parameters

<dl> <dt>

*pSidAttrArray* \[in\]
</dt> <dd>

A pointer to memory allocated by [**AuthzComputeGroupsCallback**](authzcomputegroupscallback.md).

</dd> </dl>

## Return value

This callback function does not return a value.

## Remarks

Attribute variables must be in the form of an expression when used with logical operators; otherwise, they are evaluated as unknown.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                   |
| Redistributable<br/>          | Windows Server 2003 Administration Tools Pack on Windows XP<br/> |



## See also

<dl> <dt>

[Basic Access Control Functions](authorization-functions.md)
</dt> <dt>

[**AuthzComputeGroupsCallback**](authzcomputegroupscallback.md)
</dt> </dl>

 

 




