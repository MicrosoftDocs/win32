---
title: Help Button
description: The Help Button is a control that the user can click to display the application help system.
ms.assetid: 5f08a8b2-bc83-4256-bcc4-aecfbd07ea51
ms.topic: article
ms.date: 05/31/2018
---

# Help Button

The Help Button is a control that the user can click to display the application help system.

-   [Details](#details)
-   [Help Button Properties](#help-button-properties)
-   [Related topics](#related-topics)

## Details

The following screen shot illustrates the Ribbon Help Button.

![screen shot showing the help button.](images/controls/helpbutton.png)

## Help Button Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Help Button control.

Typically, a Help Button property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) method and set with the [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method.

 

The following table lists the property keys that are associated with the Help Button control.



| Property Key                                                                                     | Notes                                     |
|--------------------------------------------------------------------------------------------------|-------------------------------------------|
| [UI\_PKEY\_Keytip](windowsribbon-reference-properties-uipkey-keytip.md)                         | Can only be updated through invalidation. |
| [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md)                           | Can only be updated through invalidation. |
| [UI\_PKEY\_TooltipDescription](windowsribbon-reference-properties-uipkey-tooltipdescription.md) | Can only be updated through invalidation. |
| [UI\_PKEY\_TooltipTitle](windowsribbon-reference-properties-uipkey-tooltiptitle.md)             | Can only be updated through invalidation. |



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**HelpButton element**](windowsribbon-element-helpbutton.md)
</dt> </dl>

 

 