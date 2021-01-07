---
description: The InstallSFPCatalogFile action installs the catalogs used by Windows Me for Windows File Protection.
ms.assetid: 1c8253f1-ac7d-4346-a16e-887d16f521d9
title: InstallSFPCatalogFile Action
ms.topic: article
ms.date: 05/31/2018
---

# InstallSFPCatalogFile Action

The InstallSFPCatalogFile action installs the catalogs used by Windows Me for Windows File Protection. InstallSFPCatalogFile queries the [Component table](component-table.md), [File table](file-table.md), [FileSFPCatalog table](filesfpcatalog-table.md) and [SFPCatalog table](sfpcatalog-table.md). Catalogs are installed if they are associated with a file in a component that is set for local installation or if they are associated with a file being repaired in a locally installed component.

## Sequence Restrictions

The InstallSFPCatalogFile action must be sequenced before [InstallFiles](installfiles-action.md) and after [CostFinalize](costfinalize-action.md).

## ActionData Messages



| Field | Description of action data                                    |
|-------|---------------------------------------------------------------|
| \[1\] | Name of the catalog being installed.                          |
| \[2\] | Name of the catalog this catalog's installation depends upon. |



 

## Remarks

A catalog that is dependent on another catalog installed after the parent catalog.

 

 



