---
description: Used to identify a key storage property.
ms.assetid: 407f0e42-07c8-4ec6-81c6-f8bde005adb0
title: Key Storage Property Identifiers (Ncrypt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Key Storage Property Identifiers

The following values are used to identify a key storage property.

<dl> <dt>

<span id="NCRYPT_ALGORITHM_GROUP_PROPERTY"></span><span id="ncrypt_algorithm_group_property"></span>**NCRYPT\_ALGORITHM\_GROUP\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Algorithm Group"
</dt> <dt>



A null-terminated Unicode string that contains the name of the object's algorithm group. This property only applies to keys. The following identifiers are returned by the Microsoft key storage provider.



| Identifier                                     | Value              | Description                                                   |
|------------------------------------------------|--------------------|---------------------------------------------------------------|
| **NCRYPT\_RSA\_ALGORITHM\_GROUP**<br/>   | "RSA"<br/>   | The RSA algorithm group.<br/>                           |
| **NCRYPT\_DH\_ALGORITHM\_GROUP**<br/>    | "DH"<br/>    | The Diffie-Hellman algorithm group.<br/>                |
| **NCRYPT\_DSA\_ALGORITHM\_GROUP**<br/>   | "DSA"<br/>   | The DSA algorithm group.<br/>                           |
| **NCRYPT\_ECDSA\_ALGORITHM\_GROUP**<br/> | "ECDSA"<br/> | The elliptic curve DSA algorithm group.<br/>            |
| **NCRYPT\_ECDH\_ALGORITHM\_GROUP**<br/>  | "ECDH"<br/>  | The elliptic curve Diffie-Hellman algorithm group.<br/> |



 


</dt> </dl> </dd> <dt>

<span id="NCRYPT_ALGORITHM_PROPERTY"></span><span id="ncrypt_algorithm_property"></span>**NCRYPT\_ALGORITHM\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Algorithm Name"
</dt> <dt>



A null-terminated Unicode string that contains the name of the object's algorithm. This can be one of the predefined [**CNG Algorithm Identifiers**](cng-algorithm-identifiers.md) or another registered algorithm identifier. This property only applies to keys.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_ASSOCIATED_ECDH_KEY"></span><span id="ncrypt_associated_ecdh_key"></span>**NCRYPT\_ASSOCIATED\_ECDH\_KEY**
</dt> <dd> <dl> <dt>

L"SmartCardAssociatedECDHKey"
</dt> <dt>



An **LPWSTR** value that indicates the container name of the Elliptic Curve Diffie-Hellman (ECDH) key to use during logon for a given handle to an Elliptic Curve Digital Signature Algorithm (ECDSA) key. If there are no ECDH keys on the card, the [*key storage provider*](/windows/desktop/SecGloss/k-gly) (KSP) returns **NTE\_NOT\_FOUND**. This property applies to ECDSA keys for logon with smart cards. The property is supported by the Microsoft Smart Card key storage provider and not by the Microsoft Software key storage provider.

**Windows Server 2008 and Windows Vista:** This value is not supported.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_BLOCK_LENGTH_PROPERTY"></span><span id="ncrypt_block_length_property"></span>**NCRYPT\_BLOCK\_LENGTH\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Block Length"
</dt> <dt>



A **DWORD** that contains the length, in bytes, of the encryption block. This property only applies to keys that support encryption.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_CERTIFICATE_PROPERTY"></span><span id="ncrypt_certificate_property"></span>**NCRYPT\_CERTIFICATE\_PROPERTY**
</dt> <dd> <dl> <dt>

L"SmartCardKeyCertificate"
</dt> <dt>



A [*BLOB*](/windows/desktop/SecGloss/b-gly) that contains an X.509 certificate that is associated with the key.

**Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** A [*BLOB*](/windows/desktop/SecGloss/b-gly) that contains the [*smart card*](/windows/desktop/SecGloss/s-gly) key [*certificate*](/windows/desktop/SecGloss/c-gly). This property is not supported by the Microsoft Software Key Storage Provider.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_DH_PARAMETERS_PROPERTY"></span><span id="ncrypt_dh_parameters_property"></span>**NCRYPT\_DH\_PARAMETERS\_PROPERTY**
</dt> <dd> <dl> <dt>

L"DHParameters"
</dt> <dt>



Specifies parameters to use with a Diffie-Hellman key. This data type is a pointer to a [**BCRYPT\_DH\_PARAMETER\_HEADER**](/windows/desktop/api/Bcrypt/ns-bcrypt-bcrypt_dh_parameter_header) structure. This property can only be set and must be set for the key before the key is completed.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_EXPORT_POLICY_PROPERTY"></span><span id="ncrypt_export_policy_property"></span>**NCRYPT\_EXPORT\_POLICY\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Export Policy"
</dt> <dt>



A **DWORD** that contains a set of flags that specify the export policy for a persisted key. This property only applies to keys. This can contain zero or a combination of one or more of the following values.



| Identifier                                    | Value      | Description                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NCRYPT\_ALLOW\_EXPORT\_FLAG**               | 0x00000001 | The private key can be exported.                                                                                                                                                                                                                                                                                 |
| **NCRYPT\_ALLOW\_PLAINTEXT\_EXPORT\_FLAG**    | 0x00000002 | The private key can be exported in plaintext form.                                                                                                                                                                                                                                                               |
| **NCRYPT\_ALLOW\_ARCHIVING\_FLAG**            | 0x00000004 | The private key can be exported once for archiving purposes. This flag only applies to the original key handle on which it is set. This policy can only be applied to the original key handle. After the key handle has been closed, the key can no longer be exported for archiving purposes.                   |
| **NCRYPT\_ALLOW\_PLAINTEXT\_ARCHIVING\_FLAG** | 0x00000008 | The private key can be exported once in plaintext form for archiving purposes. This flag only applies to the original key handle on which it is set. This policy can only be applied to the original key handle. After the key handle has been closed, the key can no longer be exported for archiving purposes. |



 


</dt> </dl> </dd> <dt>

<span id="NCRYPT_IMPL_TYPE_PROPERTY"></span><span id="ncrypt_impl_type_property"></span>**NCRYPT\_IMPL\_TYPE\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Impl Type"
</dt> <dt>



A **DWORD** that contains a set of flags that define implementation details of the provider. This property only applies to key storage providers. This can contain zero or a combination of one or more of the following values.



| Identifier                            | Value      | Description                                               |
|---------------------------------------|------------|-----------------------------------------------------------|
| **NCRYPT\_IMPL\_HARDWARE\_FLAG**      | 0x00000001 | The provider is hardware based.                           |
| **NCRYPT\_IMPL\_SOFTWARE\_FLAG**      | 0x00000002 | The provider is software based.                           |
| **NCRYPT\_IMPL\_REMOVABLE\_FLAG**     | 0x00000008 | The provider is removable.                                |
| **NCRYPT\_IMPL\_HARDWARE\_RNG\_FLAG** | 0x00000010 | The provider is a hardware based random number generator. |



 


</dt> </dl> </dd> <dt>

<span id="NCRYPT_KEY_TYPE_PROPERTY"></span><span id="ncrypt_key_type_property"></span>**NCRYPT\_KEY\_TYPE\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Key Type"
</dt> <dt>



A **DWORD** that contains a set of flags that define the key type. This property only applies to keys. This can contain zero or the following value.



| Identifier                     | Value      | Description                                                                                              |
|--------------------------------|------------|----------------------------------------------------------------------------------------------------------|
| **NCRYPT\_MACHINE\_KEY\_FLAG** | 0x00000001 | The key applies to the local computer. If this flag is not present, the key applies to the current user. |



 


</dt> </dl> </dd> <dt>

<span id="NCRYPT_KEY_USAGE_PROPERTY"></span><span id="ncrypt_key_usage_property"></span>**NCRYPT\_KEY\_USAGE\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Key Usage"
</dt> <dt>



A **DWORD** that contains a set of flags that define the usage details for a key. This property only applies to keys. This can contain zero or a combination of one or more of the following values.



| Identifier                              | Value      | Description                                          |
|-----------------------------------------|------------|------------------------------------------------------|
| **NCRYPT\_ALLOW\_DECRYPT\_FLAG**        | 0x00000001 | The key can be used for decryption.                  |
| **NCRYPT\_ALLOW\_SIGNING\_FLAG**        | 0x00000002 | The key can be used for signing.                     |
| **NCRYPT\_ALLOW\_KEY\_AGREEMENT\_FLAG** | 0x00000004 | The key can be used for secret agreement encryption. |
| **NCRYPT\_ALLOW\_ALL\_USAGES**          | 0x00ffffff | The key can be used for any purpose.                 |



 


</dt> </dl> </dd> <dt>

<span id="NCRYPT_LAST_MODIFIED_PROPERTY"></span><span id="ncrypt_last_modified_property"></span>**NCRYPT\_LAST\_MODIFIED\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Modified"
</dt> <dt>



Indicates when the key was last modified. This data type is a pointer to a [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) structure. This property only applies to persisted keys.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_LENGTH_PROPERTY"></span><span id="ncrypt_length_property"></span>**NCRYPT\_LENGTH\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Length"
</dt> <dt>



A **DWORD** that contains the length, in bits, of the key. This property only applies to keys.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_LENGTHS_PROPERTY"></span><span id="ncrypt_lengths_property"></span>**NCRYPT\_LENGTHS\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Lengths"
</dt> <dt>



Indicates the key sizes that are supported by the key. This data type is a pointer to an [**NCRYPT\_SUPPORTED\_LENGTHS**](/windows/desktop/api/Ncrypt/ns-ncrypt-ncrypt_supported_lengths) structure that contains this information. This property only applies to keys.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_MAX_NAME_LENGTH_PROPERTY"></span><span id="ncrypt_max_name_length_property"></span>**NCRYPT\_MAX\_NAME\_LENGTH\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Max Name Length"
</dt> <dt>



A **DWORD** that contains the maximum length, in characters, of the name of a persistent key. This property only applies to a provider.

This property is primarily intended to be used by key storage providers that store their keys on a device that has a limited amount of available memory, such as a smart card.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_NAME_PROPERTY"></span><span id="ncrypt_name_property"></span>**NCRYPT\_NAME\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Name"
</dt> <dt>



A pointer to a null-terminated Unicode string that contains the name of the object.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_PIN_PROMPT_PROPERTY"></span><span id="ncrypt_pin_prompt_property"></span>**NCRYPT\_PIN\_PROMPT\_PROPERTY**
</dt> <dd> <dl> <dt>

L"SmartCardPinPrompt"
</dt> <dt>



This value is not supported.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_PIN_PROPERTY"></span><span id="ncrypt_pin_property"></span>**NCRYPT\_PIN\_PROPERTY**
</dt> <dd> <dl> <dt>

L"SmartCardPin"
</dt> <dt>



A pointer to a null-terminated Unicode string that contains the PIN. The PIN is used for a smart card key or the password for a password-protected key stored in a software-based KSP. This property can only be set. Microsoft KSPs will cache this value so that the user is only prompted once per process.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_PROVIDER_HANDLE_PROPERTY"></span><span id="ncrypt_provider_handle_property"></span>**NCRYPT\_PROVIDER\_HANDLE\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Provider Handle"
</dt> <dt>



An **NCRYPT\_PROV\_HANDLE** that contains the handle of the CNG key storage provider. When you are finished using the handle, you must call [**NCryptFreeObject**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptfreeobject) to release it.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_READER_PROPERTY"></span><span id="ncrypt_reader_property"></span>**NCRYPT\_READER\_PROPERTY**
</dt> <dd> <dl> <dt>

L"SmartCardReader"
</dt> <dt>



A pointer to a null-terminated Unicode string that contains the name of the smart card reader. This property can only be set.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_ROOT_CERTSTORE_PROPERTY"></span><span id="ncrypt_root_certstore_property"></span>**NCRYPT\_ROOT\_CERTSTORE\_PROPERTY**
</dt> <dd> <dl> <dt>

L"SmartcardRootCertStore"
</dt> <dt>



An **HCERTSTORE** that represents the smart card root certificate store.


</dt> </dl> </dd> <dt>

<span id="_NCRYPT_SCARD_PIN_ID"></span><span id="_ncrypt_scard_pin_id"></span> **NCRYPT\_SCARD\_PIN\_ID**
</dt> <dd> <dl> <dt>

L"SmartCardPinId"
</dt> <dt>



A pointer to the **PIN\_ID** value associated with a given [*cryptographic key*](/windows/desktop/SecGloss/c-gly) on a [*smart card*](/windows/desktop/SecGloss/s-gly). This is a read-only property. The **PIN\_ID** data type is defined in Cardmod.h.

**Windows Server 2008 and Windows Vista:** This value is not supported.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_SCARD_PIN_INFO"></span><span id="ncrypt_scard_pin_info"></span>**NCRYPT\_SCARD\_PIN\_INFO**
</dt> <dd> <dl> <dt>

L"SmartCardPinInfo"
</dt> <dt>



A pointer to [**PIN\_INFO**](/windows/desktop/api/mbnapi/ns-mbnapi-mbn_pin_info) structure of the PIN associated with a given cryptographic key on the smart card. The caller provides the key handle. This property is a read-only property. The **PIN\_INFO** structure is defined in Cardmod.h.

**Windows Server 2008 and Windows Vista:** This value is not supported.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_SECURE_PIN_PROPERTY"></span><span id="ncrypt_secure_pin_property"></span>**NCRYPT\_SECURE\_PIN\_PROPERTY**
</dt> <dd> <dl> <dt>

L"SmartCardSecurePin"
</dt> <dt>



A pointer to a null-terminated Unicode string that contains the smart card session PIN. This property can only be set.

**Windows Vista:** This property is not supported.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_SECURITY_DESCR_PROPERTY"></span><span id="ncrypt_security_descr_property"></span>**NCRYPT\_SECURITY\_DESCR\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Security Descr"
</dt> <dt>



A pointer to a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) structure that contains access control information for the key. This property only applies to persistent keys. The *dwFlags* parameter of the [**NCryptGetProperty**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptgetproperty) or [**NCryptSetProperty**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptsetproperty) function identifies the part of the security descriptor to get or set.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_SECURITY_DESCR_SUPPORT_PROPERTY"></span><span id="ncrypt_security_descr_support_property"></span>**NCRYPT\_SECURITY\_DESCR\_SUPPORT\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Security Descr Support"
</dt> <dt>



