---
description: ICE02 validates that certain references between the Component, File, and Registry tables are reciprocal. These references must to be reciprocal for the installer to correctly determine the installation state of components.
ms.assetid: 864404f1-439d-49a2-973d-4e6e1618863e
title: ICE02
ms.topic: article
ms.date: 05/31/2018
---

# ICE02

ICE02 validates that certain references between the [Component](component-table.md), [File](file-table.md), and [Registry](registry-table.md) tables are reciprocal. These references must to be reciprocal for the installer to correctly determine the installation state of components.

The installer uses the KeyPath column of the Component table to detect the presence of the component listed in the Component column. The KeyPath column contains a key into the Registry or File tables. Both of these tables have a Component\_ column that contains a key back into the Component table pointing to the component that controls the registry entry or file. These references must be reciprocal.

## Result

ICE02 posts an error message if it finds a reference that should be reciprocal and is not.

## Example

ICE02 would post the following error message for a .msi file containing the database entries shown.

``` syntax
File: 'Red_File' cannot be the key file for Component: 'Blue'. The file belongs to Component: 'Red'
```

[Component Table](component-table.md) (partial)



| Component | KeyPath   |
|-----------|-----------|
| Red       | Red\_File |
| Blue      | Red\_File |



 

[File Table](file-table.md) (partial)



| File Column | Component\_ |
|-------------|-------------|
| Red\_File   | Red         |
| Blue\_File  | Blue        |



 

Component Blue references Red\_File, but Red\_File is not controlled by Component Blue and therefore cannot be the KeyPath file. If the installer were called to get the installation state of Blue it would incorrectly check whether Red\_File was installed. Changing the KeyPath field for Blue in the Component Table to Blue\_File fixes the error.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



