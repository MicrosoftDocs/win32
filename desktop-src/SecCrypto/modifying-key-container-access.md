---
description: Access to the keys from the LocalService or NetworkService accounts can be obtained programmatically by using the CryptSetProvParam function to modify the PP\_KEYSET\_SEC\_DESCR parameter.
ms.assetid: 22e8a153-c218-426a-bd81-7bdbb504c96f
title: Modifying Key Container Access
ms.topic: article
ms.date: 05/31/2018
---

# Modifying Key Container Access

The default key container that is created by CryptoAPI does not allow access to the keys from the LocalService or NetworkService accounts. This can be corrected programmatically by using the [**CryptSetProvParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetprovparam) function to modify the **PP\_KEYSET\_SEC\_DESCR** parameter.

The following example shows how to use the [**CryptSetProvParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetprovparam) function to modify the **PP\_KEYSET\_SEC\_DESCR** to allow access to a key container to the LocalService or NetworkService accounts.

> [!Note]  
> The following code is given as a tool and should only be used if absolutely necessary. You should only have to run this code once on each computer to allow access to the keys.

 


```C++
//-------------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
// Example of how to modify the access restrictions for the default 
// key container.

#include <stdio.h>
#include <tchar.h>
#include <windows.h>
#include <accctrl.h>
#include <aclapi.h>

// Link with the Advapi32.lib file.
#pragma comment (lib, "advapi32")

// Local function prototypes.
BOOL GetHandleToCSP(HCRYPTPROV*, LPCTSTR, DWORD);
BOOL GenPrivateKeys(HCRYPTPROV,DWORD);
BOOL GetHandleToCSP(HCRYPTPROV*, LPCTSTR, DWORD);
SECURITY_DESCRIPTOR* GetProvSecurityDesc(HCRYPTPROV);
BOOL ModifyDacl(HCRYPTPROV hProv);

#define MY_CONTAINER_NAME TEXT("testcapiservicemachinecontainer")

int _tmain(int argc, _TCHAR* argv[])
{
    HCRYPTKEY hKey = 0;
    HCRYPTPROV hProv = 0;

   if(!GetHandleToCSP(
        &hProv,
        MY_CONTAINER_NAME, 
        CRYPT_MACHINE_KEYSET))
    {
        printf("OpenCtxHandle failed.\n");
        goto CommonReturn;
    }
   printf("Acquired a context.\n");

   if(!GenPrivateKeys(hProv,0))
    {
        printf("GenPrivateKeys failed.\n");
        goto CommonReturn;
    }
    printf("Generated Private keys.\n");

    // Change the ACLs to allow read for local service.
    if(!ModifyDacl(hProv))
    {
        printf("ModifyDacl failed.\n");
        goto CommonReturn;
    }
    printf("Modified default ACLs on container.\n");

CommonReturn:
    if(hProv)
    {
        CryptReleaseContext(hProv, 0);
    }

    return 0;

}

/********************************************************************
    GetHandleToCSP

    Acquire a handle to the cryptographic service provider.
********************************************************************/
BOOL GetHandleToCSP( 
    HCRYPTPROV *phProv,
    LPCTSTR pszContainerName,
    DWORD dwProvFlag)
{
    if(!CryptAcquireContext(
        phProv,
        pszContainerName,
        MS_STRONG_PROV,
        PROV_RSA_FULL,
        dwProvFlag))
    {
        if(NTE_BAD_KEYSET == GetLastError() || 
            NTE_EXISTS == GetLastError())
        {
            if(!CryptAcquireContext(
                phProv,
                pszContainerName,
                MS_STRONG_PROV,
                PROV_RSA_FULL,
                CRYPT_NEWKEYSET | dwProvFlag))
            {
                printf("Error 0x%08x.\n",GetLastError());
                return FALSE;
            }
        }
        else 
        {
            printf(" Error in CryptAcquireContext 0x%08x.\n",
                GetLastError());
            return FALSE;
        }
    }
    return TRUE;
}

/********************************************************************
    GenPrivateKeys

    Generates a signature and a key exchange key.
********************************************************************/
BOOL GenPrivateKeys(
    HCRYPTPROV hProv,
    DWORD dwflagkey)
{
    BOOL fRet = FALSE;
    HCRYPTKEY hSigKey = 0;
    HCRYPTKEY hExchKey= 0;

    // Generate the signature key.
    if(!CryptGenKey(
        hProv,
        AT_SIGNATURE,
        dwflagkey,
        &hSigKey))
    {
        printf("CryptGenKey failed with 0x%08x.\n",GetLastError());
        goto CommonReturn;
    }

    // Generate the key exchange key.
    if(!CryptGenKey(
        hProv,
        AT_KEYEXCHANGE,
        dwflagkey,
        &hExchKey))
    {
        printf("CryptGenKey failed with 0x%08x.\n",GetLastError());
        goto CommonReturn;
    }
    
    fRet = TRUE;

CommonReturn:
    if(hSigKey)
    {
        CryptDestroyKey(hSigKey);
    }

    if(hExchKey)
    {
        CryptDestroyKey(hExchKey);
    }

    return fRet;
}

/********************************************************************
    GetProvSecurityDesc

    Retrieves the security descriptor for the specified provider.
********************************************************************/
SECURITY_DESCRIPTOR* GetProvSecurityDesc(HCRYPTPROV hProv) 
{
    SECURITY_DESCRIPTOR *psd = NULL;
    unsigned long ulSize = 0;

    // Get the size of the security descriptor.
    if(!CryptGetProvParam(
        hProv,
        PP_KEYSET_SEC_DESCR,
        0,
        &ulSize,
        DACL_SECURITY_INFORMATION))
    {
        int ret = GetLastError();
        if (ret != ERROR_INSUFFICIENT_BUFFER) 
        {
            fprintf(
                stderr, 
                "Error getting file security DACL: %d.\n", 
                ret);
            goto Error_Occurred;
        }
    }

    // Allocate the memory for the security descriptor.
    psd = (SECURITY_DESCRIPTOR *)LocalAlloc(LPTR, ulSize);
    if (!psd) 
    {
        fprintf(stderr, "Out of memory for security descriptor!\n");
        goto Error_Occurred;
    }

    // Retrieve the security descriptor.
    if(!CryptGetProvParam(
        hProv,
        PP_KEYSET_SEC_DESCR,
        (BYTE*)psd,
        &ulSize,
        DACL_SECURITY_INFORMATION))
    {
        fprintf(
            stderr, 
            "CryptGetProvParam failed with 0x%08x.\n", 
            GetLastError());
        goto Error_Occurred;
    }

    return psd;

Error_Occurred:
    // An error occurred, so if memory was allocated, free it.
    if(psd)
    {
        LocalFree(psd);
        psd = NULL;
    }

    return NULL;
}

/********************************************************************
    GetDacl

    Retrieves the DACL from the specified security descriptor.
********************************************************************/
ACL* GetDacl(SECURITY_DESCRIPTOR *psd) 
{
    ACL *pACL = NULL;
    int defaulted = 0;
    int present = 0;

    if (!psd) 
    {
        return NULL;
    }

    if (!GetSecurityDescriptorDacl(
        psd, 
        &present, 
        &pACL, 
        &defaulted)) 
    {
        fprintf(
            stderr, 
            "Error getting DACL from security descriptor: %d.\n", 
            GetLastError());
        return 0;
    }

    if (!present) 
    {
        fprintf(
            stderr, 
            "Security descriptor has no DACL present.\n");
        return 0;
    }

    return pACL;
}

/********************************************************************
    ModifyDacl

    Modifies the DACL for the key storage folder for the specified 
    provider.
********************************************************************/
BOOL ModifyDacl(HCRYPTPROV hProv)
{
    PSID pSid = NULL;
    DWORD cbSid = 0;
    LPTSTR szDomainName = NULL;
    DWORD cbDomainName = 0;
    SID_NAME_USE SidType;
    EXPLICIT_ACCESS ea[1] = {0};
    DWORD dwRes = 0;
    SECURITY_DESCRIPTOR *pCurrentSD = NULL;
    PSECURITY_DESCRIPTOR pNewSD = NULL;
    PACL pCurrentDACL = NULL;
    PACL pNewACL = NULL;

    while (!LookupAccountName(
        NULL, 
        TEXT("LocalService"), 
        pSid, 
        &cbSid,
        szDomainName, 
        &cbDomainName, 
        &SidType))
      {
         if (GetLastError() == ERROR_INSUFFICIENT_BUFFER)
         {
            pSid = LocalAlloc(LPTR, cbSid);
            szDomainName = (LPTSTR)LocalAlloc(LPTR, 
                (cbDomainName * sizeof(TCHAR)));

            if (pSid == NULL || szDomainName == NULL)
            {
               printf("LocalAlloc failed.\n");

               goto CommonReturn;
            }
         }
         else
         {
             printf("LookupAccountName error: %d.\n", 
                 GetLastError());

             goto CommonReturn;
         }
      }

    //Get existing ACLs for the file. 
    pCurrentSD = GetProvSecurityDesc(hProv);
    if (!pCurrentSD) 
    {
        printf("Unable to retrieve SD.\n");

        goto CommonReturn;
    }

    pCurrentDACL = GetDacl(pCurrentSD);
    if (!pCurrentDACL) 
    {
        printf("Unable to retrieve DACL.\n");

        goto CommonReturn;
    }

    // Initialize an EXPLICIT_ACCESS structure for an ACE.
    // The ACE will allow the user read access to the container.
    ZeroMemory(&ea, 1 * sizeof(EXPLICIT_ACCESS));
    ea[0].grfAccessPermissions = FILE_READ_DATA;
    ea[0].grfAccessMode = SET_ACCESS;
    ea[0].grfInheritance= NO_INHERITANCE;
    ea[0].Trustee.TrusteeForm = TRUSTEE_IS_SID;
    ea[0].Trustee.TrusteeType = TRUSTEE_IS_USER;
    ea[0].Trustee.ptstrName  = (LPTSTR) pSid;

    // Create a new ACL that contains the new ACEs as well as the 
    // old ones.
    dwRes = SetEntriesInAcl(1, ea, pCurrentDACL, &pNewACL);
    if (ERROR_SUCCESS != dwRes) 
    {
        printf("SetEntriesInAcl error: %u.\n", GetLastError());

        goto CommonReturn;
    }

    // Initialize a security descriptor.  
    pNewSD = (PSECURITY_DESCRIPTOR) LocalAlloc(LPTR, 
        SECURITY_DESCRIPTOR_MIN_LENGTH); 
    if (NULL == pNewSD) 
    { 
        printf("LocalAlloc error: %u.\n", GetLastError());

        goto CommonReturn; 
    } 
 
    if (!InitializeSecurityDescriptor(pNewSD, 
        SECURITY_DESCRIPTOR_REVISION)) 
    {  
        printf("InitializeSecurityDescriptor error: %u.\n",
            GetLastError());

        goto CommonReturn; 
    } 
 
    // Add the ACL to the security descriptor. 
    if (!SetSecurityDescriptorDacl(
        pNewSD, 
        TRUE,   
        pNewACL, 
        FALSE)) 
    {  
        printf("SetSecurityDescriptorDacl error: %u.\n", 
            GetLastError());
        
        goto CommonReturn; 
    } 

    // Set the new security descriptor.
    if(!CryptSetProvParam(
        hProv,
        PP_KEYSET_SEC_DESCR,
        (BYTE*)pNewSD,
        DACL_SECURITY_INFORMATION))
    {
        printf("CryptSetProvParam error: 0x%08x.\n", 
            GetLastError());

        goto CommonReturn;
    }

CommonReturn:
    if(pSid)
    {
        LocalFree(pSid);
    }

    if (pNewACL) 
    {
        LocalFree(pNewACL);
    }

    if (pNewSD) 
    {
        LocalFree(pNewSD);
    }

    if(pCurrentSD)
    {
        LocalFree(pCurrentSD);
    }

    return 1;
}
```



 

 



