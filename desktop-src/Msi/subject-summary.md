---
description: The value of the Subject Summary property conveys the name of the product, transform, or patch that is installed by the package.
ms.assetid: fb08a240-db30-477f-8dc0-701156d73cfc
title: Subject Summary property
ms.topic: reference
ms.date: 05/31/2018
---

# Subject Summary property

The value of the **Subject Summary** property conveys the name of the product, transform, or patch that is installed by the package.

It is up to the author of an installation database, transform, or patch package to provide the value of this property in the summary information. Authors should do the following to determine the correct value.

-   Set the **Subject Summary** property in an installation package to the same value as the [**ProductName**](productname.md) property.
-   Set the **Subject Summary** property in a transform to the same value as the **Subject Summary** property in the original installation package.
-   Set the **Subject Summary** property in the summary information of a patch package to a short description of the patch that includes the name of the product.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |



## See also

<dl> <dt>

[**PATCHNEWSUMMARYSUBJECT**](patchnewsummarysubject.md)
</dt> <dt>

[Summary Property Descriptions](summary-property-descriptions.md)
</dt> </dl>

 

 




