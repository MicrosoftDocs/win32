---
title: About Creating Information Types
description: About Creating Information Types
ms.assetid: BCA23A9B-3163-4fbd-898B-990CF1565167
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Creating Information Types

Information types enable you to specify that certain groups of help topics reach certain users. Use the following steps when creating information types.

First, define information types based on your intended audience. For example, to create the help files for this version of HTML Help Workshop we defined these information types: Reference, Design, Overview, Procedure, and Web. The Reference type was assigned to Reference topics, the Design type to topics about designing a help system, etc.

Second, assign either an **Inclusive**, **Exclusive**, or **Hidden** attribute to each information type. When the attribute is Inclusive, the user is allowed to select from one or more Inclusive information types within each category. When the attribute is Exclusive, the user can select only one information type from each category. When the attribute is [Hidden](about-the-hidden-information-type.md), the topic can only be invoked through the HTML Help API and be associated with events in the software program.

For example, a help author creates Novice, Intermediate, and Advanced information types that have the Inclusive attribute. A user will be given the choice to view all Novice, Intermediate, and Advanced topics. If the Novice, Intermediate, and Advanced information types have the Exclusive attribute, a user will only be able to select topics from one of the three types.

### Notes

-   If a topic has no information type associated with it, it will always appear.
-   Categories are optional, if you use them, you must assign all information types to a category.
-   Topics with the Hidden information type will not appear when a user makes their selections.
-   If used with a set of merged compiled help (.chm) files, information types should be standardized in all the files in the collection.
-   Information types are not supported when using a [binary table of contents](about-binary-contents-files.md).

## Related topics

<dl> <dt>

[Create Information Types](creating-information-types.md)
</dt> </dl>

 

 




