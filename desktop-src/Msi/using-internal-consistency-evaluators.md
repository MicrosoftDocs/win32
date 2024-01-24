---
description: To validate a database, use a special validation tool to merge a .cub file containing the Internal Consistency Evaluators (ICEs) into your database, execute the ICEs, and report the results.
ms.assetid: bdf38673-ee3d-47d8-ad6e-562cd5626918
title: Using Internal Consistency Evaluators
ms.topic: article
ms.date: 05/31/2018
---

# Using Internal Consistency Evaluators

To validate a database, use a special validation tool to merge a .cub file containing the [Internal Consistency Evaluators](internal-consistency-evaluators-ices.md) (ICEs) into your database, execute the ICEs, and report the results. Several such tools are provided in the Microsoft Windows Software Development Kit (SDK). Authoring environments from third-party vendors also may incorporate the ICE validation system into their authoring environment. It is also possible to write your own tool to perform ICE validation. Most ICE validation tools merge the .cub file and your database into a third, temporary database. Windows Installer displays warnings, errors, debugging information, and API errors as it executes each ICE in the .cub file. When the installer finishes executing the ICEs it closes the .msi file, .cub file, and temporary database without saving any changes. The .msi file and .cub file remain unchanged by the validation test.

ICE custom actions communicate to the user by calling [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) and posting an INSTALLMESSAGE\_USER message. An ICE message commonly returns information such as the following:

-   Name of the ICE that has found an error
-   Date the ICE was created
-   Author of the ICE
-   Date the ICE was last modified.
-   Description of the API error causing the ICE to fail
-   Description of the error
-   A warning to the user
-   Name of the database table containing the error or warning
-   Name of the table column containing the error or warning
-   Primary keys of the table containing the error or warning
-   A URL to a HTML file giving debugging suggestions
-   A string that can contain other information

Authors of installation packages can write ICE custom actions or use the standard set of ICEs included in the .cub files provided with the SDK. For more information on how to write an ICE, see [Building an ICE](building-an-ice.md).

After writing the appropriate ICEs for validation, a developer must collect the custom actions together into an .msi database, called a .cub file, that contains only the ICEs and their required tables. A .cub file cannot be installed and is used only to store and provide access to ICE custom actions. For more information on making .cub files, see [Building an ICE Database](building-an-ice-database.md). Alternatively, developers can validate their installation package using the existing ICEs described in [ICE Reference](ice-reference.md). These ICEs can be obtained from standard .cub files provided with the SDK.

The installation of the database table editor Orca or the validation tool msival2 provides the Logo.cub, Darice.cub, and Mergemod.cub files. The set of ICEs in the Logo.cub file is a subset of those in the Darice.cub file. If your package passes validation using Darice.cub, it will pass with Logo.cub. Mergemod.cub contains a set of ICEs used to validate merge modules. For more information, see [Merge Module ICE Reference](merge-module-ice-reference.md).

**To validate an installation package**

1.  Obtain or author the appropriate ICE custom actions. You may be able to use one or more of the existing ICEs described in the [ICE Reference](ice-reference.md). If your validation requires an ICE not yet in this list, you can create a new ICE as described in [Building an ICE](building-an-ice.md).
2.  Prepare an ICE Database containing all the ICE custom actions. See the section [Building An ICE Database](building-an-ice-database.md) for information about preparing a .cub file.
3.  Provide the .cub file and the .msi file to a package validation tool such as [Orca.exe](orca-exe.md) or [Msival2.exe](msival2-exe.md).

Note that merge modules should be validated as described in [Validating Merge Modules](validating-merge-modules.md).

 

 



