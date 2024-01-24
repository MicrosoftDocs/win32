---
description: Provides functionality for random number generation, conversions, and encoding and decoding from base64.
ms.assetid: c0073361-5d0d-4915-8110-02f6e1e0714e
title: Utilities object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Utilities
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Utilities object

\[The **Utilities** object is available for use in the operating systems specified in the Requirements section.\]

The **Utilities** object provides functionality for random number generation, conversions, and encoding and decoding from base64.

## When to use

The **Utilities** object is used to perform the following tasks:

-   Encode a string as base64 or decode a string from base64.
-   Convert a binary-packed string to a byte array and vice versa.
-   Convert a binary-packed string to a hexadecimal string and vice versa.
-   Generate a secure random number.
-   Convert local time to Coordinated Universal Time (Greenwich Mean Time) and vice versa.

## Members

The **Utilities** object has these types of members:

-   [Methods](#methods)

### Methods

The **Utilities** object has these methods.



| Method                                                               | Description                                                                  |
|:---------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [**Base64Decode**](utilities-base64decode.md)                       | Decodes a string from base64.<br/>                                     |
| [**Base64Encode**](utilities-base64encode.md)                       | Encodes a string as base64.<br/>                                       |
| [**BinaryStringToByteArray**](utilities-binarystringtobytearray.md) | Converts a binary-packed string to an array of bytes.<br/>             |
| [**BinaryToHex**](utilities-binarytohex.md)                         | Converts a binary-packed string to a hexadecimal string.<br/>          |
| [**ByteArrayToBinaryString**](utilities-bytearraytobinarystring.md) | Converts an array of bytes to a binary-packed string.<br/>             |
| [**GetRandom**](utilities-getrandom.md)                             | Generates a secure random number.<br/>                                 |
| [**HexToBinary**](utilities-hextobinary.md)                         | Converts a hexadecimal string to a binary-packed string.<br/>          |
| [**LocalTimeToUTCTime**](utilities-localtimetoutctime.md)           | Converts the computer's local time to Coordinated Universal Time.<br/> |
| [**UTCTimeToLocalTime**](utilities-utctimetolocaltime.md)           | Converts Coordinated Universal Time to the computer's local time.<br/> |



 

## Remarks

The **Utilities** object can be created, and it is safe for scripting. The ProgID for the **Utilities** object is CAPICOM.Utilities.1.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




