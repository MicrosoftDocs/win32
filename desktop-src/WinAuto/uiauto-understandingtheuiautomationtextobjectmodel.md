---
title: Understanding the UI Automation Text Object Model
description: This topic describes how Microsoft UI Automation client applications access the textual content of a text-based control.
ms.assetid: 8545EBA3-6995-4336-A197-27CE3A3339EE
keywords:
- clients,understanding UI Automation text object model
- clients,text-based controls
- clients,text ranges
- clients,Text control pattern
- clients,TextRange control pattern
ms.topic: article
ms.date: 05/31/2018
---

# Understanding the UI Automation Text Object Model

This topic describes how Microsoft UI Automation client applications access the textual content of a text-based control.

-   [Control-specific Object Model](#control-specific-object-model)
-   [Related topics](#related-topics)

Text-based controls expose textual content to UI Automation client applications through a simple text object model. Client applications have access to the text object model through the [Text and TextRange](uiauto-about-text-and-textrange-patterns.md) control pattern interfaces, including [**IUIAutomationTextPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtextpattern) and [**IUIAutomationTextRange**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtextrange). Client applications can use these interfaces to retrieve textual content, text attributes, and embedded objects such as tables and hyperlinks from text-based controls.

Control types that support the UI Automation text object model include the [Edit](uiauto-supporteditcontroltype.md) and [Document](uiauto-supportdocumentcontroltype.md) control types. Other control types such as [ToolTip](uiauto-supporttooltipcontroltype.md) and [Text](uiauto-supporttextcontroltype.md) might also support the text object model, but they are not required to.

> [!Note]  
> The UI Automation text object model does not provide a means to insert or modify text. However, some controls enable text to be inserted or modified either through the [**IUIAutomationValuePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationvaluepattern) interface, or through direct keyboard input.

 

## Control-specific Object Model

A text-based control that implements its own Document Object Model (DOM) can expose the DOM by implementing the [ObjectModel](uiauto-implementingobjectmodel.md) control pattern. Exposing the DOM can give client applications greater access to, and control over, the content of a text-based control.

A client application can discover whether a particular text-based control implements a DOM by retrieving the control's [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface. Then, call the [**IUIAutomationElement::GetCurrentPropertyValue**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpropertyvalue) method, specifying the [**UIA\_IsObjectModelPatternAvailablePropertyId**](uiauto-control-pattern-availability-propids.md) property identifier, and a variant that receives TRUE if the control implements a DOM.

To access the DOM, call the [**IUIAutomationElement::GetCurrentPattern**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpattern) method, specifying the [**UIA\_ObjectModelPatternId**](uiauto-controlpattern-ids.md) control pattern identifier and a variable that receives the [**IUIAutomationObjectModelPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationobjectmodelpattern) interface. Call the [**IUIAutomationObjectModelPattern::GetUnderlyingObjectModel**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationobjectmodelpattern-getunderlyingobjectmodel) method to retrieve the DOM interface.

## Related topics

<dl> <dt>

[Text and TextRange Control Patterns](uiauto-implementingtextandtextrange.md)
</dt> <dt>

[UI Automation Support for Textual Content](uiauto-ui-automation-textpattern-overview.md)
</dt> <dt>

[Working with Text-based Controls](uiauto-workingwithtextbasedcontrols.md)
</dt> </dl>

 

 




