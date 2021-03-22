---
description: Generates a secure random number using the default cryptographic service provider (CSP).
ms.assetid: 52c49f73-58b8-455f-9368-54f38de55776
title: Utilities.GetRandom method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Utilities.GetRandom
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Utilities.GetRandom method

\[The **GetRandom** method is available for use in the operating systems specified in the Requirements section.\]

The **GetRandom** method generates a secure random number using the default [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).

## Syntax


```VB
Utilities.GetRandom( _
  [ ByVal Length ], _
  [ ByVal EncodingType ] _
)
```



## Parameters

<dl> <dt>

*Length* \[in, optional\]
</dt> <dd>

The length, in bytes, of the random number to create. The default value is 8 bytes.

</dd> <dt>

*EncodingType* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_ENCODING\_TYPE**](capicom-encoding-type.md) enumeration that indicates the type of encoding to use for the generated random number. The default value is CAPICOM\_ENCODE\_BINARY. This parameter can be one of the following values.



| Value                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_ENCODE_ANY"></span><span id="capicom_encode_any"></span><dl> <dt>**CAPICOM\_ENCODE\_ANY**</dt> </dl>          | This encoding type is used only when the input data has an unknown encoding type. If this value is used to specify the output's encoding type, CAPICOM\_ENCODE\_BASE64 will be used instead. Introduced in CAPICOM 2.0.<br/> |
| <span id="CAPICOM_ENCODE_BASE64"></span><span id="capicom_encode_base64"></span><dl> <dt>**CAPICOM\_ENCODE\_BASE64**</dt> </dl> | Data is saved as a base64-encoded string.<br/>                                                                                                                                                                               |
| <span id="CAPICOM_ENCODE_BINARY"></span><span id="capicom_encode_binary"></span><dl> <dt>**CAPICOM\_ENCODE\_BINARY**</dt> </dl> | Data is saved as a pure binary sequence.<br/>                                                                                                                                                                                |



 

</dd> </dl>

## Return value

A randomly generated number *Length* bytes long, with the specified encoding.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Utilities**](utilities.md)
</dt> </dl>

 

 
