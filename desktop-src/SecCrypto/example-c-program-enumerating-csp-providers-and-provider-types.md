---
description: Lists the CSPs available on a computer by using CryptoAPI.
ms.assetid: 10a5210d-7992-4832-9435-67ac2b851a97
title: 'Example C Program: Enumerating CSP Providers and Provider Types'
ms.topic: article
ms.date: 05/31/2018
---

# Example C Program: Enumerating CSP Providers and Provider Types

The following example lists the CSPs available on a computer and uses the following [*CryptoAPI*](../secgloss/c-gly.md) functions:

-   [**CryptEnumProviderTypes**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumprovidertypesa)
-   [**CryptEnumProviders**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumprovidersa)
-   [**CryptGetDefaultProvider**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetdefaultprovidera)
-   [**CryptGetProvParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetprovparam)

This example uses the function [**MyHandleError**](myhandleerror.md). The code for this function is included in this example. Code for this and other auxiliary functions is also listed under [General Purpose Functions](general-purpose-functions.md).

The following example shows enumerating CSPs and provider types.


```C++
//-------------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
#pragma comment(lib, "crypt32.lib")

#include <stdio.h>
#include <tchar.h>
#include <windows.h>
#include <wincrypt.h>

void MyHandleError(TCHAR* s);
void Wait(TCHAR* s);

int _tmain(int argc, _TCHAR* argv[])
{
    // Declare and initialize variables.
    HCRYPTPROV hProv;
    LPTSTR pszName;
    DWORD dwType;
    DWORD cbName;
    DWORD dwIndex = 0;
    BYTE* ptr;
    ALG_ID aiAlgid;
    DWORD dwBits;
    DWORD dwNameLen;
    CHAR szName[100];
    BYTE pbData[1024];
    DWORD cbData = 1024;
    DWORD dwIncrement = sizeof(DWORD);
    DWORD dwFlags = CRYPT_FIRST;
    DWORD dwParam = PP_CLIENT_HWND;
    CHAR* pszAlgType = NULL;
    BOOL fMore = TRUE;
    LPTSTR pbProvName;
    DWORD cbProvName;

    //--------------------------------------------------------------
    // Print header lines for provider types.
    _tprintf(TEXT("Listing Available Provider Types.\n"));
    _tprintf(TEXT("Provider type    Provider Type Name\n"));
    _tprintf(TEXT("_____________    ")
        TEXT("_____________________________________\n"));

    // Loop through enumerating provider types.
    dwIndex = 0;
    while(CryptEnumProviderTypes(
        dwIndex,
        NULL,
        0,
        &dwType,
        NULL,
        &cbName))
    {
        //-----------------------------------------------------------
        // cbName is the length of the name of the next provider 
        // type.

        // Allocate memory in a buffer to retrieve that name.
        if (!(pszName = (LPTSTR)LocalAlloc(LMEM_ZEROINIT, cbName)))
        {
           MyHandleError(TEXT("ERROR - LocalAlloc failed!"));
        }

        //-----------------------------------------------------------
        // Get the provider type name.
        if (CryptEnumProviderTypes(
            dwIndex++,
            NULL,
            NULL,
            &dwType,   
            pszName,
            &cbName))     
        {
            _tprintf (TEXT("     %4.0d        %s\n"), 
                dwType, 
                pszName);
        }
        else
        {
            MyHandleError(TEXT("ERROR - CryptEnumProviders"));
        }

        LocalFree(pszName);
    }

    //--------------------------------------------------------------
    // Print header lines for providers.
    _tprintf(TEXT("\n\nListing Available Providers.\n"));
    _tprintf(TEXT("Provider type    Provider Name\n"));
    _tprintf(TEXT("_____________    ")
        TEXT("_____________________________________\n"));

    //---------------------------------------------------------------
    // Loop through enumerating providers.
    dwIndex = 0;
    while(CryptEnumProviders(
        dwIndex,
        NULL,
        0,
        &dwType,
        NULL,
        &cbName))
    {
        //-----------------------------------------------------------
        // cbName is the length of the name of the next provider.
        // Allocate memory in a buffer to retrieve that name.
        if (!(pszName = (LPTSTR)LocalAlloc(LMEM_ZEROINIT, cbName)))
        {
           MyHandleError(TEXT("ERROR - LocalAlloc failed!"));
        }

        //-----------------------------------------------------------
        // Get the provider name.
        if (CryptEnumProviders(
            dwIndex++,
            NULL,
            0,
            &dwType,
            pszName,
            &cbName))
        {
            _tprintf (TEXT("     %4.0d        %s\n"), 
                dwType, 
                pszName);
        }
        else
        {
            MyHandleError(TEXT("ERROR - CryptEnumProviders"));
        }

        LocalFree(pszName);
    } // End while loop.

    //---------------------------------------------------------------
    // Get the name of the default CSP specified for the 
    // PROV_RSA_FULL type for the computer.

    //---------------------------------------------------------------
    // Get the length of the RSA_FULL default provider name.
    if (!(CryptGetDefaultProvider(
        PROV_RSA_FULL, 
        NULL, 
        CRYPT_MACHINE_DEFAULT,
        NULL, 
        &cbProvName))) 
    { 
       MyHandleError(TEXT("Error getting the length of the ")
           TEXT("default provider name."));
    }

    //---------------------------------------------------------------
    // Allocate local memory for the name of the default provider.
    if (!(pbProvName = (LPTSTR)LocalAlloc(
        LMEM_ZEROINIT, 
        cbProvName)))
    {
        MyHandleError(TEXT("Error during memory allocation ")
            TEXT("for provider name."));
    }

    //---------------------------------------------------------------
    // Get the name of the default PROV_RSA_FULL provider.
    if (CryptGetDefaultProvider(
        PROV_RSA_FULL, 
        NULL, 
        CRYPT_MACHINE_DEFAULT,
        pbProvName,
        &cbProvName)) 
    {
        _tprintf(TEXT("\nThe default provider name is \"%s\"\n"), 
            pbProvName);
    }
    else
    {
        MyHandleError(TEXT("Getting the provider name failed."));
    }

    LocalFree(pbProvName);

    //-----------------------------------------------------
    //  Acquire a cryptographic context.
    if(!CryptAcquireContext(
        &hProv, 
        NULL,
        NULL,
        PROV_RSA_FULL, 
        NULL))  
    {
        MyHandleError(TEXT("Error during CryptAcquireContext!"));
    }

    //------------------------------------------------------
    // Enumerate the supported algorithms.

    //------------------------------------------------------
    // Print header for algorithm information table.
    _tprintf(TEXT("\nEnumerating the supported ")
        TEXT("algorithms\n\n"));
    _tprintf(TEXT("     Algid      Bits      Type        ")
        TEXT("Name         Algorithm\n"));
    _tprintf(TEXT("                                     Length")
        TEXT("          Name\n"));
    _tprintf(TEXT("    _______________________________________")
        TEXT("_________________\n"));
    while(fMore)
    {
        //------------------------------------------------------
        // Retrieve information about an algorithm.
        if(CryptGetProvParam(
            hProv, 
            PP_ENUMALGS, 
            pbData, 
            &cbData, 
            dwFlags))
        {       
            //-------------------------------------------------------
            // Extract algorithm information from the pbData buffer.
           dwFlags = 0;
           ptr = pbData;
           aiAlgid = *(ALG_ID *)ptr;
           ptr += sizeof(ALG_ID);
           dwBits = *(DWORD *)ptr;
           ptr += dwIncrement;
           dwNameLen = *(DWORD *)ptr;
           ptr += dwIncrement;
           strncpy_s(szName,(char *) ptr, sizeof(szName), dwNameLen);
           
            //-------------------------------------------------------
            // Determine the algorithm type.
           switch(GET_ALG_CLASS(aiAlgid)) 
           {
           case ALG_CLASS_DATA_ENCRYPT: 
               pszAlgType = "Encrypt  ";
               break;
            
            case ALG_CLASS_HASH:         
                pszAlgType = "Hash     ";
                break;

            case ALG_CLASS_KEY_EXCHANGE: 
                pszAlgType = "Exchange ";
                break;

            case ALG_CLASS_SIGNATURE:    
                pszAlgType = "Signature";
                break;

            default:
                pszAlgType = "Unknown  ";
                break;
           }

           //--------------------------------------------------------
            // Print information about the algorithm.
            printf("    %8.8xh    %-4d    %s     %-2d          %s\n",
                aiAlgid, 
                dwBits, 
                pszAlgType, 
                dwNameLen, 
                szName);
        }
        else
        {
            fMore = FALSE;
        }
    }

    Wait(TEXT("\nPress Enter to continue."));

    if(!(CryptReleaseContext(hProv, 0)))
    {
        MyHandleError(TEXT("Error during CryptReleaseContext.")); 
    }

    if(GetLastError() == ERROR_NO_MORE_ITEMS)
    { 
       _tprintf(TEXT("\nThe program completed without error.\n"));
    }
    else
    { 
       MyHandleError(TEXT("Error reading algorithm!"));
    }

} // End main.

//-------------------------------------------------------------------
//  This example uses the function MyHandleError, a simple error
//  handling function, to print an error message and exit 
//  the program. 
//  For most applications, replace this function with one 
//  that does more extensive error reporting.

void MyHandleError(TCHAR *s)
{
    _tprintf(TEXT("An error occurred in running the program.\n"));
    _tprintf(TEXT("%s\n"),s);
    _tprintf(TEXT("Error number %x\n."), GetLastError());
    _tprintf(TEXT("Program terminating.\n"));
    exit(1);
}

void Wait(TCHAR *s)
{
    char x;
    _tprintf(s);
    x = getchar();
}

```



 

 
