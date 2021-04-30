---
description: The ConfigurableItem object represents a single row from the ModuleConfiguration table.
ms.assetid: bbd0d9bc-a463-4cd8-93ee-963dcee8efa6
title: ConfigurableItem object (Mergemod.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ConfigurableItem
- IMsmConfigurableItem
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# ConfigurableItem object

The **ConfigurableItem object** represents a single row from the [ModuleConfiguration table](moduleconfiguration-table.md). This is a single configurable "attribute" from the module. The interface consists read-only properties, one for each column in the ModuleConfiguration table. The Interface definition is as follows.

## Members

The **ConfigurableItem** object has these types of members:

-   [Properties](#properties)

### Properties

The **ConfigurableItem** object has these properties.



| Property                                                         | Description                                                                                                                               |
|:-----------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| [**Attributes**](configurableitem-attributes.md)<br/>     | Returns the value in the Attributes field of this object's record in the ModuleConfiguration table.<br/>                            |
| [**Context**](configurableitem-context.md)<br/>           | Returns the value in the Context field of this object's record in the ModuleConfiguration table.<br/>                               |
| [**DefaultValue**](configurableitem-defaultvalue.md)<br/> | Returns the value in the DefaultValue field of this object's record in the ModuleConfiguration table.<br/>                          |
| [**Description**](configurableitem-description.md)<br/>   | Returns the value in the Description field of this object's record in the ModuleConfiguration table.<br/>                           |
| [**DisplayName**](configurableitem-displayname.md)<br/>   | Returns the value in the DisplayName field of this object's record in the ModuleConfiguration table.<br/>                           |
| [**Format**](configurableitem-format.md)<br/>             | Returns the value in the Format field of this object's record in the ModuleConfiguration table.<br/>                                |
| [**HelpKeyword**](configurableitem-helpkeyword.md)<br/>   | Returns the value in the HelpKeyword field of this object's record in the ModuleConfiguration table.<br/>                           |
| [**HelpLocation**](configurableitem-helplocation.md)<br/> | Returns the value in the HelpLocation field of this object's record in the ModuleConfiguration table.<br/>                          |
| [**Name**](configurableitem-name.md)<br/>                 | Returns the value in the Name field of this object's record in the [ModuleConfiguration table](moduleconfiguration-table.md).<br/> |
| [**Type**](configurableitem-type.md)<br/>                 | Returns the value in the Type field of this object's record in the ModuleConfiguration table.<br/>                                  |



 

## C++

interface **IMsmConfigurableItem : IDispatch**

## Interface ID



| Constant                      | Value                                  |
|-------------------------------|----------------------------------------|
| **IID\_IMsmConfigurableItem** | {4D6E6284-D21D-401E-84F6-909E00B50F71} |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 2.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 




