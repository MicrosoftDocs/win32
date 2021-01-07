---
description: The RegisterClassInfo action manages the registration of COM class information with the system. It uses the AppId table.
ms.assetid: f8b60a75-9c0e-41c5-b6af-6a05a26b2d71
title: RegisterClassInfo Action
ms.topic: article
ms.date: 05/31/2018
---

# RegisterClassInfo Action

The RegisterClassInfo action manages the registration of COM class information with the system. It uses the [AppId table](appid-table.md).

## Sequence Restrictions

The RegisterClassInfo action must come after the [InstallFiles](installfiles-action.md) action and the [UnregisterClassInfo](unregisterclassinfo-action.md) action.

The sequencing of the actions in the following group is restricted. If any subset of these actions occur together in a sequence table, they must have the same relative sequence order as shown:

-   [UnregisterClassInfo](unregisterclassinfo-action.md)
-   [UnregisterExtensionInfo](unregisterextensioninfo-action.md)
-   [UnregisterProgIdInfo](unregisterprogidinfo-action.md)
-   [UnregisterMIMEInfo](unregistermimeinfo-action.md)
-   RegisterClassInfo
-   [RegisterExtensionInfo](registerextensioninfo-action.md)
-   [RegisterProgIdInfo](registerprogidinfo-action.md)
-   [RegisterMIMEInfo](registermimeinfo-action.md)

For example, RegisterClassInfo must come after [UnregisterMIMEInfo](unregistermimeinfo-action.md) in the sequence table.

## ActionData Messages



| Field | Description of action data                          |
|-------|-----------------------------------------------------|
| \[1\] | GUID class identifier of the registered COM server. |



 

## Remarks

If the system supports install-on-demand for OLE servers, RegisterClassInfo registers all COM classes in the [Class table](class-table.md) associated with a feature selected to be installed or advertised. Otherwise this action only registers the COM classes associated with a feature selected for installation.

## Related topics

<dl> <dt>

[**OLEAdvtSupport property**](oleadvtsupport.md)
</dt> </dl>

 

 



