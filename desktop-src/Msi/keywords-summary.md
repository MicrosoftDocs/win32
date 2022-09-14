---
description: The Keywords Summary property in installation databases or transforms contains a list of keywords.
ms.assetid: e19dc495-e4d4-465f-8464-c60af8985334
title: Keywords Summary property
ms.topic: reference
ms.date: 05/31/2018
---

# Keywords Summary property

The **Keywords Summary** property in installation databases or transforms contains a list of keywords. The keywords may be used by file browsers to do keyword searches for a file. This property contains a list of sources of the patch in a patch package.

It is up to the author of an installation database, transform, or patch package to provide the value of this property in the summary information. Authors should do the following to determine the correct value.

-   In an installation package, set the value of this property to a list of keywords. The keyword should include "Installer" as well as product-specific keywords, and may be localized.
-   In a transform, set the value of this property to a list of keywords. The keyword should include "Installer" as well as product-specific keywords, and may be localized.
-   In a patch package, set the value of this property to a semicolon-delimited list of network or URL locations for the sources of the patch. When the patch is installed, the installer adds these to the source list for the patch package. If the cached patch becomes missing, the installer can search for a source in the original location, a location added to the source list by the **Keywords Summary** property, or a location added to the source list using the [**MsiSourceListAddSource**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourcea) or [**MsiSourceListAddSourceEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourceexa) functions.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |



## See also

<dl> <dt>

[Summary Property Descriptions](summary-property-descriptions.md)
</dt> </dl>

 

 




