---
description: This topic describes how to embed the certificates that make up a certificate chain into an XPS document.
ms.assetid: c6aae8ff-2e1e-43de-9105-171e4187d193
title: Embed Certificate Chains in a Document
ms.topic: article
ms.date: 05/31/2018
---

# Embed Certificate Chains in a Document

This topic describes how to embed the certificates that make up a certificate chain into an XPS document. A certificate chain consists of all the certificates, except the root certificate, that are needed to certify the subject identified by the end certificate.

To embed a certificate chain into an XPS document, first create the certificate chain as illustrated in the following code example.

The **CreateCertificateChain** method in the code example accepts *certificateStore* as a parameter, which is an **HCERTSTORE** value. If this value is **NULL**, the certificates will be retrieved from the client computer's certificate server. If the value is the handle to a certificate store, the certificates will be retrieved from that store referenced by *certificateStore* as well as from the client computer's certificate server.


```C++
HRESULT 
CreateCertificateChain (
    __in PCCERT_CONTEXT            certificate,
    __in HCERTSTORE                certificateStore,
    __out PCCERT_CHAIN_CONTEXT* certificateChain
)
{
    HRESULT  hr = S_OK;

    CERT_CHAIN_PARA certificateChainParameters = {0};

    certificateChainParameters.cbSize = sizeof(CERT_CHAIN_PARA);
    certificateChainParameters.RequestedUsage.dwType = USAGE_MATCH_TYPE_AND;

    // CertGetCertificateChain builds a certificate chain that starts 
    //  from the PCCERT_CONTEXT structure provided by the caller.
    //  After the certificate chain has been successfully created, 
    //  then the authenticity of the certificate can be determined 
    //  by examining the errors, if any, that occurred while the chain
    //  was created.
    BOOL successCreatingCertChain = CertGetCertificateChain (
        NULL,
        certificate,
        NULL,
        certificateStore,
        &certificateChainParameters,
        CERT_CHAIN_REVOCATION_CHECK_CHAIN_EXCLUDE_ROOT,
        NULL,
        certificateChain);

    if (!successCreatingCertChain)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
    }
    return hr;
}
```



The following code example creates a certificate chain from certificates and then adds these certificates to an XPS document. Note that [**CertGetCertificateChain**](/windows/desktop/api/wincrypt/nf-wincrypt-certgetcertificatechain) creates the certificate chain in which the signing certificate is first and the root certificate is last. The signing certificate and the root certificate are not added in this example. The signing certificates will be added with a call to the [**IXpsSignatureManager::Sign**](/windows/desktop/api/xpsdigitalsignature/nf-xpsdigitalsignature-ixpssignaturemanager-sign) method, which should be the last signature method called on the document. The root certificate is not added when the document is signed, because it must be provided by the client computer's certificate server when the signature is validated.


