---
title: Creating a Local Group and Adding a User
description: To create a new local group, call the NetLocalGroupAdd function. To add a user to that group, call the NetLocalGroupAddMembers function.
ms.assetid: 28bba4bd-5e6b-4139-8fd0-a00fb6e82902
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Local Group and Adding a User

To create a new local group, call the [**NetLocalGroupAdd**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupadd) function. To add a user to that group, call the [**NetLocalGroupAddMembers**](/windows/desktop/api/Lmaccess/nf-lmaccess-netlocalgroupaddmembers) function.

The following program allows you to create a user and a local group and add the user to the local group.


```C++
#ifndef UNICODE
#define UNICODE
#endif 

#include <windows.h>
#include <lmcons.h>
#include <lmaccess.h>
#include <lmerr.h>
#include <lmapibuf.h>
#include <stdio.h>
#include <stdlib.h>

#pragma comment(lib, "netapi32.lib")

NET_API_STATUS NetSample( LPWSTR lpszDomain,
                          LPWSTR lpszUser,
                          LPWSTR lpszPassword,
                          LPWSTR lpszLocalGroup )
{

    USER_INFO_1               user_info;
    LOCALGROUP_INFO_1         localgroup_info;
    LOCALGROUP_MEMBERS_INFO_3 localgroup_members;
    LPWSTR                    lpszPrimaryDC = NULL;
    NET_API_STATUS            err = 0;
    DWORD                     parm_err = 0;

// First get the name of the primary domain controller. 
// Be sure to free the returned buffer. 

    err = NetGetDCName( NULL,                    // local computer 
                   lpszDomain,                   // domain name 
                   (LPBYTE *) &lpszPrimaryDC );  // returned PDC 

    if ( err != 0 )
    {
        printf( "Error getting DC name: %d\n", err );
        return( err );
    }

// Set up the USER_INFO_1 structure. 

    user_info.usri1_name = lpszUser;
    user_info.usri1_password = lpszPassword;
    user_info.usri1_priv = USER_PRIV_USER;
    user_info.usri1_home_dir = TEXT("");
    user_info.usri1_comment = TEXT("Sample User");
    user_info.usri1_flags = UF_SCRIPT;
    user_info.usri1_script_path = TEXT("");

    err = NetUserAdd( lpszPrimaryDC,        // PDC name 
                      1,                    // level 
                      (LPBYTE) &user_info,  // input buffer 
                      &parm_err );          // parameter in error 

    switch ( err )
    {
    case 0:
        printf("User successfully created.\n");
        break;
    case NERR_UserExists:
        printf("User already exists.\n");
        err = 0;
        break;
    case ERROR_INVALID_PARAMETER:
        printf("Invalid parameter error adding user; parameter index = %d\n",
                parm_err);
        NetApiBufferFree( lpszPrimaryDC );
        return( err );
    default:
        printf("Error adding user: %d\n", err);
        NetApiBufferFree( lpszPrimaryDC );
        return( err );
    }

// Set up the LOCALGROUP_INFO_1 structure. 

    localgroup_info.lgrpi1_name = lpszLocalGroup;
    localgroup_info.lgrpi1_comment = TEXT("Sample local group.");

    err = NetLocalGroupAdd( lpszPrimaryDC,    // PDC name 
                  1,                          // level 
                  (LPBYTE) &localgroup_info,  // input buffer 
                  &parm_err );                // parameter in error 

    switch ( err )
    {
    case 0:
        printf("Local group successfully created.\n");
        break;
    case ERROR_ALIAS_EXISTS:
        printf("Local group already exists.\n");
        err = 0;
        break;
    case ERROR_INVALID_PARAMETER:
        printf("Invalid parameter error adding local group; parameter index = %d\n",
                err, parm_err);
        NetApiBufferFree( lpszPrimaryDC );
        return( err );
    default:
        printf("Error adding local group: %d\n", err);
        NetApiBufferFree( lpszPrimaryDC );
        return( err );
    }

// Now add the user to the local group. 

    localgroup_members.lgrmi3_domainandname = lpszUser;

    err = NetLocalGroupAddMembers( lpszPrimaryDC,        // PDC name 
                           lpszLocalGroup,               // group name 
                           3,                            // name 
                           (LPBYTE) &localgroup_members, // buffer 
                           1 );                          // count

    switch ( err )
    {
    case 0:
        printf("User successfully added to local group.\n");
        break;
    case ERROR_MEMBER_IN_ALIAS:
        printf("User already in local group.\n");
        err = 0;
        break;
    default:
        printf("Error adding user to local group: %d\n", err);
        break;
    }

    NetApiBufferFree( lpszPrimaryDC );
    return( err );
}

int main()
{
    NET_API_STATUS err = 0;

    printf( "Calling NetSample.\n" );
    err = NetSample( L"SampleDomain",
                     L"SampleUser",
                     L"SamplePswd",
                     L"SampleLG" );
    printf( "NetSample returned %d\n", err );
    return( 0 );
}
```



 

 




