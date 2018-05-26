---
title: C++ Code Only
description: Provides test considerations that apply only to C/C++ developers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 69365c65-e445-4a54-8ed2-8294e331d7b1
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- snap-in testing MMC , C++
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# C++ Code Only

The following considerations apply only to C/C++ developers:

-   Namespace extensions have a special purpose. Only a single instance of a namespace extension is created for a single instance of the snap-in that it is extending, regardless of the number of nodes that it extends. Thus, a namespace extension must maintain several "trees" of nodes, one per node extended. Ensure that this logic is coded into the snap-in.
-   Check data objects and cookies that use the macros [**IS\_SPECIAL\_DATAOBJECT**](/windows/win32/Mmc/nf-mmc-is_special_dataobject?branch=master) and [**IS\_SPECIAL\_COOKIE**](/windows/win32/Mmc/nf-mmc-is_special_cookie?branch=master) to ensure that the special data objects and special cookies are handled appropriately. Every snap-in should handle a **NULL** cookie because MMC uses this value to refer to the static node belonging to a stand-alone snap-in. Every snap-in should handle a **NULL** data object because some notifications such as [**MMCN\_DESELECT\_ALL**](mmcn-deselect-all.md) and [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) send a **NULL** data object by default.
-   For history and view persistence to work well, ensure the snap-in handles [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) appropriately.
-   Verify that [**IComponentData::Notify**](/windows/win32/Mmc/nf-mmc-icomponentdata-notify?branch=master), [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master), and [**IExtendControlbar::ControlBarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master) return **S\_FALSE** to notifications they do not handle.
-   For data objects, support the new [**CCF\_NODEID2**](ccf-nodeid2.md) clipboard format, not the old [**CCF\_NODEID**](ccf-nodeid.md) format.
-   If you use Wizard97 wizards, ensure that you implement [**IExtendPropertySheet2::GetWatermarks**](/windows/win32/Mmc/nf-mmc-iextendpropertysheet2-getwatermarks?branch=master) and that it returns **S\_OK**.
-   If you are using Microsoft Foundation Classes (MFC), you should call AFX\_MANAGE\_STATE. If you do not make this call, the module and thread state will be wrong and it can be difficult to debug the problem.
-   Snap-ins can return **S\_OK** from [**IComponent::CompareObjects**](/windows/win32/Mmc/nf-mmc-icomponent-compareobjects?branch=master) only if the two objects that expose an [**IDataObject**](https://msdn.microsoft.com/library/windows/desktop/ms688421) interface for comparison refer to the same object.
-   The notification handler for a snap-in should return **S\_FALSE** by default. The **S\_FALSE** value triggers the default operation for the notification. Failure to follow this strategy could limit future functionality.

 

 




