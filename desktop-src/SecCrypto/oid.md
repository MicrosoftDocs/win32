---
description: Represents an object identifier (OID) that is used by several CAPICOM properties.
ms.assetid: 'd9dc2a9a-920b-41e1-91fb-da1628df577d'
title: OID object
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- OID
api_type:
- COM
api_location:
- Capicom.dll
---

# OID object

\[The **OID** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**Oid Class**](/dotnet/api/system.security.cryptography.oid) in the [**System.Security.Cryptography**](/dotnet/api/system.security.cryptography?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **OID** object represents an [*object identifier*](../secgloss/o-gly.md) (OID) that is used by several CAPICOM properties.

## When to use

The **OID** object is used to perform the following tasks:

-   Set or retrieve a CAPICOM name and display name for the OID.
-   Set or retrieve the dotted number for the OID.

## Members

The **OID** object has these types of members:

-   [Properties](#properties)

### Properties

The **OID** object has these properties.



| Property                                            | Access type           | Description                                                                                      |
|:----------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------|
| [**FriendlyName**](oid-friendlyname.md)<br/> | Read/write<br/> | Sets or retrieves the display name for the OID.<br/>                                       |
| [**Name**](oid-name.md)<br/>                 | Read/write<br/> | Sets or retrieves the CAPICOM-defined name for the OID. This is the default property.<br/> |
| [**Value**](oid-value.md)<br/>               | Read/write<br/> | Sets or retrieves the value of the OID dotted number of the OID.<br/>                      |



 

## Remarks

The **OID** object can be created, and it is safe for scripting. The ProgID for the **OID** object is CAPICOM.OID.1.

The following CAPICOM object properties return an **OID** object:

-   [**PolicyInformation.OID**](policyinformation-oid.md)
-   [**Qualifier.OID**](qualifier-oid.md)
-   [**Extension.OID**](extension-oid.md)
-   [**Template.OID**](template-oid.md)

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
