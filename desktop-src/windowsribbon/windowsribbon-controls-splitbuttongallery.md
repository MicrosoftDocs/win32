---
title: Split Button Gallery
description: The Split Button Gallery is a composite control that contains a primary button which exposes a single default item or Command, and a secondary button which when clicked displays the rest of the item or Command collection in a mutually exclusive drop-down list.
ms.assetid: c0fcfe72-d2e9-465d-941a-b3832b36b8c2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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

Typically, a Split Button Gallery property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](https://msdn.microsoft.com/library/windows/desktop/dd371375) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371494) callback method.

The [**IUICommandHandler::UpdateProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371494) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371370) method and set with the [**IUIFramework::SetUICommandProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371478) method.

 

The following table lists the property keys that are associated with the Split Button Gallery control.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property Key</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-booleanvalue">UI_PKEY_BooleanValue</a></td>
<td>Supports <a href="https://msdn.microsoft.com/library/windows/desktop/dd371370"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd371478"><strong>IUIFramework::SetUICommandProperty</strong></a>.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-categories">UI_PKEY_Categories</a></td>
<td>Supports <a href="https://msdn.microsoft.com/library/windows/desktop/dd371370"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd371478"><strong>IUIFramework::SetUICommandProperty</strong></a>.</td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-enabled">UI_PKEY_Enabled</a></td>
<td>Supports <a href="https://msdn.microsoft.com/library/windows/desktop/dd371370"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd371478"><strong>IUIFramework::SetUICommandProperty</strong></a>.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-itemssource">UI_PKEY_ItemsSource</a></td>
<td>Supports <a href="https://msdn.microsoft.com/library/windows/desktop/dd371370"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd371478"><strong>IUIFramework::SetUICommandProperty</strong></a>.</td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-keytip">UI_PKEY_Keytip</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-label">UI_PKEY_Label</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-largehighcontrastimage">UI_PKEY_LargeHighContrastImage</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-largeimage">UI_PKEY_LargeImage</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-selecteditem">UI_PKEY_SelectedItem</a>(only valid for an item gallery)<br/></td>
<td>Supports <a href="https://msdn.microsoft.com/library/windows/desktop/dd371370"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd371478"><strong>IUIFramework::SetUICommandProperty</strong></a>.
<blockquote>
[!Note]<br />
If the Command associated with the control is invalidated through a call to <a href="https://msdn.microsoft.com/library/windows/desktop/dd371375"><strong>IUIFramework::InvalidateUICommand</strong></a>, the framework queries this property when <code>UI_INVALIDATIONS_VALUE</code> is passed as the value of <em>flags</em>.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-smallhighcontrastimage">UI_PKEY_SmallHighContrastImage</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-smallimage">UI_PKEY_SmallImage</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-tooltipdescription">UI_PKEY_TooltipDescription</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-tooltiptitle">UI_PKEY_TooltipTitle</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[**SplitButtonGallery markup element**](windowsribbon-element-splitbuttongallery.md)
</dt> <dt>

[Working with Galleries](ribbon-controls-galleries.md)
</dt> <dt>

[Gallery Sample](windowsribbon-gallerysample.md)
</dt> </dl>

 

 





