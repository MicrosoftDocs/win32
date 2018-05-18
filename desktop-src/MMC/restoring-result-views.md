---
title: Restoring Result Views
description: A result view must be restored if it is revisited through the navigational history offered by the MMC Back/Forward buttons, or if it is displayed after a saved console file is loaded.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dee09c50-76f1-4186-846c-1cde3d05fd03'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Restoring Result Views

A result view must be restored if it is revisited through the navigational history offered by the MMC Back/Forward buttons, or if it is displayed after a saved console file is loaded. The [**IComponent2**](icomponent2.md) interface, introduced in MMC 2.0, is implemented by snap-ins so that snap-in-specific details of a view can be restored. An example of a snap-in specific detail is the case where a snap-in modifies a result view in response to a snap-in provided menu item; MMC will not recognize this view setting.

In MMC 1.1, a snap-in implemented the [**IComponent::GetResultViewType**](icomponent-getresultviewtype.md) method to inform MMC of a result view type, and the snap-in responded to [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) notifications (through the [**IComponent::Notify**](icomponent-notify.md) method) to restore the view. However, the use of **IComponent::GetResultViewType** and **MMCN\_RESTORE\_VIEW** notifications did not easily allow a snap-in to restore the view with snap-in-specific details, thereby impacting the user experience during view restoration.

MMC 2.0 makes snap-in specific settings easier to restore through the use of the [**IComponent2::GetResultViewType2**](icomponent2-getresultviewtype2.md) and [**IComponent2::RestoreResultView**](icomponent2-restoreresultview.md) methods. When the snap-in provides result view information to MMC (during MMC's call to the snap-in's **IComponent2::GetResultViewType2** method), the snap-in specifies a description for the result view. As the user makes changes to the view settings, the snap-in can internally maintain the view settings values. The snap-in does this by storing the specific data as part of the snap-in's view description information; note that MMC does not store the snap-in specific information. When the view is revisited, MMC restores the generic settings of the view, and the snap-in (notified through MMC's call to the snap-in's **IComponent2::RestoreResultView** method) uses the internally stored view settings to complete the view restoration.

Both of the [**IComponent2::GetResultViewType2**](icomponent2-getresultviewtype2.md) and [**IComponent2::RestoreResultView**](icomponent2-restoreresultview.md) methods use a pointer to a [**RESULT\_VIEW\_TYPE\_INFO**](result-view-type-info.md) structure. The snap-in and MMC know which view is being restored by the pstrPersistableViewDescription member of the **RESULT\_VIEW\_TYPE\_INFO** structure. The snap-in must internally maintain data about the view associated with pstrPersistableViewDescription in order to apply snap-in specific view settings during view restoration.

In MMC 2.0, if a snap-in implements **IComponent2**, then its implementation of [**IComponent::GetResultViewType**](icomponent-getresultviewtype.md) will not be called and its implementation of [**IComponent::Notify**](icomponent-notify.md) will not receive [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) notifications. As stated previously, in MMC 2.0, if the snap-in implements **IComponent2**, then MMC uses [**IComponent2::GetResultViewType2**](icomponent2-getresultviewtype2.md) and [**IComponent2::RestoreResultView**](icomponent2-restoreresultview.md) to retrieve the result view type and inform the snap-in that it must restore the result view, respectively.

If the same snap-in is intended to also run in MMC 1.x, then the snap-in should provide a complete implementation of [**IComponent::GetResultViewType**](icomponent-getresultviewtype.md) and the MMCN\_RESTORE\_VIEW handler in [**IComponent::Notify**](icomponent-notify.md), as MMC 1.x uses these methods to retrieve the view type and inform the snap-in that it must restore the result view.

## Related topics

<dl> <dt>

[**IComponent2**](icomponent2.md)
</dt> <dt>

[**RESULT\_VIEW\_TYPE\_INFO**](result-view-type-info.md)
</dt> </dl>

 

 




