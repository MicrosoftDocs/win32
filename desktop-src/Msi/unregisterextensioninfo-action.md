---
description: The UnregisterExtensionInfo action manages the removal of extension-related information from the system registry.
ms.assetid: 62bb9d17-c221-4bd2-bd7f-9930e28bb946
title: UnregisterExtensionInfo Action
ms.topic: article
ms.date: 05/31/2018
---

# UnregisterExtensionInfo Action

The UnregisterExtensionInfo action manages the removal of extension-related information from the system registry.

## Sequence Restrictions

The UnregisterExtensionInfo action must come after the [InstallInitialize](installinitialize-action.md) action and before the [RegisterExtensionInfo](registerextensioninfo-action.md) action.

[RemoveRegistryValues](removeregistryvalues-action.md) must come before UnregisterExtensionInfo in the sequence.

The sequencing of the actions in the following group is restricted. If any subset of these actions occur together in a sequence table, they must have the same relative sequence order as shown:

-   [UnregisterClassInfo](unregisterclassinfo-action.md)
-   UnregisterExtensionInfo
-   [UnregisterProgIdInfo](unregisterprogidinfo-action.md)
-   [UnregisterMIMEInfo](unregistermimeinfo-action.md)
-   [RegisterClassInfo](registerclassinfo-action.md)
-   [RegisterExtensionInfo](registerextensioninfo-action.md)
-   [RegisterProgIdInfo](registerprogidinfo-action.md)
-   [RegisterMIMEInfo](registermimeinfo-action.md)

For example, UnregisterExtensionInfo must come before [UnregisterProgIdInfo](unregisterprogidinfo-action.md) in the sequence table.

## ActionData Messages



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | Removed extension.         |



 

## Remarks

If the system does not support the install-on-demand of extension servers, UnregisterExtensionInfo removes all extension servers in the [Extension table](extension-table.md) associated with either an uninstalled feature or a feature installed as advertised from the registry. Otherwise, this action removes the extension servers associated with a feature that is selected to be removed from the registry.

## Related topics

<dl> <dt>

[**ShellAdvtSupport Property**](shelladvtsupport.md)
</dt> </dl>

 

 



