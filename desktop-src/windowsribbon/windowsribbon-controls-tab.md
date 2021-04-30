---
title: Tab (Windows Ribbon Framework)
description: A Tab contains groups of related controls.
ms.assetid: 7315ca96-73c8-4ea1-bce0-172ebc4dd43a
ms.topic: article
ms.date: 05/31/2018
---

# Tab (Windows Ribbon Framework)

A Tab contains [groups](windowsribbon-controls-group.md) of related controls.

-   [Details](#details)
-   [Tab Properties](#tab-properties)
-   [Related topics](#related-topics)

## Details

There are three types of Tab in the Ribbon framework.



| Type               | Description                                                                                                                                                                                                                                                                         |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Core tab**       | Core tabs that organize the default functions of the application.                                                                                                                                                                                                                   |
| **Contextual tab** | Tabs that are displayed during specific document or workspace states. For example, if a user selects a particular object type, such as an image contained in the header of a table, then various contextual tabs might be displayed that expose both table and image functionality. |
| **Modal tab**      | Core tabs that are displayed during a specific document or workspace [application mode](ribbon-applicationmodes.md), such as print preview.                                                                                                                                        |



 

The following screen shot shows a core Tab from Windows 7 Paint.

![screen shot that shows a core tab control.](images/controls/coretab.png)

## Tab Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Tab control.

Typically, a Tab property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) method and set with the [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method.

 

The following table lists the property keys that are associated with the Tab control.



| Property Key                                                                                     | Notes                                     |
|--------------------------------------------------------------------------------------------------|-------------------------------------------|
| [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md)                           | Can only be updated through invalidation. |
| [UI\_PKEY\_Keytip](windowsribbon-reference-properties-uipkey-keytip.md)                         | Can only be updated through invalidation. |
| [UI\_PKEY\_TooltipDescription](windowsribbon-reference-properties-uipkey-tooltipdescription.md) | Can only be updated through invalidation. |
| [UI\_PKEY\_TooltipTitle](windowsribbon-reference-properties-uipkey-tooltiptitle.md)             | Can only be updated through invalidation. |



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**Tab markup element**](windowsribbon-element-tab.md)
</dt> </dl>

 

 
