---
title: Form of Command Tree
description: Form of Command Tree
ms.assetid: 1c0bafa8-667e-4be1-ae3d-ed5bd56c6502
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Form of Command Tree

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A command tree is made up of zero or more command-tree nodes. A command-tree node is a [**DBCOMMANDTREE**](dbcommandtree.md) structure with the following members.

<dl> <dt>

<span id="op"></span><span id="OP"></span>**op**
</dt> <dd>

An operator from [Data Manipulation Operators](data-manipulation-operators.md) that defines the operation that will take on the associated field.

</dd> <dt>

<span id="wKind"></span><span id="wkind"></span><span id="WKIND"></span>**wKind**
</dt> <dd>

A value that defines the data type of the associated field, a member of [**DBVALUEKIND**](dbvaluekind.md). This type tags the value so that the command processor knows how to interpret it.

</dd> <dt>

<span id="pctFirstChild"></span><span id="pctfirstchild"></span><span id="PCTFIRSTCHILD"></span>**pctFirstChild**
</dt> <dd>

A link to the first child of this node.

</dd> <dt>

<span id="pctNextSibling"></span><span id="pctnextsibling"></span><span id="PCTNEXTSIBLING"></span>**pctNextSibling**
</dt> <dd>

A link to the next sibling of this node.

</dd> <dt>

<span id="value"></span><span id="VALUE"></span>**value**
</dt> <dd>

A union to hold the value for every data type supported by this OLE DB provider. For any union member that holds 8 bytes or less, the value itself is stored here. Otherwise, **value** is a **pwszValue** member, a pointer to the data.

</dd> </dl>

-   For a list of the types of nodes that can exist, see [Catalog of DML Nodes](catalog-of-dml-nodes.md).

 

 




