---
description: ICE34 validates that each radio button on every RadioButtonGroup Control has a property in the Property column of the RadioButton table that specifies its radio button group.
ms.assetid: 23a88a5a-89e9-47bc-9c0a-6101ce03123c
title: ICE34
ms.topic: article
ms.date: 05/31/2018
---

# ICE34

ICE34 validates that each radio button on every [RadioButtonGroup Control](radiobuttongroup-control.md) has a property in the Property column of the [RadioButton table](radiobutton-table.md) that specifies its radio button group. ICE34 validates that this property exists and is set to a default value in the [Property table](property-table.md) which is equal to one of the group's radio button values in the Value column of the RadioButton table.

A radio button group must have a default for users to be able to select a choice using the TAB key. This is required for proper user accessibility.

ICE34 reports missing tables.

## Result

ICE34 post an error message if there is a radio button that specifies an invalid property.

## Example

ICE34 reports the following errors for the example shown.



| ICE34 error                                                                                                                                                                | Description                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Control DialogA.Control2 must have a property because it is of type RadioButtonGroup.                                                                                      | There is a [RadioButtonGroup control](radiobuttongroup-control.md), without the [Indirect control](indirect-control-attribute.md) bit set in the Attributes column of the [Control table](control-table.md), that does not have a property listed in the Property column. |
| Maybe is not a valid default value for the RadioButtonGroup using property Property3. The value must be listed as an option in the RadioButtonGroup table.                 | There is a default value for a property specified in the Value column of the [Property table](property-table.md) that is not one of the values for the radio button group specified in the Value column of the [RadioButton table](radiobutton-table.md).                  |
| Property PropertyB must be defined because it is an indirect property of a RadioButtonGroup control DialogA.Control4                                                       | The property referenced by this RadioButton group is an indirect property, and the value of the indirect property is not one of the choices for the RadioButton group.                                                                                                       |
| Maybe is not a valid default value for the property PropertyA. The property is an indirect RadioButtonGroup property of control DialogA.Control5 (via property Property5). | The value of the indirect property referenced via the control is not one of the default values for that RadioButtonGroup.                                                                                                                                                    |



 

[Control Table](control-table.md) (partial)



| Dialog  | Control  | Type             | Attributes | Property  |
|---------|----------|------------------|------------|-----------|
| DialogA | Control1 | RadioButtonGroup | 0          | Property1 |
| DialogA | Control2 | RadioButtonGroup | 0          |           |
| DialogA | Control3 | RadioButtonGroup | 0          | Property3 |
| DialogA | Control4 | RadioButtonGroup | 8          | Property4 |
| DialogA | Control5 | RadioButtonGroup | 8          | Property5 |



 

[Property Table](property-table.md) (partial)



| Property  | Value     |
|-----------|-----------|
| Property1 | Yes       |
| Property3 | Maybe     |
| Property4 | PropertyB |
| Property5 | PropertyA |
| PropertyA | Maybe     |



 

[RadioButton Table](radiobutton-table.md) (partial)



| Property  | Order | Value |
|-----------|-------|-------|
| Property1 | 1     | Yes   |
| Property1 | 2     | Now   |
| Property2 | 1     | Yes   |
| Property2 | 2     | No    |
| Property3 | 1     | Yes   |
| Property3 | 2     | No    |
| Property4 | 1     | Yes   |
| Property4 | 2     | No    |
| PropertyA | 1     | Yes   |
| PropertyA | 2     | No    |
| PropertyB | 1     | Yes   |
| PropertyB | 2     | No    |



 

To fix the errors reported by this ICE, check the following:

-   That every RadioButton control entry without the indirect attribute set has a property listed in the Property column:
-   That every such property has at least one corresponding entry in the RadioButton table.
-   That every such property is defined in the Property table, with a value that is one of the choices from the RadioButton table.
-   That every property referenced in the Property column of a RadioButton control with the indirect attribute set is defined in the Property table.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



