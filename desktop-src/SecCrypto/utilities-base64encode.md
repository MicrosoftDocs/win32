---
description: Encodes a string as base64.
ms.assetid: 73a279e3-40b0-4db8-89d3-95627f0878dd
title: Utilities.Base64Encode method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Utilities.Base64Encode
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Utilities.Base64Encode method

\[The **Base64Encode** method is available for use in the operating systems specified in the Requirements section.\]

The **Base64Encode** method encodes a string as base64.

## Syntax


```VB
Utilities.Base64Encode( _
  ByVal SrcString _
)
```



## Parameters

<dl> <dt>

*SrcString* \[in\]
</dt> <dd>

The string to encode as base64.

</dd> </dl>

## Return value

The base64-encoded string.

## Remarks

Base64 encoding is the scheme used to transmit binary data. Base64 processes data as 24-bit groups, mapping this data to four encoded characters. Base64 encoding is sometimes referred to as 3-to-4 encoding. Each 6 bits of the 24-bit group is used as an index into a mapping table (the base64 alphabet) to obtain a character for the encoded data. The encoded data has line lengths that are limited to 76 characters.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Utilities**](utilities.md)
</dt> </dl>

 

 




