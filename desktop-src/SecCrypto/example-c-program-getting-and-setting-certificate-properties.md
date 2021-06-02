---
description: Gets and sets certificate properties, and illustrates the following tasks and CryptoAPI functions.
ms.assetid: 4cc20a59-d8e9-4c9b-9438-21bccbbe4a64
title: 'Example C Program: Getting and Setting Certificate Properties'
ms.topic: article
ms.date: 05/31/2018
---

# Example C Program: Getting and Setting Certificate Properties

The following example gets and sets certificate properties, and illustrates the following tasks and [*CryptoAPI*](../secgloss/c-gly.md) functions.

-   Opening a system store by using [**CertOpenSystemStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopensystemstorea).
-   Using [**CertEnumCertificatesInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumcertificatesinstore) to list all of the certificates in the open store.
-   Retrieving and printing the subject name from the certificate by using [**CertGetNameString**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetnamestringa).
-   Setting the [*enhanced key usage*](../secgloss/e-gly.md) property on certificates by using the [**CertAddEnhancedKeyUsageIdentifier**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddenhancedkeyusageidentifier) function.
-   Setting the display name property on the certificate by using [**CertSetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcertificatecontextproperty).
-   Retrieving a certificate's properties by using [**CertGetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty).
-   Closing a certificate store by using [**CertCloseStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certclosestore) with the CERT\_CLOSE\_STORE\_CHECK\_FLAG flag.


