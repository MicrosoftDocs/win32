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
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation Text Attributes

This topic describes how Microsoft UI Automation exposes the format and style properties (*text attributes*) of textual content, and provides a list of supported text attributes.

UI Automation providers expose text attributes through the [**GetAttributeValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-getattributevalue) and [**FindAttribute**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-findattribute) methods of the [TextRange](uiauto-about-text-and-textrange-patterns.md) control pattern. Client applications use the [**IUIAutomationTextRange::GetAttributeValue**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-getattributevalue) method to retrieve the value of a particular text attribute for a text range. Clients can use the [**IUIAutomationTextRange::FindAttribute**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-findattribute) method to search a text range for text that has a particular attribute. If any matching text is found, the method creates a new text range that contains the matching text.

The text attributes in the following list are supported by the **TextRange** control pattern. The attribute names are derived from the UI Automation text attribute identifiers. For example, the **AnimationStyle** attribute is identified by clients as [**UIA\_AnimationStyleAttributeId**](uiauto-textattribute-ids.md) (defined in Uiautomationclient.h) and by providers as **Text\_AnimationStyle\_Attribute\_GUID** (defined in Uiautomationcoreapi.h). For more information about each supported text attribute, see [**Text Attribute Identifiers**](uiauto-textattribute-ids.md).

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
| **AnnotationObjects** | [**UIA\_AnnotationObjectsAttributeId**](uiauto-annotation-type-identifiers.md) |
| **AnnotationTypes**   | [**UIA\_AnnotationTypesAttributeId**](uiauto-annotation-type-identifiers.md)   |



 

## Font Attributes

The name, size, and weight of a font is available through the following attributes.



| Attribute      | Identifier                                                                               |
|----------------|------------------------------------------------------------------------------------------|
| **FontName**   | [**UIA\_FontNameAttributeId**](uiauto-textattribute-ids.md)     |
| **FontSize**   | [**UIA\_FontSizeAttributeId**](uiauto-textattribute-ids.md)     |
| **FontWeight** | [**UIA\_FontWeightAttributeId**](uiauto-textattribute-ids.md) |



 

## Language Attributes

Information about the language of the text is available through the following attributes.



| Attribute              | Identifier                                                                                               |
|------------------------|----------------------------------------------------------------------------------------------------------|
| **Culture**            | [**UIA\_CultureAttributeId**](uiauto-textattribute-ids.md)                       |
| **TextFlowDirections** | [**UIA\_TextFlowDirectionsAttributeId**](uiauto-textattribute-ids.md) |



 

## Link Attribute

The following attribute provides the text range that is the target of a link in a document.



| Attribute | Identifier                                                                   |
|-----------|------------------------------------------------------------------------------|
| **Link**  | [**UIA\_LinkAttributeId**](uiauto-textattribute-ids.md) |



 

## Page Margin Attributes

The bounding rectangles of a text range do not expose the coordinates of the text in the page. However, a provider can expose the page margin information using the following text attributes.



| Attribute          | Identifier                                                                                       |
|--------------------|--------------------------------------------------------------------------------------------------|
| **MarginBottom**   | [**UIA\_MarginBottomAttributeId**](uiauto-textattribute-ids.md)     |
| **MarginLeading**  | [**UIA\_MarginLeadingAttributeId**](uiauto-textattribute-ids.md)   |
| **MarginTop**      | [**UIA\_MarginTopAttributeId**](uiauto-textattribute-ids.md)           |
| **MarginTrailing** | [**UIA\_MarginTrailingAttributeId**](uiauto-textattribute-ids.md) |



 

## Text Alignment Attributes

Information about text alignment such as indentation, tab settings, and horizontal alignment is available through the following attributes.



