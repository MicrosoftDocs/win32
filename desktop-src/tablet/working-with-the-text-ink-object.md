---
description: To aid the support of ink in applications, there are two objects, both of which can be embedded and are supported by any OLE container, the text ink object (tInk) and the sketch ink object (sInk).
ms.assetid: 0202e91c-c7a0-4e7b-a1c6-a2f58c11c0be
title: Working with the Text Ink Object
ms.topic: article
ms.date: 05/31/2018
---

# Working with the Text Ink Object

To aid the support of ink in applications, there are two objects, both of which can be embedded and are supported by any OLE container, the text ink object (tInk) and the sketch ink object (sInk).

The text ink object is an OLE object representing ink that is expected to form words. A text ink object enables the handwritten ink to be converted to text by choosing from a list of alternates. The color and size of the text ink object can be set programmatically and can be based on the attributes of the text around the object. The text ink object is intended to contain a single word.

The text ink object supports the standard set of OLE interfaces required for embedding and clipboard support. The [**IPersistStream**](/windows/win32/api/objidl/nn-objidl-ipersiststream) interface reads from and writes to a stream in ink serialized format (ISF). The text ink object provides the [**IInkLineInfo**](/windows/desktop/api/msinkaut/nn-msinkaut-iinklineinfo) interface to access its display properties, and recognition result list.

The text ink object can be used for interoperability between applications either by placing it in the OLE object slot on the Clipboard, by embedding it in RTF, or by persisting it in an ISF stream.

A text ink object can be generated in the following ways.

-   The [InkEdit](inkedit-control-reference.md) control makes use of the text ink object. The InkEdit control's functionality is a super-set of the standard RichEdit control functionality. Ink is inserted into the InkEdit control's RTF stream as a text ink object.
-   When an application copies an [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) or an [InkEdit](inkedit-control-reference.md) object onto the Clipboard and the [**InkClipboardFormats Enumeration**](/windows/desktop/api/msinkaut/ne-msinkaut-inkclipboardformats) format is set, the OLE object Clipboard slot contains a text ink OLE object.
-   Tablet PC Input Panel can generate text ink objects.

For example, your application can recognize handwriting and add the recognition result to the strokes. Then, if you copy and paste the strokes to Microsoft Word as a text ink object, alternates for that word is available in Word 2003 and later versions.

In order to successfully contain text ink objects, an application must implement OLE container support for embedded objects. Then, to make the container fully support text ink, you must institute:

-   Modifications to the application for Find and Replace. Instead of skipping embedded objects in the search, these objects must be interrogated for type. If they are a text ink object, they must be instantiated and queried for their corresponding text.
-   Modifications to selection behavior. Selection of text ink objects should never appear with sizing handles. They should be selected in the same way that text is selected in the document. Selection code for objects must detect if the type is text ink and display the selection appropriately.
-   Use of ambient properties. Ambient properties such as font size, color, and bold formatting need to be transmitted to the text ink object. Application of these properties changes the width of the handwritten ink, so a size update is required by calling the [**IInkLineInfo::GetInkExtent**](/windows/desktop/api/msinkaut/nf-msinkaut-iinklineinfo-getinkextent) or [**IOleObject::GetExtent**](/windows/win32/api/oleidl/nf-oleidl-ioleobject-getextent) method.

## In This Section

-   [Converting a Text Ink Object to Ink](converting-a-text-ink-object-to-ink.md)
-   [Text Ink APIs](text-ink-apis.md)
-   [sInk and tInk Objects](sink-and-tink-objects.md)

 

 
