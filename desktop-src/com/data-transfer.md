---
title: Data Transfer
description: Data Transfer
ms.assetid: 26b16438-f940-4086-869e-74021ed00b1e
ms.topic: article
ms.date: 05/31/2018
---

# Data Transfer

The Component Object Model (COM) provides a standard mechanism for transferring data between applications. This mechanism is the *data object*, which is simply any COM object that implements the [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) interface. Some data objects, such as a piece of text copied to the clipboard, have **IDataObject** as their sole interface. Others, such as compound document objects, expose several interfaces, of which **IDataObject** is simply one. Data objects are fundamental to the working of compound documents, although they also have widespread application outside that OLE technology.

By exchanging pointers to a data object, providers and consumers of data can manage data transfers in a uniform manner, regardless of the format of the data, the type of medium used to transfer the data, or the target device on which it is to be rendered. You can include support in your application for basic clipboard transfers, drag and drop transfers, and OLE compound document transfers with a single implementation of [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject). Having done that, the amount of code required to accommodate the special semantics of each protocol is minimal.

For more information, see the following topics:

-   [Data Transfer Interfaces](data-transfer-interfaces.md)
-   [Data Formats and Transfer Media](data-formats-and-transfer-media.md)
-   [Drag and Drop](drag-and-drop.md)

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> </dl>

 

 




