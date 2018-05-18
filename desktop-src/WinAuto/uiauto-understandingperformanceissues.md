---
title: Understanding Performance Issues
description: This topic describes performance issues associated with using the Text and TextRange control patterns.
ms.assetid: 'D78BFFA8-E303-441D-9D32-AD22E1B1A249'
keywords: ["clients,understanding performance issues", "clients,text-based controls", "clients,text ranges", "clients,Text control pattern", "clients,TextRange control pattern"]
---

# Understanding Performance Issues

This topic describes performance issues associated with using the [Text and TextRange](uiauto-implementingtextandtextrange.md) control patterns.

## 

The [**IUIAutomationTextPattern**](uiauto-iuiautomationtextpattern.md) and [**IUIAutomationTextRange**](uiauto-iuiautomationtextrange.md) interfaces rely on cross-process calls—they do not provide a caching mechanism to improve performance when retrieving or processing textual content.

A client application can improve performance by using the [**IUIAutomationTextRange::GetText**](uiauto-iuiautomationtextrange-gettext.md) method to retrieve moderately sized blocks of text. For example, using **GetText** to retrieve single characters will incur a cross-process performance hit for each character, whereas not specifying a maximum length when calling **GetText** will incur one cross-process hit, but can have high latency depending on the size of the text range.

## Related topics

<dl> <dt>

[Text and TextRange Control Patterns](uiauto-implementingtextandtextrange.md)
</dt> <dt>

[UI Automation Support for Textual Content](uiauto-ui-automation-textpattern-overview.md)
</dt> <dt>

[Working with Text-based Controls](uiauto-workingwithtextbasedcontrols.md)
</dt> </dl>

 

 




