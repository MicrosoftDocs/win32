---
description: The following example demonstrates an alternate process of encoding a signed message, using that signed message as the inner content for an enveloped message. In preparation for decoding, the inner content is tested to determine its inner-content type.
ms.assetid: ba174e3c-bc2f-48bd-a1bf-fec491dc0ce3
title: Alternate Code for Encoding an Enveloped Message
ms.topic: article
ms.date: 05/31/2018
---

# Alternate Code for Encoding an Enveloped Message

The following example demonstrates an alternate process of encoding a signed message, using that signed message as the [*inner content*](../secgloss/i-gly.md) for an enveloped message. In preparation for decoding, the inner content is tested to determine its inner-content type.

This example illustrates the following CryptoAPI functions:

-   [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta)
-   [**CertOpenSystemStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopensystemstorea)
-   [**CryptMsgCalculateEncodedLength**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgcalculateencodedlength)
-   [**CryptMsgOpenToEncode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentoencode)
-   [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate)
-   [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam)
-   [**CryptMsgOpenToDecode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentodecode)
-   [**CertFindCertificateInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindcertificateinstore)
-   [**CryptMsgClose**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgclose)
-   [**CertCloseStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certclosestore)
-   [**CryptReleaseContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptreleasecontext)

This example also uses the functions [**MyHandleError**](myhandleerror.md) and [**GetSignerCert**](getsignercert.md). C code for these functions is included with the example. For code that demonstrates these and other auxiliary functions, see [General Purpose Functions](general-purpose-functions.md).


