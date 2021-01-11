---
description: The following example uses the OpenProcessToken and GetTokenInformation functions to get the group memberships in an access token.
ms.assetid: f895dfef-75ad-419c-95d0-6480bdf9c769
title: Searching for a SID in an Access Token in C++
ms.topic: article
ms.date: 05/31/2018
---

# Searching for a SID in an Access Token in C++

The following example uses the [**OpenProcessToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocesstoken) and [**GetTokenInformation**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) functions to get the group memberships in an [*access token*](/windows/desktop/SecGloss/a-gly). Then it uses the [**AllocateAndInitializeSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-allocateandinitializesid) function to create a SID that identifies the well-known SID of the administrator group for the local computer. Next, it uses the [**EqualSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-equalsid) function to compare the well-known SID with the group SIDs from the access token. If the SID is present in the token, the function checks the attributes of the SID to determine whether it is enabled.

The [**CheckTokenMembership**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-checktokenmembership) function should be used to determine whether a specified SID is present and enabled in an access token. This function eliminates potential misinterpretations of the active group membership.


```C++
#include <windows.h>
#include <stdio.h>
#pragma comment(lib, "advapi32.lib")

#define MAX_NAME 256

BOOL SearchTokenGroupsForSID (VOID) 
{
    DWORD i, dwSize = 0, dwResult = 0;
    HANDLE hToken;
    PTOKEN_GROUPS pGroupInfo;
    SID_NAME_USE SidType;
    char lpName[MAX_NAME];
    char lpDomain[MAX_NAME];
    PSID pSID = NULL;
    SID_IDENTIFIER_AUTHORITY SIDAuth = SECURITY_NT_AUTHORITY;
       
    // Open a handle to the access token for the calling process.

    if (!OpenProcessToken( GetCurrentProcess(), TOKEN_QUERY, &hToken )) 
    {
        printf( "OpenProcessToken Error %u\n", GetLastError() );
        return FALSE;
    }

    // Call GetTokenInformation to get the buffer size.

    if(!GetTokenInformation(hToken, TokenGroups, NULL, dwSize, &dwSize)) 
    {
        dwResult = GetLastError();
        if( dwResult != ERROR_INSUFFICIENT_BUFFER ) {
            printf( "GetTokenInformation Error %u\n", dwResult );
            return FALSE;
        }
    }

    // Allocate the buffer.

    pGroupInfo = (PTOKEN_GROUPS) GlobalAlloc( GPTR, dwSize );

    // Call GetTokenInformation again to get the group information.

    if(! GetTokenInformation(hToken, TokenGroups, pGroupInfo, 
                            dwSize, &dwSize ) ) 
    {
        printf( "GetTokenInformation Error %u\n", GetLastError() );
        return FALSE;
    }

    // Create a SID for the BUILTIN\Administrators group.

    if(! AllocateAndInitializeSid( &SIDAuth, 2,
                     SECURITY_BUILTIN_DOMAIN_RID,
                     DOMAIN_ALIAS_RID_ADMINS,
                     0, 0, 0, 0, 0, 0,
                     &pSID) ) 
    {
        printf( "AllocateAndInitializeSid Error %u\n", GetLastError() );
        return FALSE;
    }

    // Loop through the group SIDs looking for the administrator SID.

    for(i=0; i<pGroupInfo->GroupCount; i++) 
    {
        if ( EqualSid(pSID, pGroupInfo->Groups[i].Sid) ) 
        {

            // Lookup the account name and print it.

            dwSize = MAX_NAME;
            if( !LookupAccountSid( NULL, pGroupInfo->Groups[i].Sid,
                                  lpName, &dwSize, lpDomain, 
                                  &dwSize, &SidType ) ) 
            {
                dwResult = GetLastError();
                if( dwResult == ERROR_NONE_MAPPED )
                   strcpy_s (lpName, dwSize, "NONE_MAPPED" );
                else 
                {
                    printf("LookupAccountSid Error %u\n", GetLastError());
                    return FALSE;
                }
            }
            printf( "Current user is a member of the %s\\%s group\n", 
                    lpDomain, lpName );

            // Find out whether the SID is enabled in the token.
            if (pGroupInfo->Groups[i].Attributes & SE_GROUP_ENABLED)
                printf("The group SID is enabled.\n");
            else if (pGroupInfo->Groups[i].Attributes & 
                              SE_GROUP_USE_FOR_DENY_ONLY)
                printf("The group SID is a deny-only SID.\n");
            else 
                printf("The group SID is not enabled.\n");
        }
    }

    if (pSID)
        FreeSid(pSID);
    if ( pGroupInfo )
        GlobalFree( pGroupInfo );
    return TRUE;
}
```



 

 
