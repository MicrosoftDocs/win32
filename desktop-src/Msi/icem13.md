---
description: ICEM13 verifies that the merge module does not contain publisher policy and configuration assemblies.
ms.assetid: 1281ee21-a154-4275-a9e6-6e92fff548ed
title: ICEM13
ms.topic: article
ms.date: 05/31/2018
---

# ICEM13

ICEM13 verifies that the merge module does not contain publisher policy and configuration assemblies. Publisher policy and configuration assemblies should not be included in merge modules intended for redistribution because this can affect other applications on a user's computer.

This ICEM is available in the Mergemod.cub file provided in the Windows Installer 2.0 SDK and later. For details, see [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Result

ICEM13 posts a warning message if it finds a component specified in the Component field of the merge module's [MsiAssembly Table](msiassembly-table.md) that is a publisher policy or configuration assembly.

## Example

ICEM13 posts the following warning message if it finds a row in the [MsiAssembly Table](msiassembly-table.md) with a component '\[1\]' specified in the Component field that is a publisher policy or configuration assembly that has been included in the merge module.

``` syntax
This entry Component_=`[1]` in MsiAssembly Table is a Policy/Configuration Assembly. A Publisher Policy/Configuration assembly should not be redistributed with a merge module. Policy/Configuration may impact other applications and should only be installed with products.
```

It is possible to install publisher policy and configuration assemblies using the Windows Installer, it is not recommended that these assemblies be redistributed in merge modules.

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



