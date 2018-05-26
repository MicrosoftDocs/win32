---
Description: Used with the BCryptGetProperty and BCryptSetProperty functions to identify a property.
ms.assetid: ebcc8202-94b4-47ad-9918-e5bc843a258f
title: Cryptography Primitive Property Identifiers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cryptography Primitive Property Identifiers

The following values are used with the [**BCryptGetProperty**](/windows/win32/Bcrypt/nf-bcrypt-bcryptgetproperty?branch=master) and [**BCryptSetProperty**](/windows/win32/Bcrypt/nf-bcrypt-bcryptsetproperty?branch=master) functions to identify a property.

<dl> <dt>

<span id="BCRYPT_ALGORITHM_NAME"></span><span id="bcrypt_algorithm_name"></span>**BCRYPT\_ALGORITHM\_NAME**
</dt> <dd> <dl> <dt>

L"AlgorithmName"
</dt> <dt>



A null-terminated Unicode string that contains the name of the algorithm.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_AUTH_TAG_LENGTH"></span><span id="bcrypt_auth_tag_length"></span>**BCRYPT\_AUTH\_TAG\_LENGTH**
</dt> <dd> <dl> <dt>

L"AuthTagLength"
</dt> <dt>



The authentication tag lengths that are supported by the algorithm. This property is a [**BCRYPT\_AUTH\_TAG\_LENGTHS\_STRUCT**](/windows/win32/Bcrypt/ns-bcrypt-__bcrypt_key_lengths_struct?branch=master) structure. This property only applies to algorithms.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_BLOCK_LENGTH"></span><span id="bcrypt_block_length"></span>**BCRYPT\_BLOCK\_LENGTH**
</dt> <dd> <dl> <dt>

L"BlockLength"
</dt> <dt>



The size, in bytes, of a cipher block for the algorithm. This property only applies to block cipher algorithms. This data type is a **DWORD**.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_BLOCK_SIZE_LIST"></span><span id="bcrypt_block_size_list"></span>**BCRYPT\_BLOCK\_SIZE\_LIST**
</dt> <dd> <dl> <dt>

L"BlockSizeList"
</dt> <dt>



A list of the block lengths supported by an encryption algorithm. This data type is an array of **DWORDs**. The number of elements in the array can be determined by dividing the number of bytes retrieved by the size of a single **DWORD**.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_CHAINING_MODE"></span><span id="bcrypt_chaining_mode"></span>**BCRYPT\_CHAINING\_MODE**
</dt> <dd> <dl> <dt>

L"ChainingMode"
</dt> <dt>



A pointer to a null-terminated Unicode string that represents the chaining mode of the encryption algorithm. This property can be set on an algorithm handle or a key handle to one of the following values.



| Identifier                   | Value                         | Description                                                                                                                                                                    |
|------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BCRYPT\_CHAIN\_MODE\_CBC** | L"ChainingModeCBC"<br/> | Sets the algorithm's chaining mode to [*cipher block chaining*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-cipher-block-chaining-gly).<br/>            |
| **BCRYPT\_CHAIN\_MODE\_CCM** | L"ChainingModeCCM"<br/> | Sets the algorithm's chaining mode to counter with CBC-MAC mode (CCM).**Windows Vista:** This value is supported beginning with Windows Vista with SP1.<br/> <br/> |
| **BCRYPT\_CHAIN\_MODE\_CFB** | L"ChainingModeCFB"<br/> | Sets the algorithm's chaining mode to [*cipher feedback*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-cipher-feedback-gly).<br/>                              |
| **BCRYPT\_CHAIN\_MODE\_ECB** | L"ChainingModeECB"<br/> | Sets the algorithm's chaining mode to [*electronic codebook*](https://msdn.microsoft.com/library/windows/desktop/ms721575#-security-electronic-codebook-gly).<br/>                  |
| **BCRYPT\_CHAIN\_MODE\_GCM** | L"ChainingModeGCM"<br/> | Sets the algorithm's chaining mode to Galois/counter mode (GCM).**Windows Vista:** This value is supported beginning with Windows Vista with SP1.<br/> <br/>       |
| **BCRYPT\_CHAIN\_MODE\_NA**  | L"ChainingModeN/A"<br/> | The algorithm does not support chaining.<br/>                                                                                                                            |



 


</dt> </dl> </dd> <dt>

<span id="BCRYPT_DH_PARAMETERS"></span><span id="bcrypt_dh_parameters"></span>**BCRYPT\_DH\_PARAMETERS**
</dt> <dd> <dl> <dt>

L"DHParameters"
</dt> <dt>



