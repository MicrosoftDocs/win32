---
description: Lists the functions provided by CryptoAPI.
ms.assetid: 9a65f73d-6f8c-4271-a2d0-d91ad952f9c6
title: Cryptography Functions
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

The cryptographic XML functions provide an API for creating and representing digital signatures by using XML formatted data. For information about XML formatted signatures, see the XML-Signature Syntax and Processing specification at <https://go.microsoft.com/fwlink/p/?linkid=139649>.



| Function                                                                          | Description                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**A\_SHAFinal**](a-shafinal.md)                                                 | Computes the final hash of the data entered by the MD5Update function.                                                                                                                                                                                                                                           |
| [**A\_SHAInit**](a-shainit.md)                                                   | Initiates the hashing of a stream of data.                                                                                                                                                                                                                                                                       |
| [**A\_SHAUpdate**](a-shaupdate.md)                                               | Adds data to a specified hash object.                                                                                                                                                                                                                                                                            |
| [**CryptXmlCreateReference**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlcreatereference)                        | Creates a reference to an XML signature.                                                                                                                                                                                                                                                                         |
| [**CryptXmlAddObject**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmladdobject)                                    | Adds the **Object** element to the Signature in the Document Context opened for encoding.                                                                                                                                                                                                                        |
| [**CryptXmlClose**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlclose)                                            | Closes a cryptographic XML object handle.                                                                                                                                                                                                                                                                        |
| [**CryptXmlDigestReference**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmldigestreference)                        | Used by an application to digest the resolved reference. This function applies transforms before updating the digest.                                                                                                                                                                                            |
| [**CryptXmlDllCloseDigest**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllclosedigest)                          | Frees the CRYPT\_XML\_DIGEST allocated by the [**CryptXmlDllCreateDigest**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllcreatedigest) function.                                                                                                                                                                                               |
| [**CryptXmlDllCreateDigest**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllcreatedigest)                        | Creates a digest object for the specified method.                                                                                                                                                                                                                                                                |
| [**CryptXmlDllCreateKey**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllcreatekey)                              | Parses the **KeyValue** element and creates a Cryptography API: Next Generation (CNG) BCrypt key handle to verify a signature.                                                                                                                                                                                   |
| [**CryptXmlDllDigestData**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldlldigestdata)                            | Puts data into the digest.                                                                                                                                                                                                                                                                                       |
| [**CryptXmlDllEncodeAlgorithm**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllencodealgorithm)                  | Encodes **SignatureMethod** or **DigestMethod** elements for agile algorithms with default parameters.                                                                                                                                                                                                           |
| [**CryptXmlDllEncodeKeyValue**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllencodekeyvalue)                    | Encodes a **KeyValue** element.                                                                                                                                                                                                                                                                                  |
| [**CryptXmlDllFinalizeDigest**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllfinalizedigest)                    | Retrieves the digest value.                                                                                                                                                                                                                                                                                      |
| [**CryptXmlDllGetAlgorithmInfo**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllgetalgorithminfo)                | Decodes the XML algorithm and returns information about the algorithm.                                                                                                                                                                                                                                           |
| [**CryptXmlDllGetInterface**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllgetinterface)                        | Retrieves a pointer to the cryptographic extension functions for the specified algorithm.                                                                                                                                                                                                                        |
| [**CryptXmlDllSignData**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllsigndata)                                | Signs data.                                                                                                                                                                                                                                                                                                      |
| [**CryptXmlDllVerifySignature**](/windows/win32/api/cryptxml/nc-cryptxml-cryptxmldllverifysignature)                  | Verifies a signature.                                                                                                                                                                                                                                                                                            |
| [**CryptXmlEncode**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlencode)                                          | Encodes signature data by using the supplied XML writer callback function.                                                                                                                                                                                                                                       |
| [**CryptXmlGetAlgorithmInfo**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgetalgorithminfo)                      | Decodes the CRYPT\_XML\_ALGORITHM structure and returns information about the algorithm.                                                                                                                                                                                                                         |
| [**CryptXmlGetDocContext**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgetdoccontext)                            | Returns the document context specified by the supplied handle.                                                                                                                                                                                                                                                   |
| [**CryptXmlGetReference**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgetreference)                              | Returns the **Reference** element specified by the supplied handle.                                                                                                                                                                                                                                              |
| [**CryptXmlGetSignature**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgetsignature)                              | Returns an XML **Signature** element.                                                                                                                                                                                                                                                                            |
| [**CryptXmlGetStatus**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgetstatus)                                    | Returns a [**CRYPT\_XML\_STATUS**](/windows/desktop/api/Cryptxml/ns-cryptxml-crypt_xml_status) structure that contains status information about the object specified by the supplied handle.                                                                                                                                                           |
| [**CryptXmlGetTransforms**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlgettransforms)                            | Returns information about the default transform chain engine.                                                                                                                                                                                                                                                    |
| [**CryptXmlImportPublicKey**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlimportpublickey)                        | Imports the public key specified by the supplied handle.                                                                                                                                                                                                                                                         |
| [**CryptXmlOpenToEncode**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlopentoencode)                              | Opens an XML digital signature to encode and returns a handle of the opened **Signature** element. The handle encapsulates a document context with a single [**CRYPT\_XML\_SIGNATURE**](/windows/desktop/api/Cryptxml/ns-cryptxml-crypt_xml_signature) structure and remains open until the [**CryptXmlClose**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlclose) function is called. |
| [**CryptXmlOpenToDecode**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlopentodecode)                              | Opens an XML digital signature to decode and returns the handle of the document context that encapsulates a [**CRYPT\_XML\_SIGNATURE**](/windows/desktop/api/Cryptxml/ns-cryptxml-crypt_xml_signature) structure. The document context can include one or more **Signature** elements.                                                                 |
| [**CryptXmlSetHMACSecret**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlsethmacsecret)                            | Sets the HMAC secret on the handle before calling the [**CryptXmlSign**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlsign) or [**CryptXmlVerify**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlverifysignature) function.                                                                                                                                                        |
| [**CryptXmlSign**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlsign)                                              | Creates a cryptographic signature of a **SignedInfo** element.                                                                                                                                                                                                                                                   |
| [**CryptXmlVerifySignature**](/windows/desktop/api/Cryptxml/nf-cryptxml-cryptxmlverifysignature)                        | Performs a cryptographic signature validation of a **SignedInfo** element.                                                                                                                                                                                                                                       |
| [*PFN\_CRYPT\_XML\_WRITE\_CALLBACK*](/windows/desktop/api/Cryptxml/nc-cryptxml-pfn_crypt_xml_write_callback)            | Creates a transform for a specified data provider.                                                                                                                                                                                                                                                               |
| [*PFN\_CRYPT\_XML\_CREATE\_TRANSFORM*](/windows/desktop/api/Cryptxml/nc-cryptxml-pfn_crypt_xml_create_transform)        | Writes cryptographic XML data.                                                                                                                                                                                                                                                                                   |
| [*PFN\_CRYPT\_XML\_DATA\_PROVIDER\_READ*](/windows/desktop/api/Cryptxml/nc-cryptxml-pfn_crypt_xml_data_provider_read)   | Reads cryptographic XML data.                                                                                                                                                                                                                                                                                    |
| [*PFN\_CRYPT\_XML\_DATA\_PROVIDER\_CLOSE*](/windows/desktop/api/Cryptxml/nc-cryptxml-pfn_crypt_xml_data_provider_close) | Releases the cryptographic XML data provider.                                                                                                                                                                                                                                                                    |
| [*PFN\_CRYPT\_XML\_ENUM\_ALG\_INFO*](/windows/desktop/api/Cryptxml/nc-cryptxml-pfn_crypt_xml_enum_alg_info)             | Enumerates predefined and registered [**CRYPT\_XML\_ALGORITHM\_INFO**](/windows/desktop/api/Cryptxml/ns-cryptxml-crypt_xml_algorithm_info) entries.                                                                                                                                                                                                    |



 

## Signer Functions

Provides functions to sign and time stamp data.