```C++
HRESULT
EmbedCertificateChainInXpsPackage (
    __in IXpsSigningOptions *signingOptions,
    __in PCCERT_CONTEXT signingCertificate
)
{
    HRESULT                 hr                           = S_OK;
    PCCERT_CHAIN_CONTEXT    certificateChainContext      = NULL;
    IOpcCertificateSet      *certificateSetToUpdate      = NULL;
    DWORD                   certificateChainContextIndex = 0;

    // Create the entire certificate chain that originates 
    //  from the certificate that is used to sign the XPS document.
    hr = CreateCertificateChain(
        signingCertificate, 
        NULL, 
        &certificateChainContext);

    if (SUCCEEDED(hr))
    {
        // The signing options of an XPS document contain a pointer to 
        //  an IOpcCertificateSet interface that can be retrieved by 
        //  calling the GetCertificateSet method.
        hr = signingOptions->GetCertificateSet(&certificateSetToUpdate);
    }
    if (SUCCEEDED(hr))
    {
        // for each certificate chain context in this certificate...
        for (certificateChainContextIndex = 0; 
             certificateChainContextIndex < certificateChainContext->cChain; 
             certificateChainContextIndex++)
        {
            // inside a certificate chain context, 
            DWORD adjustedSimpleChainStartIndex = 0;
            DWORD adjustedSimpleChainEndIndex = 0;
            DWORD simpleCertChainIndex = 0;
            CERT_SIMPLE_CHAIN  *simpleCertificateChainWithinContext = NULL;

            // get the information about the certificate chain
            //  set the first item in the certificate chain to load
            //  Ignore the first PCCERT_CONTEXT in the first CERT_SIMPLE_CHAIN
            //  because this is the certificate that was used to build
            //  the chain and is already loaded in the document
            if (certificateChainContextIndex == 0)
            {
                adjustedSimpleChainStartIndex = 1;
            }
            else
            {
                adjustedSimpleChainStartIndex = 0;
            }
                    
            //  get the last item in the certificate chain
            simpleCertificateChainWithinContext = 
                certificateChainContext->rgpChain[certificateChainContextIndex];
            adjustedSimpleChainEndIndex = 
                simpleCertificateChainWithinContext->cElement;

            // Ignore the last PCCERT_CONTEXT in the last CERT_SIMPLE_CHAIN
            //  because this is the root certificate that must be retrieved
            //  from the client computer's certificate server.
            if (certificateChainContextIndex == certificateChainContext->cChain - 1)
            {
                if (adjustedSimpleChainEndIndex != 0)
                {
                    adjustedSimpleChainEndIndex = adjustedSimpleChainEndIndex - 1;
                }
            }

            // for each certificate chain in this context...
            for (simpleCertChainIndex = adjustedSimpleChainStartIndex; 
                 simpleCertChainIndex < adjustedSimpleChainEndIndex;
                 simpleCertChainIndex++)
            {
                // Add the certificate to the XPS document.
                PCCERT_CONTEXT certificateToEmbed = 
                    simpleCertificateChainWithinContext->rgpElement[simpleCertChainIndex]->pCertContext;
                if (FAILED(hr = certificateSetToUpdate->Add(certificateToEmbed)))
                {
                    break; // out of for loop with failed hr
                }
            }
        }
    }
    return hr;
}
```



## Related topics

<dl> <dt>

**Next Steps**
</dt> <dt>

[Load a Certificate from a File](load-a-certificate-from-a-file.md)
</dt> <dt>

[Verify That a Certificate Supports a Signature Method](verify-a-certificate-supports-a-signature-method.md)
</dt> <dt>

[Verify the System Supports a Digest Method](verify-a-certificate-supports-a-digest-method.md)
</dt> <dt>

**Used in This Example**
</dt> <dt>

[**CERT\_CONTEXT**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_context)
</dt> <dt>

[**CertGetCertificateChain**](/windows/desktop/api/wincrypt/nf-wincrypt-certgetcertificatechain)
</dt> <dt>

[**CRYPT\_OID\_INFO**](/windows/desktop/api/wincrypt/ns-wincrypt-crypt_oid_info)
</dt> <dt>

[**IOpcCertificateSet**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopccertificateset)
</dt> <dt>

[**IXpsSigningOptions**](/windows/desktop/api/xpsdigitalsignature/nn-xpsdigitalsignature-ixpssigningoptions)
</dt> <dt>

**For More Information**
</dt> <dt>

[Cryptography API](/windows/desktop/SecCrypto/cryptography-portal)
</dt> <dt>

[Cryptography Functions](/windows/desktop/SecCrypto/cryptography-functions)
</dt> <dt>

[Digital Certificates](/windows/desktop/SecCrypto/digital-certificates)
</dt> <dt>

[Certificate Chains](/windows/desktop/SecCrypto/certificate-chains)
</dt> <dt>

[Certificate Trust Verification](/windows/desktop/SecCrypto/certificate-trust-verification)
</dt> <dt>

[XPS Digital Signature API Errors](xps-digital-signatures-errors.md)
</dt> <dt>

[XPS Document Errors](xps-document-errors.md)
</dt> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> </dl>

 

 
