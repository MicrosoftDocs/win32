---
title: UI Automation Text Attributes
description: This topic describes how Microsoft UI Automation exposes the format and style properties (text attributes) of textual content, and provides a list of supported text attributes.
ms.assetid: 3a099cb6-d7ed-41bd-9091-7e39768b4581
keywords:
- UI Automation,text attributes
- text attributes,about
- text attributes,variant types
- text attributes,data types
- UI Automation,list of attributes
- UI Automation,list of text attributes
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation Text Attributes

This topic describes how Microsoft UI Automation exposes the format and style properties (*text attributes*) of textual content, and provides a list of supported text attributes.

UI Automation providers expose text attributes through the [**GetAttributeValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-getattributevalue) and [**FindAttribute**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-findattribute) methods of the [TextRange](uiauto-about-text-and-textrange-patterns.md) control pattern. Client applications use the [**IUIAutomationTextRange::GetAttributeValue**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-getattributevalue) method to retrieve the value of a particular text attribute for a text range. Clients can use the [**IUIAutomationTextRange::FindAttribute**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-findattribute) method to search a text range for text that has a particular attribute. If any matching text is found, the method creates a new text range that contains the matching text.

The text attributes in the following list are supported by the **TextRange** control pattern. The attribute names are derived from the UI Automation text attribute identifiers. For example, the **AnimationStyle** attribute is identified by clients as [**UIA\_AnimationStyleAttributeId**](https://www.bing.com/search?q=**UIA\_AnimationStyleAttributeId**) (defined in Uiautomationclient.h) and by providers as **Text\_AnimationStyle\_Attribute\_GUID** (defined in Uiautomationcoreapi.h). For more information about each supported text attribute, see [**Text Attribute Identifiers**](uiauto-textattribute-ids.md).

> [!Note]  
> Some of the attributes listed are supported starting with Windows 8. See [**Text Attribute Identifiers**](uiauto-textattribute-ids.md) for notes regarding version support.

 

This topic contains the following sections:

-   [Annotation Attributes](#annotation-attributes)
-   [Font Attributes](#font-attributes)
-   [Language Attributes](#language-attributes)
-   [Link Attribute](#link-attribute)
-   [Page Margin Attributes](#page-margin-attributes)
-   [Text Alignment Attributes](#text-alignment-attributes)
-   [Text Color Attributes](#text-color-attributes)
-   [Text Decoration Attributes](#text-decoration-attributes)
-   [Text Style Attributes](#text-style-attributes)
-   [Interaction and Selection Attributes](#interaction-and-selection-attributes)
-   [Related topics](#related-topics)

## Annotation Attributes

Annotation objects and annotation types are available through the following attributes.



| Attribute             | Identifier                                                            |
|-----------------------|-----------------------------------------------------------------------|
| **AnnotationObjects** | [**UIA\_AnnotationObjectsAttributeId**](uiauto-textattribute-ids.md) |
| **AnnotationTypes**   | [**UIA\_AnnotationTypesAttributeId**](uiauto-textattribute-ids.md)   |



 

## Font Attributes

The name, size, and weight of a font is available through the following attributes.



| Attribute      | Identifier                                                                               |
|----------------|------------------------------------------------------------------------------------------|
| **FontName**   | [**UIA\_FontNameAttributeId**](https://www.bing.com/search?q=**UIA\_FontNameAttributeId**)     |
| **FontSize**   | [**UIA\_FontSizeAttributeId**](https://www.bing.com/search?q=**UIA\_FontSizeAttributeId**)     |
| **FontWeight** | [**UIA\_FontWeightAttributeId**](https://www.bing.com/search?q=**UIA\_FontWeightAttributeId**) |



 

## Language Attributes

Information about the language of the text is available through the following attributes.



| Attribute              | Identifier                                                                                               |
|------------------------|----------------------------------------------------------------------------------------------------------|
| **Culture**            | [**UIA\_CultureAttributeId**](https://www.bing.com/search?q=**UIA\_CultureAttributeId**)                       |
| **TextFlowDirections** | [**UIA\_TextFlowDirectionsAttributeId**](https://www.bing.com/search?q=**UIA\_TextFlowDirectionsAttributeId**) |



 

## Link Attribute

The following attribute provides the text range that is the target of a link in a document.



| Attribute | Identifier                                                                   |
|-----------|------------------------------------------------------------------------------|
| **Link**  | [**UIA\_LinkAttributeId**](https://www.bing.com/search?q=**UIA\_LinkAttributeId**) |



 

## Page Margin Attributes

The bounding rectangles of a text range do not expose the coordinates of the text in the page. However, a provider can expose the page margin information using the following text attributes.



| Attribute          | Identifier                                                                                       |
|--------------------|--------------------------------------------------------------------------------------------------|
| **MarginBottom**   | [**UIA\_MarginBottomAttributeId**](https://www.bing.com/search?q=**UIA\_MarginBottomAttributeId**)     |
| **MarginLeading**  | [**UIA\_MarginLeadingAttributeId**](https://www.bing.com/search?q=**UIA\_MarginLeadingAttributeId**)   |
| **MarginTop**      | [**UIA\_MarginTopAttributeId**](https://www.bing.com/search?q=**UIA\_MarginTopAttributeId**)           |
| **MarginTrailing** | [**UIA\_MarginTrailingAttributeId**](https://www.bing.com/search?q=**UIA\_MarginTrailingAttributeId**) |



 

## Text Alignment Attributes

Information about text alignment such as indentation, tab settings, and horizontal alignment is available through the following attributes.



| Attribute                   | Identifier                                                                                                         |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------|
| **HorizontalTextAlignment** | [**UIA\_HorizontalTextAlignmentAttributeId**](https://www.bing.com/search?q=**UIA\_HorizontalTextAlignmentAttributeId**) |
| **IndentationFirstLine**    | [**UIA\_IndentationFirstLineAttributeId**](https://www.bing.com/search?q=**UIA\_IndentationFirstLineAttributeId**)       |
| **IndentationLeading**      | [**UIA\_IndentationLeadingAttributeId**](https://www.bing.com/search?q=**UIA\_IndentationLeadingAttributeId**)           |
| **IndentationTrailing**     | [**UIA\_IndentationTrailingAttributeId**](https://www.bing.com/search?q=**UIA\_IndentationTrailingAttributeId**)         |
| **Tabs**                    | [**UIA\_TabsAttributeId**](https://www.bing.com/search?q=**UIA\_TabsAttributeId**)                                       |



 

## Text Color Attributes

The foreground and background text colors are available through the following text attributes. Both colors are specified as a [**COLORREF**](https://msdn.microsoft.com/library/windows/desktop/dd183449) data type.



| Attribute           | Identifier                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------------|
| **BackgroundColor** | [**UIA\_BackgroundColorAttributeId**](https://www.bing.com/search?q=**UIA\_BackgroundColorAttributeId**) |
| **ForegroundColor** | [**UIA\_ForegroundColorAttributeId**](https://www.bing.com/search?q=**UIA\_ForegroundColorAttributeId**) |



 

## Text Decoration Attributes

Text decorations include areas such as bullets, underlining, and animations. If text includes leading bullets or numbers, the symbol or text used for the bullet or number should be included in the text stream, if applicable.

Information about text decorations is available through the following attributes.



| Attribute              | Identifier                                                                                               |
|------------------------|----------------------------------------------------------------------------------------------------------|
| **AnimationStyle**     | [**UIA\_AnimationStyleAttributeId**](https://www.bing.com/search?q=**UIA\_AnimationStyleAttributeId**)         |
| **BulletStyle**        | [**UIA\_BulletStyleAttributeId**](https://www.bing.com/search?q=**UIA\_BulletStyleAttributeId**)               |
| **OutlineStyles**      | [**UIA\_OutlineStylesAttributeId**](https://www.bing.com/search?q=**UIA\_OutlineStylesAttributeId**)           |
| **OverlineColor**      | [**UIA\_OverlineColorAttributeId**](https://www.bing.com/search?q=**UIA\_OverlineColorAttributeId**)           |
| **OverlineStyle**      | [**UIA\_OverlineStyleAttributeId**](https://www.bing.com/search?q=**UIA\_OverlineStyleAttributeId**)           |
| **StrikethroughColor** | [**UIA\_StrikethroughColorAttributeId**](https://www.bing.com/search?q=**UIA\_StrikethroughColorAttributeId**) |
| **StrikethroughStyle** | [**UIA\_StrikethroughStyleAttributeId**](https://www.bing.com/search?q=**UIA\_StrikethroughStyleAttributeId**) |
| **UnderlineColor**     | [**UIA\_UnderlineColorAttributeId**](https://www.bing.com/search?q=**UIA\_UnderlineColorAttributeId**)         |
| **UnderlineStyle**     | [**UIA\_UnderlineStyleAttributeId**](https://www.bing.com/search?q=**UIA\_UnderlineStyleAttributeId**)         |



 

## Text Style Attributes

Information about text styles is available though the following attributes.



| Attribute         | Identifier                                                                                     |
|-------------------|------------------------------------------------------------------------------------------------|
| **CapStyle**      | [**UIA\_CapStyleAttributeId**](https://www.bing.com/search?q=**UIA\_CapStyleAttributeId**)           |
| **IsHidden**      | [**UIA\_IsHiddenAttributeId**](https://www.bing.com/search?q=**UIA\_IsHiddenAttributeId**)           |
| **IsItalic**      | [**UIA\_IsItalicAttributeId**](https://www.bing.com/search?q=**UIA\_IsItalicAttributeId**)           |
| **IsReadOnly**    | [**UIA\_IsReadOnlyAttributeId**](https://www.bing.com/search?q=**UIA\_IsReadOnlyAttributeId**)       |
| **IsSuperscript** | [**UIA\_IsSuperscriptAttributeId**](https://www.bing.com/search?q=**UIA\_IsSuperscriptAttributeId**) |
| **IsSubscript**   | [**UIA\_IsSubscriptAttributeId**](https://www.bing.com/search?q=**UIA\_IsSubscriptAttributeId**)     |



 

## Interaction and Selection Attributes

Information about current text selection in the range and focus state is available though the following attributes.



| Attribute              | Identifier                                                                                     |
|------------------------|------------------------------------------------------------------------------------------------|
| **IsActive**           | [**UIA\_IsActiveAttributeId**](https://www.bing.com/search?q=**UIA\_IsActiveAttributeId**)           |
| **SelectionActiveEnd** | [**UIA\_SelectionActiveEndAttributeId**](https://www.bing.com/search?q=**UIA\_SelectionActiveEndAttributeId**) |
| **CaretPosition**      | [**UIA\_CaretPositionAttributeId**](https://www.bing.com/search?q=**UIA\_CaretPositionAttributeId**)      |
| **CaretBidiMode**      | [**UIA\_CaretBidiModeAttributeId**](https://www.bing.com/search?q=**UIA\_CaretBidiModeAttributeId**) |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[About the UI Automation Text and TextRange Control Patterns](uiauto-about-text-and-textrange-patterns.md)
</dt> <dt>

[Text and TextRange Control Patterns](uiauto-implementingtextandtextrange.md)
</dt> <dt>

[Working with Text-based Controls](uiauto-workingwithtextbasedcontrols.md)
</dt> </dl>

 

 




