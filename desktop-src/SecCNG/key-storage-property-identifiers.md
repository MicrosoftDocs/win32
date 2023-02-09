---
description: Used to identify a key storage property.
ms.assetid: 407f0e42-07c8-4ec6-81c6-f8bde005adb0
title: Key Storage Property Identifiers (Ncrypt.h)
ms.topic: reference
ms.date: 02/08/2023
---

# Key Storage Property Identifiers

The following values are used to identify a key storage property.

## Identifiers

### NCRYPT\_ALGORITHM\_GROUP\_PROPERTY

`L"Algorithm Group"`

A null-terminated Unicode string that contains the name of the object's algorithm group. This property only applies to keys. The following identifiers are returned by the Microsoft key storage provider.

| Identifier                                     | Value              | Description                                                   |
|------------------------------------------------|--------------------|---------------------------------------------------------------|
| **NCRYPT\_RSA\_ALGORITHM\_GROUP** | "RSA" | The RSA algorithm group. |
| **NCRYPT\_DH\_ALGORITHM\_GROUP** | "DH" | The Diffie-Hellman algorithm group. |
| **NCRYPT\_DSA\_ALGORITHM\_GROUP** | "DSA" | The DSA algorithm group. |
| **NCRYPT\_ECDSA\_ALGORITHM\_GROUP** | "ECDSA" | The elliptic curve DSA algorithm group. |
| **NCRYPT\_ECDH\_ALGORITHM\_GROUP** | "ECDH" | The elliptic curve Diffie-Hellman algorithm group. |

### NCRYPT\_ALGORITHM\_PROPERTY

`L"Algorithm Name"`

A null-terminated Unicode string that contains the name of the object's algorithm. This can be one of the predefined [**CNG Algorithm Identifiers**](cng-algorithm-identifiers.md) or another registered algorithm identifier. This property only applies to keys.

### NCRYPT\_ASSOCIATED\_ECDH\_KEY

`L"SmartCardAssociatedECDHKey"`

An **LPWSTR** value that indicates the container name of the **Elliptic Curve Diffie-Hellman (ECDH)** key to use during logon for a given handle to an **Elliptic Curve Digital Signature Algorithm (ECDSA)** key. If there are no ECDH keys on the card, the [*key storage provider*](/windows/win32/SecGloss/k-gly) (KSP) returns `NTE_NOT_FOUND`. This property applies to ECDSA keys for logon with smart cards. The property is supported by the Microsoft Smart Card key storage provider and not by the Microsoft Software key storage provider.

**Windows Server 2008 and Windows Vista:** This value is not supported.

### NCRYPT\_BLOCK\_LENGTH\_PROPERTY

`L"Block Length"`

A **DWORD** that contains the length, in bytes, of the encryption block. This property only applies to keys that support encryption.

### NCRYPT\_CERTIFICATE\_PROPERTY

`L"SmartCardKeyCertificate"`

A [*BLOB*](/windows/win32/SecGloss/b-gly) that contains an X.509 certificate that is associated with the key.

**Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** A [*BLOB*](/windows/win32/SecGloss/b-gly) that contains the [*smart card*](/windows/win32/SecGloss/s-gly) key [*certificate*](/windows/win32/SecGloss/c-gly). This property is not supported by the Microsoft Software Key Storage Provider.

### NCRYPT\_DH\_PARAMETERS\_PROPERTY

`L"DHParameters"`

Specifies parameters to use with a Diffie-Hellman key. This data type is a pointer to a [**BCRYPT\_DH\_PARAMETER\_HEADER**](/windows/win32/api/Bcrypt/ns-bcrypt-bcrypt_dh_parameter_header) structure. This property can only be set and must be set for the key before the key is completed.

### NCRYPT\_EXPORT\_POLICY\_PROPERTY

`L"Export Policy"`

A **DWORD** that contains a set of flags that specify the export policy for a persisted key. This property only applies to keys. This can contain zero or a combination of one or more of the following values.

