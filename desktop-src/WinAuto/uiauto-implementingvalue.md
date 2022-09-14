---
title: Value Control Pattern
description: Describes guidelines and conventions for implementing IValueProvider, including information about properties and methods.
ms.assetid: 6b11d281-aca7-4548-853c-e7322999825d
keywords:
- UI Automation,implementing Value control pattern
- UI Automation,Value control pattern
- UI Automation,IValueProvider
- IValueProvider
- implementing UI Automation Value control patterns
- Value control patterns
- control patterns,IValueProvider
- control patterns,implementing UI Automation Value
- control patterns,Value
- interfaces,IValueProvider
ms.topic: article
ms.date: 05/31/2018
---

# Value Control Pattern

Describes guidelines and conventions for implementing [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider), including information about properties and methods. The **Value** control pattern is used to support controls that have an intrinsic value not spanning a range and that can be represented as a string.

The value string can be editable, depending on the control and its settings. For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IValueProvider**](#required-members-for-ivalueprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **Value** control pattern, note the following guidelines and conventions:

-   Controls such as a list item or tree item must support the **Value** control pattern if the value of any of the items is editable, regardless of the current edit mode of the control. The parent control must also support the **Value** control pattern if the child items are editable. The following image shows an example of an editable list item.

    ![illustration showing editable list item](images/uia-valuepattern-editable-listitem.jpg)

- Single and multi-line edit controls must implement [**ITextProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextprovider) to expose their read-only content.
- Multi-line edit controls must implement [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider) if their contents can be changed.
- [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider) does not support the retrieval of formatting information or substring values. Implement [**ITextProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextprovider) in these scenarios.
- [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider) must be implemented by controls such as the color picker selection control from Microsoft Word (see the following image), which supports string mapping between a color value (for example, "yellow") and an equivalent internal [RGB](/windows/win32/api/wingdi/nf-wingdi-rgb) value.

    ![illustration showing color swatch string mapping](images/uia-valuepattern-colorpicker.jpg)

- A control should have its **IsEnabled** property set to **TRUE** and its [**ITextProvider::IsReadOnly**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-get_isreadonly) property set to **FALSE** before allowing a call to [**ITextProvider::SetValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-setvalue).

## Required Members for **IValueProvider**

The following properties and methods are required for implementing the [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider) interface.



| Required members                                       | Member type | Notes |
|--------------------------------------------------------|-------------|-------|
| [**IsReadOnly**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-get_isreadonly) | Property    | None  |
| [**Value**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-get_value)           | Property    | None  |
| [**SetValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-setvalue)     | Method      | None  |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> <dt>

[Text and TextRange Control Patterns](uiauto-implementingtextandtextrange.md)
</dt> </dl>

 

 