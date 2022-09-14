---
description: The AuthzGetCentralAccessPolicyCallback function is an application-defined function that retrieves the central access policy. AuthzGetCentralAccessPolicyCallback is a placeholder for the application-defined function name.
ms.assetid: 1D5831EF-ACA8-4EE9-A7C1-E1A3CB74CEC0
title: AuthzGetCentralAccessPolicyCallback callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AuthzGetCentralAccessPolicyCallback
api_type: 
- UserDefined
api_location: 
---

# AuthzGetCentralAccessPolicyCallback callback function

The *AuthzGetCentralAccessPolicyCallback* function is an application-defined function that retrieves the central access policy. *AuthzGetCentralAccessPolicyCallback* is a placeholder for the application-defined function name.

## Syntax


```C++
BOOL CALLBACK AuthzGetCentralAccessPolicyCallback (
  _In_     AUTHZ_CLIENT_CONTEXT_HANDLE hAuthzClientContext,
  _In_     PSID                        capid,
  _In_opt_ PVOID                       pArgs,
  _Out_    PBOOL                       pCentralAccessPolicyApplicable,
  _Out_    PVOID                       ppCentralAccessPolicy
);
```



## Parameters

<dl> <dt>

*hAuthzClientContext* \[in\]
</dt> <dd>

Handle to the client context.

</dd> <dt>

*capid* \[in\]
</dt> <dd>

ID of the central access policy to retrieve.

</dd> <dt>

*pArgs* \[in, optional\]
</dt> <dd>

Optional arguments that were passed to the [**AuthzAccessCheck**](/windows/desktop/api/Authz/nf-authz-authzaccesscheck) function through the **OptionalArguments** member of the [**AUTHZ\_ACCESS\_REQUEST**](/windows/desktop/api/Authz/ns-authz-authz_access_request) structure.

</dd> <dt>

*pCentralAccessPolicyApplicable* \[out\]
</dt> <dd>

Pointer to a Boolean value that the resource manager uses to indicate whether a central access policy should be used during access evaluation.

</dd> <dt>

*ppCentralAccessPolicy* \[out\]
</dt> <dd>

Pointer to the central access policy (CAP) to be used for evaluating access. If this value is **NULL**, the default CAP is applied.

</dd> </dl>

## Return value

If the function succeeds, the function returns **TRUE**.

If the function is unable to perform the evaluation, it returns **FALSE**. Use [**SetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-setlasterror) to return an error to the access check function.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                   |
| Redistributable<br/>          | Windows Server 2003 Administration Tools Pack on Windows XP<br/> |



## See also

<dl> <dt>

[**AUTHZ\_ACCESS\_REQUEST**](/windows/desktop/api/Authz/ns-authz-authz_access_request)
</dt> <dt>

[**AUTHZ\_INIT\_INFO**](/windows/desktop/api/Authz/ns-authz-authz_init_info)
</dt> <dt>

[**AuthzAccessCheck**](/windows/desktop/api/Authz/nf-authz-authzaccesscheck)
</dt> </dl>

 

