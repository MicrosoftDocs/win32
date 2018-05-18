---
Description: 'Represents an object identifier (OID) that is used by several CAPICOM properties.'
ms.assetid: '6c1eb2cc-84ac-4920-99ba-56ac8de4a851'
title: OID object
---

# OID object

\[The **OID** object is available for use in the operating systems specified in the Requirements section. Instead, use the [**Oid Class**](T:System.Security.Cryptography.Oid) in the [**System.Security.Cryptography**](frlrfSystemSecurityCryptography) namespace.\]

The **OID** object represents an [*object identifier*](security.o_gly#-security-object-identifier-gly) (OID) that is used by several CAPICOM properties.

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



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




