---
title: In-Ribbon Gallery
description: The In-Ribbon Gallery is a control that displays a collection of related items or Commands in the Ribbon. If there are too many items in the gallery, an expand arrow is provided to display the rest of the collection in an expanded pane.
ms.assetid: 'd608dd0d-a0af-49a6-a129-7115195c0df2'
---

# In-Ribbon Gallery

The In-Ribbon Gallery is a control that displays a collection of related items or Commands in the Ribbon. If there are too many items in the gallery, an expand arrow is provided to display the rest of the collection in an expanded pane.

-   [Details](#details)
-   [In-Ribbon Gallery Properties](#in-ribbon-gallery-properties)
-   [Related topics](#related-topics)

## Details

The following screen shot illustrates the Ribbon In-Ribbon Gallery control in Microsoft Paint.

![screen shot of a inribbongallery control in the microsoft paint ribbon.](images/controls/inribbongallery.png)

## In-Ribbon Gallery Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the In-Ribbon Gallery control.

Typically, an In-Ribbon Gallery property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](https://msdn.microsoft.com/library/windows/desktop/dd371375) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371494) callback method.

The [**IUICommandHandler::UpdateProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371494) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371370) method and set with the [**IUIFramework::SetUICommandProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371478) method.

 

The following table lists the property keys that are associated with the In-Ribbon Gallery control.



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
<td>[UI_PKEY_Categories](windowsribbon-reference-properties-uipkey-categories.md)</td>
<td>Supports [<strong>IUIFramework::GetUICommandProperty</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371370) and [<strong>IUIFramework::SetUICommandProperty</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371478).</td>
</tr>
<tr class="even">
<td>[UI_PKEY_Enabled](windowsribbon-reference-properties-uipkey-enabled.md)</td>
<td>Supports [<strong>IUIFramework::GetUICommandProperty</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371370) and [<strong>IUIFramework::SetUICommandProperty</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371478).</td>
</tr>
<tr class="odd">
<td>[UI_PKEY_ItemsSource](windowsribbon-reference-properties-uipkey-itemssource.md)</td>
<td>Supports [<strong>IUIFramework::GetUICommandProperty</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371370) and [<strong>IUIFramework::SetUICommandProperty</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371478).</td>
</tr>
<tr class="even">
<td>[UI_PKEY_Keytip](windowsribbon-reference-properties-uipkey-keytip.md)</td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="odd">
<td>[UI_PKEY_Label](windowsribbon-reference-properties-uipkey-label.md)</td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td>[UI_PKEY_LargeHighContrastImage](windowsribbon-reference-properties-uipkey-largehighcontrastimage.md)</td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="odd">
<td>[UI_PKEY_LargeImage](windowsribbon-reference-properties-uipkey-largeimage.md)</td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td>[UI_PKEY_SelectedItem](windowsribbon-reference-properties-uipkey-selecteditem.md)(only valid for an item gallery)<br/></td>
<td>Supports [<strong>IUIFramework::GetUICommandProperty</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371370) and [<strong>IUIFramework::SetUICommandProperty</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371478).
<blockquote>
[!Note]<br />
If the Command associated with the control is invalidated through a call to [<strong>IUIFramework::InvalidateUICommand</strong>](https://msdn.microsoft.com/library/windows/desktop/dd371375), the framework queries this property when <code>UI_INVALIDATIONS_VALUE</code> is passed as the value of <em>flags</em>.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[UI_PKEY_SmallHighContrastImage](windowsribbon-reference-properties-uipkey-smallhighcontrastimage.md)</td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td>[UI_PKEY_SmallImage](windowsribbon-reference-properties-uipkey-smallimage.md)</td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="odd">
<td>[UI_PKEY_TooltipDescription](windowsribbon-reference-properties-uipkey-tooltipdescription.md)</td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td>[UI_PKEY_TooltipTitle](windowsribbon-reference-properties-uipkey-tooltiptitle.md)</td>
<td>Can only be updated through invalidation.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**InRibbonGallery element**](windowsribbon-element-inribbongallery.md)
</dt> <dt>

[Working with Galleries](ribbon-controls-galleries.md)
</dt> <dt>

[Gallery Sample](windowsribbon-gallerysample.md)
</dt> </dl>

 

 





