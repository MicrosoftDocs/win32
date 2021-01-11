---
description: Reads an existing CMC certificate request from a file, wraps it in another CMC request, signs this outer request, submits it to a certification authority (CA), and saves the certificate response from the CA to a file.
ms.assetid: b1a9161d-1f9a-4c5b-acd2-6058dc65a258
title: enrollNestedCMC
ms.topic: article
ms.date: 05/31/2018
---

# enrollNestedCMC

The enrollNestedCMC sample reads an existing CMC certificate request from a file, wraps it in another CMC request, signs this outer request, submits it to a certification authority (CA), and saves the certificate response from the CA to a file.

## Location

When you install the Microsoft Windows Software Development Kit (SDK), the sample is installed, by default, in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\X509 Certificate Enrollment\\VC\\enrollNestedCMC folder.

## Discussion

The enrollNestedCMC sample:

1.  Processes the following command line arguments:
    -   The name of the input file.
    -   The name of the output file.
    -   An optional request template.
2.  Reads an existing CMC request from a file as a base63-encoded byte array, converts the byte array to a **BSTR**, creates an [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) object, and uses the **BSTR** to initialize the request object. The initialized object becomes the inner request.
3.  Uses the inner request object created and initialized in the preceding step to initialize another CMC request.
4.  Retrieves an existing signing certificate or, if one cannot be found, creates a certificate request from the template specified on the command line and attempts to enroll it. The findCertByTemplate and enrollCertByTemplate functions are defined in enrollCommon.cpp.
5.  Retrieves the [**ISignerCertificates**](/windows/desktop/api/CertEnroll/nn-certenroll-isignercertificates) collection from the outer CMC request, creates a new [**ISignerCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-isignercertificate) object, initializes it by using the retrieved signing certificate, and adds it to the collection.
6.  Encodes the CMC request by using Distinguished Encoding Rules (DER) and retrieves the request as a **BSTR**.
7.  Creates an [**ICertConfig**](/windows/desktop/api/certcli/nn-certcli-icertconfig) object and use it to retrieve a string that contains the CA configuration.
8.  Creates a CryptoAPI [**ICertRequest2**](/windows/desktop/api/certcli/nn-certcli-icertrequest2) object and uses it plus the strings that contain the CA configuration and the certificate request to submit the request to the CA.
9.  Checks the status of the enrollment process and saves the certificate response from the CA to a file. The EncodeToFileW function is defined in enrollCommon.cpp.

## Related topics

<dl> <dt>

[CMC Request](cmc-request.md)
</dt> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

 
