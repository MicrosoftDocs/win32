---
title: Transform Control Pattern
description: Describes guidelines and conventions for implementing ITransformProvider and ITransformProvider2, including information about properties and methods.
ms.assetid: e1d862a0-8085-42b4-9710-cf11e1a467cf
keywords:
- UI Automation,implementing Transform control pattern
- UI Automation,Transform control pattern
- UI Automation,ITransformProvider
- ITransformProvider
- implementing UI Automation Transform control patterns
- Transform control patterns
- control patterns,ITransformProvider
- control patterns,implementing UI Automation Transform
- control patterns,Transform
- interfaces,ITransformProvider
ms.topic: article
ms.date: 05/31/2018
---

# Transform Control Pattern

Describes guidelines and conventions for implementing [**ITransformProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itransformprovider) and [**ITransformProvider2**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-itransformprovider2), including information about properties and methods. The Transform control pattern is used to support controls that can be moved, resized, or rotated within a two-dimensional space.

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **ITransformProvider**](#required-members-for-itransformprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **Transform** control pattern, note the following guidelines and conventions:

-   Support for this control pattern is not limited to objects on the desktop. This control pattern must also be supported by the children of a container object if the children can be moved, resized, or rotated freely within the boundaries of the container.
-   An object cannot be moved, resized, or rotated such that its resulting screen location would be completely outside the coordinates of its container and therefore inaccessible to the keyboard or mouse (for example, when a top-level window is moved off-screen or a child object is moved outside the boundaries of the container's viewport). In these cases, the object is placed as close to the requested screen coordinates as possible with the top or left coordinates overridden to be within the container boundaries.
-   For multi-monitor systems, if an object is moved, resized, or rotated completely outside the combined desktop screen coordinates, the object is placed on the primary monitor as close to the requested coordinates as possible.
-   All parameters and property values are absolute and independent of locale.

## Required Members for **ITransformProvider**

The following properties and methods are required for implementing the [**ITransformProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itransformprovider) interface.



| Required members                                         | Member type | Notes |
|----------------------------------------------------------|-------------|-------|
| [**CanMove**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider-get_canmove)     | Property    | None  |
| [**CanResize**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider-get_canresize) | Property    | None  |
| [**CanRotate**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider-get_canrotate) | Property    | None  |
| [**Move**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider-move)           | Method      | None  |
| [**Resize**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider-resize)       | Method      | None  |
| [**Rotate**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider-rotate)       | Method      | None  |



 

The following additional properties and methods are required for implementing the [**ITransformProvider2**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itransformprovider) interface.



| Required members                                              | Member type | Notes |
|---------------------------------------------------------------|-------------|-------|
| [**CanZoom**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-itransformprovider2-get_canzoom)     | Property    | None  |
| [**Zoom**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-itransformprovider2-zoom)           | Method      | None  |
| [**ZoomByUnit**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider2-zoombyunit)   | Method      | None  |
| [**ZoomLevel**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider2-get_zoomlevel)     | Property    | None  |
| [**ZoomMaximum**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider2-get_zoommaximum) | Property    | None  |
| [**ZoomMinimum**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itransformprovider2-get_zoomminimum) | Property    | None  |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 