---
title: Getting and Setting Session Options
description: There are several options that can be read or set prior to binding to an LDAP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1447d242-b8db-4b7e-9871-2193f747be4e
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Getting and Setting Session Options LDAP
- Getting Session Options LDAP
- Setting Session Options LDAP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Getting and Setting Session Options

There are several options that can be read or set prior to binding to an LDAP server. These range from retrieving data about the server to setting up connection parameters. For example, if [**ldap\_get\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_option?branch=master) is called with **LDAP\_OPT\_HOST\_NAME**, it returns the name of the LDAP server to which the connection is made. If [**ldap\_set\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_set_option?branch=master) is called with **LDAP\_SIZELIMIT**, it limits the number of entries to return from a search. If **ldap\_set\_option** is called with **LDAP\_TIMELIMIT**, it sets a limit on the number of seconds the server uses to wait for a bind or search request to complete before performing a timeout.

There are some LDAP directory features only available in LDAP version 3. To verify the latest version supported on the client host, call [**ldap\_get\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_option?branch=master) with **LDAP\_OPT\_API\_INFO**. If version 3 is supported, call [**ldap\_set\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_set_option?branch=master) with **LDAP\_OPT\_PROTOCOL\_VERSION**, and **LDAP\_VERSION3** for the version parameter. The connection default is version 2.

For more information and a complete list of possible LDAP options, see [Session Options](session-options.md).

## Retrieving default session option values

The following code example shows how to retrieve some of the default values for the option settings.


