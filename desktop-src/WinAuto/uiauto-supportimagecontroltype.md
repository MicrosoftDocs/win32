---
title: Image Control Type
description: This topic provides information about Microsoft UI Automation support for the Image control type.
ms.assetid: 439c708c-4fb4-481b-a2ff-3816d649f3ff
keywords:
- UI Automation,support for Image control type
- UI Automation,Image control type
- UI Automation,tree structure for Image control type
- UI Automation,properties for Image control type
- UI Automation,control patterns for Image control type
- UI Automation,events for Image control type
- tree structures,Image control type
- properties,Image control type
- control patterns,Image control type
- events,Image control type
- support for Image control type
- Image control type
- control types,tree structure for Image control type
- control types,control patterns for Image control type
- control types,support for Image
- control types,Image
ms.topic: article
ms.date: 10/08/2019
---

# Image Control Type

This topic provides information about Microsoft UI Automation support for the **Image** control type.

Image controls used as icons, informational graphics, and charts will support the **Image** control type. Controls used as background or watermark images will not support the **Image** control type.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Image** control type. The UI Automation requirements apply to all image controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

- [Typical Tree Structure](#typical-tree-structure)
- [Relevant Properties](#relevant-properties)
- [Required Control Patterns](#required-control-patterns)
- [Required Events](#required-events)
- [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to image controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).

| Control view | Content view |
| ------------ | ------------ |
| Image | Image (Depends whether the image contains information, based on the value of the [Automation Element Property Identifiers](uiauto-automation-element-propids.md) property) |

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the image controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).

| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes. | The image control's clickable point must be a point within the bounding rectangle of the image control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Image**  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [**UIA\_HelpTextPropertyId**](uiauto-automation-element-propids.md)                         | See notes. | The **HelpText** property exposes a localized string which describes the actual visual appearance of the control or other tooltip information associated with the image. This property must be supported when a long description is needed to convey more information about the image control (for example, if the image is a complicated chart or diagram). This property maps to the HTML **LongDesc** tag and the Scalable Vector Graphics (SVG) **Desc** tag. Developers working with image controls must support a property to allow the visual description to be set on the control. This property must be mapped to the UI Automation **VisualDescription** property. |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | See notes. | The image control must be included in the content view of the UI Automation tree when it contains meaningful information not already exposed to the end user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | The image control is always included in the control view of the UI Automation tree.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes. | If the control can receive keyboard focus, it must support this property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**UIA\_ItemStatusPropertyId**](uiauto-automation-element-propids.md)                     | See notes. | If the image control represents state information about a particular item on the screen, the control should be contained within the item. When the image is contained within an item, the item must support the status property and raise appropriate notifications when the status changes. If an image is a standalone control and is conveying status this property must be supported.                                                                                                                                                                                                                                                                                    |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes. | If there is a static text label, this property must expose a reference to that control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes. | Localized string corresponding to the **Image** control type. The default value is "image" for en-US or English (United States).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes. | The **Name** property must be exposed for all image controls that contain information. Programmatic access to this information requires that a textual equivalent to the graphic be provided. If the image control is purely decorative, it must only show up in the control view of the UI Automation tree and is not required to have a name (see [Remarks](#remarks)). UI frameworks must support an ALT or alternate text property on images that can be set from within their framework. This property will then map to the UI Automation Name property.                                                                                                                                                     |

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported for image controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).

| Control Pattern                                                 | Support | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IGridItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igriditemprovider)           | Depends | The image control supports the [GridItem](uiauto-implementinggriditem.md) control pattern if the control is within a grid container.                                                                                                                                                                                                                                                                                                                      |
| [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider)               | Never   | If the image control is a clickable object, the control should support a control type that supports the [Invoke](uiauto-implementinginvoke.md) control pattern, such as the [Button](uiauto-supportbuttoncontroltype.md) control type. For an image object that contains multiple clickable objects, the element (Image control type) may host child links ([Hyperlink](uiauto-supporthyperlinkcontroltype.md) control type) in the UI Automation tree. |
| [**ISelectionItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider) | Never   | Image controls should not support the [SelectionItem](uiauto-implementingselectionitem.md) control pattern. If images are part of a container that is selectable such as a button that has an image icon as content, that container supports the pattern, not the image within.                                                                                                                                                                           |
| [**ITableItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itableitemprovider)         | Depends | The image control supports the [TableItem](uiauto-implementingtableitem.md) control pattern if the control is within a container that has header controls.                                                                                                                                                                                                                                                                                                |

## Required Events

The following table lists the UI Automation events that image controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).

| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_ItemStatusPropertyId**](uiauto-automation-element-propids.md) property-changed event.               | If the control supports the [**ItemStatus**](uiauto-automation-element-propids.md) property, it must support this event.  |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) property-changed event.                           |                                                                                                                            |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |

## Remarks

The World Wide Web Consortium (W3C) defines a decorative image as one that doesn’t add information to the content of a page. For more detail see the W3C topic on [decorative images](https://www.w3.org/WAI/tutorials/images/decorative/).

With respect to UI Automation:

- If an image is purely decorative, is not interactive, and conveys no information, the image:
  - Might or might not be in the UIA tree
  - Might or might not be in the UIA raw view
  - Must not be in the UIA control view
  - Must not be in the content view
  - Might or might not have a name
- If an image conveys information, but there is clearly associated text that provides the same information (such as a play button that contains a left-pointing triangle graphic along with the text "play"), the image is considered decorative and the image:
  - Must be in the raw view
  - Must be in the control view
  - Must not be in the content view
  - Might or might not have a value in the Name property
  - The text that also conveys the meaning of the image must be in the content view
- If an image is informative and conveys detail that is not provided by any associated text, the image:
  - Must be in the raw view
  - Must be in the control view
  - Must be in the content view
  - Must have a name value that describes the image and its meaning

## Related topics

### Conceptual

- [UI Automation Control Types Overview](uiauto-controltypesoverview.md)
- [UI Automation Overview](uiauto-uiautomationoverview.md)
