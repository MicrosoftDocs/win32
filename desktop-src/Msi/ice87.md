---
description: ICE87 validates that the following properties have not been authored in the Property Table. These properties should instead be set on a command line.
ms.assetid: b769a01a-a610-474d-ada6-19b91441907c
title: ICE87
ms.topic: article
ms.date: 05/31/2018
---

# ICE87

ICE87 validates that the following properties have not been authored in the [Property Table](property-table.md). These properties should instead be set on a command line.

-   [**ADDLOCAL property**](addlocal.md)
-   [**REMOVE property**](remove.md)
-   [**ADDSOURCE property**](addsource.md)
-   [**ADDDEFAULT property**](adddefault.md)
-   [**REINSTALL property**](reinstall.md)
-   [**ADVERTISE property**](advertise.md)
-   [**COMPADDLOCAL property**](compaddlocal.md)
-   [**COMPADDSOURCE property**](compaddsource.md)
-   [**FILEADDLOCAL property**](fileaddlocal.md)
-   [**FILEADDSOURCE property**](fileaddsource.md)
-   [**FILEADDDEFAULT property**](fileadddefault.md)

## Result

ICE87 posts the following warning.



| ICE87 warning                                                                                                                        | Description                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| The property '\[1\]' shouldn't be authored into the Property table. Doing so might cause the product to not be uninstalled correctly | The specified property should not be set in the [Property table](property-table.md). Set the property on a command line instead. |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



