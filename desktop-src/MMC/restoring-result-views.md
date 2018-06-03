---
title: Restoring Result Views
description: A result view must be restored if it is revisited through the navigational history offered by the MMC Back/Forward buttons, or if it is displayed after a saved console file is loaded.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dee09c50-76f1-4186-846c-1cde3d05fd03
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Restoring Result Views

A result view must be restored if it is revisited through the navigational history offered by the MMC Back/Forward buttons, or if it is displayed after a saved console file is loaded. The [**IComponent2**](/windows/desktop/api/Mmc/nn-mmc-icomponent2) interface, introduced in MMC 2.0, is implemented by snap-ins so that snap-in-specific details of a view can be restored. An example of a snap-in specific detail is the case where a snap-in modifies a result view in response to a snap-in provided menu item; MMC will not recognize this view setting.

In MMC 1.1, a snap-in implemented the [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) method to inform MMC of a result view type, and the snap-in responded to [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) notifications (through the [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) method) to restore the view. However, the use of **IComponent::GetResultViewType** and **MMCN\_RESTORE\_VIEW** notifications did not easily allow a snap-in to restore the view with snap-in-specific details, thereby impacting the user experience during view restoration.

MMC 2.0 makes snap-in specific settings easier to restore through the use of the [**IComponent2::GetResultViewType2**](/windows/desktop/api/Mmc/nf-mmc-icomponent2-getresultviewtype2) and [**IComponent2::RestoreResultView**](/windows/desktop/api/Mmc/nf-mmc-icomponent2-restoreresultview) methods. When the snap-in provides result view information to MMC (during MMC's call to the snap-in's **IComponent2::GetResultViewType2** method), the snap-in specifies a description for the result view. As the user makes changes to the view settings, the snap-in can internally maintain the view settings values. The snap-in does this by storing the specific data as part of the snap-in's view description information; note that MMC does not store the snap-in specific information. When the view is revisited, MMC restores the generic settings of the view, and the snap-in (notified through MMC's call to the snap-in's **IComponent2::RestoreResultView** method) uses the internally stored view settings to complete the view restoration.

Both of the [**IComponent2::GetResultViewType2**](/windows/desktop/api/Mmc/nf-mmc-icomponent2-getresultviewtype2) and [**IComponent2::RestoreResultView**](/windows/desktop/api/Mmc/nf-mmc-icomponent2-restoreresultview) methods use a pointer to a [**RESULT\_VIEW\_TYPE\_INFO**](/windows/desktop/api/Mmc/ns-mmc-_result_view_type_info) structure. The snap-in and MMC know which view is being restored by the pstrPersistableViewDescription member of the **RESULT\_VIEW\_TYPE\_INFO** structure. The snap-in must internally maintain data about the view associated with pstrPersistableViewDescription in order to apply snap-in specific view settings during view restoration.

In MMC 2.0, if a snap-in implements **IComponent2**, then its implementation of [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) will not be called and its implementation of [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) will not receive [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) notifications. As stated previously, in MMC 2.0, if the snap-in implements **IComponent2**, then MMC uses [**IComponent2::GetResultViewType2**](/windows/desktop/api/Mmc/nf-mmc-icomponent2-getresultviewtype2) and [**IComponent2::RestoreResultView**](/windows/desktop/api/Mmc/nf-mmc-icomponent2-restoreresultview) to retrieve the result view type and inform the snap-in that it must restore the result view, respectively.

If the same snap-in is intended to also run in MMC 1.x, then the snap-in should provide a complete implementation of [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) and the MMCN\_RESTORE\_VIEW handler in [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify), as MMC 1.x uses these methods to retrieve the view type and inform the snap-in that it must restore the result view.

## Related topics

<dl> <dt>

[**IComponent2**](/windows/desktop/api/Mmc/nn-mmc-icomponent2)
</dt> <dt>

[**RESULT\_VIEW\_TYPE\_INFO**](/windows/desktop/api/Mmc/ns-mmc-_result_view_type_info)
</dt> </dl>

 

 




