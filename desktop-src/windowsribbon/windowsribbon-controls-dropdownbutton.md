---
title: Drop-Down Button
description: The Drop-Down Button consists of a button that when clicked displays a drop-down list of mutually exclusive items.
ms.assetid: 41c5da07-43f7-4544-83be-248941cb8633
ms.topic: article
ms.date: 05/31/2018
---

# Drop-Down Button

The Drop-Down Button consists of a button that when clicked displays a drop-down list of mutually exclusive items.

-   [Details](#details)
-   [Drop-Down Button Properties](#drop-down-button-properties)
-   [Related topics](#related-topics)

## Details

This control is useful for exposing closely related items in cases where no obvious default is available and where the individual items can be represented by an image, text, or both.

The following screen shot illustrates the Ribbon Drop-Down Button in a sample Ribbon.

![screen shot of a dropdownbutton control in a sample ribbon.](images/controls/dropdownbutton.png)

## Drop-Down Button Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Drop-Down Button control.

Typically, a Drop-Down Button property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [**IUICommandHandler::UpdateProperty**](https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) method and set with the [**IUIFramework::SetUICommandProperty**](https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method.

 

The following table lists the property keys that are associated with the Drop-Down Button control.



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
<td>Supports <a href="https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>.</td>
</tr>
<tr class="even">
<td><a href="windowsribbon-reference-properties-uipkey-enabled">UI_PKEY_Enabled</a></td>
<td>Supports <a href="https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>.<br/> If all child items are disabled, the framework sets <a href="windowsribbon-reference-properties-uipkey-enabled">UI_PKEY_Enabled</a> to false (0). Otherwise, if one or more child items are enabled, UI_PKEY_Enabled is set to true (-1).
<blockquote>
[!Important]<br />
The <a href="windowsribbon-reference-properties-uipkey-enabled">UI_PKEY_Enabled</a> property for the Drop-Down Button control should be invalidated after one or more child items are enabled or disabled. This ensures that the framework queries the updated property value and refreshes the state of the Drop-Down Button control in the ribbon UI.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-reference-properties-uipkey-itemssource">UI_PKEY_ItemsSource</a></td>
<td>Supports <a href="https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>.</td>
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
<td><a href="windowsribbon-reference-properties-uipkey-selecteditem">UI_PKEY_SelectedItem</a></td>
<td>Supports <a href="https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>.
<blockquote>
[!Note]<br />
If the Command associated with the control is invalidated through a call to <a href="https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand"><strong>IUIFramework::InvalidateUICommand</strong></a>, the framework queries this property when <code>UI_INVALIDATIONS_VALUE</code> is passed as the value of <em>flags</em>.
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

[**DropDownButton markup element**](windowsribbon-element-dropdownbutton.md)
</dt> </dl>

 

 