| Function                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SignerFreeSignerContext**](signerfreesignercontext.md) | Frees a [**SIGNER\_CONTEXT**](signer-context.md) structure allocated by a previous call to the [**SignerSignEx**](signersignex.md) function.                                                                                                                                                                                                                                                                      |
| [**SignError**](signerror.md)                             | Calls the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function and converts the return code to an **HRESULT**.                                                                                                                                                                                                                                                                                                            |
| [**SignerSign**](signersign.md)                           | Signs the specified file.                                                                                                                                                                                                                                                                                                                                                                                           |
| [**SignerSignEx**](signersignex.md)                       | Signs the specified file and returns a pointer to the signed data.                                                                                                                                                                                                                                                                                                                                                  |
| [**SignerSignEx2**](signersignex2.md)                     | Signs and time stamps the specified file, allowing multiple nested signatures.                                                                                                                                                                                                                                                                                                                                      |
| [**SignerTimeStamp**](signertimestamp.md)                 | Time stamps the specified subject. This function supports Authenticode time stamping. To perform X.509 Public Key Infrastructure (RFC 3161) time stamping, use the [**SignerTimeStampEx2**](signertimestampex2.md) function.                                                                                                                                                                                       |
| [**SignerTimeStampEx**](signertimestampex.md)             | Time stamps the specified subject and optionally returns a pointer to a [**SIGNER\_CONTEXT**](signer-context.md) structure that contains a pointer to a [*BLOB*](../secgloss/b-gly.md). This function supports Authenticode time stamping. To perform X.509 Public Key Infrastructure (RFC 3161) time stamping, use the [**SignerTimeStampEx2**](signertimestampex2.md) function. |
| [**SignerTimeStampEx2**](signertimestampex2.md)           | Time stamps the specified subject and optionally returns a pointer to a [**SIGNER\_CONTEXT**](signer-context.md) structure that contains a pointer to a [*BLOB*](../secgloss/b-gly.md). This function can be used to perform X.509 Public Key Infrastructure, RFC 3161–compliant, time stamps.                                                                                     |
| [**SignerTimeStampEx3**](signertimestampex3.md)           | Time stamps the specified subject and supports setting time stamps on multiple signatures.                                                                                                                                                                                                                                                                                                                          |



 

## Base Cryptography Functions

Base cryptographic functions provide the most flexible means of developing cryptography applications. All communication with a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) occurs through these functions.

A CSP is an independent module that performs all cryptographic operations. At least one CSP is required with each application that uses cryptographic functions. A single application can occasionally use more than one CSP.

If more than one CSP is used, the one to use can be specified in the CryptoAPI cryptographic function calls. One CSP, the Microsoft Base Cryptographic Provider, is bundled with the [*CryptoAPI*](../secgloss/c-gly.md). This CSP is used as a default provider by many of the CryptoAPI functions if no other CSP is specified.

Each CSP provides a different implementation of the cryptographic support provided to CryptoAPI. Some provide stronger cryptographic algorithms; others contain hardware components, such as [*smart cards*](../secgloss/s-gly.md). In addition, some CSPs can occasionally communicate directly with users, such as when [*digital signatures*](../secgloss/d-gly.md) are performed by using the user's [*signature private key*](../secgloss/s-gly.md).

Base cryptographic functions are in the following broad groups:

-   Service Provider Functions
-   Key Generation and Exchange Functions
-   Object Encoding and Decoding Functions
-   Data Encryption and Decryption Functions
-   Hash and Digital Signature Functions

### Service Provider Functions

Applications use the following service functions to connect and disconnect a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).

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
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta"><strong>CryptAcquireContext</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Acquires a handle to the current user's <a href="/windows/desktop/SecGloss/k-gly"><em>key container</em></a> within a particular CSP.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcontextaddref"><strong>CryptContextAddRef</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Increments the <a href="/windows/desktop/SecGloss/r-gly"><em>reference count</em></a> on an <a href="hcryptprov.md"><strong>HCRYPTPROV</strong></a> handle.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumprovidersa"><strong>CryptEnumProviders</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Enumerates the providers on a computer.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumprovidertypesa"><strong>CryptEnumProviderTypes</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Enumerates the types of providers supported on the computer.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetdefaultprovidera"><strong>CryptGetDefaultProvider</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Determines the default CSP either for the current user or for the computer for a specified provider type.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetprovparam"><strong>CryptGetProvParam</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves the parameters that govern the operations of a CSP.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptinstalldefaultcontext"><strong>CryptInstallDefaultContext</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Installs a previously acquired <a href="hcryptprov.md"><strong>HCRYPTPROV</strong></a> context to be used as a default context.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptreleasecontext"><strong>CryptReleaseContext</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Releases the handle acquired by the <a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta"><strong>CryptAcquireContext</strong></a> function.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetprovidera"><strong>CryptSetProvider</strong></a> and <a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetproviderexa"><strong>CryptSetProviderEx</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies the user default CSP for a particular CSP type.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetprovparam"><strong>CryptSetProvParam</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies attributes of a CSP.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptuninstalldefaultcontext"><strong>CryptUninstallDefaultContext</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Removes a default context previously installed by <a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptinstalldefaultcontext"><strong>CryptInstallDefaultContext</strong></a>.</td>
</tr>
<tr class="even">
<td><a href="freecryptprovfromcertex.md"><strong>FreeCryptProvFromCertEx</strong></a></td>
<td>Releases the handle either to a <a href="/windows/desktop/SecGloss/c-gly"><em>cryptographic service provider</em></a> (CSP) or to a Cryptography API: Next Generation (CNG) key.</td>
</tr>
</tbody>
</table>



 

### Key Generation and Exchange Functions

Key generation and exchange functions [*exchange keys*](../secgloss/e-gly.md) with other users and create, configure, and destroy [*cryptographic keys*](../secgloss/c-gly.md).

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
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptderivekey"><strong>CryptDeriveKey</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a key derived from a password.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdestroykey"><strong>CryptDestroyKey</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Destroys a key.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptduplicatekey"><strong>CryptDuplicateKey</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Makes an exact copy of a key, including the <a href="/windows/desktop/SecGloss/s-gly"><em>state</em></a> of the key.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey"><strong>CryptExportKey</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Transfers a key from the CSP into a <a href="/windows/desktop/SecGloss/k-gly"><em>key BLOB</em></a> in the application's memory space.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgenkey"><strong>CryptGenKey</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a random key.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgenrandom"><strong>CryptGenRandom</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Generates random data.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetkeyparam"><strong>CryptGetKeyParam</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves a key's parameters.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetuserkey"><strong>CryptGetUserKey</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Gets a handle to the key exchange or signature key.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey"><strong>CryptImportKey</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Transfers a key from a <a href="/windows/desktop/SecGloss/k-gly"><em>key BLOB</em></a> to a CSP.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetkeyparam"><strong>CryptSetKeyParam</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies a key's parameters.</td>
</tr>
</tbody>
</table>



 

### Object Encoding and Decoding Functions

These are generalized encoding and decoding functions. They are used to encode and decode [*certificates*](../secgloss/c-gly.md), [*certificate revocation lists*](../secgloss/c-gly.md) (CRLs), [*certificate requests*](../secgloss/c-gly.md), and certificate extensions.

| Function                                           | Description                                                                                                                                      |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptDecodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobject)     | Decodes a structure of type *lpszStructType*.                                                                                                    |
| [**CryptDecodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobjectex) | Decodes a structure of type *lpszStructType*. [**CryptDecodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodeobjectex) supports the one-pass memory allocation option. |
| [**CryptEncodeObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobject)     | Encodes a structure of type *lpszStructType*.                                                                                                    |
| [**CryptEncodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobjectex) | Encodes a structure of type *lpszStructType*. [**CryptEncodeObjectEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencodeobjectex) supports the one-pass memory allocation option. |



 

### Data Encryption and Decryption Functions

