---
description: The UnregisterMIMEInfo action unregisters MIME-related registry information from the system. The action unregisters MIME information for servers from the MIME table for which the corresponding feature is currently selected to be uninstalled.
ms.assetid: 9a5c12da-e78f-4c99-9b82-d41624593c61
title: UnregisterMIMEInfo Action
ms.topic: article
ms.date: 05/31/2018
---

# UnregisterMIMEInfo Action

The UnregisterMIMEInfo action unregisters MIME-related registry information from the system. The action unregisters MIME information for servers from the [MIME table](mime-table.md) for which the corresponding feature is currently selected to be uninstalled.

## Sequence Restrictions

The UnregisterMIMEInfo action must come after the [InstallInitialize](installinitialize-action.md) action, [UnregisterClassInfo](unregisterclassinfo-action.md) action, [UnregisterExtensionInfo](unregisterextensioninfo-action.md) action, and before the [RegisterMIMEInfo](registermimeinfo-action.md) action.

[RemoveRegistryValues](removeregistryvalues-action.md) must come before UnregisterMIMEInfo in the sequence.

The sequencing of the actions in the following group is restricted. If any subset of these actions occur together in a sequence table, they must have the same relative sequence order as shown:

-   [UnregisterClassInfo](unregisterclassinfo-action.md)
-   [UnregisterExtensionInfo](unregisterextensioninfo-action.md)
-   [UnregisterProgIdInfo](unregisterprogidinfo-action.md)
-   UnregisterMIMEInfo
-   [RegisterClassInfo](registerclassinfo-action.md)
-   [RegisterExtensionInfo](registerextensioninfo-action.md)
-   [RegisterProgIdInfo](registerprogidinfo-action.md)
-   [RegisterMIMEInfo](registermimeinfo-action.md)

For example, UnregisterMIMEInfo must come before [RegisterExtensionInfo](registerextensioninfo-action.md) in the sequence table.

## ActionData Messages



| Field | Description of action data                    |
|-------|-----------------------------------------------|
| \[1\] | Identifier of unregistered MIME content type. |
| \[2\] | Extension associated with MIME content type.  |



 

 

 