| Attribute                   | Identifier                                                                                                         |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------|
| **HorizontalTextAlignment** | [**UIA\_HorizontalTextAlignmentAttributeId**](uiauto-textattribute-ids.md) |
| **IndentationFirstLine**    | [**UIA\_IndentationFirstLineAttributeId**](uiauto-textattribute-ids.md)       |
| **IndentationLeading**      | [**UIA\_IndentationLeadingAttributeId**](uiauto-textattribute-ids.md)           |
| **IndentationTrailing**     | [**UIA\_IndentationTrailingAttributeId**](uiauto-textattribute-ids.md)         |
| **Tabs**                    | [**UIA\_TabsAttributeId**](uiauto-textattribute-ids.md)                                       |



 

## Text Color Attributes

The foreground and background text colors are available through the following text attributes. Both colors are specified as a [**COLORREF**](/windows/desktop/gdi/colorref) data type.



| Attribute           | Identifier                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------------|
| **BackgroundColor** | [**UIA\_BackgroundColorAttributeId**](uiauto-textattribute-ids.md) |
| **ForegroundColor** | [**UIA\_ForegroundColorAttributeId**](uiauto-textattribute-ids.md) |



 

## Text Decoration Attributes

Text decorations include areas such as bullets, underlining, and animations. If text includes leading bullets or numbers, the symbol or text used for the bullet or number should be included in the text stream, if applicable.

Information about text decorations is available through the following attributes.



| Attribute              | Identifier                                                                                               |
|------------------------|----------------------------------------------------------------------------------------------------------|
| **AnimationStyle**     | [**UIA\_AnimationStyleAttributeId**](uiauto-textattribute-ids.md)         |
| **BulletStyle**        | [**UIA\_BulletStyleAttributeId**](uiauto-textattribute-ids.md)               |
| **OutlineStyles**      | [**UIA\_OutlineStylesAttributeId**](uiauto-textattribute-ids.md)           |
| **OverlineColor**      | [**UIA\_OverlineColorAttributeId**](uiauto-textattribute-ids.md)           |
| **OverlineStyle**      | [**UIA\_OverlineStyleAttributeId**](uiauto-textattribute-ids.md)           |
| **StrikethroughColor** | [**UIA\_StrikethroughColorAttributeId**](uiauto-textattribute-ids.md) |
| **StrikethroughStyle** | [**UIA\_StrikethroughStyleAttributeId**](uiauto-textattribute-ids.md) |
| **UnderlineColor**     | [**UIA\_UnderlineColorAttributeId**](uiauto-textattribute-ids.md)         |
| **UnderlineStyle**     | [**UIA\_UnderlineStyleAttributeId**](uiauto-textattribute-ids.md)         |



 

## Text Style Attributes

Information about text styles is available though the following attributes.



| Attribute         | Identifier                                                                                     |
|-------------------|------------------------------------------------------------------------------------------------|
| **CapStyle**      | [**UIA\_CapStyleAttributeId**](uiauto-textattribute-ids.md)           |
| **IsHidden**      | [**UIA\_IsHiddenAttributeId**](uiauto-textattribute-ids.md)           |
| **IsItalic**      | [**UIA\_IsItalicAttributeId**](uiauto-textattribute-ids.md)           |
| **IsReadOnly**    | [**UIA\_IsReadOnlyAttributeId**](uiauto-textattribute-ids.md)       |
| **IsSuperscript** | [**UIA\_IsSuperscriptAttributeId**](uiauto-textattribute-ids.md) |
| **IsSubscript**   | [**UIA\_IsSubscriptAttributeId**](uiauto-textattribute-ids.md)     |



 

## Interaction and Selection Attributes

Information about current text selection in the range and focus state is available though the following attributes.



| Attribute              | Identifier                                                                                     |
|------------------------|------------------------------------------------------------------------------------------------|
| **IsActive**           | [**UIA\_IsActiveAttributeId**](uiauto-textattribute-ids.md)           |
| **SelectionActiveEnd** | [**UIA\_SelectionActiveEndAttributeId**](uiauto-textattribute-ids.md) |
| **CaretPosition**      | [**UIA\_CaretPositionAttributeId**](uiauto-textattribute-ids.md)      |
| **CaretBidiMode**      | [**UIA\_CaretBidiModeAttributeId**](uiauto-textattribute-ids.md) |



 

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

 

 