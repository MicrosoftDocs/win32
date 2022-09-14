---
title: UI Automation Control Types Overview
description: Microsoft UI Automation control types are properties that serve as well-known identifiers that indicate the kind of control that a particular UI element represents, such as a combo box or a button.
ms.assetid: 61818b64-09cb-4443-acca-4743941c48d3
keywords:
- UI Automation,control types overview
- UI Automation,UIA_LocalizedControlTypePropertyId property
- control types,about
- control types,requisites
- control types,prerequisites
- control types,predefined
- control types,UIA_LocalizedControlTypePropertyId property
- predefined control types
- UIA_LocalizedControlTypePropertyId property
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation Control Types Overview

Microsoft UI Automation control types are properties that serve as well-known identifiers that indicate the kind of control that a particular UI element represents, such as a combo box or a button. Client applications use the type to identify the capabilities of a control and to determine how to interact with it.

This topic contains the following sections:

-   [UI Automation Control Type Requisites](#ui-automation-control-type-requisites)
-   [The LocalizedControlType Property](#the-localizedcontroltype-property)
-   [Current UI Automation Control Types](#current-ui-automation-control-types)
-   [Related topics](#related-topics)

## UI Automation Control Type Requisites

Each UI Automation control type has a set of conditions associated with it. When a provider assigns a control type to a control, the provider must ensure that the control meets all of the conditions associated with that control type. The conditions include the following:

-   UI Automation control patterns: Each control type has a set of control patterns that the control must support, a set that is optional, and a set that the control must not support.
-   UI Automation property values: Each control type has a set of properties that the control must support.
-   UI Automation events: Each control type has a set of events that the control must support.
-   UI Automation tree structure: Each control type defines how the control must appear in the UI Automation tree structure.

When a control meets the conditions for a particular control type, the [**IUIAutomationElement::CurrentControlType**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentcontroltype) (or [**IUIAutomationElement::CachedControlType**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_cachedcontroltype)) property value will indicate that control type.

If your control does not meet the specifications for a particular control type, use [**UIA\_CustomControlTypeId**](uiauto-controltype-ids.md) as the control type ID, and completely describe the control by using the relevant control patterns and properties. You can also set the [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) property to a string that best describes the type of your control.

## The LocalizedControlType Property

If you use a predefined control type to describe your control, use the default value for the [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) property and allow UI Automation to provide a localized string for providers to expose properly. If you cannot use a predefined control type to describe your control, set the **UIA\_LocalizedControlTypePropertyId** property to a localized string that accurately describes the type of your control. The string should be concise, yet accurate enough that an assistive technology such as a screen reader can use it in the UI to inform the user of the control's type.

## Current UI Automation Control Types

The following topics describe the UI Automation control types. For each control type, the description includes the set of conditions that a control of the given type must support:

-   AppBar Control Type
-   [Button Control Type](uiauto-supportbuttoncontroltype.md)
-   [Calendar Control Type](uiauto-supportcalendarcontroltype.md)
-   [CheckBox Control Type](uiauto-supportcheckboxcontroltype.md)
-   [ComboBox Control Type](uiauto-supportcomboboxcontroltype.md)
-   [DataGrid Control Type](uiauto-supportdatagridcontroltype.md)
-   [DataItem Control Type](uiauto-supportdataitemcontroltype.md)
-   [Document Control Type](uiauto-supportdocumentcontroltype.md)
-   [Edit Control Type](uiauto-supporteditcontroltype.md)
-   [Group Control Type](uiauto-supportgroupcontroltype.md)
-   [Header Control Type](uiauto-supportheadercontroltype.md)
-   [HeaderItem Control Type](uiauto-supportheaderitemcontroltype.md)
-   [Hyperlink Control Type](uiauto-supporthyperlinkcontroltype.md)
-   [Image Control Type](uiauto-supportimagecontroltype.md)
-   [List Control Type](uiauto-supportlistcontroltype.md)
-   [ListItem Control Type](uiauto-supportlistitemcontroltype.md)
-   [Menu Control Type](uiauto-supportmenucontroltype.md)
-   [MenuBar Control Type](uiauto-supportmenubarcontroltype.md)
-   [MenuItem Control Type](uiauto-supportmenuitemcontroltype.md)
-   [Pane Control Type](uiauto-supportpanecontroltype.md)
-   [ProgressBar Control Type](uiauto-supportprogressbarcontroltype.md)
-   [RadioButton Control Type](uiauto-supportradiobuttoncontroltype.md)
-   [ScrollBar Control Type](uiauto-supportscrollbarcontroltype.md)
-   [SemanticZoom Control Type](/windows/desktop/WinAuto/uiauto-supportsemanticzoomcontroltype)
-   [Separator Control Type](uiauto-supportseparatorcontroltype.md)
-   [Slider Control Type](uiauto-supportslidercontroltype.md)
-   [Spinner Control Type](uiauto-supportspinnercontroltype.md)
-   [SplitButton Control Type](uiauto-supportsplitbuttoncontroltype.md)
-   [StatusBar Control Type](uiauto-supportstatusbarcontroltype.md)
-   [Tab Control Type](uiauto-supporttabcontroltype.md)
-   [TabItem Control Type](uiauto-supporttabitemcontroltype.md)
-   [Table Control Type](uiauto-supporttablecontroltype.md)
-   [Text Control Type](uiauto-supporttextcontroltype.md)
-   [Thumb Control Type](uiauto-supportthumbcontroltype.md)
-   [TitleBar Control Type](uiauto-supporttitlebarcontroltype.md)
-   [ToolBar Control Type](uiauto-supporttoolbarcontroltype.md)
-   [ToolTip Control Type](uiauto-supporttooltipcontroltype.md)
-   [Tree Control Type](uiauto-supporttreecontroltype.md)
-   [TreeItem Control Type](uiauto-supporttreeitemcontroltype.md)
-   [Window Control Type](uiauto-supportwindowcontroltype.md)

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Control Type Identifiers](uiauto-controltype-ids.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Supporting UI Automation Control Types](uiauto-supportinguiautocontroltypes.md)
</dt> <dt>

[UI Automation Support for Standard Controls](uiauto-controlsupport.md)
</dt> <dt>

[UI Automation Fundamentals](entry-uiautocore-overview.md)
</dt> </dl>

 

 