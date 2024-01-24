---
description: The Client object represents a relationship between a component and client product.
ms.assetid: ac1fbd74-fbc4-4f76-8e14-af48443a8528
title: Client object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Client
api_type: 
- COM
api_location: 
- Msi.dll
---

# Client object

The Client object represents a relationship between a component and client product.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This object is available beginning with Windows Installer 5.0.

## Members

The **Client** object has these types of members:

-   [Properties](#properties)

### Properties

The **Client** object has these properties.



| Property                                                 | Description                                                 |
|:---------------------------------------------------------|:------------------------------------------------------------|
| [**ComponentCode**](client-componentcode.md)<br/> | The component code of the component in question.<br/> |
| [**Context**](client-context.md)<br/>             | The context of the product.<br/>                      |
| [**ProductCode**](client-productcode.md)<br/>     | The client product of the component in question.<br/> |
| [**UserSID**](client-usersid.md)<br/>             | The user SID for the component.<br/>                  |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 or later.<br/>                                         |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl> |
| IID<br/>     | IID\_IClient is defined as 000C1098-0000-0000-C000-000000000046<br/>         |



## See also

<dl> <dt>

[Using the Automation Interface](using-the-automation-interface.md)
</dt> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




