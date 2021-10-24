---
description: You can use the CryptSignMessage function to cosign a message.
ms.assetid: b400436f-a71f-426a-ac8a-7fdcfa6d7575
title: 'Example C Program: Cosigning and Decoding a Message'
ms.topic: article
ms.date: 05/31/2018
---

# Example C Program: Cosigning and Decoding a Message

You can use the [**CryptSignMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignmessage) function to cosign a message. This is accomplished by calling [**CryptSignMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignmessage) once to sign the original message, and then call **CryptSignMessage** again to cosign the signed message.

When you verify the signature of a cosigned message, you use the [**CryptGetMessageSignerCount**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetmessagesignercount) function to get the number of signers of the message and then call the [**CryptVerifyMessageSignature**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifymessagesignature) for each signature. If all of the signatures are verified, then you know the cosigned message is valid.

The following example shows how to sign a message by more than one person (cosign the message), verify all signatures, and decode the message.

<b>Note</b> This function may return a count of duplicate signers and therefore may not be sufficient to avert attacks. We recommend using the sid (SignerIdentifier) field from SignerInfo to identify duplicate signers in a message.  

```C++
//-------------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
#pragma comment(lib, "crypt32.lib")

#include <stdio.h>
#include <conio.h>
#include <tchar.h>
#include <windows.h>
#include <wincrypt.h>

// Link with the Crypt32.lib file.
#pragma comment (lib, "Crypt32")

#define MY_ENCODING_TYPE  (PKCS_7_ASN_ENCODING | X509_ASN_ENCODING)

//-------------------------------------------------------------------
// Define the name of the store where the needed certificate can be 
// found. 

#define CERT_STORE_NAME  L"MY"

//-------------------------------------------------------------------
// Define the name of a certificate subject.
// To use this program, the definitions of SIGNER_NAME and 
// CO_SIGNER_NAME must be changed to the name of the subject of a 
// certificate that has access to a private key. That certificate 
// must have either the CERT_KEY_PROV_INFO_PROP_ID or  
// CERT_KEY_CONTEXT_PROP_ID property set for the context to 
// provide access to the private signature key.

//-------------------------------------------------------------------
// You can use commands similar to the following to create a 
// certificates that can be used with this example:
//
// makecert -n "cn=test_signer" -sk Test -ss my
// makecert -n "cn=test_co_signer" -sk Test -ss my

//#define SIGNER_NAME L"test_signer"
//#define CO_SIGNER_NAME L"test_co_signer"

#define SIGNER_NAME L"Insert_signer_name_here"
#define CO_SIGNER_NAME L"Insert_co_signer_name_here"

#define MAX_NAME 256

//-------------------------------------------------------------------
// Local function prototypes.
void MyHandleError(LPTSTR psz);
bool SignMessage(CRYPT_DATA_BLOB *pEncodedMessageBlob);
bool CosignMessage(CRYPT_DATA_BLOB *pSignedMessageBlob, 
    CRYPT_DATA_BLOB *pCosignedMessageBlob);
bool VerifyCosignedMessage(CRYPT_DATA_BLOB *pEncodedMessageBlob, 
    CRYPT_DATA_BLOB *pDecodedMessageBlob);

int _tmain(int argc, _TCHAR* argv[])
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    CRYPT_DATA_BLOB EncodedMessage;

    if(SignMessage(&EncodedMessage))
    {
        CRYPT_DATA_BLOB DecodedMessage;

        if(VerifyCosignedMessage(&EncodedMessage, &DecodedMessage))
        {
            free(DecodedMessage.pbData);
        }

        free(EncodedMessage.pbData);
    }

    _tprintf(TEXT("Press any key to exit."));
    _getch();

    return 0;
}

//-------------------------------------------------------------------
// MyHandleError
void MyHandleError(LPTSTR psz)
{
    _ftprintf(stderr, TEXT("An error occurred in the program. \n"));
    _ftprintf(stderr, TEXT("%s\n"), psz);
    _ftprintf(stderr, TEXT("Error number %x.\n"), GetLastError());
    _ftprintf(stderr, TEXT("Program terminating. \n"));
} // End of MyHandleError.

//-------------------------------------------------------------------
// SignMessage
bool SignMessage(CRYPT_DATA_BLOB *pEncodedMessageBlob)
{
    bool fReturn = false;
    BYTE* pbMessage;
    DWORD cbMessage;
    HCERTSTORE hCertStore = NULL;   
    PCCERT_CONTEXT pSignerCert = NULL; 
    CRYPT_SIGN_MESSAGE_PARA  SigParams;
    DWORD cbSignedMessageBlob=0;
    BYTE  *pbSignedMessageBlob = NULL;

    // Initialize the output pointer.
    pEncodedMessageBlob->cbData = 0;
    pEncodedMessageBlob->pbData = NULL;

    // The message to be signed.
    // Usually, the message exists somewhere and a pointer is
    // passed to the application.
    pbMessage = 
        (BYTE*)TEXT("CryptoAPI is a good way to handle security");

    // Calculate the size of message. To include the
    // terminating null character, the length is one more byte 
    // than the length returned by the strlen function.
    cbMessage = (lstrlen((TCHAR*) pbMessage) + 1) * sizeof(TCHAR);

    // Create the MessageArray and the MessageSizeArray.
    const BYTE* MessageArray[] = {pbMessage};
    DWORD MessageSizeArray[1];
    MessageSizeArray[0] = cbMessage;

    //  Begin processing. 
    _tprintf(TEXT("The message to be signed is \"%s\".\n"),
        pbMessage);

    // Open the certificate store.
    if(!(hCertStore = CertOpenStore(
       CERT_STORE_PROV_SYSTEM,
       0,
       NULL,
       CERT_SYSTEM_STORE_CURRENT_USER,
       CERT_STORE_NAME)))
    {
         MyHandleError(TEXT("The MY store could not be opened."));
         goto exit_SignMessage;
    }

    // Get a pointer to the signer's certificate.
    // This certificate must have access to the signer's private key.
    if(pSignerCert = CertFindCertificateInStore(
       hCertStore,
       MY_ENCODING_TYPE,
       0,
       CERT_FIND_SUBJECT_STR,
       SIGNER_NAME,
       NULL))
    {
       _tprintf(TEXT("The signer's certificate was found.\n"));
    }
    else
    {
        MyHandleError( TEXT("Signer certificate not found."));
        goto exit_SignMessage;
    }

    // Initialize the signature structure.
    SigParams.cbSize = sizeof(CRYPT_SIGN_MESSAGE_PARA);
    SigParams.dwMsgEncodingType = MY_ENCODING_TYPE;
    SigParams.pSigningCert = pSignerCert;
    SigParams.HashAlgorithm.pszObjId = szOID_RSA_SHA1RSA;
    SigParams.HashAlgorithm.Parameters.cbData = NULL;
    SigParams.cMsgCert = 1;
    SigParams.rgpMsgCert = &pSignerCert;
    SigParams.cAuthAttr = 0;
    SigParams.dwInnerContentType = 0;
    SigParams.cMsgCrl = 0;
    SigParams.cUnauthAttr = 0;
    SigParams.dwFlags = 0;
    SigParams.pvHashAuxInfo = NULL;
    SigParams.rgAuthAttr = NULL;

    // First, get the size of the signed BLOB.
    if(CryptSignMessage(
        &SigParams,
        FALSE,
        1,
        MessageArray,
        MessageSizeArray,
        NULL,
        &cbSignedMessageBlob))
    {
        _tprintf(TEXT("%d bytes needed for the encoded BLOB.\n"),
            cbSignedMessageBlob);
    }
    else
    {
        MyHandleError(TEXT("Getting signed BLOB size failed"));
        goto exit_SignMessage;
    }

    // Allocate memory for the signed BLOB.
    if(!(pbSignedMessageBlob = 
       (BYTE*)malloc(cbSignedMessageBlob)))
    {
        MyHandleError(
            TEXT("Memory allocation error while signing."));
        goto exit_SignMessage;
    }

    // Get the signed message BLOB.
    if(CryptSignMessage(
          &SigParams,
          FALSE,
          1,
          MessageArray,
          MessageSizeArray,
          pbSignedMessageBlob,
          &cbSignedMessageBlob))
    {
        _tprintf(TEXT("The message was signed successfully. \n"));

        // pbSignedMessageBlob now contains the signed BLOB.
        fReturn = true;
    }
    else
    {
        MyHandleError(TEXT("Error getting signed BLOB"));
        goto exit_SignMessage;
    }

exit_SignMessage:

    // Clean up and free memory as needed.
    if(pSignerCert)
    {
        CertFreeCertificateContext(pSignerCert);
        pSignerCert = NULL;
    }
    
    if(hCertStore)
    {
        CertCloseStore(hCertStore, CERT_CLOSE_STORE_CHECK_FLAG);
        hCertStore = NULL;
    }

    if(pbSignedMessageBlob && fReturn)
    {
        fReturn = false;
        CRYPT_DATA_BLOB SignedMessageBlob;
        CRYPT_DATA_BLOB CosignedMessageBlob;

        SignedMessageBlob.cbData = cbSignedMessageBlob;
        SignedMessageBlob.pbData = pbSignedMessageBlob;

        if(CosignMessage(&SignedMessageBlob, &CosignedMessageBlob))
        {
            pEncodedMessageBlob->cbData = CosignedMessageBlob.cbData;
            pEncodedMessageBlob->pbData = CosignedMessageBlob.pbData;

            fReturn = true;
        }
    }
    
    if(pbSignedMessageBlob)
    {
        free(pbSignedMessageBlob);
        pbSignedMessageBlob = NULL;
    }

    return fReturn;
}

//-------------------------------------------------------------------
// CosignMessage
bool CosignMessage(
    CRYPT_DATA_BLOB *pSignedMessageBlob, 
    CRYPT_DATA_BLOB *pCosignedMessageBlob)
{
    bool fReturn = false;
    HCERTSTORE hCertStore = NULL;   
    PCCERT_CONTEXT pCosignerCert = NULL; 
    HCRYPTPROV hCryptProv = NULL;
    HCRYPTMSG hMsg = NULL;
    DWORD cbCosignedMessageBlob=0;
    BYTE  *pbCosignedMessageBlob = NULL;

    // Initialize the output pointer.
    pCosignedMessageBlob->cbData = 0;
    pCosignedMessageBlob->pbData = NULL;

    // Open the certificate store.
    if(!(hCertStore = CertOpenStore(
       CERT_STORE_PROV_SYSTEM,
       0,
       NULL,
       CERT_SYSTEM_STORE_CURRENT_USER,
       CERT_STORE_NAME)))
    {
         MyHandleError(TEXT("The MY store could not be opened."));
         goto exit_CosignMessage;
    }

    // Get a pointer to the cosigner's certificate.
    // This certificate must have access to the cosigner's private 
    // key.
    if((pCosignerCert = CertFindCertificateInStore(
       hCertStore,
       MY_ENCODING_TYPE,
       0,
       CERT_FIND_SUBJECT_STR,
       CO_SIGNER_NAME,
       NULL)))
    {
       _tprintf(TEXT("The signer's certificate was found.\n"));
    }
    else
    {
        MyHandleError( TEXT("Signer certificate not found."));
        goto exit_CosignMessage;
    }

    DWORD dwKeySpec;
    if(!(CryptAcquireCertificatePrivateKey(
        pCosignerCert,
        0,
        NULL,
        &hCryptProv,
        &dwKeySpec,
        NULL)))
    {
        MyHandleError(
            TEXT("CryptAcquireCertificatePrivateKey failed."));
        goto exit_CosignMessage;
    }

    // Open a message for decoding.
    if(!(hMsg = CryptMsgOpenToDecode(
        MY_ENCODING_TYPE,
        0,
        0,
        NULL,
        NULL,
        NULL)))
    {
        MyHandleError(TEXT("CryptMsgOpenToDecode failed."));
        goto exit_CosignMessage;
    }

    // Update the message with the encoded BLOB.
    if(!(CryptMsgUpdate(
        hMsg,
        pSignedMessageBlob->pbData,
        pSignedMessageBlob->cbData,
        TRUE)))
    {
        MyHandleError(TEXT("CryptMsgUpdate failed."));
        goto exit_CosignMessage;
    }

    // Initialize the CMSG_SIGNER_ENCODE_INFO structure for the 
    // cosigner.
    CMSG_SIGNER_ENCODE_INFO CosignerInfo;
    memset(&CosignerInfo, 0, sizeof(CMSG_SIGNER_ENCODE_INFO));
    CosignerInfo.cbSize = sizeof(CMSG_SIGNER_ENCODE_INFO);
    CosignerInfo.pCertInfo = pCosignerCert->pCertInfo;
    CosignerInfo.hCryptProv = hCryptProv;
    CosignerInfo.dwKeySpec = dwKeySpec;
    CosignerInfo.HashAlgorithm.pszObjId = szOID_RSA_SHA1RSA;

    // Add the cosigner to the message.
    if(CryptMsgControl(
        hMsg,
        0,
        CMSG_CTRL_ADD_SIGNER,
        &CosignerInfo))
    {
        _tprintf(TEXT("CMSG_CTRL_ADD_SIGNER succeeded. \n"));
    }
    else
    {
        MyHandleError(TEXT("CMSG_CTRL_ADD_SIGNER failed."));
        goto exit_CosignMessage;
    }

    // Add the cosigner's certificate to the message.
    CERT_BLOB CosignCertBlob;
    CosignCertBlob.cbData = pCosignerCert->cbCertEncoded;
    CosignCertBlob.pbData = pCosignerCert->pbCertEncoded;

    if(CryptMsgControl(
        hMsg,
        0,
        CMSG_CTRL_ADD_CERT,
        &CosignCertBlob))
    {
        _tprintf(TEXT("CMSG_CTRL_ADD_CERT succeeded. \n"));
    }
    else
    {
        MyHandleError(TEXT("CMSG_CTRL_ADD_CERT failed."));
        goto exit_CosignMessage;
    }

    // Get the size of the cosigned BLOB.
    if(CryptMsgGetParam(
        hMsg,
        CMSG_ENCODED_MESSAGE,
        0,
        NULL,
        &cbCosignedMessageBlob))
    {
        _tprintf(TEXT("The size for the encoded BLOB is %d.\n"), 
            cbCosignedMessageBlob);
    }
    else
    {
        MyHandleError(TEXT("Sizing of cbSignerInfo failed."));
        goto exit_CosignMessage;
    }

    // Allocate memory for the cosigned BLOB.
    if(!(pbCosignedMessageBlob = 
       (BYTE*)malloc(cbCosignedMessageBlob)))
    {
        MyHandleError(
            TEXT("Memory allocation error while cosigning."));
        goto exit_CosignMessage;
    }

    // Get the cosigned message BLOB.
    if(CryptMsgGetParam(
        hMsg,
        CMSG_ENCODED_MESSAGE,
        0,
        pbCosignedMessageBlob,
        &cbCosignedMessageBlob))
    {
        _tprintf(TEXT("The message was cosigned successfully. \n"));

        // pbSignedMessageBlob now contains the signed BLOB.
        fReturn = true;
    }
    else
    {
        MyHandleError(TEXT("Sizing of cbSignerInfo failed."));
        goto exit_CosignMessage;
    }

exit_CosignMessage:

    // Clean up and free memory as needed.

    if(hMsg)
    {
        CryptMsgClose(hMsg);
    }

    if(hCryptProv)
    {
        CryptReleaseContext(hCryptProv, 0);
        hCryptProv = NULL;
    }

    if(pCosignerCert)
    {
        CertFreeCertificateContext(pCosignerCert);
        pCosignerCert = NULL;
    }
    
    if(hCertStore)
    {
        CertCloseStore(hCertStore, CERT_CLOSE_STORE_CHECK_FLAG);
        hCertStore = NULL;
    }

    // Only free the cosigned message if a failure occurred.
    if(!fReturn)
    {
        if(pbCosignedMessageBlob)
        {
            free(pbCosignedMessageBlob);
            pbCosignedMessageBlob = NULL;
        }
    }

    if(pbCosignedMessageBlob)
    {
        pCosignedMessageBlob->cbData = cbCosignedMessageBlob;
        pCosignedMessageBlob->pbData = pbCosignedMessageBlob;
    }
    
    return fReturn;
}

//-------------------------------------------------------------------
// VerifyCosignedMessage
bool VerifyCosignedMessage(
    CRYPT_DATA_BLOB *pCosignedMessageBlob, 
    CRYPT_DATA_BLOB *pDecodedMessageBlob)
{
    bool fReturn = false;
    BYTE *pbDecodedMessage = NULL;
    DWORD cbDecodedMessage=0;

    // Get the number of signers of the message.
    LONG lSigners = CryptGetMessageSignerCount(
        MY_ENCODING_TYPE, 
        pCosignedMessageBlob->pbData, 
        pCosignedMessageBlob->cbData);
    if(-1 == lSigners)
    {
        MyHandleError(TEXT("CryptGetMessageSignerCount failed."));
        goto exit_VerifyCosignedMessage;
    }

    // Loop through all of the signers and verify the signature for 
    // each one.
    CRYPT_VERIFY_MESSAGE_PARA VerifyParams;
    VerifyParams.cbSize = sizeof(CRYPT_VERIFY_MESSAGE_PARA);
    VerifyParams.dwMsgAndCertEncodingType = MY_ENCODING_TYPE;
    VerifyParams.hCryptProv = NULL;
    VerifyParams.pfnGetSignerCertificate = NULL;
    VerifyParams.pvGetArg = NULL;

    for(LONG i = 0; i < lSigners; i++)
    {
        if(!(CryptVerifyMessageSignature(
            &VerifyParams,
            i,
            pCosignedMessageBlob->pbData,
            pCosignedMessageBlob->cbData,
            NULL,
            NULL,
            NULL)))
        {
            MyHandleError(TEXT("One of the message signatures ")
                TEXT("could not be verified."));
            goto exit_VerifyCosignedMessage;
        }
    }

    // At this point, all of the signatures in the message have been 
    // verified. Get the decoded data from the message.
    _tprintf(
        TEXT("All signatures in the message have been verified.\n"));

    // Get the size of the decoded message
    if(!(CryptVerifyMessageSignature(
        &VerifyParams,
        0,
        pCosignedMessageBlob->pbData,
        pCosignedMessageBlob->cbData,
        NULL,
        &cbDecodedMessage,
        NULL)))
    {
        MyHandleError(TEXT("CryptVerifyMessageSignature failed."));
        goto exit_VerifyCosignedMessage;
    }

    // Allocate memory for the decoded message.
    if(!(pbDecodedMessage = 
       (BYTE*)malloc(cbDecodedMessage)))
    {
        MyHandleError(
            TEXT("Memory allocation error while decoding."));
        goto exit_VerifyCosignedMessage;
    }

    if((CryptVerifyMessageSignature(
        &VerifyParams,
        0,
        pCosignedMessageBlob->pbData,
        pCosignedMessageBlob->cbData,
        pbDecodedMessage,
        &cbDecodedMessage,
        NULL)))
    {
        fReturn  = true;
    }
    else
    {
        MyHandleError(TEXT("CryptVerifyMessageSignature failed."));
        goto exit_VerifyCosignedMessage;
    }

    _tprintf(TEXT("The verified message is \"%s\".\n"),
        pbDecodedMessage);

exit_VerifyCosignedMessage:

    // If an error occurred and memory was allocated, free it.
    if(!fReturn)
    {
        if(pbDecodedMessage)
        {
            free(pbDecodedMessage);
            pbDecodedMessage = NULL;
        }
    }

    if(pbDecodedMessage)
    {
        pDecodedMessageBlob->cbData = cbDecodedMessage;
        pDecodedMessageBlob->pbData = pbDecodedMessage;
    }

    return fReturn;
}
```



 

 



