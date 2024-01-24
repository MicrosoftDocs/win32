---
description: The following procedure describes the general steps to authoring merge modules.
ms.assetid: 4b3871c0-f452-4935-9ee3-78b0ac847e67
title: Authoring Merge Modules
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Merge Modules

The following procedure describes the general steps to authoring merge modules.

**To create a new merge module**

1.  Obtain a software tool you can use to edit the merge module database.
2.  Obtain a blank merge module database.
3.  Generate a [GUID](guid.md) for the merge module. You need to use this GUID when authoring the primary keys of database tables in the merge module.
4.  Add a record to the [Component table](component-table.md) for each component delivered by the merge. A Component table is required in every merge module. Note that merge modules operate with components and not with features. In certain cases, however, a database table entry may need to reference a feature. For details, see [Referencing Features in Merge Modules](referencing-features-in-merge-modules.md).
5.  Add a [Directory table](directory-table.md) to the merge module that specifies the layout of directories the merge module adds to the target database. A Directory table is required in every merge module.
6.  Import a blank [FeatureComponents table](featurecomponents-table.md) into the merge module database. This empty table provides a guideline for the merge tool in cases where the .msi file does not contain its own FeatureComponents table.
7.  Collect all the files delivered by this merge module and create the [MergeModule.CABinet](mergemodule-cabinet.md) cabinet file. Add the cabinet to the merge module as a stream inside the .msm file.
8.  Add a record to the File table for every file stored in MergeModule.CABinet.
9.  Add the information necessary to identify the merge module in the [ModuleSignature table](modulesignature-table.md). Every merge module requires a ModuleSignature table.
10. List the components in the merge module in the [ModuleComponents table](modulecomponents-table.md). Every merge module requires a ModuleComponents table.
11. Add merge module sequence tables to the .msm file only if the merge module needs to modify the [*sequence tables*](s-gly.md) of the target installation database.
12. Add a \_Validation table to the merge module. A merge module requires a \_Validation table to pass validation.
13. Merge modules require a user interface in only rare cases. Including a UI with a merge module is not recommended. In cases where a user interface is required, the UI tables can be merged into the .msi file the same as other tables.
14. Add registry information to the appropriate registry tables in the merge module database. Add registry information for type libraries, classes, extensions, and verbs into the [TypeLib](typelib-table.md), [Class](class-table.md), [AppId](appid-table.md), [ProgId](progid-table.md), [Extension](extension-table.md), [Verb](verb-table.md), or [MIME](mime-table.md) tables. All other registry information can go into the [Registry table](registry-table.md). The use of the SelfReg table is not recommended.
15. Add the summary information to the [Merge Module Summary Information Stream](merge-module-summary-information-stream-reference.md).
16. Run validation on all merge modules before attempting to install.

## Related topics

<dl> <dt>

[Obtaining Blank Merge Module Databases](obtaining-blank-merge-module-databases.md)
</dt> <dt>

[Obtaining Merge Module Authoring Tools](obtaining-merge-module-authoring-tools.md)
</dt> <dt>

[Naming Primary Keys in Merge Module Databases](naming-primary-keys-in-merge-module-databases.md)
</dt> <dt>

[Authoring Merge Module Component Tables](authoring-merge-module-component-tables.md)
</dt> <dt>

[Authoring Merge Module Directory Tables](authoring-merge-module-directory-tables.md)
</dt> <dt>

[Authoring Merge Module FeatureComponents Tables](authoring-merge-module-featurecomponents-tables.md)
</dt> <dt>

[Generating MergeModule.CABinet Cabinet Files](generating-mergemodule-cabinet-cabinet-files.md)
</dt> <dt>

[Authoring Merge Module File Tables](authoring-merge-module-file-tables.md)
</dt> <dt>

[Authoring ModuleSignature Tables](authoring-modulesignature-tables.md)
</dt> <dt>

[Authoring ModuleComponents Tables](authoring-modulecomponents-tables.md)
</dt> <dt>

[Authoring Merge Module Sequence Tables](authoring-merge-module-sequence-tables.md)
</dt> <dt>

[Validating Merge Modules](validating-merge-modules.md)
</dt> <dt>

[Authoring User Interfaces in Merge Modules](authoring-user-interfaces-in-merge-modules.md)
</dt> <dt>

[Authoring Merge Module Registry Tables](authoring-merge-module-registry-tables.md)
</dt> <dt>

[Authoring Merge Module Summary Information Streams](authoring-merge-module-summary-information-streams.md)
</dt> <dt>

[Merge Module Summary Information Stream Reference](merge-module-summary-information-stream-reference.md)
</dt> <dt>

Validating Merge Modules
</dt> <dt>

[Using 64-bit Merge Modules](using-64-bit-merge-modules.md)
</dt> </dl>

 

 



