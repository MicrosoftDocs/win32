---
description: The UnpublishComponents action manages the unadvertisement of components listed in the PublishComponent table.
ms.assetid: 3e50f668-6d08-405e-a5a4-f422041ef0b1
title: UnpublishComponents Action
ms.topic: article
ms.date: 05/31/2018
---

# UnpublishComponents Action

The UnpublishComponents action manages the unadvertisement of components listed in the PublishComponent table. These are components that may be faulted in by other products. This action removes information about published components from the [PublishComponent table](publishcomponent-table.md) for which the corresponding feature is currently selected to be uninstalled.

## Sequence Restrictions

There are no sequence restrictions.

## ActionData Messages



| Field | Description of action data                                   |
|-------|--------------------------------------------------------------|
| \[1\] | GUID representing the component ID of an advertised feature. |
| \[2\] | Qualifier of the component ID.                               |



 

