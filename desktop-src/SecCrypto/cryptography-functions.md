---
Description: Lists the functions provided by CryptoAPI.
ms.assetid: 9a65f73d-6f8c-4271-a2d0-d91ad952f9c6
title: Cryptography Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
| [**CryptXmlCreateReference**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlcreatereference)                        | Creates a reference to an XML signature.                                                                                                                                                                                                                                                                         |
| [**CryptXmlAddObject**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmladdobject)                                    | Adds the **Object** element to the Signature in the Document Context opened for encoding.                                                                                                                                                                                                                        |
| [**CryptXmlClose**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlclose)                                            | Closes a cryptographic XML object handle.                                                                                                                                                                                                                                                                        |
| [**CryptXmlDigestReference**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmldigestreference)                        | Used by an application to digest the resolved reference. This function applies transforms before updating the digest.                                                                                                                                                                                            |
| [**CryptXmlDllCloseDigest**](https://msdn.microsoft.com/en-us/library/Dd433809(v=VS.85).aspx)                          | Frees the CRYPT\_XML\_DIGEST allocated by the [**CryptXmlDllCreateDigest**](https://msdn.microsoft.com/en-us/library/Dd433810(v=VS.85).aspx) function.                                                                                                                                                                                               |
| [**CryptXmlDllCreateDigest**](https://msdn.microsoft.com/en-us/library/Dd433810(v=VS.85).aspx)                        | Creates a digest object for the specified method.                                                                                                                                                                                                                                                                |
| [**CryptXmlDllCreateKey**](https://msdn.microsoft.com/en-us/library/Dd433811(v=VS.85).aspx)                              | Parses the **KeyValue** element and creates a Cryptography API: Next Generation (CNG) BCrypt key handle to verify a signature.                                                                                                                                                                                   |
| [**CryptXmlDllDigestData**](https://msdn.microsoft.com/en-us/library/Dd433812(v=VS.85).aspx)                            | Puts data into the digest.                                                                                                                                                                                                                                                                                       |
| [**CryptXmlDllEncodeAlgorithm**](https://msdn.microsoft.com/en-us/library/Dd433813(v=VS.85).aspx)                  | Encodes **SignatureMethod** or **DigestMethod** elements for agile algorithms with default parameters.                                                                                                                                                                                                           |
| [**CryptXmlDllEncodeKeyValue**](https://msdn.microsoft.com/en-us/library/Dd433814(v=VS.85).aspx)                    | Encodes a **KeyValue** element.                                                                                                                                                                                                                                                                                  |
| [**CryptXmlDllFinalizeDigest**](https://msdn.microsoft.com/en-us/library/Dd433815(v=VS.85).aspx)                    | Retrieves the digest value.                                                                                                                                                                                                                                                                                      |
| [**CryptXmlDllGetAlgorithmInfo**](https://msdn.microsoft.com/en-us/library/Dd433816(v=VS.85).aspx)                | Decodes the XML algorithm and returns information about the algorithm.                                                                                                                                                                                                                                           |
| [**CryptXmlDllGetInterface**](https://msdn.microsoft.com/en-us/library/Dd433817(v=VS.85).aspx)                        | Retrieves a pointer to the cryptographic extension functions for the specified algorithm.                                                                                                                                                                                                                        |
| [**CryptXmlDllSignData**](https://msdn.microsoft.com/en-us/library/Dd433818(v=VS.85).aspx)                                | Signs data.                                                                                                                                                                                                                                                                                                      |
| [**CryptXmlDllVerifySignature**](https://msdn.microsoft.com/en-us/library/Dd433819(v=VS.85).aspx)                  | Verifies a signature.                                                                                                                                                                                                                                                                                            |
| [**CryptXmlEncode**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlencode)                                          | Encodes signature data by using the supplied XML writer callback function.                                                                                                                                                                                                                                       |
| [**CryptXmlGetAlgorithmInfo**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgetalgorithminfo)                      | Decodes the CRYPT\_XML\_ALGORITHM structure and returns information about the algorithm.                                                                                                                                                                                                                         |
| [**CryptXmlGetDocContext**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgetdoccontext)                            | Returns the document context specified by the supplied handle.                                                                                                                                                                                                                                                   |
| [**CryptXmlGetReference**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgetreference)                              | Returns the **Reference** element specified by the supplied handle.                                                                                                                                                                                                                                              |
| [**CryptXmlGetSignature**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgetsignature)                              | Returns an XML **Signature** element.                                                                                                                                                                                                                                                                            |
| [**CryptXmlGetStatus**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgetstatus)                                    | Returns a [**CRYPT\_XML\_STATUS**](/windows/desktop/api/Cryptxml/ns-cryptxml-_crypt_xml_status) structure that contains status information about the object specified by the supplied handle.                                                                                                                                                           |
| [**CryptXmlGetTransforms**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgettransforms)                            | Returns information about the default transform chain engine.                                                                                                                                                                                                                                                    |
| [**CryptXmlImportPublicKey**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlimportpublickey)                        | Imports the public key specified by the supplied handle.                                                                                                                                                                                                                                                         |
| [**CryptXmlOpenToEncode**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlopentoencode)                              | Opens an XML digital signature to encode and returns a handle of the opened **Signature** element. The handle encapsulates a document context with a single [**CRYPT\_XML\_SIGNATURE**](/windows/desktop/api/Cryptxml/ns-cryptxml-_crypt_xml_signature) structure and remains open until the [**CryptXmlClose**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlclose) function is called. |
| [**CryptXmlOpenToDecode**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlopentodecode)                              | Opens an XML digital signature to decode and returns the handle of the document context that encapsulates a [**CRYPT\_XML\_SIGNATURE**](/windows/desktop/api/Cryptxml/ns-cryptxml-_crypt_xml_signature) structure. The document context can include one or more **Signature** elements.                                                                 |
| [**CryptXmlSetHMACSecret**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlsethmacsecret)                            | Sets the HMAC secret on the handle before calling the [**CryptXmlSign**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlsign) or [**CryptXmlVerify**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlverifysignature) function.                                                                                                                                                        |
| [**CryptXmlSign**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlsign)                                              | Creates a cryptographic signature of a **SignedInfo** element.                                                                                                                                                                                                                                                   |
| [**CryptXmlVerifySignature**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlverifysignature)                        | Performs a cryptographic signature validation of a **SignedInfo** element.                                                                                                                                                                                                                                       |
| [*PFN\_CRYPT\_XML\_WRITE\_CALLBACK*](/windows/desktop/api/Cryptxml/nc-cryptxml-pfn_crypt_xml_write_callback)            | Creates a transform for a specified data provider.                                                                                                                                                                                                                                                               |
| [*PFN\_CRYPT\_XML\_CREATE\_TRANSFORM*](/windows/desktop/api/Cryptxml/nc-cryptxml-pfn_crypt_xml_create_transform)        | Writes cryptographic XML data.                                                                                                                                                                                                                                                                                   |
| [*PFN\_CRYPT\_XML\_DATA\_PROVIDER\_READ*](/windows/desktop/api/Cryptxml/nc-cryptxml-pfn_crypt_xml_data_provider_read)   | Reads cryptographic XML data.                                                                                                                                                                                                                                                                                    |
| [*PFN\_CRYPT\_XML\_DATA\_PROVIDER\_CLOSE*](/windows/desktop/api/Cryptxml/nc-cryptxml-pfn_crypt_xml_data_provider_close) | Releases the cryptographic XML data provider.                                                                                                                                                                                                                                                                    |
| [*PFN\_CRYPT\_XML\_ENUM\_ALG\_INFO*](/windows/desktop/api/Cryptxml/nc-cryptxml-pfn_crypt_xml_enum_alg_info)             | Enumerates predefined and registered [**CRYPT\_XML\_ALGORITHM\_INFO**](/windows/desktop/api/Cryptxml/ns-cryptxml-_crypt_xml_algorithm_info) entries.                                                                                                                                                                                                    |



 

## Signer Functions

Provides functions to sign and time stamp data.



| Function                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SignerFreeSignerContext**](signerfreesignercontext.md) | Frees a [**SIGNER\_CONTEXT**](signer-context.md) structure allocated by a previous call to the [**SignerSignEx**](signersignex.md) function.                                                                                                                                                                                                                                                                      |
| [**SignError**](signerror.md)                             | Calls the [**GetLastError**](https://msdn.microsoft.com/en-us/library/ms679360(v=VS.85).aspx) function and converts the return code to an **HRESULT**.                                                                                                                                                                                                                                                                                                            |
| [**SignerSign**](signersign.md)                           | Signs the specified file.                                                                                                                                                                                                                                                                                                                                                                                           |
| [**SignerSignEx**](signersignex.md)                       | Signs the specified file and returns a pointer to the signed data.                                                                                                                                                                                                                                                                                                                                                  |
| [**SignerSignEx2**](signersignex2.md)                     | Signs and time stamps the specified file, allowing multiple nested signatures.                                                                                                                                                                                                                                                                                                                                      |
| [**SignerTimeStamp**](signertimestamp.md)                 | Time stamps the specified subject. This function supports Authenticode time stamping. To perform X.509 Public Key Infrastructure (RFC 3161) time stamping, use the [**SignerTimeStampEx2**](signertimestampex2.md) function.                                                                                                                                                                                       |
| [**SignerTimeStampEx**](signertimestampex.md)             | Time stamps the specified subject and optionally returns a pointer to a [**SIGNER\_CONTEXT**](signer-context.md) structure that contains a pointer to a [*BLOB*](https://msdn.microsoft.com/en-us/library/ms721569(v=VS.85).aspx). This function supports Authenticode time stamping. To perform X.509 Public Key Infrastructure (RFC 3161) time stamping, use the [**SignerTimeStampEx2**](signertimestampex2.md) function. |
| [**SignerTimeStampEx2**](signertimestampex2.md)           | Time stamps the specified subject and optionally returns a pointer to a [**SIGNER\_CONTEXT**](signer-context.md) structure that contains a pointer to a [*BLOB*](https://msdn.microsoft.com/en-us/library/ms721569(v=VS.85).aspx). This function can be used to perform X.509 Public Key Infrastructure, RFC 3161–compliant, time stamps.                                                                                     |
| [**SignerTimeStampEx3**](signertimestampex3.md)           | Time stamps the specified subject and supports setting time stamps on multiple signatures.                                                                                                                                                                                                                                                                                                                          |



 

## Base Cryptography Functions

Base cryptographic functions provide the most flexible means of developing cryptography applications. All communication with a [*cryptographic service provider*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CSP) occurs through these functions.

A CSP is an independent module that performs all cryptographic operations. At least one CSP is required with each application that uses cryptographic functions. A single application can occasionally use more than one CSP.

If more than one CSP is used, the one to use can be specified in the CryptoAPI cryptographic function calls. One CSP, the Microsoft Base Cryptographic Provider, is bundled with the [*CryptoAPI*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx). This CSP is used as a default provider by many of the CryptoAPI functions if no other CSP is specified.

Each CSP provides a different implementation of the cryptographic support provided to CryptoAPI. Some provide stronger cryptographic algorithms; others contain hardware components, such as [*smart cards*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx). In addition, some CSPs can occasionally communicate directly with users, such as when [*digital signatures*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx) are performed by using the user's [*signature private key*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx).

Base cryptographic functions are in the following broad groups:

-   Service Provider Functions
-   Key Generation and Exchange Functions
-   Object Encoding and Decoding Functions
-   Data Encryption and Decryption Functions
-   Hash and Digital Signature Functions

### Service Provider Functions

Applications use the following service functions to connect and disconnect a [*cryptographic service provider*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CSP).

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
<td>[<strong>CryptAcquireContext</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Acquires a handle to the current user's [<em>key container</em>](https://msdn.microsoft.com/en-us/library/ms721590(v=VS.85).aspx) within a particular CSP.</td>
</tr>
<tr class="even">
<td>[<strong>CryptContextAddRef</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcontextaddref)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Increments the [<em>reference count</em>](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) on an [<strong>HCRYPTPROV</strong>](hcryptprov.md) handle.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptEnumProviders</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumprovidersa)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Enumerates the providers on a computer.</td>
</tr>
<tr class="even">
<td>[<strong>CryptEnumProviderTypes</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumprovidertypesa)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Enumerates the types of providers supported on the computer.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGetDefaultProvider</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetdefaultprovidera)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Determines the default CSP either for the current user or for the computer for a specified provider type.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGetProvParam</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetprovparam)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves the parameters that govern the operations of a CSP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptInstallDefaultContext</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptinstalldefaultcontext)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Installs a previously acquired [<strong>HCRYPTPROV</strong>](hcryptprov.md) context to be used as a default context.</td>
</tr>
<tr class="even">
<td>[<strong>CryptReleaseContext</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptreleasecontext)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Releases the handle acquired by the [<strong>CryptAcquireContext</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) function.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSetProvider</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetprovidera) and [<strong>CryptSetProviderEx</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetproviderexa)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies the user default CSP for a particular CSP type.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSetProvParam</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetprovparam)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies attributes of a CSP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUninstallDefaultContext</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptuninstalldefaultcontext)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Removes a default context previously installed by [<strong>CryptInstallDefaultContext</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptinstalldefaultcontext).</td>
</tr>
<tr class="even">
<td>[<strong>FreeCryptProvFromCertEx</strong>](freecryptprovfromcertex.md)</td>
<td>Releases the handle either to a [<em>cryptographic service provider</em>](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CSP) or to a Cryptography API: Next Generation (CNG) key.</td>
</tr>
</tbody>
</table>



 

### Key Generation and Exchange Functions

Key generation and exchange functions [*exchange keys*](https://msdn.microsoft.com/en-us/library/ms721575(v=VS.85).aspx) with other users and create, configure, and destroy [*cryptographic keys*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx).

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
<td>[<strong>CryptDeriveKey</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptderivekey)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a key derived from a password.</td>
</tr>
<tr class="even">
<td>[<strong>CryptDestroyKey</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdestroykey)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Destroys a key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptDuplicateKey</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptduplicatekey)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Makes an exact copy of a key, including the [<em>state</em>](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) of the key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptExportKey</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Transfers a key from the CSP into a [<em>key BLOB</em>](https://msdn.microsoft.com/en-us/library/ms721590(v=VS.85).aspx) in the application's memory space.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGenKey</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgenkey)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a random key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGenRandom</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgenrandom)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Generates random data.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGetKeyParam</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetkeyparam)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves a key's parameters.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGetUserKey</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetuserkey)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Gets a handle to the key exchange or signature key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptImportKey</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Transfers a key from a [<em>key BLOB</em>](https://msdn.microsoft.com/en-us/library/ms721590(v=VS.85).aspx) to a CSP.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSetKeyParam</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetkeyparam)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies a key's parameters.</td>
</tr>
</tbody>
</table>



 

### Object Encoding and Decoding Functions

These are generalized encoding and decoding functions. They are used to encode and decode [*certificates*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx), [*certificate revocation lists*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CRLs), [*certificate requests*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx), and certificate extensions.

| Function                                           | Description                                                                                                                                      |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptDecodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobject)     | Decodes a structure of type *lpszStructType*.                                                                                                    |
| [**CryptDecodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobjectex) | Decodes a structure of type *lpszStructType*. [**CryptDecodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobjectex) supports the one-pass memory allocation option. |
| [**CryptEncodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobject)     | Encodes a structure of type *lpszStructType*.                                                                                                    |
| [**CryptEncodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobjectex) | Encodes a structure of type *lpszStructType*. [**CryptEncodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobjectex) supports the one-pass memory allocation option. |



 

### Data Encryption and Decryption Functions

The following functions support encryption and decryption operations. [**CryptEncrypt**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencrypt) and [**CryptDecrypt**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecrypt) require a [*cryptographic key*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) before being called. This is done by using the [**CryptGenKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgenkey), [**CryptDeriveKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptderivekey), or [**CryptImportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey) function. The encryption algorithm is specified when the key is created. [**CryptSetKeyParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetkeyparam) can set additional encryption parameters.

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
<td>[<strong>CryptDecrypt</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecrypt)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Decrypts a section of [<em>ciphertext</em>](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) by using the specified encryption key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptEncrypt</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencrypt)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Encrypts a section of [<em>plaintext</em>](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) by using the specified encryption key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptProtectData</strong>](/windows/desktop/api/Dpapi/nf-dpapi-cryptprotectdata)</td>
<td>Performs encryption on the data in a [<strong>DATA_BLOB</strong>](https://www.bing.com/search?q=<strong>DATA_BLOB</strong>) structure.</td>
</tr>
<tr class="even">
<td>[<strong>CryptProtectMemory</strong>](/windows/desktop/api/Dpapi/nf-dpapi-cryptprotectmemory)</td>
<td>Encrypts memory to protect sensitive information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUnprotectData</strong>](/windows/desktop/api/Dpapi/nf-dpapi-cryptunprotectdata)</td>
<td>Performs a decryption and integrity check of the data in a [<strong>DATA_BLOB</strong>](https://www.bing.com/search?q=<strong>DATA_BLOB</strong>).</td>
</tr>
<tr class="even">
<td>[<strong>CryptUnprotectMemory</strong>](/windows/desktop/api/Dpapi/nf-dpapi-cryptunprotectmemory)</td>
<td>Decrypts memory that was encrypted using [<strong>CryptProtectMemory</strong>](/windows/desktop/api/Dpapi/nf-dpapi-cryptprotectmemory).</td>
</tr>
</tbody>
</table>



 

### Hash and Digital Signature Functions

These functions compute [*hashes*](https://msdn.microsoft.com/en-us/library/ms721586(v=VS.85).aspx) of data and also create and verify [*digital signatures*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx). Hashes are also known as message digests.

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
<td>[<strong>CryptCreateHash</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcreatehash)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates an empty hash object.</td>
</tr>
<tr class="even">
<td>[<strong>CryptDestroyHash</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdestroyhash)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Destroys a hash object.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptDuplicateHash</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptduplicatehash)</td>
<td>Duplicates a hash object.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGetHashParam</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgethashparam)</td>
<td>Retrieves a hash object parameter.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptHashData</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashdata)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes a block of data, adding it to the specified hash object.</td>
</tr>
<tr class="even">
<td>[<strong>CryptHashSessionKey</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashsessionkey)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes a session key, adding it to the specified hash object.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSetHashParam</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsethashparam)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Sets a hash object parameter.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSignHash</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignhasha)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Signs the specified hash object.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUIWizDigitalSign</strong>](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuiwizdigitalsign)</td>
<td>Displays a wizard that digitally signs a document or a [<em>BLOB</em>](https://msdn.microsoft.com/en-us/library/ms721569(v=VS.85).aspx).</td>
</tr>
<tr class="even">
<td>[<strong>CryptUIWizFreeDigitalSignContext</strong>](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuiwizfreedigitalsigncontext)</td>
<td>Releases a pointer to a [<strong>CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT</strong>](/windows/desktop/api/Cryptuiapi/ns-cryptuiapi-_cryptui_wiz_digital_sign_context) structure.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptVerifySignature</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifysignaturea)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Verifies a digital signature, given a handle to the hash object.</td>
</tr>
<tr class="even">
<td>[<strong>PFNCFILTERPROC</strong>](/windows/desktop/api/Cryptuiapi/nc-cryptuiapi-pfncfilterproc)</td>
<td>Filters the certificates that appear in the digital signature wizard displayed by the [<strong>CryptUIWizDigitalSign</strong>](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuiwizdigitalsign) function.</td>
</tr>
</tbody>
</table>



 

## Certificate and Certificate Store Functions

Certificate and certificate store functions manage the use, storage, and retrieval of [*certificates*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx), [*certificate revocation lists*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CRLs), and [*certificate trust lists*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CTLs). These functions are divided into the following groups:

-   Certificate Store Functions
-   Certificate and Certificate Store Maintenance Functions
-   Certificate Functions
-   Certificate Revocation List Functions
-   Certificate Trust List Functions
-   Extended Property Functions
-   MakeCert Functions

### Certificate Store Functions

A user site can, over time, collect many certificates. Typically, a site has certificates for the user of the site as well as other certificates that describe those individuals and entities with whom the user communicates. For each entity, there can be more than one certificate. For each individual certificate, there should be a chain of verifying certificates that provides a trail back to a trusted [*root certificate*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx). [*Certificate stores*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) and their related functions provide functionality to store, retrieve, enumerate, verify, and use the information stored in the certificates.

| Function                                                               | Description                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddStoreToCollection**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddstoretocollection)           | Adds a sibling certificate store to a collection certificate store.                                                                                                                                                                                                                                                                       |
| [**CertCloseStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certclosestore)                               | Closes a certificate store handle.                                                                                                                                                                                                                                                                                                        |
| [**CertControlStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcontrolstore)                           | Allows an application to be notified when there is a difference between the contents of a cached store and the contents of the store that is persisted to storage. It also provides desynchronization of the cached store, if necessary, and provides a means to commit changes made in the cached store to persisted storage.<br/> |
| [**CertDuplicateStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatestore)                       | Duplicates a store handle by incrementing the [*reference count*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx).                                                                                                                                                                                            |
| [**CertEnumPhysicalStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumphysicalstore)                 | Enumerates the physical stores for a specified system store.                                                                                                                                                                                                                                                                              |
| [**CertEnumSystemStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumsystemstore)                     | Enumerates all available system stores.                                                                                                                                                                                                                                                                                                   |
| [**CertEnumSystemStoreLocation**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumsystemstorelocation)     | Enumerates all of the locations that have an available system store.                                                                                                                                                                                                                                                                      |
| [**CertGetStoreProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetstoreproperty)                   | Gets a store property.                                                                                                                                                                                                                                                                                                                    |
| [**CertOpenStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenstore)                                 | Opens a certificate store using a specified store provider type.                                                                                                                                                                                                                                                                          |
| [**CertOpenSystemStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopensystemstorea)                     | Opens a system certificate store based on a subsystem protocol.                                                                                                                                                                                                                                                                           |
| [**CertRegisterPhysicalStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certregisterphysicalstore)         | Adds a physical store to a registry system store collection.                                                                                                                                                                                                                                                                              |
| [**CertRegisterSystemStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certregistersystemstore)             | Registers a system store.                                                                                                                                                                                                                                                                                                                 |
| [**CertRemoveStoreFromCollection**](/windows/desktop/api/Wincrypt/nf-wincrypt-certremovestorefromcollection) | Removes a sibling certificate store from a collection store.                                                                                                                                                                                                                                                                              |
| [**CertSaveStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsavestore)                                 | Saves the certificate store.                                                                                                                                                                                                                                                                                                              |
| [**CertSetStoreProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetstoreproperty)                   | Sets a store property.                                                                                                                                                                                                                                                                                                                    |
| [**CertUnregisterPhysicalStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certunregisterphysicalstore)     | Removes a physical store from a specified system store collection.                                                                                                                                                                                                                                                                        |
| [**CertUnregisterSystemStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certunregistersystemstore)         | Unregisters a specified system store.                                                                                                                                                                                                                                                                                                     |
| [**CryptUIWizExport**](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuiwizexport)                           | Presents a wizard that exports a certificate, certificate trust list (CTL), certificate revocation list (CRL), or certificate store.                                                                                                                                                                                                      |
| [**CryptUIWizImport**](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuiwizimport)                           | Presents a wizard that imports a certificate, certificate trust list (CTL), certificate revocation list (CRL), or certificate store.                                                                                                                                                                                                      |



 