The following functions support encryption and decryption operations. [**CryptEncrypt**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencrypt) and [**CryptDecrypt**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecrypt) require a [*cryptographic key*](../secgloss/c-gly.md) before being called. This is done by using the [**CryptGenKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgenkey), [**CryptDeriveKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptderivekey), or [**CryptImportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey) function. The encryption algorithm is specified when the key is created. [**CryptSetKeyParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetkeyparam) can set additional encryption parameters.

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
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecrypt"><strong>CryptDecrypt</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Decrypts a section of <a href="/windows/desktop/SecGloss/c-gly"><em>ciphertext</em></a> by using the specified encryption key.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencrypt"><strong>CryptEncrypt</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Encrypts a section of <a href="/windows/desktop/SecGloss/p-gly"><em>plaintext</em></a> by using the specified encryption key.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dpapi/nf-dpapi-cryptprotectdata"><strong>CryptProtectData</strong></a></td>
<td>Performs encryption on the data in a <a href="/previous-versions/windows/desktop/legacy/aa381414(v=vs.85)"><strong>DATA_BLOB</strong></a> structure.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dpapi/nf-dpapi-cryptprotectmemory"><strong>CryptProtectMemory</strong></a></td>
<td>Encrypts memory to protect sensitive information.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dpapi/nf-dpapi-cryptunprotectdata"><strong>CryptUnprotectData</strong></a></td>
<td>Performs a decryption and integrity check of the data in a <a href="/previous-versions/windows/desktop/legacy/aa381414(v=vs.85)"><strong>DATA_BLOB</strong></a>.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Dpapi/nf-dpapi-cryptunprotectmemory"><strong>CryptUnprotectMemory</strong></a></td>
<td>Decrypts memory that was encrypted using <a href="/windows/desktop/api/Dpapi/nf-dpapi-cryptprotectmemory"><strong>CryptProtectMemory</strong></a>.</td>
</tr>
</tbody>
</table>



 

### Hash and Digital Signature Functions

These functions compute [*hashes*](../secgloss/h-gly.md) of data and also create and verify [*digital signatures*](../secgloss/d-gly.md). Hashes are also known as message digests.

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
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcreatehash"><strong>CryptCreateHash</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates an empty hash object.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdestroyhash"><strong>CryptDestroyHash</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Destroys a hash object.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptduplicatehash"><strong>CryptDuplicateHash</strong></a></td>
<td>Duplicates a hash object.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgethashparam"><strong>CryptGetHashParam</strong></a></td>
<td>Retrieves a hash object parameter.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashdata"><strong>CryptHashData</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes a block of data, adding it to the specified hash object.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashsessionkey"><strong>CryptHashSessionKey</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes a session key, adding it to the specified hash object.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsethashparam"><strong>CryptSetHashParam</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Sets a hash object parameter.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignhasha"><strong>CryptSignHash</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Signs the specified hash object.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuiwizdigitalsign"><strong>CryptUIWizDigitalSign</strong></a></td>
<td>Displays a wizard that digitally signs a document or a <a href="/windows/desktop/SecGloss/b-gly"><em>BLOB</em></a>.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuiwizfreedigitalsigncontext"><strong>CryptUIWizFreeDigitalSignContext</strong></a></td>
<td>Releases a pointer to a <a href="/windows/desktop/api/Cryptuiapi/ns-cryptuiapi-cryptui_wiz_digital_sign_context"><strong>CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT</strong></a> structure.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifysignaturea"><strong>CryptVerifySignature</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Verifies a digital signature, given a handle to the hash object.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Cryptuiapi/nc-cryptuiapi-pfncfilterproc"><strong>PFNCFILTERPROC</strong></a></td>
<td>Filters the certificates that appear in the digital signature wizard displayed by the <a href="/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-cryptuiwizdigitalsign"><strong>CryptUIWizDigitalSign</strong></a> function.</td>
</tr>
</tbody>
</table>



 

## Certificate and Certificate Store Functions

Certificate and certificate store functions manage the use, storage, and retrieval of [*certificates*](../secgloss/c-gly.md), [*certificate revocation lists*](../secgloss/c-gly.md) (CRLs), and [*certificate trust lists*](../secgloss/c-gly.md) (CTLs). These functions are divided into the following groups:

-   Certificate Store Functions
-   Certificate and Certificate Store Maintenance Functions
-   Certificate Functions
-   Certificate Revocation List Functions
-   Certificate Trust List Functions
-   Extended Property Functions
-   MakeCert Functions

### Certificate Store Functions

A user site can, over time, collect many certificates. Typically, a site has certificates for the user of the site as well as other certificates that describe those individuals and entities with whom the user communicates. For each entity, there can be more than one certificate. For each individual certificate, there should be a chain of verifying certificates that provides a trail back to a trusted [*root certificate*](../secgloss/r-gly.md). [*Certificate stores*](../secgloss/c-gly.md) and their related functions provide functionality to store, retrieve, enumerate, verify, and use the information stored in the certificates.

| Function                                                               | Description                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddStoreToCollection**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddstoretocollection)           | Adds a sibling certificate store to a collection certificate store.                                                                                                                                                                                                                                                                       |
| [**CertCloseStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certclosestore)                               | Closes a certificate store handle.                                                                                                                                                                                                                                                                                                        |
| [**CertControlStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcontrolstore)                           | Allows an application to be notified when there is a difference between the contents of a cached store and the contents of the store that is persisted to storage. It also provides desynchronization of the cached store, if necessary, and provides a means to commit changes made in the cached store to persisted storage.<br/> |
| [**CertDuplicateStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatestore)                       | Duplicates a store handle by incrementing the [*reference count*](../secgloss/r-gly.md).                                                                                                                                                                                            |
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

Most [*Certificate*](../secgloss/c-gly.md) functions have related functions to deal with [*CRLs*](../secgloss/c-gly.md) and [*CTLs*](../secgloss/c-gly.md). For more information about related CRL and CTL functions, see Certificate Revocation List Functions and Certificate Trust List Functions.

| Function                                                                             | Description                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddCertificateContextToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcertificatecontexttostore)         | Adds a certificate context to the certificate store.                                                                                                                                                                                            |
| [**CertAddCertificateLinkToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcertificatelinktostore)               | Adds a link in a certificate store to a certificate context in a different store.                                                                                                                                                               |
| [**CertAddEncodedCertificateToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddencodedcertificatetostore)         | Converts the encoded certificate to a certificate context, and then adds the context to the certificate store.                                                                                                                                  |
| [**CertAddRefServerOcspResponse**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddrefserverocspresponse)                 | Increments the reference count for an **HCERT\_SERVER\_OCSP\_RESPONSE** handle.                                                                                                                                                                 |
| [**CertAddRefServerOcspResponseContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddrefserverocspresponsecontext)   | Increments the reference count for a [**CERT\_SERVER\_OCSP\_RESPONSE\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_server_ocsp_response_context) structure.                                                                                                              |
| [**CertCloseServerOcspResponse**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcloseserverocspresponse)                   | Closes an [*online certificate status protocol*](../secgloss/o-gly.md) (OCSP) server response handle.                                               |
| [**CertCreateCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatecertificatecontext)                 | Creates a certificate context from an encoded certificate. The created context is not put in a certificate store.                                                                                                                               |
| [**CertCreateSelfSignCertificate**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreateselfsigncertificate)               | Creates a self-signed certificate.                                                                                                                                                                                                              |
| [**CertDeleteCertificateFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certdeletecertificatefromstore)             | Deletes a certificate from the certificate store.                                                                                                                                                                                               |
| [**CertDuplicateCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatecertificatecontext)           | Duplicates a certificate context by incrementing its [*reference count*](../secgloss/r-gly.md).                                                                                           |
| [**CertEnumCertificatesInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumcertificatesinstore)                   | Enumerates the certificate contexts in the certificate store.                                                                                                                                                                                   |
| [**CertFindCertificateInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindcertificateinstore)                     | Finds the first, or next, certificate context in the certificate store that meets a search criterion.                                                                                                                                           |
| [**CertFreeCertificateContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatecontext)                     | Frees a certificate context.                                                                                                                                                                                                                    |
| [**CertGetIssuerCertificateFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetissuercertificatefromstore)       | Gets a certificate context from the certificate store for the first, or next, issuer of the specified subject certificate.                                                                                                                      |
| [**CertGetServerOcspResponseContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetserverocspresponsecontext)         | Retrieves a non-blocking, time valid [*online certificate status protocol*](../secgloss/o-gly.md) (OCSP) response context for the specified handle. |
| [**CertGetSubjectCertificateFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetsubjectcertificatefromstore)     | Gets from the certificate store the subject certificate context, which is uniquely identified by its issuer and serial number.                                                                                                                  |
| [**CertGetValidUsages**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetvalidusages)                                     | Returns an array of usages that consist of the intersection of the valid usages for all certificates in an array of certificates.                                                                                                               |
| [**CertOpenServerOcspResponse**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenserverocspresponse)                     | Opens a handle to an [*online certificate status protocol*](../secgloss/o-gly.md) (OCSP) response associated with a server certificate chain.       |
| [**CertRetrieveLogoOrBiometricInfo**](/windows/desktop/api/Wincrypt/nf-wincrypt-certretrievelogoorbiometricinfo)           | Performs a URL retrieval of logo or biometric information specified in either the **szOID\_LOGOTYPE\_EXT** or **szOID\_BIOMETRIC\_EXT** certificate extension.                                                                                  |
| [**CertSelectCertificate**](/windows/win32/api/cryptdlg/nf-cryptdlg-certselectcertificatea)                               | Presents a dialog box that allows the user to select certificates from a set of certificates that match a given criteria.                                                                                                                       |
| [**CertSelectCertificateChains**](/windows/desktop/api/Wincrypt/nf-wincrypt-certselectcertificatechains)                   | Retrieves certificate chains based on specified selection criteria.                                                                                                                                                                             |
| [**CertSelectionGetSerializedBlob**](/windows/desktop/api/Cryptuiapi/nf-cryptuiapi-certselectiongetserializedblob)             | A helper function used to retrieve a serialized certificate [*BLOB*](../secgloss/b-gly.md) from a [**CERT\_SELECTUI\_INPUT**](/windows/desktop/api/Cryptuiapi/ns-cryptuiapi-cert_selectui_input) structure.                                               |
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

