---
description: When a client application logs on to Windows Management Instrumentation (WMI) for the first time, it must set the default process security level with a call to CoInitializeSecurity.
ms.assetid: 4248fd1b-0867-40d8-8c9c-541156212df8
ms.tgt_platform: multiple
title: Setting the Default Process Security Level Using C++
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Default Process Security Level Using C++

When a client application logs on to Windows Management Instrumentation (WMI) for the first time, it must set the default process security level with a call to [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity). COM uses the information in the call to determine how much security another process must have to access the client application process.

The following sections are discussed in this topic:

-   [Changing the Default Authentication Credentials Using C++](#changing-the-default-authentication-credentials-using-c)
-   [Changing the Default Impersonation Levels Using C++](#changing-the-default-impersonation-levels-using-c)

For most client applications the arguments shown in the following example set the default security for WMI.


```C++
HRESULT hr = NULL;
hr = CoInitializeSecurity(
        NULL,                       // security descriptor
       -1,                          // use this simple setting
       NULL,                        // use this simple setting
       NULL,                        // reserved
       RPC_C_AUTHN_LEVEL_DEFAULT,   // authentication level  
       RPC_C_IMP_LEVEL_IMPERSONATE, // impersonation level
       NULL,                        // use this simple setting
       EOAC_NONE,                   // no special capabilities
       NULL);                          // reserved

if (FAILED(hr))
{
  CoUninitialize();
  cout << "Failed to initialize security. Error code = 0x"
       << hex << hr << endl;
  return;
}
```



The code requires the following references and \#include statements to compile correctly.


```C++
#define _WIN32_DCOM
#include <iostream>
using namespace std;
#include <Wbemidl.h>

#pragma comment(lib, "wbemuuid.lib")
```



Setting the authentication level to **RPC\_C\_AUTHN\_LEVEL\_DEFAULT** allows DCOM to negotiate the authentication level to match the security demands of the target computer. For more information, see [Changing the Default Authentication Credentials Using C++](#changing-the-default-authentication-credentials-using-c) and [Changing the Default Impersonation Settings Using C++](#changing-the-default-impersonation-levels-using-c).

## Changing the Default Authentication Credentials Using C++

The default authentication credentials work for most situations, but you might need to use different authentication credentials in different situations. For example, you might want to add encryption to the authentication procedures.

The following table lists and describes the different levels of authentication.



| Authentication level                 | Description                                                                           |
|--------------------------------------|---------------------------------------------------------------------------------------|
| RPC\_C\_AUTHN\_LEVEL\_DEFAULT        | Default security authentication.                                                      |
| RPC\_C\_AUTHN\_LEVEL\_NONE           | No authentication.                                                                    |
| RPC\_C\_AUTHN\_LEVEL\_CONNECT        | Authentication only when the client creates a relationship with the server.           |
| RPC\_C\_AUTHN\_LEVEL\_CALL           | Authentication each time the server receives an RPC.                                  |
| RPC\_C\_AUTHN\_LEVEL\_PKT            | Authentication each time the server receives data from a client.                      |
| RPC\_C\_AUTHN\_LEVEL\_PKT\_INTEGRITY | Authentication that no data from the packet has been modified.                        |
| RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY   | Includes all previous authentication levels, and encrypts the value of each RPC call. |



 

You can specify the default authentication credentials for multiple users by using a **SOLE\_AUTHENTICATION\_LIST** structure in the *pAuthList* parameter of [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity).

The following code example shows how to change the authentication credentials.


```C++
// Auth Identity structure
SEC_WINNT_AUTH_IDENTITY_W        authidentity;
SecureZeroMemory( &authidentity, sizeof(authidentity) );

authidentity.User = L"MyUser";
authidentity.UserLength = wcslen( authidentity.User );
authidentity.Domain = L"MyDomain ";
authidentity.DomainLength = wcslen( authidentity.Domain );
authidentity.Password = L"";
authidentity.PasswordLength = wcslen( authidentity.Password );
authidentity.Flags = SEC_WINNT_AUTH_IDENTITY_UNICODE;

SecureZeroMemory( authninfo, sizeof(SOLE_AUTHENTICATION_INFO)*2 );

// NTLM Settings
authninfo[0].dwAuthnSvc = RPC_C_AUTHN_WINNT;
authninfo[0].dwAuthzSvc = RPC_C_AUTHZ_NONE;
authninfo[0].pAuthInfo = &authidentity;

// Kerberos Settings
authninfo[1].dwAuthnSvc = RPC_C_AUTHN_GSS_KERBEROS ;
authninfo[1].dwAuthzSvc = RPC_C_AUTHZ_NONE;
authninfo[1].pAuthInfo = &authidentity;

SOLE_AUTHENTICATION_LIST    authentlist;

authentlist.cAuthInfo = 2;
authentlist.aAuthInfo = authninfo;

CoInitializeSecurity( 
  NULL, 
  -1, 
  NULL, 
  NULL, 
  RPC_C_AUTHN_LEVEL_CALL, 
  RPC_C_IMP_LEVEL_IMPERSONATE,
  &authentlist, 
  EOAC_NONE,
  NULL);
```



## Changing the Default Impersonation Levels Using C++

COM provides default security levels read from the system registry. However, unless specifically modified, the registry settings set the impersonation level too low for WMI to function. Typically, the default impersonation level is **RPC\_C\_IMP\_LEVEL\_IDENTIFY**, but WMI needs at least **RPC\_C\_IMP\_LEVEL\_IMPERSONATE** to function with most providers, and you might encounter a situation where you need to set a higher level of impersonation. For more information, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md). The following table lists the different levels of impersonation.



| Level                           | Description                                                                                                   |
|---------------------------------|---------------------------------------------------------------------------------------------------------------|
| RPC\_C\_IMP\_LEVEL\_DEFAULT     | The operating system chooses the level of impersonation.                                                      |
| RPC\_C\_IMP\_LEVEL\_ANONYMOUS   | The server can impersonate the client, but the impersonation token cannot be used for anything.               |
| RPC\_C\_IMP\_LEVEL\_IDENTIFY    | The server can obtain the identity of the client and impersonate the client for ACL checking.                 |
| RPC\_C\_IMP\_LEVEL\_IMPERSONATE | The server can impersonate the client across one computer boundary.                                           |
| RPC\_C\_IMP\_LEVEL\_DELEGATE    | The server can impersonate the client across multiple boundaries, and can make calls on behalf of the client. |



 

 

 
