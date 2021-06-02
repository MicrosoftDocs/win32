---
description: The RegisterMIMEInfo action registers MIME-related registry information with the system.
ms.assetid: 2ba88b5f-bd8a-4572-af82-9c0b91b9b6d9
title: RegisterMIMEInfo Action
ms.topic: article
ms.date: 05/31/2018
---

# RegisterMIMEInfo Action

The RegisterMIMEInfo action registers MIME-related registry information with the system.

## Sequence Restrictions

The RegisterMIMEInfo action must come after the [InstallFiles](installfiles-action.md) action, [UnregisterMIMEInfo](unregistermimeinfo-action.md) action, [RegisterClassInfo](registerclassinfo-action.md) action, and the [RegisterExtensionInfo](registerextensioninfo-action.md) action.

The sequencing of the actions in the following group is restricted. If any subset of these actions occur together in a sequence table, they must have the same relative sequence order as shown:

-   [UnregisterClassInfo](unregisterclassinfo-action.md)
-   [UnregisterExtensionInfo](unregisterextensioninfo-action.md)
-   [UnregisterProgIdInfo](unregisterprogidinfo-action.md)
-   [UnregisterMIMEInfo](unregistermimeinfo-action.md)
-   [RegisterClassInfo](registerclassinfo-action.md)
-   [RegisterExtensionInfo](registerextensioninfo-action.md)
-   [RegisterProgIdInfo](registerprogidinfo-action.md)
-   RegisterMIMEInfo

For example, RegisterMIMEInfo must come after [UnregisterMIMEInfo](unregistermimeinfo-action.md) in the sequence table.

## ActionData Messages



| Field | Description of action data                   |
|-------|----------------------------------------------|
| \[1\] | Identifier of registered MIME content type.  |
| \[2\] | Extension associated with MIME content type. |



 

## Remarks

The RegisterMIMEInfo action registers all MIME information for servers from the [MIME table](mime-table.md) for which the corresponding class server or extension server has been selected to be installed.

 

 