Indicates whether the provider supports security descriptors for keys. This property is a **DWORD** that contains 1 if the provider supports security descriptors for keys. If this property contains any other value, or if the [**NCryptGetProperty**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptgetproperty) function returns **NTE\_NOT\_SUPPORTED**, then the provider does not support security descriptors for keys. This property only applies to providers.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_SMARTCARD_GUID_PROPERTY"></span><span id="ncrypt_smartcard_guid_property"></span>**NCRYPT\_SMARTCARD\_GUID\_PROPERTY**
</dt> <dd> <dl> <dt>

L"SmartCardGuid"
</dt> <dt>



A BLOB that contains the identifier of the smart card.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_UI_POLICY_PROPERTY"></span><span id="ncrypt_ui_policy_property"></span>**NCRYPT\_UI\_POLICY\_PROPERTY**
</dt> <dd> <dl> <dt>

L"UI Policy"
</dt> <dt>



If used with the [**NCryptSetProperty**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptsetproperty) or [**NCryptGetProperty**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptgetproperty) function, this is a pointer to an [**NCRYPT\_UI\_POLICY**](/windows/desktop/api/Ncrypt/ns-ncrypt-ncrypt_ui_policy) structure that contains the strong key user interface policy for the key. This property only applies to persistent keys. This property can only be set when the key is being generated. Once the [**NCryptFinalizeKey**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptfinalizekey) function has been called for this key, this property becomes read-only.

