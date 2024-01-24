---
description: The MsiPatchHeaders table holds the binary patch header streams used for patch validation.
ms.assetid: aefdd365-1681-43e4-8470-04a5d6efd993
title: MsiPatchHeaders Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiPatchHeaders Table

The MsiPatchHeaders table holds the binary patch header streams used for patch validation.

The MsiPatchHeaders table is used when long [File table](file-table.md) keys result in a failure to generate the patch header stream in the [Patch table](patch-table.md). This can be due to the stream name limitation described in [OLE Limitations on Streams](ole-limitations-on-streams.md). In this case, the Patch table can reference the MsiPatchHeaders table to create the patch header stream.

The MsiPatchHeaders table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| StreamRef | [Identifier](identifier.md) | Y   | N        |
| Header    | [Binary](binary.md)         | N   | N        |



 

## Columns

<dl> <dt>

<span id="StreamRef"></span><span id="streamref"></span><span id="STREAMREF"></span>StreamRef
</dt> <dd>

The primary key for the table that uniquely identifies a particular patch header.

</dd> <dt>

<span id="Header"></span><span id="header"></span><span id="HEADER"></span>Header
</dt> <dd>

This column is the binary stream patch header used for patch validation.

</dd> </dl>

## Remarks

This table is processed by the [PatchFiles action](patchfiles-action.md). This table is usually added to the install package by a transform from a patch package. It is usually not authored directly into an installation package.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE29](ice29.md)  
</dl>

 

 



