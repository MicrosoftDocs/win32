---
description: The Property table contains the property names and values for all defined properties in the installation. Properties with Null values are not present in the table.
ms.assetid: '1f4215b2-dc71-4e6e-bc2e-3b43316806b9'
title: Property Table
ms.topic: article
ms.date: 05/31/2018
---

# Property Table

The Property table contains the property names and values for all defined properties in the installation. Properties with Null values are not present in the table.

The Property table has the following columns.



| Column   | Type                         | Key | Nullable |
|----------|------------------------------|-----|----------|
| Property | [Identifier](identifier.md) | Y   | N        |
| Value    | [Text](text.md)             | N   | N        |



 

## Columns

<dl> <dt>

<span id="Property"></span><span id="property"></span><span id="PROPERTY"></span>Property
</dt> <dd>

The name of a property. See [Properties](properties.md).

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

A localizable string value for the property. This may never be Null or an empty string.

</dd> </dl>

## Remarks

Note that you cannot use the Property table to set a property to the value of another property. The installer does nothing to the text string entered in the Value column before setting the property in the Property column. If FirstProperty is entered into the Property column and \[SecondProperty\] in the Value column, the value of FirstProperty is set to the text string "\[SecondProperty\]" and not to the value of the SecondProperty property. This is necessary to prevent creating circular references in the Property table. Instead, you can set one property to another by using a [Custom Action Type 51](custom-action-type-51.md).

Note that the [**AdminProperties**](adminproperties.md) property can be used to override the values in the Property table during an [Administrative Installation](administrative-installation.md).

Do not use properties for passwords or other information that must remain secure. The installer may write the value of a property authored into the Property table, or created at runtime, into a log or the system registry.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE05](ice05.md)  
[ICE06](ice06.md)  
[ICE16](ice16.md)  
[ICE24](ice24.md)  
[ICE31](ice31.md)  
[ICE34](ice34.md)  
[ICE36](ice36.md)  
[ICE40](ice40.md)  
[ICE46](ice46.md)  
[ICE48](ice48.md)  
[ICE52](ice52.md)  
[ICE61](ice61.md)  
[ICE73](ice73.md)  
[ICE74](ice74.md)  
[ICE80](ice80.md)  
[ICE87](ice87.md)  
[ICE88](ice88.md)  
[ICE91](ice91.md)  
[ICE99](ice99.md)  
</dl>

 

 



