---
description: To generate a merge module, you need to obtain a software tool with which to edit an .msm file.
ms.assetid: bc14d36a-b299-4c61-ade2-43fad142d21d
title: Obtaining Merge Module Authoring Tools
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Merge Module Authoring Tools

To generate a merge module, you need to obtain a software tool with which to edit an .msm file. Because an .msm file is basically a simplified .msi file, you may be able to use the same tools used to create an installation database. For example, the application Orca.exe provided with the Windows Installer SDK.

An alternative is to purchase one of the installer packaging tools to be available from independent software vendors. There are several third-party tools under development that may be used for producing merge modules. If you choose to use a third-party tool you should verify that it generates merge modules that are consistent with the standard described in this document. In particular, you should determine that the editing tools have not done any of the following to the merge module.

-   Added extraneous tables to the merge module that are not referenced in the [ModuleIgnoreTable table](moduleignoretable-table.md).

    Delete these tables or add them to the ModuleIgnoreTable table.

-   Added an unnecessary [TextStyle table](textstyle-table.md) to the merge module.

    If your merge module has no UI (and it generally should not) you can safely delete this table.

-   Added unnecessary entries to the [Directory table](directory-table.md).

    Remove unnecessary entries from the Directory table.

-   Left information out of the merge module's \_Validation table.

    This prevents merge module validation. Add a complete \_Validation table.

## Related topics

<dl> <dt>

[Authoring User Interfaces in Merge Modules](authoring-user-interfaces-in-merge-modules.md)
</dt> <dt>

[Authoring Merge Module Directory Tables](authoring-merge-module-directory-tables.md)
</dt> <dt>

[Validating Merge Modules](validating-merge-modules.md)
</dt> </dl>

 

 



