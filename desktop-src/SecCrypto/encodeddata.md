---
description: Represents a block of ASN.1 encoded data.
ms.assetid: af7acc5f-da0a-4235-8496-05db94664ea5
title: EncodedData object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- EncodedData
api_type:
- COM
api_location:
- Capicom.dll
---

# EncodedData object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**AsnEncodedData Class**](/dotnet/api/system.security.cryptography.asnencodeddata) in the [**System.Security.Cryptography**](/dotnet/api/system.security.cryptography) namespace.\]

The **EncodedData** object represents a block of ASN.1 encoded data.

## When to use

The **EncodedData** object is returned by several CAPICOM object properties. When returned, this object is used to perform the following tasks:

-   Obtain a string representation of the encoded data.
-   Obtain the decoder object, if it exists, that is associated with the encoded data.
-   Determine the type of encoded data.

## Members

The **EncodedData** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **EncodedData** object has these methods.



| Method                                 | Description                                                     |
|:---------------------------------------|:----------------------------------------------------------------|
| [**Decoder**](encodeddata-decoder.md) | Obtains a decoder object, if one exists.<br/>             |
| [**Format**](encodeddata-format.md)   | Returns a string representation of the encoded data.<br/> |



 

### Properties

The **EncodedData** object has these properties.



| Property                                      | Access type          | Description                                                          |
|:----------------------------------------------|:---------------------|:---------------------------------------------------------------------|
| [**Value**](encodeddata-value.md)<br/> | Read-only<br/> | Retrieves the encoded data. This is the default property.<br/> |



 

## Remarks

The only supported type of encoded data is [**CertificatePolicies**](certificatepolicies.md).

The **EncodedData** object cannot be created.

The following CAPICOM object properties return an **EncodedData** object:

-   **PublicKey.EncodedKey**
-   **PublicKey.EncodedParameters**
-   **Extension.EncodedData**
-   **Policy.EncodedData**

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
