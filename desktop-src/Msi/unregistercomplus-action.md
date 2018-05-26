---
Description: The UnregisterComPlus action removes COM+ applications from the registry.
ms.assetid: bcedc436-a048-487e-9a84-e766da57a0b3
title: UnregisterComPlus Action
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UnregisterComPlus Action

The UnregisterComPlus action removes COM+ applications from the registry.

## Sequence Restrictions

The [RegisterComPlus action](registercomplus-action.md) must follow the [InstallFiles action](installfiles-action.md) and the UnregisterComPlus action.

## ActionData Messages



| Field | Description of action data                                    |
|-------|---------------------------------------------------------------|
| \[1\] | Application identifier of the COM+ application being removed. |



 

## Related topics

<dl> <dt>

[RegisterComPlus action](registercomplus-action.md)
</dt> <dt>

[Complus table](complus-table.md)
</dt> <dt>

[Installing a COM+ Application with the Windows Installer](installing-a-com--application-with-the-windows-installer.md)
</dt> </dl>

 

 



