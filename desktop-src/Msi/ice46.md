---
description: ICE46 checks for custom properties in conditions, formatted text, and other locations that differ from a system defined property only by the case of one or more characters.
ms.assetid: 892d7462-0222-4fa0-b14c-17742a266c0a
title: ICE46
ms.topic: article
ms.date: 05/31/2018
---

# ICE46

ICE46 checks for custom properties in conditions, formatted text, and other locations that differ from a system defined property only by the case of one or more characters.

## Result

ICE46 posts an informational message if there is a custom property in a condition, formatted text, and other location that differs from a system defined properties only in the case of one or more characters.

## Example

ICE46 reports the following errors for the example shown.



| ICE46 error                                                                                                                                            | Description                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Property ReinstallMode defined in property table differs from another defined property only by case.                                                   | The system defined property name **REINSTALLMODE** differs from the custom property by case only. Properties are case sensitive, so custom property is not the same as the system property. This is a common cause of errors. |
| Property 'Myproperty' referenced in column 'InstallExecuteSequence'.'Condition' of row 'InstallFinalize' differs from a defined property by case only. | The property table defines the table MyProperty, but the referenced property is Myproperty. Properties are case sensitive, so the two properties are NOT the same. This is a common cause of errors.                          |



 

[Property Table](property-table.md)



| Property      | Value   |
|---------------|---------|
| ReinstallMode | omus    |
| MyProperty    | a value |



 

[InstallExecuteSequence Table](installexecutesequence-table.md) (partial)



| Action          | Condition  |
|-----------------|------------|
| InstallFinalize | Myproperty |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



