---
title: Button
description: The Button is a control the user can click to provide input to an application.
ms.assetid: 6d4aa571-dbea-4139-a6b7-45a85595dd04
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Button

The Button is a control the user can click to provide input to an application.

-   [Introduction](#introduction)
-   [Button Properties](#button-properties)
-   [Related topics](#related-topics)

## Introduction

The following screen shot contains three examples of the Ribbon Button element.

![screen shot of button controls in the microsoft wordpad ribbon.](images/controls/button.png)

## Button Properties

The Ribbon framework defines a collection of [property keys](windowsribbon-reference-properties.md) for the Button control.

Typically, a Button property is updated in the ribbon UI by invalidating the Command associated with the control through a call to the [**IUIFramework::InvalidateUICommand**](https://msdn.microsoft.com/library/windows/desktop/dd371375) method. The invalidation event is handled, and the property updates defined, by the [**IUICommandHandler::UpdateProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371494) callback method.

The [**IUICommandHandler::UpdateProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371494) callback method is not executed, and the application queried for an updated property value, until the property is required by the framework. For example, when a tab is activated and a control revealed in the ribbon UI, or when a tooltip is displayed.

> [!Note]  
> In some cases, a property can be retrieved through the [**IUIFramework::GetUICommandProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371370) method and set with the [**IUIFramework::SetUICommandProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371478) method.

 

The following table lists the property keys that are associated with the Button control.



| Property Key                                                                                             | Notes                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UI\_PKEY\_Enabled](windowsribbon-reference-properties-uipkey-enabled.md)                               | Supports [**IUIFramework::GetUICommandProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371370) and [**IUIFramework::SetUICommandProperty**](https://msdn.microsoft.com/library/windows/desktop/dd371478). |
| [UI\_PKEY\_Keytip](windowsribbon-reference-properties-uipkey-keytip.md)                                 | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md)                                   | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_LabelDescription](windowsribbon-reference-properties-uipkey-labeldescription.md)             | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_LargeHighContrastImage](windowsribbon-reference-properties-uipkey-largehighcontrastimage.md) | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_LargeImage](windowsribbon-reference-properties-uipkey-largeimage.md)                         | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_SmallHighContrastImage](windowsribbon-reference-properties-uipkey-smallhighcontrastimage.md) | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_SmallImage](windowsribbon-reference-properties-uipkey-smallimage.md)                         | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_TooltipDescription](windowsribbon-reference-properties-uipkey-tooltipdescription.md)         | Can only be updated through invalidation.                                                                                                                                                                                     |
| [UI\_PKEY\_TooltipTitle](windowsribbon-reference-properties-uipkey-tooltiptitle.md)                     | Can only be updated through invalidation.                                                                                                                                                                                     |



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Control Library](windowsribbon-controls-entry.md)
</dt> <dt>

[**Button markup element**](windowsribbon-element-button.md)
</dt> </dl>

 

 




