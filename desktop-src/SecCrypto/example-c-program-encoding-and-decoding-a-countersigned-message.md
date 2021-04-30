---
description: Shows how to encode and decode a countersigned message. This example uses the MyHandleError example function. Code for the MyHandleError function and other auxiliary functions is also listed under General Purpose Functions.
ms.assetid: 12930d4d-2ea5-4d95-b9cf-4f0dd351ce05
title: 'Example C Program: Encoding and Decoding a Countersigned Message'
ms.topic: article
ms.date: 05/31/2018
---

# Example C Program: Encoding and Decoding a Countersigned Message

The following example shows how to encode and decode a countersigned message. This example uses the [**MyHandleError**](myhandleerror.md) example function. Code for the **MyHandleError** function and other auxiliary functions is also listed under [General Purpose Functions](general-purpose-functions.md).


```C++
#include <stdafx.h>

#include <stdlib.h>
#include <stdio.h>
#include <tchar.h>
#include <windows.h>
#include <wincrypt.h>

// Link with the Crypt32.lib file.
#pragma comment (lib, "crypt32")

#define MY_ENCODING_TYPE  (PKCS_7_ASN_ENCODING | X509_ASN_ENCODING)

//-------------------------------------------------------------------
//   Define the names of two certificate subjects.
//   To use this program, the definitions of SIGNER_NAME and 
//   COUNTER_SIGNER_NAME must be changed to the names of 
//   the subjects of certificates that have access to private keys. 
//   These certificates must have either the 
//   CERT_KEY_PROV_INFO_PROP_ID or CERT_KEY_CONTEXT_PROP_ID 
//   property set for the contexts to provide access to private 
//   signature keys.

#define SIGNER_NAME L"Insert_signer_name_here"
#define COUNTER_SIGNER_NAME L"Insert_counter_signer_name_here"

#define MAX_NAME 256

void MyHandleError(char *s);

int _tmain(int argc, _TCHAR* argv[])
{
    //---------------------------------------------------------------
    // Declare and initialize variables. This includes declaring and 
    // initializing a pointer to message content to be countersigned 
    // and encoded. Usually, the message content will exist somewhere
    // and a pointer to it is passed to the application. 

    BYTE* pbContent;
    DWORD cbContent;
    HCRYPTPROV hCryptProv;
    HCERTSTORE hStoreHandle;
    PCCERT_CONTEXT pSignerCert;
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
    char pszNameString[MAX_NAME];
    CRYPT_VERIFY_MESSAGE_PARA VerifyParams;
    BYTE *pbDecodedMessageBlob;
    DWORD cbDecodedMessageBlob;
    DWORD dwKeySpec;

    // The message.
    pbContent = (BYTE*)"I must go back to where all messages start.";

    //---------------------------------------------------------------
    // Begin processing. 

    //---------------------------------------------------------------
    //  Initialize cbContent to the length of pbContent
    //  including the terminating NULL character.
    cbContent = lstrlenA((char *) pbContent) + 1;

    printf("The example message is ->.\n");
    printf("%s\n\n", pbContent);

    //---------------------------------------------------------------
    // Open the MY system certificate store.
    if(!(hStoreHandle = CertOpenStore(
        CERT_STORE_PROV_SYSTEM,
        0,
        NULL,
        CERT_SYSTEM_STORE_CURRENT_USER,
        L"MY")))
    {
        MyHandleError("Could not open the MY system store.");
    }

    //---------------------------------------------------------------
    // Get a pointer to a signer's signature certificate.
    if(pSignerCert = CertFindCertificateInStore(
        hStoreHandle,
        MY_ENCODING_TYPE,
        0,
        CERT_FIND_SUBJECT_STR,
        SIGNER_NAME,
        NULL))
    {
        //-----------------------------------------------------------
        // A certificate was found. Get and print the name of the 
        // subject of the certificate.
        if(CertGetNameStringA(
            pSignerCert,
            CERT_NAME_SIMPLE_DISPLAY_TYPE,
            0,
            NULL,
            pszNameString,
            MAX_NAME) > 1)
         {
            printf("The message signer is %s.\n",pszNameString);
         }
         else
         {
            MyHandleError("Getting the signer name failed.\n");
         }
    }
    else
    {
        MyHandleError("Cert not found.\n");
    }

    //---------------------------------------------------------------
    // Initialize the CMSG_SIGNER_ENCODE_INFO structure.

    //---------------------------------------------------------------
    // Get a handle to a cryptographic provider. 
    if(!(CryptAcquireCertificatePrivateKey(
        pSignerCert,
        0,
        NULL,
        &hCryptProv,
        &dwKeySpec,
        NULL)))
    {
        MyHandleError("CryptAcquireContext failed.");
    }
     
    memset(&SignerEncodeInfo, 0, sizeof(CMSG_SIGNER_ENCODE_INFO));
    SignerEncodeInfo.cbSize = sizeof(CMSG_SIGNER_ENCODE_INFO);
    SignerEncodeInfo.pCertInfo = pSignerCert->pCertInfo;
    SignerEncodeInfo.hCryptProv = hCryptProv;
    SignerEncodeInfo.dwKeySpec = dwKeySpec;
    SignerEncodeInfo.HashAlgorithm.pszObjId = szOID_RSA_MD5;
    SignerEncodeInfo.pvHashAuxInfo = NULL;

    //---------------------------------------------------------------
    // Initialize the first element of an array of signers. 
    // Note: Currently, there is only one signer.
    SignerEncodeInfoArray[0] = SignerEncodeInfo;

    //---------------------------------------------------------------
    // Initialize the CMSG_SIGNED_ENCODE_INFO structure.
    SignerCertBlob.cbData = pSignerCert->cbCertEncoded;
    SignerCertBlob.pbData = pSignerCert->pbCertEncoded;

    //---------------------------------------------------------------
    //  Initialize the first element of an array of signer BLOBs.
    //  Note: In this program, only one signer BLOB is used.
    SignerCertBlobArray[0] = SignerCertBlob;
    memset(&SignedMsgEncodeInfo, 0, sizeof(CMSG_SIGNED_ENCODE_INFO));
    SignedMsgEncodeInfo.cbSize = sizeof(CMSG_SIGNED_ENCODE_INFO);
    SignedMsgEncodeInfo.cSigners = 1;
    SignedMsgEncodeInfo.rgSigners = SignerEncodeInfoArray;
    SignedMsgEncodeInfo.cCertEncoded = 1;
    SignedMsgEncodeInfo.rgCertEncoded = SignerCertBlobArray;

    //---------------------------------------------------------------
    // Get the size of the encoded message BLOB.
    cbEncodedBlob = CryptMsgCalculateEncodedLength(
        MY_ENCODING_TYPE,
        0,
        CMSG_SIGNED,
        &SignedMsgEncodeInfo,
        NULL,
        cbContent);
    if(!cbEncodedBlob)
    {
        MyHandleError("Getting cbEncodedBlob length failed.");
    }

    //---------------------------------------------------------------
    // Allocate memory for the encoded BLOB.
    pbEncodedBlob = (BYTE *) malloc(cbEncodedBlob);
    if(!pbEncodedBlob)
    {
       MyHandleError("malloc operation failed.");
    }

    //---------------------------------------------------------------
    // Open a message to encode.
    hMsg = CryptMsgOpenToEncode(
        MY_ENCODING_TYPE,
        0,
        CMSG_SIGNED,
        &SignedMsgEncodeInfo,
        NULL,
        NULL);
    if(!hMsg)
    {
        MyHandleError("OpenToEncode failed.");
    }

    //---------------------------------------------------------------
    // Update the message with the data.
    if(!(CryptMsgUpdate(
        hMsg,
        pbContent,
        cbContent,
        TRUE)))
    {
        MyHandleError("CryptMsgUpdate failed.");
    }

    //---------------------------------------------------------------
    // Get the resulting message.
    if(CryptMsgGetParam(
        hMsg,
        CMSG_CONTENT_PARAM,
        0,
        pbEncodedBlob,
        &cbEncodedBlob))
    {
        printf("Message successfully signed.\n");
    }
    else
    {
        MyHandleError("CryptMsgGetParam failed.");
    }

    //---------------------------------------------------------------
    // The message is signed and encoded.
    // Close the message handle and the certificate store.
    CryptMsgClose(hMsg);
    CertCloseStore(hStoreHandle, CERT_CLOSE_STORE_FORCE_FLAG);
    CryptReleaseContext(hCryptProv,0);

    //---------------------------------------------------------------
    // Next, countersign the signed message. 
    // Assume that pbEncodedBlob, the message just created, was sent 
    // to an intended recipient.

    // From the recipient's point of view, the following code 
    // completes these steps: 
    //     1.  Decodes the message
    //     2.  Verifies the signature on the message
    //     3.  Adds a countersignature to the signed message
    //
    // The counter-signed message is returned to the original signer 
    // of the message, where the counter-signature is verified.

    //---------------------------------------------------------------
    // Open a message for decoding.
    hMsg = CryptMsgOpenToDecode(
        MY_ENCODING_TYPE,
        0,
        0,
        NULL,
        NULL,
        NULL);
    if(!hMsg)
    {
        MyHandleError("CryptOpenToDecode failed.");
    }

    //---------------------------------------------------------------
    // Update the message with the encoded BLOB.
    if(!(CryptMsgUpdate(
        hMsg,
        pbEncodedBlob,
        cbEncodedBlob,
        TRUE)))
    {
        MyHandleError("Decode CryptMsgUpdate failed.");
    }

    //---------------------------------------------------------------
    // Get the size of the message.
    if(CryptMsgGetParam(
        hMsg,
        CMSG_CONTENT_PARAM,
        0,
        NULL,
        &cbDecoded))
    {
        printf("The message is %d bytes long.\n", cbDecoded);
    }
    else
    {
        MyHandleError("Decode CMSG_CONTENT_PARAM failed.");
    }

    //---------------------------------------------------------------
    // Allocate memory.
    pbDecoded = (BYTE*)malloc(cbDecoded);
    if(!pbDecoded)
    {
        MyHandleError("Decode memory allocation failed.");
    }

    //---------------------------------------------------------------
    // Copy the message to the buffer.
    if(CryptMsgGetParam(
        hMsg,
        CMSG_CONTENT_PARAM,
        0,
        pbDecoded,
        &cbDecoded))
    {
        printf("The successfully decoded message is -> ");
        printf("%s\n", pbDecoded);
    }
    else
    {
        MyHandleError("Decode CMSG_CONTENT_PARAM #2 failed.");
    }

    //---------------------------------------------------------------
    //  Check the signature. 
    //  Initialize the VerifyParams data structure.
    VerifyParams.cbSize = sizeof(CRYPT_VERIFY_MESSAGE_PARA);
    VerifyParams.dwMsgAndCertEncodingType = MY_ENCODING_TYPE;
    VerifyParams.hCryptProv = 0;
    VerifyParams.pfnGetSignerCertificate = NULL;
    VerifyParams.pvGetArg = NULL;

    if(!(CryptVerifyMessageSignature(
        &VerifyParams,
        0,
        pbEncodedBlob,
        cbEncodedBlob,
        NULL,
        &cbDecodedMessageBlob,
        NULL)))
    {
        printf("Getting the size of the verification message " \
            "failed.\n");
    }

    pbDecodedMessageBlob = (BYTE*)malloc(cbDecodedMessageBlob);
    if(!pbDecodedMessageBlob)
    {
        MyHandleError("Memory allocation failed.");
    }

    if(CryptVerifyMessageSignature(
        &VerifyParams,
        0,
        pbEncodedBlob,
        cbEncodedBlob,
        pbDecodedMessageBlob,
        &cbDecodedMessageBlob,
        NULL))
    {
        printf("The Signature verified message is -> \n");
        printf("%s \n\n",pbDecodedMessageBlob);
    }
    else
    {
        MyHandleError("Verification message failed.");
    }

    //---------------------------------------------------------------
    // Proceed with the countersigning.
    // First, open a certificate store.
    if(!(hStoreHandle = CertOpenStore(
         CERT_STORE_PROV_SYSTEM, 
         0,                     
         NULL,
         CERT_SYSTEM_STORE_CURRENT_USER,
         L"MY")))
    {
        MyHandleError("Could not open the MY system store.");
    }

    //---------------------------------------------------------------
    // Get the countersigner's certificate. 
    if(pCntrSigCert = CertFindCertificateInStore(
        hStoreHandle,
        MY_ENCODING_TYPE,            
        0,                           
        CERT_FIND_SUBJECT_STR,       
        COUNTER_SIGNER_NAME,         
        NULL))
    {
        if(CertGetNameStringA(
            pCntrSigCert ,
            CERT_NAME_SIMPLE_DISPLAY_TYPE,
            0,
            NULL,
            pszNameString,
            MAX_NAME) > 1)
        {
            printf("The counter signer is %s.\n", pszNameString);
        }
        else
        {
            MyHandleError("Getting the countersigner name " \
                "failed.\n");
        }
    }
    else
    {
        MyHandleError("Could not find the countersigner's " \
           "certificate.");
    }

    //---------------------------------------------------------------
    // Initialize the CMSG_SIGNER_ENCODE_INFO structure.
    if(!(CryptAcquireCertificatePrivateKey(
        pCntrSigCert,
        0,
        NULL,
        &hCryptProv,
        &dwKeySpec,
        NULL)))
    {
        MyHandleError("CryptAcquireContext failed.");
    }

    memset(&CountersignerInfo, 0, sizeof(CMSG_SIGNER_ENCODE_INFO));
    CountersignerInfo.cbSize = sizeof(CMSG_SIGNER_ENCODE_INFO);
    CountersignerInfo.pCertInfo = pCntrSigCert->pCertInfo;
    CountersignerInfo.hCryptProv = hCryptProv;
    CountersignerInfo.dwKeySpec = dwKeySpec;
    CountersignerInfo.HashAlgorithm.pszObjId = szOID_RSA_MD5;

    CntrSignArray[0] = CountersignerInfo;

    //---------------------------------------------------------------
    // Countersign the message.
    if(CryptMsgCountersign(
        hMsg,
        0,
        1,
        CntrSignArray))
    {
        printf("CryptMsgCountersign succeeded.\n");
    }
    else
    {
        MyHandleError("CryptMsgCountersign failed.");
    }

    //---------------------------------------------------------------
    // Get a pointer to the new, countersigned message BLOB.
    // Get the size of memory required.
    if(CryptMsgGetParam(
        hMsg,
        CMSG_ENCODED_MESSAGE,
        0,
        NULL,
        &cbEncodedBlob))
    {
        printf("The size of the encoded BLOB is %d.\n",
           cbEncodedBlob);
    }
    else
    {
        MyHandleError("Sizing of cbSignerInfo failed.");
    }

    //---------------------------------------------------------------
    // Allocate memory.
    pbEncodedBlob = (BYTE*) malloc(cbEncodedBlob);
    if(pbEncodedBlob)
    {
        printf("%d bytes allocated.\n", cbEncodedBlob);
    }
    else
    {
        MyHandleError("cbSignerInfo memory allocation failed.");
    }

    //---------------------------------------------------------------
    // Get the new message encoded BLOB.
    if(CryptMsgGetParam(
        hMsg,
        CMSG_ENCODED_MESSAGE,
        0,
        pbEncodedBlob,
        &cbEncodedBlob))
    {
        printf("The message is complete. \n");
    }
    else
    {
        MyHandleError("Getting pbEncodedBlob failed.");
    }

    //---------------------------------------------------------------
    //  The message is complete. Close the handle.
    CryptMsgClose(hMsg); 

    //---------------------------------------------------------------
    // Verify the countersignature.
    // Assume that the countersigned message 
    // went back to the originator, 
    // where, again, it will be decoded.

    //---------------------------------------------------------------
    // Before verifying the countersignature, 
    // the message must first
    // be decoded.

    //---------------------------------------------------------------
    // Open a message for decoding.
    if(hMsg = CryptMsgOpenToDecode(
        MY_ENCODING_TYPE,
        0,
        0,
        0,
        NULL,
        NULL))
    {
        printf("The message to decode has been opened.\n");
    }
    else
    {
        MyHandleError("CryptMsgOpenToDecode failed.");
    }

    //---------------------------------------------------------------
    // Update the message with the encoded BLOB.
    if(CryptMsgUpdate(
        hMsg,
        pbEncodedBlob,
        cbEncodedBlob,
        TRUE))
    {
        printf("The message to decode has been updated.\n");
    }
    else
    {
        MyHandleError("Updating the countersignature message " \
            "failed.");
    }

    //---------------------------------------------------------------
    // Get a pointer to the CERT_INFO member of 
    // countersigner's  certificate. 

    //---------------------------------------------------------------
    // Retrieve the signer information from the message.
    // Get the size of memory required.
    if(CryptMsgGetParam(
        hMsg,
        CMSG_ENCODED_SIGNER,
        0,
        NULL,
        &cbSignerInfo))
    {
        printf("Signer information is %d bytes.\n", cbSignerInfo);
    }
    else
    {
        MyHandleError("Sizing of cbSignerInfo failed.");
    }

    //---------------------------------------------------------------
    // Allocate memory.
    pbSignerInfo = (BYTE*) malloc(cbSignerInfo);
    if(!pbSignerInfo)
    {
        MyHandleError("cbSignerInfo memory allocation failed.");
    }

    //---------------------------------------------------------------
    // Get the message signer information.
    if(!(CryptMsgGetParam(
        hMsg,
        CMSG_ENCODED_SIGNER,
        0,
        pbSignerInfo,
        &cbSignerInfo)))
    {
        MyHandleError("Getting pbSignerInfo failed.");
    }

    //---------------------------------------------------------------
    // Retrieve the countersigner information from the message.
    // Get the size of memory required.
    if(CryptMsgGetParam(
        hMsg,
        CMSG_SIGNER_UNAUTH_ATTR_PARAM,
        0,
        NULL,
        &cbCountersignerInfo))
    {
        printf("Counter Signer information is %d bytes.\n", 
            cbCountersignerInfo);
    }
    else
    {
        MyHandleError("Sizing of cbCountersignerInfo failed.");
    }

    //---------------------------------------------------------------
    // Allocate memory.
    pCountersignerInfo = 
        (CRYPT_ATTRIBUTES*)malloc(cbCountersignerInfo);
    if(!pCountersignerInfo)
    {
        MyHandleError("pbCountersignInfo memory allocation failed.");
    }

    //---------------------------------------------------------------
    // Get the message counter signer info.
    if(!(CryptMsgGetParam(
        hMsg,
        CMSG_SIGNER_UNAUTH_ATTR_PARAM,
        0,
        pCountersignerInfo,
        &cbCountersignerInfo)))
    {
        MyHandleError("Getting pbCountersignerInfo failed.");
    }

    //---------------------------------------------------------------
    //  Verify the countersignature.
    if(CryptMsgVerifyCountersignatureEncoded(
         0,
         MY_ENCODING_TYPE,
         pbSignerInfo,
         cbSignerInfo,
         pCountersignerInfo->rgAttr->rgValue->pbData,
         pCountersignerInfo->rgAttr->rgValue->cbData,
         pCntrSigCert->pCertInfo))
    {
         printf("Verification of countersignature succeeded.\n");
    }
    else
    {
         printf("Verification of countersignature failed.\n");
         if(GetLastError() == NTE_BAD_SIGNATURE)
         {
               printf("Bad signature.\n");
         }
         else
         {
               printf("Other verification error.\n");
         }
    }

    //---------------------------------------------------------------
    // Clean up.
    free(pbEncodedBlob);
    free(pbDecoded);
    free(pbSignerInfo);
    free(pCountersignerInfo);
    CertCloseStore(hStoreHandle, CERT_CLOSE_STORE_FORCE_FLAG);
    CryptMsgClose(hMsg);
    CryptReleaseContext(hCryptProv,0);

    return 0;
}

//-------------------------------------------------------------------
//  Define function MyHandleError
void MyHandleError(char *s)
{
    fprintf(stderr,"An error occurred in running the program. \n");
    fprintf(stderr,"%s\n",s);
    fprintf(stderr,"Error number %x.\n",GetLastError());
    fprintf(stderr,"Program terminating. \n");
    exit(1);
}
```



 

 



