---
title: Item Monikers
description: Another OLE-implemented moniker class is the item moniker, which can be used to identify an object contained in another object.
ms.assetid: ddcf3669-4ad0-4a4e-80a6-eb78058cff09
ms.topic: article
ms.date: 05/31/2018
---

# Item Monikers

Another OLE-implemented moniker class is the *item moniker*, which can be used to identify an object contained in another object. One type of contained object is an OLE object embedded in a compound document. A compound document could identify the embedded objects it contains by assigning each one an arbitrary name, such as "embedobj1," "embedobj2," and so forth. Another type of contained object is a user selection in a document, such as a range of cells in a spreadsheet or a range of characters in a text document. An object that consists of a selection is called a *pseudo-object* because it isn't treated as a distinct object until a user marks the selection. A spreadsheet might identify a cell range using a name such as "1A:7F," while a word processing document might identify a range of characters using the name of a bookmark.

An item moniker is useful primarily when concatenated, or *composed*, with another moniker, one that identifies the container. An item moniker is usually created and then composed onto (for example) a file moniker to create the equivalent of a complete path to the object. For example, you can compose the file moniker "c:\\work\\report.doc" (which identifies the container object) with the item moniker "embedobj1" (which identifies an object within the container) to form the moniker "c:\\work\\report.doc\\embedobj1," which uniquely identifies a particular object within a particular file. You can also concatenate additional item monikers to identify deeply nested objects. For example, if "embedobj1" is the name of a spreadsheet object, to identify a certain range of cells in that spreadsheet object you could append another item moniker to create a moniker that would be the equivalent of "c:\\work\\report.doc\\embedobj1\\1A:7F."

When combined with a file moniker, an item moniker forms a complete path. Item monikers thus extend the notion of path names beyond the file system, defining path names to identify individual objects, not just files.

There is a significant difference between an item moniker and a file moniker. The path contained in a file moniker is meaningful to anyone who understands the file system, while the partial path contained in an item moniker is meaningful only to a particular container. Everyone knows what "c:\\work\\report.doc" refers to, but only one particular container object knows what "1A:7F" refers to. One container cannot interpret an item moniker created by another application; the only container that knows which object is referred to by an item moniker is the container that assigned the item moniker to the object in the first place. For this reason, the source of the object named by the combination of a file and item moniker must not only implement [**IPersistFile**](/windows/desktop/api/ObjIdl/nn-objidl-ipersistfile), to facilitate binding the file moniker, but also [**IOleItemContainer**](/windows/desktop/api/OleIdl/nn-oleidl-ioleitemcontainer) to facilitate resolving the name of the item moniker into the appropriate object, in the context of a file.

The advantage of monikers is that someone using a moniker to locate an object doesn't need to understand the name contained within the item moniker, as long as the item moniker is part of a composite. Generally, it would not make sense for an item moniker to exist on its own. Instead, you would compose an item moniker onto a file moniker. You would then call [**IMoniker::BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject) on the composite, which binds the individual monikers within it, interpreting the names.

To create an item moniker object and return its pointer to the moniker provider, OLE provides the helper function [**CreateItemMoniker**](/windows/desktop/api/Objbase/nf-objbase-createitemmoniker). This function creates an item moniker object and returns its pointer to the provider.

## Related topics

<dl> <dt>

[Anti-Monikers](anti-monikers.md)
</dt> <dt>

[Class Monikers](class-monikers.md)
</dt> <dt>

[Composite Monikers](composite-monikers.md)
</dt> <dt>

[File Monikers](file-monikers.md)
</dt> <dt>

[Pointer Monikers](pointer-monikers.md)
</dt> </dl>

 

 




