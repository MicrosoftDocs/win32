---
title: About the Text and TextRange Control Patterns
description: The textual content of a control is exposed by using the Text control pattern, which represents the contents of a text container as a text stream.
ms.assetid: acc2b513-9367-416a-b0d9-3c2bcc14a8a7
keywords:
- UI Automation,textual content support
- UI Automation,text pattern overview
- UI Automation,text controls overview
- UI Automation,Text control pattern
- UI Automation,Text Services Framework (TSF)
- UI Automation,TSF
- UI Automation,performance
- text patterns,about
- text patterns,Text Services Framework (TSF)
- text controls,about
- textual content,support for
- text controls,performance
- Text control pattern
- control patterns,Text
- Text Services Framework (TSF)
- TSF (Text Services Framework)
- performance
ms.topic: article
ms.date: 05/31/2018
---

# About the Text and TextRange Control Patterns

The textual content of a control is exposed by using the [Text](uiauto-implementingtextandtextrange.md) control pattern, which represents the contents of a text container as a text stream. The Text control pattern requires the support of the TextRange control pattern to expose format and style attributes. The TextRange control pattern supports the Text control pattern by representing contiguous or multiple, disjoint text spans (or ranges) in a text container with a collection of start and end endpoints. The TextRange control pattern supports functionality such as selection, comparison, retrieval and traversal.

> [!Note]  
> The [Text](uiauto-implementingtextandtextrange.md) control pattern does not provide a means to insert or modify text. However, depending on the control, this may be accomplished by using the Microsoft UI Automation [Value](uiauto-implementingvalue.md) control pattern or through direct keyboard input. There's also a [**TextEdit**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-itexteditprovider) pattern that supports programmatic change to text.

 

The functionality described in this topic is vital to assistive technology vendors and their end users. Assistive technologies can use UI Automation to gather complete text formatting information for the user and provide programmatic navigation and selection of text by [**TextUnit**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) (character, word, line, or paragraph).

This topic contains the following sections:

