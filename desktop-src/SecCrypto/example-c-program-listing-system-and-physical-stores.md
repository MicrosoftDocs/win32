---
description: Enumerates the system certificate store locations, the system certificate stores, and the physical stores associated with each system store.
ms.assetid: bc4268ea-f657-4789-9d0a-6e5354508f86
title: 'Example C Program: Listing System and Physical Stores'
ms.topic: article
ms.date: 05/31/2018
---

# Example C Program: Listing System and Physical Stores

The following example enumerates the system [*certificate store*](../secgloss/c-gly.md) locations, the system certificate stores, and the physical stores associated with each system store. This example demonstrates the creation of callback functions and callback functions that call other callback functions.

This example illustrates the following [*CryptoAPI*](../secgloss/c-gly.md) functions:

-   [**CertEnumSystemStoreLocation**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumsystemstorelocation)
-   [**CertEnumSystemStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumsystemstore)

This example also uses the function [**MyHandleError**](myhandleerror.md). Code for this function is included with the sample. Code for this and other auxiliary functions is also listed under [General Purpose Functions](general-purpose-functions.md).


```C++
#include <stdio.h>
#include <windows.h>
#include <Wincrypt.h>
#define MY_ENCODING_TYPE  (PKCS_7_ASN_ENCODING | X509_ASN_ENCODING)
void MyHandleError(char *s);
#pragma comment(lib, "crypt32.lib")

typedef struct _ENUM_ARG {
    BOOL        fAll;
    BOOL        fVerbose;
    DWORD       dwFlags;
    const void  *pvStoreLocationPara;
    HKEY        hKeyBase;
} ENUM_ARG, *PENUM_ARG;

//-------------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
// Declare callback functions. 
// Definitions of these functions follow main.

static BOOL WINAPI EnumPhyCallback(
       const void *pvSystemStore,
       DWORD dwFlags, 
       LPCWSTR pwszStoreName, 
       PCERT_PHYSICAL_STORE_INFO pStoreInfo,
       void *pvReserved, 
       void *pvArg);

static BOOL WINAPI EnumSysCallback(
       const void *pvSystemStore,
       DWORD dwFlags,
       PCERT_SYSTEM_STORE_INFO pStoreInfo,
       void *pvReserved,
       void *pvArg);

static BOOL WINAPI EnumLocCallback(
       LPCWSTR pwszStoreLocation,
       DWORD dwFlags,
       void *pvReserved,
       void *pvArg);

//-------------------------------------------------------------------
// Begin main.

void main(void) 
{
//-------------------------------------------------------------------
// Declare and initialize variables.

DWORD dwExpectedError = 0;
DWORD dwLocationID = CERT_SYSTEM_STORE_CURRENT_USER_ID;
DWORD dwFlags = 0;
CERT_PHYSICAL_STORE_INFO PhyStoreInfo;
ENUM_ARG EnumArg;
LPSTR pszStoreParameters = NULL;          
LPWSTR pwszStoreParameters = NULL;
LPWSTR pwszSystemName = NULL;
LPWSTR pwszPhysicalName = NULL;
LPWSTR pwszStoreLocationPara = NULL;
void *pvSystemName;                   
void *pvStoreLocationPara;              
DWORD dwNameCnt = 0;
LPCSTR pszTestName;
HKEY hKeyRelocate = HKEY_CURRENT_USER;
LPSTR pszRelocate = NULL;               
HKEY hKeyBase = NULL;

//-------------------------------------------------------------------
//  Initialize data structure variables.

memset(&PhyStoreInfo, 0, sizeof(PhyStoreInfo));
PhyStoreInfo.cbSize = sizeof(PhyStoreInfo);
PhyStoreInfo.pszOpenStoreProvider = sz_CERT_STORE_PROV_SYSTEM_W;
pszTestName = "Enum";  
pvSystemName = pwszSystemName;
pvStoreLocationPara = pwszStoreLocationPara;

memset(&EnumArg, 0, sizeof(EnumArg));
EnumArg.dwFlags = dwFlags;
EnumArg.hKeyBase = hKeyBase;

EnumArg.pvStoreLocationPara = pvStoreLocationPara;
EnumArg.fAll = TRUE;
dwFlags &= ~CERT_SYSTEM_STORE_LOCATION_MASK;
dwFlags |= (dwLocationID << CERT_SYSTEM_STORE_LOCATION_SHIFT) &
    CERT_SYSTEM_STORE_LOCATION_MASK;

printf("Begin enumeration of store locations. \n");
if(CertEnumSystemStoreLocation(
    dwFlags,
    &EnumArg,
    EnumLocCallback
    ))
{
    printf("\nFinished enumerating locations. \n");
}
else
{
    MyHandleError("Enumeration of locations failed.");
}
printf("\nBegin enumeration of system stores. \n");

if(CertEnumSystemStore(
    dwFlags,
    pvStoreLocationPara,
    &EnumArg,
    EnumSysCallback
    ))
{
    printf("\nFinished enumerating system stores. \n");
}
else
{
    MyHandleError("Enumeration of system stores failed.");
}

printf("\n\nEnumerate the physical stores "
    "for the MY system store. \n");
if(CertEnumPhysicalStore(
    L"MY",
    dwFlags,
    &EnumArg,
    EnumPhyCallback
    ))
{
    printf("Finished enumeration of the physical stores. \n");
}
else
{
    MyHandleError("Enumeration of physical stores failed.");
}
}    //   End of main

//-------------------------------------------------------------------
//   Define function GetSystemName.

static BOOL GetSystemName( 
    const void *pvSystemStore,
    DWORD dwFlags, 
    PENUM_ARG pEnumArg, 
    LPCWSTR *ppwszSystemName )
{
//-------------------------------------------------------------------
// Declare local variables.

*ppwszSystemName = NULL;

if (pEnumArg->hKeyBase && 0 == (dwFlags & 
    CERT_SYSTEM_STORE_RELOCATE_FLAG)) 
{
  printf("Failed => RELOCATE_FLAG not set in callback. \n");
  return FALSE;
} 
else 
{
  if (dwFlags & CERT_SYSTEM_STORE_RELOCATE_FLAG) 
  {
     PCERT_SYSTEM_STORE_RELOCATE_PARA pRelocatePara;
     if (!pEnumArg->hKeyBase) 
     {
        MyHandleError("Failed => RELOCATE_FLAG is set in callback");
     }
     pRelocatePara = (PCERT_SYSTEM_STORE_RELOCATE_PARA) 
         pvSystemStore;
     if (pRelocatePara->hKeyBase != pEnumArg->hKeyBase) 
     {
         MyHandleError("Wrong hKeyBase passed to callback");
     }
     *ppwszSystemName = pRelocatePara->pwszSystemStore;
  } 
  else
  {
    *ppwszSystemName = (LPCWSTR) pvSystemStore;
  }
}
return TRUE;
}

//-------------------------------------------------------------------
// Define the callback functions.

static BOOL WINAPI EnumPhyCallback(
      const void *pvSystemStore,
      DWORD dwFlags, 
      LPCWSTR pwszStoreName, 
      PCERT_PHYSICAL_STORE_INFO pStoreInfo,
      void *pvReserved, 
      void *pvArg )
{
//-------------------------------------------------------------------
//  Declare and initialize local variables.
PENUM_ARG pEnumArg = (PENUM_ARG) pvArg;
LPCWSTR pwszSystemStore;

//-------------------------------------------------------------------
//  Begin callback process.

if (GetSystemName(
       pvSystemStore, 
       dwFlags, 
       pEnumArg, 
       &pwszSystemStore))
{
printf("    %S", pwszStoreName);
}
else
{
   MyHandleError("GetSystemName failed.");
}
if (pEnumArg->fVerbose &&
      (dwFlags & CERT_PHYSICAL_STORE_PREDEFINED_ENUM_FLAG))
      printf(" (implicitly created)");
printf("\n"); 
return TRUE;
}

static BOOL WINAPI EnumSysCallback(
    const void *pvSystemStore,
    DWORD dwFlags,
    PCERT_SYSTEM_STORE_INFO pStoreInfo,
    void *pvReserved,
    void *pvArg)
//-------------------------------------------------------------------
//  Begin callback process.
{
//-------------------------------------------------------------------
//  Declare and initialize local variables.

PENUM_ARG pEnumArg = (PENUM_ARG) pvArg;
LPCWSTR pwszSystemStore;
static int line_counter=0;
char x;

//-------------------------------------------------------------------
//  Begin processing.

//-------------------------------------------------------------------
//   Control break. If 5 or more lines have been printed,
//   pause and reset the line counter.

if(line_counter++ > 5)
{
   printf("Enumeration of system store: Press Enter to continue.");
   scanf_s("%c",&x);
   line_counter=0;
}

//-------------------------------------------------------------------
//  Prepare and display the next detail line.

if (GetSystemName(pvSystemStore, dwFlags, pEnumArg, &pwszSystemStore))
{
     printf("  %S\n", pwszSystemStore);
}
else
{
     MyHandleError("GetSystemName failed.");
}
if (pEnumArg->fAll || pEnumArg->fVerbose) 
{
    dwFlags &= CERT_SYSTEM_STORE_MASK;
    dwFlags |= pEnumArg->dwFlags & ~CERT_SYSTEM_STORE_MASK;
    if (!CertEnumPhysicalStore(
       pvSystemStore,
       dwFlags,
       pEnumArg,
       EnumPhyCallback
       )) 
    {
        DWORD dwErr = GetLastError();
        if (!(ERROR_FILE_NOT_FOUND == dwErr ||
            ERROR_NOT_SUPPORTED == dwErr))
        {
               printf("    CertEnumPhysicalStore");
        }
    }
}
return TRUE;
}

static BOOL WINAPI EnumLocCallback(
    LPCWSTR pwszStoreLocation,
    DWORD dwFlags,
    void *pvReserved,
    void *pvArg)

{
//-------------------------------------------------------------------
//  Declare and initialize local variables.

PENUM_ARG pEnumArg = (PENUM_ARG) pvArg;
DWORD dwLocationID = (dwFlags & CERT_SYSTEM_STORE_LOCATION_MASK) >>
   CERT_SYSTEM_STORE_LOCATION_SHIFT;
static int linecount=0;
char x;

//-------------------------------------------------------------------
//  Begin processing.

//-------------------------------------------------------------------
// Break if more than 5 lines have been printed.

if(linecount++ > 5)
{
   printf("Enumeration of store locations: "
       "Press Enter to continue.");
   scanf_s("%c",&x);
   linecount=0;
}

//-------------------------------------------------------------------
//  Prepare and display the next detail line.

printf("======   %S   ======\n", pwszStoreLocation);
if (pEnumArg->fAll) 
{
    dwFlags &= CERT_SYSTEM_STORE_MASK;
    dwFlags |= pEnumArg->dwFlags & ~CERT_SYSTEM_STORE_LOCATION_MASK;
    CertEnumSystemStore(
         dwFlags,
         (void *) pEnumArg->pvStoreLocationPara,
         pEnumArg,
         EnumSysCallback ); 
}
return TRUE;
}

//-------------------------------------------------------------------
//  This example uses the function MyHandleError, a simple error
//  handling function, to print an error message to  
//  the standard error (stderr) file and exit the program. 
//  For most applications, replace this function with one 
//  that does more extensive error reporting.

void MyHandleError(char *s)
{
    fprintf(stderr,"An error occurred in running the program. \n");
    fprintf(stderr,"%s\n",s);
    fprintf(stderr, "Error number %x.\n", GetLastError());
    fprintf(stderr, "Program terminating. \n");
    exit(1);
} // End of MyHandleError
```



 

 
