---
Description: Lists the functions provided by CryptoAPI.
ms.assetid: 9a65f73d-6f8c-4271-a2d0-d91ad952f9c6
title: Cryptography Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cryptography Functions

Cryptography functions are categorized according to usage as follows:

-   [CryptXML Functions](#cryptxml-functions)
-   [Signer Functions](#signer-functions)
-   [Base Cryptography Functions](#base-cryptography-functions)
    -   [Service Provider Functions](#service-provider-functions)
    -   [Key Generation and Exchange Functions](#key-generation-and-exchange-functions)
    -   [Object Encoding and Decoding Functions](#object-encoding-and-decoding-functions)
    -   [Data Encryption and Decryption Functions](#data-encryption-and-decryption-functions)
    -   [Hash and Digital Signature Functions](#hash-and-digital-signature-functions)
-   [Certificate and Certificate Store Functions](#certificate-and-certificate-store-functions)
    -   [Certificate Store Functions](#certificate-and-certificate-store-functions)
    -   [Certificate and Certificate Store Maintenance Functions](#certificate-and-certificate-store-maintenance-functions)
    -   [Certificate Functions](#certificate-functions)
    -   [Certificate Revocation List Functions](#certificate-revocation-list-functions)
    -   [Certificate Trust List Functions](#certificate-trust-list-functions)
    -   [Extended Property Functions](#extended-property-functions)
-   [MakeCert Functions](#makecert-functions)
-   [Certificate Verification Functions](#certificate-verification-functions)
    -   [Verification Functions Using CTLs](#verification-functions-using-ctls)
    -   [Certificate Chain Verification Functions](#certificate-chain-verification-functions)
-   [Message Functions](#message-functions)
    -   [Low-level Message Functions](#low-level-message-functions)
    -   [Simplified Message Functions](#simplified-message-functions)
-   [Auxiliary Functions](#auxiliary-functions)
    -   [Data Management Functions](#data-management-functions)
    -   [Data Conversion Functions](#data-conversion-functions)
    -   [Enhanced Key Usage Functions](#enhanced-key-usage-functions)
    -   [Key Identifier Functions](#key-identifier-functions)
    -   [OID Support Functions](#oid-support-functions)
    -   [Remote Object Retrieval Functions](#remote-object-retrieval-functions)
    -   [PFX Functions](#pfx-functions)
-   [Certificate Services Backup and Restore Functions](#certificate-services-backup-and-restore-functions)
-   [Callback Functions](#callback-functions)
-   [Catalog Definition Functions](#catalog-definition-functions)
-   [Catalog Functions](#catalog-functions)
-   [WinTrust Functions](#wintrust-functions)
-   [Object Locator Functions](#object-locator-functions)

## CryptXML Functions

The cryptographic XML functions provide an API for creating and representing digital signatures by using XML formatted data. For information about XML formatted signatures, see the XML-Signature Syntax and Processing specification at <http://go.microsoft.com/fwlink/p/?linkid=139649>.



| Function                                                                          | Description                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**A\_SHAFinal**](a-shafinal.md)                                                 | Computes the final hash of the data entered by the MD5Update function.                                                                                                                                                                                                                                           |
| [**A\_SHAInit**](a-shainit.md)                                                   | Initiates the hashing of a stream of data.                                                                                                                                                                                                                                                                       |
| [**A\_SHAUpdate**](a-shaupdate.md)                                               | Adds data to a specified hash object.                                                                                                                                                                                                                                                                            |
| [**CryptXmlCreateReference**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlcreatereference?branch=master)                        | Creates a reference to an XML signature.                                                                                                                                                                                                                                                                         |
| [**CryptXmlAddObject**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmladdobject?branch=master)                                    | Adds the **Object** element to the Signature in the Document Context opened for encoding.                                                                                                                                                                                                                        |
| [**CryptXmlClose**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlclose?branch=master)                                            | Closes a cryptographic XML object handle.                                                                                                                                                                                                                                                                        |
| [**CryptXmlDigestReference**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmldigestreference?branch=master)                        | Used by an application to digest the resolved reference. This function applies transforms before updating the digest.                                                                                                                                                                                            |
| [**CryptXmlDllCloseDigest**](/windows/win32/Cryptxml/nc-cryptxml-cryptxmldllclosedigest?branch=master)                          | Frees the CRYPT\_XML\_DIGEST allocated by the [**CryptXmlDllCreateDigest**](/windows/win32/Cryptxml/nc-cryptxml-cryptxmldllcreatedigest?branch=master) function.                                                                                                                                                                                               |
| [**CryptXmlDllCreateDigest**](/windows/win32/Cryptxml/nc-cryptxml-cryptxmldllcreatedigest?branch=master)                        | Creates a digest object for the specified method.                                                                                                                                                                                                                                                                |
| [**CryptXmlDllCreateKey**](/windows/win32/cryptxml/nc-cryptxml-cryptxmldllcreatekey?branch=master)                              | Parses the **KeyValue** element and creates a Cryptography API: Next Generation (CNG) BCrypt key handle to verify a signature.                                                                                                                                                                                   |
| [**CryptXmlDllDigestData**](/windows/win32/Cryptxml/nc-cryptxml-cryptxmldlldigestdata?branch=master)                            | Puts data into the digest.                                                                                                                                                                                                                                                                                       |
| [**CryptXmlDllEncodeAlgorithm**](/windows/win32/Cryptxml/nc-cryptxml-cryptxmldllencodealgorithm?branch=master)                  | Encodes **SignatureMethod** or **DigestMethod** elements for agile algorithms with default parameters.                                                                                                                                                                                                           |
| [**CryptXmlDllEncodeKeyValue**](/windows/win32/cryptxml/nc-cryptxml-cryptxmldllencodekeyvalue?branch=master)                    | Encodes a **KeyValue** element.                                                                                                                                                                                                                                                                                  |
| [**CryptXmlDllFinalizeDigest**](/windows/win32/Cryptxml/nc-cryptxml-cryptxmldllfinalizedigest?branch=master)                    | Retrieves the digest value.                                                                                                                                                                                                                                                                                      |
| [**CryptXmlDllGetAlgorithmInfo**](/windows/win32/Cryptxml/nc-cryptxml-cryptxmldllgetalgorithminfo?branch=master)                | Decodes the XML algorithm and returns information about the algorithm.                                                                                                                                                                                                                                           |
| [**CryptXmlDllGetInterface**](/windows/win32/Cryptxml/nc-cryptxml-cryptxmldllgetinterface?branch=master)                        | Retrieves a pointer to the cryptographic extension functions for the specified algorithm.                                                                                                                                                                                                                        |
| [**CryptXmlDllSignData**](/windows/win32/Cryptxml/nc-cryptxml-cryptxmldllsigndata?branch=master)                                | Signs data.                                                                                                                                                                                                                                                                                                      |
| [**CryptXmlDllVerifySignature**](/windows/win32/Cryptxml/nc-cryptxml-cryptxmldllverifysignature?branch=master)                  | Verifies a signature.                                                                                                                                                                                                                                                                                            |
| [**CryptXmlEncode**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlencode?branch=master)                                          | Encodes signature data by using the supplied XML writer callback function.                                                                                                                                                                                                                                       |
| [**CryptXmlGetAlgorithmInfo**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlgetalgorithminfo?branch=master)                      | Decodes the CRYPT\_XML\_ALGORITHM structure and returns information about the algorithm.                                                                                                                                                                                                                         |
| [**CryptXmlGetDocContext**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlgetdoccontext?branch=master)                            | Returns the document context specified by the supplied handle.                                                                                                                                                                                                                                                   |
| [**CryptXmlGetReference**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlgetreference?branch=master)                              | Returns the **Reference** element specified by the supplied handle.                                                                                                                                                                                                                                              |
| [**CryptXmlGetSignature**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlgetsignature?branch=master)                              | Returns an XML **Signature** element.                                                                                                                                                                                                                                                                            |
| [**CryptXmlGetStatus**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlgetstatus?branch=master)                                    | Returns a [**CRYPT\_XML\_STATUS**](/windows/win32/Cryptxml/ns-cryptxml-_crypt_xml_status?branch=master) structure that contains status information about the object specified by the supplied handle.                                                                                                                                                           |
| [**CryptXmlGetTransforms**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlgettransforms?branch=master)                            | Returns information about the default transform chain engine.                                                                                                                                                                                                                                                    |
| [**CryptXmlImportPublicKey**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlimportpublickey?branch=master)                        | Imports the public key specified by the supplied handle.                                                                                                                                                                                                                                                         |
| [**CryptXmlOpenToEncode**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlopentoencode?branch=master)                              | Opens an XML digital signature to encode and returns a handle of the opened **Signature** element. The handle encapsulates a document context with a single [**CRYPT\_XML\_SIGNATURE**](/windows/win32/Cryptxml/ns-cryptxml-_crypt_xml_signature?branch=master) structure and remains open until the [**CryptXmlClose**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlclose?branch=master) function is called. |
| [**CryptXmlOpenToDecode**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlopentodecode?branch=master)                              | Opens an XML digital signature to decode and returns the handle of the document context that encapsulates a [**CRYPT\_XML\_SIGNATURE**](/windows/win32/Cryptxml/ns-cryptxml-_crypt_xml_signature?branch=master) structure. The document context can include one or more **Signature** elements.                                                                 |
| [**CryptXmlSetHMACSecret**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlsethmacsecret?branch=master)                            | Sets the HMAC secret on the handle before calling the [**CryptXmlSign**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlsign?branch=master) or [**CryptXmlVerify**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlverifysignature?branch=master) function.                                                                                                                                                        |
| [**CryptXmlSign**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlsign?branch=master)                                              | Creates a cryptographic signature of a **SignedInfo** element.                                                                                                                                                                                                                                                   |
| [**CryptXmlVerifySignature**](/windows/win32/Cryptxml/nf-cryptxml-cryptxmlverifysignature?branch=master)                        | Performs a cryptographic signature validation of a **SignedInfo** element.                                                                                                                                                                                                                                       |
| [*PFN\_CRYPT\_XML\_WRITE\_CALLBACK*](/windows/win32/Cryptxml/nc-cryptxml-pfn_crypt_xml_write_callback?branch=master)            | Creates a transform for a specified data provider.                                                                                                                                                                                                                                                               |
| [*PFN\_CRYPT\_XML\_CREATE\_TRANSFORM*](/windows/win32/Cryptxml/nc-cryptxml-pfn_crypt_xml_create_transform?branch=master)        | Writes cryptographic XML data.                                                                                                                                                                                                                                                                                   |
| [*PFN\_CRYPT\_XML\_DATA\_PROVIDER\_READ*](/windows/win32/Cryptxml/nc-cryptxml-pfn_crypt_xml_data_provider_read?branch=master)   | Reads cryptographic XML data.                                                                                                                                                                                                                                                                                    |
| [*PFN\_CRYPT\_XML\_DATA\_PROVIDER\_CLOSE*](/windows/win32/Cryptxml/nc-cryptxml-pfn_crypt_xml_data_provider_close?branch=master) | Releases the cryptographic XML data provider.                                                                                                                                                                                                                                                                    |
| [*PFN\_CRYPT\_XML\_ENUM\_ALG\_INFO*](/windows/win32/Cryptxml/nc-cryptxml-pfn_crypt_xml_enum_alg_info?branch=master)             | Enumerates predefined and registered [**CRYPT\_XML\_ALGORITHM\_INFO**](/windows/win32/Cryptxml/ns-cryptxml-_crypt_xml_algorithm_info?branch=master) entries.                                                                                                                                                                                                    |



 

## Signer Functions

Provides functions to sign and time stamp data.



| Function                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SignerFreeSignerContext**](signerfreesignercontext.md) | Frees a [**SIGNER\_CONTEXT**](signer-context.md) structure allocated by a previous call to the [**SignerSignEx**](signersignex.md) function.                                                                                                                                                                                                                                                                      |
| [**SignError**](signerror.md)                             | Calls the [**GetLastError**](base.getlasterror) function and converts the return code to an **HRESULT**.                                                                                                                                                                                                                                                                                                            |
| [**SignerSign**](signersign.md)                           | Signs the specified file.                                                                                                                                                                                                                                                                                                                                                                                           |
| [**SignerSignEx**](signersignex.md)                       | Signs the specified file and returns a pointer to the signed data.                                                                                                                                                                                                                                                                                                                                                  |
| [**SignerSignEx2**](signersignex2.md)                     | Signs and time stamps the specified file, allowing multiple nested signatures.                                                                                                                                                                                                                                                                                                                                      |
| [**SignerTimeStamp**](signertimestamp.md)                 | Time stamps the specified subject. This function supports Authenticode time stamping. To perform X.509 Public Key Infrastructure (RFC 3161) time stamping, use the [**SignerTimeStampEx2**](signertimestampex2.md) function.                                                                                                                                                                                       |
| [**SignerTimeStampEx**](signertimestampex.md)             | Time stamps the specified subject and optionally returns a pointer to a [**SIGNER\_CONTEXT**](signer-context.md) structure that contains a pointer to a [*BLOB*](security.b_gly#-security-blob-gly). This function supports Authenticode time stamping. To perform X.509 Public Key Infrastructure (RFC 3161) time stamping, use the [**SignerTimeStampEx2**](signertimestampex2.md) function. |
| [**SignerTimeStampEx2**](signertimestampex2.md)           | Time stamps the specified subject and optionally returns a pointer to a [**SIGNER\_CONTEXT**](signer-context.md) structure that contains a pointer to a [*BLOB*](security.b_gly#-security-blob-gly). This function can be used to perform X.509 Public Key Infrastructure, RFC 3161–compliant, time stamps.                                                                                     |
| [**SignerTimeStampEx3**](signertimestampex3.md)           | Time stamps the specified subject and supports setting time stamps on multiple signatures.                                                                                                                                                                                                                                                                                                                          |



 

## Base Cryptography Functions

Base cryptographic functions provide the most flexible means of developing cryptography applications. All communication with a [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) occurs through these functions.

A CSP is an independent module that performs all cryptographic operations. At least one CSP is required with each application that uses cryptographic functions. A single application can occasionally use more than one CSP.

If more than one CSP is used, the one to use can be specified in the CryptoAPI cryptographic function calls. One CSP, the Microsoft Base Cryptographic Provider, is bundled with the [*CryptoAPI*](security.c_gly#-security-cryptoapi-gly). This CSP is used as a default provider by many of the CryptoAPI functions if no other CSP is specified.

Each CSP provides a different implementation of the cryptographic support provided to CryptoAPI. Some provide stronger cryptographic algorithms; others contain hardware components, such as [*smart cards*](security.s_gly#-security-smart-card-gly). In addition, some CSPs can occasionally communicate directly with users, such as when [*digital signatures*](security.d_gly#-security-digital-signature-gly) are performed by using the user's [*signature private key*](security.s_gly#-security-signature-private-key-gly).

Base cryptographic functions are in the following broad groups:

-   Service Provider Functions
-   Key Generation and Exchange Functions
-   Object Encoding and Decoding Functions
-   Data Encryption and Decryption Functions
-   Hash and Digital Signature Functions

### Service Provider Functions

Applications use the following service functions to connect and disconnect a [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>CryptAcquireContext</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptacquirecontexta?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Acquires a handle to the current user's [<em>key container</em>](security.k_gly#-security-key-container-gly) within a particular CSP.</td>
</tr>
<tr class="even">
<td>[<strong>CryptContextAddRef</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptcontextaddref?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Increments the [<em>reference count</em>](security.r_gly#-security-reference-count-gly) on an [<strong>HCRYPTPROV</strong>](hcryptprov.md) handle.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptEnumProviders</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptenumprovidersa?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Enumerates the providers on a computer.</td>
</tr>
<tr class="even">
<td>[<strong>CryptEnumProviderTypes</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptenumprovidertypesa?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Enumerates the types of providers supported on the computer.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGetDefaultProvider</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptgetdefaultprovidera?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Determines the default CSP either for the current user or for the computer for a specified provider type.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGetProvParam</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptgetprovparam?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves the parameters that govern the operations of a CSP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptInstallDefaultContext</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptinstalldefaultcontext?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Installs a previously acquired [<strong>HCRYPTPROV</strong>](hcryptprov.md) context to be used as a default context.</td>
</tr>
<tr class="even">
<td>[<strong>CryptReleaseContext</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptreleasecontext?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Releases the handle acquired by the [<strong>CryptAcquireContext</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptacquirecontexta?branch=master) function.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSetProvider</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptsetprovidera?branch=master) and [<strong>CryptSetProviderEx</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptsetproviderexa?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies the user default CSP for a particular CSP type.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSetProvParam</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptsetprovparam?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies attributes of a CSP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUninstallDefaultContext</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptuninstalldefaultcontext?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Removes a default context previously installed by [<strong>CryptInstallDefaultContext</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptinstalldefaultcontext?branch=master).</td>
</tr>
<tr class="even">
<td>[<strong>FreeCryptProvFromCertEx</strong>](freecryptprovfromcertex.md)</td>
<td>Releases the handle either to a [<em>cryptographic service provider</em>](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) or to a Cryptography API: Next Generation (CNG) key.</td>
</tr>
</tbody>
</table>



 

### Key Generation and Exchange Functions

Key generation and exchange functions [*exchange keys*](security.e_gly#-security-exchange-key-pair-gly) with other users and create, configure, and destroy [*cryptographic keys*](security.c_gly#-security-cryptographic-key-gly).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>CryptDeriveKey</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptderivekey?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a key derived from a password.</td>
</tr>
<tr class="even">
<td>[<strong>CryptDestroyKey</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptdestroykey?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Destroys a key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptDuplicateKey</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptduplicatekey?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Makes an exact copy of a key, including the [<em>state</em>](security.s_gly#-security-state-gly) of the key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptExportKey</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptexportkey?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Transfers a key from the CSP into a [<em>key BLOB</em>](security.k_gly#-security-key-blob-gly) in the application's memory space.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGenKey</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptgenkey?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a random key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGenRandom</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptgenrandom?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Generates random data.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGetKeyParam</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptgetkeyparam?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves a key's parameters.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGetUserKey</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptgetuserkey?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Gets a handle to the key exchange or signature key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptImportKey</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptimportkey?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Transfers a key from a [<em>key BLOB</em>](security.k_gly#-security-key-blob-gly) to a CSP.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSetKeyParam</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptsetkeyparam?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies a key's parameters.</td>
</tr>
</tbody>
</table>



 

### Object Encoding and Decoding Functions

These are generalized encoding and decoding functions. They are used to encode and decode [*certificates*](security.c_gly#-security-certificate-gly), [*certificate revocation lists*](security.c_gly#-security-certificate-revocation-list-gly) (CRLs), [*certificate requests*](security.c_gly#-security-certificate-request-gly), and certificate extensions.

| Function                                           | Description                                                                                                                                      |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptDecodeObject**](/windows/win32/Wincrypt/nf-wincrypt-cryptdecodeobject?branch=master)     | Decodes a structure of type *lpszStructType*.                                                                                                    |
| [**CryptDecodeObjectEx**](/windows/win32/Wincrypt/nf-wincrypt-cryptdecodeobjectex?branch=master) | Decodes a structure of type *lpszStructType*. [**CryptDecodeObjectEx**](/windows/win32/Wincrypt/nf-wincrypt-cryptdecodeobjectex?branch=master) supports the one-pass memory allocation option. |
| [**CryptEncodeObject**](/windows/win32/Wincrypt/nf-wincrypt-cryptencodeobject?branch=master)     | Encodes a structure of type *lpszStructType*.                                                                                                    |
| [**CryptEncodeObjectEx**](/windows/win32/Wincrypt/nf-wincrypt-cryptencodeobjectex?branch=master) | Encodes a structure of type *lpszStructType*. [**CryptEncodeObjectEx**](/windows/win32/Wincrypt/nf-wincrypt-cryptencodeobjectex?branch=master) supports the one-pass memory allocation option. |



 

### Data Encryption and Decryption Functions

The following functions support encryption and decryption operations. [**CryptEncrypt**](/windows/win32/Wincrypt/nf-wincrypt-cryptencrypt?branch=master) and [**CryptDecrypt**](/windows/win32/Wincrypt/nf-wincrypt-cryptdecrypt?branch=master) require a [*cryptographic key*](security.c_gly#-security-cryptographic-key-gly) before being called. This is done by using the [**CryptGenKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptgenkey?branch=master), [**CryptDeriveKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptderivekey?branch=master), or [**CryptImportKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptimportkey?branch=master) function. The encryption algorithm is specified when the key is created. [**CryptSetKeyParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptsetkeyparam?branch=master) can set additional encryption parameters.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>CryptDecrypt</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptdecrypt?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Decrypts a section of [<em>ciphertext</em>](security.c_gly#-security-ciphertext-gly) by using the specified encryption key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptEncrypt</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptencrypt?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Encrypts a section of [<em>plaintext</em>](security.p_gly#-security-plaintext-gly) by using the specified encryption key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptProtectData</strong>](/windows/win32/Dpapi/nf-dpapi-cryptprotectdata?branch=master)</td>
<td>Performs encryption on the data in a [<strong>DATA_BLOB</strong>](crypt-integer-blob.md) structure.</td>
</tr>
<tr class="even">
<td>[<strong>CryptProtectMemory</strong>](/windows/win32/Dpapi/nf-dpapi-cryptprotectmemory?branch=master)</td>
<td>Encrypts memory to protect sensitive information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUnprotectData</strong>](/windows/win32/Dpapi/nf-dpapi-cryptunprotectdata?branch=master)</td>
<td>Performs a decryption and integrity check of the data in a [<strong>DATA_BLOB</strong>](crypt-integer-blob.md).</td>
</tr>
<tr class="even">
<td>[<strong>CryptUnprotectMemory</strong>](/windows/win32/Dpapi/nf-dpapi-cryptunprotectmemory?branch=master)</td>
<td>Decrypts memory that was encrypted using [<strong>CryptProtectMemory</strong>](/windows/win32/Dpapi/nf-dpapi-cryptprotectmemory?branch=master).</td>
</tr>
</tbody>
</table>



 

### Hash and Digital Signature Functions

These functions compute [*hashes*](security.h_gly#-security-hash-gly) of data and also create and verify [*digital signatures*](security.d_gly#-security-digital-signature-gly). Hashes are also known as message digests.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>CryptCreateHash</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptcreatehash?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates an empty hash object.</td>
</tr>
<tr class="even">
<td>[<strong>CryptDestroyHash</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptdestroyhash?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Destroys a hash object.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptDuplicateHash</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptduplicatehash?branch=master)</td>
<td>Duplicates a hash object.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGetHashParam</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptgethashparam?branch=master)</td>
<td>Retrieves a hash object parameter.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptHashData</strong>](/windows/win32/Wincrypt/nf-wincrypt-crypthashdata?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes a block of data, adding it to the specified hash object.</td>
</tr>
<tr class="even">
<td>[<strong>CryptHashSessionKey</strong>](/windows/win32/Wincrypt/nf-wincrypt-crypthashsessionkey?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes a session key, adding it to the specified hash object.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSetHashParam</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptsethashparam?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Sets a hash object parameter.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSignHash</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptsignhasha?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Signs the specified hash object.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUIWizDigitalSign</strong>](/windows/win32/Cryptuiapi/nf-cryptuiapi-cryptuiwizdigitalsign?branch=master)</td>
<td>Displays a wizard that digitally signs a document or a [<em>BLOB</em>](security.b_gly#-security-blob-gly).</td>
</tr>
<tr class="even">
<td>[<strong>CryptUIWizFreeDigitalSignContext</strong>](/windows/win32/Cryptuiapi/nf-cryptuiapi-cryptuiwizfreedigitalsigncontext?branch=master)</td>
<td>Releases a pointer to a [<strong>CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT</strong>](/windows/win32/Cryptuiapi/ns-cryptuiapi-_cryptui_wiz_digital_sign_context?branch=master) structure.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptVerifySignature</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptverifysignaturea?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Verifies a digital signature, given a handle to the hash object.</td>
</tr>
<tr class="even">
<td>[<strong>PFNCFILTERPROC</strong>](/windows/win32/Cryptuiapi/nc-cryptuiapi-pfncfilterproc?branch=master)</td>
<td>Filters the certificates that appear in the digital signature wizard displayed by the [<strong>CryptUIWizDigitalSign</strong>](/windows/win32/Cryptuiapi/nf-cryptuiapi-cryptuiwizdigitalsign?branch=master) function.</td>
</tr>
</tbody>
</table>



 

## Certificate and Certificate Store Functions

Certificate and certificate store functions manage the use, storage, and retrieval of [*certificates*](security.c_gly#-security-certificate-gly), [*certificate revocation lists*](security.c_gly#-security-certificate-revocation-list-gly) (CRLs), and [*certificate trust lists*](security.c_gly#-security-certificate-trust-list-gly) (CTLs). These functions are divided into the following groups:

-   Certificate Store Functions
-   Certificate and Certificate Store Maintenance Functions
-   Certificate Functions
-   Certificate Revocation List Functions
-   Certificate Trust List Functions
-   Extended Property Functions
-   MakeCert Functions

### Certificate Store Functions

A user site can, over time, collect many certificates. Typically, a site has certificates for the user of the site as well as other certificates that describe those individuals and entities with whom the user communicates. For each entity, there can be more than one certificate. For each individual certificate, there should be a chain of verifying certificates that provides a trail back to a trusted [*root certificate*](security.r_gly#-security-root-certificate-gly). [*Certificate stores*](security.c_gly#-security-certificate-store-gly) and their related functions provide functionality to store, retrieve, enumerate, verify, and use the information stored in the certificates.

| Function                                                               | Description                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddStoreToCollection**](/windows/win32/Wincrypt/nf-wincrypt-certaddstoretocollection?branch=master)           | Adds a sibling certificate store to a collection certificate store.                                                                                                                                                                                                                                                                       |
| [**CertCloseStore**](/windows/win32/Wincrypt/nf-wincrypt-certclosestore?branch=master)                               | Closes a certificate store handle.                                                                                                                                                                                                                                                                                                        |
| [**CertControlStore**](/windows/win32/Wincrypt/nf-wincrypt-certcontrolstore?branch=master)                           | Allows an application to be notified when there is a difference between the contents of a cached store and the contents of the store that is persisted to storage. It also provides desynchronization of the cached store, if necessary, and provides a means to commit changes made in the cached store to persisted storage.<br/> |
| [**CertDuplicateStore**](/windows/win32/Wincrypt/nf-wincrypt-certduplicatestore?branch=master)                       | Duplicates a store handle by incrementing the [*reference count*](security.r_gly#-security-reference-count-gly).                                                                                                                                                                                            |
| [**CertEnumPhysicalStore**](/windows/win32/Wincrypt/nf-wincrypt-certenumphysicalstore?branch=master)                 | Enumerates the physical stores for a specified system store.                                                                                                                                                                                                                                                                              |
| [**CertEnumSystemStore**](/windows/win32/Wincrypt/nf-wincrypt-certenumsystemstore?branch=master)                     | Enumerates all available system stores.                                                                                                                                                                                                                                                                                                   |
| [**CertEnumSystemStoreLocation**](/windows/win32/Wincrypt/nf-wincrypt-certenumsystemstorelocation?branch=master)     | Enumerates all of the locations that have an available system store.                                                                                                                                                                                                                                                                      |
| [**CertGetStoreProperty**](/windows/win32/Wincrypt/nf-wincrypt-certgetstoreproperty?branch=master)                   | Gets a store property.                                                                                                                                                                                                                                                                                                                    |
| [**CertOpenStore**](/windows/win32/Wincrypt/nf-wincrypt-certopenstore?branch=master)                                 | Opens a certificate store using a specified store provider type.                                                                                                                                                                                                                                                                          |
| [**CertOpenSystemStore**](/windows/win32/Wincrypt/nf-wincrypt-certopensystemstorea?branch=master)                     | Opens a system certificate store based on a subsystem protocol.                                                                                                                                                                                                                                                                           |
| [**CertRegisterPhysicalStore**](/windows/win32/Wincrypt/nf-wincrypt-certregisterphysicalstore?branch=master)         | Adds a physical store to a registry system store collection.                                                                                                                                                                                                                                                                              |
| [**CertRegisterSystemStore**](/windows/win32/Wincrypt/nf-wincrypt-certregistersystemstore?branch=master)             | Registers a system store.                                                                                                                                                                                                                                                                                                                 |
| [**CertRemoveStoreFromCollection**](/windows/win32/Wincrypt/nf-wincrypt-certremovestorefromcollection?branch=master) | Removes a sibling certificate store from a collection store.                                                                                                                                                                                                                                                                              |
| [**CertSaveStore**](/windows/win32/Wincrypt/nf-wincrypt-certsavestore?branch=master)                                 | Saves the certificate store.                                                                                                                                                                                                                                                                                                              |
| [**CertSetStoreProperty**](/windows/win32/Wincrypt/nf-wincrypt-certsetstoreproperty?branch=master)                   | Sets a store property.                                                                                                                                                                                                                                                                                                                    |
| [**CertUnregisterPhysicalStore**](/windows/win32/Wincrypt/nf-wincrypt-certunregisterphysicalstore?branch=master)     | Removes a physical store from a specified system store collection.                                                                                                                                                                                                                                                                        |
| [**CertUnregisterSystemStore**](/windows/win32/Wincrypt/nf-wincrypt-certunregistersystemstore?branch=master)         | Unregisters a specified system store.                                                                                                                                                                                                                                                                                                     |
| [**CryptUIWizExport**](/windows/win32/Cryptuiapi/nf-cryptuiapi-cryptuiwizexport?branch=master)                           | Presents a wizard that exports a certificate, certificate trust list (CTL), certificate revocation list (CRL), or certificate store.                                                                                                                                                                                                      |
| [**CryptUIWizImport**](/windows/win32/Cryptuiapi/nf-cryptuiapi-cryptuiwizimport?branch=master)                           | Presents a wizard that imports a certificate, certificate trust list (CTL), certificate revocation list (CRL), or certificate store.                                                                                                                                                                                                      |



 

### Certificate and Certificate Store Maintenance Functions

CryptoAPI provides a set of general certificate and certificate store maintenance functions.

| Function                                                                                                                              | Description                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**CertAddSerializedElementToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddserializedelementtostore?branch=master)                                                            | Adds the serialized certificate or CRL element to the store.                                   |
| [**CertCreateContext**](/windows/win32/Wincrypt/nf-wincrypt-certcreatecontext?branch=master)                                                                                        | Creates the specified context from the encoded bytes. The new context is not put into a store. |
| [**CertEnumSubjectInSortedCTL**](/windows/win32/Wincrypt/nf-wincrypt-certenumsubjectinsortedctl?branch=master)                                                                      | Enumerates the TrustedSubjects in a sorted CTL context.                                        |
| [**CertFindSubjectInCTL**](/windows/win32/Wincrypt/nf-wincrypt-certfindsubjectinctl?branch=master)                                                                                  | Finds the specified subject in a CTL.                                                          |
| [**CertFindSubjectInSortedCTL**](/windows/win32/Wincrypt/nf-wincrypt-certfindsubjectinsortedctl?branch=master)                                                                      | Finds the specified subject in a sorted CTL.                                                   |
| [**OpenPersonalTrustDBDialog**](/windows/win32/wintrust/nf-wintrust-openpersonaltrustdbdialog?branch=master) and [**OpenPersonalTrustDBDialogEx**](/windows/win32/wintrust/nf-wintrust-openpersonaltrustdbdialogex?branch=master) | Displays the **Certificates** dialog box.                                                      |



 

### Certificate Functions

Most [*Certificate*](security.c_gly#-security-certificate-gly) functions have related functions to deal with [*CRLs*](security.c_gly#-security-certificate-revocation-list-gly) and [*CTLs*](security.c_gly#-security-certificate-trust-list-gly). For more information about related CRL and CTL functions, see Certificate Revocation List Functions and Certificate Trust List Functions.

| Function                                                                             | Description                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddCertificateContextToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcertificatecontexttostore?branch=master)         | Adds a certificate context to the certificate store.                                                                                                                                                                                            |
| [**CertAddCertificateLinkToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcertificatelinktostore?branch=master)               | Adds a link in a certificate store to a certificate context in a different store.                                                                                                                                                               |
| [**CertAddEncodedCertificateToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddencodedcertificatetostore?branch=master)         | Converts the encoded certificate to a certificate context, and then adds the context to the certificate store.                                                                                                                                  |
| [**CertAddRefServerOcspResponse**](/windows/win32/Wincrypt/nf-wincrypt-certaddrefserverocspresponse?branch=master)                 | Increments the reference count for an **HCERT\_SERVER\_OCSP\_RESPONSE** handle.                                                                                                                                                                 |
| [**CertAddRefServerOcspResponseContext**](/windows/win32/Wincrypt/nf-wincrypt-certaddrefserverocspresponsecontext?branch=master)   | Increments the reference count for a [**CERT\_SERVER\_OCSP\_RESPONSE\_CONTEXT**](/windows/win32/Wincrypt/ns-wincrypt-_cert_server_ocsp_response_context?branch=master) structure.                                                                                                              |
| [**CertCloseServerOcspResponse**](/windows/win32/Wincrypt/nf-wincrypt-certcloseserverocspresponse?branch=master)                   | Closes an [*online certificate status protocol*](security.o_gly#-security-online-certificate-status-protocol-gly) (OCSP) server response handle.                                               |
| [**CertCreateCertificateContext**](/windows/win32/Wincrypt/nf-wincrypt-certcreatecertificatecontext?branch=master)                 | Creates a certificate context from an encoded certificate. The created context is not put in a certificate store.                                                                                                                               |
| [**CertCreateSelfSignCertificate**](/windows/win32/Wincrypt/nf-wincrypt-certcreateselfsigncertificate?branch=master)               | Creates a self-signed certificate.                                                                                                                                                                                                              |
| [**CertDeleteCertificateFromStore**](/windows/win32/Wincrypt/nf-wincrypt-certdeletecertificatefromstore?branch=master)             | Deletes a certificate from the certificate store.                                                                                                                                                                                               |
| [**CertDuplicateCertificateContext**](/windows/win32/Wincrypt/nf-wincrypt-certduplicatecertificatecontext?branch=master)           | Duplicates a certificate context by incrementing its [*reference count*](security.r_gly#-security-reference-count-gly).                                                                                           |
| [**CertEnumCertificatesInStore**](/windows/win32/Wincrypt/nf-wincrypt-certenumcertificatesinstore?branch=master)                   | Enumerates the certificate contexts in the certificate store.                                                                                                                                                                                   |
| [**CertFindCertificateInStore**](/windows/win32/Wincrypt/nf-wincrypt-certfindcertificateinstore?branch=master)                     | Finds the first, or next, certificate context in the certificate store that meets a search criterion.                                                                                                                                           |
| [**CertFreeCertificateContext**](/windows/win32/Wincrypt/nf-wincrypt-certfreecertificatecontext?branch=master)                     | Frees a certificate context.                                                                                                                                                                                                                    |
| [**CertGetIssuerCertificateFromStore**](/windows/win32/Wincrypt/nf-wincrypt-certgetissuercertificatefromstore?branch=master)       | Gets a certificate context from the certificate store for the first, or next, issuer of the specified subject certificate.                                                                                                                      |
| [**CertGetServerOcspResponseContext**](/windows/win32/Wincrypt/nf-wincrypt-certgetserverocspresponsecontext?branch=master)         | Retrieves a non-blocking, time valid [*online certificate status protocol*](security.o_gly#-security-online-certificate-status-protocol-gly) (OCSP) response context for the specified handle. |
| [**CertGetSubjectCertificateFromStore**](/windows/win32/Wincrypt/nf-wincrypt-certgetsubjectcertificatefromstore?branch=master)     | Gets from the certificate store the subject certificate context, which is uniquely identified by its issuer and serial number.                                                                                                                  |
| [**CertGetValidUsages**](/windows/win32/Wincrypt/nf-wincrypt-certgetvalidusages?branch=master)                                     | Returns an array of usages that consist of the intersection of the valid usages for all certificates in an array of certificates.                                                                                                               |
| [**CertOpenServerOcspResponse**](/windows/win32/Wincrypt/nf-wincrypt-certopenserverocspresponse?branch=master)                     | Opens a handle to an [*online certificate status protocol*](security.o_gly#-security-online-certificate-status-protocol-gly) (OCSP) response associated with a server certificate chain.       |
| [**CertRetrieveLogoOrBiometricInfo**](/windows/win32/Wincrypt/nf-wincrypt-certretrievelogoorbiometricinfo?branch=master)           | Performs a URL retrieval of logo or biometric information specified in either the **szOID\_LOGOTYPE\_EXT** or **szOID\_BIOMETRIC\_EXT** certificate extension.                                                                                  |
| [**CertSelectCertificate**](/windows/win32/CryptDlg/?branch=master)                               | Presents a dialog box that allows the user to select certificates from a set of certificates that match a given criteria.                                                                                                                       |
| [**CertSelectCertificateChains**](/windows/win32/Wincrypt/nf-wincrypt-certselectcertificatechains?branch=master)                   | Retrieves certificate chains based on specified selection criteria.                                                                                                                                                                             |
| [**CertSelectionGetSerializedBlob**](/windows/win32/Cryptuiapi/nf-cryptuiapi-certselectiongetserializedblob?branch=master)             | A helper function used to retrieve a serialized certificate [*BLOB*](security.b_gly#-security-blob-gly) from a [**CERT\_SELECTUI\_INPUT**](/windows/win32/Cryptuiapi/ns-cryptuiapi-cert_selectui_input?branch=master) structure.                                               |
| [**CertSerializeCertificateStoreElement**](/windows/win32/Wincrypt/nf-wincrypt-certserializecertificatestoreelement?branch=master) | Serializes a certificate context's encoded certificate and an encoded representation of its properties.                                                                                                                                         |
| [**CertVerifySubjectCertificateContext**](/windows/win32/Wincrypt/nf-wincrypt-certverifysubjectcertificatecontext?branch=master)   | Performs the enabled verification checks on the subject certificate using the issuer.                                                                                                                                                           |
| [**CryptUIDlgCertMgr**](/windows/win32/Cryptuiapi/nf-cryptuiapi-cryptuidlgcertmgr?branch=master)                                       | Displays a dialog box that allows the user to manage certificates.                                                                                                                                                                              |
| [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md)                   | Displays a dialog box that allows a user to select a certificate.                                                                                                                                                                               |
| [**CryptUIDlgSelectCertificateFromStore**](/windows/win32/Cryptuiapi/nf-cryptuiapi-cryptuidlgselectcertificatefromstore?branch=master) | Displays a dialog box that allows the selection of a certificate from a specified store.                                                                                                                                                        |
| [**CryptUIDlgViewCertificate**](/windows/win32/Cryptuiapi/nf-cryptuiapi-cryptuidlgviewcertificatea?branch=master)                       | Presents a dialog box that displays a specified certificate.                                                                                                                                                                                    |
| [**CryptUIDlgViewContext**](/windows/win32/Cryptuiapi/nf-cryptuiapi-cryptuidlgviewcontext?branch=master)                               | Displays a certificate, CRL, or CTL.                                                                                                                                                                                                            |
| [**CryptUIDlgViewSignerInfo**](cryptuidlgviewsignerinfo.md)                         | Displays a dialog box that contains the signer information for a signed message.                                                                                                                                                                |
| [**GetFriendlyNameOfCert**](/windows/win32/CryptDlg/nf-cryptdlg-getfriendlynameofcerta?branch=master)                               | Retrieves the display name for a certificate.                                                                                                                                                                                                   |
| [**RKeyCloseKeyService**](rkeyclosekeyservice.md)                                   | Closes a key service handle.                                                                                                                                                                                                                    |
| [**RKeyOpenKeyService**](rkeyopenkeyservice.md)                                     | Opens a key service handle on a remote computer.                                                                                                                                                                                                |
| [**RKeyPFXInstall**](rkeypfxinstall.md)                                             | Installs a certificate on a remote computer.                                                                                                                                                                                                    |



 

### Certificate Revocation List Functions

These functions manage the storage and retrieval of [*certificate revocation lists*](security.c_gly#-security-certificate-revocation-list-gly) (CRLs).

| Function                                                             | Description                                                                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddCRLContextToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcrlcontexttostore?branch=master)         | Adds a CRL context to the certificate store.                                                                                                                                          |
| [**CertAddCRLLinkToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddcrllinktostore?branch=master)               | Adds a link in a store to a CRL context in a different store.                                                                                                                         |
| [**CertAddEncodedCRLToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddencodedcrltostore?branch=master)         | Converts the encoded CRL to a CRL context, and then adds the context to the certificate store.                                                                                        |
| [**CertCreateCRLContext**](/windows/win32/Wincrypt/nf-wincrypt-certcreatecrlcontext?branch=master)                 | Creates a CRL context from an encoded CRL. The created context is not put in a certificate store.                                                                                     |
| [**CertDeleteCRLFromStore**](/windows/win32/Wincrypt/nf-wincrypt-certdeletecrlfromstore?branch=master)             | Deletes a CRL from the certificate store.                                                                                                                                             |
| [**CertDuplicateCRLContext**](/windows/win32/Wincrypt/nf-wincrypt-certduplicatecrlcontext?branch=master)           | Duplicates a CRL context by incrementing the [*reference count*](security.r_gly#-security-reference-count-gly).                                         |
| [**CertEnumCRLsInStore**](/windows/win32/Wincrypt/nf-wincrypt-certenumcrlsinstore?branch=master)                   | Enumerates the CRL contexts in a store.                                                                                                                                               |
| [**CertFindCertificateInCRL**](/windows/win32/Wincrypt/nf-wincrypt-certfindcertificateincrl?branch=master)         | Searches the [*certificate revocation list*](security.c_gly#-security-certificate-revocation-list-gly) (CRL) for the specified certificate. |
| [**CertFindCRLInStore**](/windows/win32/Wincrypt/nf-wincrypt-certfindcrlinstore?branch=master)                     | Finds the first, or next, CRL context in the certificate store that matches a specific criterion.                                                                                     |
| [**CertFreeCRLContext**](/windows/win32/Wincrypt/nf-wincrypt-certfreecrlcontext?branch=master)                     | Frees a CRL context.                                                                                                                                                                  |
| [**CertGetCRLFromStore**](/windows/win32/Wincrypt/nf-wincrypt-certgetcrlfromstore?branch=master)                   | Gets the first, or next, CRL context from the certificate store for the specified issuer certificate.                                                                                 |
| [**CertSerializeCRLStoreElement**](/windows/win32/Wincrypt/nf-wincrypt-certserializecrlstoreelement?branch=master) | Serializes the CRL context's encoded CRL and its properties.                                                                                                                          |



 

### Certificate Trust List Functions

These functions manage the storage and retrieval of [*certificate trust lists*](security.c_gly#-security-certificate-trust-list-gly) (CTLs).

| Function                                                               | Description                                                                                                          |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**CertAddCTLContextToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddctlcontexttostore?branch=master)           | Adds a CTL context to the certificate store.                                                                         |
| [**CertAddCTLLinkToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddctllinktostore?branch=master)                 | Adds a link in a store to a CRL context in a different store.                                                        |
| [**CertAddEncodedCTLToStore**](/windows/win32/Wincrypt/nf-wincrypt-certaddencodedctltostore?branch=master)           | Converts the encoded CTL to a CTL context, and then adds the context to the certificate store.                       |
| [**CertCreateCTLContext**](/windows/win32/Wincrypt/nf-wincrypt-certcreatectlcontext?branch=master)                   | Creates a CTL context from an encoded certificate trust list. The created context is not put in a certificate store. |
| [**CertDeleteCTLFromStore**](/windows/win32/Wincrypt/nf-wincrypt-certdeletectlfromstore?branch=master)               | Deletes a CTL from the certificate store.                                                                            |
| [**CertDuplicateCTLContext**](/windows/win32/Wincrypt/nf-wincrypt-certduplicatectlcontext?branch=master)             | Duplicates a CTL context by incrementing the reference count.                                                        |
| [**CertEnumCTLsInStore**](/windows/win32/Wincrypt/nf-wincrypt-certenumctlsinstore?branch=master)                     | Enumerates the CTL contexts in the certificate store.                                                                |
| [**CertFindCTLInStore**](/windows/win32/Wincrypt/nf-wincrypt-certfindctlinstore?branch=master)                       | Finds the first, or next, CTL context in the certificate store that matches a specific criteria.                     |
| [**CertFreeCTLContext**](/windows/win32/Wincrypt/nf-wincrypt-certfreectlcontext?branch=master)                       | Frees a CTL context.                                                                                                 |
| [**CertModifyCertificatesToTrust**](/windows/win32/CryptDlg/nf-cryptdlg-certmodifycertificatestotrust?branch=master) | Modifies the set of certificates in a CTL for a given purpose.                                                       |
| [**CertSerializeCTLStoreElement**](/windows/win32/Wincrypt/nf-wincrypt-certserializectlstoreelement?branch=master)   | Serializes the CTL context's encoded CTL and its properties.                                                         |



 

### Extended Property Functions

The following functions work with extended properties of certificates, CRLs, and CTLs.

| Function                                                                             | Description                                                      |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**CertEnumCertificateContextProperties**](/windows/win32/Wincrypt/nf-wincrypt-certenumcertificatecontextproperties?branch=master) | Enumerates the properties for the specified certificate context. |
| [**CertEnumCRLContextProperties**](/windows/win32/Wincrypt/nf-wincrypt-certenumcrlcontextproperties?branch=master)                 | Enumerates the properties for the specified CRL context.         |
| [**CertEnumCTLContextProperties**](/windows/win32/Wincrypt/nf-wincrypt-certenumctlcontextproperties?branch=master)                 | Enumerates the properties for the specified CTL context.         |
| [**CertGetCertificateContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty?branch=master)       | Retrieves certificate properties.                                |
| [**CertGetCRLContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certgetcrlcontextproperty?branch=master)                       | Retrieves CRL properties.                                        |
| [**CertGetCTLContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certgetctlcontextproperty?branch=master)                       | Retrieves CTL properties.                                        |
| [**CertSetCertificateContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certsetcertificatecontextproperty?branch=master)       | Sets certificate properties.                                     |
| [**CertSetCRLContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certsetcrlcontextproperty?branch=master)                       | Sets CRL properties.                                             |
| [**CertSetCTLContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certsetctlcontextproperty?branch=master)                       | Sets CTL properties.                                             |



 

## MakeCert Functions

The following functions support the [MakeCert](makecert.md) tool.



| Function                                                                               | Description                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FreeCryptProvFromCert**](freecryptprovfromcert.md)                                 | Releases the handle to a [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) and optionally deletes the temporary container created by the [**GetCryptProvFromCert**](getcryptprovfromcert.md) function. |
| [**GetCryptProvFromCert**](getcryptprovfromcert.md)                                   | Gets a handle to a CSP and a key specification for a certificate context.                                                                                                                                                                                                                                |
| [**PvkFreeCryptProv**](pvkfreecryptprov.md)                                           | Releases the handle to a CSP and optionally deletes the temporary container created by the [**PvkGetCryptProv**](pvkgetcryptprov.md) function.                                                                                                                                                          |
| [**PvkGetCryptProv**](pvkgetcryptprov.md)                                             | Gets a handle to a CSP based on either a [*private key*](security.p_gly#-security-private-key-gly) file name or a key container name.                                                                                                                                          |
| [**PvkPrivateKeyAcquireContextFromMemory**](pvkprivatekeyacquirecontextfrommemory.md) | Creates a temporary container in the CSP and loads a private key from memory into the container.                                                                                                                                                                                                         |
| [**PvkPrivateKeySave**](pvkprivatekeysave.md)                                         | Saves a private key and its corresponding [*public key*](security.p_gly#-security-public-key-gly) to a specified file.                                                                                                                                                          |
| [**SignError**](signerror.md)                                                         | Calls [**GetLastError**](base.getlasterror) and converts the return code to an **HRESULT**.                                                                                                                                                                                                              |



 

## Certificate Verification Functions

Certificates are verified using [*CTLs*](security.c_gly#-security-certificate-trust-list-gly) or certificate chains. Functions are provided for both of these:

-   Verification Functions Using CTLs
-   Certificate Chain Verification Functions

### Verification Functions Using CTLs

These functions use CTLs in the verification process. Additional functions for working with CTLs can be found in Certificate Trust List Functions and Extended Property Functions.

The following functions use CTLs directly for verification.

| Function                                                         | Description                                  |
|------------------------------------------------------------------|----------------------------------------------|
| [**CertVerifyCTLUsage**](/windows/win32/Wincrypt/nf-wincrypt-certverifyctlusage?branch=master)                 | Verifies the usage of a CTL.                 |
| [**CryptMsgEncodeAndSignCTL**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgencodeandsignctl?branch=master)     | Encodes and signs a CTL as a message.        |
| [**CryptMsgGetAndVerifySigner**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsggetandverifysigner?branch=master) | Retrieves and verifies a CTL from a message. |
| [**CryptMsgSignCTL**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgsignctl?branch=master)                       | Signs a message that contains a CTL.         |



 

### Certificate Chain Verification Functions

Certificate chains are built to provide trust information about individual certificates.

| Function Name                                                                                                    | Description                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertCreateCertificateChainEngine**](/windows/win32/Wincrypt/nf-wincrypt-certcreatecertificatechainengine?branch=master)                                     | Creates a new, nondefault chain engine for an application.                                                                                                                                                          |
| [**CertCreateCTLEntryFromCertificateContextProperties**](/windows/win32/Wincrypt/nf-wincrypt-certcreatectlentryfromcertificatecontextproperties?branch=master) | Creates a CTL entry whose attributes are the certificate context's properties.                                                                                                                                      |
| [**CertDuplicateCertificateChain**](/windows/win32/Wincrypt/nf-wincrypt-certduplicatecertificatechain?branch=master)                                           | Duplicates a certificate chain by incrementing the chain's [*reference count*](security.r_gly#-security-reference-count-gly) and returning a pointer to the chain.                    |
| [**CertFindChainInStore**](/windows/win32/Wincrypt/nf-wincrypt-certfindchaininstore?branch=master)                                                             | Finds the first, or next, certificate chain context in a store.                                                                                                                                                     |
| [**CertFreeCertificateChain**](/windows/win32/Wincrypt/nf-wincrypt-certfreecertificatechain?branch=master)                                                     | Frees a certificate chain by reducing its reference count.                                                                                                                                                          |
| [**CertFreeCertificateChainEngine**](/windows/win32/Wincrypt/nf-wincrypt-certfreecertificatechainengine?branch=master)                                         | Frees a nondefault certificate chain engine.                                                                                                                                                                        |
| [**CertFreeCertificateChainList**](/windows/win32/Wincrypt/nf-wincrypt-certfreecertificatechainlist?branch=master)                                             | Frees the array of pointers to chain contexts.                                                                                                                                                                      |
| [**CertGetCertificateChain**](/windows/win32/Wincrypt/nf-wincrypt-certgetcertificatechain?branch=master)                                                       | Builds a chain context starting from an end certificate and going back to a trusted [*root certificate*](security.r_gly#-security-root-certificate-gly), if possible.                |
| [**CertIsValidCRLForCertificate**](/windows/win32/Wincrypt/nf-wincrypt-certisvalidcrlforcertificate?branch=master)                                             | Checks a [*CRL*](security.c_gly#-security-certificate-revocation-list-gly) to determine whether it would include a specific certificate if that certificate were revoked. |
| [**CertSetCertificateContextPropertiesFromCTLEntry**](/windows/win32/Wincrypt/nf-wincrypt-certsetcertificatecontextpropertiesfromctlentry?branch=master)       | Sets properties on the certificate context using the attributes in the CTL entry.                                                                                                                                   |
| [**CertVerifyCertificateChainPolicy**](/windows/win32/Wincrypt/nf-wincrypt-certverifycertificatechainpolicy?branch=master)                                     | Checks a certificate chain to verify its validity, including its compliance with any specified validity policy criteria.                                                                                            |



 

## Message Functions

[*CryptoAPI*](security.c_gly#-security-cryptoapi-gly) message functions consist of two groups of functions: low-level message functions and [*simplified message functions*](security.s_gly#-security-simplified-message-functions-gly).

Low-level message functions create and work directly with PKCS \#7 messages. These functions encode PKCS \#7 data for transmission and decode PKCS \#7 data received. They also decrypt and verify the signatures of received messages. For an overview of the PKCS \#7 standard and low-level messages, see [Low-level Messages](low-level-messages.md).

Simplified message functions are at a higher level and wrap several low-level message functions and certificate functions into single functions that perform a specific task in a specific manner. These functions reduce the number of function calls needed to accomplish a task, thereby simplifying CryptoAPI use. For an overview of simplified messages, see [Simplified Messages](simplified-messages.md).

-   Low-level Message Functions
-   Simplified Message Functions

### Low-level Message Functions

Low-level message functions provide the functionality necessary to encode data for transmission and to decode PKCS \#7 messages received. Functionality is also provided to decrypt and verify the signatures of received messages. Use of these low-level message functions in most applications is not recommended. For most applications, the use of Simplified Message Functions, which wrap several low-level message functions into a single function call, is preferred.

| Function                                                                                   | Description                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptMsgCalculateEncodedLength**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgcalculateencodedlength?branch=master)                   | Calculates the length of an encoded cryptographic message.                                                                                                                                                                     |
| [**CryptMsgClose**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgclose?branch=master)                                                     | Closes a handle of a cryptographic message.                                                                                                                                                                                    |
| [**CryptMsgControl**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgcontrol?branch=master)                                                 | Performs a special control function after the final [**CryptMsgUpdate**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgupdate?branch=master) of an encoded or decoded cryptographic message.                                                                                   |
| [**CryptMsgCountersign**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgcountersign?branch=master)                                         | Countersigns an already existing signature in a message.                                                                                                                                                                       |
| [**CryptMsgCountersignEncoded**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgcountersignencoded?branch=master)                           | Countersigns an already existing signature (encoded SignerInfo, as defined by PKCS \#7).                                                                                                                                       |
| [**CryptMsgDuplicate**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgduplicate?branch=master)                                             | Duplicates a cryptographic message handle by incrementing the [*reference count*](security.r_gly#-security-reference-count-gly). The reference count keeps track of the lifetime of the message. |
| [**CryptMsgGetParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsggetparam?branch=master)                                               | Acquires a parameter after encoding or decoding a cryptographic message.                                                                                                                                                       |
| [**CryptMsgOpenToDecode**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgopentodecode?branch=master)                                       | Opens a cryptographic message for decoding.                                                                                                                                                                                    |
| [**CryptMsgOpenToEncode**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgopentoencode?branch=master)                                       | Opens a cryptographic message for encoding.                                                                                                                                                                                    |
| [**CryptMsgUpdate**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgupdate?branch=master)                                                   | Updates the contents of a cryptographic message.                                                                                                                                                                               |
| [**CryptMsgVerifyCountersignatureEncoded**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgverifycountersignatureencoded?branch=master)     | Verifies a [*countersignature*](security.c_gly#-security-countersignature-gly) in terms of the SignerInfo structure (as defined by PKCS \#7).                                                   |
| [**CryptMsgVerifyCountersignatureEncodedEx**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgverifycountersignatureencodedex?branch=master) | Verifies that the *pbSignerInfoCounterSignature* parameter contains the encrypted [*hash*](security.h_gly#-security-hash-gly) of the **encryptedDigest** field of the *pbSignerInfo* parameter structure.   |



 

### Simplified Message Functions

[*Simplified message functions*](security.s_gly#-security-simplified-message-functions-gly) wrap Low-level Message Functions into a single function to accomplish a specified task.

| Function                                                                               | Description                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptDecodeMessage**](/windows/win32/Wincrypt/nf-wincrypt-cryptdecodemessage?branch=master)                                       | Decodes a cryptographic message.                                                                                                                                                                                                                                             |
| [**CryptDecryptAndVerifyMessageSignature**](/windows/win32/Wincrypt/nf-wincrypt-cryptdecryptandverifymessagesignature?branch=master) | Decrypts the specified message, and verifies the signer.                                                                                                                                                                                                                     |
| [**CryptDecryptMessage**](/windows/win32/Wincrypt/nf-wincrypt-cryptdecryptmessage?branch=master)                                     | Decrypts the specified message.                                                                                                                                                                                                                                              |
| [**CryptEncryptMessage**](/windows/win32/Wincrypt/nf-wincrypt-cryptencryptmessage?branch=master)                                     | Encrypts the message for the recipient or recipients.                                                                                                                                                                                                                        |
| [**CryptGetMessageCertificates**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetmessagecertificates?branch=master)                     | Returns the [*certificate store*](security.c_gly#-security-certificate-store-gly) that contains the message's certificates and [*CRLs*](security.c_gly#-security-certificate-revocation-list-gly). |
| [**CryptGetMessageSignerCount**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetmessagesignercount?branch=master)                       | Returns the count of signers in the signed message.                                                                                                                                                                                                                          |
| [**CryptHashMessage**](/windows/win32/Wincrypt/nf-wincrypt-crypthashmessage?branch=master)                                           | Creates a hash of the message.                                                                                                                                                                                                                                               |
| [**CryptSignAndEncryptMessage**](/windows/win32/Wincrypt/nf-wincrypt-cryptsignandencryptmessage?branch=master)                       | Signs the message, and then encrypts it for the recipient or recipients.                                                                                                                                                                                                     |
| [**CryptSignMessageWithKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptsignmessagewithkey?branch=master)                             | Signs a message using a CSP's private key specified in the parameters to the function.                                                                                                                                                                                       |
| [**CryptSignMessage**](/windows/win32/Wincrypt/nf-wincrypt-cryptsignmessage?branch=master)                                           | Signs the message.                                                                                                                                                                                                                                                           |
| [**CryptVerifyDetachedMessageHash**](/windows/win32/Wincrypt/nf-wincrypt-cryptverifydetachedmessagehash?branch=master)               | Verifies a hashed message that contains a detached hash.                                                                                                                                                                                                                     |
| [**CryptVerifyDetachedMessageSignature**](/windows/win32/Wincrypt/nf-wincrypt-cryptverifydetachedmessagesignature?branch=master)     | Verifies a signed message that contains a detached signature or signatures.                                                                                                                                                                                                  |
| [**CryptVerifyMessageHash**](/windows/win32/Wincrypt/nf-wincrypt-cryptverifymessagehash?branch=master)                               | Verifies a hashed message.                                                                                                                                                                                                                                                   |
| [**CryptVerifyMessageSignature**](/windows/win32/Wincrypt/nf-wincrypt-cryptverifymessagesignature?branch=master)                     | Verifies a signed message.                                                                                                                                                                                                                                                   |
| [**CryptVerifyMessageSignatureWithKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptverifymessagesignaturewithkey?branch=master)       | Verifies a signed message's signature by using specified public key information.                                                                                                                                                                                             |



 

## Auxiliary Functions

The auxiliary functions are grouped as follows:

-   Data Management Functions
-   Data Conversion Functions
-   Enhanced Key Usage Functions
-   Key Identifier Functions
-   OID Support Functions
-   Remote Object Retrieval Functions
-   PFX Functions

### Data Management Functions

The following CryptoAPI functions manage data and certificates.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>CertCompareCertificate</strong>](/windows/win32/Wincrypt/nf-wincrypt-certcomparecertificate?branch=master)</td>
<td>Compares two certificates to determine whether they are identical.</td>
</tr>
<tr class="even">
<td>[<strong>CertCompareCertificateName</strong>](/windows/win32/Wincrypt/nf-wincrypt-certcomparecertificatename?branch=master)</td>
<td>Compares two certificate names to determine whether they are identical.</td>
</tr>
<tr class="odd">
<td>[<strong>CertCompareIntegerBlob</strong>](/windows/win32/Wincrypt/nf-wincrypt-certcompareintegerblob?branch=master)</td>
<td>Compares two integer [<em>BLOBs</em>](security.b_gly#-security-blob-gly).</td>
</tr>
<tr class="even">
<td>[<strong>CertComparePublicKeyInfo</strong>](/windows/win32/Wincrypt/nf-wincrypt-certcomparepublickeyinfo?branch=master)</td>
<td>Compares two [<em>public keys</em>](security.p_gly#-security-public-key-gly) to determine whether they are identical.</td>
</tr>
<tr class="odd">
<td>[<strong>CertFindAttribute</strong>](/windows/win32/Wincrypt/nf-wincrypt-certfindattribute?branch=master)</td>
<td>Finds the first attribute identified by its [<em>object identifier</em>](security.o_gly#-security-object-identifier-gly) (OID).</td>
</tr>
<tr class="even">
<td>[<strong>CertFindExtension</strong>](/windows/win32/Wincrypt/nf-wincrypt-certfindextension?branch=master)</td>
<td>Finds the first extension identified by its OID.</td>
</tr>
<tr class="odd">
<td>[<strong>CertFindRDNAttr</strong>](/windows/win32/Wincrypt/nf-wincrypt-certfindrdnattr?branch=master)</td>
<td>Finds the first [<em>RDN</em>](security.r_gly#-security-relative-distinguished-name-gly) attribute identified by its OID in the name list of the <em>Relative Distinguished Names</em>.</td>
</tr>
<tr class="even">
<td>[<strong>CertGetIntendedKeyUsage</strong>](/windows/win32/Wincrypt/nf-wincrypt-certgetintendedkeyusage?branch=master)</td>
<td>Acquires the intended key usage bytes from the certificate.</td>
</tr>
<tr class="odd">
<td>[<strong>CertGetPublicKeyLength</strong>](/windows/win32/Wincrypt/nf-wincrypt-certgetpublickeylength?branch=master)</td>
<td>Acquires the public/private key's bit length from the [<em>public key BLOB</em>](security.p_gly#-security-public-key-blob-gly).</td>
</tr>
<tr class="even">
<td>[<strong>CertIsRDNAttrsInCertificateName</strong>](/windows/win32/Wincrypt/nf-wincrypt-certisrdnattrsincertificatename?branch=master)</td>
<td>Compares the attributes in the [<em>certificate name</em>](security.c_gly#-security-certificate-name-blob-gly) with the specified [<strong>CERT_RDN</strong>](/windows/win32/Wincrypt/ns-wincrypt-_cert_rdn?branch=master) to determine whether all attributes are included there.</td>
</tr>
<tr class="odd">
<td>[<strong>CertIsStrongHashToSign</strong>](/windows/win32/Wincrypt/nf-wincrypt-certisstronghashtosign?branch=master)</td>
<td>Determines whether the specified hash algorithm and the public key in the signing certificate can be used to perform strong signing.</td>
</tr>
<tr class="even">
<td>[<strong>CertVerifyCRLRevocation</strong>](/windows/win32/Wincrypt/nf-wincrypt-certverifycrlrevocation?branch=master)</td>
<td>Verifies that the subject certificate is not on the [<em>certificate revocation list</em>](security.c_gly#-security-certificate-revocation-list-gly) (CRL).</td>
</tr>
<tr class="odd">
<td>[<strong>CertVerifyCRLTimeValidity</strong>](/windows/win32/Wincrypt/nf-wincrypt-certverifycrltimevalidity?branch=master)</td>
<td>Verifies the time validity of a CRL.</td>
</tr>
<tr class="even">
<td>[<strong>CertVerifyRevocation</strong>](/windows/win32/Wincrypt/nf-wincrypt-certverifyrevocation?branch=master)</td>
<td>Verifies that the subject certificate is not on the CRL.</td>
</tr>
<tr class="odd">
<td>[<strong>CertVerifyTimeValidity</strong>](/windows/win32/Wincrypt/nf-wincrypt-certverifytimevalidity?branch=master)</td>
<td>Verifies the time validity of a certificate.</td>
</tr>
<tr class="even">
<td>[<strong>CertVerifyValidityNesting</strong>](/windows/win32/Wincrypt/nf-wincrypt-certverifyvaliditynesting?branch=master)</td>
<td>Verifies that the subject's time validity nests within the issuer's time validity.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptExportPKCS8</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptexportpkcs8?branch=master)</td>
<td>This function is superseded by the [<strong>CryptExportPKCS8Ex</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptexportpkcs8ex?branch=master) function.</td>
</tr>
<tr class="even">
<td>[<strong>CryptExportPKCS8Ex</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptexportpkcs8ex?branch=master)</td>
<td>Exports the private key in PKCS #8 format.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptExportPublicKeyInfo</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptexportpublickeyinfo?branch=master)</td>
<td>Exports the public key information associated with the provider's corresponding private key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptExportPublicKeyInfoEx</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptexportpublickeyinfoex?branch=master)</td>
<td>Exports the public key information associated with the provider's corresponding private key. This function differs from [<strong>CryptExportPublicKeyInfo</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptexportpublickeyinfo?branch=master) in that the user can specify the public key algorithm, thereby overriding the default provided by the CSP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptExportPublicKeyInfoFromBCryptKeyHandle</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptexportpublickeyinfofrombcryptkeyhandle?branch=master)</td>
<td>Exports the public key info associated with a provider's corresponding private key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptFindCertificateKeyProvInfo</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptfindcertificatekeyprovinfo?branch=master)</td>
<td>Enumerates the cryptographic providers and their [<em>key containers</em>](security.k_gly#-security-key-container-gly) to find the private key that corresponds to a certificate's public key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptFindLocalizedName</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptfindlocalizedname?branch=master)</td>
<td>Finds the localized name for a specified name, for example, finds the localized name for the store name of the Root system.</td>
</tr>
<tr class="even">
<td>[<strong>CryptHashCertificate</strong>](/windows/win32/Wincrypt/nf-wincrypt-crypthashcertificate?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes the encoded content.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptHashCertificate2</strong>](/windows/win32/Wincrypt/nf-wincrypt-crypthashcertificate2?branch=master)</td>
<td>Hashes a block of data by using a Cryptography API: Next Generation (CNG) hash provider.</td>
</tr>
<tr class="even">
<td>[<strong>CryptHashPublicKeyInfo</strong>](/windows/win32/Wincrypt/nf-wincrypt-crypthashpublickeyinfo?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Computes the hash of the encoded public key information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptHashToBeSigned</strong>](/windows/win32/Wincrypt/nf-wincrypt-crypthashtobesigned?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Computes the hash of the &quot;to be signed&quot; information in the encoded signed content ([<strong>CERT_SIGNED_CONTENT_INFO</strong>](/windows/win32/Wincrypt/ns-wincrypt-_cert_signed_content_info?branch=master)).</td>
</tr>
<tr class="even">
<td>[<strong>CryptImportPKCS8</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptimportpkcs8?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Imports the [<em>private key</em>](security.p_gly#-security-private-key-gly) in PKCS #8 format to a [<em>cryptographic service provider</em>](security.c_gly#-security-cryptographic-service-provider-gly) (CSP).</td>
</tr>
<tr class="odd">
<td>[<strong>CryptImportPublicKeyInfo</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptimportpublickeyinfo?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Converts and imports public key information into the provider, and returns a handle of the public key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptImportPublicKeyInfoEx</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptimportpublickeyinfoex?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Converts and imports the public key information into the provider, and returns a handle of the public key. Additional parameters (over those specified by [<strong>CryptImportPublicKeyInfo</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptimportpublickeyinfo?branch=master)) that can be used to override defaults are provided to supplement [<strong>CERT_PUBLIC_KEY_INFO</strong>](/windows/win32/Wincrypt/ns-wincrypt-_cert_public_key_info?branch=master).</td>
</tr>
<tr class="odd">
<td>[<strong>CryptImportPublicKeyInfoEx2</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptimportpublickeyinfoex2?branch=master)</td>
<td>Imports a public key into a CNG asymmetric provider.</td>
</tr>
<tr class="even">
<td>[<strong>CryptMemAlloc</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptmemalloc?branch=master)</td>
<td>Allocates memory for a buffer. This memory is used by all Crypt32.lib functions that return allocated buffers.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptMemFree</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptmemfree?branch=master)</td>
<td>Frees memory allocated by [<strong>CryptMemAlloc</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptmemalloc?branch=master) or [<strong>CryptMemRealloc</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptmemrealloc?branch=master).</td>
</tr>
<tr class="even">
<td>[<strong>CryptMemRealloc</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptmemrealloc?branch=master)</td>
<td>Frees memory currently allocated for a buffer, and allocates memory for a new buffer.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptQueryObject</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptqueryobject?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves information about the content of a BLOB or a file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSignAndEncodeCertificate</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptsignandencodecertificate?branch=master)</td>
<td>Encodes the &quot;to be signed&quot; information, signs this encoded information, and encodes the resulting signed, encoded information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSignCertificate</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptsigncertificate?branch=master)</td>
<td>Signs the &quot;to be signed&quot; information in the encoded, signed content.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPAddProvider</strong>](/windows/win32/Mssip/nf-mssip-cryptsipaddprovider?branch=master)</td>
<td>Adds a Subject Interface Package (SIP).</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPCreateIndirectData</strong>](/windows/win32/Mssip/nf-mssip-cryptsipcreateindirectdata?branch=master)</td>
<td>Returns a [<strong>SIP_INDIRECT_DATA</strong>](/windows/win32/Mssip/ns-mssip-sip_indirect_data_?branch=master) structure that contains a [<em>hash</em>](security.h_gly#-security-hash-gly) of the supplied [<strong>SIP_SUBJECTINFO</strong>](/windows/win32/Mssip/ns-mssip-sip_subjectinfo_?branch=master) structure, the digest algorithm, and an encoding attribute. The hash can be used as an indirect reference to the data.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPGetCaps</strong>](/windows/win32/Mssip/nf-mssip-cryptsipgetcaps?branch=master)</td>
<td>Retrieves the capabilities of an SIP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPGetSignedDataMsg</strong>](/windows/win32/Mssip/nf-mssip-cryptsipgetsigneddatamsg?branch=master)</td>
<td>Retrieves an Authenticode signature from the file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPLoad</strong>](/windows/win32/Mssip/nf-mssip-cryptsipload?branch=master)</td>
<td>Loads the dynamic link library that implements a subject interface package and assigns appropriate library export functions to a [<strong>SIP_DISPATCH_INFO</strong>](/windows/win32/Mssip/ns-mssip-sip_dispatch_info_?branch=master) structure.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPPutSignedDataMsg</strong>](/windows/win32/Mssip/nf-mssip-cryptsipputsigneddatamsg?branch=master)</td>
<td>Stores an Authenticode Signature in the target file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPRemoveProvider</strong>](/windows/win32/Mssip/nf-mssip-cryptsipremoveprovider?branch=master)</td>
<td>Removes a SIP added by a previous call to the [<strong>CryptSIPAddProvider</strong>](/windows/win32/Mssip/nf-mssip-cryptsipaddprovider?branch=master) function.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPRemoveSignedDataMsg</strong>](/windows/win32/Mssip/nf-mssip-cryptsipremovesigneddatamsg?branch=master)</td>
<td>Removes a specified Authenticode signature.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPRetrieveSubjectGuid</strong>](/windows/win32/Mssip/nf-mssip-cryptsipretrievesubjectguid?branch=master)</td>
<td>Retrieves a GUID based on the header information in a specified file.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPRetrieveSubjectGuidForCatalogFile</strong>](/windows/win32/Mssip/nf-mssip-cryptsipretrievesubjectguidforcatalogfile?branch=master)</td>
<td>Retrieves the subject GUID associated with the specified file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPVerifyIndirectData</strong>](/windows/win32/Mssip/nf-mssip-cryptsipverifyindirectdata?branch=master)</td>
<td>Validates the indirect hashed data against the supplied subject.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUpdateProtectedState</strong>](/windows/win32/Dpapi/nf-dpapi-cryptupdateprotectedstate?branch=master)</td>
<td>Migrates the current user's master keys after the user's [<em>security identifier</em>](security.s_gly#-security-security-identifier-gly) (SID) has changed.</td>
</tr>
<tr class="even">
<td>[<strong>CryptVerifyCertificateSignature</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptverifycertificatesignature?branch=master)</td>
<td>Verifies the signature of a subject certificate or a [<em>CRL</em>](security.c_gly#-security-certificate-revocation-list-gly) by using the public key information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptVerifyCertificateSignatureEx</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptverifycertificatesignatureex?branch=master)</td>
<td>An extended version of [<strong>CryptVerifyCertificateSignature</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptverifycertificatesignature?branch=master).</td>
</tr>
<tr class="even">
<td>[<strong>GetEncSChannel</strong>](/windows/win32/Wincrypt/nf-wincrypt-getencschannel?branch=master)</td>
<td>Stores the encrypted Schannel DLL contents in memory.</td>
</tr>
<tr class="odd">
<td>[<strong>pCryptSIPGetCaps</strong>](/windows/win32/Mssip/nc-mssip-pcryptsipgetcaps?branch=master)</td>
<td>Implemented by an SIP to report capabilities.</td>
</tr>
</tbody>
</table>



 

### Data Conversion Functions

The following CryptoAPI functions convert certificate structure members to different forms.

| Function                                           | Description                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAlgIdToOID**](/windows/win32/Wincrypt/nf-wincrypt-certalgidtooid?branch=master)           | Converts a CryptoAPI algorithm identifier (ALG\_ID) to an [*Abstract Syntax Notation One*](security.a_gly#-security-abstract-syntax-notation-one-gly) (ASN.1) [*object identifier*](security.o_gly#-security-object-identifier-gly) (OID) string. |
| [**CertGetNameString**](/windows/win32/Wincrypt/nf-wincrypt-certgetnamestringa?branch=master)     | Acquires the subject or issuer name from a certificate, and converts it to a null-terminated character string.                                                                                                                                                                                                               |
| [**CertNameToStr**](/windows/win32/Wincrypt/nf-wincrypt-certnametostra?branch=master)             | Converts a certificate name [*BLOB*](security.b_gly#-security-blob-gly) to a zero-terminated string.                                                                                                                                                                                                      |
| [**CertOIDToAlgId**](/windows/win32/Wincrypt/nf-wincrypt-certoidtoalgid?branch=master)           | Converts the ASN.1 Object Identifier string to the CSP algorithm identifier.                                                                                                                                                                                                                                                 |
| [**CertRDNValueToStr**](/windows/win32/Wincrypt/nf-wincrypt-certrdnvaluetostra?branch=master)     | Converts a Name Value to a null-terminated string.                                                                                                                                                                                                                                                                           |
| [**CertStrToName**](/windows/win32/Wincrypt/nf-wincrypt-certstrtonamea?branch=master)             | Converts a null-terminated [*X.500*](security.x_gly#-security-x-500-gly) string to an encoded certificate name.                                                                                                                                                                                          |
| [**CryptBinaryToString**](/windows/win32/Wincrypt/nf-wincrypt-cryptbinarytostringa?branch=master) | Converts a binary sequence into a formatted string.                                                                                                                                                                                                                                                                          |
| [**CryptFormatObject**](/windows/win32/Wincrypt/nf-wincrypt-cryptformatobject?branch=master)     | Formats encoded data, and returns a Unicode string.                                                                                                                                                                                                                                                                          |
| [**CryptStringToBinary**](/windows/win32/Wincrypt/nf-wincrypt-cryptstringtobinarya?branch=master) | Converts a formatted string to a binary sequence.                                                                                                                                                                                                                                                                            |



 

### Enhanced Key Usage Functions

The following functions deal with the [*enhanced key usage*](security.e_gly#-security-enhanced-key-usage-gly) (EKU) extension and the EKU extended property of certificates. The EKU extension and extended property specify and limit the valid uses of a certificate. The extensions are part of the certificate itself. They are set by the issuer of the certificate and are read-only. Certificate-extended properties are values associated with a certificate that can be set in an application.

| Function                                                                             | Description                                                                    |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**CertAddEnhancedKeyUsageIdentifier**](/windows/win32/Wincrypt/nf-wincrypt-certaddenhancedkeyusageidentifier?branch=master)       | Adds a usage identifier to a certificate's EKU property.                       |
| [**CertGetEnhancedKeyUsage**](/windows/win32/Wincrypt/nf-wincrypt-certgetenhancedkeyusage?branch=master)                           | Acquires, from a certificate, information about the EKU extension or property. |
| [**CertRemoveEnhancedKeyUsageIdentifier**](/windows/win32/Wincrypt/nf-wincrypt-certremoveenhancedkeyusageidentifier?branch=master) | Removes the usage identifier from a certificate's EKU extended property.       |
| [**CertSetEnhancedKeyUsage**](/windows/win32/Wincrypt/nf-wincrypt-certsetenhancedkeyusage?branch=master)                           | Sets the EKU property for a certificate.                                       |



 

### Key Identifier Functions

Key identifier functions allow the user to create, set, retrieve, or locate a key identifier or its properties.

A key identifier is the unique identifier of a [*public/private key pair*](security.p_gly#-security-public-private-key-pair-gly). It can be any unique identifier but is usually the 20-byte SHA1 hash of an encoded [**CERT\_PUBLIC\_KEY\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_cert_public_key_info?branch=master) structure. A key identifier can be obtained through the certificate's CERT\_KEY\_IDENTIFIER\_PROP\_ID. The key identifier allows the use of that [*key pair*](security.k_gly#-security-key-pair-gly) to encrypt or decrypt messages without using the certificate.

Key identifiers are not associated with [*CRLs*](security.c_gly#-security-certificate-revocation-list-gly) or [*CTLs*](security.c_gly#-security-certificate-trust-list-gly).

A key identifier can have the same properties as a certificate context. For more information, see [**CertCreateContext**](/windows/win32/Wincrypt/nf-wincrypt-certcreatecontext?branch=master).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>CryptCreateKeyIdentifierFromCSP</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptcreatekeyidentifierfromcsp?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a key identifier from a CSP's [<em>public key BLOB</em>](security.p_gly#-security-public-key-blob-gly).</td>
</tr>
<tr class="even">
<td>[<strong>CryptEnumKeyIdentifierProperties</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptenumkeyidentifierproperties?branch=master)</td>
<td>Enumerates key identifiers and their properties.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGetKeyIdentifierProperty</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptgetkeyidentifierproperty?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Acquires a specific property from a specified key identifier.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSetKeyIdentifierProperty</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptsetkeyidentifierproperty?branch=master)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Sets a property of a specified key identifier.</td>
</tr>
</tbody>
</table>



 

### OID Support Functions

These functions provide [*object identifier*](security.o_gly#-security-object-identifier-gly) (OID) support. These functions install, register, and dispatch to OID and encoding type-specific functions.

The following CryptoAPI functions use these OID support functions:

-   [**CryptEncodeObject**](/windows/win32/Wincrypt/nf-wincrypt-cryptencodeobject?branch=master)
-   [**CryptEncodeObjectEx**](/windows/win32/Wincrypt/nf-wincrypt-cryptencodeobjectex?branch=master)
-   [**CryptDecodeObject**](/windows/win32/Wincrypt/nf-wincrypt-cryptdecodeobject?branch=master)
-   [**CryptDecodeObjectEx**](/windows/win32/Wincrypt/nf-wincrypt-cryptdecodeobjectex?branch=master)
-   [**CertVerifyRevocation**](/windows/win32/Wincrypt/nf-wincrypt-certverifyrevocation?branch=master)
-   [**CertOpenStore**](/windows/win32/Wincrypt/nf-wincrypt-certopenstore?branch=master)

For an overview of this process, see [Extending CryptoAPI Functionality](extending-cryptoapi-functionality.md).

The following functions work with OIDs.

| Function                                                                       | Description                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptEnumOIDFunction**](/windows/win32/Wincrypt/nf-wincrypt-cryptenumoidfunction?branch=master)                           | Enumerates the registered OID functions identified by their encoding type, function name, and OID.                                                                                                                 |
| [**CryptEnumOIDInfo**](/windows/win32/Wincrypt/nf-wincrypt-cryptenumoidinfo?branch=master)                                   | Enumerates the registered OID information identified by their group, and calls *pfnEnumOIDInfo* for matches.                                                                                                       |
| [**CryptFindOIDInfo**](/windows/win32/Wincrypt/nf-wincrypt-cryptfindoidinfo?branch=master)                                   | Uses the specified key and group to find OID information.                                                                                                                                                          |
| [**CryptFreeOIDFunctionAddress**](/windows/win32/Wincrypt/nf-wincrypt-cryptfreeoidfunctionaddress?branch=master)             | Releases the handle count that was incremented and returned by [**CryptGetOIDFunctionAddress**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetoidfunctionaddress?branch=master) or [**CryptGetDefaultOIDFunctionAddress**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetdefaultoidfunctionaddress?branch=master). |
| [**CryptGetDefaultOIDDllList**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetdefaultoiddlllist?branch=master)                 | Acquires the list of registered default DLL entries for the specified function set and encoding type.                                                                                                              |
| [**CryptGetDefaultOIDFunctionAddress**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetdefaultoidfunctionaddress?branch=master) | Either acquires the first or next installed default function, or loads the DLL that contains the default function.                                                                                                 |
| [**CryptGetOIDFunctionAddress**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetoidfunctionaddress?branch=master)               | Searches the list of installed functions for an encoding type and OID match. If a match is not found there, the registry is searched for a match.                                                                  |
| [**CryptGetOIDFunctionValue**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetoidfunctionvalue?branch=master)                   | Acquires the value for the specified encoding type, function name, OID, and value name.                                                                                                                            |
| [**CryptInitOIDFunctionSet**](/windows/win32/Wincrypt/nf-wincrypt-cryptinitoidfunctionset?branch=master)                     | Initializes and returns a handle of the OID function set identified by the function name supplied.                                                                                                                 |
| [**CryptInstallOIDFunctionAddress**](/windows/win32/Wincrypt/nf-wincrypt-cryptinstalloidfunctionaddress?branch=master)       | Installs a set of callable OID function addresses.                                                                                                                                                                 |
| [**CryptRegisterDefaultOIDFunction**](/windows/win32/Wincrypt/nf-wincrypt-cryptregisterdefaultoidfunction?branch=master)     | Registers the DLL that contains the default function to be called for the specified encoding type and function name.                                                                                               |
| [**CryptRegisterOIDFunction**](/windows/win32/Wincrypt/nf-wincrypt-cryptregisteroidfunction?branch=master)                   | Registers the DLL that contains the function to be called for the specified encoding type, function name, and OID.                                                                                                 |
| [**CryptRegisterOIDInfo**](/windows/win32/Wincrypt/nf-wincrypt-cryptregisteroidinfo?branch=master)                           | Registers the OID information specified in the [**CRYPT\_OID\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_crypt_oid_info?branch=master) structure, persisting it to the registry.                                                                                |
| [**CryptSetOIDFunctionValue**](/windows/win32/Wincrypt/nf-wincrypt-cryptsetoidfunctionvalue?branch=master)                   | Sets the value for the specified encoding type, function name, OID, and value name.                                                                                                                                |
| [**CryptUnregisterDefaultOIDFunction**](/windows/win32/Wincrypt/nf-wincrypt-cryptunregisterdefaultoidfunction?branch=master) | Removes the registration for the DLL that contains the default function to be called for the specified encoding type and function name.                                                                            |
| [**CryptUnregisterOIDFunction**](/windows/win32/Wincrypt/nf-wincrypt-cryptunregisteroidfunction?branch=master)               | Removes the registration for the DLL that contains the function to be called for the specified encoding type, function name, and OID.                                                                              |
| [**CryptUnregisterOIDInfo**](/windows/win32/Wincrypt/nf-wincrypt-cryptunregisteroidinfo?branch=master)                       | Removes the registration for the specified OID information.                                                                                                                                                        |



 

### Remote Object Retrieval Functions

The following functions allow the user to retrieve a Public Key Infrastructure (PKI) object, acquire the URL of a certificate, CTL, or CRL, or to extract a URL from an object.

| Function                                                     | Description                                                            |
|--------------------------------------------------------------|------------------------------------------------------------------------|
| [**CryptGetObjectUrl**](/windows/win32/Wincrypt/nf-wincrypt-cryptgetobjecturl?branch=master)               | Acquires the URL of the remote object from a certificate, CTL, or CRL. |
| [**CryptRetrieveObjectByUrl**](/windows/win32/Wincrypt/nf-wincrypt-cryptretrieveobjectbyurla?branch=master) | Retrieves the PKI object from a location specified by a URL.           |



 

### PFX Functions

The following functions support Personal Information Exchange (PFX) format [*BLOBs*](security.b_gly#-security-blob-gly).

| Function                                             | Description                                                                                                                                                                                                                                                                  |
|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PFXExportCertStore**](/windows/win32/Wincrypt/nf-wincrypt-pfxexportcertstore?branch=master)     | Exports from the referenced [*certificate store*](security.c_gly#-security-certificate-store-gly) the certificates and, if available, their associated [*private keys*](security.p_gly#-security-private-key-gly). |
| [**PFXExportCertStoreEx**](/windows/win32/Wincrypt/nf-wincrypt-pfxexportcertstoreex?branch=master) | Exports from the referenced certificate store the certificates and, if available, their associated private keys.                                                                                                                                                             |
| [**PFXImportCertStore**](/windows/win32/Wincrypt/nf-wincrypt-pfximportcertstore?branch=master)     | Imports a PFX BLOB, and returns the handle of a store that contains certificates and any associated private keys.                                                                                                                                                            |
| [**PFXIsPFXBlob**](/windows/win32/Wincrypt/nf-wincrypt-pfxispfxblob?branch=master)                 | Attempts to decode the outer layer of a BLOB as a PFX packet.                                                                                                                                                                                                                |
| [**PFXVerifyPassword**](/windows/win32/Wincrypt/nf-wincrypt-pfxverifypassword?branch=master)       | Attempts to decode the outer layer of a BLOB as a PFX packet and to decrypt it with the given password.                                                                                                                                                                      |



 

## Certificate Services Backup and Restore Functions

Certificate Services includes functions for backing up and restoring the Certificate Services database. These Certificate Services backup and restore functions are contained in Certadm.dll. Unlike the other API elements associated with Certificate Services, these functions are not encapsulated in an object that can be used to call class methods. Instead, the backup and restore APIs are called by first loading the Certadm.dll library into memory by calling [**LoadLibrary**](base.loadlibrary) and then determining the address of the functions by calling [**GetProcAddress**](base.getprocaddress). When you have finished calling the Certificate Services backup and restore functions, call [**FreeLibrary**](base.freelibrary) to free Certadm.dll resources from memory.

> [!Note]Backup and restore functions provided by Certadm.dll do not backup or restore the Certificate Service's [*private keys*](security.p_gly#-security-private-key-gly). For information about backing up the Certificate Services private keys, see [Backing Up and Restoring the Certificate Services Private Key](backing-up-and-restoring-the-certificate-services-private-key.md).
>
> To call the backup and restore functions, you must have backup and restore [*privileges*](security.p_gly#-security-privilege-gly). For details, see [Setting the Backup and Restore Privileges](setting-the-backup-and-restore-privileges.md).

 

> [!Note]  
> If **CoInitializeEx** was previously called in the same thread used to call the Certificate Services backup and restore APIs, the COINIT\_APARTMENTTHREADED flag must have been passed to **CoInitializeEx**. That is, when using the same thread, you cannot call the Certificate Services backup and restore API if the thread has previously passed in the COINIT\_MULTITHREADED flag in a call to **CoInitializeEx**.

 

The Certificate Services Backup APIs are defined in Certbcli.h. However, when you create your program, use Certsrv.h as the include file.

The following APIs are exported by Certadm.dll.

| Function                                                                         | Description                                                                                                           |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**CertSrvBackupClose**](/windows/win32/Certbcli/nf-certbcli-certsrvbackupclose?branch=master)                                 | Closes an opened file.                                                                                                |
| [**CertSrvBackupEnd**](/windows/win32/Certbcli/nf-certbcli-certsrvbackupend?branch=master)                                     | Ends a backup session.                                                                                                |
| [**CertSrvBackupFree**](/windows/win32/Certbcli/nf-certbcli-certsrvbackupfree?branch=master)                                   | Frees a buffer allocated by the backup and restore APIs.                                                              |
| [**CertSrvBackupGetBackupLogs**](/windows/win32/Certbcli/nf-certbcli-certsrvbackupgetbackuplogsw?branch=master)                 | Returns a list of log files that need to be backed up.                                                                |
| [**CertSrvBackupGetDatabaseNames**](/windows/win32/Certbcli/nf-certbcli-certsrvbackupgetdatabasenamesw?branch=master)           | Returns a list of database files that need to be backed up.                                                           |
| [**CertSrvBackupGetDynamicFileList**](/windows/win32/Certbcli/nf-certbcli-certsrvbackupgetdynamicfilelistw?branch=master)       | Retrieves the list of Certificate Services dynamic file names that need to be backed up for the given backup context. |
| [**CertSrvBackupOpenFile**](/windows/win32/Certbcli/nf-certbcli-certsrvbackupopenfilew?branch=master)                           | Opens a file in preparation for backing it up.                                                                        |
| [**CertSrvBackupPrepare**](/windows/win32/Certbcli/nf-certbcli-certsrvbackuppreparew?branch=master)                             | Prepares the database for the online backup.                                                                          |
| [**CertSrvBackupRead**](/windows/win32/Certbcli/nf-certbcli-certsrvbackupread?branch=master)                                   | Reads the contents of an opened file.                                                                                 |
| [**CertSrvBackupTruncateLogs**](/windows/win32/Certbcli/nf-certbcli-certsrvbackuptruncatelogs?branch=master)                   | Truncates the log files.                                                                                              |
| [**CertSrvIsServerOnline**](/windows/win32/Certbcli/nf-certbcli-certsrvisserveronlinew?branch=master)                           | Determines whether a Certificate Services server is online (actively running).                                        |
| [**CertSrvRestoreEnd**](/windows/win32/Certbcli/nf-certbcli-certsrvrestoreend?branch=master)                                   | Ends a restore session.                                                                                               |
| [**CertSrvRestoreGetDatabaseLocations**](/windows/win32/Certbcli/nf-certbcli-certsrvrestoregetdatabaselocationsw?branch=master) | Retrieves database locations (used for both backup and restore scenarios).                                            |
| [**CertSrvRestorePrepare**](/windows/win32/Certbcli/nf-certbcli-certsrvrestorepreparew?branch=master)                           | Begins a restore session.                                                                                             |
| [**CertSrvRestoreRegister**](/windows/win32/Certbcli/nf-certbcli-certsrvrestoreregisterw?branch=master)                         | Registers a restore operation.                                                                                        |
| [**CertSrvRestoreRegisterComplete**](/windows/win32/Certbcli/nf-certbcli-certsrvrestoreregistercomplete?branch=master)         | Completes a previously registered restore operation.                                                                  |
| [**CertSrvRestoreRegisterThroughFile**](/windows/win32/Certbcli/nf-certbcli-certsrvrestoreregisterthroughfile?branch=master)   | Registers a restore operation.                                                                                        |
| [**CertSrvServerControl**](/windows/win32/Certbcli/nf-certbcli-certsrvservercontrolw?branch=master)                             | Sends a control command to the Certificate Services instance.                                                         |



 

## Callback Functions

The callback functions in this section are used to register or install application-defined [*certificate store*](security.c_gly#-security-certificate-store-gly) providers and to provide related functionality through callback functions. Callback functions are implemented by an application and are called by [*CryptoAPI*](security.c_gly#-security-cryptoapi-gly) functions. Callback functions enable the application to control, in part, the way that CryptoAPI functions manipulate data.

| Callback function                                                                                                        | Use                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertChainFindByIssuerCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_chain_find_by_issuer_callback?branch=master)                                                   | An application-defined callback function that allows the application to filter certificates that might be added to the certificate chain.                                                                                                                                                                                                     |
| [**CertDllOpenStoreProv**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_dll_open_store_prov_func?branch=master)                                                                     | Defines the store provider open function.                                                                                                                                                                                                                                                                                                     |
| [**CertEnumPhysicalStoreCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_enum_physical_store?branch=master)                                                   | Callback function used by the [**CertEnumPhysicalStore**](/windows/win32/Wincrypt/nf-wincrypt-certenumphysicalstore?branch=master) function to format and present information on each physical store found.                                                                                                                                                                                 |
| [**CertEnumSystemStoreCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_enum_system_store?branch=master)                                                       | Callback function used by the [**CertEnumSystemStore**](/windows/win32/Wincrypt/nf-wincrypt-certenumsystemstore?branch=master) function to format and present information on each physical store found.                                                                                                                                                                                     |
| [**CertEnumSystemStoreLocationCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_enum_system_store_location?branch=master)                                       | Callback function used by the [**CertEnumSystemStoreLocation**](/windows/win32/Wincrypt/nf-wincrypt-certenumsystemstorelocation?branch=master) function to format and present information on each physical store found.                                                                                                                                                                     |
| [**CertStoreProvCloseCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_close?branch=master)                                                         | Determines what happens when an open store's [*reference count*](security.r_gly#-security-reference-count-gly) becomes zero.                                                                                                                                                                                    |
| [**CertStoreProvControl**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_control?branch=master)                                                                     | Allows an application to be notified when there is a difference between the contents of a cached store in use and the contents of that store as it is persisted to storage.                                                                                                                                                                   |
| [**CertStoreProvDeleteCertCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_delete_cert?branch=master)                                               | Determines actions to be taken before a certificate is deleted from a certificate store.                                                                                                                                                                                                                                                      |
| [**CertStoreProvDeleteCRLCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_delete_crl?branch=master)                                                 | Determines actions to be taken before a [*certificate revocation list*](security.c_gly#-security-certificate-revocation-list-gly) (CRL) is deleted from a certificate store.                                                                                                                        |
| [**CertStoreProvDeleteCTL**](certstoreprovdeletectl.md)                                                                 | Determines whether a CTL can be deleted.                                                                                                                                                                                                                                                                                                      |
| [**CertStoreProvFindCert**](certstoreprovfindcert.md)                                                                   | Finds the first, or next, certificate in a store that matches specified criteria.                                                                                                                                                                                                                                                             |
| [**CertStoreProvFindCRL**](certstoreprovfindcrl.md)                                                                     | Finds the first, or next, CRL in a store that matches specified criteria.                                                                                                                                                                                                                                                                     |
| [**CertStoreProvFindCTL**](certstoreprovfindctl.md)                                                                     | Finds the first, or next, CTL in a store that matches specified criteria.                                                                                                                                                                                                                                                                     |
| [**CertStoreProvFreeFindCert**](certstoreprovfreefindcert.md)                                                           | Frees a previously found certificate context.                                                                                                                                                                                                                                                                                                 |
| [**CertStoreProvFreeFindCRL**](certstoreprovfreefindcrl.md)                                                             | Frees a previously found CRL context.                                                                                                                                                                                                                                                                                                         |
| [**CertStoreProvFreeFindCTL**](certstoreprovfreefindctl.md)                                                             | Frees a previously found CTL context.                                                                                                                                                                                                                                                                                                         |
| [**CertStoreProvGetCertProperty**](certstoreprovgetcertproperty.md)                                                     | Retrieves a specified property of a certificate.                                                                                                                                                                                                                                                                                              |
| [**CertStoreProvGetCRLProperty**](certstoreprovgetcrlproperty.md)                                                       | Retrieves a specified property of a CRL.                                                                                                                                                                                                                                                                                                      |
| [**CertStoreProvGetCTLProperty**](certstoreprovgetctlproperty.md)                                                       | Retrieves a specified property of a CTL.                                                                                                                                                                                                                                                                                                      |
| [**CertStoreProvReadCertCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_read_cert?branch=master)                                                   | Currently not used but might be exported to future CSPs.                                                                                                                                                                                                                                                                                      |
| [**CertStoreProvReadCRLCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_read_crl?branch=master)                                                     | Currently not used but might be exported to future CSPs.                                                                                                                                                                                                                                                                                      |
| [**CertStoreProvReadCTL**](/windows/win32/Wincrypt/?branch=master)                                                                     | Read the provider's copy of the CTL context, and, if it exists, create a new CTL context.                                                                                                                                                                                                                                                     |
| [**CertStoreProvSetCertPropertyCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_set_cert_property?branch=master)                                     | Determines actions to be taken before a call to [**CertSetCertificateContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certsetcertificatecontextproperty?branch=master) or [**CertGetCertificateContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty?branch=master).                                                                                                                             |
| [**CertStoreProvSetCRLPropertyCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_set_crl_property?branch=master)                                       | Determines actions to be taken before a call to [**CertSetCRLContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certsetcrlcontextproperty?branch=master) or [**CertGetCRLContextProperty**](/windows/win32/Wincrypt/nf-wincrypt-certgetcrlcontextproperty?branch=master).                                                                                                                                                             |
| [**CertStoreProvSetCTLProperty**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_set_ctl_property?branch=master)                                                       | Determines whether a property can be set on a CTL.                                                                                                                                                                                                                                                                                            |
| [**CertStoreProvWriteCertCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_write_cert?branch=master)                                                 | Determines actions to be taken before adding a certificate to a store.                                                                                                                                                                                                                                                                        |
| [**CertStoreProvWriteCRLCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_write_crl?branch=master)                                                   | Determines actions to be taken before adding a CRL to a store.                                                                                                                                                                                                                                                                                |
| [**CertStoreProvWriteCTL**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_store_prov_write_ctl?branch=master)                                                                   | Determines whether a CTL can be added to the store.                                                                                                                                                                                                                                                                                           |
| [**CRYPT\_ENUM\_KEYID\_PROP**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_enum_keyid_prop?branch=master)                                                                | Callback function used by the [**CryptEnumKeyIdentifierProperties**](/windows/win32/Wincrypt/nf-wincrypt-cryptenumkeyidentifierproperties?branch=master) function.                                                                                                                                                                                                                          |
| [**CRYPT\_ENUM\_OID\_FUNCTION**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_enum_oid_func?branch=master)                                                            | Callback function used by the [**CryptEnumOIDFunction**](/windows/win32/Wincrypt/nf-wincrypt-cryptenumoidfunction?branch=master) function.                                                                                                                                                                                                                                                  |
| [**CRYPT\_ENUM\_OID\_INFO**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_enum_oid_info?branch=master)                                                                    | Callback function used by the [**CryptEnumOIDInfo**](/windows/win32/Wincrypt/nf-wincrypt-cryptenumoidinfo?branch=master) function.                                                                                                                                                                                                                                                          |
| [**CryptGetSignerCertificateCallback**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_get_signer_certificate?branch=master)                                           | Callback function used with the [**CRYPT\_VERIFY\_MESSAGE\_PARA**](/windows/win32/Wincrypt/ns-wincrypt-_crypt_verify_message_para?branch=master) structure to get and verify a message signer's certificate.                                                                                                                                                                                 |
| [**PCRYPT\_DECRYPT\_PRIVATE\_KEY\_FUNC**](/windows/win32/Wincrypt/nc-wincrypt-pcrypt_decrypt_private_key_func?branch=master)                                           | Callback function used by the [**CryptImportPKCS8**](/windows/win32/Wincrypt/nf-wincrypt-cryptimportpkcs8?branch=master) function.                                                                                                                                                                                                                                                          |
| [**PCRYPT\_ENCRYPT\_PRIVATE\_KEY\_FUNC**](/windows/win32/Wincrypt/nc-wincrypt-pcrypt_encrypt_private_key_func?branch=master)                                           | Callback function used when creating the [**CRYPT\_ENCRYPTED\_PRIVATE\_KEY\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_crypt_encrypted_private_key_info?branch=master) structure.                                                                                                                                                                                                          |
| [**PCRYPT\_RESOLVE\_HCRYPTPROV\_FUNC**](/windows/win32/Wincrypt/nc-wincrypt-pcrypt_resolve_hcryptprov_func?branch=master)                                              | Callback function used by the [**CryptImportPKCS8**](/windows/win32/Wincrypt/nf-wincrypt-cryptimportpkcs8?branch=master) function.                                                                                                                                                                                                                                                          |
| [**PFN\_CDF\_PARSE\_ERROR\_CALLBACK**](/windows/win32/Mscat/nc-mscat-pfn_cdf_parse_error_callback?branch=master)                                                 | A user-defined function called for Catalog Definition Function errors while parsing a catalog definition file (CDF).                                                                                                                                                                                                                          |
| [**PFN\_CERT\_CREATE\_CONTEXT\_SORT\_FUNC**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cert_create_context_sort_func?branch=master)                                      | Called for each sorted context entry when a context is created.                                                                                                                                                                                                                                                                               |
| [**PFN\_CMSG\_CNG\_IMPORT\_CONTENT\_ENCRYPT\_KEY**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cmsg_cng_import_content_encrypt_key?branch=master)                         | A CNG [*object identifier*](security.o_gly#-security-object-identifier-gly) (OID) installable function for import of an already decrypted content encryption key (CEK).                                                                                                                                       |
| [**PFN\_CMSG\_CNG\_IMPORT\_KEY\_AGREE**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cmsg_cng_import_key_agree?branch=master)                                              | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_CNG\_IMPORT\_KEY\_TRANS**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cmsg_cng_import_key_trans?branch=master)                                              | A CNG OID installable function for import and [*decryption*](security.d_gly#-security-decryption-gly) of a key-transport-recipient, encrypted, content [*encryption*](security.e_gly#-security-encryption-gly) key (CEK).                                                                   |
| [**PFN\_CMSG\_EXPORT\_KEY\_AGREE**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cmsg_export_key_agree?branch=master)                                                       | Encrypts and exports the content encryption key for a key agreement recipient of an enveloped message.                                                                                                                                                                                                                                        |
| [**PFN\_CMSG\_EXPORT\_KEY\_TRANS**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cmsg_export_key_trans?branch=master)                                                       | Encrypts and exports the content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                        |
| [**PFN\_CMSG\_EXPORT\_MAIL\_LIST**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cmsg_export_mail_list?branch=master)                                                       | Encrypts and exports the content encryption key for a mailing list recipient of an enveloped message.                                                                                                                                                                                                                                         |
| [**PFN\_CMSG\_GEN\_CONTENT\_ENCRYPT\_KEY**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cmsg_gen_content_encrypt_key?branch=master)                                        | Generates the [*symmetric key*](security.s_gly#-security-symmetric-key-gly) used to encrypt content for an enveloped message.                                                                                                                                                                                     |
| [**PFN\_CMSG\_IMPORT\_KEY\_AGREE**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cmsg_import_key_agree?branch=master)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_IMPORT\_KEY\_TRANS**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cmsg_import_key_trans?branch=master)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_IMPORT\_MAIL\_LIST**](/windows/win32/Wincrypt/nc-wincrypt-pfn_cmsg_import_mail_list?branch=master)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CRYPT\_EXPORT\_PUBLIC\_KEY\_INFO\_EX2\_FUNC**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_export_public_key_info_ex2_func?branch=master)                    | Called by [**CryptExportPublicKeyInfoEx**](/windows/win32/Wincrypt/nf-wincrypt-cryptexportpublickeyinfoex?branch=master) to export a public key BLOB and encode it.                                                                                                                                                                                                                         |
| [**PFN\_CRYPT\_EXTRACT\_ENCODED\_SIGNATURE\_PARAMETERS\_FUNC**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_extract_encoded_signature_parameters_func?branch=master) | Called to decode and return the hash algorithm identifier and optionally the signature parameters.                                                                                                                                                                                                                                            |
| [**PFN\_CRYPT\_SIGN\_AND\_ENCODE\_HASH\_FUNC**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_sign_and_encode_hash_func?branch=master)                                 | Called to sign and encode a computed hash.                                                                                                                                                                                                                                                                                                    |
| [**PFN\_CRYPT\_VERIFY\_ENCODED\_SIGNATURE\_FUNC**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_verify_encoded_signature_func?branch=master)                          | Called to decrypt an encoded signature and compare it to a computed hash.                                                                                                                                                                                                                                                                     |
| [**PFN\_IMPORT\_PUBLIC\_KEY\_INFO\_EX2\_FUNC**](/windows/win32/Wincrypt/nc-wincrypt-pfn_import_public_key_info_ex2_func?branch=master)                                 | Called by [**CryptImportPublicKeyInfoEx2**](/windows/win32/Wincrypt/nf-wincrypt-cryptimportpublickeyinfoex2?branch=master) to decode the [*public key algorithm*](security.p_gly#-security-public-key-algorithm-gly) identifier, load the algorithm provider, and import the [*key pair*](security.k_gly#-security-key-pair-gly). |
| [**PFNCCERTDISPLAYPROC**](pfnccertdisplayproc.md)                                                                       | A user-defined callback function that allows the caller of the [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md) function to handle the display of certificates that the user selects to view.                                                                                                                               |
| [**PFNCMFILTERPROC**](/windows/win32/CryptDlg/nc-cryptdlg-pfncmfilterproc?branch=master)                                                                               | Filters each certificate to decide if it will appear in the certificate selection dialog box displayed by the [**CertSelectCertificate**](/windows/win32/CryptDlg/?branch=master) function.                                                                                                                                                                |
| [**PFNCMHOOKPROC**](/windows/win32/CryptDlg/nc-cryptdlg-pfncmhookproc?branch=master)                                                                                   | Called before messages are processed by the certificate selection dialog box produced by the [**CertSelectCertificate**](/windows/win32/CryptDlg/?branch=master) function.                                                                                                                                                                                 |



 

## Catalog Definition Functions

These functions are used to create a catalog. All of these functions are called by [MakeCat](makecat.md).

| Function                                                                           | Description                                                                                                               |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**CryptCATCDFClose**](/windows/win32/Mscat/nf-mscat-cryptcatcdfclose?branch=master)                                       | Closes a catalog definition file and frees the memory for the corresponding [**CRYPTCATCDF**](/windows/win32/Mscat/ns-mscat-cryptcatcdf_?branch=master) structure. |
| [**CryptCATCDFEnumAttributesWithCDFTag**](cryptcatcdfenumattributeswithcdftag.md) | Enumerates the attributes of member files in the **CatalogFiles** section of a CDF.                                       |
| [**CryptCATCDFEnumCatAttributes**](/windows/win32/Mscat/nf-mscat-cryptcatcdfenumcatattributes?branch=master)               | Enumerates catalog-level attributes within the **CatalogHeader** section of a CDF.                                        |
| [**CryptCATCDFEnumMembersByCDFTagEx**](cryptcatcdfenummembersbycdftagex.md)       | Enumerates the individual file members in the **CatalogFiles** section of a CDF.                                          |
| [**CryptCATCDFOpen**](/windows/win32/Mscat/nf-mscat-cryptcatcdfopen?branch=master)                                         | Opens an existing CDF for reading and initializes a [**CRYPTCATCDF**](/windows/win32/Mscat/ns-mscat-cryptcatcdf_?branch=master) structure.                         |



 

## Catalog Functions

These functions are used to manage a catalog.

| Function                                                                             | Description                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptCATAdminAcquireContext**](/windows/win32/Mscat/nf-mscat-cryptcatadminacquirecontext?branch=master)                   | Acquires a handle to a catalog administrator context. This handle can be used by subsequent calls to the [**CryptCATAdminAddCatalog**](/windows/win32/Mscat/nf-mscat-cryptcatadminaddcatalog?branch=master), [**CryptCATAdminEnumCatalogFromHash**](/windows/win32/Mscat/nf-mscat-cryptcatadminenumcatalogfromhash?branch=master), and [**CryptCATAdminRemoveCatalog**](/windows/win32/Mscat/nf-mscat-cryptcatadminremovecatalog?branch=master) functions. |
| [**CryptCATAdminAcquireContext2**](/windows/win32/Mscat/nf-mscat-cryptcatadminacquirecontext2?branch=master)                 | Acquires a handle to a catalog administrator context for a given hash algorithm and hash policy.                                                                                                                                                                                                                                   |
| [**CryptCATAdminAddCatalog**](/windows/win32/Mscat/nf-mscat-cryptcatadminaddcatalog?branch=master)                           | Adds a catalog to the catalog database.                                                                                                                                                                                                                                                                                            |
| [**CryptCATAdminCalcHashFromFileHandle**](/windows/win32/Mscat/nf-mscat-cryptcatadmincalchashfromfilehandle?branch=master)   | Calculates the hash for a file.                                                                                                                                                                                                                                                                                                    |
| [**CryptCATAdminCalcHashFromFileHandle2**](/windows/win32/Mscat/nf-mscat-cryptcatadmincalchashfromfilehandle2?branch=master) | Calculates the hash for a file by using the specified algorithm.                                                                                                                                                                                                                                                                   |
| [**CryptCATAdminEnumCatalogFromHash**](/windows/win32/Mscat/nf-mscat-cryptcatadminenumcatalogfromhash?branch=master)         | Enumerates the catalogs that contain a specified hash.                                                                                                                                                                                                                                                                             |
| [**CryptCATAdminReleaseCatalogContext**](/windows/win32/Mscat/nf-mscat-cryptcatadminreleasecatalogcontext?branch=master)     | Releases a handle to a catalog context previously returned by the [**CryptCATAdminAddCatalog**](/windows/win32/Mscat/nf-mscat-cryptcatadminaddcatalog?branch=master) function.                                                                                                                                                                                             |
| [**CryptCATAdminReleaseContext**](/windows/win32/Mscat/nf-mscat-cryptcatadminreleasecontext?branch=master)                   | Releases the handle previously assigned by the [**CryptCATAdminAcquireContext**](/windows/win32/Mscat/nf-mscat-cryptcatadminacquirecontext?branch=master) function.                                                                                                                                                                                                        |
| [**CryptCATAdminRemoveCatalog**](/windows/win32/Mscat/nf-mscat-cryptcatadminremovecatalog?branch=master)                     | Deletes a catalog file and removes that catalog's entry from the Windows catalog database.                                                                                                                                                                                                                                         |
| [**CryptCATAdminResolveCatalogPath**](/windows/win32/Mscat/nf-mscat-cryptcatadminresolvecatalogpath?branch=master)           | Retrieves the fully qualified path of the specified catalog.                                                                                                                                                                                                                                                                       |
| [**CryptCATCatalogInfoFromContext**](/windows/win32/Mscat/nf-mscat-cryptcatcataloginfofromcontext?branch=master)             | Retrieves catalog information from a specified catalog context.                                                                                                                                                                                                                                                                    |
| [**CryptCATClose**](/windows/win32/Mscat/nf-mscat-cryptcatclose?branch=master)                                               | Closes a catalog handle opened previously by the [**CryptCATOpen**](/windows/win32/Mscat/nf-mscat-cryptcatopen?branch=master) function.                                                                                                                                                                                                                                    |
| [**CryptCATEnumerateAttr**](/windows/win32/Mscat/nf-mscat-cryptcatenumerateattr?branch=master)                               | Enumerates the attributes associated with a member of a catalog.                                                                                                                                                                                                                                                                   |
| [**CryptCATEnumerateCatAttr**](/windows/win32/Mscat/nf-mscat-cryptcatenumeratecatattr?branch=master)                         | Enumerates the attributes associated with a catalog.                                                                                                                                                                                                                                                                               |
| [**CryptCATEnumerateMember**](/windows/win32/Mscat/nf-mscat-cryptcatenumeratemember?branch=master)                           | Enumerates the members of a catalog.                                                                                                                                                                                                                                                                                               |
| [**CryptCATGetAttrInfo**](/windows/win32/Mscat/nf-mscat-cryptcatgetattrinfo?branch=master)                                   | Retrieves information about an attribute of a member of a catalog.                                                                                                                                                                                                                                                                 |
| [**CryptCATGetMemberInfo**](/windows/win32/Mscat/nf-mscat-cryptcatgetmemberinfo?branch=master)                               | Retrieves member information from the catalog's PKCS \#7. In addition to retrieving the member information for a specified reference tag, this function opens a member context.                                                                                                                                                    |
| [**CryptCATOpen**](/windows/win32/Mscat/nf-mscat-cryptcatopen?branch=master)                                                 | Opens a catalog, and returns a context handle to the open catalog.                                                                                                                                                                                                                                                                 |
| [**IsCatalogFile**](/windows/win32/Mscat/nf-mscat-iscatalogfile?branch=master)                                               | Retrieves a Boolean value that indicates whether the specified file is a catalog file.                                                                                                                                                                                                                                             |



 

## WinTrust Functions

The following functions are used to perform various trust operations.

| Function                                                                               | Description                                                                                                                                                          |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WintrustAddActionID**](/windows/win32/Wintrust/nf-wintrust-wintrustaddactionid?branch=master)                                     | Adds a trust provider action to the user's system.                                                                                                                   |
| [**WintrustGetRegPolicyFlags**](/windows/win32/Wintrust/nf-wintrust-wintrustgetregpolicyflags?branch=master)                         | Retrieves policy flags for a policy provider.                                                                                                                        |
| [**WintrustAddDefaultForUsage**](/windows/win32/Wintrust/nf-wintrust-wintrustadddefaultforusage?branch=master)                       | Specifies the default usage identifier and callback information for a provider                                                                                       |
| [**WintrustGetDefaultForUsage**](/windows/win32/Wintrust/nf-wintrust-wintrustgetdefaultforusage?branch=master)                       | Retrieves the default usage identifier and callback information.                                                                                                     |
| [**WintrustLoadFunctionPointers**](/windows/win32/Wintrust/nf-wintrust-wintrustloadfunctionpointers?branch=master)                   | Loads function entry points for a specified action GUID.                                                                                                             |
| [**WintrustRemoveActionID**](/windows/win32/Wintrust/nf-wintrust-wintrustremoveactionid?branch=master)                               | Removes an action added by the [**WintrustAddActionID**](/windows/win32/Wintrust/nf-wintrust-wintrustaddactionid?branch=master) function.                                                                          |
| [**WintrustSetDefaultIncludePEPageHashes**](/windows/win32/Wintrust/nf-wintrust-wintrustsetdefaultincludepepagehashes?branch=master) | Sets the default setting that determines whether page hashes are included when creating subject interface package (SIP) indirect data for portable executable files. |
| [**WintrustSetRegPolicyFlags**](/windows/win32/Wintrust/nf-wintrust-wintrustsetregpolicyflags?branch=master)                         | Sets policy flags for a policy provider.                                                                                                                             |
| [**WinVerifyTrust**](/windows/win32/Wintrust/nf-wintrust-winverifytrust?branch=master)                                               | Performs a trust verification action on a specified object.                                                                                                          |
| [**WinVerifyTrustEx**](/windows/win32/Wintrust/nf-wintrust-winverifytrustex?branch=master)                                           | Performs a trust verification action on a specified object and takes a pointer to a WINTRUST\_DATA structure.                                                        |
| [**WTHelperCertCheckValidSignature**](/windows/win32/Wintrust/nf-wintrust-wthelpercertcheckvalidsignature?branch=master)             | Checks whether a signature is valid.                                                                                                                                 |
| [**WTHelperCertFindIssuerCertificate**](wthelpercertfindissuercertificate.md)         | Finds an issuer certificate from the specified certificate stores that matches the specified subject certificate.                                                    |
| [**WTHelperCertIsSelfSigned**](/windows/win32/Wintrust/nf-wintrust-wthelpercertisselfsigned?branch=master)                           | Checks whether a certificate is self-signed.                                                                                                                         |
| [**WTHelperGetFileHash**](wthelpergetfilehash.md)                                     | Verifies the signature of a signed file and obtains the hash value and algorithm identifier for the file.                                                            |
| [**WTHelperGetProvCertFromChain**](/windows/win32/Wintrust/nf-wintrust-wthelpergetprovcertfromchain?branch=master)                   | Retrieves a trust provider certificate from the certificate chain.                                                                                                   |
| [**WTHelperGetProvPrivateDataFromChain**](/windows/win32/Wintrust/nf-wintrust-wthelpergetprovprivatedatafromchain?branch=master)     | Receives a [**CRYPT\_PROVIDER\_PRIVDATA**](/windows/win32/Wintrust/ns-wintrust-_crypt_provider_privdata?branch=master) structure from the chain by using the provider ID.                                           |
| [**WTHelperGetProvSignerFromChain**](/windows/win32/Wintrust/nf-wintrust-wthelpergetprovsignerfromchain?branch=master)               | Retrieves a signer or countersigner by index from the chain.                                                                                                         |
| [**WTHelperProvDataFromStateData**](/windows/win32/Wintrust/nf-wintrust-wthelperprovdatafromstatedata?branch=master)                 | Retrieves trust provider information from a specified handle.                                                                                                        |



 

## Object Locator Functions

The following callback functions can be implemented by a custom provider that is intended to be called by the Secure Channel (Schannel) security package to retrieve certificates.



| Function                                                                                                             | Description                                             |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FLUSH**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_flush?branch=master)                      | Specifies that an object has changed.                   |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_GET**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_get?branch=master)                          | Retrieves an object.                                    |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_RELEASE**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_release?branch=master)                  | Releases the provider.                                  |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FREE\_PASSWORD**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_free_password?branch=master)     | Releases the password used to encrypt a PFX byte array. |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FREE**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_free?branch=master)                        | Releases the object returned by the provider.           |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FREE\_IDENTIFIER**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_free_identifier?branch=master) | Releases memory for an object identifier.               |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_INITIALIZE**](/windows/win32/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_initialize?branch=master)            | Initializes the provider.                               |



 

 

 