-   [UI Automation TextPattern and the Text Services Framework](#ui-automation-textpattern-and-the-text-services-framework)
-   [Control Types](#control-types)
-   [Provider Interfaces](#provider-interfaces)
-   [Client Interfaces](#client-interfaces)
-   [Performance](#performance)
-   [Text Pattern and Virtualized Embedded Objects](#text-pattern-and-virtualized-embedded-objects)
-   [Using the Custom Control Type with the Text Control Pattern](#using-the-custom-control-type-with-the-text-control-pattern)
-   [Lifetime of a Text Range](#lifetime-of-a-text-range)
-   [Related topics](#related-topics)

## UI Automation TextPattern and the Text Services Framework

Text Services Framework (TSF) is a simple and scalable system framework that enables natural language services and advanced text input on the desktop and in applications. In addition to providing interfaces for applications to expose their text store, it also supports metadata for the text store.

TSF was designed for applications that need to inject input into context-aware scenarios. The [Text](uiauto-implementingtextandtextrange.md) control pattern, however, is a read-only solution that is intended to provide optimized access to a text store for screen-readers and Braille devices.

Accessible technologies that require read-only access to a text store can use the Text control pattern, but will need the functionality of TSF for context-aware input.

For more information, see [Text Services Framework](/windows/desktop/TSF/text-services-framework).

## Control Types

The UI Automation [Edit](uiauto-supporteditcontroltype.md) control type and [Document](uiauto-supportdocumentcontroltype.md) control type must support the [Text](uiauto-implementingtextandtextrange.md) control pattern. For improved accessibility, Microsoft recommends that the [ToolTip](uiauto-supporttooltipcontroltype.md) and Text control types also support the Text control pattern, but it is not required.

## Provider Interfaces

UI Automation providers support the [Text](uiauto-implementingtextandtextrange.md) control pattern for a control by implementing the [**ITextProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextprovider) and [**ITextRangeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextrangeprovider) interfaces. These interfaces expose detailed attribute information for text in the control and provide robust navigational capabilities.

A provider does not need to support all text attributes if the control lacks support for any particular attribute.

A provider must support the [**ITextProvider::GetSelection**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextprovider-getselection) and [**ITextRangeProvider::Select**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-select) methods if the control supports text selection or placement of the text cursor (or system caret) within the text area. If the control does not support this functionality, it does not need to support either of these methods. However, the control must expose the type of text selection it supports by implementing the [**ITextProvider::SupportedTextSelection**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextprovider-get_supportedtextselection) property.

A provider must always support the [**TextUnit**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) constants, **TextUnit\_Character** and **TextUnit\_Document**, as well as any others it is capable of supporting.

> [!Note]  
> The provider may skip support for a specific [**TextUnit**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-textunit) by deferring to the next largest unit supported in the following order: **TextUnit\_Character**, **TextUnit\_Format**, **TextUnit\_Word**, **TextUnit\_Line**, **TextUnit\_Paragraph**, **TextUnit\_Page**, and **TextUnit\_Document**.

 

## Client Interfaces

UI Automation client applications use the [**IUIAutomationTextPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtextpattern) and [**IUIAutomationTextRange**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtextrange) interfaces to access the textual content of a text control. Clients use **IUIAutomationTextPattern** to select spans of text called *text ranges*, and to retrieve pointers to **IUIAutomationTextRange** interfaces for the ranges. The **IUIAutomationTextRange** interface enables clients to manipulate the text range, and to retrieve information about the text in the range, including attributes such as font name, foreground color, underline style, and so on. For more information, see [Text Attribute Identifiers](uiauto-textattribute-ids.md).

## Performance

The **Text** control pattern relies on cross-process calls for most of its functionality, so it does not provide a caching mechanism to improve performance when it processes content. Other control patterns in Microsoft UI Automation can be accessed by using the [**IUIAutomationElement::GetCachedPattern**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedpattern) method.

One technique for improving performance is to ensure that UI Automation clients attempt to retrieve moderately sized blocks of text by using the [**IUIAutomationTextRange::GetText**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtextrange-gettext) method. For example, using **GetText** to retrieve single characters will incur cross-process hits for each character, whereas not specifying a maximum length when calling **GetText** will incur one cross-process hit, but can have high latency depending on the size of the text range.

## Text Pattern and Virtualized Embedded Objects

Whenever possible, a provider implementation of [**ITextProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextprovider) and [**ITextRangeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextrangeprovider) should support the entire text of a document, including any text outside of the viewport. For off-screen text or embedded objects that are virtualized, providers should support the [VirtualizedItem control pattern](uiauto-implementingvirtualizeditem.md) ([**IVirtualizedItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivirtualizeditemprovider)).

If a document is virtualized while the entire text stream is still available, the [**ITextProvider::DocumentRange**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextprovider-get_documentrange) property will retrieve a text range that includes the entire document. However, calling the [**ITextRangeProvider**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itextrangeprovider-getchildren) method will retrieve a collection of virtualized objects that represent all embedded objects in the document. To interact with a virtualized embedded object, clients must call the [**IVirtualizedItemProvider::Realize**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivirtualizeditemprovider-realize) method, which makes the items fully accessible as UI Automation elements. Clients must follow a similar process to work with grid elements in an embedded table where a portion of the table is off-screen and virtualized.

## Using the Custom Control Type with the Text Control Pattern

While the [Text](uiauto-implementingtextandtextrange.md) control pattern supports many text attributes and embedded objects, it is not possible to define in advance all possible document elements and presentation types. For document elements that are not supported by the existing attributes or standard control types, providers can use the extensibility features provided by the UI Automation **Custom** control type.

For applications and user interfaces that are based on page presentations, the boundary and layout presentation of "page" can also be expressed as an embedded object that has a custom control type (that is, `LocalizedControlType="page"`). That way, the embedded object can host other page elements that cannot easily be part of the document text stream, such as the header and footer fields of each page, as children of the "page" embedded object. Alternatively, each "page" object can support the [Text](uiauto-implementingtextandtextrange.md) control pattern independently, which works well for applications such as authoring tools for slide show presentations, or page-based desktop publishing environments.

## Lifetime of a Text Range

If possible, a provider should ensure that any text changes, such as deletions, insertions, and moves, are reflected in the associated text range. If updating the text range is not possible, the provider should raise a [**UIA\_Text\_TextChangedEventId**](uiauto-event-ids.md) event to notify clients that the text range is no longer valid and a new one must be retrieved.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[How UI Automation Supports Embedded Objects](uiauto-textpattern-and-embedded-objects-overview.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Support for Textual Content](uiauto-ui-automation-textpattern-overview.md)
</dt> <dt>

[Working with Text-based Controls](uiauto-workingwithtextbasedcontrols.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[Text Services Framework](/windows/desktop/TSF/text-services-framework)
</dt> </dl>

 

 