---
title: Example Code for Using LDAP VLV
description: The following code example shows how to create and use a VLV control in LDAP.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'd4c4f5ca-13a2-45f6-8b4f-2ff0cb67eb8d'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Example Code for Using LDAP VLV"]
---

# Example Code for Using LDAP VLV

The following code example shows how to create and use a VLV control in LDAP.


```C++
//  Add Wldap32.lib to your project.
//  Add Wldap32.dll to your project.

#include "stdafx.h"
#define SECURITY_WIN32
#include "windows.h"
#include "stdio.h"
#include "winldap.h"
#include "rpc.h"
#include "rpcdce.h"
#include "security.h"
#include "stdio.h"
const size_t newsize = 100;

//  Entry point for application
void __cdecl main (int argc, char* argv[])
{
    PWCHAR hostName = NULL;
    LDAP* pLdapConnection = NULL;
    ULONG version = LDAP_VERSION3;
    ULONG ldapErr;
    INT returnCode = 0;
    ULONG connectSuccess = 0;

    //  Pass in the host name. If no host name 
    //  was passed, set the pointer to NULL to use serverless
    //  binding.
    if (argc > 1)
    {
        //  Convert argv[] to a wchar_t*
        size_t origsize = strlen(argv[1]) + 1;
        size_t convertedChars = 0;
        wchar_t wcstring[newsize];
        mbstowcs_s(&amp;convertedChars, wcstring, origsize, argv[1], _TRUNCATE);
        wcscat_s(wcstring, L" (wchar_t *)");
        hostName = wcstring;
    }
    else
    {
        hostName = NULL;
    }

    //  Initialize a session. LDAP_PORT is the default port, 389.
    pLdapConnection = ldap_init(hostName, LDAP_PORT);

    if (pLdapConnection == NULL)
    {
        //  Set the HRESULT based on the Windows error code.
        char hr = HRESULT_FROM_WIN32(GetLastError());
        printf("ldap_init failed with 0x%x.\n",hr);
        goto error_exit;
    }
    else
        printf("ldap_init succeeded \n");

    //  Set the version to 3.0 (default is 2.0).
    returnCode = ldap_set_option(pLdapConnection,
                                 LDAP_OPT_PROTOCOL_VERSION,
                                 (void*)&amp;version);
    if(returnCode != LDAP_SUCCESS)
    {
        printf("SetOption Error:%0X\n", version);
        goto error_exit;
    }

    // Connect to the server.
    connectSuccess = ldap_connect(pLdapConnection, NULL);
    if(connectSuccess != LDAP_SUCCESS)
    {
        printf("ldap_connect failed with 0x%x.\n",connectSuccess);
        goto error_exit;
    }

    //  Bind with current credentials (login credentials). Be
    //  aware that the password itself is never sent over the 
    //  network, and encryption is not used.
    returnCode = ldap_bind_s(pLdapConnection, NULL, NULL,
                             LDAP_AUTH_NEGOTIATE);
    if (returnCode != LDAP_SUCCESS)
    {
        goto error_exit;
    }

    //  Create the VLV control and send it to the server.
    LDAPVLVInfo     vlvInfo;
    PLDAPControl    pvlvCtrl;
    PLDAPControl    psortCtrl;
    PLDAPControl    ctrlArr[3];

    //  Enter the members of the VLV control.
    vlvInfo.ldvlv_after_count = 1;
    vlvInfo.ldvlv_attrvalue = NULL;
    vlvInfo.ldvlv_before_count = 1;
    vlvInfo.ldvlv_context = NULL;
    vlvInfo.ldvlv_count = 0;
    vlvInfo.ldvlv_extradata = NULL;
    vlvInfo.ldvlv_offset = 2;
    vlvInfo.ldvlv_version = LDAP_VLVINFO_VERSION;

    ldapErr = ldap_create_vlv_control(pLdapConnection,
                                      &amp;vlvInfo,
                                      TRUE,
                                      &amp;pvlvCtrl);

    printf("Create VLV control returned 0x%x\n",ldapErr);
    if (LDAP_SUCCESS != ldapErr)
    return;

    //  Create a sort control and attach it.
    LDAPSortKey sortkeys;
    PLDAPSortKey sortkeyList[2];

    sortkeys.sk_attrtype = L"name";
    sortkeys.sk_matchruleoid = NULL;
    sortkeys.sk_reverseorder = FALSE;

    sortkeyList[0] = &amp;sortkeys;
    sortkeyList[1] = NULL;

    ldapErr = ldap_create_sort_control(pLdapConnection,
                                      sortkeyList,
                                      TRUE,
                                      &amp;psortCtrl);

    printf("Create Sort control returned 0x%x\n",ldapErr);
    if (LDAP_SUCCESS != ldapErr)
    return;

    //  Send the VLV control, with a search request, to the server.
    ctrlArr[0] = psortCtrl;
    ctrlArr[1] = pvlvCtrl;
    ctrlArr[2] = NULL;
    PLDAPMessage pRes;

    ldapErr = ldap_search_ext_s(pLdapConnection,
                                L"OU=Users,DC=DCname,DC=Fabrikam,DC=com",
                                LDAP_SCOPE_SUBTREE,
                                L"objectClass=*",
                                NULL,
                                1,
                                ctrlArr,
                                NULL,
                                NULL,
                                0,
                                &amp;pRes);

    printf("Ldap search returned 0x%x\n",ldapErr);
   
    //  Choose the control returned from the server.
    PLDAPControl *pvlvResponse = NULL;
    ldapErr = ldap_parse_result(pLdapConnection,
                                pRes,
                                NULL,
                                NULL,
                                NULL,
                                NULL,
                                &amp;pvlvResponse,
                                FALSE);

    printf("Ldap parse_result returned 0x%x\n",ldapErr);

    //  Parse the VLV control returned from the server.
    ULONG   targetPos =0;
    ULONG   listCount = 0;
    int     errCode = LDAP_SUCCESS;
    PBERVAL context = NULL;


    ldapErr = ldap_parse_vlv_control(pLdapConnection,
                                     pvlvResponse,
                                     &amp;targetPos,
                                     &amp;listCount,
                                     &amp;context,
                                     &amp;errCode);

    printf("Ldap parse vlv control returned 0x%x\n",ldapErr);
    printf("TargetPos = %d\n", targetPos);
    printf("ListCount = %d\n", listCount);
    printf("errcode = 0x%x\n", errCode);

    //  Free resources
    ldap_unbind(pLdapConnection);
    ldap_control_free(pvlvCtrl);
    ldap_control_free(psortCtrl);
    ldap_msgfree(pRes);
    ldap_controls_free(pvlvResponse);
    ber_bvfree(context);

    return;

    // On error perform normal cleanup, set return flag to error, and exit.
    error_exit:
    ldap_unbind(pLdapConnection);
    return;
}
```



 

 




