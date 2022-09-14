---
title: Looking Up a User's Full Name
description: Computers can be organized into a domain, which is a collection of computers network. The domain administrator maintains centralized user and group account information.
ms.assetid: 296ecfd0-1b65-482c-bee1-eff2130cc14e
ms.topic: article
ms.date: 05/31/2018
---

# Looking Up a User's Full Name

Computers can be organized into a *domain*, which is a collection of computers network. The domain administrator maintains centralized user and group account information.

To find the full name of a user, given the user name and domain name:

-   Convert the user name and domain name to Unicode, if they are not already Unicode strings.
-   Look up the computer name of the domain controller (DC) by calling [**NetGetDCName**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgetdcname).
-   Look up the user name on the DC computer by calling [**NetUserGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetinfo).
-   Convert the full user name to ANSI, unless the program is expecting to work with Unicode strings.

The following sample code is a function (GetFullName) that takes a user name and a domain name in the first two arguments and returns the user's full name in the third argument.


```C++
#include <windows.h>
#include <lm.h>
#include <stdio.h>

#pragma comment(lib, "netapi32.lib")

BOOL GetFullName( char *UserName, char *Domain, char *dest )
{
    WCHAR wszUserName[UNLEN+1];          // Unicode user name
    WCHAR wszDomain[256]; 
    LPBYTE ComputerName;
    
//    struct _SERVER_INFO_100 *si100;  // Server structure
    struct _USER_INFO_2 *ui;         // User structure

// Convert ANSI user name and domain to Unicode

    MultiByteToWideChar( CP_ACP, 0, UserName,
        (int) strlen(UserName)+1, wszUserName, 
        sizeof(wszUserName)/sizeof(WCHAR) );

    MultiByteToWideChar( CP_ACP, 0, Domain,
        (int) strlen(Domain)+1, wszDomain, 
        sizeof(wszDomain)/sizeof(WCHAR) );

// Get the computer name of a DC for the domain.

    NetGetDCName( NULL, wszDomain, &ComputerName );

// Look up the user on the DC.

    if( NetUserGetInfo( (LPWSTR) ComputerName,
        (LPWSTR) &wszUserName, 2, (LPBYTE *) &ui ) )
    {
        wprintf( L"Error getting user information.\n" );
        return( FALSE );
    }

// Convert the Unicode full name to ANSI.

    WideCharToMultiByte( CP_ACP, 0, ui->usri2_full_name, -1,
        dest, 256, NULL, NULL );

    return (TRUE);
}
```



 

 




