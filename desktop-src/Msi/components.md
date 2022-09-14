---
description: The Component object represents a unique instance of a component that is available for enumeration.
ms.assetid: 'cdc99bc3-9e2a-49db-8c01-b9634aefac38'
title: Component object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Component
api_type: 
- COM
api_location: 
- Msi.dll
---

# Component object

The Component object represents a unique instance of a component that is available for enumeration.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This object is available beginning with Windows Installer 5.0.

## Members

The **Component** object has these types of members:

-   [Properties](#properties)

### Properties

The **Component** object has these properties.



| Property                                                    | Description                                                                               |
|:------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**ComponentCode**](component-componentcode.md)<br/> | The component code of the component in question.<br/>                               |
| [**Context**](component-context.md)<br/>             | The context that was determined to be applicable to the component in question.<br/> |
| [**UserSID**](component-usersid.md)<br/>             | The user SID for the enumerated component.<br/>                                     |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 or later.<br/>                                         |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl> |
| IID<br/>     | IID\_IComponent is defined as 000C1097-0000-0000-C000-000000000046<br/>      |



## See also

<dl> <dt>

[Using the Automation Interface](using-the-automation-interface.md)
</dt> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