Specifies parameters to use with a Diffie-Hellman key. This data type is a pointer to a [**BCRYPT\_DH\_PARAMETER\_HEADER**](/windows/win32/Bcrypt/ns-bcrypt-_bcrypt_dh_parameter_header?branch=master) structure. This property can only be set and must be set for the key before the key is completed.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_DSA_PARAMETERS"></span><span id="bcrypt_dsa_parameters"></span>**BCRYPT\_DSA\_PARAMETERS**
</dt> <dd> <dl> <dt>

L"DSAParameters"
</dt> <dt>



Specifies parameters to use with a DSA key. This property is a [**BCRYPT\_DSA\_PARAMETER\_HEADER**](/windows/win32/Bcrypt/ns-bcrypt-_bcrypt_dsa_parameter_header?branch=master) or a [**BCRYPT\_DSA\_PARAMETER\_HEADER\_V2**](/windows/win32/Bcrypt/ns-bcrypt-_bcrypt_dsa_parameter_header_v2?branch=master) structure. This property can only be set and must be set for the key before the key is completed.

**Windows 8:** Beginning with Windows 8, this property can be a [**BCRYPT\_DSA\_PARAMETER\_HEADER\_V2**](/windows/win32/Bcrypt/ns-bcrypt-_bcrypt_dsa_parameter_header_v2?branch=master) structure. Use this structure if the key size exceeds 1024 bits and is less than or equal to 3072 bits. If the key size is greater than or equal to 512 but less than or equal to 1024 bits, use the [**BCRYPT\_DSA\_PARAMETER\_HEADER**](/windows/win32/Bcrypt/ns-bcrypt-_bcrypt_dsa_parameter_header?branch=master) structure.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_EFFECTIVE_KEY_LENGTH"></span><span id="bcrypt_effective_key_length"></span>**BCRYPT\_EFFECTIVE\_KEY\_LENGTH**
</dt> <dd> <dl> <dt>

L"EffectiveKeyLength"
</dt> <dt>



The size, in bits, of the effective length of an RC2 key. This data type is a **DWORD**.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_HASH_BLOCK_LENGTH"></span><span id="bcrypt_hash_block_length"></span>**BCRYPT\_HASH\_BLOCK\_LENGTH**
</dt> <dd> <dl> <dt>

L"HashBlockLength"
</dt> <dt>



The size, in bytes, of the block for a hash. This property only applies to hash algorithms. This data type is a **DWORD**.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_HASH_LENGTH"></span><span id="bcrypt_hash_length"></span>**BCRYPT\_HASH\_LENGTH**
</dt> <dd> <dl> <dt>

L"HashDigestLength"
</dt> <dt>



The size, in bytes, of the hash value of a hash provider. This data type is a **DWORD**.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_HASH_OID_LIST"></span><span id="bcrypt_hash_oid_list"></span>**BCRYPT\_HASH\_OID\_LIST**
</dt> <dd> <dl> <dt>

L"HashOIDList"
</dt> <dt>



