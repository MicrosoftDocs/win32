---
description: Example code that shows how to add a new user to an existing encrypted file by using the AddUsersToEncryptedFile function.
ms.assetid: 39260882-dc02-4f08-9d9b-f170c1e391df
title: Adding Users to an Encrypted File
ms.topic: article
ms.date: 05/31/2018
---

# Adding Users to an Encrypted File

The code sample in this topic adds a new user to an existing encrypted file by using the [**AddUsersToEncryptedFile**](/windows/desktop/api/Winefs/nf-winefs-adduserstoencryptedfile) function. It requires the user's Encrypting File System (EFS) certificate (from the Active Directory) to exist in the Trusted People user certificate store.

This sample adds a new Data Recovery Field to the encrypted file. As a result, the newly added user can decrypt the encrypted file. The caller must already have access to the encrypted file, either as the original owner, the data recovery agent, or as a user who was previously added to the encrypted file.


```C++
//-------------------------------------------------------------------
// 
//  Adduser.c: adds a user to an encrypted file.
//
//  Note: Build project must link Crypt32.lib
//-------------------------------------------------------------------
#define UNICODE 1

#include <Windows.h>
#include <malloc.h>
#include <stdlib.h>
#include <stdio.h>
#include <wchar.h>
#include <wincrypt.h>
#include <winefs.h>

#pragma comment(lib, "Advapi32.lib")
#pragma comment(lib, "Crypt32.lib")

//-------------------------------------------------------------------
// Utility function that outputs this application's usage 
// instructions.
//
VOID usage(LPWSTR wszAppName)
{
    wprintf(L"\n%s: adds users to encrypted files.\n", wszAppName);
    wprintf(L"\nUsage:\tadduser <file> <user name> <subject name>\n\n");
    wprintf(L"\t<file> is the name of the file\n");
    wprintf(L"\t<user name> is the name of the user's account\n");
    wprintf(L"\t\tExample: for name@example.com, use \"name\"\n");
    wprintf(L"\t<subject name> is the \"IssuedTo\" name on the ");
    wprintf(L"certificate\n\t\tfrom the TrustedPeople store.\n");
    exit(1);
}

VOID ErrorExit(LPWSTR wszErrorMessage, DWORD dwErrorCode);

void __cdecl wmain(int argc, wchar_t *argv[])
{
    LPWSTR wszFile    = NULL;
    LPWSTR wszAccount = NULL;
    LPWSTR wszSubject = NULL;
    PSID   pSid       = NULL;
    DWORD  cbSid      = 0;
    LPWSTR wszDomain  = NULL;
    DWORD  cchDomain  = 0;
    SID_NAME_USE SidType = SidTypeUser;
    HCERTSTORE hStore = NULL;
    PCCERT_CONTEXT pCertContext = NULL;
    PENCRYPTION_CERTIFICATE      pEfsEncryptionCert     = NULL;
    PENCRYPTION_CERTIFICATE_LIST pEfsEncryptionCertList = NULL;
    DWORD dwResult = ERROR_SUCCESS;

    // Simple check whether to explain usage to the user.
    //
    if(argc !=4)
    {
        usage(argv[0]);
    }

    // TODO: Check the parameters for correctness.
    //
    wszFile = argv[1];
    wszAccount = argv[2];
    wszSubject = argv[3];

    // First, look up the user's SID using the specified account name.
    // Call LookupAccountName twice; first to find the size of the 
    // SID, and a second time to retrieve the SID.
    //
    LookupAccountName(NULL,wszAccount,pSid,&cbSid,
                      wszDomain,&cchDomain,&SidType);
    if(0 == cbSid)
    {
        ErrorExit(L"LookupAccountName did not return the SID size.",
                     GetLastError());
    }
    pSid = (PSID)malloc(cbSid);
    if(!pSid)
    {
        ErrorExit(L"Failed to allocate SID.", GetLastError());
    }
    wszDomain = (LPWSTR)malloc(cchDomain * sizeof(WCHAR));
    if(!wszDomain)
    {
        ErrorExit(L"Failed to allocate string.", GetLastError());
    }
    if(!LookupAccountName(NULL,wszAccount,pSid,&cbSid,
                          wszDomain,&cchDomain,&SidType))
    {
        ErrorExit(L"LookupAccountName failed.", GetLastError());
    }

    // Obtain the user's certificate.
    // Search the TrustedPeople store for the specified subject name.
    // Anyone who has encrypted a file on the computer has an 
    // encryption certificate placed the TrustedPeople store by the 
    // system. It is likely that the user has a matching private key.
    //
    hStore = CertOpenSystemStore( (HCRYPTPROV)NULL,L"TrustedPeople");
    if (! hStore)
    {
        ErrorExit(L"OpenSystemStore failed.", GetLastError());
    }

    pCertContext = CertFindCertificateInStore( hStore,
                           X509_ASN_ENCODING | PKCS_7_ASN_ENCODING,
                           0,
                           CERT_FIND_SUBJECT_STR,
                           (VOID*)wszSubject,
                           NULL);
    if(!pCertContext)
    {
        ErrorExit(L"FindCertificateInStore failed.", GetLastError());
    }

    // Create the ENCRYPTION_CERTIFICATE using the cert context and 
    // the user's SID.
    //
    pEfsEncryptionCert = (PENCRYPTION_CERTIFICATE) 
                       malloc(sizeof(ENCRYPTION_CERTIFICATE));
    if(!pEfsEncryptionCert)
    {
        ErrorExit(L"Failed to allocate structure.", GetLastError());
    }
    pEfsEncryptionCert->cbTotalLength = 
        sizeof(ENCRYPTION_CERTIFICATE);
    pEfsEncryptionCert->pUserSid = (SID *)pSid;
    pEfsEncryptionCert->pCertBlob = (PEFS_CERTIFICATE_BLOB) 
                                 malloc(sizeof(EFS_CERTIFICATE_BLOB));
    if(!pEfsEncryptionCert->pCertBlob)
    {
        ErrorExit(L"Failed to allocate cert blob.", GetLastError());
    }
    pEfsEncryptionCert->pCertBlob->dwCertEncodingType = 
                        pCertContext->dwCertEncodingType;
    pEfsEncryptionCert->pCertBlob->cbData = 
                        pCertContext->cbCertEncoded;
    pEfsEncryptionCert->pCertBlob->pbData =
                        pCertContext->pbCertEncoded;

    // AddUsersToEncryptedFile takes an ENCRYPTION_CERTIFICATE_LIST; 
    // create one with only one ENCRYPTION_CERTIFICATE in it.
    //
    pEfsEncryptionCertList = (PENCRYPTION_CERTIFICATE_LIST) 
                          malloc(sizeof(ENCRYPTION_CERTIFICATE_LIST));
    if(!pEfsEncryptionCertList)
    {
        ErrorExit(L"Failed to allocate structure.", GetLastError());
    }
    pEfsEncryptionCertList->nUsers = 1;
    pEfsEncryptionCertList->pUsers = &pEfsEncryptionCert;

    // Call the API to add the user.
    //
    dwResult = 
        AddUsersToEncryptedFile(wszFile,pEfsEncryptionCertList);
    if(ERROR_SUCCESS == dwResult)
    {
        wprintf(L"The user was successfully added to the file.\n");
    }
    else
    {
        ErrorExit(L"AddUsersToEncryptedFile failed.", dwResult);
    }

    // Clean up all allocated resources.
    //
    if(wszDomain) free(wszDomain);
    if(pSid) free(pSid);
    if(pCertContext) CertFreeCertificateContext(pCertContext);
    if(hStore) CertCloseStore(hStore,CERT_CLOSE_STORE_FORCE_FLAG);

    if(pEfsEncryptionCertList)
    {
        if (pEfsEncryptionCertList->pUsers)
        {
            if(pEfsEncryptionCertList->pUsers[0])
            {
                if((pEfsEncryptionCertList->pUsers[0])->pCertBlob) 
                 free((pEfsEncryptionCertList->pUsers[0])->pCertBlob);
                free(pEfsEncryptionCertList->pUsers[0]);
            }
            free(pEfsEncryptionCertList->pUsers);
        }
        free(pEfsEncryptionCertList);
    }
  
    wprintf(L"The program ran to completion without error.\n");
    exit(0);
}


//------------------------------------------------------------------
//  A simple error handling function that prints an error message 
//  and exits the program. 
//
//  TODO: Replace this function with one that has better error 
//  reporting.
//
VOID ErrorExit(LPWSTR wszErrorMessage, DWORD dwErrorCode)
{
    fwprintf(stderr, L"An error occurred in running the program. \n");
    fwprintf(stderr, L"%s\n", wszErrorMessage);
    fwprintf(stderr, L"Error code: 0x%08x\n", dwErrorCode);
    fwprintf(stderr, L"Program terminating. \n");
    exit(1);
}
```



## Related topics

<dl> <dt>

[**CertCloseStore**](/windows/desktop/api/wincrypt/nf-wincrypt-certclosestore)
</dt> <dt>

[**CertFindCertificateInStore**](/windows/desktop/api/wincrypt/nf-wincrypt-certfindcertificateinstore)
</dt> <dt>

[**CertFreeCertificateContext**](/windows/desktop/api/wincrypt/nf-wincrypt-certfreecertificatecontext)
</dt> <dt>

[**CertOpenSystemStore**](/windows/desktop/api/wincrypt/nf-wincrypt-certopensystemstorea)
</dt> <dt>

[File Encryption](file-encryption.md)
</dt> <dt>

[**LookupAccountName**](/windows/desktop/api/winbase/nf-winbase-lookupaccountnamea)
</dt> </dl>

 

 
