---
title: validate.cpp
description: validate.cpp
ms.assetid: 'b349ac84-33c5-4e98-a8ed-09bfa015a62e'
keywords: ["Packaging APIs,sample applications", "packaging,sample applications", "packages,sample applications", "Packaging APIs,music bundle signature sample", "packaging,music bundle signature sample", "packages,music bundle signature sample", "music bundle signature sample,validate.cpp", "Packaging APIs,validate.cpp", "packaging,validate.cpp", "packages,validate.cpp", "validate.cpp", "sample applications,music bundle signature"]
---

# validate.cpp


```C++
/*****************************************************************************
*
* File: Validate.cpp
*
* Description: 
* This sample is a simple application that might be used as a starting-point
* for an application that uses the Packaging API. This sample demonstrates
* signature generation and validation using a sample signing policy described
* in Sign.h
*
* ------------------------------------
*
*  This file is part of the Microsoft Windows SDK Code Samples.
* 
*  Copyright (C) Microsoft Corporation.  All rights reserved.
* 
* This source code is intended only as a supplement to Microsoft
* Development Tools and/or on-line documentation.  See these other
* materials for detailed information regarding Microsoft code samples.
* 
* THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
* KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
* PARTICULAR PURPOSE.
* 
****************************************************************************/

#include <stdio.h>
#include <windows.h>
#include <shlobj.h>

#include <msopc.h>  // For OPC APIs

#include <WinCrypt.h>   // For certificate stuff
#include <CryptDlg.h>   // For certificate selection dialog

#include <strsafe.h>
#include <new>

#include "Util.h"
#include "Sign.h"
#include "Validate.h"

// Validates a signature and finds the certificate of the signer.
//
// Parameters:
//      opcDigSigManager - The digital signature manager from which we get the
//                         signature.
//      signature        - The signature to validate.
//      isValid          - When the function returns successfully, isValid
//                         indicates whether the signature is valid.
//      signerCert       - When the function returns successfully and isValid is
//                         true, it holds the certificate of the signer.
HRESULT
ValidateSignature(
    IOpcDigitalSignatureManager* opcDigSigManager,
    IOpcDigitalSignature* signature,
    BOOL* isValid,
    PCCERT_CONTEXT* signerCert
    )
{
    *isValid = FALSE;
    *signerCert = NULL;
    HRESULT hr = S_OK;
    IOpcCertificateEnumerator * certEnumerator = NULL;

    // Get an enumerator of certificates related to the signature.
    hr = signature->GetCertificateEnumerator(&amp;certEnumerator);

    // There may be multiple certificates related to a signature, but only one
    // is the certificate that was used to generate the signature (the signer
    // certificate). Package signature validation requires this signer
    // certificate; therefore, we will enumerate the certificates related to
    // the signature and try to validate the signature with each certificate.
    // When validation succeeds, the certificate that was used must be the
    // signer certificate. 
    //
    // In production code, when there are multiple certificates related to a
    // signature, the application should build a certificate chain starting
    // from the signer certificate, going through the other certificates, and
    // leading to a trusted, root certificate (see CertGetCertificateChain for
    // more details). This root certificate should be availible on the client
    // system or obtainable from a certificate store. If a chain from the
    // signer certificate to a trusted, root certificate cannot be built, then
    // the signer certificate cannot be trusted.
    //
    // To build a certificate chain, the application calls the
    // CertGetCertificateChain function. If the client system does not have all
    // the needed certificates they must be obtained from a certificate store
    // or building the chain will fail.
    //
    // The certificates in the certificate enumerator of a signature can be
    // used to facilitate chain bulding by being included in a certificate
    // store that is then passed to the CertGetCertificateChain function as
    // an additional store. The application can create a memory certificate
    // store that contains all of the certificates in the enumerator by calling
    // the CertOpenStore function.
    //
    // For simplicity, this sample does not perform validation with a certificate
    // chain and does not provide an example of certificate chain building.
    UINT32 certCount = 0;
    BOOL hasNext = TRUE;
    while (
        SUCCEEDED(hr)
        &amp;&amp;
        SUCCEEDED(hr = certEnumerator->MoveNext(&amp;hasNext))
        &amp;&amp;
        hasNext
        )
    {
        OPC_SIGNATURE_VALIDATION_RESULT result;
        PCCERT_CONTEXT cert = NULL;

        certCount++;

        // The contract of GetCurrent ensures that if the method fails,
        // it will not return a valid CERT_CONTEXT. If it succeeds,
        // CertFreeCertificateContext is called to free the CERT_CONTEXT;
        // unless it is being returned to the caller in signerCert.
        hr = certEnumerator->GetCurrent(&amp;cert);

        if (FAILED(hr))
        {
            // Filter with known possible errors, so that we can still continue
            // safely.
            UINT32 facilityCode = HRESULT_FACILITY(hr);

            if (facilityCode == FACILITY_SECURITY || facilityCode == FACILITY_OPC)
            {
                // The error may be due to a corrupted certificate, a bad
                // certificate relationship, or a missing certificate part.
                // Warn the end user and continue to search for the next
                // available certificate.
                fwprintf(
                    stdout, 
                    L"Warning: Found corrupted certificate in the package. "
                    L"IOpcCertificateEnumerator::GetCurrent() returns hr=0x%x\n",
                    hr
                    );

                hr = S_OK;  // Reset hr to continue with the loop.
                continue;
            }
            else
            {
                // Do not continue for unanticipated or critical errors, such
                // as E_OUTOFMEMORY.
                break;
            }
        }

        // Verify that the signature is valid, meaning that no signed content 
        // has been modified.
        hr = opcDigSigManager->Validate(signature, cert, &amp;result);

        if (SUCCEEDED(hr))
        {
            if (result == OPC_SIGNATURE_VALID)
            {
                // Found the signer certificate and confirmed that the
                // signature is valid.
                *isValid = TRUE;
                *signerCert = cert;
                break;
            }
        }
        else
        {
            // The HRESULT from IOpcDigitalSignatureManager::Validate()
            // describes why validation failed. 
            UINT32 facilityCode = HRESULT_FACILITY(hr);

            if (facilityCode == FACILITY_SECURITY)
            {
                // The error may have been caused by attempting to validate
                // the signature with a certificate that is not the signer
                // certificate. Try the next available certificate.
                fwprintf(
                    stdout, 
                    L"Warning: Tried to validate signature with certificate %u and it failed with hr=0x%x. \n",
                    certCount,
                    hr
                    );

                hr = S_OK;  // Reset hr to continue with the loop.
            }
            // Do not continue for unanticipated or critical errors, such
            // as E_OUTOFMEMORY.
        }
        // Free the CERT_CONTEXT that was obtained from the certificate enumerator.
        CertFreeCertificateContext(cert);
    }

    if (SUCCEEDED(hr) &amp;&amp; certCount == 0)
    {
        // OPC spec does not require that the signer certificate for a
        // signature be stored in the package. For simplicity, this sample does
        // require that that signer certificate for the signature be stored in
        // the package.
        //
        // If the signer certificate is not stored in the package, the
        // application that validates the signature should choose the
        // appropriate certificate, as illustrated in the following example.
        //      Person A signs a package but does not store the signer certificate
        //      in the package. Person B gets the package and is told that the 
        //      package was signed by person A. Person B's system must have a
        //      copy of the signer certificate used by person A (with public key
        //      only); therefore, person B can explicitly use that certificate
        //      to verify that the package was really signed by person A.
        fwprintf(
            stderr, 
            L"There is no certificate associated with the signature. Cannot validate the signature.\n"
            );
    }

    // Release resources
    if (certEnumerator)
    {
        certEnumerator->Release();
        certEnumerator = NULL;
    }

    return hr;
}

HRESULT
PrintRelationshipReferenceInfo(
    IOpcSignatureRelationshipReference* relsReference
    )
{
    IOpcUri * sourceUri = NULL;
    BSTR uriString = NULL;

    OPC_RELATIONSHIPS_SIGNING_OPTION relsSigningOption = OPC_RELATIONSHIP_SIGN_USING_SELECTORS;

    HRESULT hr = relsReference->GetSourceUri(&amp;sourceUri);

    if (SUCCEEDED(hr))
    {
        hr = sourceUri->GetDisplayUri(&amp;uriString);
    }

    if (SUCCEEDED(hr))
    {
        fwprintf(stdout, L"Source Uri: %s\n", uriString);
    }

    if (SUCCEEDED(hr))
    {
        hr = relsReference->GetRelationshipSigningOption(&amp;relsSigningOption);
    }

    if (SUCCEEDED(hr))
    {
        if (relsSigningOption == OPC_RELATIONSHIP_SIGN_PART)
        {
            // Note: In this sample no relationships part is signed as a whole,
            // so this statement should not be executed.
            fwprintf(stdout, L"The whole relationships part is signed.\n");
        }
        else // relsSigningOption == OPC_RELATIONSHIP_SIGN_USING_SELECTORS
        {
            IOpcRelationshipSelectorEnumerator * selectorEnumerator = NULL;
            BOOL hasNext = FALSE;

            hr = relsReference->GetRelationshipSelectorEnumerator(&amp;selectorEnumerator);

            while(
                SUCCEEDED(hr)
                &amp;&amp;
                SUCCEEDED(hr = selectorEnumerator->MoveNext(&amp;hasNext))
                &amp;&amp;
                hasNext
                )
            {
                IOpcRelationshipSelector * selector = NULL;
                LPCWSTR token = NULL;
                LPWSTR criterion = NULL;

                hr = selectorEnumerator->GetCurrent(&amp;selector);

                OPC_RELATIONSHIP_SELECTOR selectorType = OPC_RELATIONSHIP_SELECT_BY_ID;
                if (SUCCEEDED(hr))
                {
                    hr = selector->GetSelectorType(&amp;selectorType);
                }

                switch (selectorType)
                {
                case OPC_RELATIONSHIP_SELECT_BY_ID:
                    token = L"Id";
                    fwprintf(stdout, L"Select by relationship Id.\n");
                    break;

                case OPC_RELATIONSHIP_SELECT_BY_TYPE:
                    token = L"Type";
                    fwprintf(stdout, L"Select by relationship Type.\n");
                    break;

                default:
                    fwprintf(stderr, L"Invalid OPC_RELATIONSHIP_SELECTOR value.\n");
                    hr = E_UNEXPECTED;
                }

                if (SUCCEEDED(hr))
                {
                    hr = selector->GetSelectionCriterion(&amp;criterion);
                }

                if (SUCCEEDED(hr))
                {
                    fwprintf(stdout, L"%s = %s\n", token, criterion);
                }

                if (selector)
                {
                    selector->Release();
                    selector = NULL;
                }

                CoTaskMemFree(static_cast<LPVOID>(criterion));
            }

            if (selectorEnumerator)
            {
                selectorEnumerator->Release();
                selectorEnumerator = NULL;
            }
        }
    }

    // Release resources
    if (sourceUri)
    {
        sourceUri->Release();
        sourceUri = NULL;
    }

    SysFreeString(uriString);

    return hr;
}

HRESULT
PrintSigningInfo(
    IOpcDigitalSignature* signature
    )
{
    IOpcSignaturePartReferenceEnumerator * signedPartsEnumerator = NULL;
    IOpcSignatureRelationshipReferenceEnumerator * signedRelationshipsEnumerator = NULL;
    BOOL hasNext = FALSE;

    HRESULT hr = signature->GetSignaturePartReferenceEnumerator(&amp;signedPartsEnumerator);

    if (SUCCEEDED(hr))
    {
        fwprintf(stdout, L"\nThe signature signed the following parts:\n");
    }

    while(
        SUCCEEDED(hr)
        &amp;&amp;
        SUCCEEDED(hr = signedPartsEnumerator->MoveNext(&amp;hasNext))
        &amp;&amp;
        hasNext
        )
    {
        IOpcSignaturePartReference * partReference = NULL;
        IOpcPartUri * partName = NULL;
        BSTR nameString = NULL;

        hr = signedPartsEnumerator->GetCurrent(&amp;partReference);

        if (SUCCEEDED(hr))
        {
            hr = partReference->GetPartName(&amp;partName);
        }

        if (SUCCEEDED(hr))
        {
            hr = partName->GetDisplayUri(&amp;nameString);
        }

        if (SUCCEEDED(hr))
        {
            fwprintf(stdout, nameString);
            fwprintf(stdout, L"\n");
        }

        // Release resources
        if (partReference)
        {
            partReference->Release();
            partReference = NULL;
        }

        if (partName)
        {
            partName->Release();
            partName = NULL;
        }

        SysFreeString(nameString);
    }

    if (SUCCEEDED(hr))
    {
        hr = signature->GetSignatureRelationshipReferenceEnumerator(&amp;signedRelationshipsEnumerator);

        fwprintf(stdout, L"\nThe signature signed the following relationships:\n");
    }

    while(
        SUCCEEDED(hr)
        &amp;&amp;
        SUCCEEDED(hr = signedRelationshipsEnumerator->MoveNext(&amp;hasNext))
        &amp;&amp;
        hasNext
        )
    {
        IOpcSignatureRelationshipReference * relsReference = NULL;

        hr = signedRelationshipsEnumerator->GetCurrent(&amp;relsReference);

        if (SUCCEEDED(hr))
        {
            hr = PrintRelationshipReferenceInfo(relsReference);
        }

        fwprintf(stdout, L"\n");

        // Release resources
        if (relsReference)
        {
            relsReference->Release();
            relsReference = NULL;
        }
    }

    // Release resources
    if (signedPartsEnumerator)
    {
        signedPartsEnumerator->Release();
        signedPartsEnumerator = NULL;
    }

    if (signedRelationshipsEnumerator)
    {
        signedRelationshipsEnumerator->Release();
        signedRelationshipsEnumerator = NULL;
    }

    return hr;
}

// Performs music bundle signature validation task.
HRESULT
ValidateMusicBundleSignature(
    IOpcFactory* opcFactory
    )
{
    IOpcPackage * opcPackage = NULL;
    IOpcDigitalSignatureManager * opcDigSigManager = NULL;
    IOpcDigitalSignatureEnumerator * signatureEnumerator = NULL;
    BOOL hasNext = FALSE;
    UINT32 count = 0;

    // Load the signed music bundle package.
    HRESULT hr = ReadPackageFromFile(g_signedFilePath, opcFactory, &amp;opcPackage);

    if (SUCCEEDED(hr))
    {
        // Create a digital signature manager for the package.
        hr = opcFactory->CreateDigitalSignatureManager(opcPackage, &amp;opcDigSigManager);
    }

    if (SUCCEEDED(hr))
    {
        // Get an enumerator of all the signatures applied to the package.
        hr = opcDigSigManager->GetSignatureEnumerator(&amp;signatureEnumerator);
    }

    // Report all signatures (if there are multiples) in the music bundle and
    // validate all of them. For simplicity, this sample only generates one
    // signature, however, the validation functions are written more
    // generically to handle packages that have multiple signatures. 
    while (
        SUCCEEDED(hr)
        &amp;&amp;
        SUCCEEDED(hr = signatureEnumerator->MoveNext(&amp;hasNext))
        &amp;&amp;
        hasNext
        )
    {
        count++;

        IOpcDigitalSignature * signature = NULL;
        BOOL isValid = FALSE;
        PCCERT_CONTEXT signerCert = NULL;

        hr = signatureEnumerator->GetCurrent(&amp;signature);

        if (SUCCEEDED(hr))
        {
            fwprintf(stdout, L"Found Signature %u:\n", count);

            hr = ValidateSignature(opcDigSigManager, signature, &amp;isValid, &amp;signerCert);

            if (SUCCEEDED(hr))
            {
                if (isValid)
                {
                    WCHAR certFileName[MAX_PATH];

                    fwprintf(stdout, L"Signature %u is valid.\n", count);
    
                    // In production code, the application should check that
                    // the signature is compliant with the signing policy. For
                    // example, checking all the required parts and
                    // relationships are signed properly. For details regarding
                    // the music bundle signing policy, see the sample signing
                    // policy in Sign.h).
                    //
                    // For simplicity, this sample prints signing information
                    // for the user to review and verify.
                    PrintSigningInfo(signature);

                    hr = StringCchPrintf(certFileName, MAX_PATH, L"Signer%u.cer", count);
    
                    if (SUCCEEDED(hr))
                    {
                        hr = SaveCertificateToFile(signerCert, certFileName);

                        if (SUCCEEDED(hr))
                        {
                            // In production code, the application may build a
                            // certificate chain (leading to a trusted, root
                            // certificate) to verify the signer certificate
                            // (for details, see CertGetCertificateChain).
                            //
                            // For simplicity, this sample stores the signer
                            // certificate as a file, thus allowing the user
                            // to double-click the file and open it in the
                            // certificate UI to verify the certificate.
                            fwprintf(
                                stdout, 
                                L"The signer of signature %u is identified by the certificate stored in %s. "
                                L"Please inspect the certificate to see whether you trust the signer "
                                L"(you can double click the certificate file to open it).\n", 
                                count,
                                certFileName
                                );
                        }
                        else
                        {
                            fwprintf(
                                stderr,
                                L"Failed to save the certificate to file. \n"
                                );
                        }
                    }
    
                    CertFreeCertificateContext(signerCert);
                }
                else
                {
                    fwprintf(stdout, L"Signature %u is invalid.\n", count);
                }
            }
        }
        else
        {
            // The HRESULT from ValidateSignature() describes why signature
            // validation failed.
            UINT32 facilityCode = HRESULT_FACILITY(hr);

            // Check for errors that are recoverable, and attempt to validate
            // the next signature, if there is one.
            if (facilityCode == FACILITY_OPC
                ||
                facilityCode == FACILITY_SECURITY
                ||
                facilityCode == FACILITY_WEBSERVICES)
            {
                // These errors indicate that the signature has problems, such
                // as a missing signature part is, corrupted or mal-formed
                // signature markup, and so on. By looking up the error code,
                // the end user may be able to determine why validation of the
                // signature failed.
                fwprintf(
                    stdout, 
                    L"Warning: Found Signature %u but it is corrupted. "
                    L"IOpcDigitalSignatureEnumerator::GetCurrent() returns hr=0x%x\n", 
                    count,
                    hr
                    );

                hr = S_OK;  // Reset hr to continue with the loop.
            }
        }

        if (signature)
        {
            signature->Release();
            signature = NULL;
        }
    }

    if (SUCCEEDED(hr) &amp;&amp; count == 0)
    {
        fwprintf(stderr, L"Music bundle [%s] has no signature.\n", g_signedFilePath);
        hr = E_UNEXPECTED;
    }

    // Release resources
    if (opcPackage)
    {
        opcPackage->Release();
        opcPackage = NULL;
    }

    if (opcDigSigManager)
    {
        opcDigSigManager->Release();
        opcDigSigManager = NULL;
    }

    if (signatureEnumerator)
    {
        signatureEnumerator->Release();
        signatureEnumerator = NULL;
    }

    return hr;
}
```



## Related topics

<dl> <dt>

[Music Bundle Signature Sample](music-bundle-signature-sample.md)
</dt> </dl>

 

 




