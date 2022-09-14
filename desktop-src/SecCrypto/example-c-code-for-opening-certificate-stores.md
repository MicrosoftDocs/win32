---
description: The following examples provide code to open a variety of common certificate stores. These examples are a series of code fragments and are not stand-alone programs.
ms.assetid: 975a56d1-aa45-470e-b385-753baa1911ff
title: Example C Code for Opening Certificate Stores
ms.topic: article
ms.date: 05/31/2018
---

# Example C Code for Opening Certificate Stores

The following examples provide code to open a variety of common certificate stores. These examples are a series of code fragments and are not stand-alone programs.

The following example opens the My system store.


```C++
HCERTSTORE hSysStore;
hSysStore = CertOpenStore(
   CERT_STORE_PROV_SYSTEM,   // the store provider type
   0,                        // the encoding type is not needed
   NULL,                     // use the default HCRYPTPROV
   CERT_SYSTEM_STORE_CURRENT_USER,
                             // set the store location in a 
                             // registry location
   L"My"    // the store name as a Unicode string
   );

// If call was successful, close hSystStore; otherwise, 
// call print an error message.
if(hSysStore)
{
    if (!(CertCloseStore(hSysStore, 0)))
    {
        printf("Error closing system store.");
    }
}
else
   printf("Error opening system store.");


// Substitute other common system store names
// for "My" 
// including "root", "trust", or "CA".
```



The following example opens a memory store.


```C++
HCERTSTORE hMemStore;
hMemStore = CertOpenStore(
   CERT_STORE_PROV_MEMORY,   // the memory provider type
   0,                        // the encoding type is not needed
   NULL,                     // use the default HCRYPTPROV
   0,                        // accept the default dwFlags
   NULL                      // pvPara is not used
   );

// If call was successful, close hMemStore; otherwise, 
// call print an error message.
if(hMemStore)
{
    if (!(CertCloseStore(hMemStore, 0)))
    {
        printf("Error closing memory store.");
    }
}
else
   printf("Error opening memory store.");
```



The following example opens a store from disk. The example uses the **CreateMyDACL** function, defined in the [Creating a DACL](../secbp/creating-a-dacl.md) topic, to ensure the open file is created with a proper DACL.


```C++
// In this example, the read-only flag is set.
HANDLE       hFile;
HCERTSTORE   hFileStore;
LPCWSTR       pszFileName = L"TestStor2.sto";
SECURITY_ATTRIBUTES sa;   // for DACL

// Create a DACL for the file.
sa.nLength = sizeof(SECURITY_ATTRIBUTES);
sa.bInheritHandle = FALSE;  

// Call function to set the DACL. The DACL
// is set in the SECURITY_ATTRIBUTES 
// lpSecurityDescriptor member.
// if CreateMyDACL(&sa) fails, exit(1)

//  Obtain a file handle.
hFile = CreateFile(
     pszFileName,                  // the file name
     GENERIC_READ|GENERIC_WRITE,   // access mode: 
                                   // read from and write to
                                   // this file
     0,                            // share mode
     &sa,                          // security 
     OPEN_ALWAYS,                  // how to create
     FILE_ATTRIBUTE_NORMAL,        // file attributes
     NULL);                        // template

if (!(hFile))
{
    fprintf(stderr, "Could not create file.\n");
    exit(1);
}

//-------------------------------------------------------------------
//   At this point, read and use data in the open file that precedes
//   the serialized certificate store data. The file pointer must
//   be placed at the beginning of the certificate store data before 
//   CertOpenStore is called with the CERT_STORE_PROV_FILE provider.
//   Open the store.

hFileStore = CertOpenStore(
    CERT_STORE_PROV_FILE,      //  load certificates from a file
    0,                         //  encoding type not used
    NULL,                      //  use the default HCRYPTPROV
    CERT_STORE_READONLY_FLAG,  //  see the LOWORD of dwFlags to make
                               //  the store read-only
    hFile                      //  the handle for the open file 
                               //  that is the source of the 
                               //  certificates
    );

//-------------------------------------------------------------------
// Include code to work with the certificates.
// The data file from which the certificate store information has  
// been read is still open. Any data in that file that follows the 
// serialized store can be read from the file and used at this point.

//-------------------------------------------------------------------
// Close the file store and the file.

if(hFileStore)
{
   if(!(CertCloseStore(
           hFileStore, 
           CERT_CLOSE_STORE_CHECK_FLAG)))
   {
       fprintf(stderr, "Error closing store.\n");
   }
}
else 
{
   fprintf(stderr, "Error opening store.\n");
}

if(!(CloseHandle(hFile)))
{
    fprintf(stderr, "Error closing hFile.\n");
}
```



