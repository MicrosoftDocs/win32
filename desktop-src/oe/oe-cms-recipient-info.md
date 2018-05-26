---
title: CMS\_RECIPIENT\_INFO structure
description: Contains key information for an encrypted message recipient.
ms.assetid: aa84b0f3-08fb-4440-a9c6-7863e6bae3bf
keywords:
- CMS_RECIPIENT_INFO structure Windows Mail (formerly Outlook Express)
- PCMS_RECIPIENT_INFO structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- CMS_RECIPIENT_INFO
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMS\_RECIPIENT\_INFO structure

\[The **CMS\_RECIPIENT\_INFO** structure is available for use in Windows XP. It might be altered or unavailable in subsequent versions.\]

Contains key information for an encrypted message recipient.

## Syntax


```C++
typedef struct tagCMS_RECIPIENT_INFO {
  DWORD                       dwRecipientType;
  PCCERT_CONTEXT              pccert;
  CRYPT_ALGORITHM_IDENTIFIER  KeyEncryptionAlgorithm;
  void                        *pvKeyEncryptionAuxInfo;
  DWORD                       cbKeyEncryptionAuxInfo;
  CRYPT_ALGORITHM_IDENTIFIER  KeyWrapAlgorithm;
  void                        *pvKeyWrapAuxInfo;
  DWORD                       cbKeyWrapAuxInfo;
  DWORD                       dwU1;
  union {
    CRYPT_BIT_BLOB SubjectPublicKey;
    struct {
      HCRYPTPROV hprov;
      HCRYPTKEY  hkey;
    } u2;
    struct {
      CRYPT_DATA_BLOB            UserKeyingMaterial;
      CRYPT_ALGORITHM_IDENTIFIER EphemeralAlgorithm;
      CRYPT_BIT_BLOB             SubjectPublicKey;
    } u3;
    struct {
      CRYPT_DATA_BLOB UserKeyingMaterial;
      HCRYPTPROV      hprov;
      DWORD           dwKeySpec;
      CERT_ID         senderCertId;
      CRYPT_BIT_BLOB  SubjectPublicKey;
    } u4;
  } u1;
  DWORD                       dwU3;
  union {
    CERT_ISSUER_SERIAL_NUMBER IssuerSerial;
    CRYPT_DATA_BLOB           KeyId;
  } u3;
  FILETIME                    filetime;
  PCRYPT_ATTRIBUTE_TYPE_VALUE pOtherAttr;
} CMS_RECIPIENT_INFO, *PCMS_RECIPIENT_INFO;
```



## Members

<dl> <dt>

**dwRecipientType**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the recipient type.



| Value                                                                                                                                                                                                                                                                                | Meaning                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <span id="CMS_RECIPIENT_INFO_TYPE_UNKNOWN"></span><span id="cms_recipient_info_type_unknown"></span><dl> <dt>**CMS\_RECIPIENT\_INFO\_TYPE\_UNKNOWN**</dt> <dt>0</dt> </dl>        | Indicates that the type is unknown. <br/>                                      |
| <span id="CMS_RECIPIENT_INFO_TYPE_KEYTRANS"></span><span id="cms_recipient_info_type_keytrans"></span><dl> <dt>**CMS\_RECIPIENT\_INFO\_TYPE\_KEYTRANS**</dt> <dt>1</dt> </dl>     | Indicates that the recipient uses key transport algorithms. <br/>              |
| <span id="CMS_RECIPIENT_INFO_TYPE_KEYAGREE"></span><span id="cms_recipient_info_type_keyagree"></span><dl> <dt>**CMS\_RECIPIENT\_INFO\_TYPE\_KEYAGREE**</dt> <dt>2</dt> </dl>     | Indicates that the recipient uses key agreement algorithms. <br/>              |
| <span id="CMS_RECIPIENT_INFO_TYPE_MAIL_LIST"></span><span id="cms_recipient_info_type_mail_list"></span><dl> <dt>**CMS\_RECIPIENT\_INFO\_TYPE\_MAIL\_LIST**</dt> <dt>3</dt> </dl> | Indicates that the recipient uses previously distributed symmetric keys. <br/> |



 

</dd> <dt>

**pccert**
</dt> <dd>

Type: **PCCERT\_CONTEXT**

</dd> <dd>

