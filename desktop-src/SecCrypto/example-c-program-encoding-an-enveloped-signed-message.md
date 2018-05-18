---
Description: 'Creates, signs, and envelopes a message.'
ms.assetid: '1d9d8a7a-0088-41a7-98fe-4f0e9cb21f31'
title: 'Example C Program: Encoding an Enveloped, Signed Message'
---

# Example C Program: Encoding an Enveloped, Signed Message

The following example creates, signs, and envelopes a message, and it illustrates the following tasks and [*CryptoAPI*](security.c_gly#-security-cryptoapi-gly) functions:

-   Acquiring the handle of a CSP using [**CryptAcquireContext**](cryptacquirecontext.md).
-   Opening a system store using [**CertOpenStore**](certopenstore.md).
-   Finding a signer and recipient certificates using [**CertFindCertificateInStore**](certfindcertificateinstore.md).
-   Initializing appropriate data structures for signing an enveloped message.
-   Finding the length of the enveloped message using [**CryptMsgCalculateEncodedLength**](cryptmsgcalculateencodedlength.md).
-   Creating and signs the message using [**CryptMsgOpenToEncode**](cryptmsgopentoencode.md), [**CryptMsgUpdate**](cryptmsgupdate.md), and [**CryptMsgGetParam**](cryptmsggetparam.md).
-   Enveloping the signed and encoded message for a receiver using [**CryptMsgOpenToEncode**](cryptmsgopentoencode.md), [**CryptMsgUpdate**](cryptmsgupdate.md), and [**CryptMsgGetParam**](cryptmsggetparam.md).

This example will fail if a usable private key does not exist in the default [*key container*](security.k_gly#-security-key-container-gly). If the needed private key is not available, code using [**CryptAcquireCertificatePrivateKey**](cryptacquirecertificateprivatekey.md), as demonstrated in the code sample [Example C Program: Sending and Receiving a Signed and Encrypted Message](example-c-program-sending-and-receiving-a-signed-and-encrypted-message.md), can be used.

This example uses the function [**MyHandleError**](myhandleerror.md). The code for this function is included with the sample. Code for this and other auxiliary functions is also listed under [General Purpose Functions](general-purpose-functions.md).


```C++
#pragma comment(lib, "crypt32.lib")

#include <stdio.h>
#include <windows.h>
#include <Wincrypt.h>
#define MY_ENCODING_TYPE  (PKCS_7_ASN_ENCODING | X509_ASN_ENCODING)
void MyHandleError(char *s);

void main(void)
{
//-------------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
// Declare and initialize variables.

BYTE* pbContent = (BYTE*) "Security is our only business.";
                                    // a byte pointer
DWORD cbContent = strlen((char *) pbContent)+1;
                                    // the size of the message
HCERTSTORE hStoreHandle;
HCRYPTPROV hCryptProv;
PCCERT_CONTEXT pSignerCert;         // signer's certificate
PCCERT_CONTEXT pRecipCert;          // receiver's certificate
LPWSTR pswzRecipientName = L"Hortense";
LPWSTR pswzCertSubject = L"Full Test Cert";
PCERT_INFO RecipCertArray[1];
DWORD ContentEncryptAlgSize;
CRYPT_ALGORITHM_IDENTIFIER ContentEncryptAlgorithm;
CMSG_ENVELOPED_ENCODE_INFO EnvelopedEncodeInfo;
DWORD cbEncodedBlob;
BYTE *pbEncodedBlob;
DWORD cbSignedBlob;
BYTE *pbSignedBlob;
HCRYPTMSG hMsg;
DWORD HashAlgSize;
CRYPT_ALGORITHM_IDENTIFIER HashAlgorithm;
CMSG_SIGNER_ENCODE_INFO SignerEncodeInfo;
CERT_BLOB SignerCertBlob;
CERT_BLOB SignerCertBlobArray[1];
CMSG_SIGNER_ENCODE_INFO SignerEncodeInfoArray[1];
CMSG_SIGNED_ENCODE_INFO SignedMsgEncodeInfo;

//-------------------------------------------------------------------
// Begin processing. Display the original message.

printf("The original message => %s\n",pbContent);  

//-------------------------------------------------------------------
// Acquire a cryptographic provider. 

if(CryptAcquireContext(
        &amp;hCryptProv,      // address for handle to be returned
        NULL,             // use the current user's logon name
        NULL,             // use the default provider
        PROV_RSA_FULL,    // provider type
        0))               // zero allows access to private keys
{
    printf("Context CSP acquired. \n");
}
else
{
   if ( GetLastError() == NTE_BAD_KEYSET)
   {
        printf("A Usable private key was not found \n");
        printf("in the default key container. Either a \n");
        printf("private key must be generated in that container \n");
        printf("or CryptAquireCertificatePrivateKey can be used \n");
        printf("to gain access to the needed private key.");
   }
    MyHandleError("CryptAcquireContext failed.");
}
//-------------------------------------------------------------------
// Open the My system certificate store.

if(hStoreHandle = CertOpenStore(
       CERT_STORE_PROV_SYSTEM,
       0,
       NULL,
       CERT_SYSTEM_STORE_CURRENT_USER,
       L"MY"))
{
    printf("The MY system store is open. \n");
}
else
{
    MyHandleError( "Error getting store handle.");
}
//-------------------------------------------------------------------
// Get the signer's certificate. This certificate must be in the
// My store, and its private key must be available.

if(pSignerCert = CertFindCertificateInStore(
   hStoreHandle,
   MY_ENCODING_TYPE,
   0,
   CERT_FIND_SUBJECT_STR,
   pswzCertSubject,
   NULL))
{
    printf("Found certificate for %S.\n",pswzCertSubject);
}
else
{
    MyHandleError("Signer certificate not found.");
}
//-------------------------------------------------------------------
// Initialize the algorithm identifier structure.

HashAlgSize = sizeof(HashAlgorithm);
memset(&amp;HashAlgorithm, 0, HashAlgSize);    // initialize to zero
HashAlgorithm.pszObjId = szOID_RSA_MD5;    // initialize the 
                                           // necessary member
//-------------------------------------------------------------------
// Initialize the CMSG_SIGNER_ENCODE_INFO structure.

memset(&amp;SignerEncodeInfo, 0, sizeof(CMSG_SIGNER_ENCODE_INFO));
SignerEncodeInfo.cbSize = sizeof(CMSG_SIGNER_ENCODE_INFO);
SignerEncodeInfo.pCertInfo = pSignerCert->pCertInfo;
SignerEncodeInfo.hCryptProv = hCryptProv;
SignerEncodeInfo.dwKeySpec = AT_KEYEXCHANGE;
SignerEncodeInfo.HashAlgorithm = HashAlgorithm;
SignerEncodeInfo.pvHashAuxInfo = NULL;

//-------------------------------------------------------------------
// Create an array of one. 
// Note: The current program is set up for only a single signer.

SignerEncodeInfoArray[0] = SignerEncodeInfo;

//-------------------------------------------------------------------
// Initialize the CMSG_SIGNED_ENCODE_INFO structure.

SignerCertBlob.cbData = pSignerCert->cbCertEncoded;
SignerCertBlob.pbData = pSignerCert->pbCertEncoded;

//-------------------------------------------------------------------
// Initialize the array of one CertBlob.

SignerCertBlobArray[0] = SignerCertBlob;
memset(&amp;SignedMsgEncodeInfo, 0, sizeof(CMSG_SIGNED_ENCODE_INFO));
SignedMsgEncodeInfo.cbSize = sizeof(CMSG_SIGNED_ENCODE_INFO);
SignedMsgEncodeInfo.cSigners = 1;
SignedMsgEncodeInfo.rgSigners = SignerEncodeInfoArray;
SignedMsgEncodeInfo.cCertEncoded = 1;
SignedMsgEncodeInfo.rgCertEncoded = SignerCertBlobArray;
SignedMsgEncodeInfo.rgCrlEncoded = NULL;

//-------------------------------------------------------------------
// Get the size of the encoded, signed message BLOB.

if(cbSignedBlob = CryptMsgCalculateEncodedLength(
    MY_ENCODING_TYPE,       // message encoding type
    0,                      // flags
    CMSG_SIGNED,            // message type
    &amp;SignedMsgEncodeInfo,   // pointer to structure
    NULL,                   // inner content OID
    cbContent))             // size of content
{
    printf("%d, the length of data calculated. \n",cbSignedBlob);
}
else
{
   if ( GetLastError() == NTE_BAD_KEYSET)
   {
        printf("A Usable private key was not found \n");
        printf("in the default key container. Either a \n");
        printf("private key must be generated in that container \n");
        printf("or CryptAquireCertificatePRivateKey can be used \n");
        printf("to gain access to the needed private key.");
    }
    MyHandleError("Getting cbSignedBlob length failed.");
}
//-------------------------------------------------------------------
// Allocate memory for the encoded BLOB.

if(pbSignedBlob = (BYTE *) malloc(cbSignedBlob))
{
   printf("Memory has been allocated for the signed message. \n");
}
else
{
   MyHandleError("Memory allocation failed.");
}
//-------------------------------------------------------------------
// Open a message to encode.

if(hMsg = CryptMsgOpenToEncode(
    MY_ENCODING_TYPE,        // encoding type
    0,                       // flags
    CMSG_SIGNED,             // message type
    &amp;SignedMsgEncodeInfo,    // pointer to structure
    NULL,                    // inner content OID
    NULL))                   // stream information (not used)
{
    printf("The message to be encoded has been opened. \n");
}
else
{
    MyHandleError("OpenToEncode failed.");
}
//-------------------------------------------------------------------
// Update the message with the data.

if(CryptMsgUpdate(
     hMsg,         // handle to the message
     pbContent,    // pointer to the content
     cbContent,    // size of the content
     TRUE))        // last call
{
    printf("Content has been added to the encoded message. \n");
}
else
{
    MyHandleError("MsgUpdate failed.");
}
//-------------------------------------------------------------------
// Get the resulting message.

if(CryptMsgGetParam(
    hMsg,                      // handle to the message
    CMSG_CONTENT_PARAM,        // parameter type
    0,                         // index
    pbSignedBlob,              // pointer to the BLOB
    &amp;cbSignedBlob))            // size of the BLOB
{
    printf("Message encoded successfully. \n");
}
else
{
    MyHandleError("MsgGetParam failed.");
}
//-------------------------------------------------------------------
// pbSignedBlob now points to the encoded, signed content.

//-------------------------------------------------------------------
// Get a pointer to the recipient certificate.
// For this program, the recipient's certificate must also be in the
// My store. At this point, only the recipient's public key is needed.
// To open the enveloped message, however, the recipient's 
// private key must also be available.

if(pRecipCert=CertFindCertificateInStore(      
      hStoreHandle,
      MY_ENCODING_TYPE,            // use X509_ASN_ENCODING
      0,                           // no dwFlags needed
      CERT_FIND_SUBJECT_STR,       // find a certificate with a
                                   // subject that matches the 
                                   // string in the next parameter
      pswzRecipientName,           // the Unicode string to be found
                                   // in a certificate's subject
      NULL))                       // NULL for the first call to the
                                   // function
                                   // in all subsequent
                                   // calls, it is the last pointer
                                   // returned by the function
{
     printf("Certificate for %S found. \n", pswzRecipientName);
}
else
{
     MyHandleError("Could not find the countersigner's "
         "certificate.");
}
//-------------------------------------------------------------------
// Initialize the first element of the array of CERT_INFOs. 
// In this example, there is only a single recipient.

RecipCertArray[0] = pRecipCert->pCertInfo;

//-------------------------------------------------------------------
// Initialize the symmetric-encryption algorithm identifier
// structure.

ContentEncryptAlgSize = sizeof(ContentEncryptAlgorithm);
memset(&amp;ContentEncryptAlgorithm, 
       0,
       ContentEncryptAlgSize);               // initialize to zero

//-------------------------------------------------------------------
// Initialize the necessary members. This particular OID does not
// need any parameters. Some OIDs, however, will require that
// the other members be initialized.

ContentEncryptAlgorithm.pszObjId = szOID_RSA_RC4;

//-------------------------------------------------------------------
// Initialize the CMSG_ENVELOPED_ENCODE_INFO structure.

memset(&amp;EnvelopedEncodeInfo, 
       0,
       sizeof(CMSG_ENVELOPED_ENCODE_INFO));
EnvelopedEncodeInfo.cbSize = sizeof(CMSG_ENVELOPED_ENCODE_INFO);
EnvelopedEncodeInfo.hCryptProv = hCryptProv;
EnvelopedEncodeInfo.ContentEncryptionAlgorithm = 
                                        ContentEncryptAlgorithm;
EnvelopedEncodeInfo.pvEncryptionAuxInfo = NULL;
EnvelopedEncodeInfo.cRecipients = 1;
EnvelopedEncodeInfo.rgpRecipients = RecipCertArray;

//-------------------------------------------------------------------
// Get the size of the encoded message BLOB.

if(cbEncodedBlob = CryptMsgCalculateEncodedLength(
     MY_ENCODING_TYPE,        // message encoding type
     0,                       // flags
     CMSG_ENVELOPED,          // message type
     &amp;EnvelopedEncodeInfo,    // pointer to structure
     szOID_RSA_signedData,    // inner content OID
     cbSignedBlob))           // size of content
{
    printf("Length of the encoded BLOB will be %d.\n",cbEncodedBlob);
}
else
{
    MyHandleError("Getting enveloped cbEncodedBlob length failed.");
}
//--------------------------------------------------------------------
// Allocate memory for the encoded BLOB.

if(pbEncodedBlob = (BYTE *) malloc(cbEncodedBlob))
{
    printf("Memory has been allocated for the BLOB. \n");
}
else
{
    MyHandleError("Enveloped malloc operation failed.");
}
//-------------------------------------------------------------------
// Open a message to encode.

if(hMsg = CryptMsgOpenToEncode(
     MY_ENCODING_TYPE,        // encoding type
     0,                       // flags
     CMSG_ENVELOPED,          // message type
     &amp;EnvelopedEncodeInfo,    // pointer to structure
     szOID_RSA_signedData,    // inner content OID
     NULL))                   // stream information (not used)
{
    printf("The message to encode is open. \n");
}
else
{
    MyHandleError("Enveloped OpenToEncode failed.");
}
//-------------------------------------------------------------------
// Update the message with the data.

if(CryptMsgUpdate(
     hMsg,              // handle to the message
     pbSignedBlob,      // pointer to the signed data BLOB
     cbSignedBlob,      // size of the data BLOB
     TRUE))             // last call
{
    printf("The signed BLOB has been added to the message. \n");
}
else
{
    MyHandleError("Enveloped MsgUpdate failed.");
}
//-------------------------------------------------------------------
// Get the resulting message.

if(CryptMsgGetParam(
     hMsg,                  // handle to the message
     CMSG_CONTENT_PARAM,    // parameter type
     0,                     // index
     pbEncodedBlob,         // pointer to the enveloped,
                            // signed data BLOB
     &amp;cbEncodedBlob))       // size of the BLOB
{
    printf("Enveloped message encoded successfully. \n");
}
else
{
    MyHandleError("Enveloped MsgGetParam failed.");
}
//-------------------------------------------------------------------
// Clean up.

CertFreeCertificateContext(pRecipCert);
if(CertCloseStore(
     hStoreHandle,
     CERT_CLOSE_STORE_CHECK_FLAG))
{
  printf("The certificate store closed without a certificate "
      "left open. \n");
}
else
{
  printf("The store closed but a certificate was still open. \n");
}
if(hMsg)
   CryptMsgClose(hMsg);
if(hCryptProv) 
   CryptReleaseContext(hCryptProv,0);
} // end main

//-------------------------------------------------------------------
// This example uses the function MyHandleError, a simple error
// handling function to print an error message and exit 
// the program. 
// For most applications, replace this function with one 
// that does more extensive error reporting.

void MyHandleError(char *s)
{
    fprintf(stderr,"An error occurred in running the program. \n");
    fprintf(stderr,"%s\n",s);
    fprintf(stderr, "Error number %x.\n", GetLastError());
    fprintf(stderr, "Program terminating. \n");
    exit(1);
} // end MyHandleError
```



 

 