The following example opens a file-based store using CERT\_STORE\_PROV\_FILENAME.


```C++
#include <windows.h>
#include <stdio.h>
#include "Wincrypt.h"


#define ENCODING_TYPE  (PKCS_7_ASN_ENCODING | X509_ASN_ENCODING)

void main()
{
//  The pvPara parameter here is the name of an existing file.
//  The function fails if the file does not exist.
//  The file is not opened using CreateFile before the call to 
//  CertOpenStore. 
//  CERT_STORE_PROV_FILENAME_A is used if the file name is in ASCII;
//  CERT_STORE_PROV_FILENAME is used if the file name is a
//  Unicode string.

//#define moved
HCERTSTORE    hFileStoreHandle;

hFileStoreHandle = CertOpenStore(
       CERT_STORE_PROV_FILENAME,    // the store provider type
       ENCODING_TYPE,               // if needed, use the usual
                                    // encoding types
       NULL,                        // use the default HCRYPTPROV
       0,                           // accept the default for all
                                    // dwFlags
       L"FileStore.sto" );          // the name of an existing file
                                    // as a Unicode string
if(hFileStoreHandle)
{
   if(!(CertCloseStore(hFileStoreHandle, 0)))
   {
      fprintf(stderr, "Failed to close hFileStoreHandle\n");
   }
}
else
{
   fprintf(stderr, "Failed to open store.\n");
}
```



The following example opens a collection store.


```C++
// Note that the collection store is empty.
// Certificates, CRLs, and CTLs can be added to and found in
// stores that are added as sibling stores to the collection store.

HCERTSTORE  hCollectionStoreHandle;
HCERTSTORE  hSiblingStoreHandle;
hCollectionStoreHandle = CertOpenStore(
     CERT_STORE_PROV_COLLECTION,
     0,        // for CERT_STORE_PROV_COLLECTION,
               // the rest of the parameters
               // are zero or NULL
     NULL,
     0,
     NULL);

// Check that call to CertOpenStore succeeded.
if(!(hCollectionStoreHandle))
{
    fprintf(stderr, "Could not open collection store.\n");
    exit(1);
}

//-------------------------------------------------------------------
// Open the sibling store as a file-based store.

hSiblingStoreHandle = CertOpenStore(
       CERT_STORE_PROV_FILENAME,    // the store provider type
       ENCODING_TYPE,               // if needed, use the usual
                                    // encoding type
       NULL,                        // use the default HCRYPTPROV
       0,                           // accept the default for all
                                    // dwFlags
       L"siblstore.sto");           // the name of an existing file
                                    // as a Unicode string

// Check that call to CertOpenStore succeeded.
if(!(hSiblingStoreHandle))
{
    fprintf(stderr, "Could not open sibling store.\n");
    exit(1);
}


//-------------------------------------------------------------------
// The open sibling store can now be added to the collection 
// using CertAddStoreToCollection and processing of certificates can 
// begin.

if(!(CertAddStoreToCollection(
          hCollectionStoreHandle,
          hSiblingStoreHandle,
          CERT_PHYSICAL_STORE_ADD_ENABLE_FLAG,
          1)))
{
    fprintf(stderr, "Could not add sibling store to collection.\n");
}

//-------------------------------------------------------------------
// All processing of the certificates in the
// collection store will also involve the certificates in the sibling
// store.

// Close the stores.
if(!(CertCloseStore(hCollectionStoreHandle, 0)))
{
   fprintf(stderr, "Failed to close hCollectionStoreHandle\n");
}

if(!(CertCloseStore(hCollectionStoreHandle, 0)))
{
   fprintf(stderr, "Failed to close hCollectionStoreHandle\n");
}
```



