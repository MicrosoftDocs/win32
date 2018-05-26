---
Description: An application-defined function that creates a list of security identifiers (SIDs) that apply to a client. AuthzComputeGroupsCallback is a placeholder for the application-defined function name.
ms.assetid: c20a02a0-5303-4433-a484-5a89999b32b9
title: AuthzComputeGroupsCallback callback function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AuthzComputeGroupsCallback callback function

The **AuthzComputeGroupsCallback** function is an application-defined function that creates a list of [*security identifiers*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SIDs) that apply to a client. **AuthzComputeGroupsCallback** is a placeholder for the application-defined function name.

## Syntax


```C++
BOOL CALLBACK AuthzComputeGroupsCallback(
  _In_  AUTHZ_CLIENT_CONTEXT_HANDLE hAuthzClientContext,
  _In_  PVOID                       Args,
  _Out_ PSID_AND_ATTRIBUTES         *pSidAttrArray,
  _Out_ PDWORD                      pSidCount,
  _Out_ PSID_AND_ATTRIBUTES         *pRestrictedSidAttrArray,
  _Out_ PDWORD                      pRestrictedSidCount
);
```



## Parameters

<dl> <dt>

*hAuthzClientContext* \[in\]
</dt> <dd>

A handle to a client context.

</dd> <dt>

*Args* \[in\]
</dt> <dd>

Data passed in the *DynamicGroupArgs* parameter of a call to the [**AuthzInitializeContextFromAuthzContext**](/windows/win32/Authz/nf-authz-authzinitializecontextfromauthzcontext?branch=master), [**AuthzInitializeContextFromSid**](/windows/win32/Authz/nf-authz-authzinitializecontextfromsid?branch=master), or [**AuthzInitializeContextFromToken**](/windows/win32/Authz/nf-authz-authzinitializecontextfromtoken?branch=master) function.

</dd> <dt>

*pSidAttrArray* \[out\]
</dt> <dd>

A pointer to a pointer variable that receives the address of an array of [**SID\_AND\_ATTRIBUTES**](/windows/win32/Winnt/ns-winnt-_sid_and_attributes?branch=master) structures. These structures represent the groups to which the client belongs.

</dd> <dt>

*pSidCount* \[out\]
</dt> <dd>

The number of structures in *pSidAttrArray*.

</dd> <dt>

*pRestrictedSidAttrArray* \[out\]
</dt> <dd>

A pointer to a pointer variable that receives the address of an array of [**SID\_AND\_ATTRIBUTES**](/windows/win32/Winnt/ns-winnt-_sid_and_attributes?branch=master) structures. These structures represent the groups from which the client is restricted.

</dd> <dt>

*pRestrictedSidCount* \[out\]
</dt> <dd>

The number of structures in *pSidRestrictedAttrArray*.

</dd> </dl>

## Return value

If the function successfully returns a list of SIDs, the return value is **TRUE**.

If the function fails, the return value is **FALSE**.

## Remarks

Applications can also add SIDs to the client context by calling [**AuthzAddSidsToContext**](/windows/win32/Authz/nf-authz-authzaddsidstocontext?branch=master).

Attribute variables must be in the form of an expression when used with logical operators; otherwise, they are evaluated as unknown.

## Requirements



|                                     |                                                                        |
|-------------------------------------|------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                   |
| Redistributable<br/>          | Windows Server 2003 Administration Tools Pack on Windows XP<br/> |



## See also

<dl> <dt>

[Basic Access Control Functions](authorization-functions.md#basic-access-control-functions)
</dt> <dt>

[**AuthzAddSidsToContext**](/windows/win32/Authz/nf-authz-authzaddsidstocontext?branch=master)
</dt> <dt>

[**AuthzCachedAccessCheck**](/windows/win32/Authz/nf-authz-authzcachedaccesscheck?branch=master)
</dt> <dt>

[**AuthzInitializeContextFromAuthzContext**](/windows/win32/Authz/nf-authz-authzinitializecontextfromauthzcontext?branch=master)
</dt> <dt>

[**AuthzInitializeContextFromSid**](/windows/win32/Authz/nf-authz-authzinitializecontextfromsid?branch=master)
</dt> <dt>

[**AuthzInitializeContextFromToken**](/windows/win32/Authz/nf-authz-authzinitializecontextfromtoken?branch=master)
</dt> <dt>

[**AuthzInitializeResourceManager**](/windows/win32/Authz/nf-authz-authzinitializeresourcemanager?branch=master)
</dt> <dt>

[**SID\_AND\_ATTRIBUTES**](/windows/win32/Winnt/ns-winnt-_sid_and_attributes?branch=master)
</dt> </dl>

 

 