### Certificate and Certificate Store Maintenance Functions

CryptoAPI provides a set of general certificate and certificate store maintenance functions.

| Function                                                                                                                              | Description                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**CertAddSerializedElementToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddserializedelementtostore)                                                            | Adds the serialized certificate or CRL element to the store.                                   |
| [**CertCreateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatecontext)                                                                                        | Creates the specified context from the encoded bytes. The new context is not put into a store. |
| [**CertEnumSubjectInSortedCTL**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumsubjectinsortedctl)                                                                      | Enumerates the TrustedSubjects in a sorted CTL context.                                        |
| [**CertFindSubjectInCTL**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindsubjectinctl)                                                                                  | Finds the specified subject in a CTL.                                                          |
| [**CertFindSubjectInSortedCTL**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindsubjectinsortedctl)                                                                      | Finds the specified subject in a sorted CTL.                                                   |
| [**OpenPersonalTrustDBDialog**](/windows/desktop/api/wintrust/nf-wintrust-openpersonaltrustdbdialog) and [**OpenPersonalTrustDBDialogEx**](/windows/desktop/api/wintrust/nf-wintrust-openpersonaltrustdbdialogex) | Displays the **Certificates** dialog box.                                                      |



 

### Certificate Functions

Most [*Certificate*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) functions have related functions to deal with [*CRLs*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) and [*CTLs*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx). For more information about related CRL and CTL functions, see Certificate Revocation List Functions and Certificate Trust List Functions.

