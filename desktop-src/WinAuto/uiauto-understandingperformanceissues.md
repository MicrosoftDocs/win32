---
title: Understanding Performance Issues When Using the Text and TextRange Control Patterns.
description: This topic describes performance issues associated with using the Text and TextRange control patterns.
ms.assetid: D78BFFA8-E303-441D-9D32-AD22E1B1A249
keywords:
- clients,understanding performance issues
- clients,text-based controls
- clients,text ranges
- clients,Text control pattern
- clients,TextRange control pattern
ms.topic: article
ms.date: 12/09/2022
---

# Understanding Performance Issues When Using the Text and TextRange Control Patterns

This topic describes performance issues associated with using the [**Text**](/windows/win32/api/uiautomationclient/nn-uiautomationclient-iuiautomationtextpattern) and [**TextRange**](/windows/win32/api/uiautomationclient/nn-uiautomationclient-iuiautomationtextrange) control patterns.

The [**IUIAutomationTextPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtextpattern) and [**IUIAutomationTextRange**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtextrange) interfaces rely on cross-process calls—they do not provide a caching mechanism to improve performance when retrieving or processing textual content.

A client application can improve performance by using the [**IUIAutomationTextRange::GetText**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-gettext) method to retrieve moderately sized blocks of text. For example, using **GetText** to retrieve single characters will incur a cross-process performance hit for each character, whereas not specifying a maximum length when calling **GetText** will incur one cross-process hit, but can have high latency depending on the size of the text range.

## Related topics

[Working with Text-based Controls](uiauto-workingwithtextbasedcontrols.md), [UI Automation Support for Textual Content](/windows/win32/winauto/uiauto-ui-automation-textpattern-overview), [About the Text and TextRange Control Patterns](/windows/win32/winauto/uiauto-about-text-and-textrange-patterns), [UI Automation Client Programmer's Guide](uiauto-clientportal.md)

For UI Automation Providers, see [Text and TextRange Control Patterns](uiauto-implementingtextandtextrange.md)
