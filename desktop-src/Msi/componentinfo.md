---
description: The ComponentInfo object represents additional details about a component that may be obtained via a call from MsiGetComponentPathEx.
ms.assetid: 9b0ad0a1-c49f-4b14-817b-0cfc9b228d77
title: ComponentInfo object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ComponentInfo
api_type: 
- COM
api_location: 
- Msi.dll
---

# ComponentInfo object

The ComponentInfo object represents additional details about a component that may be obtained via a call from MsiGetComponentPathEx.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This object is available beginning with Windows Installer 5.0.

## Members

The **ComponentInfo** object has these types of members:

-   [Properties](#properties)

### Properties

The **ComponentInfo** object has these properties.



| Property                                                        | Description                                                 |
|:----------------------------------------------------------------|:------------------------------------------------------------|
| [**ComponentCode**](componentinfo-componentcode.md)<br/> | The component code of the component in question.<br/> |
| [**Path**](componentinfo-componentcode.md)<br/>          | The path of the component.<br/>                       |
| [**State**](componentinfo-state.md)<br/>                 | The state of the component.<br/>                      |



 

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 or later.<br/>                                         |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl> |
| IID<br/>     | IID\_IComponentInfo is defined as 000C1099-0000-0000-C000-000000000046<br/>  |



## See also

<dl> <dt>

[Using the Automation Interface](using-the-automation-interface.md)
</dt> <dt>

[Windows Installer Scripting Examples](windows-installer-scripting-examples.md)
</dt> </dl>

 

 




