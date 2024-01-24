---
description: The UnregisterClassInfo action manages the removal of COM class information from the system registry. It uses the AppId table.
ms.assetid: 579a69ee-92cd-4d4c-a007-998ec042f9fc
title: UnregisterClassInfo Action
ms.topic: article
ms.date: 05/31/2018
---

# UnregisterClassInfo Action

The UnregisterClassInfo action manages the removal of COM class information from the system registry. It uses the [AppId table](appid-table.md).

## Sequence Restrictions

The UnregisterClassInfo action must come after the [InstallInitialize](installinitialize-action.md) action and before the [RegisterClassInfo](registerclassinfo-action.md) action.

[RemoveRegistryValues](removeregistryvalues-action.md) must come before UnregisterClassInfo in the sequence.

The sequencing of the actions in the following group is restricted. If any subset of these actions occur together in a sequence table, they must occur in the same relative sequence as shown in the following table:

-   UnregisterClassInfo
-   [UnregisterExtensionInfo](unregisterextensioninfo-action.md)
-   [UnregisterProgIdInfo](unregisterprogidinfo-action.md)
-   [UnregisterMIMEInfo](unregistermimeinfo-action.md)
-   [RegisterClassInfo](registerclassinfo-action.md)
-   [RegisterExtensionInfo](registerextensioninfo-action.md)
-   [RegisterProgIdInfo](registerprogidinfo-action.md)
-   [RegisterMIMEInfo](registermimeinfo-action.md)

For example, [RegisterExtensionInfo](registerextensioninfo-action.md) must come before UnregisterClassInfo in the sequence table.

## ActionData Messages



| Field | Description of action data      |
|-------|---------------------------------|
| \[1\] | GUID of unregistered COM class. |



 

## Remarks

The installer sets the [**OLEAdvtSupport**](oleadvtsupport.md) property to true when the current user's system has been upgraded to work with install-on-demand through COM. If the system does not support install-on-demand through COM, UnregisterClassInfo removes all COM classes listed in the [Class table](class-table.md) associated with either uninstalled features or features installed as advertised from the system registry. Otherwise, this action removes only the COM classes associated with features selected to be uninstalled from the system registry.

 

 



