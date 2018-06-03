---
title: Example Code for Displaying Extended Controls Support
description: The following code example queries an LDAP server for extended control support, and prints a list to the console window.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 076562a6-edc9-4e5d-9e7c-9b1077aa006b
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Example Code for Displaying Extended Controls Support LDAP
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Displaying Extended Controls Support

The following code example queries an LDAP server for extended control support, and prints a list to the console window. If an error occurs it prints the hex value of the LDAP error instead. For more information and a list of error code values, see [Return Values](return-values.md).


```C++
//  Add Wldap32.lib to your project.
//  Add Wldap32.dll to your project.

#ifndef _UNICODE
#define _UNICODE
#endif
#include "stdafx.h"
#include "stdio.h"
#include "windows.h"
#include "winldap.h"
const size_t newsize = 100;

//  ULONG GetSupportedLdapControls(PCHAR hostName, PCHAR** ppValList)
//       [in] hostName      LDAP server name
//       [out] ppValList    Null-terminated array of control OIDs.
//
//  This function queries an LDAP server for a list of its
//  supported extended controls. If successful, it returns
//  LDAP_SUCCESS and an array of control OIDs.
//
//  The array returned in the pValList pointer must be freed with
//  ldap_value_free() when no longer required.
ULONG GetSupportedLdapControls(PWCHAR hostName, PWCHAR** ppValList)
{
    ULONG version = LDAP_VERSION3;
    ULONG returnCode = LDAP_SUCCESS;;
    LDAP* pLdapConnection = NULL;
    LDAPMessage* pMessage = NULL;
    LDAPMessage* pEntry = NULL;
    INT connectSuccess = 0;

    //  Initialize return value to NO CONTROLS SUPPORTED
    *ppValList = NULL;

    while(1)
    {
        //  Initialize a new LDAP session.
        pLdapConnection = ldap_init(hostName,LDAP_PORT);
        if(pLdapConnection == NULL)
        {
            returnCode = LdapGetLastError();
            if(returnCode == LDAP_SUCCESS)
                returnCode = LDAP_OTHER;
            break;
        }

        //  Use Version 3 support.
        returnCode = ldap_set_option(pLdapConnection,LDAP_OPT_VERSION,(void*)&amp;version);
        if(returnCode != LDAP_SUCCESS)
            break;

        //  Connect to the server.
        connectSuccess = ldap_connect(pLdapConnection, NULL);
        if(connectSuccess != LDAP_SUCCESS)
            break;

        //  Bind with current credentials.
        returnCode = ldap_bind_s(pLdapConnection,NULL,NULL,LDAP_AUTH_NEGOTIATE);
        if (returnCode != LDAP_SUCCESS)
            break;

        //  Get the RootDSE attributes.
        returnCode = ldap_search_s(pLdapConnection,
                                   L"",
                                   LDAP_SCOPE_BASE,
                                   L"(objectClass=*)",
                                   NULL,
                                   0,
                                   &amp;pMessage);
        if(returnCode != LDAP_SUCCESS)
            break;

        //  Return the support controls.
        pEntry = ldap_first_entry(pLdapConnection, pMessage);
        if(pEntry != NULL)
        {
            *ppValList = ldap_get_values(pLdapConnection,
                                         pEntry,
                                         L"supportedControl");
            break;
        }
        //  Perform cleanup.
        if(pMessage != NULL)
            ldap_msgfree(pMessage);
        if(pLdapConnection != NULL)
            ldap_unbind_s(pLdapConnection);
        return returnCode;
    }
}

//  Entry point for application
int main(int argc, char* argv[])
{
    PWCHAR* pValueList;
    ULONG returnCode;
    PWCHAR hostName = NULL;

    if (argc > 1)
    {
        //  Convert argv[] to a wchar_t*
        size_t origsize = strlen(argv[1]) + 1;
        const size_t newsize = 100;
        size_t convertedChars = 0;
        wchar_t wcstring[newsize];
        mbstowcs_s(&amp;convertedChars, wcstring, origsize, argv[1], _TRUNCATE);
        wcscat_s(wcstring, L" (wchar_t *)");
        hostName = wcstring;
    }

    //  Use the function to retrieve a list of control OIDs.
    returnCode = GetSupportedLdapControls(hostName, &amp;pValueList);
    if(returnCode == LDAP_SUCCESS)
    {
        PWCHAR* pV = pValueList;
        printf("Extended Controls Supported:\n");
        while(*pV)
        {
            printf("    %s\n",*pV);
            pV++;
        }
        if(pValueList != NULL)
            ldap_value_free(pValueList);
    }
    else
        printf("ERROR: code = 0x%0lX\n",returnCode);
    return 0;
}
```



 

 




