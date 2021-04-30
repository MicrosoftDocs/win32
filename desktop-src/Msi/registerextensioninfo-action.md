---
description: The RegisterExtensionInfo action manages the registration of extension related information with the system.
ms.assetid: 3c243ca3-9fa7-41ec-968e-7954d7d45432
title: RegisterExtensionInfo Action
ms.topic: article
ms.date: 05/31/2018
---

# RegisterExtensionInfo Action

The RegisterExtensionInfo action manages the registration of extension related information with the system.

## Sequence Restrictions

The RegisterExtensionInfo action must come after the [InstallFiles](installfiles-action.md) action and the [UnregisterExtensionInfo](unregisterextensioninfo-action.md) action.

The sequencing of the actions in the following group is restricted. If any subset of these actions occur together in a sequence table, they must have the same relative sequence order as shown:

-   [UnregisterClassInfo](unregisterclassinfo-action.md)
-   [UnregisterExtensionInfo](unregisterextensioninfo-action.md)
-   [UnregisterProgIdInfo](unregisterprogidinfo-action.md)
-   [UnregisterMIMEInfo](unregistermimeinfo-action.md)
-   [RegisterClassInfo](registerclassinfo-action.md)
-   RegisterExtensionInfo
-   [RegisterProgIdInfo](registerprogidinfo-action.md)
-   [RegisterMIMEInfo](registermimeinfo-action.md)

For example, RegisterExtensionInfo must come after [UnregisterMIMEInfo](unregistermimeinfo-action.md) in the sequence table.

## ActionData Messages



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | Registered extension.      |



 

## Remarks

If the system supports installation-on-demand for extension servers, RegisterExtensionInfo registers all extension servers in the [Extension table](extension-table.md) associated with features set for installation or advertisement. Otherwise this action only registers extension servers associated with features set to installation.

## Related topics

<dl> <dt>

[**ShellAdvtSupport property**](shelladvtsupport.md)
</dt> </dl>

 

 



