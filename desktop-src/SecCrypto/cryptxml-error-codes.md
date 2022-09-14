---
description: The following are the run-time error codes, defined in Cryptxml.h, that may be returned by the CryptXML functions.
ms.assetid: c3678767-aab3-4771-b2f2-8d79545d420d
title: CryptXML Error Codes (Cryptxml.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CryptXML Error Codes

The following are the run-time error codes, defined in Cryptxml.h, that may be returned by the CryptXML functions.



| Constant/value                                                                                                                                                                                                                                                                             | Description                                                                                                        |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| <span id="CRYPT_XML_E_LARGE"></span><span id="crypt_xml_e_large"></span><dl> <dt>**CRYPT\_XML\_E\_LARGE**</dt> <dt>0x80092101L</dt> </dl>                                               | The supplied value is too large.<br/>                                                                        |
| <span id="CRYPT_XML_E_ENCODING"></span><span id="crypt_xml_e_encoding"></span><dl> <dt>**CRYPT\_XML\_E\_ENCODING**</dt> <dt>0x80092103L</dt> </dl>                                      | The specified XML encoding is unsupported.<br/>                                                              |
| <span id="CRYPT_XML_E_ALGORITHM"></span><span id="crypt_xml_e_algorithm"></span><dl> <dt>**CRYPT\_XML\_E\_ALGORITHM**</dt> <dt>0x80092104L</dt> </dl>                                   | The specified XML Algorithm is unsupported.<br/>                                                             |
| <span id="CRYPT_XML_E_TRANSFORM"></span><span id="crypt_xml_e_transform"></span><dl> <dt>**CRYPT\_XML\_E\_TRANSFORM**</dt> <dt>0x80092105L</dt> </dl>                                   | The specified transform is unsupported.<br/>                                                                 |
| <span id="CRYPT_XML_E_HANDLE"></span><span id="crypt_xml_e_handle"></span><dl> <dt>**CRYPT\_XML\_E\_HANDLE**</dt> <dt>0x80092106L</dt> </dl>                                            | The supplied handle is not valid.<br/>                                                                       |
| <span id="CRYPT_XML_E_OPERATION"></span><span id="crypt_xml_e_operation"></span><dl> <dt>**CRYPT\_XML\_E\_OPERATION**</dt> <dt>0x80092107L</dt> </dl>                                   | The operation is not valid.<br/>                                                                             |
| <span id="CRYPT_XML_E_UNRESOLVED_REFERENCE"></span><span id="crypt_xml_e_unresolved_reference"></span><dl> <dt>**CRYPT\_XML\_E\_UNRESOLVED\_REFERENCE**</dt> <dt>0x80092108L</dt> </dl> | Unable to resolve the **Reference** element.<br/>                                                            |
| <span id="CRYPT_XML_E_INVALID_DIGEST"></span><span id="crypt_xml_e_invalid_digest"></span><dl> <dt>**CRYPT\_XML\_E\_INVALID\_DIGEST**</dt> <dt>0x80092109L</dt> </dl>                   | The digest value is not valid.<br/>                                                                          |
| <span id="CRYPT_XML_E_INVALID_SIGNATURE"></span><span id="crypt_xml_e_invalid_signature"></span><dl> <dt>**CRYPT\_XML\_E\_INVALID\_SIGNATURE**</dt> <dt>0x8009210AL</dt> </dl>          | The signature value is not valid.<br/>                                                                       |
| <span id="CRYPT_XML_E_HASH_FAILED"></span><span id="crypt_xml_e_hash_failed"></span><dl> <dt>**CRYPT\_XML\_E\_HASH\_FAILED**</dt> <dt>0x8009210BL</dt> </dl>                            | Unable to create or calculate the hash.<br/>                                                                 |
| <span id="CRYPT_XML_E_SIGN_FAILED"></span><span id="crypt_xml_e_sign_failed"></span><dl> <dt>**CRYPT\_XML\_E\_SIGN\_FAILED**</dt> <dt>0x8009210CL</dt> </dl>                            | The cryptographic signature operation failed.<br/>                                                           |
| <span id="CRYPT_XML_E_VERIFY_FAILED"></span><span id="crypt_xml_e_verify_failed"></span><dl> <dt>**CRYPT\_XML\_E\_VERIFY\_FAILED**</dt> <dt>0x8009210DL</dt> </dl>                      | The signature verification failed.<br/>                                                                      |
| <span id="CRYPT_XML_E_TOO_MANY_SIGNATURES"></span><span id="crypt_xml_e_too_many_signatures"></span><dl> <dt>**CRYPT\_XML\_E\_TOO\_MANY\_SIGNATURES**</dt> <dt>0x8009210EL</dt> </dl>   | The number of **Signature** elements in the document exceeded the maximum allowed limit for processing.<br/> |
| <span id="CRYPT_XML_E_INVALID_KEYVALUE"></span><span id="crypt_xml_e_invalid_keyvalue"></span><dl> <dt>**CRYPT\_XML\_E\_INVALID\_KEYVALUE**</dt> <dt>0x8009210FL</dt> </dl>             | The key value that was supplied is not valid.<br/>                                                           |
| <span id="CRYPT_XML_E_UNEXPECTED_XML"></span><span id="crypt_xml_e_unexpected_xml"></span><dl> <dt>**CRYPT\_XML\_E\_UNEXPECTED\_XML**</dt> <dt>0x80092110L</dt> </dl>                   | Invalid or unexpected XML was encountered.<br/>                                                              |
| <span id="CRYPT_XML_E_SIGNER"></span><span id="crypt_xml_e_signer"></span><dl> <dt>**CRYPT\_XML\_E\_SIGNER**</dt> <dt>0x80092111L</dt> </dl>                                            | Unable to locate the signer's key.<br/>                                                                      |
| <span id="CRYPT_XML_E_NON_UNIQUE_ID"></span><span id="crypt_xml_e_non_unique_id"></span><dl> <dt>**CRYPT\_XML\_E\_NON\_UNIQUE\_ID**</dt> <dt>0x80092112L</dt> </dl>                     | A nonunique **Id** attribute was found.<br/>                                                                 |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Cryptxml.h</dt> </dl> |



 

 




