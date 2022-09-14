---
title: Split Button
description: The Split Button is a composite control with which the user can select a default value bound to a primary button, or select from a list of mutually exclusive values displayed in a drop-down list bound to a secondary button.
ms.assetid: 0939b3be-fa88-4864-8096-a664ab2e97b5
ms.topic: article
ms.date: 05/31/2018
---

# Split Button

The Split Button is a composite control with which the user can select a default value bound to a primary button, or select from a list of mutually exclusive values displayed in a drop-down list bound to a secondary button.

-   [Introduction](#introduction)
-   [Split Button Properties](#split-button-properties)
-   [Related topics](#related-topics)

## Introduction

This control is useful for exposing closely related items in cases where an obvious default is available and where the individual items can be represented by an image, text, or both.

The following screen shot illustrates the Ribbon Split Button.

![screen shot of a splitbutton control in a sample ribbon.](images/controls/splitbutton.png)

## Split Button Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Split Button control.

Typically, a Split Button property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) method and set with the [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method.

 

The following table lists the property keys that are associated with the Split Button control.




| Property Key | Notes | 
|--------------|-------|
| <a href="windowsribbon-reference-properties-uipkey-enabled.md">UI_PKEY_Enabled</a> | Supports <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty"><strong>IUIFramework::GetUICommandProperty</strong></a> and <a href="/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty"><strong>IUIFramework::SetUICommandProperty</strong></a>.<br /> If all child items are disabled, the framework sets <a href="windowsribbon-reference-properties-uipkey-enabled.md">UI_PKEY_Enabled</a> to false (0). Otherwise, if one or more child items are enabled, UI_PKEY_Enabled is set to true (-1).<blockquote>[!Important]<br />The <a href="windowsribbon-reference-properties-uipkey-enabled.md">UI_PKEY_Enabled</a> property for the Split Button control should be invalidated after one or more child items are enabled or disabled. This ensures that the framework queries the updated property value and refreshes the state of the Split Button control in the ribbon UI.</blockquote><br /><br /> | 
| <a href="windowsribbon-reference-properties-uipkey-keytip.md">UI_PKEY_Keytip</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-tooltipdescription.md">UI_PKEY_TooltipDescription</a> | Can only be updated through invalidation. | 
| <a href="windowsribbon-reference-properties-uipkey-tooltiptitle.md">UI_PKEY_TooltipTitle</a> | Can only be updated through invalidation. | 




 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**SplitButton markup element**](windowsribbon-element-splitbutton.md)
</dt> </dl>