```C++
//--------------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
// In this and all other examples, 
// use the #define and
// #include statements listed under #includes and #defines.
#pragma comment(lib, "crypt32.lib")

#include <stdio.h>
#include <windows.h>
#include <Wincrypt.h>
#define MY_ENCODING_TYPE  (PKCS_7_ASN_ENCODING | X509_ASN_ENCODING)
void MyHandleError(char *s);

//--------------------------------------------------------------------
// This program uses the function GetSignerCert, declared here and
// defined after main.

PCCERT_CONTEXT GetSignerCert(
     HCERTSTORE hCertStore);

void main(void)
{
//--------------------------------------------------------------------
// Declare and initialize variables. This includes declaring and 
// initializing a pointer to message content to be countersigned 
// and encoded. Usually, the message content will exist somewhere,
// and a pointer to it is passed to the application. 

BYTE* pbContent = (BYTE*)"The message to be countersigned.";
                               // The message
DWORD cbContent;               // Size of message
HCRYPTPROV hCryptProv;         // CSP handle
HCERTSTORE hStoreHandle;       // Store handle
PCCERT_CONTEXT pSignerCert;    // Signer certificate
DWORD HashAlgSize;
CRYPT_ALGORITHM_IDENTIFIER HashAlgorithm;
CMSG_SIGNER_ENCODE_INFO SignerEncodeInfo;
CMSG_SIGNER_ENCODE_INFO SignerEncodeInfoArray[1];
CERT_BLOB SignerCertBlob;
CERT_BLOB SignerCertBlobArray[1];
CMSG_SIGNED_ENCODE_INFO SignedMsgEncodeInfo;
DWORD cbEncodedBlob;
BYTE* pbEncodedBlob;
HCRYPTMSG hMsg;
DWORD cbDecoded;
BYTE *pbDecoded;
PCCERT_CONTEXT pCntrSigCert;
CMSG_SIGNER_ENCODE_INFO CountersignerInfo;
CMSG_SIGNER_ENCODE_INFO CntrSignArray[1];
DWORD cbSignerInfo;
PBYTE pbSignerInfo;
DWORD cbCountersignerInfo;
PCRYPT_ATTRIBUTES pCountersignerInfo;

//--------------------------------------------------------------------
// Begin processing. 

cbContent = strlen((char *) pbContent)+1;
            // One is added to include the final NULL character.
printf("Processing begins.\n");
printf("The length of the original message is %d.\n",cbContent);
printf("Example message:->%s\n", pbContent);

//--------------------------------------------------------------------
// Get a handle to a cryptographic provider. 

if(CryptAcquireContext(
      &hCryptProv,        // Address for handle to be returned
      NULL,               // Use the logon name for the current user
      NULL,               // Use the default provider
      PROV_RSA_FULL,      // Provider type
      0))                 // Zero allows access to private keys
{
   printf("The CSP has been opened.");
}
else
{
    MyHandleError("CryptAcquireContext failed");
}
//--------------------------------------------------------------------
// Open the MY system certificate store.

if(hStoreHandle = CertOpenStore(
     CERT_STORE_PROV_SYSTEM, // The system store will be a 
                             // virtual store.
     0,                      // Encoding type not needed with 
                             // this PROV.
     NULL,                   // Accept the default HCRYPTPROV. 
     CERT_SYSTEM_STORE_CURRENT_USER,
                             // Set the system store location in the
                             // registry.
     L"MY"))                 // Other predefined system stores 
                             // could have been used,
                             // including trust, CA, or root.
{
   printf("Opened the MY system store. \n");
}else
{
   MyHandleError( "Could not open the MY system store.");
}
//--------------------------------------------------------------------
// Get a pointer to the signature certificate of the signer.

if(pSignerCert = GetSignerCert(hStoreHandle))
{
   printf("A signer certificate was found. \n");
}
else
{
   MyHandleError("Error getting signer certificate.");
}
//--------------------------------------------------------------------
// Initialize the algorithm identifier structure.

HashAlgSize = sizeof(HashAlgorithm);
memset(&HashAlgorithm, 0, HashAlgSize);  // Initialize to zero,
HashAlgorithm.pszObjId = szOID_RSA_MD5;  // then set the 
                                         // necessary member.

//--------------------------------------------------------------------
// Initialize the CMSG_SIGNER_ENCODE_INFO structure.

memset(&SignerEncodeInfo, 0, sizeof(CMSG_SIGNER_ENCODE_INFO));
SignerEncodeInfo.cbSize = sizeof(CMSG_SIGNER_ENCODE_INFO);
SignerEncodeInfo.pCertInfo = pSignerCert->pCertInfo;
SignerEncodeInfo.hCryptProv = hCryptProv;
SignerEncodeInfo.dwKeySpec = AT_KEYEXCHANGE;
SignerEncodeInfo.HashAlgorithm = HashAlgorithm;
SignerEncodeInfo.pvHashAuxInfo = NULL;

//--------------------------------------------------------------------
// Initialize the first element of an array of signers. 
// There can be only one signer.

SignerEncodeInfoArray[0] = SignerEncodeInfo;

//--------------------------------------------------------------------
// Initialize the CMSG_SIGNED_ENCODE_INFO structure.

SignerCertBlob.cbData = pSignerCert->cbCertEncoded;
SignerCertBlob.pbData = pSignerCert->pbCertEncoded;

//--------------------------------------------------------------------
//  Initialize the first element of an array of signer BLOBs.
//  Only one signer BLOB used.

SignerCertBlobArray[0] = SignerCertBlob;
memset(&SignedMsgEncodeInfo, 0, sizeof(CMSG_SIGNED_ENCODE_INFO));
SignedMsgEncodeInfo.cbSize = sizeof(CMSG_SIGNED_ENCODE_INFO);
SignedMsgEncodeInfo.cSigners = 1;
SignedMsgEncodeInfo.rgSigners = SignerEncodeInfoArray;
SignedMsgEncodeInfo.cCertEncoded = 1;
SignedMsgEncodeInfo.rgCertEncoded = SignerCertBlobArray;
SignedMsgEncodeInfo.rgCrlEncoded = NULL;

//--------------------------------------------------------------------
// Get the size of the encoded message BLOB.

if(cbEncodedBlob = CryptMsgCalculateEncodedLength(
       MY_ENCODING_TYPE,     // Message encoding type
       0,                    // Flags
       CMSG_SIGNED,          // Message type
       &SignedMsgEncodeInfo, // Pointer to structure
       NULL,                 // Inner content OID
       cbContent))           // Size of content
{
   printf("The size for the encoded BLOB is %d.\n",cbEncodedBlob);
}
else
{
    MyHandleError("Getting cbEncodedBlob length failed.");
}
//--------------------------------------------------------------------
// Allocate memory for the encoded BLOB.

if(pbEncodedBlob = (BYTE *) malloc(cbEncodedBlob))
{
   printf("Memory has been allocated for the BLOB. \n");
}
else
{
   MyHandleError("Malloc operation failed.");
}
//--------------------------------------------------------------------
// Open a message to encode.

if(hMsg = CryptMsgOpenToEncode(
         MY_ENCODING_TYPE,      // Encoding type
         0,                     // Flags
         CMSG_SIGNED,           // Message type
         &SignedMsgEncodeInfo,  // Pointer to structure
         NULL,                  // Inner content OID
         NULL))                 // Stream information (not used)
{
   printf("The message to encode is open. \n");
}
else
{
   MyHandleError("OpenToEncode failed");
}
//-------------------------------------------------------------
// Update the message with the data.

if(CryptMsgUpdate(
      hMsg,       // Handle to the message
      pbContent,  // Pointer to the content
      cbContent,  // Size of the content
      TRUE))      // Last call
{
   printf("Message to encode has been updated. \n");
}
else
{
   MyHandleError("MsgUpdate failed");
}
//--------------------------------------------------------------------
// Get the resulting message.

if(CryptMsgGetParam(
        hMsg,               // Handle to the message
        CMSG_CONTENT_PARAM, // Parameter type
        0,                  // Index
        pbEncodedBlob,      // Pointer to the BLOB
        &cbEncodedBlob))    // Size of the BLOB
{
   printf("Message successfully signed. \n");
}
else
{
   MyHandleError("MsgGetParam failed.");
}
//--------------------------------------------------------------------
// pbEncodedBlob points to the encoded, signed content.
// Include any further processing here.

CryptMsgClose(hMsg); // The message is complete--close the handle.

//--------------------------------------------------------------------
// Next, countersign the signed message. 
// Assume that the message just created and that a pointer
// (pbEncodedBlob) to the message were sent to the intended 
// recipient.
// The following code, from the recipient's point of view, adds a 
// countersignature to the signed message.
//
// Before countersigning, the message must be decoded.

//--------------------------------------------------------------------
// Open a message for decoding.

if(hMsg = CryptMsgOpenToDecode(
       MY_ENCODING_TYPE,   // Encoding type
       0,                  // Flags
       0,                  // Message type (get from message)
       hCryptProv,         // Cryptographic provider
       NULL,               // Recipient information
       NULL))              // Stream information
{
   printf("The message for decoding has been opened. \n");
}
else
{
   MyHandleError("OpenToDecode failed.");
}
//--------------------------------------------------------------------
// Update the message with the data (encoded BLOB).
// In this example, pbEncodedBlob and cbEncodedBlob were
// created in the previous code.

if(CryptMsgUpdate(
   hMsg,            // Handle to the message
   pbEncodedBlob,   // Pointer to the encoded BLOB
   cbEncodedBlob,   // Size of the encoded BLOB
   TRUE))           // Last call
{
   printf("The message to be decoded has been updated. \n");
}
else
{
   MyHandleError("Decode MsgUpdate failed.");
}
//--------------------------------------------------------------------
// Get the size of the content.

if(CryptMsgGetParam(
      hMsg,                    // Handle to the message
      CMSG_CONTENT_PARAM,      // Parameter type
      0,                       // Index
      NULL,                    // Address for returned 
                               // information
      &cbDecoded))             // Size of the returned 
                               // information
{
   printf("The message to be decoded is %d bytes long. \n", 
       cbDecoded);
}
else
{
   MyHandleError("Decode CMSG_CONTENT_PARAM failed");
}
//--------------------------------------------------------------------
// Allocate memory.

if(pbDecoded = (BYTE *) malloc(cbDecoded))
{
   printf("Memory has been allocated. \n");
}
else
{
   MyHandleError("Decode memory allocation failed");
}
//--------------------------------------------------------------------
// Get a pointer to the content.

if(CryptMsgGetParam(
      hMsg,                // Handle to the message
      CMSG_CONTENT_PARAM,  // Parameter type
      0,                   // Index
      pbDecoded,           // Address for returned information
      &cbDecoded))         // Size of the returned information
{
    printf("The successfully decoded message is =>%s\n",pbDecoded);
}
else
{
   MyHandleError("Decode CMSG_CONTENT_PARAM #2 failed.");
}
//--------------------------------------------------------------------
// Proceed with the countersigning.

//--------------------------------------------------------------------
// Initialize the CRYPT_ALGORITHM_IDENTIFIER structure. In this 
// case, the initialization performed for signing the message in 
// the previous code is used.

//--------------------------------------------------------------------
// Get the certificate of the countersigner. A certificate with a 
// subject name that matches the string in parameter five must  
// be in the MY store and must have its CERT_KEY_PROV_INFO_PROP_ID 
// property set.

if(pCntrSigCert=CertFindCertificateInStore(      
      hStoreHandle,
      MY_ENCODING_TYPE,            // Use X509_ASN_ENCODING.
      0,                           // No dwFlags needed. 
      CERT_FIND_SUBJECT_STR,       // Find a certificate with a
                                   // subject that matches the string
                                   // in the next parameter.
      L"Full Test Cert",           // The Unicode string to be found
                                   // in a certificate's subject.
      NULL))                       // NULL for the first call to the
                                   // function. In all subsequent
                                   // calls, it is the last pointer
                                   // returned by the function.
{
  printf("The desired certificate was found. \n");
}
else
{
   MyHandleError("Could not find the countersigner's certificate.");
}
//--------------------------------------------------------------------
// Initialize the PCMSG_SIGNER_ENCODE_INFO structure.

memset(&CountersignerInfo, 0, sizeof(CMSG_SIGNER_ENCODE_INFO));
CountersignerInfo.cbSize = sizeof(CMSG_SIGNER_ENCODE_INFO);
CountersignerInfo.pCertInfo = pCntrSigCert->pCertInfo;
CountersignerInfo.hCryptProv = hCryptProv;
CountersignerInfo.dwKeySpec = AT_KEYEXCHANGE;
CountersignerInfo.HashAlgorithm = HashAlgorithm;

CntrSignArray[0] = CountersignerInfo;

//--------------------------------------------------------------------
// Countersign the message.

if(CryptMsgCountersign(
       hMsg,
       0,
       1,
       CntrSignArray))
{
    printf("Countersign succeeded. \n");
}
else
{
    MyHandleError("Countersign failed.");
}
//--------------------------------------------------------------------
// Get a pointer to the new, countersigned message BLOB.
// Get the size of memory required.

if(CryptMsgGetParam(
      hMsg,                  // Handle to the message
      CMSG_ENCODED_MESSAGE,  // Parameter type
      0,                     // Index
      NULL,                  // Address for returned information
      &cbEncodedBlob))       // Size of the returned information
{
   printf("The size for the encoded BLOB is %d.\n",cbEncodedBlob);
}
else
{
   MyHandleError("Sizing of cbSignerInfo failed.");
}
//--------------------------------------------------------------------
// Allocate memory.

if(pbEncodedBlob = (BYTE*) malloc(cbEncodedBlob))
{
   printf("%d bytes allocated .\n", cbEncodedBlob);
}
else
{
    MyHandleError("cbSignerInfo memory allocation failed");
}
//--------------------------------------------------------------------
// Get the new message encoded BLOB.

if(CryptMsgGetParam(
     hMsg,                   // Handle to the message
     CMSG_ENCODED_MESSAGE,   // Parameter type
     0,                      // Index
     pbEncodedBlob,          // Address for returned information
     &cbEncodedBlob))        // Size of the returned information
{
    printf("The message is complete. \n");
}
else
{
    MyHandleError("Getting pbEncodedBlob failed");
}
//-------------------------------------------------------------------
//  The message is complete. Close the handle.
CryptMsgClose(hMsg); 

//--------------------------------------------------------------------
// Verify the countersignature.
// Assume that the countersigned message went back to the originator, 
// where, again, it will be decoded.

//--------------------------------------------------------------------
// Before verifying the countersignature, the message must first
// be decoded.

//--------------------------------------------------------------------
// Open a message for decoding.

if(hMsg = CryptMsgOpenToDecode(
      MY_ENCODING_TYPE,    // Encoding type
      0,                   // Flags
      0,                   // Message type (get from message)
      hCryptProv,          // Cryptographic provider
      NULL,                // Recipient information
      NULL))               // Stream information
{
   printf("The message to decode has been opened. \n");
}
else
{
   MyHandleError("OpenToDecode failed.");
}
//--------------------------------------------------------------------
// Update the message with the encoded BLOB.
// In this example, pbEncodedBlob and cbEncodedBlob were
// initialized in the previous code.

if(CryptMsgUpdate(
      hMsg,            // Handle to the message
      pbEncodedBlob,   // Pointer to the encoded BLOB
      cbEncodedBlob,   // Size of the encoded BLOB
      TRUE))           // Last call
{
   printf("The message to decode has been updated. \n");
}
else
{
    MyHandleError("Updating of the verified countersignature "
        "message failed.");
}
//-------------------------------------------------------------
// Get a pointer to the CERT_INFO member of the certificate of the  
// countersigner. In this case, the certificate retrieved in the
// previous code segment will be used (pCntrSigCert).

//--------------------------------------------------------------
// Retrieve the signer information from the message.
// Get the size of memory required.

if(CryptMsgGetParam(
      hMsg,                  // Handle to the message
      CMSG_ENCODED_SIGNER,   // Parameter type
      0,                     // Index
      NULL,                  // Address for returned information
      &cbSignerInfo))        // Size of the returned information
{
   printf("The size of the signer information has been "
       "retrieved.\n");
}
else
{
    MyHandleError("Sizing of cbSignerInfo failed.");
}
//--------------------------------------------------------------------
// Allocate memory.

if(pbSignerInfo = (BYTE*) malloc(cbSignerInfo))
{
   printf("%d bytes allocated for the signer "
       "information. \n", cbSignerInfo);
}
else
{
    MyHandleError("cbSignerInfo memory allocation failed");
}
//--------------------------------------------------------------------
// Get the message signer information.

if(CryptMsgGetParam(
      hMsg,                 // Handle to the message
      CMSG_ENCODED_SIGNER,  // Parameter type
      0,                    // Index
      pbSignerInfo,         // Address for returned information
      &cbSignerInfo))       // Size of the returned information
{
   printf("The signer information is retrieved. \n");
}
else
{
   MyHandleError("Getting pbSignerInfo failed.");
}
//--------------------------------------------------------------------
// Retrieve the countersigner information from the message.
// Get the size of memory required.

if(CryptMsgGetParam(
       hMsg,                         // Handle to the message
       CMSG_SIGNER_UNAUTH_ATTR_PARAM,// Parameter type
       0,                            // Index
       NULL,                         // Address for returned 
                                     // information
       &cbCountersignerInfo))        // Size of returned 
                                     // information
{
   printf("The length of the countersigner's information is "
       "retrieved. \n");
}
else
{
   MyHandleError("Sizing of cbCountersignerInfo failed.");
}
//--------------------------------------------------------------------
// Allocate memory.

if(pCountersignerInfo =
         (CRYPT_ATTRIBUTES*)malloc(cbCountersignerInfo))
{
   printf("%d bytes allocated. \n", cbCountersignerInfo);
}
else
{
    MyHandleError("pbCountersignInfo memory allocation failed.");
}
//--------------------------------------------------------------------
// Get the message SIGNER_INFO.

if(CryptMsgGetParam(
     hMsg,                           // Handle to the message
     CMSG_SIGNER_UNAUTH_ATTR_PARAM,  // Parameter type
     0,                              // Index
     pCountersignerInfo,             // Address for returned 
                                     // information
     &cbCountersignerInfo))          // Size of the returned 
                                     // information
{
   printf("Countersigner information retrieved. \n");
}
else
{
    MyHandleError("Getting pbCountersignerInfo failed.");
}
//--------------------------------------------------------------------
// Verify the countersignature.

if(CryptMsgVerifyCountersignatureEncoded(
     hCryptProv,
     MY_ENCODING_TYPE,
     pbSignerInfo,
     cbSignerInfo,
     pCountersignerInfo->rgAttr->rgValue->pbData,
     pCountersignerInfo->rgAttr->rgValue->cbData,
     pCntrSigCert->pCertInfo))
{
     printf("Verification of countersignature succeeded. \n");
}
else
{
     printf("Verification of countersignature failed. \n");
}
//--------------------------------------------------------------------
// Clean up.

free(pbEncodedBlob);
free(pbDecoded);
free(pbSignerInfo);
free(pCountersignerInfo);
CertCloseStore(
     hStoreHandle, 
     CERT_CLOSE_STORE_FORCE_FLAG);
CryptMsgClose(hMsg);
CryptReleaseContext(hCryptProv,0);

} // End of main

//--------------------------------------------------------------------
// Define function MyHandleError.
void MyHandleError(char *s)
{
    fprintf(stderr,"An error occurred in running the program. \n");
    fprintf(stderr,"%s\n",s);
    fprintf(stderr,"Error number %x.\n",GetLastError());
    fprintf(stderr,"Program terminating. \n");
    exit(1);
}

// GetSignerCert enumerates the certificates in a store and
// finds the first certificate that has a signature key. If a 
// certificate is found, a pointer to the certificate is returned.

PCCERT_CONTEXT GetSignerCert(
        HCERTSTORE hCertStore)
//--------------------------------------------------------------------
// Parameter passed in:
// hCertStore, the handle of the store to be searched.

{
//--------------------------------------------------------------------
// Declare and initialize local variables.

PCCERT_CONTEXT       pCertContext = NULL;
BOOL                 fMore = TRUE;
DWORD                dwSize = NULL;
CRYPT_KEY_PROV_INFO* pKeyInfo = NULL;
DWORD                PropId = CERT_KEY_PROV_INFO_PROP_ID;

//--------------------------------------------------------------------
// Find certificates in the store until the end of the store
// is reached or a certificate with an AT_SIGNATURE key is found.

while(fMore && 
  (pCertContext= CertFindCertificateInStore(
     hCertStore,           // Handle of the store to be searched.
     0,                    // Encoding type. Not used for this search.
     0,                    // dwFindFlags. Special find criteria.
                           // Not used in this search.
     CERT_FIND_PROPERTY,   // Find type. Determines the kind of  
                           // search to be done. In this case, search 
                           // for certificates that have a specific 
                           // extended property.
     &PropId,              // pvFindPara. Gives the specific 
                           // value searched for, here the identifier
                           // of an extended property.
     pCertContext)))       // pCertContext is NULL for the 
                           // first call to the function. 
                           // If the function were being called
                           // in a loop, after the first call,
                           // pCertContext would be the certificate
                           // returned by the previous call.
{
//-------------------------------------------------------------
// For simplicity, this code only searches 
// for the first occurrence of an AT_SIGNATURE key. 
// In many situations, a search would also look for a 
// specific subject name as well as the key type.

//-------------------------------------------------------------
// Call CertGetCertificateContextProperty once to get the
// returned structure size.

   if(!(CertGetCertificateContextProperty(
                 pCertContext,
                 CERT_KEY_PROV_INFO_PROP_ID,
                 NULL,
                 &dwSize)))
   {
      MyHandleError("Error getting key property");
   }
//--------------------------------------------------------------
// Allocate memory for the returned structure.
    
   if(pKeyInfo)
        free(pKeyInfo);
   if(!(pKeyInfo = (CRYPT_KEY_PROV_INFO*)malloc(dwSize)))
   {
       MyHandleError("Error allocating memory for pKeyInfo");
   }
   //--------------------------------------------------------------
   // Get the key information structure.

   if(!(CertGetCertificateContextProperty(
       pCertContext,
       CERT_KEY_PROV_INFO_PROP_ID,
       pKeyInfo,
       &dwSize)))
   {
       MyHandleError("The second call to the function failed.");
   }
   //-------------------------------------------     
   // Check the dwKeySpec member for a signature key.
   if(pKeyInfo->dwKeySpec == AT_SIGNATURE)
   {
        fMore  = FALSE;
    }
}  // End of while loop

if(pKeyInfo)
   free(pKeyInfo);
return (pCertContext);
}  // End of GetSignerCert.

```



 

 
