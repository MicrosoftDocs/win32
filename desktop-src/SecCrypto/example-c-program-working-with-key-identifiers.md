---
description: 'Example C Program: Working with Key Identifiers'
ms.assetid: 5ca160fd-8a63-46fa-99ce-e01a6acb81f4
title: 'Example C Program: Working with Key Identifiers'
ms.topic: article
ms.date: 05/31/2018
---

# Example C Program: Working with Key Identifiers

The following example demonstrates ways of working with key identifiers. This example illustrates the following tasks and CryptoAPI functions:

-   Creating a key identifier using [**CryptCreateKeyIdentifierFromCSP**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcreatekeyidentifierfromcsp).
-   Setting a property on a key identifier using [**CryptSetKeyIdentifierProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetkeyidentifierproperty).
-   Retrieving the contents of a key identifier property using [**CryptGetKeyIdentifierProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetkeyidentifierproperty).
-   Listing the properties of a key identifier using [**CryptEnumKeyIdentifierProperties**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumkeyidentifierproperties).
-   Declaring, defining, and using a callback function.


```C++
#include <stdio.h>
#include <windows.h>
#include <Wincrypt.h>

//-------------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
// This program demonstrates the following Key Identifier functions:
//         CryptCreateKeyIdentifierFromCSP
//         CryptSetKeyIdentifierProperty
//         CryptGetKeyIdentifierProperty
//         CryptEnumKeyIdentifierProperties
// The callback function pfnEnum is also demonstrated.

//-------------------------------------------------------------------
// Declare the Callback function

static BOOL WINAPI pfnEnum (
const CRYPT_HASH_BLOB *pKeyIdentifier, // in- pKeyIdentifier
DWORD dwFlags,                         // in- Flag values
void *pvReserved,                      // Reserved
void *pvArg,                           // in- Pass-through argument
DWORD cProp,                           // in- cProp
DWORD *rgdwPropId,                     // in- array of PropIds
void **rgpvData,                       // in- array of 
                                       //  CRYPT_KEY_PROV_INFO 
                                       //  structures
DWORD *rgcbData                        // in- rgcbData
);

//-------------------------------------------------------------------
//  Declare the MyHandleError function.

void MyHandleError(char *s);

void main(void)
{
//-------------------------------------------------------------------
// Declare and initialize variables.

PUBLICKEYSTRUC *pPubKeyStruc;
DWORD cbPubKeyStruc= sizeof(PUBLICKEYSTRUC);
if(!(pPubKeyStruc = (PUBLICKEYSTRUC *) malloc (cbPubKeyStruc)))
    MyHandleError("Memory allocation failed.");

pPubKeyStruc->bType= PUBLICKEYBLOB;
pPubKeyStruc->bVersion= CUR_BLOB_VERSION;
pPubKeyStruc->reserved= 0;
pPubKeyStruc->aiKeyAlg= CALG_RSA_KEYX;

BYTE *pbHash;
DWORD cbHash;
PCRYPT_KEY_PROV_INFO pData;

CRYPT_HASH_BLOB KeyIdentifier;

DWORD cbData;
void *pvArg;         // Pass through argument.
cbHash= 20;          // define cbHash to the size of a SHA1
                     // string- there is no need for a 2 pass
                     // call to determine size of cbHash.

//-------------------------------------------------------------------
// Allocate memory for the pbHash buffer

if(!(pbHash= (BYTE *) malloc (cbHash))
    MyHandleError("Memory allocation failed.");

//-------------------------------------------------------------------
// Create a Key Identifier

if(CryptCreateKeyIdentifierFromCSP(
   X509_ASN_ENCODING, // dwCertEncodingType
   NULL,              // pszPubKeyOID- NULL to
                      // use default OID.
   pPubKeyStruc,      // pPubKeyStruc- defined above
   cbPubKeyStruc,     // cbPubKeyStruc
   0,                 // dwFlags
   NULL,              // pvReserved
   pbHash,            // pbHash
   &cbHash            // pcbHash
   ))
{
   printf("Call to CryptCreateKeyIdentifierFromCSP succeeded.\n");
}
else
{
   MyHandleError("A key identifier was not created");
}
//-------------------------------------------------------------------
// Set the members of the key identifier.

KeyIdentifier.cbData= cbHash;
KeyIdentifier.pbData= (BYTE*) pbHash;

//-------------------------------------------------------------------
// Initialize the pdata structure.

if(!(pData= (CRYPT_KEY_PROV_INFO*) malloc 
   (sizeof(CRYPT_KEY_PROV_INFO))))
    MyHandleError("Memory allocation failed.");
pData->pwszContainerName= L"New Key container name";
pData->pwszProvName= MS_ENHANCED_PROV_W;
pData->dwProvType= PROV_RSA_FULL;
pData->dwFlags= 0;
pData->cProvParam= 0;
pData->rgProvParam= NULL;
pData->dwKeySpec= AT_SIGNATURE;

//-------------------------------------------------------------------
// Set a property on the created key identifier.

if(CryptSetKeyIdentifierProperty(
  &KeyIdentifier,             // in- defined above
  CERT_KEY_PROV_INFO_PROP_ID, // in- dwPropId
  CRYPT_KEYID_MACHINE_FLAG,   // in- dwFlags- use local computer
  NULL,                       // in- pwszComputerName
  NULL,                       // Reserved
  pData                       // in- pointer to a 
                              // CRYPT_KEY_PROV_INFO.
  ))
{
  printf("A property is set on the key identifier.\n");
}
else
{
  MyHandleError("Setting the property failed.");
}

//-------------------------------------------------------------------
// Call CryptGetKeyIdentifierProperty to set the size 
// of the property to be retrieved.

if(CryptGetKeyIdentifierProperty(
   &KeyIdentifier,             // in- defined above
   CERT_KEY_PROV_INFO_PROP_ID, // in- dwPropId
   CRYPT_KEYID_MACHINE_FLAG,   // in- dwFlags
   NULL,                       // in, optional- pwszComputerName
   NULL,                       // in, optional- pvReserved
   NULL,                       // out- pvData
   &cbData                     // in, out- pcbData
   ))
{
   printf("First call to get property succeeded.\n");
}
else
{
   MyHandleError("Call 1 to CryptGetKeyIdentifierProperty failed.");
}

//-------------------------------------------------------------------
// Free the memory allocated for pData,

free(pData);
//-------------------------------------------------------------------
// Allocate memory for the buffer to receive the property.

if(!(pData= (CRYPT_KEY_PROV_INFO*) malloc (cbData)))
    MyHandleError("Memory allocation failed.");

//-------------------------------------------------------------------
// Call CryptGetKeyIdentifierProperty a second time
// To retrieve the property into the allocated buffer.

if(CryptGetKeyIdentifierProperty(
   &KeyIdentifier,             // pKeyIdentifier
   CERT_KEY_PROV_INFO_PROP_ID, // dwPropId
   CRYPT_KEYID_MACHINE_FLAG,   // dwFlags
   NULL,                       // pwszComputerName
   NULL,                       // Reserved
   pData,                      // pData
   &cbData                     // pcbData
   ))
{
   printf("The property has been retrieved.\n");
}
else
{
   MyHandleError("Second call failed.");
}

//-------------------------------------------------------------------
// Print part of the retrieved property.

printf("Some of the properties obtained are;\n");
printf("container name= %S\n",pData->pwszContainerName);
printf("Provider name= %S\n", pData->pwszProvName);
printf("Provider type= %i\n", pData->dwProvType);
printf("length= %i\n\n", cbData);

//-------------------------------------------------------------------
// Set the pass through argument for the callback function.

pvArg= pPubKeyStruc;

//-------------------------------------------------------------------
// Call CryptEnumKeyIdentifierProperties.

printf("\nCalling CryptEnumKeyIdentifierProperties.\n");
if(CryptEnumKeyIdentifierProperties(
   &KeyIdentifier,           // in- pKeyIdentifier-
   0,                        // in- dwPropId
   CRYPT_KEYID_MACHINE_FLAG, // in- dwFlags, use LocalMachine.
   NULL,                     // in, optional- pwszComputerName set
                             // to NULL to use LocalMachine.
   NULL,                     // Reserved
   pvArg,                    // in, optional- Pointer to the
                             // pass-through argument
  (PFN_CRYPT_ENUM_KEYID_PROP )pfnEnum
                             // in- Callback function.
   ))
{
   printf("The function call succeeded.\n");
}
else
{
  MyHandleError("Call to CryptEnumKeyIdentifierProperties failed.");
}

//-------------------------------------------------------------------
// Free all allocated memory

free (pData);
free (pPubKeyStruc);
printf("all memory free\n");
printf("The program ran to completion without error.\n");
}  // end main.

//-------------------------------------------------------------------
// Define the Callback function

static BOOL WINAPI pfnEnum (
const CRYPT_HASH_BLOB *pKeyIdentifier, // in- pKeyIdentifier
DWORD dwFlags,                         // in- Flag values
void *pvReserved,                      // Reserved
void *pvArg,                           // in- Pass-through argument
DWORD cProp,                           // in- cProp
DWORD *rgdwPropId,                     // in- rgdwPropId
void **rgpvData,                       // in- rgpvData- points to an 
                                       // array of
                                       // CRYPT_KEY_PROV_INFO 
                                       // structures
DWORD *rgcbData                        // in- rgcbData
)
{
//-------------------------------------------------------------------
//  Declare and initialize local variables.

PUBLICKEYSTRUC *pArg= (PUBLICKEYSTRUC *) pvArg;

//-------------------------------------------------------------------
//  Begin processing

printf("The argument passed is a structure.\n");
printf("BLOB type= %x   ", pArg->bType);
printf("Version= %x\n", pArg->bVersion);
printf("Algorithm= %x\n\n", pArg->aiKeyAlg);
return TRUE;
} // end callback function.

//-------------------------------------------------------------------
//  Define MyHandleError

void MyHandleError(char *s)
{
printf("\n An error has occurred. \n");
printf("The error message is %s \n",s);
printf("Last error is %x \n",GetLastError());
exit(1);
} // end MyHandleError.
```



 

 