| Function                                                                             | Description                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddCertificateContextToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcertificatecontexttostore)         | Adds a certificate context to the certificate store.                                                                                                                                                                                            |
| [**CertAddCertificateLinkToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcertificatelinktostore)               | Adds a link in a certificate store to a certificate context in a different store.                                                                                                                                                               |
| [**CertAddEncodedCertificateToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddencodedcertificatetostore)         | Converts the encoded certificate to a certificate context, and then adds the context to the certificate store.                                                                                                                                  |
| [**CertAddRefServerOcspResponse**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddrefserverocspresponse)                 | Increments the reference count for an **HCERT\_SERVER\_OCSP\_RESPONSE** handle.                                                                                                                                                                 |
| [**CertAddRefServerOcspResponseContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddrefserverocspresponsecontext)   | Increments the reference count for a [**CERT\_SERVER\_OCSP\_RESPONSE\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-_cert_server_ocsp_response_context) structure.                                                                                                              |
| [**CertCloseServerOcspResponse**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcloseserverocspresponse)                   | Closes an [*online certificate status protocol*](https://msdn.microsoft.com/en-us/library/ms721599(v=VS.85).aspx) (OCSP) server response handle.                                               |
| [**CertCreateCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatecertificatecontext)                 | Creates a certificate context from an encoded certificate. The created context is not put in a certificate store.                                                                                                                               |
| [**CertCreateSelfSignCertificate**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreateselfsigncertificate)               | Creates a self-signed certificate.                                                                                                                                                                                                              |
| [**CertDeleteCertificateFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certdeletecertificatefromstore)             | Deletes a certificate from the certificate store.                                                                                                                                                                                               |
| [**CertDuplicateCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatecertificatecontext)           | Duplicates a certificate context by incrementing its [*reference count*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx).                                                                                           |
| [**CertEnumCertificatesInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumcertificatesinstore)                   | Enumerates the certificate contexts in the certificate store.                                                                                                                                                                                   |
| [**CertFindCertificateInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindcertificateinstore)                     | Finds the first, or next, certificate context in the certificate store that meets a search criterion.                                                                                                                                           |
| [**CertFreeCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatecontext)                     | Frees a certificate context.                                                                                                                                                                                                                    |
| [**CertGetIssuerCertificateFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetissuercertificatefromstore)       | Gets a certificate context from the certificate store for the first, or next, issuer of the specified subject certificate.                                                                                                                      |
| [**CertGetServerOcspResponseContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetserverocspresponsecontext)         | Retrieves a non-blocking, time valid [*online certificate status protocol*](https://msdn.microsoft.com/en-us/library/ms721599(v=VS.85).aspx) (OCSP) response context for the specified handle. |
| [**CertGetSubjectCertificateFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetsubjectcertificatefromstore)     | Gets from the certificate store the subject certificate context, which is uniquely identified by its issuer and serial number.                                                                                                                  |
| [**CertGetValidUsages**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetvalidusages)                                     | Returns an array of usages that consist of the intersection of the valid usages for all certificates in an array of certificates.                                                                                                               |
| [**CertOpenServerOcspResponse**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenserverocspresponse)                     | Opens a handle to an [*online certificate status protocol*](https://msdn.microsoft.com/en-us/library/ms721599(v=VS.85).aspx) (OCSP) response associated with a server certificate chain.       |
| [**CertRetrieveLogoOrBiometricInfo**](/windows/desktop/api/Wincrypt/nf-wincrypt-certretrievelogoorbiometricinfo)           | Performs a URL retrieval of logo or biometric information specified in either the **szOID\_LOGOTYPE\_EXT** or **szOID\_BIOMETRIC\_EXT** certificate extension.                                                                                  |
| [**CertSelectCertificate**](https://msdn.microsoft.com/en-us/library/Aa376568(v=VS.85).aspx)                               | Presents a dialog box that allows the user to select certificates from a set of certificates that match a given criteria.                                                                                                                       |
| [**CertSelectCertificateChains**](/windows/desktop/api/Wincrypt/nf-wincrypt-certselectcertificatechains)                   | Retrieves certificate chains based on specified selection criteria.                                                                                                                                                                             |
| [**CertSelectionGetSerializedBlob**](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-certselectiongetserializedblob)             | A helper function used to retrieve a serialized certificate [*BLOB*](https://msdn.microsoft.com/en-us/library/ms721569(v=VS.85).aspx) from a [**CERT\_SELECTUI\_INPUT**](/windows/desktop/api/Cryptuiapi/ns-cryptuiapi-cert_selectui_input) structure.                                               |
| [**CertSerializeCertificateStoreElement**](/windows/desktop/api/Wincrypt/nf-wincrypt-certserializecertificatestoreelement) | Serializes a certificate context's encoded certificate and an encoded representation of its properties.                                                                                                                                         |
| [**CertVerifySubjectCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifysubjectcertificatecontext)   | Performs the enabled verification checks on the subject certificate using the issuer.                                                                                                                                                           |
| [**CryptUIDlgCertMgr**](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuidlgcertmgr)                                       | Displays a dialog box that allows the user to manage certificates.                                                                                                                                                                              |
| [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md)                   | Displays a dialog box that allows a user to select a certificate.                                                                                                                                                                               |
| [**CryptUIDlgSelectCertificateFromStore**](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuidlgselectcertificatefromstore) | Displays a dialog box that allows the selection of a certificate from a specified store.                                                                                                                                                        |
| [**CryptUIDlgViewCertificate**](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuidlgviewcertificatea)                       | Presents a dialog box that displays a specified certificate.                                                                                                                                                                                    |
| [**CryptUIDlgViewContext**](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuidlgviewcontext)                               | Displays a certificate, CRL, or CTL.                                                                                                                                                                                                            |
| [**CryptUIDlgViewSignerInfo**](cryptuidlgviewsignerinfo.md)                         | Displays a dialog box that contains the signer information for a signed message.                                                                                                                                                                |
| [**GetFriendlyNameOfCert**](/windows/desktop/api/CryptDlg/nf-cryptdlg-getfriendlynameofcerta)                               | Retrieves the display name for a certificate.                                                                                                                                                                                                   |
| [**RKeyCloseKeyService**](rkeyclosekeyservice.md)                                   | Closes a key service handle.                                                                                                                                                                                                                    |
| [**RKeyOpenKeyService**](rkeyopenkeyservice.md)                                     | Opens a key service handle on a remote computer.                                                                                                                                                                                                |
| [**RKeyPFXInstall**](rkeypfxinstall.md)                                             | Installs a certificate on a remote computer.                                                                                                                                                                                                    |



 

### Certificate Revocation List Functions

These functions manage the storage and retrieval of [*certificate revocation lists*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CRLs).

| Function                                                             | Description                                                                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddCRLContextToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcrlcontexttostore)         | Adds a CRL context to the certificate store.                                                                                                                                          |
| [**CertAddCRLLinkToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcrllinktostore)               | Adds a link in a store to a CRL context in a different store.                                                                                                                         |
| [**CertAddEncodedCRLToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddencodedcrltostore)         | Converts the encoded CRL to a CRL context, and then adds the context to the certificate store.                                                                                        |
| [**CertCreateCRLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatecrlcontext)                 | Creates a CRL context from an encoded CRL. The created context is not put in a certificate store.                                                                                     |
| [**CertDeleteCRLFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certdeletecrlfromstore)             | Deletes a CRL from the certificate store.                                                                                                                                             |
| [**CertDuplicateCRLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatecrlcontext)           | Duplicates a CRL context by incrementing the [*reference count*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx).                                         |
| [**CertEnumCRLsInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumcrlsinstore)                   | Enumerates the CRL contexts in a store.                                                                                                                                               |
| [**CertFindCertificateInCRL**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindcertificateincrl)         | Searches the [*certificate revocation list*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CRL) for the specified certificate. |
| [**CertFindCRLInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindcrlinstore)                     | Finds the first, or next, CRL context in the certificate store that matches a specific criterion.                                                                                     |
| [**CertFreeCRLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecrlcontext)                     | Frees a CRL context.                                                                                                                                                                  |
| [**CertGetCRLFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcrlfromstore)                   | Gets the first, or next, CRL context from the certificate store for the specified issuer certificate.                                                                                 |
| [**CertSerializeCRLStoreElement**](/windows/desktop/api/Wincrypt/nf-wincrypt-certserializecrlstoreelement) | Serializes the CRL context's encoded CRL and its properties.                                                                                                                          |



 

### Certificate Trust List Functions

These functions manage the storage and retrieval of [*certificate trust lists*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CTLs).

| Function                                                               | Description                                                                                                          |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**CertAddCTLContextToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddctlcontexttostore)           | Adds a CTL context to the certificate store.                                                                         |
| [**CertAddCTLLinkToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddctllinktostore)                 | Adds a link in a store to a CRL context in a different store.                                                        |
| [**CertAddEncodedCTLToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddencodedctltostore)           | Converts the encoded CTL to a CTL context, and then adds the context to the certificate store.                       |
| [**CertCreateCTLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatectlcontext)                   | Creates a CTL context from an encoded certificate trust list. The created context is not put in a certificate store. |
| [**CertDeleteCTLFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certdeletectlfromstore)               | Deletes a CTL from the certificate store.                                                                            |
| [**CertDuplicateCTLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatectlcontext)             | Duplicates a CTL context by incrementing the reference count.                                                        |
| [**CertEnumCTLsInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumctlsinstore)                     | Enumerates the CTL contexts in the certificate store.                                                                |
| [**CertFindCTLInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindctlinstore)                       | Finds the first, or next, CTL context in the certificate store that matches a specific criteria.                     |
| [**CertFreeCTLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreectlcontext)                       | Frees a CTL context.                                                                                                 |
| [**CertModifyCertificatesToTrust**](/windows/desktop/api/CryptDlg/nf-cryptdlg-certmodifycertificatestotrust) | Modifies the set of certificates in a CTL for a given purpose.                                                       |
| [**CertSerializeCTLStoreElement**](/windows/desktop/api/Wincrypt/nf-wincrypt-certserializectlstoreelement)   | Serializes the CTL context's encoded CTL and its properties.                                                         |



 

### Extended Property Functions

The following functions work with extended properties of certificates, CRLs, and CTLs.

| Function                                                                             | Description                                                      |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**CertEnumCertificateContextProperties**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumcertificatecontextproperties) | Enumerates the properties for the specified certificate context. |
| [**CertEnumCRLContextProperties**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumcrlcontextproperties)                 | Enumerates the properties for the specified CRL context.         |
| [**CertEnumCTLContextProperties**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumctlcontextproperties)                 | Enumerates the properties for the specified CTL context.         |
| [**CertGetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty)       | Retrieves certificate properties.                                |
| [**CertGetCRLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcrlcontextproperty)                       | Retrieves CRL properties.                                        |
| [**CertGetCTLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetctlcontextproperty)                       | Retrieves CTL properties.                                        |
| [**CertSetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcertificatecontextproperty)       | Sets certificate properties.                                     |
| [**CertSetCRLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcrlcontextproperty)                       | Sets CRL properties.                                             |
| [**CertSetCTLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetctlcontextproperty)                       | Sets CTL properties.                                             |



 

## MakeCert Functions

The following functions support the [MakeCert](makecert.md) tool.



| Function                                                                               | Description                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FreeCryptProvFromCert**](freecryptprovfromcert.md)                                 | Releases the handle to a [*cryptographic service provider*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CSP) and optionally deletes the temporary container created by the [**GetCryptProvFromCert**](getcryptprovfromcert.md) function. |
| [**GetCryptProvFromCert**](getcryptprovfromcert.md)                                   | Gets a handle to a CSP and a key specification for a certificate context.                                                                                                                                                                                                                                |
| [**PvkFreeCryptProv**](pvkfreecryptprov.md)                                           | Releases the handle to a CSP and optionally deletes the temporary container created by the [**PvkGetCryptProv**](pvkgetcryptprov.md) function.                                                                                                                                                          |
| [**PvkGetCryptProv**](pvkgetcryptprov.md)                                             | Gets a handle to a CSP based on either a [*private key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) file name or a key container name.                                                                                                                                          |
| [**PvkPrivateKeyAcquireContextFromMemory**](pvkprivatekeyacquirecontextfrommemory.md) | Creates a temporary container in the CSP and loads a private key from memory into the container.                                                                                                                                                                                                         |
| [**PvkPrivateKeySave**](pvkprivatekeysave.md)                                         | Saves a private key and its corresponding [*public key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) to a specified file.                                                                                                                                                          |
| [**SignError**](signerror.md)                                                         | Calls [**GetLastError**](https://msdn.microsoft.com/en-us/library/ms679360(v=VS.85).aspx) and converts the return code to an **HRESULT**.                                                                                                                                                                                                              |



 

## Certificate Verification Functions

Certificates are verified using [*CTLs*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) or certificate chains. Functions are provided for both of these:

-   Verification Functions Using CTLs
-   Certificate Chain Verification Functions

### Verification Functions Using CTLs

These functions use CTLs in the verification process. Additional functions for working with CTLs can be found in Certificate Trust List Functions and Extended Property Functions.

The following functions use CTLs directly for verification.

| Function                                                         | Description                                  |
|------------------------------------------------------------------|----------------------------------------------|
| [**CertVerifyCTLUsage**](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifyctlusage)                 | Verifies the usage of a CTL.                 |
| [**CryptMsgEncodeAndSignCTL**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgencodeandsignctl)     | Encodes and signs a CTL as a message.        |
| [**CryptMsgGetAndVerifySigner**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetandverifysigner) | Retrieves and verifies a CTL from a message. |
| [**CryptMsgSignCTL**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgsignctl)                       | Signs a message that contains a CTL.         |



 

### Certificate Chain Verification Functions

Certificate chains are built to provide trust information about individual certificates.

| Function Name                                                                                                    | Description                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertCreateCertificateChainEngine**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatecertificatechainengine)                                     | Creates a new, nondefault chain engine for an application.                                                                                                                                                          |
| [**CertCreateCTLEntryFromCertificateContextProperties**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatectlentryfromcertificatecontextproperties) | Creates a CTL entry whose attributes are the certificate context's properties.                                                                                                                                      |
| [**CertDuplicateCertificateChain**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatecertificatechain)                                           | Duplicates a certificate chain by incrementing the chain's [*reference count*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) and returning a pointer to the chain.                    |
| [**CertFindChainInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindchaininstore)                                                             | Finds the first, or next, certificate chain context in a store.                                                                                                                                                     |
| [**CertFreeCertificateChain**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatechain)                                                     | Frees a certificate chain by reducing its reference count.                                                                                                                                                          |
| [**CertFreeCertificateChainEngine**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatechainengine)                                         | Frees a nondefault certificate chain engine.                                                                                                                                                                        |
| [**CertFreeCertificateChainList**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatechainlist)                                             | Frees the array of pointers to chain contexts.                                                                                                                                                                      |
| [**CertGetCertificateChain**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcertificatechain)                                                       | Builds a chain context starting from an end certificate and going back to a trusted [*root certificate*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx), if possible.                |
| [**CertIsValidCRLForCertificate**](/windows/desktop/api/Wincrypt/nf-wincrypt-certisvalidcrlforcertificate)                                             | Checks a [*CRL*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) to determine whether it would include a specific certificate if that certificate were revoked. |
| [**CertSetCertificateContextPropertiesFromCTLEntry**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcertificatecontextpropertiesfromctlentry)       | Sets properties on the certificate context using the attributes in the CTL entry.                                                                                                                                   |
| [**CertVerifyCertificateChainPolicy**](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifycertificatechainpolicy)                                     | Checks a certificate chain to verify its validity, including its compliance with any specified validity policy criteria.                                                                                            |



 

## Message Functions

[*CryptoAPI*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) message functions consist of two groups of functions: low-level message functions and [*simplified message functions*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx).

Low-level message functions create and work directly with PKCS \#7 messages. These functions encode PKCS \#7 data for transmission and decode PKCS \#7 data received. They also decrypt and verify the signatures of received messages. For an overview of the PKCS \#7 standard and low-level messages, see [Low-level Messages](low-level-messages.md).

Simplified message functions are at a higher level and wrap several low-level message functions and certificate functions into single functions that perform a specific task in a specific manner. These functions reduce the number of function calls needed to accomplish a task, thereby simplifying CryptoAPI use. For an overview of simplified messages, see [Simplified Messages](simplified-messages.md).

-   Low-level Message Functions
-   Simplified Message Functions

### Low-level Message Functions

Low-level message functions provide the functionality necessary to encode data for transmission and to decode PKCS \#7 messages received. Functionality is also provided to decrypt and verify the signatures of received messages. Use of these low-level message functions in most applications is not recommended. For most applications, the use of Simplified Message Functions, which wrap several low-level message functions into a single function call, is preferred.

| Function                                                                                   | Description                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptMsgCalculateEncodedLength**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgcalculateencodedlength)                   | Calculates the length of an encoded cryptographic message.                                                                                                                                                                     |
| [**CryptMsgClose**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgclose)                                                     | Closes a handle of a cryptographic message.                                                                                                                                                                                    |
| [**CryptMsgControl**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgcontrol)                                                 | Performs a special control function after the final [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate) of an encoded or decoded cryptographic message.                                                                                   |
| [**CryptMsgCountersign**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgcountersign)                                         | Countersigns an already existing signature in a message.                                                                                                                                                                       |
| [**CryptMsgCountersignEncoded**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgcountersignencoded)                           | Countersigns an already existing signature (encoded SignerInfo, as defined by PKCS \#7).                                                                                                                                       |
| [**CryptMsgDuplicate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgduplicate)                                             | Duplicates a cryptographic message handle by incrementing the [*reference count*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx). The reference count keeps track of the lifetime of the message. |
| [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam)                                               | Acquires a parameter after encoding or decoding a cryptographic message.                                                                                                                                                       |
| [**CryptMsgOpenToDecode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentodecode)                                       | Opens a cryptographic message for decoding.                                                                                                                                                                                    |
| [**CryptMsgOpenToEncode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentoencode)                                       | Opens a cryptographic message for encoding.                                                                                                                                                                                    |
| [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate)                                                   | Updates the contents of a cryptographic message.                                                                                                                                                                               |
| [**CryptMsgVerifyCountersignatureEncoded**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgverifycountersignatureencoded)     | Verifies a [*countersignature*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) in terms of the SignerInfo structure (as defined by PKCS \#7).                                                   |
| [**CryptMsgVerifyCountersignatureEncodedEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgverifycountersignatureencodedex) | Verifies that the *pbSignerInfoCounterSignature* parameter contains the encrypted [*hash*](https://msdn.microsoft.com/en-us/library/ms721586(v=VS.85).aspx) of the **encryptedDigest** field of the *pbSignerInfo* parameter structure.   |



 

### Simplified Message Functions

[*Simplified message functions*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) wrap Low-level Message Functions into a single function to accomplish a specified task.

| Function                                                                               | Description                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptDecodeMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodemessage)                                       | Decodes a cryptographic message.                                                                                                                                                                                                                                             |
| [**CryptDecryptAndVerifyMessageSignature**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecryptandverifymessagesignature) | Decrypts the specified message, and verifies the signer.                                                                                                                                                                                                                     |
| [**CryptDecryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecryptmessage)                                     | Decrypts the specified message.                                                                                                                                                                                                                                              |
| [**CryptEncryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencryptmessage)                                     | Encrypts the message for the recipient or recipients.                                                                                                                                                                                                                        |
| [**CryptGetMessageCertificates**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetmessagecertificates)                     | Returns the [*certificate store*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) that contains the message's certificates and [*CRLs*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx). |
| [**CryptGetMessageSignerCount**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetmessagesignercount)                       | Returns the count of signers in the signed message.                                                                                                                                                                                                                          |
| [**CryptHashMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashmessage)                                           | Creates a hash of the message.                                                                                                                                                                                                                                               |
| [**CryptSignAndEncryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignandencryptmessage)                       | Signs the message, and then encrypts it for the recipient or recipients.                                                                                                                                                                                                     |
| [**CryptSignMessageWithKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignmessagewithkey)                             | Signs a message using a CSP's private key specified in the parameters to the function.                                                                                                                                                                                       |
| [**CryptSignMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignmessage)                                           | Signs the message.                                                                                                                                                                                                                                                           |
| [**CryptVerifyDetachedMessageHash**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifydetachedmessagehash)               | Verifies a hashed message that contains a detached hash.                                                                                                                                                                                                                     |
| [**CryptVerifyDetachedMessageSignature**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifydetachedmessagesignature)     | Verifies a signed message that contains a detached signature or signatures.                                                                                                                                                                                                  |
| [**CryptVerifyMessageHash**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifymessagehash)                               | Verifies a hashed message.                                                                                                                                                                                                                                                   |
| [**CryptVerifyMessageSignature**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifymessagesignature)                     | Verifies a signed message.                                                                                                                                                                                                                                                   |
| [**CryptVerifyMessageSignatureWithKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifymessagesignaturewithkey)       | Verifies a signed message's signature by using specified public key information.                                                                                                                                                                                             |



 

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
<td>[<strong>CertCompareCertificate</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certcomparecertificate)</td>
<td>Compares two certificates to determine whether they are identical.</td>
</tr>
<tr class="even">
<td>[<strong>CertCompareCertificateName</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certcomparecertificatename)</td>
<td>Compares two certificate names to determine whether they are identical.</td>
</tr>
<tr class="odd">
<td>[<strong>CertCompareIntegerBlob</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certcompareintegerblob)</td>
<td>Compares two integer [<em>BLOBs</em>](https://msdn.microsoft.com/en-us/library/ms721569(v=VS.85).aspx).</td>
</tr>
<tr class="even">
<td>[<strong>CertComparePublicKeyInfo</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certcomparepublickeyinfo)</td>
<td>Compares two [<em>public keys</em>](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) to determine whether they are identical.</td>
</tr>
<tr class="odd">
<td>[<strong>CertFindAttribute</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindattribute)</td>
<td>Finds the first attribute identified by its [<em>object identifier</em>](https://msdn.microsoft.com/en-us/library/ms721599(v=VS.85).aspx) (OID).</td>
</tr>
<tr class="even">
<td>[<strong>CertFindExtension</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindextension)</td>
<td>Finds the first extension identified by its OID.</td>
</tr>
<tr class="odd">
<td>[<strong>CertFindRDNAttr</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindrdnattr)</td>
<td>Finds the first [<em>RDN</em>](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) attribute identified by its OID in the name list of the <em>Relative Distinguished Names</em>.</td>
</tr>
<tr class="even">
<td>[<strong>CertGetIntendedKeyUsage</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetintendedkeyusage)</td>
<td>Acquires the intended key usage bytes from the certificate.</td>
</tr>
<tr class="odd">
<td>[<strong>CertGetPublicKeyLength</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetpublickeylength)</td>
<td>Acquires the public/private key's bit length from the [<em>public key BLOB</em>](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx).</td>
</tr>
<tr class="even">
<td>[<strong>CertIsRDNAttrsInCertificateName</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certisrdnattrsincertificatename)</td>
<td>Compares the attributes in the [<em>certificate name</em>](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) with the specified [<strong>CERT_RDN</strong>](/windows/desktop/api/Wincrypt/ns-wincrypt-_cert_rdn) to determine whether all attributes are included there.</td>
</tr>
<tr class="odd">
<td>[<strong>CertIsStrongHashToSign</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certisstronghashtosign)</td>
<td>Determines whether the specified hash algorithm and the public key in the signing certificate can be used to perform strong signing.</td>
</tr>
<tr class="even">
<td>[<strong>CertVerifyCRLRevocation</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifycrlrevocation)</td>
<td>Verifies that the subject certificate is not on the [<em>certificate revocation list</em>](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CRL).</td>
</tr>
<tr class="odd">
<td>[<strong>CertVerifyCRLTimeValidity</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifycrltimevalidity)</td>
<td>Verifies the time validity of a CRL.</td>
</tr>
<tr class="even">
<td>[<strong>CertVerifyRevocation</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifyrevocation)</td>
<td>Verifies that the subject certificate is not on the CRL.</td>
</tr>
<tr class="odd">
<td>[<strong>CertVerifyTimeValidity</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifytimevalidity)</td>
<td>Verifies the time validity of a certificate.</td>
</tr>
<tr class="even">
<td>[<strong>CertVerifyValidityNesting</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifyvaliditynesting)</td>
<td>Verifies that the subject's time validity nests within the issuer's time validity.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptExportPKCS8</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpkcs8)</td>
<td>This function is superseded by the [<strong>CryptExportPKCS8Ex</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpkcs8ex) function.</td>
</tr>
<tr class="even">
<td>[<strong>CryptExportPKCS8Ex</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpkcs8ex)</td>
<td>Exports the private key in PKCS #8 format.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptExportPublicKeyInfo</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpublickeyinfo)</td>
<td>Exports the public key information associated with the provider's corresponding private key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptExportPublicKeyInfoEx</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpublickeyinfoex)</td>
<td>Exports the public key information associated with the provider's corresponding private key. This function differs from [<strong>CryptExportPublicKeyInfo</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpublickeyinfo) in that the user can specify the public key algorithm, thereby overriding the default provided by the CSP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptExportPublicKeyInfoFromBCryptKeyHandle</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpublickeyinfofrombcryptkeyhandle)</td>
<td>Exports the public key info associated with a provider's corresponding private key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptFindCertificateKeyProvInfo</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptfindcertificatekeyprovinfo)</td>
<td>Enumerates the cryptographic providers and their [<em>key containers</em>](https://msdn.microsoft.com/en-us/library/ms721590(v=VS.85).aspx) to find the private key that corresponds to a certificate's public key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptFindLocalizedName</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptfindlocalizedname)</td>
<td>Finds the localized name for a specified name, for example, finds the localized name for the store name of the Root system.</td>
</tr>
<tr class="even">
<td>[<strong>CryptHashCertificate</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashcertificate)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes the encoded content.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptHashCertificate2</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashcertificate2)</td>
<td>Hashes a block of data by using a Cryptography API: Next Generation (CNG) hash provider.</td>
</tr>
<tr class="even">
<td>[<strong>CryptHashPublicKeyInfo</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashpublickeyinfo)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Computes the hash of the encoded public key information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptHashToBeSigned</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashtobesigned)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Computes the hash of the &quot;to be signed&quot; information in the encoded signed content ([<strong>CERT_SIGNED_CONTENT_INFO</strong>](/windows/desktop/api/Wincrypt/ns-wincrypt-_cert_signed_content_info)).</td>
</tr>
<tr class="even">
<td>[<strong>CryptImportPKCS8</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpkcs8)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Imports the [<em>private key</em>](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) in PKCS #8 format to a [<em>cryptographic service provider</em>](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CSP).</td>
</tr>
<tr class="odd">
<td>[<strong>CryptImportPublicKeyInfo</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpublickeyinfo)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Converts and imports public key information into the provider, and returns a handle of the public key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptImportPublicKeyInfoEx</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpublickeyinfoex)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Converts and imports the public key information into the provider, and returns a handle of the public key. Additional parameters (over those specified by [<strong>CryptImportPublicKeyInfo</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpublickeyinfo)) that can be used to override defaults are provided to supplement [<strong>CERT_PUBLIC_KEY_INFO</strong>](/windows/desktop/api/Wincrypt/ns-wincrypt-_cert_public_key_info).</td>
</tr>
<tr class="odd">
<td>[<strong>CryptImportPublicKeyInfoEx2</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpublickeyinfoex2)</td>
<td>Imports a public key into a CNG asymmetric provider.</td>
</tr>
<tr class="even">
<td>[<strong>CryptMemAlloc</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmemalloc)</td>
<td>Allocates memory for a buffer. This memory is used by all Crypt32.lib functions that return allocated buffers.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptMemFree</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmemfree)</td>
<td>Frees memory allocated by [<strong>CryptMemAlloc</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmemalloc) or [<strong>CryptMemRealloc</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmemrealloc).</td>
</tr>
<tr class="even">
<td>[<strong>CryptMemRealloc</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmemrealloc)</td>
<td>Frees memory currently allocated for a buffer, and allocates memory for a new buffer.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptQueryObject</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptqueryobject)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves information about the content of a BLOB or a file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSignAndEncodeCertificate</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignandencodecertificate)</td>
<td>Encodes the &quot;to be signed&quot; information, signs this encoded information, and encodes the resulting signed, encoded information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSignCertificate</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsigncertificate)</td>
<td>Signs the &quot;to be signed&quot; information in the encoded, signed content.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPAddProvider</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipaddprovider)</td>
<td>Adds a Subject Interface Package (SIP).</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPCreateIndirectData</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipcreateindirectdata)</td>
<td>Returns a [<strong>SIP_INDIRECT_DATA</strong>](/windows/desktop/api/Mssip/ns-mssip-sip_indirect_data_) structure that contains a [<em>hash</em>](https://msdn.microsoft.com/en-us/library/ms721586(v=VS.85).aspx) of the supplied [<strong>SIP_SUBJECTINFO</strong>](/windows/desktop/api/Mssip/ns-mssip-sip_subjectinfo_) structure, the digest algorithm, and an encoding attribute. The hash can be used as an indirect reference to the data.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPGetCaps</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipgetcaps)</td>
<td>Retrieves the capabilities of an SIP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPGetSignedDataMsg</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipgetsigneddatamsg)</td>
<td>Retrieves an Authenticode signature from the file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPLoad</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipload)</td>
<td>Loads the dynamic link library that implements a subject interface package and assigns appropriate library export functions to a [<strong>SIP_DISPATCH_INFO</strong>](/windows/desktop/api/Mssip/ns-mssip-sip_dispatch_info_) structure.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPPutSignedDataMsg</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipputsigneddatamsg)</td>
<td>Stores an Authenticode Signature in the target file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPRemoveProvider</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipremoveprovider)</td>
<td>Removes a SIP added by a previous call to the [<strong>CryptSIPAddProvider</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipaddprovider) function.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPRemoveSignedDataMsg</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipremovesigneddatamsg)</td>
<td>Removes a specified Authenticode signature.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPRetrieveSubjectGuid</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipretrievesubjectguid)</td>
<td>Retrieves a GUID based on the header information in a specified file.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPRetrieveSubjectGuidForCatalogFile</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipretrievesubjectguidforcatalogfile)</td>
<td>Retrieves the subject GUID associated with the specified file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPVerifyIndirectData</strong>](/windows/desktop/api/Mssip/nf-mssip-cryptsipverifyindirectdata)</td>
<td>Validates the indirect hashed data against the supplied subject.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUpdateProtectedState</strong>](/windows/desktop/api/Dpapi/nf-dpapi-cryptupdateprotectedstate)</td>
<td>Migrates the current user's master keys after the user's [<em>security identifier</em>](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) (SID) has changed.</td>
</tr>
<tr class="even">
<td>[<strong>CryptVerifyCertificateSignature</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifycertificatesignature)</td>
<td>Verifies the signature of a subject certificate or a [<em>CRL</em>](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) by using the public key information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptVerifyCertificateSignatureEx</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifycertificatesignatureex)</td>
<td>An extended version of [<strong>CryptVerifyCertificateSignature</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifycertificatesignature).</td>
</tr>
<tr class="even">
<td>[<strong>GetEncSChannel</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-getencschannel)</td>
<td>Stores the encrypted Schannel DLL contents in memory.</td>
</tr>
<tr class="odd">
<td>[<strong>pCryptSIPGetCaps</strong>](/windows/desktop/api/Mssip/nc-mssip-pcryptsipgetcaps)</td>
<td>Implemented by an SIP to report capabilities.</td>
</tr>
</tbody>
</table>



 