```C++
//  Add Wldap32.lib to your project.
//  Add Wldap32.dll to your project.

#include "stdafx.h"
#include "windows.h"
#include "winldap.h"
#include "stdio.h"
const size_t newsize = 100;

//  Entry point for application
int main(int argc, char* argv[])
{
    PWCHAR hostName = NULL;
    LDAP* pLdapConnection = NULL;
    ULONG option = 0;
    ULONG getOptSuccess = 0;
    ULONG connectSuccess = 0;
    PWCHAR optionChar = NULL;
    LDAPAPIInfo apiInfo;
    LDAPAPIInfo* pApiInfo = &amp;apiInfo;
    INT returnCode = 0;
    ULONG version = LDAP_VERSION3;

    //  Verify that the user passed a hostname.
    if (argc > 1)
    {
        //  Convert argv[] to a wchar_t*
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

    //  Initialize an LDAP session. LDAP_PORT is the default port, 389.
    pLdapConnection = ldap_init(hostName, LDAP_PORT);

    if (pLdapConnection == NULL)
    {
        //  Set the HRESULT based on the Windows error code.
        char hr = HRESULT_FROM_WIN32(GetLastError());
        printf( "ldap_init failed with 0x%x.\n",hr);
    }
    else
        printf("ldap_init succeeded \n");

    //  Connect to the server.
    connectSuccess = ldap_connect(pLdapConnection, NULL);

    if(connectSuccess == LDAP_SUCCESS)
        printf("ldap_connect succeeded \n");
    else
    {
        printf("ldap_connect failed with 0x%x.\n",connectSuccess);
        goto error_exit;
    }

    //  Set the version to 3.0 (default is 2.0).
    returnCode = ldap_set_option(pLdapConnection,
                                 LDAP_OPT_PROTOCOL_VERSION,
                                 (void*)&amp;version);
    if(returnCode != LDAP_SUCCESS)
    {
        printf("SetOption Error:%0X\n", returnCode);
        goto error_exit;
    }

    //  Connect to the server.
    connectSuccess = ldap_connect(pLdapConnection, NULL);

    if(connectSuccess != LDAP_SUCCESS)
    {
        printf("ldap_connect failed with 0x%x.\n",connectSuccess);
        goto error_exit;
    }

    //  Bind with current credentials (login credentials). Be
    //  aware that the password itself is never sent over the 
    //  network, and encryption is not used.
    returnCode = ldap_bind_s(pLdapConnection, 
                             NULL, 
                             NULL,
                             LDAP_AUTH_NEGOTIATE);
    if (returnCode != LDAP_SUCCESS)
    {
        goto error_exit;
    }

    //  Get the current LDAP API information (found in LDAP_OPT_API_INFO).
    pApiInfo->ldapai_info_version = LDAP_API_INFO_VERSION;
    getOptSuccess = ldap_get_option(pLdapConnection,
                                    LDAP_OPT_API_INFO,
                                    (void*) pApiInfo);

    if(getOptSuccess == LDAP_SUCCESS)
    {
        printf("LDAP Revision Number is %d \n", 
            pApiInfo->ldapai_api_version);
        printf("Highest LDAP Version Supported is %d \n", 
            pApiInfo->ldapai_protocol_version);
        printf("The Vendor Name is %s \n", 
            pApiInfo->ldapai_vendor_name);
        printf("The Vendor Version is %d \n", 
            pApiInfo->ldapai_vendor_version);       
    }
    else
    {
        printf("Get LDAP_OPT_API_INFO failed with 0x%x.\n",
               getOptSuccess);
        goto error_exit;
    }

    //  Get LDAP_OPT_AREC_EXCLUSIVE.
    getOptSuccess = ldap_get_option(pLdapConnection,
                                    LDAP_OPT_AREC_EXCLUSIVE,
                                    (void*) &amp;option);

    if(getOptSuccess == LDAP_SUCCESS)
        printf("LDAP_OPT_AREC_EXCLUSIVE is %d \n", option);
    else
    {
        printf("ldap_get_option failed with 0x%x.\n",getOptSuccess);
        goto error_exit;
    }

    //  Get LDAP_OPT_HOST_NAME.
    getOptSuccess = ldap_get_option(pLdapConnection,
        LDAP_OPT_HOST_NAME,
        (void*) &amp;optionChar);

    if(getOptSuccess == LDAP_SUCCESS)
        printf("LDAP_OPT_HOST_NAME is %s \n", optionChar);
    else
    {
        printf("ldap_get_option failed with 0x%x.\n",getOptSuccess);
        goto error_exit;
    }

    //  Get LDAP_OPT_REFERRAL_HOP_LIMIT.
    getOptSuccess = ldap_get_option(pLdapConnection,
                                    LDAP_OPT_REFERRAL_HOP_LIMIT,
                                    (void*) &amp;option);

    if(getOptSuccess == LDAP_SUCCESS)
        printf("LDAP_OPT_REFERRAL_HOP_LIMIT is %d \n", option);
    else
    {
        printf("ldap_get_option failed with 0x%x.\n",getOptSuccess);
        goto error_exit;
    }

    //  Get LDAP_OPT_REFERRALS.
    getOptSuccess = ldap_get_option(pLdapConnection,
                                    LDAP_OPT_REFERRALS,
                                    (void*) &amp;option);

    if(getOptSuccess == LDAP_SUCCESS)
        printf("LDAP_OPT_REFERRALS is %d \n", option);
    else
    {
        printf("ldap_get_option failed with 0x%x.\n",getOptSuccess);
        goto error_exit;
    }

    //  Get LDAP_OPT_SIZELIMIT.
    getOptSuccess = ldap_get_option(pLdapConnection,
                                    LDAP_OPT_SIZELIMIT,
                                    (void*) &amp;option);

    if(getOptSuccess == LDAP_SUCCESS)
        printf("LDAP_OPT_SIZELIMIT is %d \n", option);
    else
    {
        printf("ldap_get_option failed with 0x%x.\n",getOptSuccess);
        goto error_exit;
    }

    //  Get LDAP_OPT_SSL.
    getOptSuccess = ldap_get_option(pLdapConnection,
        LDAP_OPT_SSL,
        (void*) &amp;option);

    if(getOptSuccess == LDAP_SUCCESS)
        printf("LDAP_OPT_SSL is %d \n", option);
    else
    {
        printf("ldap_get_option failed with 0x%x.\n",getOptSuccess);
        goto error_exit;
    }

    //  Get LDAP_OPT_TIMELIMIT.
    getOptSuccess = ldap_get_option(pLdapConnection,
                                    LDAP_OPT_TIMELIMIT,
                                    (void*) &amp;option);

    if(getOptSuccess == LDAP_SUCCESS)
        printf("LDAP_OPT_TIMELIMIT is %d \n", option);
    else
    {
        printf("ldap_get_option failed with 0x%x.\n",getOptSuccess);
        goto error_exit;
    }

    //  Get LDAP_OPT_AUTO_RECONNECT.
    getOptSuccess = ldap_get_option(pLdapConnection,
                                    LDAP_OPT_AUTO_RECONNECT,
                                    (void*) &amp;option);

    if(getOptSuccess == LDAP_SUCCESS)
        printf("LDAP_OPT_AUTO_RECONNECT is %d \n", option);
    else
    {
        printf("ldap_get_option failed with 0x%x.\n",getOptSuccess);
        goto error_exit;
    }

    //  Get LDAP_OPT_PROMPT_CREDENTIALS.
    getOptSuccess = ldap_get_option(pLdapConnection,
                                    LDAP_OPT_PROMPT_CREDENTIALS,
                                    (void*) &amp;option);

    if(getOptSuccess == LDAP_SUCCESS)
        printf("LDAP_OPT_PROMPT_CREDENTIALS is %d \n", option);
    else
    {
        printf("ldap_get_option failed with 0x%x.\n",getOptSuccess);
        goto error_exit;
    }

    //  Perform normal cleanup and exit.
    ldap_unbind(pLdapConnection);
    ldap_memfree(optionChar);

    return 0;

    //  On error perform normal cleanup, set return flag to error, and exit.
error_exit:
    ldap_unbind(pLdapConnection);
    ldap_memfree(optionChar);
    return -1;
}
```



The following list shows the command line output from the preceding code example.

``` syntax
ldap_init succeeded
ldap_connect succeeded
The current LDAP version number is 2
LDAP Revision Number is 2004
Highest LDAP Version Supported is 3
The Vendor Name is Microsoft Corporation.
The Vendor Version is 510
LDAP_OPT_AREC_EXCLUSIVE is 0
LDAP_OPT_HOST_NAME is rhadsidoc.fabrikam.com
LDAP_OPT_REFERRAL_HOP_LIMIT is 32
LDAP_OPT_REFERRALS is 1
LDAP_OPT_SIZELIMIT is 0
LDAP_OPT_SSL is 0
LDAP_OPT_TIMELIMIT is 0
LDAP_OPT_AUTO_RECONNECT is 1
LDAP_OPT_PROMPT_CREDENTIALS is 1
```

 

 