Contains a pointer to a [CERT\_CONTEXT](http://msdn.microsoft.com/library/seccrypto/security/cert_context.asp) structure.

</dd> <dt>

**KeyEncryptionAlgorithm**
</dt> <dd>

Type: **[CRYPT\_ALGORITHM\_IDENTIFIER](http://msdn.microsoft.com/library/seccrypto/security/crypt_algorithm_identifier.asp)**

</dd> <dd>

Contains a [CRYPT\_ALGORITHM\_IDENTIFIER](http://msdn.microsoft.com/library/seccrypto/security/crypt_algorithm_identifier.asp) structure.

</dd> <dt>

**pvKeyEncryptionAuxInfo**
</dt> <dd>

Type: **void\***

</dd> <dd>

Contains a pointer to a structure that contains additional encryption information.

</dd> <dt>

**cbKeyEncryptionAuxInfo**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that specifies the size (in bytes) of **pvKeyEncryptionAuxInfo**.

</dd> <dt>

**KeyWrapAlgorithm**
</dt> <dd>

Type: **[CRYPT\_ALGORITHM\_IDENTIFIER](http://msdn.microsoft.com/library/seccrypto/security/crypt_algorithm_identifier.asp)**

</dd> <dd>

Contains a [CRYPT\_ALGORITHM\_IDENTIFIER](http://msdn.microsoft.com/library/seccrypto/security/crypt_algorithm_identifier.asp) structure.

</dd> <dt>

**pvKeyWrapAuxInfo**
</dt> <dd>

Type: **void\***

</dd> <dd>

Contains a pointer to a structure that contains additional encryption information.

</dd> <dt>

**cbKeyWrapAuxInfo**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that specifies the size (in bytes) of **pvKeyWrapAuxInfo**.

</dd> <dt>

**dwU1**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that is used as a switch flag that indicates which set of values occupies the **u1** union.



| Value                                                                                                                                                                                                                                                                                                                 | Meaning                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <span id="CMS_RECIPIENT_INFO_PUBKEY_KEYTRANS"></span><span id="cms_recipient_info_pubkey_keytrans"></span><dl> <dt>**CMS\_RECIPIENT\_INFO\_PUBKEY\_KEYTRANS**</dt> <dt>1</dt> </dl>                                | Indicates a key transport algorithm. <br/>                   |
| <span id="CMS_RECIPIENT_INFO_PUBKEY_PROVIDER"></span><span id="cms_recipient_info_pubkey_provider"></span><dl> <dt>**CMS\_RECIPIENT\_INFO\_PUBKEY\_PROVIDER**</dt> <dt>2</dt> </dl>                                | Indicates previously distributed keys. <br/>                 |
| <span id="CMS_RECIPIENT_INFO_PUBKEY_EPHEMERAL_KEYAGREE"></span><span id="cms_recipient_info_pubkey_ephemeral_keyagree"></span><dl> <dt>**CMS\_RECIPIENT\_INFO\_PUBKEY\_EPHEMERAL\_KEYAGREE**</dt> <dt>3</dt> </dl> | Indicates ephemeral key agreement algorithm. <br/>           |
| <span id="CMS_RECIPIENT_INFO_PUBKEY_STATIC_KEYAGREE"></span><span id="cms_recipient_info_pubkey_static_keyagree"></span><dl> <dt>**CMS\_RECIPIENT\_INFO\_PUBKEY\_STATIC\_KEYAGREE**</dt> <dt>4</dt> </dl>          | Indicates a store and forward key agreement algorithm. <br/> |



 

</dd> <dt>

**u1**
</dt> <dd> <dl> <dt>

**SubjectPublicKey**
</dt> <dd>

Type: **[CRYPT\_BIT\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/crypt_bit_blob.asp)**

</dd> <dd>

Contains a [CRYPT\_BIT\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/crypt_bit_blob.asp) that contains the recipient's public key. This structure occupies the **u1** union when **dwU1** is equal to **CMS\_RECIPIENT\_INFO\_PUBKEY\_KEYTRANS**.

</dd> <dt>

**u2**
</dt> <dd>

This structure occupies the **u1** union when **dwU1** is equal to **CMS\_RECIPIENT\_INFO\_PUBKEY\_PROVIDER**.

<dl> <dt>

**hprov**
</dt> <dd>

Type: **[HCRYPTPROV](http://msdn.microsoft.com/library/seccrypto/security/hcryptprov.asp)**

</dd> <dd>

Contains an [HCRYPTPROV](http://msdn.microsoft.com/library/seccrypto/security/hcryptprov.asp) handle to the CSP used to encrypt and export the recipient key.

</dd> <dt>

**hkey**
</dt> <dd>

Type: **[HCRYPTKEY](http://msdn.microsoft.com/library/seccrypto/security/hcryptkey.asp)**

</dd> <dd>

Contains a [HCRYPTKEY](http://msdn.microsoft.com/library/seccrypto/security/hcryptkey.asp) handle to the cryptographic key to be used by the CSP indicated by **hprov**.

</dd> </dl> </dd> <dt>

**u3**
</dt> <dd>

This structure occupies the **u1** union when **dwU1** is equal to **CMS\_RECIPIENT\_INFO\_PUBKEY\_EPHEMERAL\_KEYAGREE**.

<dl> <dt>

**UserKeyingMaterial**
</dt> <dd>

Type: **CRYPT\_DATA\_BLOB**

</dd> <dd>

Contains a [CRYPT\_DATA\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/cryptoapi_blob.asp) that contains the UKM provided by the sender.

</dd> <dt>

**EphemeralAlgorithm**
</dt> <dd>

Type: **[CRYPT\_ALGORITHM\_IDENTIFIER](http://msdn.microsoft.com/library/seccrypto/security/crypt_algorithm_identifier.asp)**

</dd> <dd>

Contains a [CRYPT\_ALGORITHM\_IDENTIFIER](http://msdn.microsoft.com/library/seccrypto/security/crypt_algorithm_identifier.asp) structure containing the ephemeral public key algorithm and parameters.

</dd> <dt>

**SubjectPublicKey**
</dt> <dd>

Type: **[CRYPT\_BIT\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/crypt_bit_blob.asp)**

</dd> <dd>

Contains a [CRYPT\_BIT\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/crypt_bit_blob.asp) that contains the recipient's public key.

</dd> </dl> </dd> <dt>

**u4**
</dt> <dd>

This structure occupies the **u1** union when **dwU1** is equal to **CMS\_RECIPIENT\_INFO\_PUBKEY\_STATIC\_KEYAGREE**.

<dl> <dt>

**UserKeyingMaterial**
</dt> <dd>

Type: **CRYPT\_DATA\_BLOB**

</dd> <dd>

Contains a [CRYPT\_DATA\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/cryptoapi_blob.asp) that contains the UKM provided by the sender.

</dd> <dt>

**hprov**
</dt> <dd>

Type: **[HCRYPTPROV](http://msdn.microsoft.com/library/seccrypto/security/hcryptprov.asp)**

</dd> <dd>

Contains an [HCRYPTPROV](http://msdn.microsoft.com/library/seccrypto/security/hcryptprov.asp) handle to the CSP used to encrypt and export the recipient key.

</dd> <dt>

**dwKeySpec**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the sender's private key.

</dd> <dt>

**senderCertId**
</dt> <dd>

Type: **[CERT\_ID](http://msdn.microsoft.com/library/seccrypto/security/cert_id.asp)**

</dd> <dd>

Contains the [CERT\_ID](http://msdn.microsoft.com/library/seccrypto/security/cert_id.asp) of the sender's certificate.

</dd> <dt>

**SubjectPublicKey**
</dt> <dd>

Type: **[CRYPT\_BIT\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/crypt_bit_blob.asp)**

</dd> <dd>

Contains a [CRYPT\_BIT\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/crypt_bit_blob.asp) that contains the recipient's public key.

</dd> </dl> </dd> </dl> </dd> <dt>

**dwU3**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that is used as a switch flag that indicates which key ID type occupies the **u3** union.



| Value                                                                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CMS_RECIPIENT_INFO_KEYID_ISSUERSERIAL"></span><span id="cms_recipient_info_keyid_issuerserial"></span><dl> <dt>**CMS\_RECIPIENT\_INFO\_KEYID\_ISSUERSERIAL**</dt> <dt>1</dt> </dl> | Indicates that the certificate ID is stored in a [CRYPT\_DATA\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/cert_issuer_serial_number.asp) structure. <br/>          |
| <span id="CMS_RECIPIENT_INFO_KEYID_KEY_ID"></span><span id="cms_recipient_info_keyid_key_id"></span><dl> <dt>**CMS\_RECIPIENT\_INFO\_KEYID\_KEY\_ID**</dt> <dt>2</dt> </dl>                  | Indicates that the certificate ID is stored in a [CRYPT\_DATA\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/cryptoapi_blob.asp) (CRYPT\_HASH\_BLOB) structure. <br/> |



 

</dd> <dt>

**u3**
</dt> <dd> <dl> <dt>

**IssuerSerial**
</dt> <dd>

Type: **[CERT\_ISSUER\_SERIAL\_NUMBER](http://msdn.microsoft.com/library/seccrypto/security/cert_issuer_serial_number.asp)**

</dd> <dd>

Contains a [CERT\_ISSUER\_SERIAL\_NUMBER](http://msdn.microsoft.com/library/seccrypto/security/cert_issuer_serial_number.asp) that contains the issuer and the issuer's serial number for a certificate. This structure occupies the **u3** union when **dwU3** is equal to **CMS\_RECIPIENT\_INFO\_KEYID\_ISSUERSERIAL**.

</dd> <dt>

**KeyId**
</dt> <dd>

Type: **CRYPT\_DATA\_BLOB**

</dd> <dd>

Contains a [CRYPT\_DATA\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/cryptoapi_blob.asp) that contains the a certificate key identifier. This structure occupies the **u3** union when **dwU3** is equal to **CMS\_RECIPIENT\_INFO\_KEYID\_KEY\_ID**.

</dd> </dl> </dd> <dt>

**filetime**
</dt> <dd>

Type: **[FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp)**

</dd> <dd>

Contains a [FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp) structure that contains a single KEK from a set that was previously distributed. Used when **dwRecipientType** is **CMS\_RECIPIENT\_INFO\_TYPE\_MAIL\_LIST**.

</dd> <dt>

**pOtherAttr**
</dt> <dd>

Type: **PCRYPT\_ATTRIBUTE\_TYPE\_VALUE**

</dd> <dd>

Contains a pointer to a [CRYPT\_ATTRIBUTE\_TYPE\_VALUE](http://msdn.microsoft.com/library/seccrypto/security/crypt_attribute_type_value.asp) structure that contains encryption attributes. Used when **dwRecipientType** is **CMS\_RECIPIENT\_INFO\_TYPE\_MAIL\_LIST**.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





