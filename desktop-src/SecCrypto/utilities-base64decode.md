---
description: Decodes a string from base64.
ms.assetid: acf2dba6-a0e8-4b77-a5a6-93cfa6afe874
title: Utilities.Base64Decode method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Utilities.Base64Decode
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Utilities.Base64Decode method

\[The **Base64Decode** method is available for use in the operating systems specified in the Requirements section.\]

The **Base64Decode** method decodes a string from base64.

## Syntax


```VB
Utilities.Base64Decode( _
  ByVal EncodedString _
)
```



## Parameters

<dl> <dt>

*EncodedString* \[in\]
</dt> <dd>

The base64-encoded string to decode.

</dd> </dl>

## Return value

The decoded string.

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

 

 




