---
description: Find and print the name of the owner of a file.
ms.assetid: b0dbc785-58a7-4f39-ab39-b96abece5b93
title: Finding the Owner of a File Object in C++
ms.topic: article
ms.date: 05/31/2018
---

# Finding the Owner of a File Object in C++

The following example uses the [**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo) and [**LookupAccountSid**](/windows/desktop/api/Winbase/nf-winbase-lookupaccountsida) functions to find and print the name of the owner of a file. The file exists in the current working directory on the local server.


```C++
#include <stdio.h>
#include <windows.h>
#include <tchar.h>
#include "accctrl.h"
#include "aclapi.h"
#pragma comment(lib, "advapi32.lib")

int main(void)
{
DWORD dwRtnCode = 0;
PSID pSidOwner = NULL;
BOOL bRtnBool = TRUE;
LPTSTR AcctName = NULL;
LPTSTR DomainName = NULL;
DWORD dwAcctName = 1, dwDomainName = 1;
SID_NAME_USE eUse = SidTypeUnknown;
HANDLE hFile;
PSECURITY_DESCRIPTOR pSD = NULL;


// Get the handle of the file object.
hFile = CreateFile(
                  TEXT("myfile.txt"),
                  GENERIC_READ,
                  FILE_SHARE_READ,
                  NULL,
                  OPEN_EXISTING,
                  FILE_ATTRIBUTE_NORMAL,
                  NULL);

// Check GetLastError for CreateFile error code.
if (hFile == INVALID_HANDLE_VALUE) {
          DWORD dwErrorCode = 0;

          dwErrorCode = GetLastError();
          _tprintf(TEXT("CreateFile error = %d\n"), dwErrorCode);
          return -1;
}



// Get the owner SID of the file.
dwRtnCode = GetSecurityInfo(
                  hFile,
                  SE_FILE_OBJECT,
                  OWNER_SECURITY_INFORMATION,
                  &pSidOwner,
                  NULL,
                  NULL,
                  NULL,
                  &pSD);

// Check GetLastError for GetSecurityInfo error condition.
if (dwRtnCode != ERROR_SUCCESS) {
          DWORD dwErrorCode = 0;

          dwErrorCode = GetLastError();
          _tprintf(TEXT("GetSecurityInfo error = %d\n"), dwErrorCode);
          return -1;
}

// First call to LookupAccountSid to get the buffer sizes.
bRtnBool = LookupAccountSid(
                  NULL,           // local computer
                  pSidOwner,
                  AcctName,
                  (LPDWORD)&dwAcctName,
                  DomainName,
                  (LPDWORD)&dwDomainName,
                  &eUse);

// Reallocate memory for the buffers.
AcctName = (LPTSTR)GlobalAlloc(
          GMEM_FIXED,
          dwAcctName);

// Check GetLastError for GlobalAlloc error condition.
if (AcctName == NULL) {
          DWORD dwErrorCode = 0;

          dwErrorCode = GetLastError();
          _tprintf(TEXT("GlobalAlloc error = %d\n"), dwErrorCode);
          return -1;
}

    DomainName = (LPTSTR)GlobalAlloc(
           GMEM_FIXED,
           dwDomainName);

    // Check GetLastError for GlobalAlloc error condition.
    if (DomainName == NULL) {
          DWORD dwErrorCode = 0;

          dwErrorCode = GetLastError();
          _tprintf(TEXT("GlobalAlloc error = %d\n"), dwErrorCode);
          return -1;

    }

    // Second call to LookupAccountSid to get the account name.
    bRtnBool = LookupAccountSid(
          NULL,                   // name of local or remote computer
          pSidOwner,              // security identifier
          AcctName,               // account name buffer
          (LPDWORD)&dwAcctName,   // size of account name buffer 
          DomainName,             // domain name
          (LPDWORD)&dwDomainName, // size of domain name buffer
          &eUse);                 // SID type

    // Check GetLastError for LookupAccountSid error condition.
    if (bRtnBool == FALSE) {
          DWORD dwErrorCode = 0;

          dwErrorCode = GetLastError();

          if (dwErrorCode == ERROR_NONE_MAPPED)
              _tprintf(TEXT
                  ("Account owner not found for specified SID.\n"));
          else 
              _tprintf(TEXT("Error in LookupAccountSid.\n"));
          return -1;

    } else if (bRtnBool == TRUE) 

        // Print the account name.
        _tprintf(TEXT("Account owner = %s\n"), AcctName);

    return 0;
}
```



 

 



