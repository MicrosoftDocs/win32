---
title: Enabling MMC 2.0 Standard Verbs
description: A primary snap-in has the opportunity to enable MMC standard verbs for scope or result items when its IComponent Notify method is called with the MMCN\_SELECT notification message.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bfb239bb-0f46-47bc-addf-ea5db8088c6a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- enabling MMC 2.0 standard verbs
- enabling MMC 2.0 standard verbs
- verbs MMC 2.0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enabling MMC 2.0 Standard Verbs

A primary snap-in has the opportunity to enable MMC standard verbs for scope or result items when its [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) method is called with the [**MMCN\_SELECT**](mmcn-select.md) notification message. Be aware that MMC standard verbs are not to be confused with context menu items that snap-ins can add to the context menus of their scope and result items. For more information about context menus, see [Working with Context Menus](working-with-context-menus.md).

The [**MMC\_CONSOLE\_VERB**](/windows/win32/Mmc/ne-mmc-_mmc_console_verb?branch=master) enumeration defines the command identifiers available for standard verbs. The following verbs are allowed:

-   MMC\_VERB\_NONE
-   MMC\_VERB\_OPEN
-   MMC\_VERB\_COPY
-   MMC\_VERB\_PASTE
-   MMC\_VERB\_DELETE
-   MMC\_VERB\_PROPERTIES
-   MMC\_VERB\_RENAME
-   MMC\_VERB\_REFRESH
-   MMC\_VERB\_PRINT
-   MMC\_VERB\_CUT

When a standard verb is enabled for an item and the user selects it, MMC calls the snap-in's [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) method with the appropriate notification message. See the [**MMC\_CONSOLE\_VERB**](/windows/win32/Mmc/ne-mmc-_mmc_console_verb?branch=master) documentation in the MMC SDK for details.

Be aware that MMC does not send a notification message in the case of the MMC\_VERB\_PROPERTIES, MMC\_VERB\_COPY and MMC\_VERB\_CUT verbs. When the MMC\_VERB\_PROPERTIES verb is enabled and the user selects it, MMC calls the [**IExtendPropertySheet2::CreatePropertyPages**](iextendpropertysheet2-createpropertypages.md) method of all snap-ins (primary and extension) that add property pages for the selected item. Be aware that primary snap-ins are responsible for enabling the MMC\_VERB\_PROPERTIES verb. Extension snap-ins cannot do this, because they do not own the item for which the verb is enabled.

If the snap-in does not explicitly enable or hide MMC\_VERB\_CUT but does enable MMC\_VERB\_COPY and MMC\_VERB\_DELETE, then MMC\_VERB\_CUT will be automatically enabled. Once the snap-in explicitly enables and does not hide MMC\_VERB\_CUT, then the states of MMC\_VERB\_COPY and MMC\_VERB\_DELETE do not automatically determine the MMC\_VERB\_CUT state. If MMC\_VERB\_COPY and MMC\_VERB\_DELETE are enabled and MMC\_VERB\_CUT is hidden, then MMC\_VERB\_CUT will not appear as an item in a context menu or toolbar, but the Cut verb could be invoked by means of the keyboard accelerator (Ctrl+X).

When the MMC\_VERB\_COPY or MMC\_VERB\_CUT verb is enabled and the user selects it, MMC calls the snap-in's [**IComponentData::QueryDataObject**](/windows/win32/Mmc/nf-mmc-icomponentdata-querydataobject?branch=master) or [**IComponent::QueryDataObject**](/windows/win32/Mmc/nf-mmc-icomponent-querydataobject?branch=master) implementation to request a data object for the selected item.

The MMC\_VERB\_DELETE, MMC\_VERB\_COPY, and MMC\_VERB\_PASTE verbs must all be enabled in snap-ins that support cut/copy/paste operations. Be aware that snap-ins that support cut/copy/paste operations also automatically support drag-and-drop operations as well — no extra coding is required. For more information, see [Drag and Drop](drag-and-drop.md).

As mentioned above, snap-ins enable standard verbs in their [**MMCN\_SELECT**](mmcn-select.md) notification handler. In the notification handler, snap-ins should call [**IConsole2::QueryConsoleVerb**](iconsole2-queryconsoleverb.md) to request a pointer to MMC's [**IConsoleVerb**](/windows/win32/Mmc/nn-mmc-iconsoleverb?branch=master) interface implementation. Using the returned interface pointer, snap-ins can then call the [**IConsoleVerb::SetVerbState**](/windows/win32/Mmc/nf-mmc-iconsoleverb-setverbstate?branch=master) method to enable (or disable) the standard verbs, one call per standard verb. Snap-ins can also call the [**SetDefaultVerb**](/windows/win32/Mmc/nf-mmc-iconsoleverb-setdefaultverb?branch=master) method to set the default verb for an item. The default verb is indicated in bold type in the item's context menu.

Some of the standard verbs have associated toolbar buttons. For example, when the MMC\_VERB\_DELETE verb is enabled for an item, MMC displays a toolbar button when the item is selected. The user can then either click the toolbar button or click the **Delete** context menu item to delete the item.

## Note

MMC will not send Cut, Copy, Paste, or Rename notifications to OCX controls.

## Related topics

<dl> <dt>

[Enabling MMC Standard Verbs: Implementation Details](enabling-mmc-standard-verbs-implementation-details.md)
</dt> <dt>

[Enabling Drag and Drop in the MMC](drag-and-drop.md)
</dt> <dt>

[Enabling Multiselection in the MMC](multiselection.md)
</dt> </dl>

 

 




