---
description: Specifies the encrypted byte block size for sample-based pattern encryption.
ms.assetid: 1F370DEC-20B5-456D-BB68-C94E183410F3
title: MFSampleExtension_Encryption_CryptByteBlock attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_Encryption\_CryptByteBlock attribute

Specifies the encrypted byte block size for sample-based pattern encryption.

## Data type

**UINT32**

## Remarks

The number of clear (non-encrypted) bytes in the subsample mapping block are specified in the [MFSampleExtension\_Encryption\_SkipByteBlock](mfsampleextension-encryption-skipbyteblock.md) attribute. If either of these attributes are not present or have a value of 0, it means that the sample data is not encrypted. Either both of these values must be non-zero, positive values, or both must have a value of zero.

In cases where the Source is MP4-based, the value is set based off the values of default\_crypt\_byte\_block within the track encryption box (‘tenc’) in the MP4 header. For more information, see [MFSampleExtension\_Encryption\_ProtectionScheme](mfsampleextension-encryption-protectionscheme.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



 

 




