---
description: CryptXML defines the following global limits in the Cryptxml.h header file.
ms.assetid: 8f4dc314-76fc-40ce-a1e1-a701ae39d66d
title: CryptXML Limits (Cryptxml.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CryptXML Limits

CryptXML defines the following global limits in the Cryptxml.h header file.



| Constant/value                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                           |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CRYPT_XML_BLOB_MAX"></span><span id="crypt_xml_blob_max"></span><dl> <dt>**CRYPT\_XML\_BLOB\_MAX**</dt> <dt>0x7FFFFFF8</dt> </dl>                             | Encoded data cannot exceed 2 gigabytes (GB).<br/>                                                                                                                                                                               |
| <span id="CRYPT_XML_ID_MAX"></span><span id="crypt_xml_id_max"></span><dl> <dt>**CRYPT\_XML\_ID\_MAX**</dt> <dt>256</dt> </dl>                                          | Id length cannot exceed 256 characters.<br/>                                                                                                                                                                                    |
| <span id="CRYPT_XML_URI_MAX"></span><span id="crypt_xml_uri_max"></span><dl> <dt>**CRYPT\_XML\_URI\_MAX**</dt> <dt>8\*1024</dt> </dl>                                   | URI length cannot exceed 8192 characters.<br/>                                                                                                                                                                                  |
| <span id="CRYPT_XML_SIGNATURES_MAX"></span><span id="crypt_xml_signatures_max"></span><dl> <dt>**CRYPT\_XML\_SIGNATURES\_MAX**</dt> <dt>16</dt> </dl>                   | The default maximum number of **Signature** elements per document. This value can be overridden by specifying a new maximum when passing property values as [**CRYPT\_XML\_PROPERTY**](/windows/desktop/api/Cryptxml/ns-cryptxml-crypt_xml_property) structures.<br/> |
| <span id="CRYPT_XML_TRANSFORM_MAX"></span><span id="crypt_xml_transform_max"></span><dl> <dt>**CRYPT\_XML\_TRANSFORM\_MAX**</dt> <dt>16</dt> </dl>                      | The maximum number of transforms, represented by [**CRYPT\_XML\_ALGORITHM**](/windows/desktop/api/Cryptxml/ns-cryptxml-crypt_xml_algorithm) structures, per reference, represented by a [**CRYPT\_XML\_REFERENCE**](/windows/desktop/api/Cryptxml/ns-cryptxml-crypt_xml_reference) structure.<br/>          |
| <span id="CRYPT_XML_SIGNATURE_VALUE_MAX"></span><span id="crypt_xml_signature_value_max"></span><dl> <dt>**CRYPT\_XML\_SIGNATURE\_VALUE\_MAX**</dt> <dt>2048</dt> </dl> | The maximum length, in bytes, of a [**CRYPT\_XML\_SIGNATURE**](/windows/desktop/api/Cryptxml/ns-cryptxml-crypt_xml_signature) structure.<br/>                                                                                                                         |
| <span id="CRYPT_XML_DIGEST_VALUE_MAX"></span><span id="crypt_xml_digest_value_max"></span><dl> <dt>**CRYPT\_XML\_DIGEST\_VALUE\_MAX**</dt> <dt>128</dt> </dl>           | The maximum length, in bytes, of a digest.<br/>                                                                                                                                                                                 |
| <span id="CRYPT_XML_OBJECTS_MAX"></span><span id="crypt_xml_objects_max"></span><dl> <dt>**CRYPT\_XML\_OBJECTS\_MAX**</dt> <dt>256</dt> </dl>                           | Used internally to specify the maximum number of **Object** elements allowed per signature.<br/>                                                                                                                                |
| <span id="CRYPT_XML_REFERENCES_MAX"></span><span id="crypt_xml_references_max"></span><dl> <dt>**CRYPT\_XML\_REFERENCES\_MAX**</dt> <dt>0x7FF8</dt> </dl>               | The maximum number of **Reference** elements allowed.<br/>                                                                                                                                                                      |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Cryptxml.h</dt> </dl> |



 

 




