---
description: The RegisterProgIdInfo action manages the registration of OLE ProgId information with the system.
ms.assetid: f6fd4d0d-d2dc-4953-9402-314c7932746b
title: RegisterProgIdInfo Action
ms.topic: article
ms.date: 05/31/2018
---

# RegisterProgIdInfo Action

The RegisterProgIdInfo action manages the registration of OLE ProgId information with the system.

## Sequence Restrictions

The RegisterProgIdInfo action must come after the [InstallFiles](installfiles-action.md) action, [UnregisterProgIdInfo](unregisterprogidinfo-action.md) action, [RegisterClassInfo](registerclassinfo-action.md) action, and the [RegisterExtensionInfo](registerextensioninfo-action.md) action.

The sequencing of the actions in the following group is restricted. If any subset of these actions occur together in a sequence table, they must have the same relative sequence order as shown:

-   [UnregisterClassInfo](unregisterclassinfo-action.md)
-   [UnregisterExtensionInfo](unregisterextensioninfo-action.md)
-   [UnregisterProgIdInfo](unregisterprogidinfo-action.md)
-   [UnregisterMIMEInfo](unregistermimeinfo-action.md)
-   [RegisterClassInfo](registerclassinfo-action.md)
-   [RegisterExtensionInfo](registerextensioninfo-action.md)
-   RegisterProgIdInfo
-   [RegisterMIMEInfo](registermimeinfo-action.md)

For example, RegisterProgIdInfo must come after [RegisterExtensionInfo](registerextensioninfo-action.md) in the sequence table.

## ActionData Messages



| Field | Description of action data                |
|-------|-------------------------------------------|
| \[1\] | Program identifier of registered program. |



 

## Remarks

The RegisterProgIdInfo action registers all ProgId information for servers that are specified in the [ProgId table](progid-table.md) and for which the corresponding class server or extension server has been selected to be installed.

## Related topics

<dl> <dt>

[Class table](class-table.md)
</dt> <dt>

[Extension table](extension-table.md)
</dt> </dl>

 

 



