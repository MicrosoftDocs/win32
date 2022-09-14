---
description: The UnregisterProgIdInfo action manages the unregistration of OLE ProgId information with the system.
ms.assetid: c9837845-4ffc-4496-8330-11b46d27ec7a
title: UnregisterProgIdInfo Action
ms.topic: article
ms.date: 05/31/2018
---

# UnregisterProgIdInfo Action

The UnregisterProgIdInfo action manages the unregistration of OLE ProgId information with the system.

## Sequence Restrictions

The UnregisterProgIdInfo action must come after the [InstallInitialize](installinitialize-action.md) action, [UnregisterClassInfo](unregisterclassinfo-action.md) action, [UnregisterExtensioninfo](unregisterextensioninfo-action.md) action, and before the [RegisterProgIdInfo](registerprogidinfo-action.md) action.

[RemoveRegistryValues](removeregistryvalues-action.md) must come before UnregisterProgIdInfo in the sequence.

The sequencing of the actions in the following group is restricted. If any subset of these actions occur together in a sequence table, they must have the same relative sequence order as shown:

-   [UnregisterClassInfo](unregisterclassinfo-action.md)
-   [UnregisterExtensioninfo](unregisterextensioninfo-action.md)
-   UnregisterProgIdInfo
-   [UnregisterMIMEInfo](unregistermimeinfo-action.md)
-   [RegisterClassInfo](registerclassinfo-action.md)
-   [RegisterExtensionInfo](registerextensioninfo-action.md)
-   [RegisterProgIdInfo](registerprogidinfo-action.md)
-   [RegisterMIMEInfo](registermimeinfo-action.md)

For example, UnregisterProgIdInfo must come before [UnregisterMIMEInfo](unregistermimeinfo-action.md) in the sequence table.

## ActionData Messages



| Field | Description of action data                |
|-------|-------------------------------------------|
| \[1\] | Program identifier of registered program. |



 

## Remarks

The UnregisterProgIdInfo action removes ProgId information from the registry ([ProgId Table](progid-table.md)) for features that are connected to the extension information ([Extension table](extension-table.md)) or the Class information ([Class table](class-table.md)) and are currently selected to be uninstalled.

 

 



