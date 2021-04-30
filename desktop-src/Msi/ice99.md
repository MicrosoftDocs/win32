---
description: ICE99 verifies that no property name entered in the Directory table duplicates a name reserved for the public or private use of the Windows Installer.
ms.assetid: a7657c14-6542-4a7b-a8f7-727b109cfc39
title: ICE99
ms.topic: article
ms.date: 05/31/2018
---

# ICE99

ICE99 verifies that no property name entered in the [Directory](directory-table.md) table duplicates a name reserved for the public or private use of the Windows Installer.

## Result

ICE99 posts the following error.



| ICE99 error                                                                                                      | Description                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| The directory name: \[1\] is the same as one of the MSI Public Properties and can cause unforeseen side effects. | The value in the Directory column of the [Directory](directory-table.md) table duplicates a property name reserved by the Windows Installer. |



 

## Example

ICE99 reports the following error for the example:

``` syntax
CustomActionData is the same as one of the MSI Public Properties and can cause unforeseen side effects.
```

[Directory](directory-table.md) (partial)



| Directory        | Directory\_Parent | DefaultDir |
|------------------|-------------------|------------|
| CustomActionData |                   |            |



 

To correct this warning you should change the name of CustomActionData.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> <dt>

[Directory Table](directory-table.md)
</dt> <dt>

[Not Supported in Windows Installer 3.0 and earlier](not-supported-in-windows-installer-version-3-0.md)
</dt> </dl>

 

 



