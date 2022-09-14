---
description: When a user application requests data from objects on the system through a WMI provider, impersonation means the provider presents credentials that represent the clients security level rather than the providers.
ms.assetid: 6d54f234-45aa-445b-ad50-7d5a9946c134
ms.tgt_platform: multiple
title: Impersonating a Client
ms.topic: article
ms.date: 05/31/2018
---

# Impersonating a Client

When a user application requests data from objects on the system through a WMI provider, impersonation means the provider presents credentials that represent the client's security level rather than the provider's. Impersonation prevents a client from obtaining unauthorized access to information on the system.

The following sections are discussed in this topic:

-   [Registering a Provider for Impersonation](#registering-a-provider-for-impersonation)
-   [Setting Impersonation Levels Within a Provider](#setting-impersonation-levels-within-a-provider)
-   [Maintaining Security Levels in a Provider](#maintaining-security-levels-in-a-provider)
-   [Handling Access Denied Messages in a Provider](#handling-access-denied-messages-in-a-provider)
-   [Reporting Partial Instances](#reporting-partial-instances)
-   [Reporting Partial Enumerations](#reporting-partial-enumerations)
-   [Debugging Your Access Denied Code](#debugging-your-access-denied-code)
-   [Related topics](#related-topics)

WMI typically runs as an administrative service at a high security level, using the LocalServer security context. Using an administrative service gives WMI the means to access privileged information. When calling a provider for information, WMI passes its security identifier (SID) to the provider, enabling the provider to access information at the same high security level.

During the WMI application launch process, the Windows operating system gives the WMI application the security context of the user who began the process. The security context of the user is typically a lower security level than LocalServer, so the user may not have permission to access all of the information available to WMI. When the user application asks for dynamic information, WMI passes the SID of the user to the corresponding provider. If written appropriately, the provider attempts to access information with the user SID, rather than the provider SID.

For the provider to successfully impersonate the client application, the client application and provider must meet the following criteria:

-   The client application must call WMI with a COM connection security level of **RPC\_C\_IMP\_LEVEL\_IMPERSONATE** or **RPC\_C\_IMP\_LEVEL\_DELEGATE**. For more information, see [Maintaining WMI Security](maintaining-wmi-security.md).
-   The provider must register with WMI as an impersonation provider. For more information, see [Registering a Provider for Impersonation](#registering-a-provider-for-impersonation).
-   The provider must switch to the security level of the client application before accessing privileged information. For more information, see [Setting Impersonation Levels Within a Provider](#setting-impersonation-levels-within-a-provider).
-   The provider must correctly handle error conditions if access to this information is denied. For more information, see [Handling Access Denied Messages in a Provider](#handling-access-denied-messages-in-a-provider).

## Registering a Provider for Impersonation

WMI only passes the SID of a client application to providers who have registered as impersonation providers. Enabling a provider to perform impersonation requires that you modify the provider registration process.

The following procedure describes how to register a provider for impersonation. The procedure assumes that you already understand the registration process. For more information about the registration process, see [Registering a Provider](registering-a-provider.md).

**To register a provider for impersonation**

1.  Set the [**ImpersonationLevel**](swbemsecurity-impersonationlevel.md) property of the [**\_\_Win32Provider**](--win32provider.md) class that represents your provider to 1.

    The [**ImpersonationLevel**](swbemsecurity-impersonationlevel.md) property documents whether the provider supports impersonation or not. Setting **ImpersonationLevel** to 0 indicates that the provider does not impersonate the client and performs all requested operations in the same user context as WMI. Setting **ImpersonationLevel** to 1 indicates that the provider uses impersonation calls to check operations performed on behalf of the client.

2.  Set the **PerUserInitialization** property of the same [**\_\_Win32Provider**](--win32provider.md) class to **TRUE**.

> [!Note]  
> If you register a provider with the [**\_\_Win32Provider**](--win32provider.md) property **InitializeAsAdminFirst** set to **TRUE**, then the provider uses the administration-level thread security token only during the initialization phase. While a call to [**CoImpersonateClient**](/windows/win32/api/combaseapi/nf-combaseapi-coimpersonateclient) does not fail, the provider uses the security context of WMI and not of the client.

 

The following code example shows how to register a provider for impersonation.

``` syntax
instance of __Win32Provider
{
    CLSID = "{FD4F53E0-65DC-11d1-AB64-00C04FD9159E}";
    ImpersonationLevel = 1;
    Name = "MS_NT_EVENTLOG_PROVIDER";
    PerUserInitialization = TRUE;
};
```

## Setting Impersonation Levels Within a Provider

If you register a provider with the [**\_\_Win32Provider**](--win32provider.md) class property [**ImpersonationLevel**](swbemsecurity-impersonationlevel.md) set to 1, then WMI calls your provider to impersonate various clients. To handle these calls, use the [**CoImpersonateClient**](/windows/win32/api/combaseapi/nf-combaseapi-coimpersonateclient) and [**CoRevertToSelf**](/windows/win32/api/combaseapi/nf-combaseapi-coreverttoself) COM functions in your implementation of the [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) interface.

The [**CoImpersonateClient**](/windows/win32/api/combaseapi/nf-combaseapi-coimpersonateclient) function allows a server to impersonate the client that made the call. By placing a call to **CoImpersonateClient** into your implementation of [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices), you allow your provider to set the thread token of the provider to match the thread token of the client, and thus impersonate the client. If you do not call **CoImpersonateClient**, your provider executes code at an administrator level of security, thereby creating a potential security vulnerability. If your provider temporarily needs to act as an administrator or perform the access check manually, then call [**CoRevertToSelf**](/windows/win32/api/combaseapi/nf-combaseapi-coreverttoself).

In contrast to [**CoImpersonateClient**](/windows/win32/api/combaseapi/nf-combaseapi-coimpersonateclient), [**CoRevertToSelf**](/windows/win32/api/combaseapi/nf-combaseapi-coreverttoself) is a COM function that handles thread impersonation levels. In this case, **CoRevertToSelf** changes the impersonation level back to the original impersonation setting. In general, the provider is initially an administrator and alternates between **CoImpersonateClient** and **CoRevertToSelf** depending on whether it is making a call that represents the caller or its own calls. It is the responsibility of the provider to place these calls correctly so as not to expose a security hole to the end user. For example, the provider should only call native Windows functions within the impersonated code sequence.

> [!Note]  
> The purpose of [**CoImpersonateClient**](/windows/win32/api/combaseapi/nf-combaseapi-coimpersonateclient) and [**CoRevertToSelf**](/windows/win32/api/combaseapi/nf-combaseapi-coreverttoself) is to set security for a provider. If you determine that your impersonation has failed, you should return an appropriate completion code to WMI through [**IWbemObjectSink::SetStatus**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectsink-setstatus). For more information, see [Handling Access Denied Messages in a Provider](#handling-access-denied-messages-in-a-provider).

 

## Maintaining Security Levels in a Provider

Providers cannot call [**CoImpersonateClient**](/windows/win32/api/combaseapi/nf-combaseapi-coimpersonateclient) one time in an implementation of [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) and assume that the impersonation credentials remain in place for the duration of the provider. Instead, call **CoImpersonateClient** multiple times during the course of an implementation to keep WMI from changing the credentials.

The main concern for setting impersonation for a provider is reentrancy. In this context, reentrancy is when a provider makes a call to WMI for information and waits until WMI calls back into the provider. In essence, the thread of execution leaves the provider code, only to reenter the code at a later date. Reentry is a part of the design of COM, and is generally not a concern. However, when the thread of execution enters WMI, the thread takes on the impersonation levels of WMI. When the thread returns to the provider, you must reset the impersonation levels with another call to [**CoImpersonateClient**](/windows/win32/api/combaseapi/nf-combaseapi-coimpersonateclient).

To protect yourself from security holes in your provider, you should make reentrant calls into WMI only while impersonating the client. That is, calls to WMI should be made after you call [**CoImpersonateClient**](/windows/win32/api/combaseapi/nf-combaseapi-coimpersonateclient) and before you call [**CoRevertToSelf**](/windows/win32/api/combaseapi/nf-combaseapi-coreverttoself). Because **CoRevertToSelf** causes the impersonation to be set to the user level WMI is running, generally LocalSystem, reentrant calls to WMI after calling **CoRevertToSelf** could give the user, and any providers called, a lot more capabilities than they should have.

> [!Note]  
> If you call a system function or another interface method, the call context is not guaranteed to be maintained.

 

## Handling Access Denied Messages in a Provider

Most Access Denied error messages appear when a client requests a class or information to which they do not have access. If the provider returns an Access Denied error message to WMI and WMI passes this on to the client, the client can infer that the information exists. In some situations, this can be a breach of security. Therefore, your provider should not propagate the message to the client. Instead, the set of classes that the provider would have supplied should not be exposed. Similarly, a dynamic instance provider should call to the underlying data source to determine how to deal with Access Denied messages. It is the responsibility of the provider to replicate that philosophy into the WMI environment. For more information, see [Reporting Partial Instances](#reporting-partial-instances) and [Reporting Partial Enumerations](#reporting-partial-enumerations).

When you determine how your provider should handle Access Denied messages, you must write and debug your code. While debugging, it is often convenient to distinguish between a denial due to low impersonation, and a denial due to an error in your code. You can use a simple test in your code to determine the difference. For more information, see [Debugging your Access Denied Code](#debugging-your-access-denied-code).

## Reporting Partial Instances

One common occurrence of an Access Denied message is when WMI cannot provide all the information to fill an instance. For example, a client may have the authority to view a hard disk drive object, but may not have authority to see how much space is available on the hard disk drive itself. Your provider must determine how to handle any situation when the provider cannot completely fill an instance with properties due to an access violation.

WMI does not require a single response to clients that have partial access to an instance. Instead, WMI version 1.x allows the provider one of the following options:

-   Fail the entire operation with **WBEM\_E\_ACCESS\_DENIED** and return no instances.

    Return an error object along with **WBEM\_E\_ACCESS\_DENIED**, to describe the reason for the denial.

-   Return all available properties, and fill unavailable properties with **NULL**.

> [!Note]  
> Make sure that returning **WBEM\_E\_ACCESS\_DENIED** does not create a security hole in your enterprise.

 

## Reporting Partial Enumerations

Another common occurrence of an access violation is when WMI cannot return all of an enumeration. For example, a client may have access to view all of the local network computer objects, but may not have access to view computer objects outside of his domain. Your provider must determine how to handle any situation when an enumeration cannot be completed due to an access violation.

As with an instance provider, WMI does not require a single response to a partial enumeration. Instead, WMI version 1.x allows a provider one of the following options:

-   Return **WBEM\_S\_NO\_ERROR** for all instances that the provider can access.

    If you use this option, the user is not aware that some instances were not available. A number of providers, such as those using Structured Query Language (SQL) with row-level security, return successful partial results using the security level of the caller to define the result set.

-   Fail the entire operation with **WBEM\_E\_ACCESS\_DENIED** and return no instances.

    The provider may optionally include an error object that describes the situation to the client. Note that some providers may access data sources serially and may not encounter denials until partway through the enumeration.

-   Return all of the instances that can be accessed but also return the nonerror status code **WBEM\_S\_ACCESS\_DENIED**.

    The provider should note the denial during enumeration and may continue providing instances, finishing up with the nonerror status code. The provider may also elect to terminate the enumeration at the first denial. The justification for this option is that different providers have different retrieval paradigms. A provider may have already delivered instances before discovering an access violation. Some providers may elect to continue providing other instances and others may wish to terminate.

Due to the structure of COM, you cannot marshal back any information during an error except for an error object. Therefore, you cannot return both information and an error code. If you choose to return information, you must use a nonerror status code instead.

## Debugging Your Access Denied Code

Some applications may use impersonation levels lower than **RPC\_C\_IMP\_LEVEL\_IMPERSONATE**. In this case, most impersonation calls made by the provider for the client application will fail. To successfully design and implement a provider, you must keep this idea in mind.

By default, the only other level of impersonation that can access a provider is **RPC\_C\_IMP\_LEVEL\_IDENTIFY**. In cases where a client application uses **RPC\_C\_IMP\_LEVEL\_IDENTIFY**, [**CoImpersonateClient**](/windows/win32/api/combaseapi/nf-combaseapi-coimpersonateclient) does not return an error code. Instead, the provider impersonates the client for identification purposes only. Therefore, most Windows methods called by the provider will return an access denied message. This is harmless in practice, as users will not be permitted to do anything inappropriate. However, it may be useful during provider development to know whether the client was truly impersonated or not.

The code requires the following references and \#include statements to compile correctly.


```C++
#define _WIN32_DCOM
#include <iostream>
using namespace std;
#include <wbemidl.h>
```



The following code example shows how to determine whether a provider has successfully impersonated a client application.


```C++
DWORD dwImp = 0;
HANDLE hThreadTok;
DWORD dwBytesReturned;
BOOL bRes;

// You must call this before trying to open a thread token!
CoImpersonateClient();

bRes = OpenThreadToken(
    GetCurrentThread(),
    TOKEN_QUERY,
    TRUE,
    &hThreadTok
);

if (bRes == FALSE)
{
    printf("Unable to read thread token (%d)\n", GetLastError());
    return 0;
}

bRes = GetTokenInformation(
    hThreadTok,
    TokenImpersonationLevel, 
    &dwImp,
    sizeof(DWORD),
    &dwBytesReturned
);

if (!bRes)
{
    printf("Unable to read impersonation level\n");
    CloseHandle(hThreadTok);
    return 0;
}

switch (dwImp)
{
case SecurityAnonymous:
    printf("SecurityAnonymous\n");
    break;

case SecurityIdentification:
    printf("SecurityIdentification\n");
    break;

case SecurityImpersonation:
    printf("SecurityImpersonation\n");
    break;

case SecurityDelegation:
    printf("SecurityDelegation\n");
    break;

default:
    printf("Error. Unable to determine impersonation level\n");
    break;
}

CloseHandle(hThreadTok);
```



## Related topics

<dl> <dt>

[Developing a WMI Provider](developing-a-wmi-provider.md)
</dt> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[Securing Your Provider](securing-your-provider.md)
</dt> </dl>

 

 
