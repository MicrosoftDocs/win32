---
title: Validating a Package Signature
description: This topic shows how to validate a package digital signature.
ms.assetid: 'd768b5cf-e4ab-43ab-a145-5cc547c7fe04'
---

# Validating a Package Signature

This topic shows how to validate a package digital signature.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Validating a Package Signature](#validating-a-package-signature)
    -   [Steps to Validate a Signature](#steps-to-validate-a-signature)
    -   [Code Details](#code-details)
-   [Disclaimer](#disclaimer)
-   [Related topics](#related-topics)

## Introduction

The following code examples show the `ValidateSignature` function in detail. This function uses the Packaging APIs to validate a digital signature that has been generated for a package (a package signature).

`ValidateSignature` is a helper function that is defined in the [validate.cpp](validate-cpp.md) implementation file of the [Music Bundle Signature Sample](music-bundle-signature-sample.md). For the complete program, which can load, sign, validate, and save a package, see the Music Bundle Signature Sample.

## Validating a Package Signature

For simplicity, the `ValidateSignature` function that is shown in the following sections demonstrates how to validate a single package signature with the certificate, called the signer certificate, that was used to generate the signature, without the use of a certificate chain. This method does not show how to verify a certificate trust status by building a certificate chain.

It may be necessary to take additional steps, such as loading the package, before attempting to validate a package signature, but the content of these steps may depend on the application. To see `ValidateSignature` in the context of the sample program, see the [Music Bundle Signature Sample](music-bundle-signature-sample.md).

The `ValidateSignature` function footprint that is found in [validate.cpp](validate-cpp.md):


```C++
HRESULT
ValidateSignature(
    IOpcDigitalSignatureManager* opcDigSigManager,
    IOpcDigitalSignature* signature,
    BOOL* isValid,
    PCCERT_CONTEXT* signerCert
    )
```



For the code that demonstrates how to retrieve the interface pointers that are needed by the `ValidateSignature` parameters, see the [Music Bundle Signature Sample](music-bundle-signature-sample.md).

### Steps to Validate a Signature

1.  Set the default value of output parameters and declare the other variables that will be used to validate the package signature:

    ```C++
        *isValid = FALSE;
        *signerCert = NULL;
        HRESULT hr = S_OK;
        IOpcCertificateEnumerator * certEnumerator = NULL;
    ```

    

2.  Get an enumerator of the certificates that are related to the package signature:

    ```C++
        hr = signature->GetCertificateEnumerator(&amp;certEnumerator);
    ```

    

    There may be multiple certificates related to a signature, but only one is the signer certificate that is required for package signature validation.

3.  Initialize and define a loop to iterate through the certificates:

    ```C++
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
    ```

    

    Because any one of the certificates in the enumerator could be the signer certificate, this loop will attempt to validate the signature with each certificate. When validation succeeds, the certificate that was used in the current iteration must be the signer certificate.

    1.  Reset the loop variables to capture the validation result, the certificate that was used, and the number of certificates:

        ```C++
                OPC_SIGNATURE_VALIDATION_RESULT result;
                PCCERT_CONTEXT cert = NULL;

                certCount++;
        ```

        

    2.  Attempt to retrieve a certificate from the enumerator, and check the return code for an error:

        ```C++
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
        ```

        

        If the call to [**IOpcCertificateEnumerator::GetCurrent**](iopccertificateenumerator-getcurrent.md) fails, an error code is returned and the method did not allocate memory for the certificate; therefore, memory for the certificate does not need to be freed.

        If the method fails and the error that is returned is recoverable, report the error, reset the `hr` variable to **S\_OK**, and move on to the next certificate. If the method fails and the error that is returned is not recoverable—the package signature could not be validated—exit the loop and then the `ValidateSignature` function. Use the error code returned by [**IOpcCertificateEnumerator::GetCurrent**](iopccertificateenumerator-getcurrent.md) as the return value for `ValidateSignature`.

    3.  If a certificate was retrieved successfully, attempt to validate the package signature by using that certificate:

        ```C++
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
        ```

        

        If the call to [**IOpcDigitalSignatureManager::Validate**](iopcdigitalsignaturemanager-validate.md) succeeds, set the **out** parameter variables and exit the loop.

        If the call to [**IOpcDigitalSignatureManager::Validate**](iopcdigitalsignaturemanager-validate.md) fails and the error is recoverable, report the error, reset the `hr` variable to **S\_OK**, and move on to the next certificate. If the error is not recoverable, do not reset `hr`; this ensures that when the loop conditions are checked, the loop will terminate appropriately.

    4.  Free the memory that was allocated for the certificate if [**IOpcCertificateEnumerator::GetCurrent**](iopccertificateenumerator-getcurrent.md) was called successfully, then close the loop:

        ```C++
                // Free the CERT_CONTEXT that was obtained from the certificate enumerator.
                CertFreeCertificateContext(cert);
            }
        ```

        

        Because the [**IOpcCertificateEnumerator::GetCurrent**](iopccertificateenumerator-getcurrent.md) method guarantees that memory will not be allocated when the method fails, this statement is only executed when **IOpcCertificateEnumerator::GetCurrent** returns successfully. For details, see step 3.a.

4.  If needed, check that the signer certificate is included inside the package:

    ```C++
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
    ```

    

    This check is only necessary if the signing policy of the format requires that the signer certificate be inside of the package. The ECMA-376 OpenXML, 1st Edition, Part 2: Open Packaging Conventions (OPC) does not require the signer certificate to be inside the package; however, the signing policy for this sample does include this requirement.

5.  Release resources:

    ```C++
        if (certEnumerator)
        {
            certEnumerator->Release();
            certEnumerator = NULL;
        }
    ```

    

### Code Details

The following code example shows the `ValidateSignature` function definition in one convenient block, found in [validate.cpp](validate-cpp.md).

The `ValidateSignature` function definition:


```C++
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
```



## Disclaimer

Code examples are not intended to be complete and working programs. The code examples that are referenced on this page, for example, do not perform parameter checking, error checking, or error handling. Use these examples as a starting point, then add the code necessary to create a robust application. For more information about error handling in COM, see the [Error Handling (COM)](_com_Error_Handling) topic.

## Related topics

<dl> <dt>

[Packages How-To Topics](packages-how-to-topics.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

[Packages Overview](packages-overview.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**IOpcCertificateEnumerator**](iopccertificateenumerator.md)
</dt> <dt>

[**IOpcDigitalSignature**](iopcdigitalsignature.md)
</dt> <dt>

[**IOpcDigitalSignatureManager**](iopcdigitalsignaturemanager.md)
</dt> <dt>

[Packaging API Reference](packaging-programming-reference.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> <dt>

[Music Bundle Signature Sample](music-bundle-signature-sample.md)
</dt> <dt>

[validate.cpp](validate-cpp.md)
</dt> </dl>

 

 




