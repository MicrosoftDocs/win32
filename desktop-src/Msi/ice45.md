---
description: ICE45 validates that bit field columns in the database do not set any reserved bits to 1.
ms.assetid: 43fa5e9c-2059-4217-8f8e-c194e37f238a
title: ICE45
ms.topic: article
ms.date: 05/31/2018
---

# ICE45

ICE45 validates that bit field columns in the database do not set any reserved bits to 1.

Reserved bits provide no functionality in current versions of the installer, but might in future versions. They should be set to 0 to be compatible with future versions of Windows Installer.

## Result

ICE45 posts an error message if any of the following tables contains a bit field with a reserved bit set to a value of 1.

-   [BBControl table](bbcontrol-table.md)
-   [Dialog table](dialog-table.md)
-   [Feature table](feature-table.md)
-   [File table](file-table.md)
-   [MoveFile table](movefile-table.md)
-   [ModuleConfiguration table](moduleconfiguration-table.md)
-   [ODBCDataSource table](odbcdatasource-table.md)
-   [Patch table](patch-table.md)
-   [RemoveFile table](removefile-table.md)
-   [ServiceControl table](servicecontrol-table.md)
-   [ServiceInstall table](serviceinstall-table.md)
-   [TextStyle table](textstyle-table.md)

ICE45 posts one of two warning messages if the [Control Table](control-table.md) contains a bit field with a reserved bit set to a value of 1.

## Example

ICE45 reports the following error for the example shown.

``` syntax
Row 'File1' in table 'File' has bits set in the 'Attributes' 
    column that are reserved. They must be 0 to ensure 
    compatibility with future installer versions.
```

ICE45 reports the following warning for the example shown.

``` syntax
Row 'Dialog1.Edit2' in table 'Control' has bits set in the 'Attribute' 
    column that are reserved. They should be 0 to ensure compatibility 
    with future installer versions.
```

[File Table](file-table.md) (partial)



| File  | Attributes |
|-------|------------|
| File1 | 128        |



 

[Control Table](control-table.md) (partial)



| Dialog  | Control | Attributes |
|---------|---------|------------|
| Dialog1 | Edit1   | 2097152    |
| Dialog1 | Edit2   | 1048576    |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



