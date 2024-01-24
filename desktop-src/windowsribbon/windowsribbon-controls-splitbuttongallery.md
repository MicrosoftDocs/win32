---
title: Split Button Gallery
description: The Split Button Gallery is a composite control that contains a primary button which exposes a single default item or Command, and a secondary button which when clicked displays the rest of the item or Command collection in a mutually exclusive drop-down list.
ms.assetid: c0fcfe72-d2e9-465d-941a-b3832b36b8c2
ms.topic: article
ms.date: 05/31/2018
---

# Split Button Gallery

The Split Button Gallery is a composite control that contains a primary button which exposes a single default item or Command, and a secondary button which when clicked displays the rest of the item or Command collection in a mutually exclusive drop-down list.

-   [Details](#details)
-   [Split Button Gallery Properties](#split-button-gallery-properties)
-   [Related topics](#related-topics)

## Details

This control is useful for exposing closely related items in cases where an obvious default is available and where the individual items can be represented by an image, text, or both.

The following screen shot illustrates the Ribbon Split Button Gallery in Microsoft Paint.

![screen shot of a splitbuttongallery control in the microsoft paint ribbon.](images/controls/splitbuttongallery.png)

## Split Button Gallery Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Split Button Gallery control.

Typically, a Split Button Gallery property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) method and set with the [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method.

 

The following table lists the property keys that are associated with the Split Button Gallery control.




| Property Key | Notes | 
|--------------|-------|
| <a href="windowsribbon-reference-properties-uipkey-booleanvalue.md">UI_PKEY_BooleanValue</a> | Supports <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>. | 
| <a href="windowsribbon-reference-properties-uipkey-categories.md">UI_PKEY_Categories</a> | Supports <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>. | 
| <a href="windowsribbon-reference-properties-uipkey-enabled.md">UI_PKEY_Enabled</a> | Supports <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>. | 
| <a href="windowsribbon-reference-properties-uipkey-itemssource.md">UI_PKEY_ItemsSource</a> | Supports <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>. | 
| <a href="windowsribbon-reference-properties-uipkey-keytip.md">UI_PKEY_Keytip</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-label.md">UI_PKEY_Label</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-largehighcontrastimage.md">UI_PKEY_LargeHighContrastImage</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-largeimage.md">UI_PKEY_LargeImage</a> | Can only be updated through invalidation. | 
| [UI_PKEY_SelectedItem](windowsribbon-reference-properties-uipkey-selecteditem.md)(only valid for an item gallery)<br> | Supports [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) and [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty). **Note:** If the Command associated with the control is invalidated through a call to [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand), the framework queries this property when <code>UI_INVALIDATIONS_VALUE</code> is passed as the value of **flags**.<br> | 
| <a href="windowsribbon-reference-properties-uipkey-smallhighcontrastimage.md">UI_PKEY_SmallHighContrastImage</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-smallimage.md">UI_PKEY_SmallImage</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-tooltipdescription.md">UI_PKEY_TooltipDescription</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-tooltiptitle.md">UI_PKEY_TooltipTitle</a> | Can only be updated through invalidation. | 




 

## Related topics

<dl> <dt>

[**SplitButtonGallery markup element**](windowsribbon-element-splitbuttongallery.md)
</dt> <dt>

[Working with Galleries](ribbon-controls-galleries.md)
</dt> <dt>

[Gallery Sample](windowsribbon-gallerysample.md)
</dt> </dl>

