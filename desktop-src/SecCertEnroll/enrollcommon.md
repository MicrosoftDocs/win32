---
description: The enrollCommon folder contains the following helper functions and macros used by the samples provided with the Certificate Enrollment SDK.
ms.assetid: a9b3532d-9640-4373-a6c6-7828cb6f55c7
title: enrollCommon
ms.topic: article
ms.date: 05/31/2018
---

# enrollCommon

The enrollCommon folder contains the following helper functions and macros used by the samples provided with the Certificate Enrollment SDK. It is installed by default in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\enrollCommon folder.




| Function | Description | 
|----------|-------------|
| _JumpIfError | Macro that accepts an <strong>HRESULT</strong> value, a label, and an error string, prints the string, and transfers program control to the first statement following the label. | 
| _JumpError | Same as the _JumpIfError macro. | 
| _PrintIfError | Not currently used. | 
| _PrintError | Macro that prints an error message and an <strong>HRESULT</strong> value. | 
| convertWszToSz | Converts a wide-character string to an ASCII character string by using the <strong>WideCharToMultiByte</strong> function and the current ANSI code-page identifier for the system. This function is used by the decConvertFromUnicode and findOIDFromTemplateName functions defined in enrollCommon.cpp. | 
| convertSzToWsz | Converts an ASCII string to a wide-character string by using the <strong>MultiByteToWideChar</strong> function and the current ANSI code-page identifier for the system. This function is used by the findCertByTemplate function defined in enrollCommon.cpp. | 
| convertSzToBstr | Converts an ASCII string to a <strong>BSTR</strong> by using the <strong>MultiByteToWideChar</strong> function. This function is not currently used. | 
| convertWszToBstr | Converts a wide-character string to a <strong>BSTR</strong>. This function is used by the installResponseFromPFX sample. | 
| checkEnrollStatus | Checks the status of the certificate enrollment process by using the <a href="/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment"><strong>IX509Enrollment</strong></a> and <a href="/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollmentstatus"><strong>IX509EnrollmentStatus</strong></a> interfaces. This function is used by the enrollEOBOCMC, enrollPKCS7, enrollRenewalPKCS7, enrollSimpleMachineCert, and enrollSimpleUserCert samples. | 
| findCertByKeyUsage | Enumerates the personal certificate store of the current user to find the first certificate for which the intended use of the public key matches a specified value. The value specified can be a bitwise combination of the following flags:<ul><li>CERT_DATA_ENCIPHERMENT_KEY_USAGE</li><li>CERT_DIGITAL_SIGNATURE_KEY_USAGE</li><li>CERT_KEY_AGREEMENT_KEY_USAGE</li><li>CERT_KEY_CERT_SIGN_KEY_USAGE</li><li>CERT_KEY_ENCIPHERMENT_KEY_USAGE</li><li>CERT_NON_REPUDIATION_KEY_USAGE</li><li>CERT_OFFLINE_CRL_SIGN_KEY_USAGE</li></ul>This function is used by the enrollFromPublicKey sample.<br /> | 
| findCertByEKU | Enumerates the personal certificate store of the current user to find the first certificate for which the Enhanced Key Usage (EKU) extension matches that specified on input. For more information about the EKU extension, see the <a href="/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionenhancedkeyusage"><strong>IX509ExtensionEnhancedKeyUsage</strong></a> interface. This function is used by the enrollEOBOCMC sample. | 
| findCertByTemplate | Enumerates the personal certificate store of the current user to find the first certificate for which the template matches that specified, by name, on input. This function is used by the enrollPKCS7 and enrollRenewalPKCS7 samples. | 
| enrollCertByTemplate | Initializes an <a href="/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment"><strong>IX509Enrollment</strong></a> object by using a template, attempts to enroll the implicitly created certificate request, and monitors the status of the enrollment process. This function is used by the enrollEOBOCMC, enrollFromPublicKey, enrollPKCS7, and enrollRenewalPKCS7 samples. | 
| verifyCertContext | Verifies compliance of the certificate chain against the specified (base) policy and, optionally, against a specified Enhanced Key Usage (EKU) extension. For more information, see the <a href="/windows/desktop/api/wincrypt/nf-wincrypt-certverifycertificatechainpolicy"><strong>CertVerifyCertificateChainPolicy</strong></a> function and the <a href="/windows/desktop/api/wincrypt/ns-wincrypt-cert_chain_policy_para"><strong>CERT_CHAIN_POLICY_PARA</strong></a> and <a href="/windows/desktop/api/wincrypt/ns-wincrypt-cert_chain_para"><strong>CERT_CHAIN_PARA</strong></a> structures. This function is used by the enrollEOBOCMC, enrollFromPublicKey, enrollPKCS7, and enrollRenewalPKCS7 samples. | 
| decConvertFromUnicode | Converts a string of double-byte Unicode characters to a string of single-byte ANSI characters. This function is used by the DecodeFileW function defined in enrollCommon.cpp. | 
| DecodeFileW | Decodes an encoded certificate or certificate request file to a byte array. This function is used by the installResponseFromPFX sample. | 
| EncodeToFileW | Encodes a certificate or certificate request and saves it to a file. This function is used by the createCNGCustomCMC, enrollEOBOCMC, and enrollFromPublicKey samples. | 
| findOIDFromTemplateName | Retrieves the object identifier for a template specified by name. This function is used by the findCertByTemplate function defined in enrollCommon.cpp. | 




 

## Related topics

<dl> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

