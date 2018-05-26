---
Description: Implements the IX509Enrollment interface.
ms.assetid: bcf5c2f0-b99f-4de5-83f4-44f17dc31cd4
title: Certificate Response Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Certificate Response Functions

CertEnroll.dll implements the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) interface to submit a client certificate request and install the response from a [*certification authority*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certification-authority-gly) (CA).

The enrollment process can accommodate the following three scenarios:

<dl> Out-of-band enrollment

1.  Call any initialization method implemented by the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object.
2.  Call the [**CreateRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-createrequest?branch=master) method to retrieve the request.
3.  Submit the request out of band (manually or by using some other process).
4.  Receive the response from a CA.
5.  Call the [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) method.

  
Automatic enrollment

1.  Call any initialization method implemented by the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object.
2.  Call the [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) method.

  
Delayed enrollment

1.  Call any initialization method implemented by the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object.
2.  Call the [**CreateRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-createrequest?branch=master) method to retrieve the request.
3.  Store the request until you are ready to submit it.
4.  When you are ready to enroll, call the [**Initialize**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-initialize?branch=master) method to reinitialize the enrollment object.
5.  Call the [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) method when the CA returns a certificate.

  
</dl>

During the enrollment process, you can call the [**Status**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_status?branch=master) property on the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object to retrieve an [**EnrollmentEnrollStatus**](/windows/win32/CertEnroll/ne-certenroll-enrollmentenrollstatus?branch=master) enumeration value that identifies whether enrollment succeeded, is pending, was skipped, generated an error, or was denied.

Each of the following sections identifies a function exported by Xenroll.dll to install a certificate response from a CA. Each section also discusses how to use CertEnroll.dll to replace the function or indicates that no mapping between the two libraries exists:

