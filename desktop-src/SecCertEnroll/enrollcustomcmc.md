---
Description: 'Creates a CMC certificate request and enrolls a computer in a certificate hierarchy.'
ms.assetid: 'ef09ef04-8925-4d66-97ad-70b4d7cf78b9'
title: enrollCustomCMC
---

# enrollCustomCMC

The enrollCustomCMC sample creates a CMC certificate request and enrolls a computer in a certificate hierarchy.

## Location

When you install the Microsoft Windows Software Development Kit (SDK), the sample is installed, by default, in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\enrollCustomCMC folder.

## Discussion

The enrollCustomCMC sample:

1.  Processes the following command line arguments:
    -   A custom name/value pair to add to the certificate request.
    -   An alternative subject name.
    -   An object identifier (OID) for the Enhanced Key Usage (EKU) extension.
2.  Creates an [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md) request object and initializes it by using the computer context.
3.  Uses the PKCS \#10 request to initialize an [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) object.
4.  Creates an [**IX509ExtensionEnhancedKeyUsage**](ix509extensionenhancedkeyusage.md) object by using the OID specified on the command line and adds it to the extensions collection for the CMC request.
5.  Creates [**IAlternativeName**](ialternativename.md) object by using the name specified on the command line, adds it to the [**IAlternativeNames**](ialternativenames.md) collection, uses the collection to initialize an [**IX509ExtensionAlternativeNames**](ix509extensionalternativenames.md) extension and adds this to the extensions collection for the CMC request.
6.  Creates an [**IX509NameValuePair**](ix509namevaluepair.md) object by using the name and value specified on the command line, and adds it to the [**IX509NameValuePairs**](ix509namevaluepairs.md) collection on the CMC request.
7.  Creates an [**IX509Enrollment**](ix509enrollment.md) object, initializes it by using the CMC request object, and retrieves a string that contains a base64-encoded request.
8.  Creates an [**ICertConfig**](https://msdn.microsoft.com/library/windows/desktop/aa383268) object and use it to retrieve a string that contains the CA configuration.
9.  Creates a CryptoAPI [**ICertRequest2**](https://msdn.microsoft.com/library/windows/desktop/aa385041) object and uses it plus the strings that contain the CA configuration and the certificate request to submit the request to the CA.
10. Checks the submission status and, if successful, installs the certificate to the certificate store.

## Related topics

<dl> <dt>

[CMC Request](cmc-request.md)
</dt> <dt>

[PKCS \#10 Request](pkcs--10-request.md)
</dt> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

 