These functions manage the storage and retrieval of [*certificate revocation lists*](../secgloss/c-gly.md) (CRLs).

| Function                                                             | Description                                                                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddCRLContextToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcrlcontexttostore)         | Adds a CRL context to the certificate store.                                                                                                                                          |
| [**CertAddCRLLinkToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddcrllinktostore)               | Adds a link in a store to a CRL context in a different store.                                                                                                                         |
| [**CertAddEncodedCRLToStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddencodedcrltostore)         | Converts the encoded CRL to a CRL context, and then adds the context to the certificate store.                                                                                        |
| [**CertCreateCRLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certcreatecrlcontext)                 | Creates a CRL context from an encoded CRL. The created context is not put in a certificate store.                                                                                     |
| [**CertDeleteCRLFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certdeletecrlfromstore)             | Deletes a CRL from the certificate store.                                                                                                                                             |
| [**CertDuplicateCRLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatecrlcontext)           | Duplicates a CRL context by incrementing the [*reference count*](../secgloss/r-gly.md).                                         |
| [**CertEnumCRLsInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumcrlsinstore)                   | Enumerates the CRL contexts in a store.                                                                                                                                               |
| [**CertFindCertificateInCRL**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindcertificateincrl)         | Searches the [*certificate revocation list*](../secgloss/c-gly.md) (CRL) for the specified certificate. |
| [**CertFindCRLInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindcrlinstore)                     | Finds the first, or next, CRL context in the certificate store that matches a specific criterion.                                                                                     |
| [**CertFreeCRLContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecrlcontext)                     | Frees a CRL context.                                                                                                                                                                  |
| [**CertGetCRLFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcrlfromstore)                   | Gets the first, or next, CRL context from the certificate store for the specified issuer certificate.                                                                                 |
| [**CertSerializeCRLStoreElement**](/windows/desktop/api/Wincrypt/nf-wincrypt-certserializecrlstoreelement) | Serializes the CRL context's encoded CRL and its properties.                                                                                                                          |



 

### Certificate Trust List Functions

These functions manage the storage and retrieval of [*certificate trust lists*](../secgloss/c-gly.md) (CTLs).

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
| [**FreeCryptProvFromCert**](freecryptprovfromcert.md)                                 | Releases the handle to a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) and optionally deletes the temporary container created by the [**GetCryptProvFromCert**](getcryptprovfromcert.md) function. |
| [**GetCryptProvFromCert**](getcryptprovfromcert.md)                                   | Gets a handle to a CSP and a key specification for a certificate context.                                                                                                                                                                                                                                |
| [**PvkFreeCryptProv**](pvkfreecryptprov.md)                                           | Releases the handle to a CSP and optionally deletes the temporary container created by the [**PvkGetCryptProv**](pvkgetcryptprov.md) function.                                                                                                                                                          |
| [**PvkGetCryptProv**](pvkgetcryptprov.md)                                             | Gets a handle to a CSP based on either a [*private key*](../secgloss/p-gly.md) file name or a key container name.                                                                                                                                          |
| [**PvkPrivateKeyAcquireContextFromMemory**](pvkprivatekeyacquirecontextfrommemory.md) | Creates a temporary container in the CSP and loads a private key from memory into the container.                                                                                                                                                                                                         |
| [**PvkPrivateKeySave**](pvkprivatekeysave.md)                                         | Saves a private key and its corresponding [*public key*](../secgloss/p-gly.md) to a specified file.                                                                                                                                                          |
| [**SignError**](signerror.md)                                                         | Calls [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) and converts the return code to an **HRESULT**.                                                                                                                                                                                                              |



 

## Certificate Verification Functions

Certificates are verified using [*CTLs*](../secgloss/c-gly.md) or certificate chains. Functions are provided for both of these:

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
| [**CertDuplicateCertificateChain**](/windows/desktop/api/Wincrypt/nf-wincrypt-certduplicatecertificatechain)                                           | Duplicates a certificate chain by incrementing the chain's [*reference count*](../secgloss/r-gly.md) and returning a pointer to the chain.                    |
| [**CertFindChainInStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfindchaininstore)                                                             | Finds the first, or next, certificate chain context in a store.                                                                                                                                                     |
| [**CertFreeCertificateChain**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatechain)                                                     | Frees a certificate chain by reducing its reference count.                                                                                                                                                          |
| [**CertFreeCertificateChainEngine**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatechainengine)                                         | Frees a nondefault certificate chain engine.                                                                                                                                                                        |
| [**CertFreeCertificateChainList**](/windows/desktop/api/Wincrypt/nf-wincrypt-certfreecertificatechainlist)                                             | Frees the array of pointers to chain contexts.                                                                                                                                                                      |
| [**CertGetCertificateChain**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcertificatechain)                                                       | Builds a chain context starting from an end certificate and going back to a trusted [*root certificate*](../secgloss/r-gly.md), if possible.                |
| [**CertIsValidCRLForCertificate**](/windows/desktop/api/Wincrypt/nf-wincrypt-certisvalidcrlforcertificate)                                             | Checks a [*CRL*](../secgloss/c-gly.md) to determine whether it would include a specific certificate if that certificate were revoked. |
| [**CertSetCertificateContextPropertiesFromCTLEntry**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcertificatecontextpropertiesfromctlentry)       | Sets properties on the certificate context using the attributes in the CTL entry.                                                                                                                                   |
| [**CertVerifyCertificateChainPolicy**](/windows/desktop/api/Wincrypt/nf-wincrypt-certverifycertificatechainpolicy)                                     | Checks a certificate chain to verify its validity, including its compliance with any specified validity policy criteria.                                                                                            |



 

## Message Functions

