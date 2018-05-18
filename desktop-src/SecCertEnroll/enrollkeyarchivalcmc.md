---
Description: 'Creates a CMC certificate request to archive a private key on a certification authority (CA).'
ms.assetid: 'b063989a-fe92-4c2c-9d66-8a14bc830f6b'
title: enrollKeyArchivalCMC
---

# enrollKeyArchivalCMC

The enrollKeyArchivalCMC sample creates a CMC certificate request to archive a private key on a certification authority (CA). For more information, see [CMC Key Archival Request](cmc-key-archival-request.md).

## Location

When you install the Microsoft Windows Software Development Kit (SDK), the sample is installed, by default, in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\enrollKeyArchivalCMC folder.

## Discussion

The enrollKeyArchivalCMC sample:

1.  Processes the command line arguments. The command line should contain the name of the certificate template to use for enrollment.
2.  Creates an [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) certificate request object and initializes it for an end-user context by using the template name.
3.  Sets the [**ArchivePrivateKey**](ix509certificaterequestcmc-archiveprivatekey-property.md) property on the CMC request.
4.  Creates an [**ICertConfig**](https://msdn.microsoft.com/library/windows/desktop/aa383268) object and uses it to retrieve a string that contains the CA configuration.
5.  Creates a CryptoAPI [**ICertRequest2**](https://msdn.microsoft.com/library/windows/desktop/aa385041) object and uses it to retrieve the exchange certificate for the CA.
6.  Creates an [**IX509Enrollment**](ix509enrollment.md) object, initializes it by using the CMC request, creates a base64 encoded string that contains the key archival request, and submits it to the CA.

## Related topics

<dl> <dt>

[CMC Key Archival Request](cmc-key-archival-request.md)
</dt> <dt>

[CMC Request](cmc-request.md)
</dt> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

 



