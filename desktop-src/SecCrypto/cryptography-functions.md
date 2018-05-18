---
Description: 'Lists the functions provided by CryptoAPI.'
ms.assetid: '9a65f73d-6f8c-4271-a2d0-d91ad952f9c6'
title: Cryptography Functions
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
| [**CryptXmlCreateReference**](cryptxmlcreatereference.md)                        | Creates a reference to an XML signature.                                                                                                                                                                                                                                                                         |
| [**CryptXmlAddObject**](cryptxmladdobject.md)                                    | Adds the **Object** element to the Signature in the Document Context opened for encoding.                                                                                                                                                                                                                        |
| [**CryptXmlClose**](cryptxmlclose.md)                                            | Closes a cryptographic XML object handle.                                                                                                                                                                                                                                                                        |
| [**CryptXmlDigestReference**](cryptxmldigestreference.md)                        | Used by an application to digest the resolved reference. This function applies transforms before updating the digest.                                                                                                                                                                                            |
| [**CryptXmlDllCloseDigest**](cryptxmldllclosedigest.md)                          | Frees the CRYPT\_XML\_DIGEST allocated by the [**CryptXmlDllCreateDigest**](cryptxmldllcreatedigest.md) function.                                                                                                                                                                                               |
| [**CryptXmlDllCreateDigest**](cryptxmldllcreatedigest.md)                        | Creates a digest object for the specified method.                                                                                                                                                                                                                                                                |
| [**CryptXmlDllCreateKey**](cryptxmldllcreatekey.md)                              | Parses the **KeyValue** element and creates a Cryptography API: Next Generation (CNG) BCrypt key handle to verify a signature.                                                                                                                                                                                   |
| [**CryptXmlDllDigestData**](cryptxmldlldigestdata.md)                            | Puts data into the digest.                                                                                                                                                                                                                                                                                       |
| [**CryptXmlDllEncodeAlgorithm**](cryptxmldllencodealgorithm.md)                  | Encodes **SignatureMethod** or **DigestMethod** elements for agile algorithms with default parameters.                                                                                                                                                                                                           |
| [**CryptXmlDllEncodeKeyValue**](cryptxmldllencodekeyvalue.md)                    | Encodes a **KeyValue** element.                                                                                                                                                                                                                                                                                  |
| [**CryptXmlDllFinalizeDigest**](cryptxmldllfinalizedigest.md)                    | Retrieves the digest value.                                                                                                                                                                                                                                                                                      |
| [**CryptXmlDllGetAlgorithmInfo**](cryptxmldllgetalgorithminfo.md)                | Decodes the XML algorithm and returns information about the algorithm.                                                                                                                                                                                                                                           |
| [**CryptXmlDllGetInterface**](cryptxmldllgetinterface.md)                        | Retrieves a pointer to the cryptographic extension functions for the specified algorithm.                                                                                                                                                                                                                        |
| [**CryptXmlDllSignData**](cryptxmldllsigndata.md)                                | Signs data.                                                                                                                                                                                                                                                                                                      |
| [**CryptXmlDllVerifySignature**](cryptxmldllverifysignature.md)                  | Verifies a signature.                                                                                                                                                                                                                                                                                            |
| [**CryptXmlEncode**](cryptxmlencode.md)                                          | Encodes signature data by using the supplied XML writer callback function.                                                                                                                                                                                                                                       |
| [**CryptXmlGetAlgorithmInfo**](cryptxmlgetalgorithminfo.md)                      | Decodes the CRYPT\_XML\_ALGORITHM structure and returns information about the algorithm.                                                                                                                                                                                                                         |
| [**CryptXmlGetDocContext**](cryptxmlgetdoccontext.md)                            | Returns the document context specified by the supplied handle.                                                                                                                                                                                                                                                   |
| [**CryptXmlGetReference**](cryptxmlgetreference.md)                              | Returns the **Reference** element specified by the supplied handle.                                                                                                                                                                                                                                              |
| [**CryptXmlGetSignature**](cryptxmlgetsignature.md)                              | Returns an XML **Signature** element.                                                                                                                                                                                                                                                                            |
| [**CryptXmlGetStatus**](cryptxmlgetstatus.md)                                    | Returns a [**CRYPT\_XML\_STATUS**](crypt-xml-status.md) structure that contains status information about the object specified by the supplied handle.                                                                                                                                                           |
| [**CryptXmlGetTransforms**](cryptxmlgettransforms.md)                            | Returns information about the default transform chain engine.                                                                                                                                                                                                                                                    |
| [**CryptXmlImportPublicKey**](cryptxmlimportpublickey.md)                        | Imports the public key specified by the supplied handle.                                                                                                                                                                                                                                                         |
| [**CryptXmlOpenToEncode**](cryptxmlopentoencode.md)                              | Opens an XML digital signature to encode and returns a handle of the opened **Signature** element. The handle encapsulates a document context with a single [**CRYPT\_XML\_SIGNATURE**](crypt-xml-signature.md) structure and remains open until the [**CryptXmlClose**](cryptxmlclose.md) function is called. |
| [**CryptXmlOpenToDecode**](cryptxmlopentodecode.md)                              | Opens an XML digital signature to decode and returns the handle of the document context that encapsulates a [**CRYPT\_XML\_SIGNATURE**](crypt-xml-signature.md) structure. The document context can include one or more **Signature** elements.                                                                 |
| [**CryptXmlSetHMACSecret**](cryptxmlsethmacsecret.md)                            | Sets the HMAC secret on the handle before calling the [**CryptXmlSign**](cryptxmlsign.md) or [**CryptXmlVerify**](cryptxmlverifysignature.md) function.                                                                                                                                                        |
| [**CryptXmlSign**](cryptxmlsign.md)                                              | Creates a cryptographic signature of a **SignedInfo** element.                                                                                                                                                                                                                                                   |
| [**CryptXmlVerifySignature**](cryptxmlverifysignature.md)                        | Performs a cryptographic signature validation of a **SignedInfo** element.                                                                                                                                                                                                                                       |
| [*PFN\_CRYPT\_XML\_WRITE\_CALLBACK*](pfn-crypt-xml-write-callback.md)            | Creates a transform for a specified data provider.                                                                                                                                                                                                                                                               |
| [*PFN\_CRYPT\_XML\_CREATE\_TRANSFORM*](pfn-crypt-xml-create-transform.md)        | Writes cryptographic XML data.                                                                                                                                                                                                                                                                                   |
| [*PFN\_CRYPT\_XML\_DATA\_PROVIDER\_READ*](pfn-crypt-xml-data-provider-read.md)   | Reads cryptographic XML data.                                                                                                                                                                                                                                                                                    |
| [*PFN\_CRYPT\_XML\_DATA\_PROVIDER\_CLOSE*](pfn-crypt-xml-data-provider-close.md) | Releases the cryptographic XML data provider.                                                                                                                                                                                                                                                                    |
| [*PFN\_CRYPT\_XML\_ENUM\_ALG\_INFO*](pfn-crypt-xml-enum-alg-info.md)             | Enumerates predefined and registered [**CRYPT\_XML\_ALGORITHM\_INFO**](crypt-xml-algorithm-info.md) entries.                                                                                                                                                                                                    |



 

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
<td>[<strong>CryptAcquireContext</strong>](cryptacquirecontext.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Acquires a handle to the current user's [<em>key container</em>](security.k_gly#-security-key-container-gly) within a particular CSP.</td>
</tr>
<tr class="even">
<td>[<strong>CryptContextAddRef</strong>](cryptcontextaddref.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Increments the [<em>reference count</em>](security.r_gly#-security-reference-count-gly) on an [<strong>HCRYPTPROV</strong>](hcryptprov.md) handle.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptEnumProviders</strong>](cryptenumproviders.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Enumerates the providers on a computer.</td>
</tr>
<tr class="even">
<td>[<strong>CryptEnumProviderTypes</strong>](cryptenumprovidertypes.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Enumerates the types of providers supported on the computer.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGetDefaultProvider</strong>](cryptgetdefaultprovider.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Determines the default CSP either for the current user or for the computer for a specified provider type.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGetProvParam</strong>](cryptgetprovparam.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves the parameters that govern the operations of a CSP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptInstallDefaultContext</strong>](cryptinstalldefaultcontext.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Installs a previously acquired [<strong>HCRYPTPROV</strong>](hcryptprov.md) context to be used as a default context.</td>
</tr>
<tr class="even">
<td>[<strong>CryptReleaseContext</strong>](cryptreleasecontext.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Releases the handle acquired by the [<strong>CryptAcquireContext</strong>](cryptacquirecontext.md) function.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSetProvider</strong>](cryptsetprovider.md) and [<strong>CryptSetProviderEx</strong>](cryptsetproviderex.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies the user default CSP for a particular CSP type.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSetProvParam</strong>](cryptsetprovparam.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Specifies attributes of a CSP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUninstallDefaultContext</strong>](cryptuninstalldefaultcontext.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Removes a default context previously installed by [<strong>CryptInstallDefaultContext</strong>](cryptinstalldefaultcontext.md).</td>
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
<td>[<strong>CryptDeriveKey</strong>](cryptderivekey.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a key derived from a password.</td>
</tr>
<tr class="even">
<td>[<strong>CryptDestroyKey</strong>](cryptdestroykey.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Destroys a key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptDuplicateKey</strong>](cryptduplicatekey.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Makes an exact copy of a key, including the [<em>state</em>](security.s_gly#-security-state-gly) of the key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptExportKey</strong>](cryptexportkey.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Transfers a key from the CSP into a [<em>key BLOB</em>](security.k_gly#-security-key-blob-gly) in the application's memory space.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGenKey</strong>](cryptgenkey.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a random key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGenRandom</strong>](cryptgenrandom.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Generates random data.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGetKeyParam</strong>](cryptgetkeyparam.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves a key's parameters.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGetUserKey</strong>](cryptgetuserkey.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Gets a handle to the key exchange or signature key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptImportKey</strong>](cryptimportkey.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Transfers a key from a [<em>key BLOB</em>](security.k_gly#-security-key-blob-gly) to a CSP.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSetKeyParam</strong>](cryptsetkeyparam.md)</td>
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
| [**CryptDecodeObject**](cryptdecodeobject.md)     | Decodes a structure of type *lpszStructType*.                                                                                                    |
| [**CryptDecodeObjectEx**](cryptdecodeobjectex.md) | Decodes a structure of type *lpszStructType*. [**CryptDecodeObjectEx**](cryptdecodeobjectex.md) supports the one-pass memory allocation option. |
| [**CryptEncodeObject**](cryptencodeobject.md)     | Encodes a structure of type *lpszStructType*.                                                                                                    |
| [**CryptEncodeObjectEx**](cryptencodeobjectex.md) | Encodes a structure of type *lpszStructType*. [**CryptEncodeObjectEx**](cryptencodeobjectex.md) supports the one-pass memory allocation option. |



 

### Data Encryption and Decryption Functions

The following functions support encryption and decryption operations. [**CryptEncrypt**](cryptencrypt.md) and [**CryptDecrypt**](cryptdecrypt.md) require a [*cryptographic key*](security.c_gly#-security-cryptographic-key-gly) before being called. This is done by using the [**CryptGenKey**](cryptgenkey.md), [**CryptDeriveKey**](cryptderivekey.md), or [**CryptImportKey**](cryptimportkey.md) function. The encryption algorithm is specified when the key is created. [**CryptSetKeyParam**](cryptsetkeyparam.md) can set additional encryption parameters.

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
<td>[<strong>CryptDecrypt</strong>](cryptdecrypt.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Decrypts a section of [<em>ciphertext</em>](security.c_gly#-security-ciphertext-gly) by using the specified encryption key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptEncrypt</strong>](cryptencrypt.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Encrypts a section of [<em>plaintext</em>](security.p_gly#-security-plaintext-gly) by using the specified encryption key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptProtectData</strong>](cryptprotectdata.md)</td>
<td>Performs encryption on the data in a [<strong>DATA_BLOB</strong>](crypt-integer-blob.md) structure.</td>
</tr>
<tr class="even">
<td>[<strong>CryptProtectMemory</strong>](cryptprotectmemory.md)</td>
<td>Encrypts memory to protect sensitive information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUnprotectData</strong>](cryptunprotectdata.md)</td>
<td>Performs a decryption and integrity check of the data in a [<strong>DATA_BLOB</strong>](crypt-integer-blob.md).</td>
</tr>
<tr class="even">
<td>[<strong>CryptUnprotectMemory</strong>](cryptunprotectmemory.md)</td>
<td>Decrypts memory that was encrypted using [<strong>CryptProtectMemory</strong>](cryptprotectmemory.md).</td>
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
<td>[<strong>CryptCreateHash</strong>](cryptcreatehash.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates an empty hash object.</td>
</tr>
<tr class="even">
<td>[<strong>CryptDestroyHash</strong>](cryptdestroyhash.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Destroys a hash object.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptDuplicateHash</strong>](cryptduplicatehash.md)</td>
<td>Duplicates a hash object.</td>
</tr>
<tr class="even">
<td>[<strong>CryptGetHashParam</strong>](cryptgethashparam.md)</td>
<td>Retrieves a hash object parameter.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptHashData</strong>](crypthashdata.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes a block of data, adding it to the specified hash object.</td>
</tr>
<tr class="even">
<td>[<strong>CryptHashSessionKey</strong>](crypthashsessionkey.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes a session key, adding it to the specified hash object.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSetHashParam</strong>](cryptsethashparam.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Sets a hash object parameter.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSignHash</strong>](cryptsignhash.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Signs the specified hash object.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUIWizDigitalSign</strong>](cryptuiwizdigitalsign.md)</td>
<td>Displays a wizard that digitally signs a document or a [<em>BLOB</em>](security.b_gly#-security-blob-gly).</td>
</tr>
<tr class="even">
<td>[<strong>CryptUIWizFreeDigitalSignContext</strong>](cryptuiwizfreedigitalsigncontext.md)</td>
<td>Releases a pointer to a [<strong>CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT</strong>](cryptui-wiz-digital-sign-context.md) structure.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptVerifySignature</strong>](cryptverifysignature.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Verifies a digital signature, given a handle to the hash object.</td>
</tr>
<tr class="even">
<td>[<strong>PFNCFILTERPROC</strong>](pfncfilterproc.md)</td>
<td>Filters the certificates that appear in the digital signature wizard displayed by the [<strong>CryptUIWizDigitalSign</strong>](cryptuiwizdigitalsign.md) function.</td>
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
| [**CertAddStoreToCollection**](certaddstoretocollection.md)           | Adds a sibling certificate store to a collection certificate store.                                                                                                                                                                                                                                                                       |
| [**CertCloseStore**](certclosestore.md)                               | Closes a certificate store handle.                                                                                                                                                                                                                                                                                                        |
| [**CertControlStore**](certcontrolstore.md)                           | Allows an application to be notified when there is a difference between the contents of a cached store and the contents of the store that is persisted to storage. It also provides desynchronization of the cached store, if necessary, and provides a means to commit changes made in the cached store to persisted storage.<br/> |
| [**CertDuplicateStore**](certduplicatestore.md)                       | Duplicates a store handle by incrementing the [*reference count*](security.r_gly#-security-reference-count-gly).                                                                                                                                                                                            |
| [**CertEnumPhysicalStore**](certenumphysicalstore.md)                 | Enumerates the physical stores for a specified system store.                                                                                                                                                                                                                                                                              |
| [**CertEnumSystemStore**](certenumsystemstore.md)                     | Enumerates all available system stores.                                                                                                                                                                                                                                                                                                   |
| [**CertEnumSystemStoreLocation**](certenumsystemstorelocation.md)     | Enumerates all of the locations that have an available system store.                                                                                                                                                                                                                                                                      |
| [**CertGetStoreProperty**](certgetstoreproperty.md)                   | Gets a store property.                                                                                                                                                                                                                                                                                                                    |
| [**CertOpenStore**](certopenstore.md)                                 | Opens a certificate store using a specified store provider type.                                                                                                                                                                                                                                                                          |
| [**CertOpenSystemStore**](certopensystemstore.md)                     | Opens a system certificate store based on a subsystem protocol.                                                                                                                                                                                                                                                                           |
| [**CertRegisterPhysicalStore**](certregisterphysicalstore.md)         | Adds a physical store to a registry system store collection.                                                                                                                                                                                                                                                                              |
| [**CertRegisterSystemStore**](certregistersystemstore.md)             | Registers a system store.                                                                                                                                                                                                                                                                                                                 |
| [**CertRemoveStoreFromCollection**](certremovestorefromcollection.md) | Removes a sibling certificate store from a collection store.                                                                                                                                                                                                                                                                              |
| [**CertSaveStore**](certsavestore.md)                                 | Saves the certificate store.                                                                                                                                                                                                                                                                                                              |
| [**CertSetStoreProperty**](certsetstoreproperty.md)                   | Sets a store property.                                                                                                                                                                                                                                                                                                                    |
| [**CertUnregisterPhysicalStore**](certunregisterphysicalstore.md)     | Removes a physical store from a specified system store collection.                                                                                                                                                                                                                                                                        |
| [**CertUnregisterSystemStore**](certunregistersystemstore.md)         | Unregisters a specified system store.                                                                                                                                                                                                                                                                                                     |
| [**CryptUIWizExport**](cryptuiwizexport.md)                           | Presents a wizard that exports a certificate, certificate trust list (CTL), certificate revocation list (CRL), or certificate store.                                                                                                                                                                                                      |
| [**CryptUIWizImport**](cryptuiwizimport.md)                           | Presents a wizard that imports a certificate, certificate trust list (CTL), certificate revocation list (CRL), or certificate store.                                                                                                                                                                                                      |



 

### Certificate and Certificate Store Maintenance Functions

CryptoAPI provides a set of general certificate and certificate store maintenance functions.

| Function                                                                                                                              | Description                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**CertAddSerializedElementToStore**](certaddserializedelementtostore.md)                                                            | Adds the serialized certificate or CRL element to the store.                                   |
| [**CertCreateContext**](certcreatecontext.md)                                                                                        | Creates the specified context from the encoded bytes. The new context is not put into a store. |
| [**CertEnumSubjectInSortedCTL**](certenumsubjectinsortedctl.md)                                                                      | Enumerates the TrustedSubjects in a sorted CTL context.                                        |
| [**CertFindSubjectInCTL**](certfindsubjectinctl.md)                                                                                  | Finds the specified subject in a CTL.                                                          |
| [**CertFindSubjectInSortedCTL**](certfindsubjectinsortedctl.md)                                                                      | Finds the specified subject in a sorted CTL.                                                   |
| [**OpenPersonalTrustDBDialog**](openpersonaltrustdbdialog.md) and [**OpenPersonalTrustDBDialogEx**](openpersonaltrustdbdialogex.md) | Displays the **Certificates** dialog box.                                                      |



 

### Certificate Functions

Most [*Certificate*](security.c_gly#-security-certificate-gly) functions have related functions to deal with [*CRLs*](security.c_gly#-security-certificate-revocation-list-gly) and [*CTLs*](security.c_gly#-security-certificate-trust-list-gly). For more information about related CRL and CTL functions, see Certificate Revocation List Functions and Certificate Trust List Functions.

| Function                                                                             | Description                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddCertificateContextToStore**](certaddcertificatecontexttostore.md)         | Adds a certificate context to the certificate store.                                                                                                                                                                                            |
| [**CertAddCertificateLinkToStore**](certaddcertificatelinktostore.md)               | Adds a link in a certificate store to a certificate context in a different store.                                                                                                                                                               |
| [**CertAddEncodedCertificateToStore**](certaddencodedcertificatetostore.md)         | Converts the encoded certificate to a certificate context, and then adds the context to the certificate store.                                                                                                                                  |
| [**CertAddRefServerOcspResponse**](certaddrefserverocspresponse.md)                 | Increments the reference count for an **HCERT\_SERVER\_OCSP\_RESPONSE** handle.                                                                                                                                                                 |
| [**CertAddRefServerOcspResponseContext**](certaddrefserverocspresponsecontext.md)   | Increments the reference count for a [**CERT\_SERVER\_OCSP\_RESPONSE\_CONTEXT**](cert-server-ocsp-response-context.md) structure.                                                                                                              |
| [**CertCloseServerOcspResponse**](certcloseserverocspresponse.md)                   | Closes an [*online certificate status protocol*](security.o_gly#-security-online-certificate-status-protocol-gly) (OCSP) server response handle.                                               |
| [**CertCreateCertificateContext**](certcreatecertificatecontext.md)                 | Creates a certificate context from an encoded certificate. The created context is not put in a certificate store.                                                                                                                               |
| [**CertCreateSelfSignCertificate**](certcreateselfsigncertificate.md)               | Creates a self-signed certificate.                                                                                                                                                                                                              |
| [**CertDeleteCertificateFromStore**](certdeletecertificatefromstore.md)             | Deletes a certificate from the certificate store.                                                                                                                                                                                               |
| [**CertDuplicateCertificateContext**](certduplicatecertificatecontext.md)           | Duplicates a certificate context by incrementing its [*reference count*](security.r_gly#-security-reference-count-gly).                                                                                           |
| [**CertEnumCertificatesInStore**](certenumcertificatesinstore.md)                   | Enumerates the certificate contexts in the certificate store.                                                                                                                                                                                   |
| [**CertFindCertificateInStore**](certfindcertificateinstore.md)                     | Finds the first, or next, certificate context in the certificate store that meets a search criterion.                                                                                                                                           |
| [**CertFreeCertificateContext**](certfreecertificatecontext.md)                     | Frees a certificate context.                                                                                                                                                                                                                    |
| [**CertGetIssuerCertificateFromStore**](certgetissuercertificatefromstore.md)       | Gets a certificate context from the certificate store for the first, or next, issuer of the specified subject certificate.                                                                                                                      |
| [**CertGetServerOcspResponseContext**](certgetserverocspresponsecontext.md)         | Retrieves a non-blocking, time valid [*online certificate status protocol*](security.o_gly#-security-online-certificate-status-protocol-gly) (OCSP) response context for the specified handle. |
| [**CertGetSubjectCertificateFromStore**](certgetsubjectcertificatefromstore.md)     | Gets from the certificate store the subject certificate context, which is uniquely identified by its issuer and serial number.                                                                                                                  |
| [**CertGetValidUsages**](certgetvalidusages.md)                                     | Returns an array of usages that consist of the intersection of the valid usages for all certificates in an array of certificates.                                                                                                               |
| [**CertOpenServerOcspResponse**](certopenserverocspresponse.md)                     | Opens a handle to an [*online certificate status protocol*](security.o_gly#-security-online-certificate-status-protocol-gly) (OCSP) response associated with a server certificate chain.       |
| [**CertRetrieveLogoOrBiometricInfo**](certretrievelogoorbiometricinfo.md)           | Performs a URL retrieval of logo or biometric information specified in either the **szOID\_LOGOTYPE\_EXT** or **szOID\_BIOMETRIC\_EXT** certificate extension.                                                                                  |
| [**CertSelectCertificate**](certselectcertificate.md)                               | Presents a dialog box that allows the user to select certificates from a set of certificates that match a given criteria.                                                                                                                       |
| [**CertSelectCertificateChains**](certselectcertificatechains.md)                   | Retrieves certificate chains based on specified selection criteria.                                                                                                                                                                             |
| [**CertSelectionGetSerializedBlob**](certselectiongetserializedblob.md)             | A helper function used to retrieve a serialized certificate [*BLOB*](security.b_gly#-security-blob-gly) from a [**CERT\_SELECTUI\_INPUT**](cert-selectui-input.md) structure.                                               |
| [**CertSerializeCertificateStoreElement**](certserializecertificatestoreelement.md) | Serializes a certificate context's encoded certificate and an encoded representation of its properties.                                                                                                                                         |
| [**CertVerifySubjectCertificateContext**](certverifysubjectcertificatecontext.md)   | Performs the enabled verification checks on the subject certificate using the issuer.                                                                                                                                                           |
| [**CryptUIDlgCertMgr**](cryptuidlgcertmgr.md)                                       | Displays a dialog box that allows the user to manage certificates.                                                                                                                                                                              |
| [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md)                   | Displays a dialog box that allows a user to select a certificate.                                                                                                                                                                               |
| [**CryptUIDlgSelectCertificateFromStore**](cryptuidlgselectcertificatefromstore.md) | Displays a dialog box that allows the selection of a certificate from a specified store.                                                                                                                                                        |
| [**CryptUIDlgViewCertificate**](cryptuidlgviewcertificate.md)                       | Presents a dialog box that displays a specified certificate.                                                                                                                                                                                    |
| [**CryptUIDlgViewContext**](cryptuidlgviewcontext.md)                               | Displays a certificate, CRL, or CTL.                                                                                                                                                                                                            |
| [**CryptUIDlgViewSignerInfo**](cryptuidlgviewsignerinfo.md)                         | Displays a dialog box that contains the signer information for a signed message.                                                                                                                                                                |
| [**GetFriendlyNameOfCert**](getfriendlynameofcert.md)                               | Retrieves the display name for a certificate.                                                                                                                                                                                                   |
| [**RKeyCloseKeyService**](rkeyclosekeyservice.md)                                   | Closes a key service handle.                                                                                                                                                                                                                    |
| [**RKeyOpenKeyService**](rkeyopenkeyservice.md)                                     | Opens a key service handle on a remote computer.                                                                                                                                                                                                |
| [**RKeyPFXInstall**](rkeypfxinstall.md)                                             | Installs a certificate on a remote computer.                                                                                                                                                                                                    |



 

### Certificate Revocation List Functions

These functions manage the storage and retrieval of [*certificate revocation lists*](security.c_gly#-security-certificate-revocation-list-gly) (CRLs).

| Function                                                             | Description                                                                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAddCRLContextToStore**](certaddcrlcontexttostore.md)         | Adds a CRL context to the certificate store.                                                                                                                                          |
| [**CertAddCRLLinkToStore**](certaddcrllinktostore.md)               | Adds a link in a store to a CRL context in a different store.                                                                                                                         |
| [**CertAddEncodedCRLToStore**](certaddencodedcrltostore.md)         | Converts the encoded CRL to a CRL context, and then adds the context to the certificate store.                                                                                        |
| [**CertCreateCRLContext**](certcreatecrlcontext.md)                 | Creates a CRL context from an encoded CRL. The created context is not put in a certificate store.                                                                                     |
| [**CertDeleteCRLFromStore**](certdeletecrlfromstore.md)             | Deletes a CRL from the certificate store.                                                                                                                                             |
| [**CertDuplicateCRLContext**](certduplicatecrlcontext.md)           | Duplicates a CRL context by incrementing the [*reference count*](security.r_gly#-security-reference-count-gly).                                         |
| [**CertEnumCRLsInStore**](certenumcrlsinstore.md)                   | Enumerates the CRL contexts in a store.                                                                                                                                               |
| [**CertFindCertificateInCRL**](certfindcertificateincrl.md)         | Searches the [*certificate revocation list*](security.c_gly#-security-certificate-revocation-list-gly) (CRL) for the specified certificate. |
| [**CertFindCRLInStore**](certfindcrlinstore.md)                     | Finds the first, or next, CRL context in the certificate store that matches a specific criterion.                                                                                     |
| [**CertFreeCRLContext**](certfreecrlcontext.md)                     | Frees a CRL context.                                                                                                                                                                  |
| [**CertGetCRLFromStore**](certgetcrlfromstore.md)                   | Gets the first, or next, CRL context from the certificate store for the specified issuer certificate.                                                                                 |
| [**CertSerializeCRLStoreElement**](certserializecrlstoreelement.md) | Serializes the CRL context's encoded CRL and its properties.                                                                                                                          |



 

### Certificate Trust List Functions

These functions manage the storage and retrieval of [*certificate trust lists*](security.c_gly#-security-certificate-trust-list-gly) (CTLs).

| Function                                                               | Description                                                                                                          |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**CertAddCTLContextToStore**](certaddctlcontexttostore.md)           | Adds a CTL context to the certificate store.                                                                         |
| [**CertAddCTLLinkToStore**](certaddctllinktostore.md)                 | Adds a link in a store to a CRL context in a different store.                                                        |
| [**CertAddEncodedCTLToStore**](certaddencodedctltostore.md)           | Converts the encoded CTL to a CTL context, and then adds the context to the certificate store.                       |
| [**CertCreateCTLContext**](certcreatectlcontext.md)                   | Creates a CTL context from an encoded certificate trust list. The created context is not put in a certificate store. |
| [**CertDeleteCTLFromStore**](certdeletectlfromstore.md)               | Deletes a CTL from the certificate store.                                                                            |
| [**CertDuplicateCTLContext**](certduplicatectlcontext.md)             | Duplicates a CTL context by incrementing the reference count.                                                        |
| [**CertEnumCTLsInStore**](certenumctlsinstore.md)                     | Enumerates the CTL contexts in the certificate store.                                                                |
| [**CertFindCTLInStore**](certfindctlinstore.md)                       | Finds the first, or next, CTL context in the certificate store that matches a specific criteria.                     |
| [**CertFreeCTLContext**](certfreectlcontext.md)                       | Frees a CTL context.                                                                                                 |
| [**CertModifyCertificatesToTrust**](certmodifycertificatestotrust.md) | Modifies the set of certificates in a CTL for a given purpose.                                                       |
| [**CertSerializeCTLStoreElement**](certserializectlstoreelement.md)   | Serializes the CTL context's encoded CTL and its properties.                                                         |



 

### Extended Property Functions

The following functions work with extended properties of certificates, CRLs, and CTLs.

| Function                                                                             | Description                                                      |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**CertEnumCertificateContextProperties**](certenumcertificatecontextproperties.md) | Enumerates the properties for the specified certificate context. |
| [**CertEnumCRLContextProperties**](certenumcrlcontextproperties.md)                 | Enumerates the properties for the specified CRL context.         |
| [**CertEnumCTLContextProperties**](certenumctlcontextproperties.md)                 | Enumerates the properties for the specified CTL context.         |
| [**CertGetCertificateContextProperty**](certgetcertificatecontextproperty.md)       | Retrieves certificate properties.                                |
| [**CertGetCRLContextProperty**](certgetcrlcontextproperty.md)                       | Retrieves CRL properties.                                        |
| [**CertGetCTLContextProperty**](certgetctlcontextproperty.md)                       | Retrieves CTL properties.                                        |
| [**CertSetCertificateContextProperty**](certsetcertificatecontextproperty.md)       | Sets certificate properties.                                     |
| [**CertSetCRLContextProperty**](certsetcrlcontextproperty.md)                       | Sets CRL properties.                                             |
| [**CertSetCTLContextProperty**](certsetctlcontextproperty.md)                       | Sets CTL properties.                                             |



 

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
| [**CertVerifyCTLUsage**](certverifyctlusage.md)                 | Verifies the usage of a CTL.                 |
| [**CryptMsgEncodeAndSignCTL**](cryptmsgencodeandsignctl.md)     | Encodes and signs a CTL as a message.        |
| [**CryptMsgGetAndVerifySigner**](cryptmsggetandverifysigner.md) | Retrieves and verifies a CTL from a message. |
| [**CryptMsgSignCTL**](cryptmsgsignctl.md)                       | Signs a message that contains a CTL.         |



 

### Certificate Chain Verification Functions

Certificate chains are built to provide trust information about individual certificates.

| Function Name                                                                                                    | Description                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertCreateCertificateChainEngine**](certcreatecertificatechainengine.md)                                     | Creates a new, nondefault chain engine for an application.                                                                                                                                                          |
| [**CertCreateCTLEntryFromCertificateContextProperties**](certcreatectlentryfromcertificatecontextproperties.md) | Creates a CTL entry whose attributes are the certificate context's properties.                                                                                                                                      |
| [**CertDuplicateCertificateChain**](certduplicatecertificatechain.md)                                           | Duplicates a certificate chain by incrementing the chain's [*reference count*](security.r_gly#-security-reference-count-gly) and returning a pointer to the chain.                    |
| [**CertFindChainInStore**](certfindchaininstore.md)                                                             | Finds the first, or next, certificate chain context in a store.                                                                                                                                                     |
| [**CertFreeCertificateChain**](certfreecertificatechain.md)                                                     | Frees a certificate chain by reducing its reference count.                                                                                                                                                          |
| [**CertFreeCertificateChainEngine**](certfreecertificatechainengine.md)                                         | Frees a nondefault certificate chain engine.                                                                                                                                                                        |
| [**CertFreeCertificateChainList**](certfreecertificatechainlist.md)                                             | Frees the array of pointers to chain contexts.                                                                                                                                                                      |
| [**CertGetCertificateChain**](certgetcertificatechain.md)                                                       | Builds a chain context starting from an end certificate and going back to a trusted [*root certificate*](security.r_gly#-security-root-certificate-gly), if possible.                |
| [**CertIsValidCRLForCertificate**](certisvalidcrlforcertificate.md)                                             | Checks a [*CRL*](security.c_gly#-security-certificate-revocation-list-gly) to determine whether it would include a specific certificate if that certificate were revoked. |
| [**CertSetCertificateContextPropertiesFromCTLEntry**](certsetcertificatecontextpropertiesfromctlentry.md)       | Sets properties on the certificate context using the attributes in the CTL entry.                                                                                                                                   |
| [**CertVerifyCertificateChainPolicy**](certverifycertificatechainpolicy.md)                                     | Checks a certificate chain to verify its validity, including its compliance with any specified validity policy criteria.                                                                                            |



 

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
| [**CryptMsgCalculateEncodedLength**](cryptmsgcalculateencodedlength.md)                   | Calculates the length of an encoded cryptographic message.                                                                                                                                                                     |
| [**CryptMsgClose**](cryptmsgclose.md)                                                     | Closes a handle of a cryptographic message.                                                                                                                                                                                    |
| [**CryptMsgControl**](cryptmsgcontrol.md)                                                 | Performs a special control function after the final [**CryptMsgUpdate**](cryptmsgupdate.md) of an encoded or decoded cryptographic message.                                                                                   |
| [**CryptMsgCountersign**](cryptmsgcountersign.md)                                         | Countersigns an already existing signature in a message.                                                                                                                                                                       |
| [**CryptMsgCountersignEncoded**](cryptmsgcountersignencoded.md)                           | Countersigns an already existing signature (encoded SignerInfo, as defined by PKCS \#7).                                                                                                                                       |
| [**CryptMsgDuplicate**](cryptmsgduplicate.md)                                             | Duplicates a cryptographic message handle by incrementing the [*reference count*](security.r_gly#-security-reference-count-gly). The reference count keeps track of the lifetime of the message. |
| [**CryptMsgGetParam**](cryptmsggetparam.md)                                               | Acquires a parameter after encoding or decoding a cryptographic message.                                                                                                                                                       |
| [**CryptMsgOpenToDecode**](cryptmsgopentodecode.md)                                       | Opens a cryptographic message for decoding.                                                                                                                                                                                    |
| [**CryptMsgOpenToEncode**](cryptmsgopentoencode.md)                                       | Opens a cryptographic message for encoding.                                                                                                                                                                                    |
| [**CryptMsgUpdate**](cryptmsgupdate.md)                                                   | Updates the contents of a cryptographic message.                                                                                                                                                                               |
| [**CryptMsgVerifyCountersignatureEncoded**](cryptmsgverifycountersignatureencoded.md)     | Verifies a [*countersignature*](security.c_gly#-security-countersignature-gly) in terms of the SignerInfo structure (as defined by PKCS \#7).                                                   |
| [**CryptMsgVerifyCountersignatureEncodedEx**](cryptmsgverifycountersignatureencodedex.md) | Verifies that the *pbSignerInfoCounterSignature* parameter contains the encrypted [*hash*](security.h_gly#-security-hash-gly) of the **encryptedDigest** field of the *pbSignerInfo* parameter structure.   |



 

### Simplified Message Functions

[*Simplified message functions*](security.s_gly#-security-simplified-message-functions-gly) wrap Low-level Message Functions into a single function to accomplish a specified task.

| Function                                                                               | Description                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptDecodeMessage**](cryptdecodemessage.md)                                       | Decodes a cryptographic message.                                                                                                                                                                                                                                             |
| [**CryptDecryptAndVerifyMessageSignature**](cryptdecryptandverifymessagesignature.md) | Decrypts the specified message, and verifies the signer.                                                                                                                                                                                                                     |
| [**CryptDecryptMessage**](cryptdecryptmessage.md)                                     | Decrypts the specified message.                                                                                                                                                                                                                                              |
| [**CryptEncryptMessage**](cryptencryptmessage.md)                                     | Encrypts the message for the recipient or recipients.                                                                                                                                                                                                                        |
| [**CryptGetMessageCertificates**](cryptgetmessagecertificates.md)                     | Returns the [*certificate store*](security.c_gly#-security-certificate-store-gly) that contains the message's certificates and [*CRLs*](security.c_gly#-security-certificate-revocation-list-gly). |
| [**CryptGetMessageSignerCount**](cryptgetmessagesignercount.md)                       | Returns the count of signers in the signed message.                                                                                                                                                                                                                          |
| [**CryptHashMessage**](crypthashmessage.md)                                           | Creates a hash of the message.                                                                                                                                                                                                                                               |
| [**CryptSignAndEncryptMessage**](cryptsignandencryptmessage.md)                       | Signs the message, and then encrypts it for the recipient or recipients.                                                                                                                                                                                                     |
| [**CryptSignMessageWithKey**](cryptsignmessagewithkey.md)                             | Signs a message using a CSP's private key specified in the parameters to the function.                                                                                                                                                                                       |
| [**CryptSignMessage**](cryptsignmessage.md)                                           | Signs the message.                                                                                                                                                                                                                                                           |
| [**CryptVerifyDetachedMessageHash**](cryptverifydetachedmessagehash.md)               | Verifies a hashed message that contains a detached hash.                                                                                                                                                                                                                     |
| [**CryptVerifyDetachedMessageSignature**](cryptverifydetachedmessagesignature.md)     | Verifies a signed message that contains a detached signature or signatures.                                                                                                                                                                                                  |
| [**CryptVerifyMessageHash**](cryptverifymessagehash.md)                               | Verifies a hashed message.                                                                                                                                                                                                                                                   |
| [**CryptVerifyMessageSignature**](cryptverifymessagesignature.md)                     | Verifies a signed message.                                                                                                                                                                                                                                                   |
| [**CryptVerifyMessageSignatureWithKey**](cryptverifymessagesignaturewithkey.md)       | Verifies a signed message's signature by using specified public key information.                                                                                                                                                                                             |



 

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
<td>[<strong>CertCompareCertificate</strong>](certcomparecertificate.md)</td>
<td>Compares two certificates to determine whether they are identical.</td>
</tr>
<tr class="even">
<td>[<strong>CertCompareCertificateName</strong>](certcomparecertificatename.md)</td>
<td>Compares two certificate names to determine whether they are identical.</td>
</tr>
<tr class="odd">
<td>[<strong>CertCompareIntegerBlob</strong>](certcompareintegerblob.md)</td>
<td>Compares two integer [<em>BLOBs</em>](security.b_gly#-security-blob-gly).</td>
</tr>
<tr class="even">
<td>[<strong>CertComparePublicKeyInfo</strong>](certcomparepublickeyinfo.md)</td>
<td>Compares two [<em>public keys</em>](security.p_gly#-security-public-key-gly) to determine whether they are identical.</td>
</tr>
<tr class="odd">
<td>[<strong>CertFindAttribute</strong>](certfindattribute.md)</td>
<td>Finds the first attribute identified by its [<em>object identifier</em>](security.o_gly#-security-object-identifier-gly) (OID).</td>
</tr>
<tr class="even">
<td>[<strong>CertFindExtension</strong>](certfindextension.md)</td>
<td>Finds the first extension identified by its OID.</td>
</tr>
<tr class="odd">
<td>[<strong>CertFindRDNAttr</strong>](certfindrdnattr.md)</td>
<td>Finds the first [<em>RDN</em>](security.r_gly#-security-relative-distinguished-name-gly) attribute identified by its OID in the name list of the <em>Relative Distinguished Names</em>.</td>
</tr>
<tr class="even">
<td>[<strong>CertGetIntendedKeyUsage</strong>](certgetintendedkeyusage.md)</td>
<td>Acquires the intended key usage bytes from the certificate.</td>
</tr>
<tr class="odd">
<td>[<strong>CertGetPublicKeyLength</strong>](certgetpublickeylength.md)</td>
<td>Acquires the public/private key's bit length from the [<em>public key BLOB</em>](security.p_gly#-security-public-key-blob-gly).</td>
</tr>
<tr class="even">
<td>[<strong>CertIsRDNAttrsInCertificateName</strong>](certisrdnattrsincertificatename.md)</td>
<td>Compares the attributes in the [<em>certificate name</em>](security.c_gly#-security-certificate-name-blob-gly) with the specified [<strong>CERT_RDN</strong>](cert-rdn.md) to determine whether all attributes are included there.</td>
</tr>
<tr class="odd">
<td>[<strong>CertIsStrongHashToSign</strong>](certisstronghashtosign.md)</td>
<td>Determines whether the specified hash algorithm and the public key in the signing certificate can be used to perform strong signing.</td>
</tr>
<tr class="even">
<td>[<strong>CertVerifyCRLRevocation</strong>](certverifycrlrevocation.md)</td>
<td>Verifies that the subject certificate is not on the [<em>certificate revocation list</em>](security.c_gly#-security-certificate-revocation-list-gly) (CRL).</td>
</tr>
<tr class="odd">
<td>[<strong>CertVerifyCRLTimeValidity</strong>](certverifycrltimevalidity.md)</td>
<td>Verifies the time validity of a CRL.</td>
</tr>
<tr class="even">
<td>[<strong>CertVerifyRevocation</strong>](certverifyrevocation.md)</td>
<td>Verifies that the subject certificate is not on the CRL.</td>
</tr>
<tr class="odd">
<td>[<strong>CertVerifyTimeValidity</strong>](certverifytimevalidity.md)</td>
<td>Verifies the time validity of a certificate.</td>
</tr>
<tr class="even">
<td>[<strong>CertVerifyValidityNesting</strong>](certverifyvaliditynesting.md)</td>
<td>Verifies that the subject's time validity nests within the issuer's time validity.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptExportPKCS8</strong>](cryptexportpkcs8.md)</td>
<td>This function is superseded by the [<strong>CryptExportPKCS8Ex</strong>](cryptexportpkcs8ex.md) function.</td>
</tr>
<tr class="even">
<td>[<strong>CryptExportPKCS8Ex</strong>](cryptexportpkcs8ex.md)</td>
<td>Exports the private key in PKCS #8 format.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptExportPublicKeyInfo</strong>](cryptexportpublickeyinfo.md)</td>
<td>Exports the public key information associated with the provider's corresponding private key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptExportPublicKeyInfoEx</strong>](cryptexportpublickeyinfoex.md)</td>
<td>Exports the public key information associated with the provider's corresponding private key. This function differs from [<strong>CryptExportPublicKeyInfo</strong>](cryptexportpublickeyinfo.md) in that the user can specify the public key algorithm, thereby overriding the default provided by the CSP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptExportPublicKeyInfoFromBCryptKeyHandle</strong>](cryptexportpublickeyinfofrombcryptkeyhandle.md)</td>
<td>Exports the public key info associated with a provider's corresponding private key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptFindCertificateKeyProvInfo</strong>](cryptfindcertificatekeyprovinfo.md)</td>
<td>Enumerates the cryptographic providers and their [<em>key containers</em>](security.k_gly#-security-key-container-gly) to find the private key that corresponds to a certificate's public key.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptFindLocalizedName</strong>](cryptfindlocalizedname.md)</td>
<td>Finds the localized name for a specified name, for example, finds the localized name for the store name of the Root system.</td>
</tr>
<tr class="even">
<td>[<strong>CryptHashCertificate</strong>](crypthashcertificate.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Hashes the encoded content.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptHashCertificate2</strong>](crypthashcertificate2.md)</td>
<td>Hashes a block of data by using a Cryptography API: Next Generation (CNG) hash provider.</td>
</tr>
<tr class="even">
<td>[<strong>CryptHashPublicKeyInfo</strong>](crypthashpublickeyinfo.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Computes the hash of the encoded public key information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptHashToBeSigned</strong>](crypthashtobesigned.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Computes the hash of the &quot;to be signed&quot; information in the encoded signed content ([<strong>CERT_SIGNED_CONTENT_INFO</strong>](cert-signed-content-info.md)).</td>
</tr>
<tr class="even">
<td>[<strong>CryptImportPKCS8</strong>](cryptimportpkcs8.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Imports the [<em>private key</em>](security.p_gly#-security-private-key-gly) in PKCS #8 format to a [<em>cryptographic service provider</em>](security.c_gly#-security-cryptographic-service-provider-gly) (CSP).</td>
</tr>
<tr class="odd">
<td>[<strong>CryptImportPublicKeyInfo</strong>](cryptimportpublickeyinfo.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Converts and imports public key information into the provider, and returns a handle of the public key.</td>
</tr>
<tr class="even">
<td>[<strong>CryptImportPublicKeyInfoEx</strong>](cryptimportpublickeyinfoex.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Converts and imports the public key information into the provider, and returns a handle of the public key. Additional parameters (over those specified by [<strong>CryptImportPublicKeyInfo</strong>](cryptimportpublickeyinfo.md)) that can be used to override defaults are provided to supplement [<strong>CERT_PUBLIC_KEY_INFO</strong>](cert-public-key-info.md).</td>
</tr>
<tr class="odd">
<td>[<strong>CryptImportPublicKeyInfoEx2</strong>](cryptimportpublickeyinfoex2.md)</td>
<td>Imports a public key into a CNG asymmetric provider.</td>
</tr>
<tr class="even">
<td>[<strong>CryptMemAlloc</strong>](cryptmemalloc.md)</td>
<td>Allocates memory for a buffer. This memory is used by all Crypt32.lib functions that return allocated buffers.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptMemFree</strong>](cryptmemfree.md)</td>
<td>Frees memory allocated by [<strong>CryptMemAlloc</strong>](cryptmemalloc.md) or [<strong>CryptMemRealloc</strong>](cryptmemrealloc.md).</td>
</tr>
<tr class="even">
<td>[<strong>CryptMemRealloc</strong>](cryptmemrealloc.md)</td>
<td>Frees memory currently allocated for a buffer, and allocates memory for a new buffer.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptQueryObject</strong>](cryptqueryobject.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Retrieves information about the content of a BLOB or a file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSignAndEncodeCertificate</strong>](cryptsignandencodecertificate.md)</td>
<td>Encodes the &quot;to be signed&quot; information, signs this encoded information, and encodes the resulting signed, encoded information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSignCertificate</strong>](cryptsigncertificate.md)</td>
<td>Signs the &quot;to be signed&quot; information in the encoded, signed content.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPAddProvider</strong>](cryptsipaddprovider.md)</td>
<td>Adds a Subject Interface Package (SIP).</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPCreateIndirectData</strong>](cryptsipcreateindirectdata.md)</td>
<td>Returns a [<strong>SIP_INDIRECT_DATA</strong>](sip-indirect-data.md) structure that contains a [<em>hash</em>](security.h_gly#-security-hash-gly) of the supplied [<strong>SIP_SUBJECTINFO</strong>](sip-subjectinfo.md) structure, the digest algorithm, and an encoding attribute. The hash can be used as an indirect reference to the data.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPGetCaps</strong>](cryptsipgetcaps.md)</td>
<td>Retrieves the capabilities of an SIP.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPGetSignedDataMsg</strong>](cryptsipgetsigneddatamsg.md)</td>
<td>Retrieves an Authenticode signature from the file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPLoad</strong>](cryptsipload.md)</td>
<td>Loads the dynamic link library that implements a subject interface package and assigns appropriate library export functions to a [<strong>SIP_DISPATCH_INFO</strong>](sip-dispatch-info.md) structure.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPPutSignedDataMsg</strong>](cryptsipputsigneddatamsg.md)</td>
<td>Stores an Authenticode Signature in the target file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPRemoveProvider</strong>](cryptsipremoveprovider.md)</td>
<td>Removes a SIP added by a previous call to the [<strong>CryptSIPAddProvider</strong>](cryptsipaddprovider.md) function.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPRemoveSignedDataMsg</strong>](cryptsipremovesigneddatamsg.md)</td>
<td>Removes a specified Authenticode signature.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPRetrieveSubjectGuid</strong>](cryptsipretrievesubjectguid.md)</td>
<td>Retrieves a GUID based on the header information in a specified file.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptSIPRetrieveSubjectGuidForCatalogFile</strong>](cryptsipretrievesubjectguidforcatalogfile.md)</td>
<td>Retrieves the subject GUID associated with the specified file.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSIPVerifyIndirectData</strong>](cryptsipverifyindirectdata.md)</td>
<td>Validates the indirect hashed data against the supplied subject.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptUpdateProtectedState</strong>](cryptupdateprotectedstate.md)</td>
<td>Migrates the current user's master keys after the user's [<em>security identifier</em>](security.s_gly#-security-security-identifier-gly) (SID) has changed.</td>
</tr>
<tr class="even">
<td>[<strong>CryptVerifyCertificateSignature</strong>](cryptverifycertificatesignature.md)</td>
<td>Verifies the signature of a subject certificate or a [<em>CRL</em>](security.c_gly#-security-certificate-revocation-list-gly) by using the public key information.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptVerifyCertificateSignatureEx</strong>](cryptverifycertificatesignatureex.md)</td>
<td>An extended version of [<strong>CryptVerifyCertificateSignature</strong>](cryptverifycertificatesignature.md).</td>
</tr>
<tr class="even">
<td>[<strong>GetEncSChannel</strong>](getencschannel.md)</td>
<td>Stores the encrypted Schannel DLL contents in memory.</td>
</tr>
<tr class="odd">
<td>[<strong>pCryptSIPGetCaps</strong>](pfncryptsipgetcaps.md)</td>
<td>Implemented by an SIP to report capabilities.</td>
</tr>
</tbody>
</table>



 

### Data Conversion Functions

The following CryptoAPI functions convert certificate structure members to different forms.

| Function                                           | Description                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertAlgIdToOID**](certalgidtooid.md)           | Converts a CryptoAPI algorithm identifier (ALG\_ID) to an [*Abstract Syntax Notation One*](security.a_gly#-security-abstract-syntax-notation-one-gly) (ASN.1) [*object identifier*](security.o_gly#-security-object-identifier-gly) (OID) string. |
| [**CertGetNameString**](certgetnamestring.md)     | Acquires the subject or issuer name from a certificate, and converts it to a null-terminated character string.                                                                                                                                                                                                               |
| [**CertNameToStr**](certnametostr.md)             | Converts a certificate name [*BLOB*](security.b_gly#-security-blob-gly) to a zero-terminated string.                                                                                                                                                                                                      |
| [**CertOIDToAlgId**](certoidtoalgid.md)           | Converts the ASN.1 Object Identifier string to the CSP algorithm identifier.                                                                                                                                                                                                                                                 |
| [**CertRDNValueToStr**](certrdnvaluetostr.md)     | Converts a Name Value to a null-terminated string.                                                                                                                                                                                                                                                                           |
| [**CertStrToName**](certstrtoname.md)             | Converts a null-terminated [*X.500*](security.x_gly#-security-x-500-gly) string to an encoded certificate name.                                                                                                                                                                                          |
| [**CryptBinaryToString**](cryptbinarytostring.md) | Converts a binary sequence into a formatted string.                                                                                                                                                                                                                                                                          |
| [**CryptFormatObject**](cryptformatobject.md)     | Formats encoded data, and returns a Unicode string.                                                                                                                                                                                                                                                                          |
| [**CryptStringToBinary**](cryptstringtobinary.md) | Converts a formatted string to a binary sequence.                                                                                                                                                                                                                                                                            |



 

### Enhanced Key Usage Functions

The following functions deal with the [*enhanced key usage*](security.e_gly#-security-enhanced-key-usage-gly) (EKU) extension and the EKU extended property of certificates. The EKU extension and extended property specify and limit the valid uses of a certificate. The extensions are part of the certificate itself. They are set by the issuer of the certificate and are read-only. Certificate-extended properties are values associated with a certificate that can be set in an application.

| Function                                                                             | Description                                                                    |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**CertAddEnhancedKeyUsageIdentifier**](certaddenhancedkeyusageidentifier.md)       | Adds a usage identifier to a certificate's EKU property.                       |
| [**CertGetEnhancedKeyUsage**](certgetenhancedkeyusage.md)                           | Acquires, from a certificate, information about the EKU extension or property. |
| [**CertRemoveEnhancedKeyUsageIdentifier**](certremoveenhancedkeyusageidentifier.md) | Removes the usage identifier from a certificate's EKU extended property.       |
| [**CertSetEnhancedKeyUsage**](certsetenhancedkeyusage.md)                           | Sets the EKU property for a certificate.                                       |



 

### Key Identifier Functions

Key identifier functions allow the user to create, set, retrieve, or locate a key identifier or its properties.

A key identifier is the unique identifier of a [*public/private key pair*](security.p_gly#-security-public-private-key-pair-gly). It can be any unique identifier but is usually the 20-byte SHA1 hash of an encoded [**CERT\_PUBLIC\_KEY\_INFO**](cert-public-key-info.md) structure. A key identifier can be obtained through the certificate's CERT\_KEY\_IDENTIFIER\_PROP\_ID. The key identifier allows the use of that [*key pair*](security.k_gly#-security-key-pair-gly) to encrypt or decrypt messages without using the certificate.

Key identifiers are not associated with [*CRLs*](security.c_gly#-security-certificate-revocation-list-gly) or [*CTLs*](security.c_gly#-security-certificate-trust-list-gly).

A key identifier can have the same properties as a certificate context. For more information, see [**CertCreateContext**](certcreatecontext.md).

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
<td>[<strong>CryptCreateKeyIdentifierFromCSP</strong>](cryptcreatekeyidentifierfromcsp.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Creates a key identifier from a CSP's [<em>public key BLOB</em>](security.p_gly#-security-public-key-blob-gly).</td>
</tr>
<tr class="even">
<td>[<strong>CryptEnumKeyIdentifierProperties</strong>](cryptenumkeyidentifierproperties.md)</td>
<td>Enumerates key identifiers and their properties.</td>
</tr>
<tr class="odd">
<td>[<strong>CryptGetKeyIdentifierProperty</strong>](cryptgetkeyidentifierproperty.md)</td>
<td><blockquote>
[!Important]<br />
This API is deprecated. New and existing software should start using [Cryptography Next Generation APIs.](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376210%28v=vs.85%29.aspx) Microsoft may remove this API in future releases.
</blockquote>
<br/> Acquires a specific property from a specified key identifier.</td>
</tr>
<tr class="even">
<td>[<strong>CryptSetKeyIdentifierProperty</strong>](cryptsetkeyidentifierproperty.md)</td>
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

-   [**CryptEncodeObject**](cryptencodeobject.md)
-   [**CryptEncodeObjectEx**](cryptencodeobjectex.md)
-   [**CryptDecodeObject**](cryptdecodeobject.md)
-   [**CryptDecodeObjectEx**](cryptdecodeobjectex.md)
-   [**CertVerifyRevocation**](certverifyrevocation.md)
-   [**CertOpenStore**](certopenstore.md)

For an overview of this process, see [Extending CryptoAPI Functionality](extending-cryptoapi-functionality.md).

The following functions work with OIDs.

| Function                                                                       | Description                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptEnumOIDFunction**](cryptenumoidfunction.md)                           | Enumerates the registered OID functions identified by their encoding type, function name, and OID.                                                                                                                 |
| [**CryptEnumOIDInfo**](cryptenumoidinfo.md)                                   | Enumerates the registered OID information identified by their group, and calls *pfnEnumOIDInfo* for matches.                                                                                                       |
| [**CryptFindOIDInfo**](cryptfindoidinfo.md)                                   | Uses the specified key and group to find OID information.                                                                                                                                                          |
| [**CryptFreeOIDFunctionAddress**](cryptfreeoidfunctionaddress.md)             | Releases the handle count that was incremented and returned by [**CryptGetOIDFunctionAddress**](cryptgetoidfunctionaddress.md) or [**CryptGetDefaultOIDFunctionAddress**](cryptgetdefaultoidfunctionaddress.md). |
| [**CryptGetDefaultOIDDllList**](cryptgetdefaultoiddlllist.md)                 | Acquires the list of registered default DLL entries for the specified function set and encoding type.                                                                                                              |
| [**CryptGetDefaultOIDFunctionAddress**](cryptgetdefaultoidfunctionaddress.md) | Either acquires the first or next installed default function, or loads the DLL that contains the default function.                                                                                                 |
| [**CryptGetOIDFunctionAddress**](cryptgetoidfunctionaddress.md)               | Searches the list of installed functions for an encoding type and OID match. If a match is not found there, the registry is searched for a match.                                                                  |
| [**CryptGetOIDFunctionValue**](cryptgetoidfunctionvalue.md)                   | Acquires the value for the specified encoding type, function name, OID, and value name.                                                                                                                            |
| [**CryptInitOIDFunctionSet**](cryptinitoidfunctionset.md)                     | Initializes and returns a handle of the OID function set identified by the function name supplied.                                                                                                                 |
| [**CryptInstallOIDFunctionAddress**](cryptinstalloidfunctionaddress.md)       | Installs a set of callable OID function addresses.                                                                                                                                                                 |
| [**CryptRegisterDefaultOIDFunction**](cryptregisterdefaultoidfunction.md)     | Registers the DLL that contains the default function to be called for the specified encoding type and function name.                                                                                               |
| [**CryptRegisterOIDFunction**](cryptregisteroidfunction.md)                   | Registers the DLL that contains the function to be called for the specified encoding type, function name, and OID.                                                                                                 |
| [**CryptRegisterOIDInfo**](cryptregisteroidinfo.md)                           | Registers the OID information specified in the [**CRYPT\_OID\_INFO**](crypt-oid-info.md) structure, persisting it to the registry.                                                                                |
| [**CryptSetOIDFunctionValue**](cryptsetoidfunctionvalue.md)                   | Sets the value for the specified encoding type, function name, OID, and value name.                                                                                                                                |
| [**CryptUnregisterDefaultOIDFunction**](cryptunregisterdefaultoidfunction.md) | Removes the registration for the DLL that contains the default function to be called for the specified encoding type and function name.                                                                            |
| [**CryptUnregisterOIDFunction**](cryptunregisteroidfunction.md)               | Removes the registration for the DLL that contains the function to be called for the specified encoding type, function name, and OID.                                                                              |
| [**CryptUnregisterOIDInfo**](cryptunregisteroidinfo.md)                       | Removes the registration for the specified OID information.                                                                                                                                                        |



 

### Remote Object Retrieval Functions

The following functions allow the user to retrieve a Public Key Infrastructure (PKI) object, acquire the URL of a certificate, CTL, or CRL, or to extract a URL from an object.

| Function                                                     | Description                                                            |
|--------------------------------------------------------------|------------------------------------------------------------------------|
| [**CryptGetObjectUrl**](cryptgetobjecturl.md)               | Acquires the URL of the remote object from a certificate, CTL, or CRL. |
| [**CryptRetrieveObjectByUrl**](cryptretrieveobjectbyurl.md) | Retrieves the PKI object from a location specified by a URL.           |



 

### PFX Functions

The following functions support Personal Information Exchange (PFX) format [*BLOBs*](security.b_gly#-security-blob-gly).

| Function                                             | Description                                                                                                                                                                                                                                                                  |
|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PFXExportCertStore**](pfxexportcertstore.md)     | Exports from the referenced [*certificate store*](security.c_gly#-security-certificate-store-gly) the certificates and, if available, their associated [*private keys*](security.p_gly#-security-private-key-gly). |
| [**PFXExportCertStoreEx**](pfxexportcertstoreex.md) | Exports from the referenced certificate store the certificates and, if available, their associated private keys.                                                                                                                                                             |
| [**PFXImportCertStore**](pfximportcertstore.md)     | Imports a PFX BLOB, and returns the handle of a store that contains certificates and any associated private keys.                                                                                                                                                            |
| [**PFXIsPFXBlob**](pfxispfxblob.md)                 | Attempts to decode the outer layer of a BLOB as a PFX packet.                                                                                                                                                                                                                |
| [**PFXVerifyPassword**](pfxverifypassword.md)       | Attempts to decode the outer layer of a BLOB as a PFX packet and to decrypt it with the given password.                                                                                                                                                                      |



 

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
| [**CertSrvBackupClose**](certsrvbackupclose.md)                                 | Closes an opened file.                                                                                                |
| [**CertSrvBackupEnd**](certsrvbackupend.md)                                     | Ends a backup session.                                                                                                |
| [**CertSrvBackupFree**](certsrvbackupfree.md)                                   | Frees a buffer allocated by the backup and restore APIs.                                                              |
| [**CertSrvBackupGetBackupLogs**](certsrvbackupgetbackuplogs.md)                 | Returns a list of log files that need to be backed up.                                                                |
| [**CertSrvBackupGetDatabaseNames**](certsrvbackupgetdatabasenames.md)           | Returns a list of database files that need to be backed up.                                                           |
| [**CertSrvBackupGetDynamicFileList**](certsrvbackupgetdynamicfilelist.md)       | Retrieves the list of Certificate Services dynamic file names that need to be backed up for the given backup context. |
| [**CertSrvBackupOpenFile**](certsrvbackupopenfile.md)                           | Opens a file in preparation for backing it up.                                                                        |
| [**CertSrvBackupPrepare**](certsrvbackupprepare.md)                             | Prepares the database for the online backup.                                                                          |
| [**CertSrvBackupRead**](certsrvbackupread.md)                                   | Reads the contents of an opened file.                                                                                 |
| [**CertSrvBackupTruncateLogs**](certsrvbackuptruncatelogs.md)                   | Truncates the log files.                                                                                              |
| [**CertSrvIsServerOnline**](certsrvisserveronline.md)                           | Determines whether a Certificate Services server is online (actively running).                                        |
| [**CertSrvRestoreEnd**](certsrvrestoreend.md)                                   | Ends a restore session.                                                                                               |
| [**CertSrvRestoreGetDatabaseLocations**](certsrvrestoregetdatabaselocations.md) | Retrieves database locations (used for both backup and restore scenarios).                                            |
| [**CertSrvRestorePrepare**](certsrvrestoreprepare.md)                           | Begins a restore session.                                                                                             |
| [**CertSrvRestoreRegister**](certsrvrestoreregister.md)                         | Registers a restore operation.                                                                                        |
| [**CertSrvRestoreRegisterComplete**](certsrvrestoreregistercomplete.md)         | Completes a previously registered restore operation.                                                                  |
| [**CertSrvRestoreRegisterThroughFile**](certsrvrestoreregisterthroughfile.md)   | Registers a restore operation.                                                                                        |
| [**CertSrvServerControl**](certsrvservercontrol.md)                             | Sends a control command to the Certificate Services instance.                                                         |



 

## Callback Functions

The callback functions in this section are used to register or install application-defined [*certificate store*](security.c_gly#-security-certificate-store-gly) providers and to provide related functionality through callback functions. Callback functions are implemented by an application and are called by [*CryptoAPI*](security.c_gly#-security-cryptoapi-gly) functions. Callback functions enable the application to control, in part, the way that CryptoAPI functions manipulate data.

| Callback function                                                                                                        | Use                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CertChainFindByIssuerCallback**](certchainfindbyissuercallback.md)                                                   | An application-defined callback function that allows the application to filter certificates that might be added to the certificate chain.                                                                                                                                                                                                     |
| [**CertDllOpenStoreProv**](certdllopenstoreprov.md)                                                                     | Defines the store provider open function.                                                                                                                                                                                                                                                                                                     |
| [**CertEnumPhysicalStoreCallback**](certenumphysicalstorecallback.md)                                                   | Callback function used by the [**CertEnumPhysicalStore**](certenumphysicalstore.md) function to format and present information on each physical store found.                                                                                                                                                                                 |
| [**CertEnumSystemStoreCallback**](certenumsystemstorecallback.md)                                                       | Callback function used by the [**CertEnumSystemStore**](certenumsystemstore.md) function to format and present information on each physical store found.                                                                                                                                                                                     |
| [**CertEnumSystemStoreLocationCallback**](certenumsystemstorelocationcallback.md)                                       | Callback function used by the [**CertEnumSystemStoreLocation**](certenumsystemstorelocation.md) function to format and present information on each physical store found.                                                                                                                                                                     |
| [**CertStoreProvCloseCallback**](certstoreprovclosecallback.md)                                                         | Determines what happens when an open store's [*reference count*](security.r_gly#-security-reference-count-gly) becomes zero.                                                                                                                                                                                    |
| [**CertStoreProvControl**](certstoreprovcontrol.md)                                                                     | Allows an application to be notified when there is a difference between the contents of a cached store in use and the contents of that store as it is persisted to storage.                                                                                                                                                                   |
| [**CertStoreProvDeleteCertCallback**](certstoreprovdeletecertcallback.md)                                               | Determines actions to be taken before a certificate is deleted from a certificate store.                                                                                                                                                                                                                                                      |
| [**CertStoreProvDeleteCRLCallback**](certstoreprovdeletecrlcallback.md)                                                 | Determines actions to be taken before a [*certificate revocation list*](security.c_gly#-security-certificate-revocation-list-gly) (CRL) is deleted from a certificate store.                                                                                                                        |
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
| [**CertStoreProvReadCertCallback**](certstoreprovreadcertcallback.md)                                                   | Currently not used but might be exported to future CSPs.                                                                                                                                                                                                                                                                                      |
| [**CertStoreProvReadCRLCallback**](certstoreprovreadcrlcallback.md)                                                     | Currently not used but might be exported to future CSPs.                                                                                                                                                                                                                                                                                      |
| [**CertStoreProvReadCTL**](certstoreprovreadctl.md)                                                                     | Read the provider's copy of the CTL context, and, if it exists, create a new CTL context.                                                                                                                                                                                                                                                     |
| [**CertStoreProvSetCertPropertyCallback**](certstoreprovsetcertpropertycallback.md)                                     | Determines actions to be taken before a call to [**CertSetCertificateContextProperty**](certsetcertificatecontextproperty.md) or [**CertGetCertificateContextProperty**](certgetcertificatecontextproperty.md).                                                                                                                             |
| [**CertStoreProvSetCRLPropertyCallback**](certstoreprovsetcrlpropertycallback.md)                                       | Determines actions to be taken before a call to [**CertSetCRLContextProperty**](certsetcrlcontextproperty.md) or [**CertGetCRLContextProperty**](certgetcrlcontextproperty.md).                                                                                                                                                             |
| [**CertStoreProvSetCTLProperty**](certstoreprovsetctlproperty.md)                                                       | Determines whether a property can be set on a CTL.                                                                                                                                                                                                                                                                                            |
| [**CertStoreProvWriteCertCallback**](certstoreprovwritecertcallback.md)                                                 | Determines actions to be taken before adding a certificate to a store.                                                                                                                                                                                                                                                                        |
| [**CertStoreProvWriteCRLCallback**](certstoreprovwritecrlcallback.md)                                                   | Determines actions to be taken before adding a CRL to a store.                                                                                                                                                                                                                                                                                |
| [**CertStoreProvWriteCTL**](certstoreprovwritectl.md)                                                                   | Determines whether a CTL can be added to the store.                                                                                                                                                                                                                                                                                           |
| [**CRYPT\_ENUM\_KEYID\_PROP**](crypt-enum-keyid-prop.md)                                                                | Callback function used by the [**CryptEnumKeyIdentifierProperties**](cryptenumkeyidentifierproperties.md) function.                                                                                                                                                                                                                          |
| [**CRYPT\_ENUM\_OID\_FUNCTION**](crypt-enum-oid-function.md)                                                            | Callback function used by the [**CryptEnumOIDFunction**](cryptenumoidfunction.md) function.                                                                                                                                                                                                                                                  |
| [**CRYPT\_ENUM\_OID\_INFO**](crypt-enum-oid-info.md)                                                                    | Callback function used by the [**CryptEnumOIDInfo**](cryptenumoidinfo.md) function.                                                                                                                                                                                                                                                          |
| [**CryptGetSignerCertificateCallback**](cryptgetsignercertificatecallback.md)                                           | Callback function used with the [**CRYPT\_VERIFY\_MESSAGE\_PARA**](crypt-verify-message-para.md) structure to get and verify a message signer's certificate.                                                                                                                                                                                 |
| [**PCRYPT\_DECRYPT\_PRIVATE\_KEY\_FUNC**](pcrypt-decrypt-private-key-func.md)                                           | Callback function used by the [**CryptImportPKCS8**](cryptimportpkcs8.md) function.                                                                                                                                                                                                                                                          |
| [**PCRYPT\_ENCRYPT\_PRIVATE\_KEY\_FUNC**](pcrypt-encrypt-private-key-func.md)                                           | Callback function used when creating the [**CRYPT\_ENCRYPTED\_PRIVATE\_KEY\_INFO**](crypt-encrypted-private-key-info.md) structure.                                                                                                                                                                                                          |
| [**PCRYPT\_RESOLVE\_HCRYPTPROV\_FUNC**](pcrypt-resolve-hcryptprov-func.md)                                              | Callback function used by the [**CryptImportPKCS8**](cryptimportpkcs8.md) function.                                                                                                                                                                                                                                                          |
| [**PFN\_CDF\_PARSE\_ERROR\_CALLBACK**](pfn-cdf-parse-error-callback.md)                                                 | A user-defined function called for Catalog Definition Function errors while parsing a catalog definition file (CDF).                                                                                                                                                                                                                          |
| [**PFN\_CERT\_CREATE\_CONTEXT\_SORT\_FUNC**](pfn-cert-create-context-sort-func.md)                                      | Called for each sorted context entry when a context is created.                                                                                                                                                                                                                                                                               |
| [**PFN\_CMSG\_CNG\_IMPORT\_CONTENT\_ENCRYPT\_KEY**](pfn-cmsg-cng-import-content-encrypt-key.md)                         | A CNG [*object identifier*](security.o_gly#-security-object-identifier-gly) (OID) installable function for import of an already decrypted content encryption key (CEK).                                                                                                                                       |
| [**PFN\_CMSG\_CNG\_IMPORT\_KEY\_AGREE**](pfn-cmsg-cng-import-key-agree.md)                                              | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_CNG\_IMPORT\_KEY\_TRANS**](pfn-cmsg-cng-import-key-trans.md)                                              | A CNG OID installable function for import and [*decryption*](security.d_gly#-security-decryption-gly) of a key-transport-recipient, encrypted, content [*encryption*](security.e_gly#-security-encryption-gly) key (CEK).                                                                   |
| [**PFN\_CMSG\_EXPORT\_KEY\_AGREE**](pfn-cmsg-export-key-agree.md)                                                       | Encrypts and exports the content encryption key for a key agreement recipient of an enveloped message.                                                                                                                                                                                                                                        |
| [**PFN\_CMSG\_EXPORT\_KEY\_TRANS**](pfn-cmsg-export-key-trans.md)                                                       | Encrypts and exports the content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                        |
| [**PFN\_CMSG\_EXPORT\_MAIL\_LIST**](pfn-cmsg-export-mail-list.md)                                                       | Encrypts and exports the content encryption key for a mailing list recipient of an enveloped message.                                                                                                                                                                                                                                         |
| [**PFN\_CMSG\_GEN\_CONTENT\_ENCRYPT\_KEY**](pfn-cmsg-gen-content-encrypt-key.md)                                        | Generates the [*symmetric key*](security.s_gly#-security-symmetric-key-gly) used to encrypt content for an enveloped message.                                                                                                                                                                                     |
| [**PFN\_CMSG\_IMPORT\_KEY\_AGREE**](pfn-cmsg-import-key-agree.md)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_IMPORT\_KEY\_TRANS**](pfn-cmsg-import-key-trans.md)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CMSG\_IMPORT\_MAIL\_LIST**](pfn-cmsg-import-mail-list.md)                                                       | Imports a content encryption key for a key transport recipient of an enveloped message.                                                                                                                                                                                                                                                       |
| [**PFN\_CRYPT\_EXPORT\_PUBLIC\_KEY\_INFO\_EX2\_FUNC**](pfn-crypt-export-public-key-info-ex2-func.md)                    | Called by [**CryptExportPublicKeyInfoEx**](cryptexportpublickeyinfoex.md) to export a public key BLOB and encode it.                                                                                                                                                                                                                         |
| [**PFN\_CRYPT\_EXTRACT\_ENCODED\_SIGNATURE\_PARAMETERS\_FUNC**](pfn-crypt-extract-encoded-signature-parameters-func.md) | Called to decode and return the hash algorithm identifier and optionally the signature parameters.                                                                                                                                                                                                                                            |
| [**PFN\_CRYPT\_SIGN\_AND\_ENCODE\_HASH\_FUNC**](pfn-crypt-sign-and-encode-hash-func.md)                                 | Called to sign and encode a computed hash.                                                                                                                                                                                                                                                                                                    |
| [**PFN\_CRYPT\_VERIFY\_ENCODED\_SIGNATURE\_FUNC**](pfn-crypt-verify-encoded-signature-func.md)                          | Called to decrypt an encoded signature and compare it to a computed hash.                                                                                                                                                                                                                                                                     |
| [**PFN\_IMPORT\_PUBLIC\_KEY\_INFO\_EX2\_FUNC**](pfn-import-public-key-info-ex2-func.md)                                 | Called by [**CryptImportPublicKeyInfoEx2**](cryptimportpublickeyinfoex2.md) to decode the [*public key algorithm*](security.p_gly#-security-public-key-algorithm-gly) identifier, load the algorithm provider, and import the [*key pair*](security.k_gly#-security-key-pair-gly). |
| [**PFNCCERTDISPLAYPROC**](pfnccertdisplayproc.md)                                                                       | A user-defined callback function that allows the caller of the [**CryptUIDlgSelectCertificate**](cryptuidlgselectcertificate.md) function to handle the display of certificates that the user selects to view.                                                                                                                               |
| [**PFNCMFILTERPROC**](pfncmfilterproc.md)                                                                               | Filters each certificate to decide if it will appear in the certificate selection dialog box displayed by the [**CertSelectCertificate**](certselectcertificate.md) function.                                                                                                                                                                |
| [**PFNCMHOOKPROC**](pfncmhookproc.md)                                                                                   | Called before messages are processed by the certificate selection dialog box produced by the [**CertSelectCertificate**](certselectcertificate.md) function.                                                                                                                                                                                 |



 

## Catalog Definition Functions

These functions are used to create a catalog. All of these functions are called by [MakeCat](makecat.md).

| Function                                                                           | Description                                                                                                               |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**CryptCATCDFClose**](cryptcatcdfclose.md)                                       | Closes a catalog definition file and frees the memory for the corresponding [**CRYPTCATCDF**](cryptcatcdf.md) structure. |
| [**CryptCATCDFEnumAttributesWithCDFTag**](cryptcatcdfenumattributeswithcdftag.md) | Enumerates the attributes of member files in the **CatalogFiles** section of a CDF.                                       |
| [**CryptCATCDFEnumCatAttributes**](cryptcatcdfenumcatattributes.md)               | Enumerates catalog-level attributes within the **CatalogHeader** section of a CDF.                                        |
| [**CryptCATCDFEnumMembersByCDFTagEx**](cryptcatcdfenummembersbycdftagex.md)       | Enumerates the individual file members in the **CatalogFiles** section of a CDF.                                          |
| [**CryptCATCDFOpen**](cryptcatcdfopen.md)                                         | Opens an existing CDF for reading and initializes a [**CRYPTCATCDF**](cryptcatcdf.md) structure.                         |



 

## Catalog Functions

These functions are used to manage a catalog.

| Function                                                                             | Description                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CryptCATAdminAcquireContext**](cryptcatadminacquirecontext.md)                   | Acquires a handle to a catalog administrator context. This handle can be used by subsequent calls to the [**CryptCATAdminAddCatalog**](cryptcatadminaddcatalog.md), [**CryptCATAdminEnumCatalogFromHash**](cryptcatadminenumcatalogfromhash.md), and [**CryptCATAdminRemoveCatalog**](cryptcatadminremovecatalog.md) functions. |
| [**CryptCATAdminAcquireContext2**](cryptcatadminacquirecontext2.md)                 | Acquires a handle to a catalog administrator context for a given hash algorithm and hash policy.                                                                                                                                                                                                                                   |
| [**CryptCATAdminAddCatalog**](cryptcatadminaddcatalog.md)                           | Adds a catalog to the catalog database.                                                                                                                                                                                                                                                                                            |
| [**CryptCATAdminCalcHashFromFileHandle**](cryptcatadmincalchashfromfilehandle.md)   | Calculates the hash for a file.                                                                                                                                                                                                                                                                                                    |
| [**CryptCATAdminCalcHashFromFileHandle2**](cryptcatadmincalchashfromfilehandle2.md) | Calculates the hash for a file by using the specified algorithm.                                                                                                                                                                                                                                                                   |
| [**CryptCATAdminEnumCatalogFromHash**](cryptcatadminenumcatalogfromhash.md)         | Enumerates the catalogs that contain a specified hash.                                                                                                                                                                                                                                                                             |
| [**CryptCATAdminReleaseCatalogContext**](cryptcatadminreleasecatalogcontext.md)     | Releases a handle to a catalog context previously returned by the [**CryptCATAdminAddCatalog**](cryptcatadminaddcatalog.md) function.                                                                                                                                                                                             |
| [**CryptCATAdminReleaseContext**](cryptcatadminreleasecontext.md)                   | Releases the handle previously assigned by the [**CryptCATAdminAcquireContext**](cryptcatadminacquirecontext.md) function.                                                                                                                                                                                                        |
| [**CryptCATAdminRemoveCatalog**](cryptcatadminremovecatalog.md)                     | Deletes a catalog file and removes that catalog's entry from the Windows catalog database.                                                                                                                                                                                                                                         |
| [**CryptCATAdminResolveCatalogPath**](cryptcatadminresolvecatalogpath.md)           | Retrieves the fully qualified path of the specified catalog.                                                                                                                                                                                                                                                                       |
| [**CryptCATCatalogInfoFromContext**](cryptcatcataloginfofromcontext.md)             | Retrieves catalog information from a specified catalog context.                                                                                                                                                                                                                                                                    |
| [**CryptCATClose**](cryptcatclose.md)                                               | Closes a catalog handle opened previously by the [**CryptCATOpen**](cryptcatopen.md) function.                                                                                                                                                                                                                                    |
| [**CryptCATEnumerateAttr**](cryptcatenumerateattr.md)                               | Enumerates the attributes associated with a member of a catalog.                                                                                                                                                                                                                                                                   |
| [**CryptCATEnumerateCatAttr**](cryptcatenumeratecatattr.md)                         | Enumerates the attributes associated with a catalog.                                                                                                                                                                                                                                                                               |
| [**CryptCATEnumerateMember**](cryptcatenumeratemember.md)                           | Enumerates the members of a catalog.                                                                                                                                                                                                                                                                                               |
| [**CryptCATGetAttrInfo**](cryptcatgetattrinfo.md)                                   | Retrieves information about an attribute of a member of a catalog.                                                                                                                                                                                                                                                                 |
| [**CryptCATGetMemberInfo**](cryptcatgetmemberinfo.md)                               | Retrieves member information from the catalog's PKCS \#7. In addition to retrieving the member information for a specified reference tag, this function opens a member context.                                                                                                                                                    |
| [**CryptCATOpen**](cryptcatopen.md)                                                 | Opens a catalog, and returns a context handle to the open catalog.                                                                                                                                                                                                                                                                 |
| [**IsCatalogFile**](iscatalogfile.md)                                               | Retrieves a Boolean value that indicates whether the specified file is a catalog file.                                                                                                                                                                                                                                             |



 

## WinTrust Functions

The following functions are used to perform various trust operations.

| Function                                                                               | Description                                                                                                                                                          |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WintrustAddActionID**](wintrustaddactionid.md)                                     | Adds a trust provider action to the user's system.                                                                                                                   |
| [**WintrustGetRegPolicyFlags**](wintrustgetregpolicyflags.md)                         | Retrieves policy flags for a policy provider.                                                                                                                        |
| [**WintrustAddDefaultForUsage**](wintrustadddefaultforusage.md)                       | Specifies the default usage identifier and callback information for a provider                                                                                       |
| [**WintrustGetDefaultForUsage**](wintrustgetdefaultforusage.md)                       | Retrieves the default usage identifier and callback information.                                                                                                     |
| [**WintrustLoadFunctionPointers**](wintrustloadfunctionpointers.md)                   | Loads function entry points for a specified action GUID.                                                                                                             |
| [**WintrustRemoveActionID**](wintrustremoveactionid.md)                               | Removes an action added by the [**WintrustAddActionID**](wintrustaddactionid.md) function.                                                                          |
| [**WintrustSetDefaultIncludePEPageHashes**](wintrustsetdefaultincludepepagehashes.md) | Sets the default setting that determines whether page hashes are included when creating subject interface package (SIP) indirect data for portable executable files. |
| [**WintrustSetRegPolicyFlags**](wintrustsetregpolicyflags.md)                         | Sets policy flags for a policy provider.                                                                                                                             |
| [**WinVerifyTrust**](winverifytrust.md)                                               | Performs a trust verification action on a specified object.                                                                                                          |
| [**WinVerifyTrustEx**](winverifytrustex.md)                                           | Performs a trust verification action on a specified object and takes a pointer to a WINTRUST\_DATA structure.                                                        |
| [**WTHelperCertCheckValidSignature**](wthelpercertcheckvalidsignature.md)             | Checks whether a signature is valid.                                                                                                                                 |
| [**WTHelperCertFindIssuerCertificate**](wthelpercertfindissuercertificate.md)         | Finds an issuer certificate from the specified certificate stores that matches the specified subject certificate.                                                    |
| [**WTHelperCertIsSelfSigned**](wthelpercertisselfsigned.md)                           | Checks whether a certificate is self-signed.                                                                                                                         |
| [**WTHelperGetFileHash**](wthelpergetfilehash.md)                                     | Verifies the signature of a signed file and obtains the hash value and algorithm identifier for the file.                                                            |
| [**WTHelperGetProvCertFromChain**](wthelpergetprovcertfromchain.md)                   | Retrieves a trust provider certificate from the certificate chain.                                                                                                   |
| [**WTHelperGetProvPrivateDataFromChain**](wthelpergetprovprivatedatafromchain.md)     | Receives a [**CRYPT\_PROVIDER\_PRIVDATA**](crypt-provider-privdata.md) structure from the chain by using the provider ID.                                           |
| [**WTHelperGetProvSignerFromChain**](wthelpergetprovsignerfromchain.md)               | Retrieves a signer or countersigner by index from the chain.                                                                                                         |
| [**WTHelperProvDataFromStateData**](wthelperprovdatafromstatedata.md)                 | Retrieves trust provider information from a specified handle.                                                                                                        |



 

## Object Locator Functions

The following callback functions can be implemented by a custom provider that is intended to be called by the Secure Channel (Schannel) security package to retrieve certificates.



| Function                                                                                                             | Description                                             |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FLUSH**](pfn-crypt-object-locator-provider-flush.md)                      | Specifies that an object has changed.                   |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_GET**](pfn-crypt-object-locator-provider-get.md)                          | Retrieves an object.                                    |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_RELEASE**](pfn-crypt-object-locator-provider-release.md)                  | Releases the provider.                                  |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FREE\_PASSWORD**](pfn-crypt-object-locator-provider-free-password.md)     | Releases the password used to encrypt a PFX byte array. |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FREE**](pfn-crypt-object-locator-provider-free.md)                        | Releases the object returned by the provider.           |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_FREE\_IDENTIFIER**](pfn-crypt-object-locator-provider-free-identifier.md) | Releases memory for an object identifier.               |
| [**PFN\_CRYPT\_OBJECT\_LOCATOR\_PROVIDER\_INITIALIZE**](pfn-crypt-object-locator-provider-initialize.md)            | Initializes the provider.                               |



 

 

 




