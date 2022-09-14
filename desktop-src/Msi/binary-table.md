---
description: The Binary table holds the binary data for items such as bitmaps, animations, and icons. The binary table is also used to store data for custom actions. See OLE Limitations on Streams.
ms.assetid: 44c56407-df2e-4cbe-b7a3-b22e8d97eb03
title: Binary Table
ms.topic: article
ms.date: 05/31/2018
---

# Binary Table

The Binary table holds the binary data for items such as bitmaps, animations, and icons. The binary table is also used to store data for custom actions. See [OLE Limitations on Streams](ole-limitations-on-streams.md).

The Binary table has the following columns.



| Column | Type                         | Key | Nullable |
|--------|------------------------------|-----|----------|
| Name   | [Identifier](identifier.md) | Y   | N        |
| Data   | [Binary](binary.md)         | N   | N        |



 

## Columns

<dl> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

A unique key that identifies the particular binary data. If the binary data is for a control, the key appears in the Text column of the associated control in the [Control table](control-table.md). This key must be unique among all controls requiring binary data.

</dd> <dt>

<span id="Data"></span><span id="data"></span><span id="DATA"></span>Data
</dt> <dd>

The unformatted binary data.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE17](ice17.md)  
[ICE29](ice29.md)  
</dl>

 

 



