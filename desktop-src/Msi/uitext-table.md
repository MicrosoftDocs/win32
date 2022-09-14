---
description: The UIText table contains the localized versions of some of the strings used in the user interface. These strings are not part of any other table. The UIText table is for strings that have no logical place in any other table.
ms.assetid: 2965e3a8-2cbf-4445-963b-ec2040692106
title: UIText Table
ms.topic: article
ms.date: 05/31/2018
---

# UIText Table

The UIText table contains the localized versions of some of the strings used in the user interface. These strings are not part of any other table. The UIText table is for strings that have no logical place in any other table.

The UIText table has the following columns.



| Column | Type                         | Key | Nullable |
|--------|------------------------------|-----|----------|
| Key    | [Identifier](identifier.md) | Y   | N        |
| Text   | [Text](text.md)             | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>Key
</dt> <dd>

A unique key that identifies the particular string.

</dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>Text
</dt> <dd>

The localized version of the string.

</dd> </dl>

## Remarks

Some controls use the UIText table as a source of strings. For information about which strings are required in this table for each particular control, see the individual controls in the [User Interface Reference](user-interface-reference.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
</dl>

 

 