The following example opens a register store.


```C++
HCERTSTORE  hRegStore = NULL;

//--------------------------------------------------------------------
// A register subkey be opened with RegOpenKeyEx or 
// RegCreateKeyEx. A handle to the open register subkey, hkResult, is
// returned in one of parameters of RegOpenKeyEx or RegCreateKeyEx.
hRegStore = CertOpenStore(
      CERT_STORE_PROV_REG,
      0,                    // no encoding type is needed
      NULL,                 // accept the default HCRYPTPROV
      0,                    // accept the default dwFlags
      hkResult);            // hkResult is the handle of a 
                            // register subkey opened by RegOpenKeyEx
                            // or created and opened by 
                            // RegCreateKeyEx
// Close hRegStore.
if(!(CertCloseStore(hRegStore, 0)))
{
   fprintf(stderr, "Could not close hRegStore.\n");
}
```



The following example opens a certificate store based on a PKCS \#7 message.


```C++
HCERTSTORE        hLastStore;
CRYPT_DATA_BLOB   message_BLOB;

//-------------------------------------------------------------------
// Initialize the message BLOB.

HCERTSTORE hSystemStore = CertOpenStore(
   CERT_STORE_PROV_SYSTEM,   // the store provider type
   0,                        // the encoding type is not needed
   NULL,                     // use the default HCRYPTPROV
   CERT_SYSTEM_STORE_CURRENT_USER,
                             // the store location in a registry
                             // location
   L"CA");                   // the store name as a Unicode string

message_BLOB.cbData = 0;
message_BLOB.pbData = NULL;

//-------------------------------------------------------------------
// Get the cbData length.

if(CertSaveStore(
        hSystemStore,
        PKCS_7_ASN_ENCODING | X509_ASN_ENCODING,
        CERT_STORE_SAVE_AS_PKCS7,
        CERT_STORE_SAVE_TO_MEMORY,
        &message_BLOB,
        0))
{
    printf("The length is %d \n",message_BLOB.cbData);
}
else
{
// An error has occurred in saving the store. Print an error
// message and exit.
   fprintf(stderr, "Error saving a file store.");
   exit(1);
}

//-------------------------------------------------------------------
// Allocate the memory or pbData.

if( message_BLOB.pbData = (BYTE *)malloc(message_BLOB.cbData))
{
       printf("The function succeeded. \n");
}
else
{
// An error has occurred in memory allocation. Print an error
// message and exit.
   fprintf(stderr, "Error in memory allocation.\n");
   exit(1);
}

//-------------------------------------------------------------------
//  Get the contents of pbData.

if(CertSaveStore(
        hSystemStore,
        PKCS_7_ASN_ENCODING | X509_ASN_ENCODING,
        CERT_STORE_SAVE_AS_PKCS7,
        CERT_STORE_SAVE_TO_MEMORY,
        &message_BLOB,
        0))
{
   printf("Saved the store to a memory BLOB. \n");
}
else
{
// An error has occurred in saving the store. Print an error
// message and exit.
   fprintf(stderr, "Error saving file store.\n");
   exit(1);
}

if( hLastStore = CertOpenStore(
   CERT_STORE_PROV_PKCS7,
   PKCS_7_ASN_ENCODING | X509_ASN_ENCODING,
   NULL,
   0,
   &message_BLOB))
{
       printf("The function succeeded. \n");
}
else
{
// An error has occurred in opening the store. Print an error
// message and exit.
   fprintf(stderr, "Error opening file store.\n");
   exit(1);
}

// Clean up memory.
if(!(CertCloseStore(hSystemStore, 0)))
{
    fprintf(stderr, "Could not close hSystemStore\n");
}
if(!(CertCloseStore(hLastStore, 0)))
{
    fprintf(stderr, "Could not close hLastStore\n");
}
free(message_BLOB.pbData);
```



 

 