| Identifier | Value | Description |
|------------|------------|------------|
| **NCRYPT\_ALLOW\_EXPORT\_FLAG** | 0x00000001 | The private key can be exported. |
| **NCRYPT\_ALLOW\_PLAINTEXT\_EXPORT\_FLAG** | 0x00000002 | The private key can be exported in plaintext form. |
| **NCRYPT\_ALLOW\_ARCHIVING\_FLAG** | 0x00000004 | The private key can be exported once for archiving purposes. This flag only applies to the original key handle on which it is set. This policy can only be applied to the original key handle. After the key handle has been closed, the key can no longer be exported for archiving purposes. |
| **NCRYPT\_ALLOW\_PLAINTEXT\_ARCHIVING\_FLAG** | 0x00000008 | The private key can be exported once in plaintext form for archiving purposes. This flag only applies to the original key handle on which it is set. This policy can only be applied to the original key handle. After the key handle has been closed, the key can no longer be exported for archiving purposes. |

### NCRYPT\_IMPL\_TYPE\_PROPERTY

`L"Impl Type"`

A **DWORD** that contains a set of flags that define implementation details of the provider. This property only applies to key storage providers. This can contain zero or a combination of one or more of the following values.

| Identifier                            | Value      | Description                                               |
|---------------------------------------|------------|-----------------------------------------------------------|
| **NCRYPT\_IMPL\_HARDWARE\_FLAG**      | 0x00000001 | The provider is hardware based.                           |
| **NCRYPT\_IMPL\_SOFTWARE\_FLAG**      | 0x00000002 | The provider is software based.                           |
| **NCRYPT\_IMPL\_REMOVABLE\_FLAG**     | 0x00000008 | The provider is removable.                                |
| **NCRYPT\_IMPL\_HARDWARE\_RNG\_FLAG** | 0x00000010 | The provider is a hardware based random number generator. |

### NCRYPT\_KEY\_TYPE\_PROPERTY

`L"Key Type"`

A **DWORD** that contains a set of flags that define the key type. This property only applies to keys. This can contain zero or the following value.

| Identifier | Value | Description |
|------------|------------|------------|
| **NCRYPT\_MACHINE\_KEY\_FLAG** | 0x00000020 | The key applies to the local computer. If this flag is not present, the key applies to the current user. |

### NCRYPT\_KEY\_USAGE\_PROPERTY

`L"Key Usage"`

A **DWORD** that contains a set of flags that define the usage details for a key. This property only applies to keys. This can contain zero or a combination of one or more of the following values.

| Identifier                              | Value      | Description                                          |
|-----------------------------------------|------------|------------------------------------------------------|
| **NCRYPT\_ALLOW\_DECRYPT\_FLAG**        | 0x00000001 | The key can be used for decryption.                  |
| **NCRYPT\_ALLOW\_SIGNING\_FLAG**        | 0x00000002 | The key can be used for signing.                     |
| **NCRYPT\_ALLOW\_KEY\_AGREEMENT\_FLAG** | 0x00000004 | The key can be used for secret agreement encryption. |
| **NCRYPT\_ALLOW\_ALL\_USAGES**          | 0x00ffffff | The key can be used for any purpose.                 |

### NCRYPT\_LAST\_MODIFIED\_PROPERTY

`L"Modified"`

