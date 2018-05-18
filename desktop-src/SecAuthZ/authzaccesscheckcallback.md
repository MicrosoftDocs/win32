---
Description: 'An application-defined function that handles callback access control entries (ACEs) during an access check.'
ms.assetid: 'e8a510e6-0739-4765-ad07-3bcb1b9c905c'
title: AuthzAccessCheckCallback callback function
---

# AuthzAccessCheckCallback callback function

The **AuthzAccessCheckCallback** function is an application-defined function that handles callback [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) during an access check. **AuthzAccessCheckCallback** is a placeholder for the application-defined function name. The application registers this callback by calling [**AuthzInitializeResourceManager**](authzinitializeresourcemanager.md).

## Syntax


```C++
BOOL CALLBACK AuthzAccessCheckCallback(
  _In_     AUTHZ_CLIENT_CONTEXT_HANDLE hAuthzClientContext,
  _In_     PACE_HEADER                 pAce,
  _In_opt_ PVOID                       pArgs,
  _Inout_  PBOOL                       pbAceApplicable
);
```



## Parameters

<dl> <dt>

*hAuthzClientContext* \[in\]
</dt> <dd>

A handle to a client context.

</dd> <dt>

*pAce* \[in\]
</dt> <dd>

A pointer to the ACE to evaluate for inclusion in the call to the [**AuthzAccessCheck**](authzaccesscheck.md) function.

</dd> <dt>

*pArgs* \[in, optional\]
</dt> <dd>

Data passed in the *DynamicGroupArgs* parameter of the call to [**AuthzAccessCheck**](authzaccesscheck.md) or [**AuthzCachedAccessCheck**](authzcachedaccesscheck.md).

</dd> <dt>

*pbAceApplicable* \[in, out\]
</dt> <dd>

A pointer to a Boolean variable that receives the results of the evaluation of the logic defined by the application.

The results are **TRUE** if the logic determines that the ACE is applicable and will be included in the call to [**AuthzAccessCheck**](authzaccesscheck.md); otherwise, the results are **FALSE**.

</dd> </dl>

## Return value

If the function succeeds, the function returns **TRUE**.

If the function is unable to perform the evaluation, it returns **FALSE**. Use [**SetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms680627) to return an error to the access check function.

## Remarks

Security attribute variables must be present in the client context if referred to in a conditional expression, otherwise the conditional expression term referencing them will evaluate to unknown.

For more information, see the [How AccessCheck Works](how-dacls-control-access-to-an-object.md) and [Centralized Authorization Policy](centralized-authorization-policy.md) overviews.

## Requirements



|                                     |                                                                        |
|-------------------------------------|------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                   |
| Redistributable<br/>          | Windows Server 2003 Administration Tools Pack on Windows XP<br/> |



## See also

<dl> <dt>

[Basic Access Control Functions](authorization-functions.md#basic-access-control-functions)
</dt> <dt>

[Centralized Authorization Policy](centralized-authorization-policy.md)
</dt> <dt>

[How AccessCheck Works](how-dacls-control-access-to-an-object.md)
</dt> <dt>

[**AuthzAccessCheck**](authzaccesscheck.md)
</dt> <dt>

[**AuthzCachedAccessCheck**](authzcachedaccesscheck.md)
</dt> <dt>

[**AuthzInitializeRemoteResourceManager**](authzinitializeremoteresourcemanager.md)
</dt> <dt>

[**AuthzInitializeResourceManager**](authzinitializeresourcemanager.md)
</dt> </dl>

 

 




