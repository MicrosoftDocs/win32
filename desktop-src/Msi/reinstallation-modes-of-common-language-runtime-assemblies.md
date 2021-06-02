---
description: Common language runtime assemblies that are installed to the global assembly cache must have identical files in all occurrences of the assembly.
ms.assetid: 02b4ad60-d28d-44b8-955f-b367197e69c3
title: Reinstallation Modes of Common Language Runtime Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Reinstallation Modes of Common Language Runtime Assemblies

Common language runtime assemblies that are installed to the global assembly cache must have identical files in all occurrences of the assembly. This means that the reinstallation modes used by [**MsiReinstallFeature**](/windows/desktop/api/Msi/nf-msi-msireinstallfeaturea) and [**MsiReinstallProduct**](/windows/desktop/api/Msi/nf-msi-msireinstallproducta) must have different meanings for regular components and common language runtime assemblies. The following definitions of reinstall modes apply to common language runtime assemblies.



| Reinstall mode                  | Meaning for Microsoft .NET Components                                                                                              |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| REINSTALLMODE\_FILEMISSING      | Install or reinstall the common language runtime component if it is missing or incomplete.                                         |
| REINSTALLMODE\_FILEOLDERVERSION | Install or reinstall the common language runtime component if it is missing or incomplete.                                         |
| REINSTALLMODE\_FILEEQUALVERSION | Install or reinstall the common language runtime component if it is missing or incomplete.                                         |
| REINSTALLMODE\_FILEEXACT        | Install or reinstall the common language runtime component if it is missing or incomplete.                                         |
| REINSTALLMODE\_FILEVERIFY       | Install or reinstall the common language runtime component if it is missing or if the existing component is incomplete or corrupt. |
| REINSTALLMODE\_FILEREPLACE      | Always install or reinstall the common language runtime component.                                                                 |



 

 

 