Indicates when the key was last modified. This data type is a pointer to a [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure. This property only applies to persisted keys.

### NCRYPT\_LENGTH\_PROPERTY

`L"Length"`

A **DWORD** that contains the length, in bits, of the key. This property only applies to keys.

### NCRYPT\_LENGTHS\_PROPERTY

`L"Lengths"`

Indicates the key sizes that are supported by the key. This data type is a pointer to an [**NCRYPT\_SUPPORTED\_LENGTHS**](/windows/win32/api/Ncrypt/ns-ncrypt-ncrypt_supported_lengths) structure that contains this information. This property only applies to keys.

### NCRYPT\_MAX\_NAME\_LENGTH\_PROPERTY

`L"Max Name Length"`

A **DWORD** that contains the maximum length, in characters, of the name of a persistent key. This property only applies to a provider.

This property is primarily intended to be used by key storage providers that store their keys on a device that has a limited amount of available memory, such as a smart card.

### NCRYPT\_NAME\_PROPERTY

`L"Name"`

A pointer to a null-terminated Unicode string that contains the name of the object.

### NCRYPT\_PIN\_PROMPT\_PROPERTY

`L"SmartCardPinPrompt"`

This value is not supported.

### NCRYPT\_PIN\_PROPERTY

`L"SmartCardPin"`

A pointer to a null-terminated Unicode string that contains the PIN. The PIN is used for a smart card key or the password for a password-protected key stored in a software-based KSP. This property can only be set. Microsoft KSPs will cache this value so that the user is only prompted once per process.

### NCRYPT\_PROVIDER\_HANDLE\_PROPERTY

`L"Provider Handle"`

An **NCRYPT\_PROV\_HANDLE** that contains the handle of the CNG key storage provider. When you are finished using the handle, you must call [**NCryptFreeObject**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptfreeobject) to release it.

### NCRYPT\_READER\_PROPERTY

`L"SmartCardReader"`

A pointer to a null-terminated Unicode string that contains the name of the smart card reader. This property can only be set.

### NCRYPT\_ROOT\_CERTSTORE\_PROPERTY

`L"SmartcardRootCertStore"`

An **HCERTSTORE** that represents the smart card root certificate store.

### NCRYPT\_SCARD\_PIN\_ID

`L"SmartCardPinId"`

A pointer to the `PIN_ID` value associated with a given [*cryptographic key*](/windows/win32/SecGloss/c-gly) on a [*smart card*](/windows/win32/SecGloss/s-gly). This is a read-only property. The `PIN_ID` data type is defined in `Cardmod.h`.

**Windows Server 2008 and Windows Vista:** This value is not supported.

### NCRYPT\_SCARD\_PIN\_INFO

`L"SmartCardPinInfo"`

A pointer to [**PIN\_INFO**](/windows/win32/api/mbnapi/ns-mbnapi-mbn_pin_info) structure of the PIN associated with a given cryptographic key on the smart card. The caller provides the key handle. This property is a read-only property. The `PIN_INFO` structure is defined in `Cardmod.h`.

**Windows Server 2008 and Windows Vista:** This value is not supported.

### NCRYPT\_SECURE\_PIN\_PROPERTY

`L"SmartCardSecurePin"`

A pointer to a null-terminated Unicode string that contains the smart card session PIN. This property can only be set.

**Windows Vista:** This property is not supported.

### NCRYPT\_SECURITY\_DESCR\_PROPERTY

`L"Security Descr"`

A pointer to a [**SECURITY\_DESCRIPTOR**](/windows/win32/api/winnt/ns-winnt-security_descriptor) structure that contains access control information for the key. This property only applies to persistent keys. The *dwFlags* parameter of the [**NCryptGetProperty**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptgetproperty) or [**NCryptSetProperty**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptsetproperty) function identifies the part of the security descriptor to get or set.

### NCRYPT\_SECURITY\_DESCR\_SUPPORT\_PROPERTY

`L"Security Descr Support"`

Indicates whether the provider supports security descriptors for keys. This property is a **DWORD** that contains 1 if the provider supports security descriptors for keys. If this property contains any other value, or if the [**NCryptGetProperty**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptgetproperty) function returns `NTE_NOT_SUPPORTED`, then the provider does not support security descriptors for keys. This property only applies to providers.

### NCRYPT\_SMARTCARD\_GUID\_PROPERTY

`L"SmartCardGuid"`

A BLOB that contains the identifier of the smart card.

### NCRYPT\_UI\_POLICY\_PROPERTY

`L"UI Policy"`

If used with the [**NCryptSetProperty**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptsetproperty) or [**NCryptGetProperty**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptgetproperty) function, this is a pointer to an [**NCRYPT\_UI\_POLICY**](/windows/win32/api/Ncrypt/ns-ncrypt-ncrypt_ui_policy) structure that contains the strong key user interface policy for the key. This property only applies to persistent keys. This property can only be set when the key is being generated. Once the [**NCryptFinalizeKey**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptfinalizekey) function has been called for this key, this property becomes read-only.

A key storage provider can receive this parameter through an [**NCryptSetPropertyFn**](https://www.bing.com/search?q=**NCryptSetPropertyFn**) callback function. The parameter value is an `NCRYPT_UI_POLICY_BLOB` structure that contains the same information. Similarly, when an application makes a request through NCryptSetPropertyFn to the provider to return this property, the provider is expected to return an `NCRYPT_UI_POLICY_BLOB` structure.

### NCRYPT\_UNIQUE\_NAME\_PROPERTY

`L"Unique Name"`

A pointer to a null-terminated Unicode string that contains the unique name of the object. This is an alternate name that can be used when accessing the key. This property is used when it is thought that the key name originally passed to [**NCryptCreatePersistedKey**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptcreatepersistedkey) is not unique enough to reliably identify the persisted key. The Microsoft key storage provider will return the file name of the key as this property.

### NCRYPT\_USE\_CONTEXT\_PROPERTY

`L"Use Context"`

A pointer to a null-terminated Unicode string that describes the context of the operation. This property is not persistent and can be set on either a provider or a key. A key does not have access to the `NCRYPT_USE_CONTEXT_PROPERTY` property of the provider because the property is specific only to the handle it is set for.

An example where this property would be used in the context of a provider is a key storage provider that needs to prompt the user during a call to [**NCryptOpenKey**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptopenkey) (for example, "Insert your smart card in the reader."). Because the key handle is not available until after **NCryptOpenKey** returns, the application should set this property on the provider handle prior to calling **NCryptOpenKey**.

An example where this property would be used in the context of a key handle is a key storage provider that needs to prompt the user during an operation using the key (for example, "This application needs to use this key to sign a document."). The provider could then relay this context information to the user in any user interface shown during the operation.

### NCRYPT\_USE\_COUNT\_ENABLED\_PROPERTY

`L"Enabled Use Count"`

Indicates whether the provider supports usage counting for keys. This property is a **DWORD** that contains 1 if the provider supports usage counting for keys. If this property contains any other value, or if the [**NCryptGetProperty**](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptgetproperty) function returns `NTE_NOT_SUPPORTED`, then the provider does not support usage counting for keys. This property only applies to providers.

### NCRYPT\_USE\_COUNT\_PROPERTY

`L"Use Count"`

A [**ULARGE\_INTEGER**](/windows/win32/api/winnt/ns-winnt-ularge_integer~r1) variable that contains the number of operations that the specified [*private key*](/windows/win32/SecGloss/p-gly) has performed. This property is optional and may not be supported by all providers. Providers that support this property on keys should also support the `NCRYPT_USE_COUNT_ENABLED_PROPERTY` property on the provider handle. The Microsoft key storage provider does not support this property. This property only applies to persistent keys.

### NCRYPT\_USER\_CERTSTORE\_PROPERTY

`L"SmartCardUserCertStore"`

An **HCERTSTORE** that represents the smart card user certificate store.

### NCRYPT\_VERSION\_PROPERTY

`L"Version"`

A **DWORD** that contains the software version of the provider. The high word contains the major version and the low word contains the minor version. For example, `0x00030033 = 3.51`. This property only applies to providers.

### NCRYPT\_WINDOW\_HANDLE\_PROPERTY

`L"HWND Handle"`

A pointer to the window handle (**HWND**) to be used as the parent of any user interface that is displayed.

Because undesirable behavior can happen when a user interface is shown by using a **NULL** window handle for the parent, we strongly recommend that a key storage provider not display a user interface unless this property is set.

The following values are used to define limits of property data.

| Constant | Value | Description |
|--------|--------|--------|
| **NCRYPT\_MAX\_PROPERTY\_DATA** | 0x100000 | Specifies the maximum size of a property value, in bytes. |
| **NCRYPT\_MAX\_PROPERTY\_NAME** | 64 | Specifies the maximum size of a property name, in characters. |

## Requirements

| Requirement | Value |
|--------|--------|
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Header | Ncrypt.h |

## See also

- [**NCryptGetProperty**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptgetproperty)

- [**NCryptSetProperty**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptsetproperty)
