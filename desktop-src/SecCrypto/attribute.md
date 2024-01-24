---
description: Represents a single authenticated attribute.
ms.assetid: 71c4543b-683f-4ffa-8301-c40c46c490b3
title: Attribute object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Attribute
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Attribute object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**CryptographicAttributeObject Class**](/dotnet/api/system.security.cryptography.cryptographicattributeobject?view=dotnet-plat-ext-3.1&preserve-view=true) in the [**System.Security.Cryptography**](/previous-versions/windows/) namespace.\]

The **Attribute** object represents a single authenticated attribute.

## When to use

The **Attribute** object is used to perform the following tasks:

-   Set or retrieve the CAPICOM name of the attribute.
-   Set or retrieve the value of the attribute, such as signing time, the name of the document signed, or a description of the document signed.

## Members

The **Attribute** object has these types of members:

-   [Properties](#properties)

### Properties

The **Attribute** object has these properties.



| Property                                    | Access type           | Description                                                                                   |
|:--------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------|
| [**Name**](attribute-name.md)<br/>   | Read/write<br/> | Sets or retrieves the CAPICOM name of the attribute. This is the default property.<br/> |
| [**Value**](attribute-value.md)<br/> | Read/write<br/> | Sets or retrieves the value of the attribute.<br/>                                      |



 

## Remarks

The **Attribute** object can be created, and it is safe for scripting. The ProgID for the **Attribute** object is CAPICOM.Attribute.1.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 
