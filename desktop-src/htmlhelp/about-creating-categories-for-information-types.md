---
title: About Creating Categories for Information Types
description: About Creating Categories for Information Types
ms.assetid: FA4204E8-C3EA-4ac9-B89B-CADFF2A98CEB
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Creating Categories for Information Types

It is not required that you create categories for information types. If you use them, any information types you create must be assigned to a category. Be sure to plan ahead because they are difficult to remove once you add them to a help project. Follow these steps when creating categories:

First, determine and name categories that best describe and group the information types you need. For example, you might create two categories for grouping topics: Job Description and Experience Level.

Next, define information types for grouping topics in those categories based on your intended audience. For example, for the category Job Description, you might define three information types: Manager, Salesperson, and Engineer. For the category Experience Level, you might also define three information types: Novice, Intermediate, and Advanced.

Third, assign either an **Inclusive** or **Exclusive** attribute to each information type. When the attribute is Inclusive, the user is allowed to select from one or more Inclusive information types within each category. When the attribute is Exclusive, the user can select only one information type from each category.

For example, if the Novice, Intermediate, and Advanced information types have the Inclusive attribute, a user will be given the choice to view all Novice, Intermediate, and Advanced topics. If the Novice, Intermediate, and Advanced information types have the Exclusive attribute, a user will only be able to select topics from one of the three.

### Notes

-   If a topic has no information type associated with it, it will always appear.
-   You can assign more than one information type to a topic.
-   You can only assign information types to a table of contents entry.
-   If used with a [large collection](manage-large-document-sets.md) of merged compiled help (.chm) files, categories should be standardized for all the files in the collection.

## Related topics

<dl> <dt>

[Create Categories for Information Types](creating-categories-for-information-types.md)
</dt> </dl>

 

 




