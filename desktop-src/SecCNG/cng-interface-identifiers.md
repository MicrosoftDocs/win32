---
description: The following identifiers are used to identify a CNG cryptographic interface.
ms.assetid: 509c89ff-0c73-4e57-9c39-400522f2086e
title: CNG Interface Identifiers (Bcrypt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CNG Interface Identifiers

The following identifiers are used to identify a CNG cryptographic interface. In CNG, an interface identifies the type of cryptographic behavior that a provider supports. For example, a provider may be a random number generator or it may be a hashing provider.



| Constant/value                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                       |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BCRYPT_CIPHER_INTERFACE"></span><span id="bcrypt_cipher_interface"></span><dl> <dt>**BCRYPT\_CIPHER\_INTERFACE**</dt> <dt>0x00000001</dt> </dl>                                               | The symmetric cipher interface.<br/>                                                                                                                                        |
| <span id="BCRYPT_HASH_INTERFACE"></span><span id="bcrypt_hash_interface"></span><dl> <dt>**BCRYPT\_HASH\_INTERFACE**</dt> <dt>0x00000002</dt> </dl>                                                     | The hash interface.<br/>                                                                                                                                                    |
| <span id="BCRYPT_ASYMMETRIC_ENCRYPTION_INTERFACE"></span><span id="bcrypt_asymmetric_encryption_interface"></span><dl> <dt>**BCRYPT\_ASYMMETRIC\_ENCRYPTION\_INTERFACE**</dt> <dt>0x00000003</dt> </dl> | The asymmetric encryption interface.<br/>                                                                                                                                   |
| <span id="BCRYPT_SECRET_AGREEMENT_INTERFACE"></span><span id="bcrypt_secret_agreement_interface"></span><dl> <dt>**BCRYPT\_SECRET\_AGREEMENT\_INTERFACE**</dt> <dt>0x00000004</dt> </dl>                | The secret agreement interface.<br/>                                                                                                                                        |
| <span id="BCRYPT_SIGNATURE_INTERFACE"></span><span id="bcrypt_signature_interface"></span><dl> <dt>**BCRYPT\_SIGNATURE\_INTERFACE**</dt> <dt>0x00000005</dt> </dl>                                      | The signature interface.<br/>                                                                                                                                               |
| <span id="BCRYPT_RNG_INTERFACE"></span><span id="bcrypt_rng_interface"></span><dl> <dt>**BCRYPT\_RNG\_INTERFACE**</dt> <dt>0x00000006</dt> </dl>                                                        | The random number generator interface.<br/>                                                                                                                                 |
| <span id="NCRYPT_KEY_STORAGE_INTERFACE"></span><span id="ncrypt_key_storage_interface"></span><dl> <dt>**NCRYPT\_KEY\_STORAGE\_INTERFACE**</dt> <dt>0x00010001</dt> </dl>                               | The key storage interface.<br/>                                                                                                                                             |
| <span id="NCRYPT_SCHANNEL_INTERFACE"></span><span id="ncrypt_schannel_interface"></span><dl> <dt>**NCRYPT\_SCHANNEL\_INTERFACE**</dt> <dt>0x00010002</dt> </dl>                                         | The Schannel signature interface.<br/>                                                                                                                                      |
| <span id="NCRYPT_SCHANNEL_SIGNATURE_INTERFACE"></span><span id="ncrypt_schannel_signature_interface"></span><dl> <dt>**NCRYPT\_SCHANNEL\_SIGNATURE\_INTERFACE**</dt> <dt>0x00010003</dt> </dl>          | The Schannel cipher suite interface.<br/> **Windows Server 2008, Windows Vista, Windows Server 2003, Windows XP and Windows 2000:** This value is not supported.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                |
| Header<br/>                   | <dl> <dt>Bcrypt.h; </dt> <dt>Ncrypt.h</dt> </dl> |



 

 




