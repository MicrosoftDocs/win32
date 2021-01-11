---
description: The ProcessComponents action registers and unregisters components, their key paths, and the component clients.
ms.assetid: 8ad418c0-9bba-41d0-a96c-2c7b1c2467d9
title: ProcessComponents Action
ms.topic: article
ms.date: 05/31/2018
---

# ProcessComponents Action

The ProcessComponents action registers and unregisters components, their key paths, and the component clients. The ProcessComponents action queries the KeyPath column of the [Component table](component-table.md) to determine keypaths. This registration is used by [**MsiGetComponentPath**](/windows/desktop/api/Msi/nf-msi-msigetcomponentpatha) to return the path of a component for a product client.

## Sequence Restrictions

The ProcessComponents action must come after the [InstallInitialize](installinitialize-action.md) action.

## ActionData Messages

For each component being registered.



| Field | Description of action data      |
|-------|---------------------------------|
| \[1\] | ProductId                       |
| \[2\] | ComponentId                     |
| \[3\] | The key path for the component. |



 

For each component being unregistered.



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | ProductId                  |
| \[2\] | ComponentId                |



 

 

 