[*CryptoAPI*](../secgloss/c-gly.md) message functions consist of two groups of functions: low-level message functions and [*simplified message functions*](../secgloss/s-gly.md).

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
| [**CryptMsgDuplicate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgduplicate)                                             | Duplicates a cryptographic message handle by incrementing the [*reference count*](../secgloss/r-gly.md). The reference count keeps track of the lifetime of the message. |
| [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam)                                               | Acquires a parameter after encoding or decoding a cryptographic message.                                                                                                                                                       |
| [**CryptMsgOpenToDecode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentodecode)                                       | Opens a cryptographic message for decoding.                                                                                                                                                                                    |
| [**CryptMsgOpenToEncode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentoencode)                                       | Opens a cryptographic message for encoding.                                                                                                                                                                                    |
| [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate)                                                   | Updates the contents of a cryptographic message.                                                                                                                                                                               |
| [**CryptMsgVerifyCountersignatureEncoded**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgverifycountersignatureencoded)     | Verifies a [*countersignature*](../secgloss/c-gly.md) in terms of the SignerInfo structure (as defined by PKCS \#7).                                                   |
| [**CryptMsgVerifyCountersignatureEncodedEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgverifycountersignatureencodedex) | Verifies that the *pbSignerInfoCounterSignature* parameter contains the encrypted [*hash*](../secgloss/h-gly.md) of the **encryptedDigest** field of the *pbSignerInfo* parameter structure.   |



 

### Simplified Message Functions

[*simplified message functions*](../secgloss/s-gly.md) wrap Low-level Message Functions into a single function to accomplish a specified task.

| Function                                                                               | Description                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptDecodeMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecodemessage)                                       | Decodes a cryptographic message.                                                                                                                                                                                                                                             |
| [**CryptDecryptAndVerifyMessageSignature**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecryptandverifymessagesignature) | Decrypts the specified message, and verifies the signer.                                                                                                                                                                                                                     |
| [**CryptDecryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecryptmessage)                                     | Decrypts the specified message.                                                                                                                                                                                                                                              |
| [**CryptEncryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptencryptmessage)                                     | Encrypts the message for the recipient or recipients.                                                                                                                                                                                                                        |
| [**CryptGetMessageCertificates**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetmessagecertificates)                     | Returns the [*certificate store*](../secgloss/c-gly.md) that contains the message's certificates and [*CRLs*](../secgloss/c-gly.md). |
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
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certcomparecertificate"><strong>CertCompareCertificate</strong></a></td>
<td>Compares two certificates to determine whether they are identical.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certcomparecertificatename"><strong>CertCompareCertificateName</strong></a></td>
<td>Compares two certificate names to determine whether they are identical.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certcompareintegerblob"><strong>CertCompareIntegerBlob</strong></a></td>
<td>Compares two integer <a href="/windows/desktop/SecGloss/b-gly"><em>BLOBs</em></a>.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certcomparepublickeyinfo"><strong>CertComparePublicKeyInfo</strong></a></td>
<td>Compares two <a href="/windows/desktop/SecGloss/p-gly"><em>public keys</em></a> to determine whether they are identical.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certfindattribute"><strong>CertFindAttribute</strong></a></td>
<td>Finds the first attribute identified by its <a href="/windows/desktop/SecGloss/o-gly"><em>object identifier</em></a> (OID).</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certfindextension"><strong>CertFindExtension</strong></a></td>
<td>Finds the first extension identified by its OID.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certfindrdnattr"><strong>CertFindRDNAttr</strong></a></td>
<td>Finds the first <a href="/windows/desktop/SecGloss/r-gly"><em>RDN</em></a> attribute identified by its OID in the name list of the <em>Relative Distinguished Names</em>.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certgetintendedkeyusage"><strong>CertGetIntendedKeyUsage</strong></a></td>
<td>Acquires the intended key usage bytes from the certificate.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certgetpublickeylength"><strong>CertGetPublicKeyLength</strong></a></td>
<td>Acquires the public/private key's bit length from the <a href="/windows/desktop/SecGloss/p-gly"><em>public key BLOB</em></a>.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certisrdnattrsincertificatename"><strong>CertIsRDNAttrsInCertificateName</strong></a></td>
<td>Compares the attributes in the <a href="/windows/desktop/SecGloss/c-gly"><em>certificate name</em></a> with the specified <a href="/windows/desktop/api/Wincrypt/ns-wincrypt-cert_rdn"><strong>CERT_RDN</strong></a> to determine whether all attributes are included there.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certisstronghashtosign"><strong>CertIsStrongHashToSign</strong></a></td>
<td>Determines whether the specified hash algorithm and the public key in the signing certificate can be used to perform strong signing.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certverifycrlrevocation"><strong>CertVerifyCRLRevocation</strong></a></td>
<td>Verifies that the subject certificate is not on the <a href="/windows/desktop/SecGloss/c-gly"><em>certificate revocation list</em></a> (CRL).</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certverifycrltimevalidity"><strong>CertVerifyCRLTimeValidity</strong></a></td>
<td>Verifies the time validity of a CRL.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certverifyrevocation"><strong>CertVerifyRevocation</strong></a></td>
<td>Verifies that the subject certificate is not on the CRL.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certverifytimevalidity"><strong>CertVerifyTimeValidity</strong></a></td>
<td>Verifies the time validity of a certificate.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-certverifyvaliditynesting"><strong>CertVerifyValidityNesting</strong></a></td>
<td>Verifies that the subject's time validity nests within the issuer's time validity.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpkcs8"><strong>CryptExportPKCS8</strong></a></td>
<td>This function is superseded by the <a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpkcs8ex"><strong>CryptExportPKCS8Ex</strong></a> function.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpkcs8ex"><strong>CryptExportPKCS8Ex</strong></a></td>
<td>Exports the private key in PKCS #8 format.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpublickeyinfo"><strong>CryptExportPublicKeyInfo</strong></a></td>
<td>Exports the public key information associated with the provider's corresponding private key.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpublickeyinfoex"><strong>CryptExportPublicKeyInfoEx</strong></a></td>
<td>Exports the public key information associated with the provider's corresponding private key. This function differs from <a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpublickeyinfo"><strong>CryptExportPublicKeyInfo</strong></a> in that the user can specify the public key algorithm, thereby overriding the default provided by the CSP.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpublickeyinfofrombcryptkeyhandle"><strong>CryptExportPublicKeyInfoFromBCryptKeyHandle</strong></a></td>
<td>Exports the public key info associated with a provider's corresponding private key.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptfindcertificatekeyprovinfo"><strong>CryptFindCertificateKeyProvInfo</strong></a></td>
<td>Enumerates the cryptographic providers and their <a href="/windows/desktop/SecGloss/k-gly"><em>key containers</em></a> to find the private key that corresponds to a certificate's public key.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptfindlocalizedname"><strong>CryptFindLocalizedName</strong></a></td>
<td>Finds the localized name for a specified name, for example, finds the localized name for the store name of the Root system.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashcertificate"><strong>CryptHashCertificate</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes the encoded content.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashcertificate2"><strong>CryptHashCertificate2</strong></a></td>
<td>Hashes a block of data by using a Cryptography API: Next Generation (CNG) hash provider.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashpublickeyinfo"><strong>CryptHashPublicKeyInfo</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Computes the hash of the encoded public key information.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashtobesigned"><strong>CryptHashToBeSigned</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Computes the hash of the &quot;to be signed&quot; information in the encoded signed content (<a href="/windows/desktop/api/Wincrypt/ns-wincrypt-cert_signed_content_info"><strong>CERT_SIGNED_CONTENT_INFO</strong></a>).</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpkcs8"><strong>CryptImportPKCS8</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Imports the <a href="/windows/desktop/SecGloss/p-gly"><em>private key</em></a> in PKCS #8 format to a <a href="/windows/desktop/SecGloss/c-gly"><em>cryptographic service provider</em></a> (CSP).</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpublickeyinfo"><strong>CryptImportPublicKeyInfo</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Converts and imports public key information into the provider, and returns a handle of the public key.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpublickeyinfoex"><strong>CryptImportPublicKeyInfoEx</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Converts and imports the public key information into the provider, and returns a handle of the public key. Additional parameters (over those specified by <a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpublickeyinfo"><strong>CryptImportPublicKeyInfo</strong></a>) that can be used to override defaults are provided to supplement <a href="/windows/desktop/api/Wincrypt/ns-wincrypt-cert_public_key_info"><strong>CERT_PUBLIC_KEY_INFO</strong></a>.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpublickeyinfoex2"><strong>CryptImportPublicKeyInfoEx2</strong></a></td>
<td>Imports a public key into a CNG asymmetric provider.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmemalloc"><strong>CryptMemAlloc</strong></a></td>
<td>Allocates memory for a buffer. This memory is used by all Crypt32.lib functions that return allocated buffers.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmemfree"><strong>CryptMemFree</strong></a></td>
<td>Frees memory allocated by <a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmemalloc"><strong>CryptMemAlloc</strong></a> or <a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmemrealloc"><strong>CryptMemRealloc</strong></a>.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmemrealloc"><strong>CryptMemRealloc</strong></a></td>
<td>Frees memory currently allocated for a buffer, and allocates memory for a new buffer.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptqueryobject"><strong>CryptQueryObject</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves information about the content of a BLOB or a file.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignandencodecertificate"><strong>CryptSignAndEncodeCertificate</strong></a></td>
<td>Encodes the &quot;to be signed&quot; information, signs this encoded information, and encodes the resulting signed, encoded information.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsigncertificate"><strong>CryptSignCertificate</strong></a></td>
<td>Signs the &quot;to be signed&quot; information in the encoded, signed content.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipaddprovider"><strong>CryptSIPAddProvider</strong></a></td>
<td>Adds a Subject Interface Package (SIP).</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipcreateindirectdata"><strong>CryptSIPCreateIndirectData</strong></a></td>
<td>Returns a <a href="/windows/win32/api/mssip/ns-mssip-sip_indirect_data"><strong>SIP_INDIRECT_DATA</strong></a> structure that contains a <a href="/windows/desktop/SecGloss/h-gly"><em>hash</em></a> of the supplied <a href="/windows/win32/api/mssip/ns-mssip-sip_subjectinfo"><strong>SIP_SUBJECTINFO</strong></a> structure, the digest algorithm, and an encoding attribute. The hash can be used as an indirect reference to the data.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipgetcaps"><strong>CryptSIPGetCaps</strong></a></td>
<td>Retrieves the capabilities of an SIP.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipgetsigneddatamsg"><strong>CryptSIPGetSignedDataMsg</strong></a></td>
<td>Retrieves an Authenticode signature from the file.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipload"><strong>CryptSIPLoad</strong></a></td>
<td>Loads the dynamic link library that implements a subject interface package and assigns appropriate library export functions to a <a href="/windows/win32/api/mssip/ns-mssip-sip_dispatch_info"><strong>SIP_DISPATCH_INFO</strong></a> structure.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipputsigneddatamsg"><strong>CryptSIPPutSignedDataMsg</strong></a></td>
<td>Stores an Authenticode Signature in the target file.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipremoveprovider"><strong>CryptSIPRemoveProvider</strong></a></td>
<td>Removes a SIP added by a previous call to the <a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipaddprovider"><strong>CryptSIPAddProvider</strong></a> function.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipremovesigneddatamsg"><strong>CryptSIPRemoveSignedDataMsg</strong></a></td>
<td>Removes a specified Authenticode signature.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipretrievesubjectguid"><strong>CryptSIPRetrieveSubjectGuid</strong></a></td>
<td>Retrieves a GUID based on the header information in a specified file.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipretrievesubjectguidforcatalogfile"><strong>CryptSIPRetrieveSubjectGuidForCatalogFile</strong></a></td>
<td>Retrieves the subject GUID associated with the specified file.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Mssip/nf-mssip-cryptsipverifyindirectdata"><strong>CryptSIPVerifyIndirectData</strong></a></td>
<td>Validates the indirect hashed data against the supplied subject.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Dpapi/nf-dpapi-cryptupdateprotectedstate"><strong>CryptUpdateProtectedState</strong></a></td>
<td>Migrates the current user's master keys after the user's <a href="/windows/desktop/SecGloss/s-gly"><em>security identifier</em></a> (SID) has changed.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifycertificatesignature"><strong>CryptVerifyCertificateSignature</strong></a></td>
<td>Verifies the signature of a subject certificate or a <a href="/windows/desktop/SecGloss/c-gly"><em>CRL</em></a> by using the public key information.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifycertificatesignatureex"><strong>CryptVerifyCertificateSignatureEx</strong></a></td>
<td>An extended version of <a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifycertificatesignature"><strong>CryptVerifyCertificateSignature</strong></a>.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-getencschannel"><strong>GetEncSChannel</strong></a></td>
<td>Stores the encrypted Schannel DLL contents in memory.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Mssip/nc-mssip-pcryptsipgetcaps"><strong>pCryptSIPGetCaps</strong></a></td>
<td>Implemented by an SIP to report capabilities.</td>
</tr>
</tbody>
</table>



 