### Data Conversion Functions

The following CryptoAPI functions convert certificate structure members to different forms.

| Function                                           | Description                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAlgIdToOID**](/windows/desktop/api/Wincrypt/nf-wincrypt-certalgidtooid)           | Converts a CryptoAPI algorithm identifier (ALG\_ID) to an [*Abstract Syntax Notation One*](https://msdn.microsoft.com/en-us/library/ms721532(v=VS.85).aspx) (ASN.1) [*object identifier*](https://msdn.microsoft.com/en-us/library/ms721599(v=VS.85).aspx) (OID) string. |
| [**CertGetNameString**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetnamestringa)     | Acquires the subject or issuer name from a certificate, and converts it to a null-terminated character string.                                                                                                                                                                                                               |
| [**CertNameToStr**](/windows/desktop/api/Wincrypt/nf-wincrypt-certnametostra)             | Converts a certificate name [*BLOB*](https://msdn.microsoft.com/en-us/library/ms721569(v=VS.85).aspx) to a zero-terminated string.                                                                                                                                                                                                      |
| [**CertOIDToAlgId**](/windows/desktop/api/Wincrypt/nf-wincrypt-certoidtoalgid)           | Converts the ASN.1 Object Identifier string to the CSP algorithm identifier.                                                                                                                                                                                                                                                 |
| [**CertRDNValueToStr**](/windows/desktop/api/Wincrypt/nf-wincrypt-certrdnvaluetostra)     | Converts a Name Value to a null-terminated string.                                                                                                                                                                                                                                                                           |
| [**CertStrToName**](/windows/desktop/api/Wincrypt/nf-wincrypt-certstrtonamea)             | Converts a null-terminated [*X.500*](https://msdn.microsoft.com/en-us/library/ms721636(v=VS.85).aspx) string to an encoded certificate name.                                                                                                                                                                                          |
| [**CryptBinaryToString**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptbinarytostringa) | Converts a binary sequence into a formatted string.                                                                                                                                                                                                                                                                          |
| [**CryptFormatObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptformatobject)     | Formats encoded data, and returns a Unicode string.                                                                                                                                                                                                                                                                          |
| [**CryptStringToBinary**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptstringtobinarya) | Converts a formatted string to a binary sequence.                                                                                                                                                                                                                                                                            |



 

### Enhanced Key Usage Functions

The following functions deal with the [*enhanced key usage*](https://msdn.microsoft.com/en-us/library/ms721575(v=VS.85).aspx) (EKU) extension and the EKU extended property of certificates. The EKU extension and extended property specify and limit the valid uses of a certificate. The extensions are part of the certificate itself. They are set by the issuer of the certificate and are read-only. Certificate-extended properties are values associated with a certificate that can be set in an application.

| Function                                                                             | Description                                                                    |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**CertAddEnhancedKeyUsageIdentifier**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddenhancedkeyusageidentifier)       | Adds a usage identifier to a certificate's EKU property.                       |
| [**CertGetEnhancedKeyUsage**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetenhancedkeyusage)                           | Acquires, from a certificate, information about the EKU extension or property. |
| [**CertRemoveEnhancedKeyUsageIdentifier**](/windows/desktop/api/Wincrypt/nf-wincrypt-certremoveenhancedkeyusageidentifier) | Removes the usage identifier from a certificate's EKU extended property.       |
| [**CertSetEnhancedKeyUsage**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetenhancedkeyusage)                           | Sets the EKU property for a certificate.                                       |



 

### Key Identifier Functions

Key identifier functions allow the user to create, set, retrieve, or locate a key identifier or its properties.

A key identifier is the unique identifier of a [*public/private key pair*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx). It can be any unique identifier but is usually the 20-byte SHA1 hash of an encoded [**CERT\_PUBLIC\_KEY\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-_cert_public_key_info) structure. A key identifier can be obtained through the certificate's CERT\_KEY\_IDENTIFIER\_PROP\_ID. The key identifier allows the use of that [*key pair*](https://msdn.microsoft.com/en-us/library/ms721590(v=VS.85).aspx) to encrypt or decrypt messages without using the certificate.

Key identifiers are not associated with [*CRLs*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) or [*CTLs*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx).

A key identifier can have the same properties as a certificate context. For more information, see [**CertCreateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatecontext).

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
<td>[<strong>CryptCreateKeyIdentifierFromCSP</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcreatekeyidentifierfromcsp)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a key identifier from a CSP's [<em>public key BLOB</em>](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx).</td>
</tr>
<tr class="even">
<td>[<strong>CryptEnumKeyIdentifierProperties</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumkeyidentifierproperties)</td>
<td>Enumerates key identifiers and their properties.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGetKeyIdentifierProperty</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetkeyidentifierproperty)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Acquires a specific property from a specified key identifier.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSetKeyIdentifierProperty</strong>](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetkeyidentifierproperty)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Sets a property of a specified key identifier.</td>
</tr>
</tbody>
</table>



 

### OID Support Functions

These functions provide [*object identifier*](https://msdn.microsoft.com/en-us/library/ms721599(v=VS.85).aspx) (OID) support. These functions install, register, and dispatch to OID and encoding type-specific functions.

The following CryptoAPI functions use these OID support functions:

-   [**CryptEncodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobject)
-   [**CryptEncodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobjectex)
-   [**CryptDecodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobject)
-   [**CryptDecodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobjectex)
-   [**CertVerifyRevocation**](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifyrevocation)
-   [**CertOpenStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenstore)

For an overview of this process, see [Extending CryptoAPI Functionality](extending-cryptoapi-functionality.md).

The following functions work with OIDs.

| Function                                                                       | Description                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptEnumOIDFunction**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumoidfunction)                           | Enumerates the registered OID functions identified by their encoding type, function name, and OID.                                                                                                                 |
| [**CryptEnumOIDInfo**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumoidinfo)                                   | Enumerates the registered OID information identified by their group, and calls *pfnEnumOIDInfo* for matches.                                                                                                       |
| [**CryptFindOIDInfo**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptfindoidinfo)                                   | Uses the specified key and group to find OID information.                                                                                                                                                          |
| [**CryptFreeOIDFunctionAddress**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptfreeoidfunctionaddress)             | Releases the handle count that was incremented and returned by [**CryptGetOIDFunctionAddress**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetoidfunctionaddress) or [**CryptGetDefaultOIDFunctionAddress**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetdefaultoidfunctionaddress). |
| [**CryptGetDefaultOIDDllList**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetdefaultoiddlllist)                 | Acquires the list of registered default DLL entries for the specified function set and encoding type.                                                                                                              |
| [**CryptGetDefaultOIDFunctionAddress**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetdefaultoidfunctionaddress) | Either acquires the first or next installed default function, or loads the DLL that contains the default function.                                                                                                 |
| [**CryptGetOIDFunctionAddress**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetoidfunctionaddress)               | Searches the list of installed functions for an encoding type and OID match. If a match is not found there, the registry is searched for a match.                                                                  |
| [**CryptGetOIDFunctionValue**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetoidfunctionvalue)                   | Acquires the value for the specified encoding type, function name, OID, and value name.                                                                                                                            |
| [**CryptInitOIDFunctionSet**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptinitoidfunctionset)                     | Initializes and returns a handle of the OID function set identified by the function name supplied.                                                                                                                 |
| [**CryptInstallOIDFunctionAddress**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptinstalloidfunctionaddress)       | Installs a set of callable OID function addresses.                                                                                                                                                                 |
| [**CryptRegisterDefaultOIDFunction**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptregisterdefaultoidfunction)     | Registers the DLL that contains the default function to be called for the specified encoding type and function name.                                                                                               |
| [**CryptRegisterOIDFunction**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptregisteroidfunction)                   | Registers the DLL that contains the function to be called for the specified encoding type, function name, and OID.                                                                                                 |
| [**CryptRegisterOIDInfo**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptregisteroidinfo)                           | Registers the OID information specified in the [**CRYPT\_OID\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-_crypt_oid_info) structure, persisting it to the registry.                                                                                |
| [**CryptSetOIDFunctionValue**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetoidfunctionvalue)                   | Sets the value for the specified encoding type, function name, OID, and value name.                                                                                                                                |
| [**CryptUnregisterDefaultOIDFunction**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptunregisterdefaultoidfunction) | Removes the registration for the DLL that contains the default function to be called for the specified encoding type and function name.                                                                            |
| [**CryptUnregisterOIDFunction**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptunregisteroidfunction)               | Removes the registration for the DLL that contains the function to be called for the specified encoding type, function name, and OID.                                                                              |
| [**CryptUnregisterOIDInfo**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptunregisteroidinfo)                       | Removes the registration for the specified OID information.                                                                                                                                                        |



 

### Remote Object Retrieval Functions

The following functions allow the user to retrieve a Public Key Infrastructure (PKI) object, acquire the URL of a certificate, CTL, or CRL, or to extract a URL from an object.

| Function                                                     | Description                                                            |
|--------------------------------------------------------------|------------------------------------------------------------------------|
| [**CryptGetObjectUrl**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetobjecturl)               | Acquires the URL of the remote object from a certificate, CTL, or CRL. |
| [**CryptRetrieveObjectByUrl**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptretrieveobjectbyurla) | Retrieves the PKI object from a location specified by a URL.           |



 

### PFX Functions

The following functions support Personal Information Exchange (PFX) format [*BLOBs*](https://msdn.microsoft.com/en-us/library/ms721569(v=VS.85).aspx).

| Function                                             | Description                                                                                                                                                                                                                                                                  |
|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PFXExportCertStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-pfxexportcertstore)     | Exports from the referenced [*certificate store*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) the certificates and, if available, their associated [*private keys*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx). |
| [**PFXExportCertStoreEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-pfxexportcertstoreex) | Exports from the referenced certificate store the certificates and, if available, their associated private keys.                                                                                                                                                             |
| [**PFXImportCertStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-pfximportcertstore)     | Imports a PFX BLOB, and returns the handle of a store that contains certificates and any associated private keys.                                                                                                                                                            |
| [**PFXIsPFXBlob**](/windows/desktop/api/Wincrypt/nf-wincrypt-pfxispfxblob)                 | Attempts to decode the outer layer of a BLOB as a PFX packet.                                                                                                                                                                                                                |
| [**PFXVerifyPassword**](/windows/desktop/api/Wincrypt/nf-wincrypt-pfxverifypassword)       | Attempts to decode the outer layer of a BLOB as a PFX packet and to decrypt it with the given password.                                                                                                                                                                      |



 

## Certificate Services Backup and Restore Functions

Certificate Services includes functions for backing up and restoring the Certificate Services database. These Certificate Services backup and restore functions are contained in Certadm.dll. Unlike the other API elements associated with Certificate Services, these functions are not encapsulated in an object that can be used to call class methods. Instead, the backup and restore APIs are called by first loading the Certadm.dll library into memory by calling [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and then determining the address of the functions by calling [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx). When you have finished calling the Certificate Services backup and restore functions, call [**FreeLibrary**](https://msdn.microsoft.com/en-us/library/ms683152(v=VS.85).aspx) to free Certadm.dll resources from memory.

> [!Note]Backup and restore functions provided by Certadm.dll do not backup or restore the Certificate Service's [*private keys*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx). For information about backing up the Certificate Services private keys, see [Backing Up and Restoring the Certificate Services Private Key](backing-up-and-restoring-the-certificate-services-private-key.md).
>
> To call the backup and restore functions, you must have backup and restore [*privileges*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx). For details, see [Setting the Backup and Restore Privileges](setting-the-backup-and-restore-privileges.md).

 

> [!Note]  
> If **CoInitializeEx** was previously called in the same thread used to call the Certificate Services backup and restore APIs, the COINIT\_APARTMENTTHREADED flag must have been passed to **CoInitializeEx**. That is, when using the same thread, you cannot call the Certificate Services backup and restore API if the thread has previously passed in the COINIT\_MULTITHREADED flag in a call to **CoInitializeEx**.

 

The Certificate Services Backup APIs are defined in Certbcli.h. However, when you create your program, use Certsrv.h as the include file.

The following APIs are exported by Certadm.dll.

| Function                                                                         | Description                                                                                                           |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**CertSrvBackupClose**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackupclose)                                 | Closes an opened file.                                                                                                |
| [**CertSrvBackupEnd**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackupend)                                     | Ends a backup session.                                                                                                |
| [**CertSrvBackupFree**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackupfree)                                   | Frees a buffer allocated by the backup and restore APIs.                                                              |
| [**CertSrvBackupGetBackupLogs**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackupgetbackuplogsw)                 | Returns a list of log files that need to be backed up.                                                                |
| [**CertSrvBackupGetDatabaseNames**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackupgetdatabasenamesw)           | Returns a list of database files that need to be backed up.                                                           |
| [**CertSrvBackupGetDynamicFileList**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackupgetdynamicfilelistw)       | Retrieves the list of Certificate Services dynamic file names that need to be backed up for the given backup context. |
| [**CertSrvBackupOpenFile**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackupopenfilew)                           | Opens a file in preparation for backing it up.                                                                        |
| [**CertSrvBackupPrepare**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackuppreparew)                             | Prepares the database for the online backup.                                                                          |
| [**CertSrvBackupRead**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackupread)                                   | Reads the contents of an opened file.                                                                                 |
| [**CertSrvBackupTruncateLogs**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackuptruncatelogs)                   | Truncates the log files.                                                                                              |
| [**CertSrvIsServerOnline**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvisserveronlinew)                           | Determines whether a Certificate Services server is online (actively running).                                        |
| [**CertSrvRestoreEnd**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoreend)                                   | Ends a restore session.                                                                                               |
| [**CertSrvRestoreGetDatabaseLocations**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoregetdatabaselocationsw) | Retrieves database locations (used for both backup and restore scenarios).                                            |
| [**CertSrvRestorePrepare**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestorepreparew)                           | Begins a restore session.                                                                                             |
| [**CertSrvRestoreRegister**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoreregisterw)                         | Registers a restore operation.                                                                                        |
| [**CertSrvRestoreRegisterComplete**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoreregistercomplete)         | Completes a previously registered restore operation.                                                                  |
| [**CertSrvRestoreRegisterThroughFile**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoreregisterthroughfile)   | Registers a restore operation.                                                                                        |
| [**CertSrvServerControl**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvservercontrolw)                             | Sends a control command to the Certificate Services instance.                                                         |



 

## Callback Functions

The callback functions in this section are used to register or install application-defined [*certificate store*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) providers and to provide related functionality through callback functions. Callback functions are implemented by an application and are called by [*CryptoAPI*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) functions. Callback functions enable the application to control, in part, the way that CryptoAPI functions manipulate data.

| Callback function                                                                                                        | Use                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertChainFindByIssuerCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_chain_find_by_issuer_callback)                                                   | An application-defined callback function that allows the application to filter certificates that might be added to the certificate chain.                                                                                                                                                                                                     |
| [**CertDllOpenStoreProv**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_dll_open_store_prov_func)                                                                     | Defines the store provider open function.                                                                                                                                                                                                                                                                                                     |
| [**CertEnumPhysicalStoreCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_enum_physical_store)                                                   | Callback function used by the [**CertEnumPhysicalStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumphysicalstore) function to format and present information on each physical store found.                                                                                                                                                                                 |
| [**CertEnumSystemStoreCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_enum_system_store)                                                       | Callback function used by the [**CertEnumSystemStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumsystemstore) function to format and present information on each physical store found.                                                                                                                                                                                     |
| [**CertEnumSystemStoreLocationCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_enum_system_store_location)                                       | Callback function used by the [**CertEnumSystemStoreLocation**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumsystemstorelocation) function to format and present information on each physical store found.                                                                                                                                                                     |
| [**CertStoreProvCloseCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_close)                                                         | Determines what happens when an open store's [*reference count*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx) becomes zero.                                                                                                                                                                                    |
| [**CertStoreProvControl**](https://msdn.microsoft.com/en-us/library/Aa377033(v=VS.85).aspx)                                                                     | Allows an application to be notified when there is a difference between the contents of a cached store in use and the contents of that store as it is persisted to storage.                                                                                                                                                                   |
| [**CertStoreProvDeleteCertCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_delete_cert)                                               | Determines actions to be taken before a certificate is deleted from a certificate store.                                                                                                                                                                                                                                                      |
| [**CertStoreProvDeleteCRLCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_delete_crl)                                                 | Determines actions to be taken before a [*certificate revocation list*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CRL) is deleted from a certificate store.                                                                                                                        |
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
| [**CertStoreProvReadCertCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_read_cert)                                                   | Currently not used but might be exported to future CSPs.                                                                                                                                                                                                                                                                                      |
| [**CertStoreProvReadCRLCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_read_crl)                                                     | Currently not used but might be exported to future CSPs.                                                                                                                                                                                                                                                                                      |
| [**CertStoreProvReadCTL**](https://msdn.microsoft.com/en-us/library/Aa377153(v=VS.85).aspx)                                                                     | Read the provider's copy of the CTL context, and, if it exists, create a new CTL context.                                                                                                                                                                                                                                                     |
| [**CertStoreProvSetCertPropertyCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_set_cert_property)                                     | Determines actions to be taken before a call to [**CertSetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcertificatecontextproperty) or [**CertGetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty).                                                                                                                             |
| [**CertStoreProvSetCRLPropertyCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_set_crl_property)                                       | Determines actions to be taken before a call to [**CertSetCRLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcrlcontextproperty) or [**CertGetCRLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcrlcontextproperty).                                                                                                                                                             |
| [**CertStoreProvSetCTLProperty**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_set_ctl_property)                                                       | Determines whether a property can be set on a CTL.                                                                                                                                                                                                                                                                                            |
| [**CertStoreProvWriteCertCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_write_cert)                                                 | Determines actions to be taken before adding a certificate to a store.                                                                                                                                                                                                                                                                        |
| [**CertStoreProvWriteCRLCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_write_crl)                                                   | Determines actions to be taken before adding a CRL to a store.                                                                                                                                                                                                                                                                                |
| [**CertStoreProvWriteCTL**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_write_ctl)                                                                   | Determines whether a CTL can be added to the store.                                                                                                                                                                                                                                                                                           |
| [**CRYPT\_ENUM\_KEYID\_PROP**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_enum_keyid_prop)                                                                | Callback function used by the [**CryptEnumKeyIdentifierProperties**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumkeyidentifierproperties) function.                                                                                                                                                                                                                          |
| [**CRYPT\_ENUM\_OID\_FUNCTION**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_enum_oid_func)                                                            | Callback function used by the [**CryptEnumOIDFunction**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumoidfunction) function.                                                                                                                                                                                                                                                  |
| [**CRYPT\_ENUM\_OID\_INFO**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_enum_oid_info)                                                                    | Callback function used by the [**CryptEnumOIDInfo**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumoidinfo) function.                                                                                                                                                                                                                                                          |
| [**CryptGetSignerCertificateCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_get_signer_certificate)                                           | Callback function used with the [**CRYPT\_VERIFY\_MESSAGE\_PARA**](/windows/desktop/api/Wincrypt/ns-wincrypt-_crypt_verify_message_para) structure to get and verify a message signer's certificate.                                                                                                                                                                                 |
| [**PCRYPT\_DECRYPT\_PRIVATE\_KEY\_FUNC**](https://msdn.microsoft.com/en-us/library/Aa387040(v=VS.85).aspx)                                           | Callback function used by the [**CryptImportPKCS8**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpkcs8) function.                                                                                                                                                                                                                                                          |
| [**PCRYPT\_ENCRYPT\_PRIVATE\_KEY\_FUNC**](https://msdn.microsoft.com/en-us/library/Aa387041(v=VS.85).aspx)                                           | Callback function used when creating the [**CRYPT\_ENCRYPTED\_PRIVATE\_KEY\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-_crypt_encrypted_private_key_info) structure.                                                                                                                                                                                                          |
| [**PCRYPT\_RESOLVE\_HCRYPTPROV\_FUNC**](https://msdn.microsoft.com/en-us/library/Aa387042(v=VS.85).aspx)                                              | Callback function used by the [**CryptImportPKCS8**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpkcs8) function.                                                                                                                                                                                                                                                          |
| [**PFN\_CDF\_PARSE\_ERROR\_CALLBACK**](https://msdn.microsoft.com/en-us/library/Bb410248(v=VS.85).aspx)                                                 | A user-defined function called for Catalog Definition Function errors while parsing a catalog definition file (CDF).                                                                                                                                                                                                                          |
| [**PFN\_CERT\_CREATE\_CONTEXT\_SORT\_FUNC**](https://msdn.microsoft.com/en-us/library/Aa818336(v=VS.85).aspx)                                      | Called for each sorted context entry when a context is created.                                                                                                                                                                                                                                                                               |
| [**PFN\_CMSG\_CNG\_IMPORT\_CONTENT\_ENCRYPT\_KEY**](https://msdn.microsoft.com/en-us/library/Aa387048(v=VS.85).aspx)                         | A CNG [*object identifier*](https://msdn.microsoft.com/en-us/library/ms721599(v=VS.85).aspx) (OID) installable function for import of an already decrypted content encryption key (CEK).                                                                                                                                       |
| [**PFN\_CMSG\_CNG\_IMPORT\_KEY\_AGREE**](https://msdn.microsoft.com/en-us/library/Aa387294(v=VS.85).aspx)                                              | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_CNG\_IMPORT\_KEY\_TRANS**](https://msdn.microsoft.com/en-us/library/Aa387295(v=VS.85).aspx)                                              | A CNG OID installable function for import and [*decryption*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx) of a key-transport-recipient, encrypted, content [*encryption*](https://msdn.microsoft.com/en-us/library/ms721575(v=VS.85).aspx) key (CEK).                                                                   |
| [**PFN\_CMSG\_EXPORT\_KEY\_AGREE**](https://msdn.microsoft.com/en-us/library/Bb931386(v=VS.85).aspx)                                                       | Encrypts and exports the content encryption key for a key agreement recipient of an enveloped message.                                                                                                                                                                                                                                        |
| [**PFN\_CMSG\_EXPORT\_KEY\_TRANS**](https://msdn.microsoft.com/en-us/library/Bb931387(v=VS.85).aspx)                                                       | Encrypts and exports the content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                        |
| [**PFN\_CMSG\_EXPORT\_MAIL\_LIST**](https://msdn.microsoft.com/en-us/library/Bb931388(v=VS.85).aspx)                                                       | Encrypts and exports the content encryption key for a mailing list recipient of an enveloped message.                                                                                                                                                                                                                                         |
| [**PFN\_CMSG\_GEN\_CONTENT\_ENCRYPT\_KEY**](https://msdn.microsoft.com/en-us/library/Bb931389(v=VS.85).aspx)                                        | Generates the [*symmetric key*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) used to encrypt content for an enveloped message.                                                                                                                                                                                     |
| [**PFN\_CMSG\_IMPORT\_KEY\_AGREE**](https://msdn.microsoft.com/en-us/library/Bb931392(v=VS.85).aspx)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_IMPORT\_KEY\_TRANS**](https://msdn.microsoft.com/en-us/library/Bb931393(v=VS.85).aspx)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_IMPORT\_MAIL\_LIST**](https://msdn.microsoft.com/en-us/library/Bb931394(v=VS.85).aspx)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CRYPT\_EXPORT\_PUBLIC\_KEY\_INFO\_EX2\_FUNC**](https://msdn.microsoft.com/en-us/library/Aa387297(v=VS.85).aspx)                    | Called by [**CryptExportPublicKeyInfoEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpublickeyinfoex) to export a public key BLOB and encode it.                                                                                                                                                                                                                         |
| [**PFN\_CRYPT\_EXTRACT\_ENCODED\_SIGNATURE\_PARAMETERS\_FUNC**](https://msdn.microsoft.com/en-us/library/Aa387298(v=VS.85).aspx) | Called to decode and return the hash algorithm identifier and optionally the signature parameters.                                                                                                                                                                                                                                            |
| [**PFN\_CRYPT\_SIGN\_AND\_ENCODE\_HASH\_FUNC**](https://msdn.microsoft.com/en-us/library/Aa387299(v=VS.85).aspx)                                 | Called to sign and encode a computed hash.                                                                                                                                                                                                                                                                                                    |
| [**PFN\_CRYPT\_VERIFY\_ENCODED\_SIGNATURE\_FUNC**](https://msdn.microsoft.com/en-us/library/Aa387301(v=VS.85).aspx)                          | Called to decrypt an encoded signature and compare it to a computed hash.                                                                                                                                                                                                                                                                     |
| [**PFN\_IMPORT\_PUBLIC\_KEY\_INFO\_EX2\_FUNC**](https://msdn.microsoft.com/en-us/library/Aa387310(v=VS.85).aspx)                                 | Called by [**CryptImportPublicKeyInfoEx2**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpublickeyinfoex2) to decode the [*public key algorithm*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) identifier, load the algorithm provider, and import the [*key pair*](https://msdn.microsoft.com/en-us/library/ms721590(v=VS.85).aspx). |
| [**PFNCCERTDISPLAYPROC**](pfnccertdisplayproc.md)                                                                       | A user-defined callback function that allows the caller of the [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md) function to handle the display of certificates that the user selects to view.                                                                                                                               |
| [**PFNCMFILTERPROC**](/windows/desktop/api/CryptDlg/nc-cryptdlg-pfncmfilterproc)                                                                               | Filters each certificate to decide if it will appear in the certificate selection dialog box displayed by the [**CertSelectCertificate**](https://msdn.microsoft.com/en-us/library/Aa376568(v=VS.85).aspx) function.                                                                                                                                                                |
| [**PFNCMHOOKPROC**](/windows/desktop/api/CryptDlg/nc-cryptdlg-pfncmhookproc)                                                                                   | Called before messages are processed by the certificate selection dialog box produced by the [**CertSelectCertificate**](https://msdn.microsoft.com/en-us/library/Aa376568(v=VS.85).aspx) function.                                                                                                                                                                                 |



 

## Catalog Definition Functions

These functions are used to create a catalog. All of these functions are called by [MakeCat](makecat.md).

| Function                                                                           | Description                                                                                                               |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**CryptCATCDFClose**](/windows/desktop/api/Mscat/nf-mscat-cryptcatcdfclose)                                       | Closes a catalog definition file and frees the memory for the corresponding [**CRYPTCATCDF**](/windows/desktop/api/Mscat/ns-mscat-cryptcatcdf_) structure. |
| [**CryptCATCDFEnumAttributesWithCDFTag**](cryptcatcdfenumattributeswithcdftag.md) | Enumerates the attributes of member files in the **CatalogFiles** section of a CDF.                                       |
| [**CryptCATCDFEnumCatAttributes**](/windows/desktop/api/Mscat/nf-mscat-cryptcatcdfenumcatattributes)               | Enumerates catalog-level attributes within the **CatalogHeader** section of a CDF.                                        |
| [**CryptCATCDFEnumMembersByCDFTagEx**](cryptcatcdfenummembersbycdftagex.md)       | Enumerates the individual file members in the **CatalogFiles** section of a CDF.                                          |
| [**CryptCATCDFOpen**](/windows/desktop/api/Mscat/nf-mscat-cryptcatcdfopen)                                         | Opens an existing CDF for reading and initializes a [**CRYPTCATCDF**](/windows/desktop/api/Mscat/ns-mscat-cryptcatcdf_) structure.                         |



 

## Catalog Functions

These functions are used to manage a catalog.

| Function                                                                             | Description                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptCATAdminAcquireContext**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminacquirecontext)                   | Acquires a handle to a catalog administrator context. This handle can be used by subsequent calls to the [**CryptCATAdminAddCatalog**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminaddcatalog), [**CryptCATAdminEnumCatalogFromHash**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminenumcatalogfromhash), and [**CryptCATAdminRemoveCatalog**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminremovecatalog) functions. |
| [**CryptCATAdminAcquireContext2**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminacquirecontext2)                 | Acquires a handle to a catalog administrator context for a given hash algorithm and hash policy.                                                                                                                                                                                                                                   |
| [**CryptCATAdminAddCatalog**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminaddcatalog)                           | Adds a catalog to the catalog database.                                                                                                                                                                                                                                                                                            |
| [**CryptCATAdminCalcHashFromFileHandle**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadmincalchashfromfilehandle)   | Calculates the hash for a file.                                                                                                                                                                                                                                                                                                    |
| [**CryptCATAdminCalcHashFromFileHandle2**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadmincalchashfromfilehandle2) | Calculates the hash for a file by using the specified algorithm.                                                                                                                                                                                                                                                                   |
| [**CryptCATAdminEnumCatalogFromHash**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminenumcatalogfromhash)         | Enumerates the catalogs that contain a specified hash.                                                                                                                                                                                                                                                                             |
| [**CryptCATAdminReleaseCatalogContext**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminreleasecatalogcontext)     | Releases a handle to a catalog context previously returned by the [**CryptCATAdminAddCatalog**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminaddcatalog) function.                                                                                                                                                                                             |
| [**CryptCATAdminReleaseContext**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminreleasecontext)                   | Releases the handle previously assigned by the [**CryptCATAdminAcquireContext**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminacquirecontext) function.                                                                                                                                                                                                        |
| [**CryptCATAdminRemoveCatalog**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminremovecatalog)                     | Deletes a catalog file and removes that catalog's entry from the Windows catalog database.                                                                                                                                                                                                                                         |
| [**CryptCATAdminResolveCatalogPath**](/windows/desktop/api/Mscat/nf-mscat-cryptcatadminresolvecatalogpath)           | Retrieves the fully qualified path of the specified catalog.                                                                                                                                                                                                                                                                       |
| [**CryptCATCatalogInfoFromContext**](/windows/desktop/api/Mscat/nf-mscat-cryptcatcataloginfofromcontext)             | Retrieves catalog information from a specified catalog context.                                                                                                                                                                                                                                                                    |
| [**CryptCATClose**](/windows/desktop/api/Mscat/nf-mscat-cryptcatclose)                                               | Closes a catalog handle opened previously by the [**CryptCATOpen**](/windows/desktop/api/Mscat/nf-mscat-cryptcatopen) function.                                                                                                                                                                                                                                    |
| [**CryptCATEnumerateAttr**](/windows/desktop/api/Mscat/nf-mscat-cryptcatenumerateattr)                               | Enumerates the attributes associated with a member of a catalog.                                                                                                                                                                                                                                                                   |
| [**CryptCATEnumerateCatAttr**](/windows/desktop/api/Mscat/nf-mscat-cryptcatenumeratecatattr)                         | Enumerates the attributes associated with a catalog.                                                                                                                                                                                                                                                                               |
| [**CryptCATEnumerateMember**](/windows/desktop/api/Mscat/nf-mscat-cryptcatenumeratemember)                           | Enumerates the members of a catalog.                                                                                                                                                                                                                                                                                               |
| [**CryptCATGetAttrInfo**](/windows/desktop/api/Mscat/nf-mscat-cryptcatgetattrinfo)                                   | Retrieves information about an attribute of a member of a catalog.                                                                                                                                                                                                                                                                 |
| [**CryptCATGetMemberInfo**](/windows/desktop/api/Mscat/nf-mscat-cryptcatgetmemberinfo)                               | Retrieves member information from the catalog's PKCS \#7. In addition to retrieving the member information for a specified reference tag, this function opens a member context.                                                                                                                                                    |
| [**CryptCATOpen**](/windows/desktop/api/Mscat/nf-mscat-cryptcatopen)                                                 | Opens a catalog, and returns a context handle to the open catalog.                                                                                                                                                                                                                                                                 |
| [**IsCatalogFile**](/windows/desktop/api/Mscat/nf-mscat-iscatalogfile)                                               | Retrieves a Boolean value that indicates whether the specified file is a catalog file.                                                                                                                                                                                                                                             |



 

## WinTrust Functions

The following functions are used to perform various trust operations.

| Function                                                                               | Description                                                                                                                                                          |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WintrustAddActionID**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustaddactionid)                                     | Adds a trust provider action to the user's system.                                                                                                                   |
| [**WintrustGetRegPolicyFlags**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustgetregpolicyflags)                         | Retrieves policy flags for a policy provider.                                                                                                                        |
| [**WintrustAddDefaultForUsage**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustadddefaultforusage)                       | Specifies the default usage identifier and callback information for a provider                                                                                       |
| [**WintrustGetDefaultForUsage**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustgetdefaultforusage)                       | Retrieves the default usage identifier and callback information.                                                                                                     |
| [**WintrustLoadFunctionPointers**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustloadfunctionpointers)                   | Loads function entry points for a specified action GUID.                                                                                                             |
| [**WintrustRemoveActionID**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustremoveactionid)                               | Removes an action added by the [**WintrustAddActionID**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustaddactionid) function.                                                                          |
| [**WintrustSetDefaultIncludePEPageHashes**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustsetdefaultincludepepagehashes) | Sets the default setting that determines whether page hashes are included when creating subject interface package (SIP) indirect data for portable executable files. |
| [**WintrustSetRegPolicyFlags**](/windows/desktop/api/Wintrust/nf-wintrust-wintrustsetregpolicyflags)                         | Sets policy flags for a policy provider.                                                                                                                             |
| [**WinVerifyTrust**](/windows/desktop/api/Wintrust/nf-wintrust-winverifytrust)                                               | Performs a trust verification action on a specified object.                                                                                                          |
| [**WinVerifyTrustEx**](/windows/desktop/api/Wintrust/nf-wintrust-winverifytrustex)                                           | Performs a trust verification action on a specified object and takes a pointer to a WINTRUST\_DATA structure.                                                        |
| [**WTHelperCertCheckValidSignature**](/windows/desktop/api/Wintrust/nf-wintrust-wthelpercertcheckvalidsignature)             | Checks whether a signature is valid.                                                                                                                                 |
| [**WTHelperCertFindIssuerCertificate**](wthelpercertfindissuercertificate.md)         | Finds an issuer certificate from the specified certificate stores that matches the specified subject certificate.                                                    |
| [**WTHelperCertIsSelfSigned**](/windows/desktop/api/Wintrust/nf-wintrust-wthelpercertisselfsigned)                           | Checks whether a certificate is self-signed.                                                                                                                         |
| [**WTHelperGetFileHash**](wthelpergetfilehash.md)                                     | Verifies the signature of a signed file and obtains the hash value and algorithm identifier for the file.                                                            |
| [**WTHelperGetProvCertFromChain**](/windows/desktop/api/Wintrust/nf-wintrust-wthelpergetprovcertfromchain)                   | Retrieves a trust provider certificate from the certificate chain.                                                                                                   |
| [**WTHelperGetProvPrivateDataFromChain**](/windows/desktop/api/Wintrust/nf-wintrust-wthelpergetprovprivatedatafromchain)     | Receives a [**CRYPT\_PROVIDER\_PRIVDATA**](/windows/desktop/api/Wintrust/ns-wintrust-_crypt_provider_privdata) structure from the chain by using the provider ID.                                           |
| [**WTHelperGetProvSignerFromChain**](/windows/desktop/api/Wintrust/nf-wintrust-wthelpergetprovsignerfromchain)               | Retrieves a signer or countersigner by index from the chain.                                                                                                         |
| [**WTHelperProvDataFromStateData**](/windows/desktop/api/Wintrust/nf-wintrust-wthelperprovdatafromstatedata)                 | Retrieves trust provider information from a specified handle.                                                                                                        |



 

## Object Locator Functions

The following callback functions can be implemented by a custom provider that is intended to be called by the Secure Channel (Schannel) security package to retrieve certificates.



| Function                                                                                                             | Description                                             |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FLUSH**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_flush)                      | Specifies that an object has changed.                   |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_GET**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_get)                          | Retrieves an object.                                    |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_RELEASE**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_release)                  | Releases the provider.                                  |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FREE\_PASSWORD**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_free_password)     | Releases the password used to encrypt a PFX byte array. |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FREE**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_free)                        | Releases the object returned by the provider.           |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FREE\_IDENTIFIER**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_free_identifier) | Releases memory for an object identifier.               |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_INITIALIZE**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_object_locator_provider_initialize)            | Initializes the provider.                               |



 

 

 




