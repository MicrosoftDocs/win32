---
description: An application must create a client context before it can use Authz API to perform access checks or auditing.
ms.assetid: 82f207ff-cac4-4e9a-a9e6-ddb3f6c8b30a
title: Initializing a Client Context
ms.topic: article
ms.date: 05/31/2018
---

# Initializing a Client Context

An application must create a client context before it can use Authz API to perform access checks or auditing.

An application must call the [**AuthzInitializeResourceManager**](/windows/desktop/api/Authz/nf-authz-authzinitializeresourcemanager) function to initialize the resource manager. The application can then call one of several functions to create a client context. Additionally, if you are performing access checks or auditing remotely, you must use the [**AuthzInitializeRemoteResourceManager**](/windows/desktop/api/Authz/nf-authz-authzinitializeremoteresourcemanager) function.

To create a client context based on an existing client context, call the [**AuthzInitializeContextFromAuthzContext**](/windows/desktop/api/Authz/nf-authz-authzinitializecontextfromauthzcontext) function.

The [**AuthzInitializeContextFromToken**](/windows/desktop/api/Authz/nf-authz-authzinitializecontextfromtoken) function creates a new client context by using information in a logon token. The [**AuthzInitializeContextFromSid**](/windows/desktop/api/Authz/nf-authz-authzinitializecontextfromsid) function creates a new client context by using the specified [**SID**](/windows/desktop/api/Winnt/ns-winnt-sid).

If possible, call the [**AuthzInitializeContextFromToken**](/windows/desktop/api/Authz/nf-authz-authzinitializecontextfromtoken) function instead of [**AuthzInitializeContextFromSid**](/windows/desktop/api/Authz/nf-authz-authzinitializecontextfromsid). **AuthzInitializeContextFromSid** attempts to retrieve the information available in a logon token had the client actually logged on. An actual logon token provides more information, such as logon type and logon properties, and reflects the behavior of the authentication package used for the logon. The client context created by **AuthzInitializeContextFromToken** uses a logon token, and the resulting client context is more complete and accurate than a client context created by **AuthzInitializeContextFromSid**.

> [!Note]  
> Security attribute variables must be present in the client context if referred to in a conditional expression; otherwise, the conditional expression term referencing them will be evaluated as unknown. For more information on conditional expressions, see the [Security Descriptor Definition Language for Conditional ACEs](security-descriptor-definition-language-for-conditional-aces-.md) topic.

 

## Example

The following example initializes the Authz resource manager and calls the [**AuthzInitializeContextFromToken**](/windows/desktop/api/Authz/nf-authz-authzinitializecontextfromtoken) function to create a client context from the logon token associated with the current process.


```C++
BOOL AuthzInitFromToken(AUTHZ_CLIENT_CONTEXT_HANDLE *phClientContext)
{

    HANDLE                            hToken = NULL;
    LUID                            Luid = {0, 0};

    
    ULONG                            uFlags = 0;


    //Initialize Resource Manager
    if(!AuthzInitializeResourceManager(
        AUTHZ_RM_FLAG_NO_AUDIT,
        NULL,
        NULL,
        NULL,
        L"My Resource Manager",
        &g_hResourceManager
        ))
    {
        printf_s("AuthzInitializeResourceManager failed with %d\n", GetLastError);
        return FALSE;
    }
    

    //Get the current token.

    if(!OpenProcessToken(GetCurrentProcess(), TOKEN_ALL_ACCESS, &hToken))
    {
        printf_s("OpenProcessToken failed with %d\n", GetLastError);
        return FALSE;
    }


    //Initialize the client context

    if(!AuthzInitializeContextFromToken(
        0,
        hToken,
        g_hResourceManager,
        NULL,
        Luid,
        NULL,
        phClientContext
        ))
    {    
        printf_s("AuthzInitializeContextFromToken failed with %d\n", GetLastError);
        return FALSE;
    }

    
    printf_s("Initialized client context. \n");
    return TRUE;

}
```



## Related topics

<dl> <dt>

[Adding SIDs to a Client Context](adding-sids-to-a-client-context.md)
</dt> <dt>

[Caching Access Checks](caching-access-checks.md)
</dt> <dt>

[Checking Access with Authz API](checking-access-with-authz-api.md)
</dt> <dt>

[How AccessCheck Works](how-dacls-control-access-to-an-object.md)
</dt> <dt>

[Querying a Client Context](querying-a-client-context.md)
</dt> <dt>

[Security Descriptor Definition Language for Conditional ACEs](security-descriptor-definition-language-for-conditional-aces-.md)
</dt> <dt>

[**AuthzInitializeRemoteResourceManager**](/windows/desktop/api/Authz/nf-authz-authzinitializeremoteresourcemanager)
</dt> <dt>

[**AuthzInitializeResourceManager**](/windows/desktop/api/Authz/nf-authz-authzinitializeresourcemanager)
</dt> </dl>

 

 



