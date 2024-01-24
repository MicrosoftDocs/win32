---
description: ICE76 verifies the use of the SFP (WFP) catalog within Windows Installer packages for Windows Me. This ICE also verifies that no files in the BindImage table reference SFP catalogs.
ms.assetid: e8b60b11-19ac-4ec4-aa36-a1f7a3ccd6f6
title: ICE76
ms.topic: article
ms.date: 05/31/2018
---

# ICE76

ICE76 verifies the use of the SFP (WFP) catalog within Windows Installer packages for Windows Me. This ICE also verifies that no files in the BindImage [table](bindimage-table.md) reference SFP catalogs.

Windows File Protection requires an exact match between the file and the signature embedded in the catalog file. Files that reference a SFP catalog must not be listed in the BindImage table because the effect of the [BindImage action](bindimage-action.md) on these files differs between computers. Files referenced by SFP catalogs must be in components that are permanent or installed locally.

## Result

ICE76 posts an error for each file in the [BindImage table](bindimage-table.md) that is also in the [FileSFPCatalog table](filesfpcatalog-table.md).

ICE76 outputs an error if a file in the FileSFPCatalog table belongs to a component with any of the following true:

-   **msidbComponentAttributesPermanent** is not set in the Attributes column of the [Component table](component-table.md).
-   **msidbComponentAttributesSourceOnly** is set in the Attributes column of the Component table.
-   **msidbAttributesOptional** is set in the Attributes column of the Component table.

## Example

ICE76 reports the following error for the example:

``` syntax
File 'File1' references a SFP catalog. Therefore it cannot be in the BindImage table.
```

[FileSFPCatalog Table](filesfpcatalog-table.md) (partial)



| File\_ | SFPCatalog\_ |
|--------|--------------|
| File1  | Catalog1.Cat |



 

[BindImage Table](bindimage-table.md) (partial)



| File\_ |
|--------|
| File1  |



 

To fix this do not enter any files that reference SFP catalogs into the BindImage table.

## Related topics

<dl> <dt>

[BindImage Table](bindimage-table.md)
</dt> <dt>

[Component Table](component-table.md)
</dt> <dt>

[FileSFPCatalog Table](filesfpcatalog-table.md)
</dt> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



