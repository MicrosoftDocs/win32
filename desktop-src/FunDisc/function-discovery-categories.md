---
Description: Categories are the namespaces in which components that provide similar base functionality are grouped.
ms.assetid: 476df2f0-6ed0-4275-90e7-752d7279bf1b
title: Function Discovery Categories
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Function Discovery Categories

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

*Categories* are the namespaces in which components that provide similar base functionality are grouped.

Client programs use the category namespaces in queries to retrieve function instances representing the resources being discovered. A query in Function Discovery retrieves one of the following:

-   A collection of function instances in a specific category.
-   A single function instance that has a specific ID.

For more information, see [Function Discovery Queries](function-discovery-queries.md).

## Category Types

Function Discovery supports the following category types.



| Term                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="layered_categories"></span><span id="LAYERED_CATEGORIES"></span>layered categories<br/>    | Layered categories contain a collection of subcategories. The category name begins with the string "Layered\\".<br/>                                                                                                                                                                                                                                             |
| <span id="provider_categories"></span><span id="PROVIDER_CATEGORIES"></span>provider categories<br/> | Provider categories contain Function Discovery providers, and are used by the Function Discovery runtime to determine which discovery providers to load. The category name begins with the string "Provider\\". Client programs usually do not access or search on provider categories with the possible exception of system utility and test applications.<br/> |



 

## Related topics

<dl> <dt>

[Function Discovery Queries](function-discovery-queries.md)
</dt> <dt>

[Category Definitions](category-definitions.md)
</dt> <dt>

[Subcategory Definitions](subcategory-definitions.md)
</dt> </dl>

 

 




