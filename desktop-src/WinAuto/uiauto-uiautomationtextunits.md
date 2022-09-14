---
title: UI Automation Text Units
description: This topic describes the text units supported by the Microsoft UI Automation \ 32;TextRange control pattern. UI Automation providers and clients use text units to specify the amount by which to move or change the size of a text range.
ms.assetid: 3ec43a81-c4f1-4c73-865f-a60c751fc3fb
keywords:
- UI Automation,text units
- text units,about
- UI Automation,list of text units
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation text units

This topic describes the text units supported by the Microsoft UI Automation [TextRange](uiauto-implementingtextandtextrange.md) control pattern. UI Automation providers and clients use text units to specify the amount by which to move or change the size of a text range.

-   [Text Unit API Elements](#text-unit-api-elements)
-   [Text Unit Descriptions](#text-unit-descriptions)
    -   [Character](#character)
    -   [Format](#format)
    -   [Word](#word)
    -   [Line](#line)
    -   [Paragraph](#paragraph)
    -   [Page](#page)
    -   [Document](#document)
-   [Other Potential Ranges](#other-potential-ranges)
-   [Related topics](#related-topics)

## Text unit API elements

The UI Automation API includes the following methods that require a text unit to be specified:

-   [**ITextRangeProvider::Move**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-move)
-   [**ITextRangeProvider::ExpandToEnclosingUnit**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-expandtoenclosingunit)
-   [**ITextRangeProvider::MoveEndpointByUnit**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-moveendpointbyunit)
-   [**IUIAutomationTextRange::Move**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-move)
-   [**IUIAutomationTextRange::ExpandToEnclosingUnit**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-expandtoenclosingunit)
-   [**IUIAutomationTextRange::MoveEndpointByUnit**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-moveendpointbyunit)

The [**TextUnit**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) enumeration defines the text units that are supported by UI Automation text ranges. To specify the text unit, a member of the [**TextUnit**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) enumeration is specified in a call to an [**ITextRangeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextrangeprovider) or [**IUIAutomationTextRange**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtextrange) method. The text units, from smallest to largest, are as follows:

-   [**TextUnit\_Character**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit)
-   [**TextUnit\_Format**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit)
-   [**TextUnit\_Word**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit)
-   [**TextUnit\_Line**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit)
-   [**TextUnit\_Paragraph**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit)
-   [**TextUnit\_Page**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit)
-   [**TextUnit\_Document**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit)

If a particular text-based control does not support the specified text unit, the provider should respond by substituting the next larger text unit that is supported by the control. For example, if [**TextUnit\_Paragraph**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) is specified but not supported, the method can substitute [**TextUnit\_Page**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) or [**TextUnit\_Document**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit).

The linguistic characteristics of the source text can make it difficult for a provider to determine text boundaries based on the specified text unit. For help in determining text boundaries, a provider can use Uniscribe API functions such as [**ScriptBreak**](/windows/desktop/api/usp10/nf-usp10-scriptbreak). For more information, see [Uniscribe](/windows/desktop/Intl/uniscribe) on the MSDN website.

## Endpoint inclusivity

A text unit endpoint can serve as both a [Start](/windows/desktop/api/uiautomationcore/ne-uiautomationcore-textpatternrangeendpoint) endpoint and an [End](/windows/desktop/api/uiautomationcore/ne-uiautomationcore-textpatternrangeendpoint) endpoint for adjacent text ranges of the same type. If the end of one text unit is also the start of another text unit, the range containing the [End](/windows/desktop/api/uiautomationcore/ne-uiautomationcore-textpatternrangeendpoint) endpoint does not share any attributes or objects of the adjacent range containing the [Start](/windows/desktop/api/uiautomationcore/ne-uiautomationcore-textpatternrangeendpoint) endpoint.

For example, a text stream, "Hello **world**", contains two word units with different font weight attributes (normal and bold). In this case, the [End](/windows/desktop/api/uiautomationcore/ne-uiautomationcore-textpatternrangeendpoint) endpoint of the word unit "Hello" and the [Start](/windows/desktop/api/uiautomationcore/ne-uiautomationcore-textpatternrangeendpoint) endpoint of the word unit "**world**" are the same, which results in the following:

- The range of "Hello" does not share the bold attribute of the word unit "world" and does not return the mixed attribute value for the font weight text attribute.
- The range of "**world**" has a single font weight (bold), and does not share the font weight of the preceding word unit “Hello”.

Here's another example where a text stream contains two word units, one of which is a link: `[Foo]() Bar`. In this case, the [End](/windows/desktop/api/uiautomationcore/ne-uiautomationcore-textpatternrangeendpoint) endpoint of the word unit `[Foo]()` and the [Start](/windows/desktop/api/uiautomationcore/ne-uiautomationcore-textpatternrangeendpoint) endpoint of the word unit "Bar" are the same, which results in the following:

- The link belongs to the text range containing "Foo".
- The link is a child of the text range "Foo", and is enclosed by the [ITextProvider](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-itextprovider).
- The text range "Bar" has no children and and is enclosed by the [ITextProvider](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-itextprovider).

**Additional notes:**

> A degenerate (empty) range at a text unit boundary with a text range of the same type assumes properties of the immediately adjacent text unit.
>
> Calling [IUIAutomationTextRange::ExpandToEnclosingUnit](/windows/desktop/api/uiautomationclient/nf-uiautomationclient-iuiautomationtextrange-expandtoenclosingunit
) on a degenerate range at a text unit boundary with a text range of the same type, expands the degenerate range to the following text unit.

## Text Unit Descriptions

This section describes each of the text units supported by UI Automation.

### Character

[**TextUnit\_Character**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) is a linguistic unit of text that represents a single character. The linguistic definition of a character varies by language. For US English, a character is typically bordered by a space or another character, such as a punctuation mark, a number, or a letter.

Control characters such as carriage returns and the Unicode left-to-right mark (LTM) should not be considered as characters, but may be included in a text range that is normalized based on the character text unit.

Punctuation marks and word break characters such as spaces should be considered as characters.

### Format

[**TextUnit\_Format**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) is used to position the boundary of a text range based on the formatting attributes of the text. For example, if a text range is currently positioned on a single character of a word, specifying **TextUnit\_Format** in a call to [**IUIAutomationTextRange::ExpandToEnclosingUnit**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-expandtoenclosingunit) expands the text range to include all text that shares all the same attributes as the single character. The resulting text range might or might not include the entire word. Also, using the format text unit will not expand a text range across the boundary of an embedded object such as an image or hyperlink.

Unlike the other text units, which include the text units that are smaller than themselves, [**TextUnit\_Format**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) can be smaller or larger than the other units. For example, if an entire document shares the same text attributes and contains no embedded objects, expanding a text range by **TextUnit\_Format** would create a new range that encompasses the entire document, while expanding the text range by [**TextUnit\_Word**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) would create a smaller range.

### Word

[**TextUnit\_Word**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) is a linguistic unit of text that represents a single, whole word. The linguistic definition of a word varies by language. For US English, words are typically bordered by spaces or punctuation characters.

When [**TextUnit\_Word**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) is used to set the boundary of a text range, the resulting text range should include any word break characters that are present at the end of the word, but before the start of the next word.

### Line

[**TextUnit\_Line**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) is a unit of text that represents a single line of text as presented in the viewport of the control. When using **TextUnit\_Line** to set the boundary of a text range, a provider should set the boundary immediately after the point where a control character breaks the line, or where the viewport of the control wraps the text to a new line. The boundary should be set where a new line starts.

### Paragraph

[**TextUnit\_Paragraph**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) is a linguistic unit of text that represents a complete paragraph. A paragraph should begin just before the first character of a paragraph and should typically end just after the last character. Any empty lines following a paragraph should be merged into the paragraph, unless something in the text source indicates otherwise. Typically, the end boundary of a paragraph also marks the end boundary of a [**TextUnit\_Line**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) text unit.

### Page

[**TextUnit\_Page**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) represents a complete text page of a document. The boundaries of a page should be set at the immediate points where a page starts and ends.

### Document

[**TextUnit\_Document**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) represents the entire contents of a document as supported by the [Text](uiauto-implementingtextandtextrange.md) control pattern. No text should exist outside of a text range that contains a document. Any objects that are inserted into a document, such as annotation notes that cross a page boundary, should be treated as embedded objects of the document and not part of the document's text content.

## Other Potential Ranges

The current [TextRange](uiauto-implementingtextandtextrange.md) control pattern specification does not allow new text unit values to be added to the [**TextUnit**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) enumeration, nor does it allow the existing text unit values to be redefined. To expose other potential ranges, such as headers and annotations, a provider should expose these ranges as embedded objects with an associated text range. That way, you can also add support for the appropriate control patterns. This solution is more flexible and extensible than defining new text units.

## Related topics

### Reference

[TextPatternRangeEndpoint](/windows/desktop/api/uiautomationcore/ne-uiautomationcore-textpatternrangeendpoint)

[ITextRangeProvider::GetChildren](/windows/win32/api/uiautomationcore/nf-uiautomationcore-itextrangeprovider-getchildren)

### Conceptual

[UI Automation Support for Textual Content](uiauto-ui-automation-textpattern-overview.md)

[Working with Text-based Controls](uiauto-workingwithtextbasedcontrols.md)