The list of [*DER*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-der-gly)-encoded hashing [*object identifiers*](https://msdn.microsoft.com/library/windows/desktop/ms721599#-security-object-identifier-gly) (OIDs). This property is a [**BCRYPT\_OID\_LIST**](/windows/win32/Bcrypt/ns-bcrypt-_bcrypt_oid_list?branch=master) structure. This property can only be read.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_INITIALIZATION_VECTOR"></span><span id="bcrypt_initialization_vector"></span>**BCRYPT\_INITIALIZATION\_VECTOR**
</dt> <dd> <dl> <dt>

L"IV"
</dt> <dt>



Contains the [*initialization vector*](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-initialization-vector-gly) (IV) for a key. This property only applies to keys.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_KEY_LENGTH"></span><span id="bcrypt_key_length"></span>**BCRYPT\_KEY\_LENGTH**
</dt> <dd> <dl> <dt>

L"KeyLength"
</dt> <dt>



The size, in bits, of the key value of a symmetric key provider. This data type is a **DWORD**.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_KEY_LENGTHS"></span><span id="bcrypt_key_lengths"></span>**BCRYPT\_KEY\_LENGTHS**
</dt> <dd> <dl> <dt>

L"KeyLengths"
</dt> <dt>



The key lengths that are supported by the algorithm. This property is a [**BCRYPT\_KEY\_LENGTHS\_STRUCT**](/windows/win32/Bcrypt/ns-bcrypt-__bcrypt_key_lengths_struct?branch=master) structure. This property only applies to algorithms.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_KEY_OBJECT_LENGTH"></span><span id="bcrypt_key_object_length"></span>**BCRYPT\_KEY\_OBJECT\_LENGTH**
</dt> <dd> <dl> <dt>

L"KeyObjectLength"
</dt> <dt>



This property is not used. The **BCRYPT\_OBJECT\_LENGTH** property is used to obtain this information.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_KEY_STRENGTH"></span><span id="bcrypt_key_strength"></span>**BCRYPT\_KEY\_STRENGTH**
</dt> <dd> <dl> <dt>

L"KeyStrength"
</dt> <dt>



The number of bits in the key. This data type is a **DWORD**. This property only applies to keys.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_MESSAGE_BLOCK_LENGTH"></span><span id="bcrypt_message_block_length"></span>**BCRYPT\_MESSAGE\_BLOCK\_LENGTH**
</dt> <dd> <dl> <dt>

L"MessageBlockLength"
</dt> <dt>



This can be set on any key handle that has the CFB chaining mode set. By default, this property is set to 1 for 8-bit CFB. Setting it to the block size in bytes causes full-block CFB to be used.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_MULTI_OBJECT_LENGTH"></span><span id="bcrypt_multi_object_length"></span>**BCRYPT\_MULTI\_OBJECT\_LENGTH**
</dt> <dd> <dl> <dt>

L"MultiObjectLength"
</dt> <dt>



This property returns a [**BCRYPT\_MULTI\_OBJECT\_LENGTH\_STRUCT**](/windows/win32/Bcrypt/ns-bcrypt-_bcrypt_multi_object_length_struct?branch=master), which contains information necessary to calculate the size of an object buffer. This property is only supported on operating system versions that support the [**BCryptCreateMultiHash**](/windows/win32/Bcrypt/nf-bcrypt-bcryptcreatemultihash?branch=master) function.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_OBJECT_LENGTH"></span><span id="bcrypt_object_length"></span>**BCRYPT\_OBJECT\_LENGTH**
</dt> <dd> <dl> <dt>

L"ObjectLength"
</dt> <dt>



The size, in bytes, of the subobject of a provider. This data type is a **DWORD**. Currently, the hash and symmetric cipher algorithm providers use caller-allocated buffers to store their subobjects. For example, the hash provider requires you to allocate memory for the hash object obtained with the [**BCryptCreateHash**](/windows/win32/Bcrypt/nf-bcrypt-bcryptcreatehash?branch=master) function. This property provides the buffer size for a provider's object so you can allocate memory for the object created by the provider.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_PADDING_SCHEMES"></span><span id="bcrypt_padding_schemes"></span>**BCRYPT\_PADDING\_SCHEMES**
</dt> <dd> <dl> <dt>

L"PaddingSchemes"
</dt> <dt>



Represents the padding scheme of the RSA algorithm provider. This data type is a **DWORD**. This can be one of the following values.



| Identifier                             | Value      | Description                                                |
|----------------------------------------|------------|------------------------------------------------------------|
| **BCRYPT\_SUPPORTED\_PAD\_ROUTER**     | 0x00000001 | The provider supports padding added by the router.         |
| **BCRYPT\_SUPPORTED\_PAD\_PKCS1\_ENC** | 0x00000002 | The provider supports the PKCS1 encryption padding scheme. |
| **BCRYPT\_SUPPORTED\_PAD\_PKCS1\_SIG** | 0x00000004 | The provider supports the PKCS1 signature padding scheme.  |
| **BCRYPT\_SUPPORTED\_PAD\_OAEP**       | 0x00000008 | The provider supports the OAEP padding scheme.             |
| **BCRYPT\_SUPPORTED\_PAD\_PSS**        | 0x00000010 | The provider supports the PSS padding scheme.              |



 


</dt> </dl> </dd> <dt>

<span id="BCRYPT_PROVIDER_HANDLE"></span><span id="bcrypt_provider_handle"></span>**BCRYPT\_PROVIDER\_HANDLE**
</dt> <dd> <dl> <dt>

L"ProviderHandle"
</dt> <dt>



The handle of the CNG provider that created the object passed in the *hObject* parameter. This data type is a **BCRYPT\_ALG\_HANDLE**. This property can only be retrieved; it cannot be set.


</dt> </dl> </dd> <dt>

<span id="BCRYPT_SIGNATURE_LENGTH"></span><span id="bcrypt_signature_length"></span>**BCRYPT\_SIGNATURE\_LENGTH**
</dt> <dd> <dl> <dt>

L"SignatureLength"
</dt> <dt>



The size, in bytes, of the length of a signature for a key. This data type is a **DWORD**. This property only applies to keys. This property can only be retrieved; it cannot be set.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Bcrypt.h</dt> </dl> |



 

 




