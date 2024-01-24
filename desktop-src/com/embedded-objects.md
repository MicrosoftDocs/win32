---
title: Embedded Objects (COM)
description: Embedded Objects
ms.assetid: 1f863fd4-fead-4dd3-b855-8820e015b52a
ms.topic: article
ms.date: 05/31/2018
---

# Embedded Objects (COM)

An embedded object is physically stored in the compound document, along with all the information needed to manage the object. In other words, the embedded object is actually a part of the compound document in which it resides. This arrangement has a couple of disadvantages. First, a compound document containing embedded objects will be larger than one containing the same objects as links. Second, changes made to the source of an embedded object will not be automatically replicated in the embedded copy, and changes in the embedded copy will not be reflected in the source, as they are with a link.

Still, for certain purposes, embedding offers several advantages over links. First, users can transfer compound documents with embedded objects to other computers, or other locations on the same computer, without breaking a link. Second, users can edit embedded objects without changing the content of the original. Sometimes, this separation is precisely what is required. Third, embedded objects can be activated in place, meaning that the user can edit or otherwise manipulate the object without having to work in a separate window from that of the object's container. Instead, when the object is activated, the container application's user interface changes to expose those tools that are necessary to manage or modify the object.

## Related topics

<dl> <dt>

[Creating Linked and Embedded Objects from Existing Data](creating-linked-and-embedded-objects-from-existing-data.md)
</dt> </dl>

 

 