```C++
#include <stdio.h>
#include <windows.h>
#include <wincrypt.h>
#pragma comment(lib, "crypt32.lib")

//--------------------------------------------------------------------
//   Copyright (C) Microsoft.  All rights reserved.
//   Declare functions MyHandleError and My_Wait.
//   These functions are defined at the end of the file.

void MyHandleError(char *s );

void My_Wait();

//--------------------------------------------------------------------
//  Begin main.

void main (void)
{

//--------------------------------------------------------------------
// This program shows all of the certificates in a 
// certificate store and lists all of the property ID numbers of all 
// of the certificate contexts.

// It also adds an enhanced key usage identifier to every other
// certificate.

//--------------------------------------------------------------------
//  Declare and initialize local variables.

HANDLE           hCertStore;        
PCCERT_CONTEXT   pCertContext=NULL;      
CRYPT_KEY_PROV_INFO *pCryptKeyProvInfo;
char pszNameString[256];
char pszStoreName[256];
char fResponse;
char fExtra;
BYTE *pName = (BYTE *)"Temp Name.";
CRYPT_DATA_BLOB  Friendly_Name_Blob={32,pName};
void*            pvData;
DWORD            cbData;
DWORD            dwFlags =  CERT_STORE_NO_CRYPT_RELEASE_FLAG;
DWORD            dwPropId = 0;   // 0 must be used on the first
                                 // call to the function. After that,
                                 // the last returned property ID is 
                                 // passed.
LPCSTR  pszUsageIdentifier = szOID_RSA_RC4;
int count = 0;

fprintf(stderr,"Please enter the store name :");
scanf_s("%s",pszStoreName);
fprintf(stderr,"The store name is %s .\n",pszStoreName);
My_Wait();

//--------------------------------------------------------------------
// Open the named system certificate store. 

if (!( hCertStore = CertOpenSystemStore(
   NULL,
   pszStoreName)))
{
     MyHandleError("Store not opened.");
}

//--------------------------------------------------------------------
// The file is open. Continue.
// In a loop, use CertEnumCertificatesInStore to get the each
// certificate in the store. 

while(pCertContext= CertEnumCertificatesInStore(
     hCertStore,
     pCertContext))
{
//--------------------------------------------------------------------
//  First, retrieve and print the subject name from the certificate.

     if(CertGetNameString(
        pCertContext,
        CERT_NAME_SIMPLE_DISPLAY_TYPE,
        0,
        NULL,
        pszNameString,
        128))
     {
          printf("\nNew Cert for %s \n",pszNameString);
     }
     else
     {
          printf("The get name failed.\n");
     }
//--------------------------------------------------------------------
//  Set the enhanced key usage property on every other certificate.

     if(count == 0)
     {
          count++;
          if(CertAddEnhancedKeyUsageIdentifier(
               pCertContext,
               pszUsageIdentifier))
          {
               printf("Enhanced key usage set.\n");
          }
          else
          {
               printf("Enhanced key usage was not set.\n");
          }
     }
     else
//--------------------------------------------------------------------
//   Do not set the usage, but reset the counter so that the property
//   will be set on the next certificate.
//   Ask if the user would like to set a display name.
     {
         printf("Would you like to set the display name ?");
         scanf_s("%c%c",&fResponse,&fExtra);
         if(fResponse == 'y')
         {
           if(CertSetCertificateContextProperty(
                pCertContext,  
                CERT_FRIENDLY_NAME_PROP_ID,      
                0,
                &Friendly_Name_Blob))
           {
               printf("A name has been set.\n");
           }
           else
           {
                printf("The display name was not set.\n");
            }
         }
          count = 0;
     }

//--------------------------------------------------------------------
// In a loop, find all of the property IDs for the given certificate.
// The loop continues until the CertEnumCertificateContextProperties 
// returns 0.

     while(dwPropId = CertEnumCertificateContextProperties(
       pCertContext, // the context whose properties are to be listed.
       dwPropId))    // number of the last property found. Must be
                     // 0 to find the first property ID.
     {
//--------------------------------------------------------------------
// Each time through the loop, a property ID has been found.
// Print the property number and information about the property.

        printf("Property # %d found->", dwPropId);
        switch(dwPropId)
        {
        case CERT_FRIENDLY_NAME_PROP_ID:
        {
//--------------------------------------------------------------------
//  Retrieve the actual display name certificate property.
//  First, get the length of the property setting the
//  pvData parameter to NULL to get a value for cbData
//  to be used to allocate memory for the pvData buffer.
          printf("FRIENDLY_NAME_PROP_ID ");
          if(!(CertGetCertificateContextProperty(
            pCertContext, 
            dwPropId, 
            NULL, 
            &cbData)))
          {
             MyHandleError("Call #1 to property length failed.");
          }
//--------------------------------------------------------------------
// The call succeeded. Use the size to allocate memory for the 
// property.
          if(!(pvData = (void*)malloc(cbData)))
          {
            MyHandleError("Memory allocation failed.");
          }
//--------------------------------------------------------------------
// Allocation succeeded. Retrieve the property data.
          if(!(CertGetCertificateContextProperty(
              pCertContext,
              dwPropId,
              pvData, 
              &cbData)))
          {
             MyHandleError("Call #2 getting the data failed.");
          }
          else
          {
             printf("\n  The display name is -> %s.", pvData);
             free(pvData);
          }
          break;
        }
        case CERT_SIGNATURE_HASH_PROP_ID:
        {
           printf("Signature hash ID. ");
           break;
        }
        case CERT_KEY_PROV_HANDLE_PROP_ID:
        {
           printf("KEY PROVE HANDLE.");
           break;
        }
        case CERT_KEY_PROV_INFO_PROP_ID:
        {
          printf("KEY PROV INFO PROP ID.");
          if(!(CertGetCertificateContextProperty(
             pCertContext,  // A pointer to the certificate
                            // where the property will be set.
             dwPropId,      // An identifier of the property to get. 
                            // In this case,
                            // CERT_KEY_PROV_INFO_PROP_ID
             NULL,          // NULL on the first call to get the
                            // length.
             &cbData)))     // The number of bytes that must be
                            // allocated for the structure.
          {
             MyHandleError("The property length was not retrieved.");
          }
          if(!(pCryptKeyProvInfo = 
                   (CRYPT_KEY_PROV_INFO *)malloc(cbData)))
          {
             MyHandleError("Error in allocation of memory.");
           }
           if(CertGetCertificateContextProperty(
                pCertContext,
                dwPropId,
                pCryptKeyProvInfo,
                &cbData))
           {
               printf("\n The current key container is %S.",
                   pCryptKeyProvInfo->pwszContainerName);
               free(pCryptKeyProvInfo);
           }
           else
           {
               free(pCryptKeyProvInfo);
               MyHandleError("The property was not retrieved.");
           }
           break;
        }
        case CERT_SHA1_HASH_PROP_ID:
        {
          printf("SHA1 HASH id.");
          break;
        }
        case CERT_MD5_HASH_PROP_ID:
        {
          printf("md5 hash id. ");
          break;
        }
        case CERT_KEY_CONTEXT_PROP_ID:
        {
          printf("KEY CONTEXT PROP id.");
          break;
        }
        case CERT_KEY_SPEC_PROP_ID:
        {
          printf("KEY SPEC PROP id.");
          break;
        }
        case CERT_ENHKEY_USAGE_PROP_ID:
        {
          printf("ENHKEY USAGE PROP id.");
          break;
        }
        case CERT_NEXT_UPDATE_LOCATION_PROP_ID:
        {
          printf("NEXT UPDATE LOCATION PROP id.");
          break;
        }
        case CERT_PVK_FILE_PROP_ID:
        {
          printf("PVK FILE PROP id. ");
          break;
        }
        case CERT_DESCRIPTION_PROP_ID:
        {
          printf("DESCRIPTION PROP id. ");
          break;
        }
        case CERT_ACCESS_STATE_PROP_ID:
        {
          printf("ACCESS STATE PROP id. ");
          break;
        }
        case CERT_SMART_CARD_DATA_PROP_ID:
        {
          printf("SMAART_CARD DATA PROP id. ");
          break;
        }
        case CERT_EFS_PROP_ID:
        {
          printf("EFS PROP id. ");
          break;
        }
        case CERT_FORTEZZA_DATA_PROP_ID:
        {
          printf("FORTEZZA DATA PROP id.");
         break;
        }
        case CERT_ARCHIVED_PROP_ID:
        {
          printf("ARCHIVED PROP id.");
          break;
        }
        case CERT_KEY_IDENTIFIER_PROP_ID:
        {
          printf("KEY IDENTIFIER PROP id. ");
          break;
        }
        case CERT_AUTO_ENROLL_PROP_ID:
        {
          printf("AUTO ENROLL id. ");
          break;
        }
        }  // end switch
        printf("\n");
      } // end the inner while loop. This is the end of the display of
        // a single property of a single certificate.

      My_Wait();
} // end the outer while loop. Move on to the next certificate.

//--------------------------------------------------------------------
// Free Memory and close the open store.
if(pCertContext)
{
    CertFreeCertificateContext(pCertContext);
}
CertCloseStore(hCertStore,0);
printf("The function completed successfully.\n");
}

//--------------------------------------------------------------------
//  Define functions MyHandleError and My_Wait.

void MyHandleError( char *s)
{
     printf("%s\n",s);
     exit(1);
}

void My_Wait()
{

     printf("Hit enter to continue.");
     getchar();
}
```



 

 