-   [acceptFilePKCS7WStr](#acceptfilepkcs7wstr)
-   [acceptFileResponseWStr](#acceptfileresponsewstr)
-   [acceptPKCS7Blob](#acceptpkcs7blob)
-   [acceptResponseBlob](#acceptresponseblob)
-   [getCertContextFromFileResponseWStr](#getcertcontextfromfileresponsewstr)
-   [getCertContextFromPKCS7](#getcertcontextfrompkcs7)
-   [getCertContextFromResponseBlob](#getcertcontextfromresponseblob)
-   [InstallPKCS7Blob](#installpkcs7blobex)
-   [InstallPKCS7BlobEx](#installpkcs7blobex)
-   [SPCFileNameWStr](#spcfilenamewstr)
-   [WriteCertToCSP](#writecerttocsp)
-   [WriteCertToUserDS](#writecerttouserds)
-   [Related topics](#related-topics)

## acceptFilePKCS7WStr

The [**acceptFilePKCS7WStr**](https://msdn.microsoft.com/library/windows/desktop/aa385498) function in Xenroll.dll installs a [*PKCS \#7*](https://msdn.microsoft.com/library/windows/desktop/ms721603) response from a file.

The CertEnroll.dll library does not directly implement functionality to install a PKCS \#7 certificate response from a file. You can, however, create a custom function to read the file data into a byte array and call [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) to install the response.

If you specify the **AllowNoOutstandingRequest** value of the [**InstallResponseRestrictionFlags**](/windows/win32/CertEnroll/ne-certenroll-installresponserestrictionflags?branch=master) enumeration for the first parameter of [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master), a dummy certificate need not exist, thereby enabling you to install a certificate without first calling [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) or [**CreateRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-createrequest?branch=master). However, if you are installing a certificate by using a web script, a dummy certificate must exist in the request store. You must therefore specify **AllowNone** for the first parameter.

## acceptFileResponseWStr

The [**acceptFileResponseWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385500) function in Xenroll.dll installs a PKCS \#7 or CMC certificate response from a file.

The CertEnroll.dll library does not directly implement functionality to install a certificate response from a file. You can, however, create a custom function to read the file data into a byte array and call [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) to install the PKCS \#7 or CMC response.

If you specify the **AllowNoOutstandingRequest** value of the [**InstallResponseRestrictionFlags**](/windows/win32/CertEnroll/ne-certenroll-installresponserestrictionflags?branch=master) enumeration for the first parameter of [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master), a dummy certificate need not exist, thereby enabling you to install a certificate without first calling [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) or [**CreateRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-createrequest?branch=master). However, if you are installing a certificate by using a web script, a dummy certificate must exist in the request store. You must therefore specify **AllowNone** for the first parameter.

## acceptPKCS7Blob

The [**acceptPKCS7Blob**](https://msdn.microsoft.com/library/windows/desktop/aa385503) function in Xenroll.dll installs a PKCS \#7 response contained in a byte array.

You can call [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) to install a PKCS \#7 message. If you specify the **AllowNoOutstandingRequest** value of the [**InstallResponseRestrictionFlags**](/windows/win32/CertEnroll/ne-certenroll-installresponserestrictionflags?branch=master) enumeration for the first parameter of [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master), a dummy certificate need not exist, thereby enabling you to install the PKCS \#7 response without first calling [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) or [**CreateRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-createrequest?branch=master). However, if you are installing a certificate by using a web script, a dummy certificate must exist in the request store. You must therefore specify **AllowNone** for the first parameter.

## acceptResponseBlob

The [**acceptResponseBlob**](https://msdn.microsoft.com/library/windows/desktop/aa385505) function in Xenroll.dll installs a PKCS \#7 or CMC certificate response contained in a byte array.

You can call [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) to install a PKCS \#7 or CMC response. If you specify the **AllowNoOutstandingRequest** value of the [**InstallResponseRestrictionFlags**](/windows/win32/CertEnroll/ne-certenroll-installresponserestrictionflags?branch=master) enumeration for the first parameter of [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master), a dummy certificate need not exist, thereby enabling you to install the response without first calling [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) or [**CreateRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-createrequest?branch=master). However, if you are installing a certificate by using a web script, a dummy certificate must exist in the request store. You must therefore specify **AllowNone** for the first parameter.

## getCertContextFromFileResponseWStr

The [**getCertContextFromFileResponseWStr**](https://msdn.microsoft.com/library/windows/desktop/aa385583) function in Xenroll.dll retrieves the client certificate from a file.

The CertEnroll.dll library does not directly implement functionality to retrieve a certificate from a CA response saved in a file. You can, however, create a custom function to read the file data into a byte array and call [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) to install the PKCS \#7 or CMC response, and call the [**Certificate**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_certificate?branch=master) property to retrieve the certificate.

If you specify the **AllowNoOutstandingRequest** value of the [**InstallResponseRestrictionFlags**](/windows/win32/CertEnroll/ne-certenroll-installresponserestrictionflags?branch=master) enumeration for the first parameter of [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master), a dummy certificate need not exist, thereby enabling you to install a certificate without first calling [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) or [**CreateRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-createrequest?branch=master). However, if you are installing a certificate by using a web script, a dummy certificate must exist in the request store. You must therefore specify **AllowNone** for the first parameter.

## getCertContextFromPKCS7

The [**getCertContextFromPKCS7**](https://msdn.microsoft.com/library/windows/desktop/aa385586) function in Xenroll.dll retrieves the client certificate from a PKCS \#7 response.

You can call the [**Certificate**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_certificate?branch=master) property on the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object to retrieve a certificate after calling the [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) or [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) method.

## getCertContextFromResponseBlob

The [**getCertContextFromResponseBlob**](https://msdn.microsoft.com/library/windows/desktop/aa385589) function in Xenroll.dll retrieves a client certificate from a PKCS \#7 or CMC response.

You can call the [**Certificate**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-get_certificate?branch=master) property on the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) object to retrieve a certificate after calling the [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) or [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) method.

## InstallPKCS7Blob

The [**InstallPKCS7Blob**](https://msdn.microsoft.com/library/windows/desktop/aa385631) function in Xenroll.dll installs a PKCS \#7 response.

You can call [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) to install a PKCS \#7 or CMC response. If you specify the **AllowNoOutstandingRequest** value of the [**InstallResponseRestrictionFlags**](/windows/win32/CertEnroll/ne-certenroll-installresponserestrictionflags?branch=master) enumeration for the first parameter of [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master), a dummy certificate need not exist, thereby enabling you to install the response without first calling [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) or [**CreateRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-createrequest?branch=master). However, if you are installing a certificate by using a web script, a dummy certificate must exist in the request store. You must therefore specify **AllowNone** for the first parameter.

## InstallPKCS7BlobEx

The [**InstallPKCS7BlobEx**](https://msdn.microsoft.com/library/windows/desktop/aa385635) function in Xenroll.dll installs a PKCS \#7 response and returns the number of certificates installed.

You can call [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) to install a PKCS \#7 or CMC response. If you specify the **AllowNoOutstandingRequest** value of the [**InstallResponseRestrictionFlags**](/windows/win32/CertEnroll/ne-certenroll-installresponserestrictionflags?branch=master) enumeration for the first parameter of [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master), a dummy certificate need not exist, thereby enabling you to install the response without first calling [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) or [**CreateRequest**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-createrequest?branch=master). However, if you are installing a certificate by using a web script, a dummy certificate must exist in the request store. You must therefore specify **AllowNone** for the first parameter.

## SPCFileNameWStr

The [**SPCFileNameWStr**](https://msdn.microsoft.com/library/windows/desktop/aa386143) function in Xenroll.dll specifies or retrieves the name of the file in which to save the certificate response. The CertEnroll.dll library does not implement functionality that enables you to copy a certificate to a specific file. The enrollment process automatically installs the certificate chain into files in the appropriate stores.

## WriteCertToCSP

The [**WriteCertToCSP**](https://msdn.microsoft.com/library/windows/desktop/aa386153) function in Xenroll.dll specifies or retrieves a Boolean value that indicates whether a certificate should be written to a [*cryptographic service provider*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-cryptographic-service-provider-gly) (CSP). Typically, if this function is called, the provider is a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

In CertEnroll.dll, when a client calls the [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) method to submit a request for a smart card certificate and a certificate is issued, [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) automatically installs the certificate on the smart card, assuming that the card is installed in the reader. The [**InstallResponse**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-installresponse?branch=master) method also automatically writes the certificate to the smart card.

## WriteCertToUserDS

The [**WriteCertToUserDS**](https://msdn.microsoft.com/library/windows/desktop/aa386154) function in Xenroll.dll specifies or retrieves a Boolean value that indicates whether a certificate should be saved in the Active Directory store. The CertEnroll.dll library does not implement functionality that enables you to specify a store to copy a certificate to.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master)
</dt> </dl>

 

 



