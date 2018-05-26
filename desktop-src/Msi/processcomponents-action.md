---
Description: The ProcessComponents action registers and unregisters components, their key paths, and the component clients.
ms.assetid: 8ad418c0-9bba-41d0-a96c-2c7b1c2467d9
title: ProcessComponents Action
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ProcessComponents Action

The ProcessComponents action registers and unregisters components, their key paths, and the component clients. The ProcessComponents action queries the KeyPath column of the [Component table](component-table.md) to determine keypaths. This registration is used by [**MsiGetComponentPath**](/windows/win32/Msi/nf-msi-msigetcomponentpatha?branch=master) to return the path of a component for a product client.

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



 

 

 