A key storage provider can receive this parameter through an [**NCryptSetPropertyFn**](https://www.bing.com/search?q=**NCryptSetPropertyFn**) callback function. The parameter value is an NCRYPT\_UI\_POLICY\_BLOB structure that contains the same information. Similarly, when an application makes a request through NCryptSetPropertyFn to the provider to return this property, the provider is expected to return an NCRYPT\_UI\_POLICY\_BLOB structure.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_UNIQUE_NAME_PROPERTY"></span><span id="ncrypt_unique_name_property"></span>**NCRYPT\_UNIQUE\_NAME\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Unique Name"
</dt> <dt>



A pointer to a null-terminated Unicode string that contains the unique name of the object. This is an alternate name that can be used when accessing the key. This property is used when it is thought that the key name originally passed to [**NCryptCreatePersistedKey**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptcreatepersistedkey) is not unique enough to reliably identify the persisted key. The Microsoft key storage provider will return the file name of the key as this property.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_USE_CONTEXT_PROPERTY"></span><span id="ncrypt_use_context_property"></span>**NCRYPT\_USE\_CONTEXT\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Use Context"
</dt> <dt>



A pointer to a null-terminated Unicode string that describes the context of the operation. This property is not persistent and can be set on either a provider or a key. A key does not have access to the **NCRYPT\_USE\_CONTEXT\_PROPERTY** property of the provider because the property is specific only to the handle it is set for.

An example where this property would be used in the context of a provider is a key storage provider that needs to prompt the user during a call to [**NCryptOpenKey**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptopenkey) (for example, "Insert your smart card in the reader."). Because the key handle is not available until after **NCryptOpenKey** returns, the application should set this property on the provider handle prior to calling **NCryptOpenKey**.

An example where this property would be used in the context of a key handle is a key storage provider that needs to prompt the user during an operation using the key (for example, "This application needs to use this key to sign a document."). The provider could then relay this context information to the user in any user interface shown during the operation.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_USE_COUNT_ENABLED_PROPERTY"></span><span id="ncrypt_use_count_enabled_property"></span>**NCRYPT\_USE\_COUNT\_ENABLED\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Enabled Use Count"
</dt> <dt>



Indicates whether the provider supports usage counting for keys. This property is a **DWORD** that contains 1 if the provider supports usage counting for keys. If this property contains any other value, or if the [**NCryptGetProperty**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptgetproperty) function returns **NTE\_NOT\_SUPPORTED**, then the provider does not support usage counting for keys. This property only applies to providers.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_USE_COUNT_PROPERTY"></span><span id="ncrypt_use_count_property"></span>**NCRYPT\_USE\_COUNT\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Use Count"
</dt> <dt>



A [**ULARGE\_INTEGER**](/windows/win32/api/winnt/ns-winnt-ularge_integer~r1) variable that contains the number of operations that the specified [*private key*](/windows/desktop/SecGloss/p-gly) has performed. This property is optional and may not be supported by all providers. Providers that support this property on keys should also support the **NCRYPT\_USE\_COUNT\_ENABLED\_PROPERTY** property on the provider handle. The Microsoft key storage provider does not support this property. This property only applies to persistent keys.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_USER_CERTSTORE_PROPERTY"></span><span id="ncrypt_user_certstore_property"></span>**NCRYPT\_USER\_CERTSTORE\_PROPERTY**
</dt> <dd> <dl> <dt>

L"SmartCardUserCertStore"
</dt> <dt>



An **HCERTSTORE** that represents the smart card user certificate store.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_VERSION_PROPERTY"></span><span id="ncrypt_version_property"></span>**NCRYPT\_VERSION\_PROPERTY**
</dt> <dd> <dl> <dt>

L"Version"
</dt> <dt>



A **DWORD** that contains the software version of the provider. The high word contains the major version and the low word contains the minor version. For example, 0x00030033 = 3.51. This property only applies to providers.


</dt> </dl> </dd> <dt>

<span id="NCRYPT_WINDOW_HANDLE_PROPERTY"></span><span id="ncrypt_window_handle_property"></span>**NCRYPT\_WINDOW\_HANDLE\_PROPERTY**
</dt> <dd> <dl> <dt>

L"HWND Handle"
</dt> <dt>



A pointer to the window handle (**HWND**) to be used as the parent of any user interface that is displayed.

Because undesirable behavior can happen when a user interface is shown by using a **NULL** window handle for the parent, we strongly recommend that a key storage provider not display a user interface unless this property is set.


</dt> </dl> </dd> </dl>

The following values are used to define limits of property data.



| Constant/value                                                                                                                                                                                                                                                 | Description                                                              |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| <span id="NCRYPT_MAX_PROPERTY_DATA"></span><span id="ncrypt_max_property_data"></span><dl> <dt>**NCRYPT\_MAX\_PROPERTY\_DATA**</dt> <dt>0x100000</dt> </dl> | Specifies the maximum size of a property value, in bytes.<br/>     |
| <span id="NCRYPT_MAX_PROPERTY_NAME"></span><span id="ncrypt_max_property_name"></span><dl> <dt>**NCRYPT\_MAX\_PROPERTY\_NAME**</dt> <dt>64</dt> </dl>       | Specifies the maximum size of a property name, in characters.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Ncrypt.h</dt> </dl> |



## See also

<dl> <dt>

[**NCryptGetProperty**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptgetproperty)
</dt> <dt>

[**NCryptSetProperty**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptsetproperty)
</dt> </dl>

