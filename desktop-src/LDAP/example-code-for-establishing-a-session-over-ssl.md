---
title: Example Code for Establishing a Session over SSL
description: Establishing a secure LDAP connection using SSL, now called Transport Layer Security (TLS), requires that the server support the proper certification authority (CA) before the connection is attempted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'aaf050f5-53a4-4faa-bca9-d2865d14192f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Establishing a Session over SSL LDAP", "Establishing a Session LDAP", "Session, Establishing LDAP"]
---

# Example Code for Establishing a Session over SSL

Establishing a secure LDAP connection using SSL, now called Transport Layer Security (TLS), requires that the server support the proper certification authority (CA) before the connection is attempted. In addition, the client can supply an appropriate client certificate to the server when the SSL handshake is initiated by the connection attempt.

If the client application must determine if a particular connection is protected by SSL at run-time, the [**ldap\_get\_option**](ldap-get-option.md) function can be used with **LDAP\_OPT\_SSL** to return this data. The encryption strength can then be returned using the **LDAP\_OPT\_SSL\_INFO** option. Active Directory requires 128-bit cipher strength to allow user passwords to be modified by client applications using the LDAP provider over an SSL connection.

The following operations are performed in the example code provided:

-   Retrieves a host name. If no host name was supplied by the user then perform a serverless bind.
-   Initializes a session using [**ldap\_sslinit**](ldap-sslinit.md).
-   Specifies LDAP version 3.
-   Verifies that the host supports SSL.
-   Connects to the server.
-   Binds to the server with current credentials.
-   Retrieves the SSL cipher strength.

The following example code shows how to bind to a server using [**ldap\_sslinit**](ldap-sslinit.md), and then queries the server for the cipher strength.


```C++
//  Add Wldap32.lib to your project.
//  Add Wldap32.dll to your project.

//  SSLSESSION: Run the following code example by passing the server name as a
//  command line parameter. If no server name is passed, a serverless bind attempt is performed.
//  Example:
//    sslsession.exe [myserver.fabrikam.com]

#include "stdafx.h"
#include "windows.h"
#include "ntldap.h"
#include "winldap.h"
#include "schnlsp.h"
#include "stdio.h"
#include "tchar.h"
#include "targetver.h"
const size_t newsize = 100;

//  Entry point for your application
int main(int argc, char* argv[])
{
    LDAP* pLdapConnection = NULL;
    INT returnCode = 0; 
    INT connectSuccess = 0;
    PWCHAR hostName = NULL;
    ULONG version = LDAP_VERSION3;
    SecPkgContext_ConnectionInfo sslInfo;
    LONG lv = 0;

    //  Verify that the user passed a hostname.
    if (argc > 1)
    {
        // Convert argv[] to a wchar_t*
        size_t origsize = strlen(argv[1]) + 1;
        size_t convertedChars = 0;
        wchar_t wcstring[newsize];
        mbstowcs_s(&amp;convertedChars, wcstring, origsize, argv[1], _TRUNCATE);
        wcscat_s(wcstring, L" (wchar_t *)");
        hostName = wcstring;
        printf("\nConnecting to host \"%s\" ...\n",hostName);
    }
    //  If not, perform a serverless bind.
    else
    {
        hostName = NULL;
        printf("\nConnecting to DEFAULT LDAP host ...\n");
    }

    //  Initialize an LDAP session using SSL.
    pLdapConnection = ldap_sslinit(hostName,LDAP_SSL_PORT,1);
    if (pLdapConnection == NULL)
    {
        char hr = HRESULT_FROM_WIN32(GetLastError());
        printf( "ldap_sslinit failed with 0x%x.\n",hr);
        return -1;
    }

    //  Specify version 3; the default is version 2.
    printf("Setting Protocol version to 3.\n");
    returnCode = ldap_set_option(pLdapConnection,
        LDAP_OPT_PROTOCOL_VERSION,
        (void*)&amp;version);
    if (returnCode != LDAP_SUCCESS)
        goto FatalExit;

    //  Verify that SSL is enabled on the connection.
    //  (returns LDAP_OPT_ON/_OFF).
    printf("Checking if SSL is enabled\n");
    returnCode = ldap_get_option(pLdapConnection,LDAP_OPT_SSL,(void*)&amp;lv);
    if (returnCode != LDAP_SUCCESS)
        goto FatalExit;

    //  If SSL is not enabled, enable it.
    if ((void*)lv == LDAP_OPT_ON)
        printf("SSL is enabled\n");
    else
    {
        printf("SSL not enabled.\n SSL being enabled...\n");
        returnCode = ldap_set_option(pLdapConnection,LDAP_OPT_SSL,LDAP_OPT_ON);
        if (returnCode != LDAP_SUCCESS)
            goto FatalExit;
    }

    //  Connect to the server.
    connectSuccess = ldap_connect(pLdapConnection, NULL);

    if(connectSuccess == LDAP_SUCCESS)
        printf("ldap_connect succeeded \n");
    else
    {
        printf("ldap_connect failed with 0x%x.\n",connectSuccess);
        goto FatalExit;
    }

    //  Bind with current credentials. 
    printf("Binding ...\n");
    returnCode = ldap_bind_s(pLdapConnection,NULL,NULL,LDAP_AUTH_NEGOTIATE);
    if (returnCode != LDAP_SUCCESS)
        goto FatalExit;

    //  Retrieve the SSL cipher strength.
    printf("Getting SSL info\n");
    returnCode = ldap_get_option(pLdapConnection,LDAP_OPT_SSL_INFO,&amp;sslInfo);
    if (returnCode != LDAP_SUCCESS)
        goto FatalExit;

    printf("SSL cipher strength = %d bits\n",sslInfo.dwCipherStrength);

    goto NormalExit;

    //  Perform cleanup.
NormalExit:
    if (pLdapConnection != NULL)
        ldap_unbind_s(pLdapConnection);
    return 0;

    //  Perform cleanup after an error.
FatalExit:
    if( pLdapConnection != NULL )
        ldap_unbind_s(pLdapConnection);
    printf( "\n\nERROR: 0x%x\n", returnCode);
    return returnCode;
}
```



The Microsoft LDAP server software enables the [Schannel](_com_schannel) security package to select the server certificate used to authenticate an SSL connection. Schannel uses the first valid certificate it locates that has all of the following properties:

-   Has the "server auth" Extended Key Usage (EKU).
-   Contains the fully qualified domain name (FQDN) of the server computer, either in the subject CN field or in the subject alt name extension.
-   Is located in the local computer personal certificate store, which is known programmatically as the MY certificate store.
-   Was issued from a trusted CA, within the scope of the computer or the computer domain.

Enabling SSL from the server side is host-dependent and should be detailed in the host administration guide. The following is an outline of requirements for setting up SSL on a Windows Server Domain Controller using the Microsoft Enterprise Certificate Authority:

1.  Install an Enterprise Certificate Authority on a Windows Server Domain Controller, which installs a certificate on a server, or install a third-party certificate on the Domain Controller.
2.  Open the Default Domain Controller Policy using the Group Policy Editor.
3.  Select Windows Settings under Computer Configuration.
4.  Select Security Settings, and then select Public Key Policies.
5.  Select Automatic Certificate Request Settings.
6.  Use the wizard to add a policy for Domain Controllers.

When these requirements are completed, all domain controllers request a certificate and support LDAP over SSL using port 636.

If a third-party certificate is required for LDAP SSL connections, then it is important that the Microsoft Enterprise Certificate Authority not be installed on the LDAP server; this sets the Enterprise CA certificate as the default certificate for SSL validation.

 

 