### Data Conversion Functions

The following CryptoAPI functions convert certificate structure members to different forms.

| Function                                           | Description                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAlgIdToOID**](/windows/desktop/api/Wincrypt/nf-wincrypt-certalgidtooid)           | Converts a CryptoAPI algorithm identifier (ALG\_ID) to an [*Abstract Syntax Notation One*](../secgloss/a-gly.md) (ASN.1) [*object identifier*](../secgloss/o-gly.md) (OID) string. |
| [**CertGetNameString**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetnamestringa)     | Acquires the subject or issuer name from a certificate, and converts it to a null-terminated character string.                                                                                                                                                                                                               |
| [**CertNameToStr**](/windows/desktop/api/Wincrypt/nf-wincrypt-certnametostra)             | Converts a certificate name [*BLOB*](../secgloss/b-gly.md) to a zero-terminated string.                                                                                                                                                                                                      |
| [**CertOIDToAlgId**](/windows/desktop/api/Wincrypt/nf-wincrypt-certoidtoalgid)           | Converts the ASN.1 Object Identifier string to the CSP algorithm identifier.                                                                                                                                                                                                                                                 |
| [**CertRDNValueToStr**](/windows/desktop/api/Wincrypt/nf-wincrypt-certrdnvaluetostra)     | Converts a Name Value to a null-terminated string.                                                                                                                                                                                                                                                                           |
| [**CertStrToName**](/windows/desktop/api/Wincrypt/nf-wincrypt-certstrtonamea)             | Converts a null-terminated [*X.500*](../secgloss/x-gly.md) string to an encoded certificate name.                                                                                                                                                                                          |
| [**CryptBinaryToString**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptbinarytostringa) | Converts a binary sequence into a formatted string.                                                                                                                                                                                                                                                                          |
| [**CryptFormatObject**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptformatobject)     | Formats encoded data, and returns a Unicode string.                                                                                                                                                                                                                                                                          |
| [**CryptStringToBinary**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptstringtobinarya) | Converts a formatted string to a binary sequence.                                                                                                                                                                                                                                                                            |



 

### Enhanced Key Usage Functions

The following functions deal with the [*enhanced key usage*](../secgloss/e-gly.md) (EKU) extension and the EKU extended property of certificates. The EKU extension and extended property specify and limit the valid uses of a certificate. The extensions are part of the certificate itself. They are set by the issuer of the certificate and are read-only. Certificate-extended properties are values associated with a certificate that can be set in an application.

| Function                                                                             | Description                                                                    |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**CertAddEnhancedKeyUsageIdentifier**](/windows/desktop/api/Wincrypt/nf-wincrypt-certaddenhancedkeyusageidentifier)       | Adds a usage identifier to a certificate's EKU property.                       |
| [**CertGetEnhancedKeyUsage**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetenhancedkeyusage)                           | Acquires, from a certificate, information about the EKU extension or property. |
| [**CertRemoveEnhancedKeyUsageIdentifier**](/windows/desktop/api/Wincrypt/nf-wincrypt-certremoveenhancedkeyusageidentifier) | Removes the usage identifier from a certificate's EKU extended property.       |
| [**CertSetEnhancedKeyUsage**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetenhancedkeyusage)                           | Sets the EKU property for a certificate.                                       |



 

### Key Identifier Functions

Key identifier functions allow the user to create, set, retrieve, or locate a key identifier or its properties.

A key identifier is the unique identifier of a [*public/private key pair*](../secgloss/p-gly.md). It can be any unique identifier but is usually the 20-byte SHA1 hash of an encoded [**CERT\_PUBLIC\_KEY\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_public_key_info) structure. A key identifier can be obtained through the certificate's CERT\_KEY\_IDENTIFIER\_PROP\_ID. The key identifier allows the use of that [*key pair*](../secgloss/k-gly.md) to encrypt or decrypt messages without using the certificate.

