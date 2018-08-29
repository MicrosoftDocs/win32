---
title: Drop-Down Gallery
description: The Drop-Down Gallery consists of a button that when clicked displays a drop-down list containing a collection of mutually exclusive items or Commands.
ms.assetid: 10644e10-f903-49f6-aecd-1a63d97fe447
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Drop-Down Gallery

The Drop-Down Gallery consists of a button that when clicked displays a drop-down list containing a collection of mutually exclusive items or Commands.

-   [Details](#details)
-   [Drop-Down Gallery Properties](#drop-down-gallery-properties)
-   [Related topics](#related-topics)

## Details

This control is useful for exposing related items or Commands where there is no obvious default, and the individual items can be represented by an image, text, or both.

Support for both vertical and corner gripper bars, or resizing handles, is provided through the [**DropDownGallery.MenuLayout**](windowsribbon-element-dropdowngallery-menulayout.md) element.

The following screen shot illustrates the Ribbon Drop-Down Gallery in Microsoft Paint.

![screen shot of a dropdowngallery control in the microsoft paint ribbon.](images/controls/dropdowngallery.png)

## Drop-Down Gallery Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Drop-Down Gallery control.

Typically, a Drop-Down Gallery property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](https://msdn.microsoft.com/library/windows/desktop/dd371375) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371494) callback method.

The [**IUICommandHandler::UpdateProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371494) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371370) method and set with the [**IUIFramework::SetUICommandProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371478) method.

 

The following table lists the property keys that are associated with the Drop-Down Gallery control.



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
<td><a href="windowsribbon-reference-properties-uipkey-categories">UI_PKEY_Categories</a></td>
<td>Supports <a href="https://msdn.microsoft.com/library/windows/desktop/dd371370"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd371478"><strong>IUIFramework::SetUICommandProperty</strong></a>.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-enabled">UI_PKEY_Enabled</a></td>
<td>Supports <a href="https://msdn.microsoft.com/library/windows/desktop/dd371370"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd371478"><strong>IUIFramework::SetUICommandProperty</strong></a>.</td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-itemssource">UI_PKEY_ItemsSource</a></td>
<td>Supports <a href="https://msdn.microsoft.com/library/windows/desktop/dd371370"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd371478"><strong>IUIFramework::SetUICommandProperty</strong></a>.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-keytip">UI_PKEY_Keytip</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-label">UI_PKEY_Label</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-largehighcontrastimage">UI_PKEY_LargeHighContrastImage</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-largeimage">UI_PKEY_LargeImage</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-selecteditem">UI_PKEY_SelectedItem</a>(only valid for an item gallery)<br/></td>
<td>Supports <a href="https://msdn.microsoft.com/library/windows/desktop/dd371370"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd371478"><strong>IUIFramework::SetUICommandProperty</strong></a>.
<blockquote>
[!Note]<br />
If the Command associated with the control is invalidated through a call to <a href="https://msdn.microsoft.com/library/windows/desktop/dd371375"><strong>IUIFramework::InvalidateUICommand</strong></a>, the framework queries this property when <code>UI_INVALIDATIONS_VALUE</code> is passed as the value of <em>flags</em>.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-smallhighcontrastimage">UI_PKEY_SmallHighContrastImage</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-smallimage">UI_PKEY_SmallImage</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-tooltipdescription">UI_PKEY_TooltipDescription</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-tooltiptitle">UI_PKEY_TooltipTitle</a></td>
<td>Can only be updated through invalidation.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**DropDownGallery markup element**](windowsribbon-element-dropdowngallery.md)
</dt> <dt>

[Working with Galleries](ribbon-controls-galleries.md)
</dt> <dt>

[Gallery Sample](windowsribbon-gallerysample.md)
</dt> </dl>

 

 





