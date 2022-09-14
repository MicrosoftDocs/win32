---
description: The AuthzFreeCentralAccessPolicyCallback function is an application-defined function that frees memory allocated by the AuthzGetCentralAccessPolicyCallback function.
ms.assetid: F0859A67-4D20-4189-8F35-A78034E41E6A
title: AuthzFreeCentralAccessPolicyCallback callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AuthzFreeCentralAccessPolicyCallback
api_type: 
- UserDefined
api_location: 
---

# AuthzFreeCentralAccessPolicyCallback callback function

The *AuthzFreeCentralAccessPolicyCallback* function is an application-defined function that frees memory allocated by the [*AuthzGetCentralAccessPolicyCallback*](authzgetcentralaccesspolicycallback-.md) function. *AuthzFreeCentralAccessPolicyCallback* is a placeholder for the application-defined function name.

## Syntax


```C++
BOOL CALLBACK AuthzFreeCentralAccessPolicyCallback(
  _In_ PVOID pCentralAccessPolicy
);
```



## Parameters

<dl> <dt>

*pCentralAccessPolicy* \[in\]
</dt> <dd>

Pointer to the central access policy to be freed.

</dd> </dl>

## Return value

If the function succeeds, the function returns **TRUE**.

If the function is unable to perform the evaluation, it returns **FALSE**. Use [**SetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-setlasterror) to return an error to the access check function.

## See also

<dl> <dt>

[**AUTHZ\_INIT\_INFO**](/windows/desktop/api/Authz/ns-authz-authz_init_info)
</dt> <dt>

[*AuthzGetCentralAccessPolicyCallback*](authzgetcentralaccesspolicycallback-.md)
</dt> </dl>

 

 