Key identifiers are not associated with [*CRLs*](../secgloss/c-gly.md) or [*CTLs*](../secgloss/c-gly.md).

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
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcreatekeyidentifierfromcsp"><strong>CryptCreateKeyIdentifierFromCSP</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a key identifier from a CSP's <a href="/windows/desktop/SecGloss/p-gly"><em>public key BLOB</em></a>.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumkeyidentifierproperties"><strong>CryptEnumKeyIdentifierProperties</strong></a></td>
<td>Enumerates key identifiers and their properties.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgetkeyidentifierproperty"><strong>CryptGetKeyIdentifierProperty</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Acquires a specific property from a specified key identifier.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetkeyidentifierproperty"><strong>CryptSetKeyIdentifierProperty</strong></a></td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using <a href="/windows/desktop/SecCNG/cng-portal">Cryptography Next Generation APIs.</a> Microsoft may remove this API in future releases.
</blockquote>
<br/> Sets a property of a specified key identifier.</td>
</tr>
</tbody>
</table>



 

### OID Support Functions

These functions provide [*object identifier*](../secgloss/o-gly.md) (OID) support. These functions install, register, and dispatch to OID and encoding type-specific functions.

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
| [**CryptRegisterOIDInfo**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptregisteroidinfo)                           | Registers the OID information specified in the [**CRYPT\_OID\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_oid_info) structure, persisting it to the registry.                                                                                |
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

The following functions support Personal Information Exchange (PFX) format [*BLOBs*](../secgloss/b-gly.md).

| Function                                             | Description                                                                                                                                                                                                                                                                  |
|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PFXExportCertStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-pfxexportcertstore)     | Exports from the referenced [*certificate store*](../secgloss/c-gly.md) the certificates and, if available, their associated [*private keys*](../secgloss/p-gly.md). |
| [**PFXExportCertStoreEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-pfxexportcertstoreex) | Exports from the referenced certificate store the certificates and, if available, their associated private keys.                                                                                                                                                             |
| [**PFXImportCertStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-pfximportcertstore)     | Imports a PFX BLOB, and returns the handle of a store that contains certificates and any associated private keys.                                                                                                                                                            |
| [**PFXIsPFXBlob**](/windows/desktop/api/Wincrypt/nf-wincrypt-pfxispfxblob)                 | Attempts to decode the outer layer of a BLOB as a PFX packet.                                                                                                                                                                                                                |
| [**PFXVerifyPassword**](/windows/desktop/api/Wincrypt/nf-wincrypt-pfxverifypassword)       | Attempts to decode the outer layer of a BLOB as a PFX packet and to decrypt it with the given password.                                                                                                                                                                      |



 

## Certificate Services Backup and Restore Functions

