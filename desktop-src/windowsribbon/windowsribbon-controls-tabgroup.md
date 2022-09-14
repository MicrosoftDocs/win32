---
title: Tab Group
description: A Tab Group is a contextual control that is hidden or displayed at run time, based on a document or workspace state. The Tab Group contains a set of context-related Tab controls.
ms.assetid: 5b74ff46-2543-43f3-ab42-dab1bc67a75e
ms.topic: article
ms.date: 05/31/2018
---

# Tab Group

A Tab Group is a contextual control that is hidden or displayed at run time, based on a document or workspace state. The Tab Group contains a set of context-related [Tab](windowsribbon-controls-tab.md) controls.

-   [Details](#details)
-   [Tab Group Properties](#tab-group-properties)
-   [Related topics](#related-topics)

## Details

Typically, a Tab Group is displayed during specific document or workspace states, such as when a user selects a particular object type. For example, the selection of an image contained in the header of a table might require various contextual tabs to be displayed that expose both table and image functionality.

> [!IMPORTANT]
> A Tab Group does not support [application modes](ribbon-applicationmodes.md). However, the individual [Tab](windowsribbon-controls-tab.md) controls within a Tab Group may.

 

The following screen shot shows a contextual [Tab](windowsribbon-controls-tab.md) from Windows 7 Paint.

![screen shot that shows a contextual tab control.](images/controls/contextualtab.png)

## Tab Group Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Tab Group control.

Typically, a Tab Group property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method.

The [**IUICommandHandler::UpdateProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuicommandhandler-updateproperty) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) method and set with the [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) method.

 

The following table lists the property keys that are associated with the Tab Group control.



| Property Key                                                                                     | Notes                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UI\_PKEY\_ContextAvailable](windowsribbon-reference-properties-uipkey-contextavailable.md)     | Supports [**IUIFramework::GetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-getuicommandproperty) and [**IUIFramework::SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty). |
| [UI\_PKEY\_Keytip](windowsribbon-reference-properties-uipkey-keytip.md)                         | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md)                           | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_TooltipDescription](windowsribbon-reference-properties-uipkey-tooltipdescription.md) | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_TooltipTitle](windowsribbon-reference-properties-uipkey-tooltiptitle.md)             | Can only be updated through invalidation.                                                                                                                                                                                     |



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**TabGroup markup element**](windowsribbon-element-tabgroup.md)
</dt> </dl>

 

 