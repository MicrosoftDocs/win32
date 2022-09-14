---
description: The SetODBCFolders action checks for existing ODBC drivers on the system and sets the target directory of each new driver to the location of an existing driver.
ms.assetid: d1739b37-d89b-400e-a4ac-b417e0fb9918
title: SetODBCFolders Action
ms.topic: article
ms.date: 05/31/2018
---

# SetODBCFolders Action

The SetODBCFolders action checks for existing ODBC drivers on the system and sets the target directory of each new driver to the location of an existing driver.

## Sequence Restrictions

The SetODBCFolders action must come after the [CostFinalize action](costfinalize-action.md) and before the [InstallValidate action](installvalidate-action.md).

## ActionData Messages



| Field | Description of action data                                                          |
|-------|-------------------------------------------------------------------------------------|
| \[1\] | Driver description. The ODBC driver key.                                            |
| \[2\] | Original folder location of the new driver.                                         |
| \[3\] | New folder location for the new driver. This is the location of an existing driver. |



 

## Remarks

This action places a new driver into the same directory as the existing driver being replaced. The SetODBCFolders action uses the [Directory table](directory-table.md) to set the locations of existing drivers that are to be replaced.

 

 