Certificate Services includes functions for backing up and restoring the Certificate Services database. These Certificate Services backup and restore functions are contained in Certadm.dll. Unlike the other API elements associated with Certificate Services, these functions are not encapsulated in an object that can be used to call class methods. Instead, the backup and restore APIs are called by first loading the Certadm.dll library into memory by calling [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and then determining the address of the functions by calling [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress). When you have finished calling the Certificate Services backup and restore functions, call [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) to free Certadm.dll resources from memory.

> [!Note]
> Backup and restore functions provided by Certadm.dll do not backup or restore the Certificate Service's [*private keys*](../secgloss/p-gly.md). For information about backing up the Certificate Services private keys, see [Backing Up and Restoring the Certificate Services Private Key](backing-up-and-restoring-the-certificate-services-private-key.md).
> 
> To call the backup and restore functions, you must have backup and restore [*privileges*](../secgloss/p-gly.md). For details, see [Setting the Backup and Restore Privileges](setting-the-backup-and-restore-privileges.md).

 

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

The callback functions in this section are used to register or install application-defined [*certificate store*](../secgloss/c-gly.md) providers and to provide related functionality through callback functions. Callback functions are implemented by an application and are called by [*CryptoAPI*](../secgloss/c-gly.md) functions. Callback functions enable the application to control, in part, the way that CryptoAPI functions manipulate data.

| Callback function                                                                                                        | Use                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertChainFindByIssuerCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_chain_find_by_issuer_callback)                                                   | An application-defined callback function that allows the application to filter certificates that might be added to the certificate chain.                                                                                                                                                                                                     |
| [**CertDllOpenStoreProv**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_dll_open_store_prov_func)                                                                     | Defines the store provider open function.                                                                                                                                                                                                                                                                                                     |
| [**CertEnumPhysicalStoreCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_enum_physical_store)                                                   | Callback function used by the [**CertEnumPhysicalStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumphysicalstore) function to format and present information on each physical store found.                                                                                                                                                                                 |
| [**CertEnumSystemStoreCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_enum_system_store)                                                       | Callback function used by the [**CertEnumSystemStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumsystemstore) function to format and present information on each physical store found.                                                                                                                                                                                     |
| [**CertEnumSystemStoreLocationCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_enum_system_store_location)                                       | Callback function used by the [**CertEnumSystemStoreLocation**](/windows/desktop/api/Wincrypt/nf-wincrypt-certenumsystemstorelocation) function to format and present information on each physical store found.                                                                                                                                                                     |
| [**CertStoreProvCloseCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_close)                                                         | Determines what happens when an open store's [*reference count*](../secgloss/r-gly.md) becomes zero.                                                                                                                                                                                    |
| [**CertStoreProvControl**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cert_store_prov_control)                                                                     | Allows an application to be notified when there is a difference between the contents of a cached store in use and the contents of that store as it is persisted to storage.                                                                                                                                                                   |
| [**CertStoreProvDeleteCertCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_delete_cert)                                               | Determines actions to be taken before a certificate is deleted from a certificate store.                                                                                                                                                                                                                                                      |
| [**CertStoreProvDeleteCRLCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_delete_crl)                                                 | Determines actions to be taken before a [*certificate revocation list*](../secgloss/c-gly.md) (CRL) is deleted from a certificate store.                                                                                                                        |
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
| [**CertStoreProvReadCTL**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cert_store_prov_read_ctl)                                                                     | Read the provider's copy of the CTL context, and, if it exists, create a new CTL context.                                                                                                                                                                                                                                                     |
| [**CertStoreProvSetCertPropertyCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_set_cert_property)                                     | Determines actions to be taken before a call to [**CertSetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcertificatecontextproperty) or [**CertGetCertificateContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcertificatecontextproperty).                                                                                                                             |
| [**CertStoreProvSetCRLPropertyCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_set_crl_property)                                       | Determines actions to be taken before a call to [**CertSetCRLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certsetcrlcontextproperty) or [**CertGetCRLContextProperty**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetcrlcontextproperty).                                                                                                                                                             |
| [**CertStoreProvSetCTLProperty**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_set_ctl_property)                                                       | Determines whether a property can be set on a CTL.                                                                                                                                                                                                                                                                                            |
| [**CertStoreProvWriteCertCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_write_cert)                                                 | Determines actions to be taken before adding a certificate to a store.                                                                                                                                                                                                                                                                        |
| [**CertStoreProvWriteCRLCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_write_crl)                                                   | Determines actions to be taken before adding a CRL to a store.                                                                                                                                                                                                                                                                                |
| [**CertStoreProvWriteCTL**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_cert_store_prov_write_ctl)                                                                   | Determines whether a CTL can be added to the store.                                                                                                                                                                                                                                                                                           |
| [**CRYPT\_ENUM\_KEYID\_PROP**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_enum_keyid_prop)                                                                | Callback function used by the [**CryptEnumKeyIdentifierProperties**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumkeyidentifierproperties) function.                                                                                                                                                                                                                          |
| [**CRYPT\_ENUM\_OID\_FUNCTION**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_enum_oid_func)                                                            | Callback function used by the [**CryptEnumOIDFunction**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumoidfunction) function.                                                                                                                                                                                                                                                  |
| [**CRYPT\_ENUM\_OID\_INFO**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_enum_oid_info)                                                                    | Callback function used by the [**CryptEnumOIDInfo**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptenumoidinfo) function.                                                                                                                                                                                                                                                          |
| [**CryptGetSignerCertificateCallback**](/windows/desktop/api/Wincrypt/nc-wincrypt-pfn_crypt_get_signer_certificate)                                           | Callback function used with the [**CRYPT\_VERIFY\_MESSAGE\_PARA**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_verify_message_para) structure to get and verify a message signer's certificate.                                                                                                                                                                                 |
| [**PCRYPT\_DECRYPT\_PRIVATE\_KEY\_FUNC**](/windows/win32/api/wincrypt/nc-wincrypt-pcrypt_decrypt_private_key_func)                                           | Callback function used by the [**CryptImportPKCS8**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpkcs8) function.                                                                                                                                                                                                                                                          |
| [**PCRYPT\_ENCRYPT\_PRIVATE\_KEY\_FUNC**](/windows/win32/api/wincrypt/nc-wincrypt-pcrypt_encrypt_private_key_func)                                           | Callback function used when creating the [**CRYPT\_ENCRYPTED\_PRIVATE\_KEY\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_encrypted_private_key_info) structure.                                                                                                                                                                                                          |
| [**PCRYPT\_RESOLVE\_HCRYPTPROV\_FUNC**](/windows/win32/api/wincrypt/nc-wincrypt-pcrypt_resolve_hcryptprov_func)                                              | Callback function used by the [**CryptImportPKCS8**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpkcs8) function.                                                                                                                                                                                                                                                          |
| [**PFN\_CDF\_PARSE\_ERROR\_CALLBACK**](/windows/win32/api/mscat/nc-mscat-pfn_cdf_parse_error_callback)                                                 | A user-defined function called for Catalog Definition Function errors while parsing a catalog definition file (CDF).                                                                                                                                                                                                                          |
| [**PFN\_CERT\_CREATE\_CONTEXT\_SORT\_FUNC**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cert_create_context_sort_func)                                      | Called for each sorted context entry when a context is created.                                                                                                                                                                                                                                                                               |
| [**PFN\_CMSG\_CNG\_IMPORT\_CONTENT\_ENCRYPT\_KEY**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cmsg_cng_import_content_encrypt_key)                         | A CNG [*object identifier*](../secgloss/o-gly.md) (OID) installable function for import of an already decrypted content encryption key (CEK).                                                                                                                                       |
| [**PFN\_CMSG\_CNG\_IMPORT\_KEY\_AGREE**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cmsg_cng_import_key_agree)                                              | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_CNG\_IMPORT\_KEY\_TRANS**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cmsg_cng_import_key_trans)                                              | A CNG OID installable function for import and [*decryption*](../secgloss/d-gly.md) of a key-transport-recipient, encrypted, content [*encryption*](../secgloss/e-gly.md) key (CEK).                                                                   |
| [**PFN\_CMSG\_EXPORT\_KEY\_AGREE**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cmsg_export_key_agree)                                                       | Encrypts and exports the content encryption key for a key agreement recipient of an enveloped message.                                                                                                                                                                                                                                        |
| [**PFN\_CMSG\_EXPORT\_KEY\_TRANS**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cmsg_export_key_trans)                                                       | Encrypts and exports the content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                        |
| [**PFN\_CMSG\_EXPORT\_MAIL\_LIST**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cmsg_export_mail_list)                                                       | Encrypts and exports the content encryption key for a mailing list recipient of an enveloped message.                                                                                                                                                                                                                                         |
| [**PFN\_CMSG\_GEN\_CONTENT\_ENCRYPT\_KEY**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cmsg_gen_content_encrypt_key)                                        | Generates the [*symmetric key*](../secgloss/s-gly.md) used to encrypt content for an enveloped message.                                                                                                                                                                                     |
| [**PFN\_CMSG\_IMPORT\_KEY\_AGREE**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cmsg_import_key_agree)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_IMPORT\_KEY\_TRANS**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cmsg_import_key_trans)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_IMPORT\_MAIL\_LIST**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_cmsg_import_mail_list)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CRYPT\_EXPORT\_PUBLIC\_KEY\_INFO\_EX2\_FUNC**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_crypt_export_public_key_info_ex2_func)                    | Called by [**CryptExportPublicKeyInfoEx**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportpublickeyinfoex) to export a public key BLOB and encode it.                                                                                                                                                                                                                         |
| [**PFN\_CRYPT\_EXTRACT\_ENCODED\_SIGNATURE\_PARAMETERS\_FUNC**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_crypt_extract_encoded_signature_parameters_func) | Called to decode and return the hash algorithm identifier and optionally the signature parameters.                                                                                                                                                                                                                                            |
| [**PFN\_CRYPT\_SIGN\_AND\_ENCODE\_HASH\_FUNC**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_crypt_sign_and_encode_hash_func)                                 | Called to sign and encode a computed hash.                                                                                                                                                                                                                                                                                                    |
| [**PFN\_CRYPT\_VERIFY\_ENCODED\_SIGNATURE\_FUNC**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_crypt_verify_encoded_signature_func)                          | Called to decrypt an encoded signature and compare it to a computed hash.                                                                                                                                                                                                                                                                     |
| [**PFN\_IMPORT\_PUBLIC\_KEY\_INFO\_EX2\_FUNC**](/windows/win32/api/wincrypt/nc-wincrypt-pfn_import_public_key_info_ex2_func)                                 | Called by [**CryptImportPublicKeyInfoEx2**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportpublickeyinfoex2) to decode the [*public key algorithm*](../secgloss/p-gly.md) identifier, load the algorithm provider, and import the [*key pair*](../secgloss/k-gly.md). |
| [**PFNCCERTDISPLAYPROC**](pfnccertdisplayproc.md)                                                                       | A user-defined callback function that allows the caller of the [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md) function to handle the display of certificates that the user selects to view.                                                                                                                               |
| [**PFNCMFILTERPROC**](/windows/desktop/api/CryptDlg/nc-cryptdlg-pfncmfilterproc)                                                                               | Filters each certificate to decide if it will appear in the certificate selection dialog box displayed by the [**CertSelectCertificate**](/windows/win32/api/cryptdlg/nf-cryptdlg-certselectcertificatea) function.                                                                                                                                                                |
| [**PFNCMHOOKPROC**](/windows/desktop/api/CryptDlg/nc-cryptdlg-pfncmhookproc)                                                                                   | Called before messages are processed by the certificate selection dialog box produced by the [**CertSelectCertificate**](/windows/win32/api/cryptdlg/nf-cryptdlg-certselectcertificatea) function.                                                                                                                                                                                 |



 

## Catalog Definition Functions

These functions are used to create a catalog. All of these functions are called by [MakeCat](makecat.md).

| Function                                                                           | Description                                                                                                               |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**CryptCATCDFClose**](/windows/desktop/api/Mscat/nf-mscat-cryptcatcdfclose)                                       | Closes a catalog definition file and frees the memory for the corresponding [**CRYPTCATCDF**](/windows/win32/api/mscat/ns-mscat-cryptcatcdf) structure. |
| [**CryptCATCDFEnumAttributesWithCDFTag**](cryptcatcdfenumattributeswithcdftag.md) | Enumerates the attributes of member files in the **CatalogFiles** section of a CDF.                                       |
| [**CryptCATCDFEnumCatAttributes**](/windows/desktop/api/Mscat/nf-mscat-cryptcatcdfenumcatattributes)               | Enumerates catalog-level attributes within the **CatalogHeader** section of a CDF.                                        |
| [**CryptCATCDFEnumMembersByCDFTagEx**](cryptcatcdfenummembersbycdftagex.md)       | Enumerates the individual file members in the **CatalogFiles** section of a CDF.                                          |
| [**CryptCATCDFOpen**](/windows/desktop/api/Mscat/nf-mscat-cryptcatcdfopen)                                         | Opens an existing CDF for reading and initializes a [**CRYPTCATCDF**](/windows/win32/api/mscat/ns-mscat-cryptcatcdf) structure.                         |



 

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
| [**WTHelperGetProvPrivateDataFromChain**](/windows/desktop/api/Wintrust/nf-wintrust-wthelpergetprovprivatedatafromchain)     | Receives a [**CRYPT\_PROVIDER\_PRIVDATA**](/windows/desktop/api/Wintrust/ns-wintrust-crypt_provider_privdata) structure from the chain by using the provider ID.                                           |
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



 

 

 
