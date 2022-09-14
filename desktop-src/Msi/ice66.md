---
description: ICE66 uses the tables in the database to determine which schema your database should use.
ms.assetid: 7cf929a0-2c4c-40ca-a902-dfd9dcd203b8
title: ICE66
ms.topic: article
ms.date: 05/31/2018
---

# ICE66

ICE66 uses the tables in the database to determine which schema your database should use.

Some functionality may only be available if the package is installed on a system with a current Windows Installer version.

## Result

ICE66 posts a warning if your database is using the wrong schema.

## Example

ICE66 reports the following warning for the example shown.

``` syntax
WARNING: Complete functionality of the IsolatedComponents table is only available with Windows Installer versions 1.1 or greater. Your schema is 100.
```

This warning can be ignored if you want your package to be installed using a current Windows Installer version. For example, if you want your package to be installable only on version 2.0 or later, change your package schema (PID\_PAGECOUNT) to 200.

[IsolatedComponent Table](isolatedcomponent-table.md)



| Component\_Shared | Component\_Application |
|-------------------|------------------------|
| Component1        | Component2             |



 

[Summary Information Stream](summary-information-stream.md)



| PIDt           | Value |
|----------------|-------|
| PID\_PAGECOUNT | 100   |



 

## Table used during execution:

[\_Columns table](-columns-table.md)

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



