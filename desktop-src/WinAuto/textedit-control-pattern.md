---
title: TextEdit Control Pattern
description: Introduces guidelines and conventions for implementing ITextEditProvider, including information about properties and methods.
ms.assetid: AA9E04AC-1AC0-6434-ADEF-9FF82ADA7CD9
keywords:
- UI Automation,implementing TextEdit control pattern
- UI Automation,TextEdit control pattern
- control patterns,TextEdit
ms.topic: article
ms.date: 05/31/2018
---

# TextEdit Control Pattern

Introduces guidelines and conventions for implementing [**ITextEditProvider**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-itexteditprovider), including information about properties and methods. The **TextEdit** control pattern is used for programmatic access to a control that modifies text, for example a control that performs auto-correction or enables input composition.

> [!Note]  
> Implementation notes in this topic refer to APIs that come from Text Services Framework (TSF). For more info about TSF and the API reference, see [Text Services Framework](/windows/desktop/TSF/text-services-framework).

 

## Required Members for **ITextEditProvider**

These properties and methods are required for implementing the [**ITextEditProvider**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-itexteditprovider) interface.



| Required members                                                              | Member type | Notes                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetActiveComposition**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itexteditprovider-getactivecomposition) | Method      | Returns the range of the current conversion (none if there is no conversion). Return the active composition (in TSF, this is the range marked by **GUID\_PROP\_COMPOSING**). For example with the Microsoft Japanese Input Method Editor (IME), this would be the full underlined text. |
| [**GetConversionTarget**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itexteditprovider-getconversiontarget)   | Method      | Returns the current conversion target range (none if no conversion). In TSF, this is the range of characters marked as **TF\_ATTR\_TARGET\_NOTCONVERTED** or **TF\_ATTR\_TARGET\_CONVERTED** from the **TF\_DISPLAYATTRIBUTE** structure.                                               |



 

The **TextEditTextChanged** and **ConversionTargetChanged** events are required to be raised by Microsoft UI Automation elements supporting the **TextEdit** pattern.

### **TextEditTextChanged**

-   Use the [**UiaRaiseTextEditTextChangedEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraisetextedittextchangedevent) function to raise the **TextEditTextChanged** event.
-   The following table lists the cases when you should raise the event and the [**UiaRaiseTextEditTextChangedEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraisetextedittextchangedevent) parameters to use.



| TextEditChangeType                                            | Event Payload                                | Notes                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AutoCorrect**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-texteditchangetype)          | New corrected string                         | Raised when an auto-correction is made by the control. Or whenever a replacement is made through TSF and the range has a **GUID\_PROP\_TKB\_ALTERNATES** value of **TKB\_ALTERNATES\_AUTOCORRECTION\_APPLIED**.<br/>                                                                                                                                                                   |
| [**Composition**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-texteditchangetype)          | The updated string                           | The payload must only include the characters that changed (do not send the entire composition string). Raised whenever a composition replacement is made. In TSF, a composition replacement is defined as a replacement that has the **GUID\_PROP\_COMPOSING** flag set. Edit controls implementing TSF can monitor for these changes via the **OnEndEdit** notification.<br/>         |
| [**CompositionFinalized**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-texteditchangetype) | The finalized composition string (see Notes) | In TSF, the conversion string being finalized is defined by the **GUID\_PROP\_COMPOSING** flag being removed from a composition. Edit controls implementing TSF should determine the finalized string from **EndComposition** and raise the event when **OnEndEdit** is called.<br/> The finalized composition string may be empty if composition was cancelled or deleted.<br/> |



 

### **ConversionTargetChanged**

-   **ConversionTargetChanged** occurs when conversion target changes from one target to another.
-   Use the [**UiaRaiseAutomationEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraiseautomationevent) function to raise the **ConversionTargetChanged** event (pass the [**UIA\_TextEdit\_ConversionTargetChangedEventId**](https://www.bing.com/search?q=**UIA\_TextEdit\_ConversionTargetChangedEventId**) event identifier).
-   **ConversionTargetChanged** should not be raised when the content of the target changes. If the target change occurs simultaneous with a composition change, the target change event must be raised after any composition events have already been raised.
-   In TSF, the conversion target is defined by the value **TF\_ATTR\_TARGET\_CONVERTED** being set from the **TF\_DISPLAYATTRIBUTE** structure. Changes can be monitored using **OnEndEdit**.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

