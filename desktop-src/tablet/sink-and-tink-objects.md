---
description: To aid the support of ink in applications, there are two objects, both of which can be embedded and are supported by any OLE container.
ms.assetid: fbd7bdf0-63b4-48d1-be91-eabbbb3f1618
title: sInk and tInk Objects
ms.topic: article
ms.date: 05/31/2018
---

# sInk and tInk Objects

To aid the support of ink in applications, there are two objects, both of which can be embedded and are supported by any OLE container. They are produced by calling either the **Ink.ClipboardCopy Method (Rectangle, InkClipboardFormats, InkClipboardModes)** or the **Ink.ClipboardCopy Method (Strokes, InkClipboardFormats, InkClipboardModes)** method and are:

-   Text ink object (tInk). This is an OLE object representing ink that is expected to form words. A tInk object allows the handwritten ink to be converted to text, either as the text returned by a recognizer or the choice taken from a list of recognition alternates. The color and size of the ink can be set programmatically and can be based on the attributes of the text around the object. The tInk object is intended to contain a single word.The tInk object is a small, lightweight object that can perform simple operations like rendering (given a handle to a device context (HDC) and a RECT), and persisting itself (given a stream). Using a tInk object allows a seamless user experience when working in an application that uses input of both handwriting and text.
-   Sketch ink object (sInk). This is an OLE object representing ink that is not expected to form words. A sInk object is interpreted as a drawing. A sInk object is also useful for representing multiple words.

These objects can be used for interoperability between applications, either by placing them in the OLE object slot on the Clipboard or by embedding them in Rich Text Format (RTF).

You can use tInk and sInk objects in the following ways:

-   Both tInk and sInk objects are supported in Microsoft Word 2002. Users can insert ink into a Word document by using the writing and drawing text input panels provided in Word 2002. This ink is embedded into the Word file as an OLE object with the CLSID of either the sInk or tInk object.
-   The Tablet PC [InkEdit](/previous-versions/ms552265(v=vs.100)) control makes use of the tInk object. The InkEdit control is a subclass of the standard [RichTextBox](/dotnet/api/system.windows.forms.richtextbox?view=netcore-3.1) control. Ink is inserted into the InkEdit control's RTF stream as a tInk object.
-   When an application moves a selected [Ink](/previous-versions/aa515768(v=msdn.10)) object onto the Clipboard, the OLE object Clipboard slot contains a tInk or sInk OLE object.

For example, your application can recognize handwriting and mark any [Ink](/previous-versions/aa515768(v=msdn.10)) object as a tInk object. Then, if you select a word in ink and copy and paste it to Word, alternates for that word are shown in Word 2002.

> [!Note]  
> The Tablet PC Platform's Clipboard support automatically selects the Enhanced Metafile (EMF) flag for you when you place a sInk or tInk object on the Clipboard as an OLE object. The object itself is stored on the Clipboard in the embed source and object descriptor slots.

 

As another example, by using the sInk object, you can draw an ink sketch in an application, copy and paste the sketch to Word 2002, and then edit the drawing by using Tablet PC Input Panel in Word.

In order to successfully contain tInk objects, an application must implement OLE container support for embedded objects. Then, to make the container fully support tInk, you must institute:

-   Modifications to the code for Find and Replace. Instead of skipping embedded objects in the search, these objects must be interrogated for type. If they are a tInk object, they must be instantiated and queried for their corresponding text.
-   Modifications to selection behavior. Selection of tInk objects should never appear with sizing handles. They should be selected in the same way that text is selected in the document. Selection code for objects must detect if the type is tInk and display the selection appropriately.
-   Use of ambient properties. Ambient properties such as font size, color, and bold formatting need to be transmitted to the tInk object. Application of these properties changes the width of the handwritten ink, so a size update is required by calling the [**GetInkExtent Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinklineinfo-getinkextent) or [IOleObject::GetExtent](/windows/win32/api/oleidl/nf-oleidl-ioleobject-getextent) method.
-   Override the default [IOleObject::DoVerb](/windows/win32/api/oleidl/nf-oleidl-ioleobject-doverb) method processing. This allows conversion to text to pass a batch of tInk objects to the recognizer, which can then break the words into recognition segments.

For more information about breaking words into recognition segments, see [Recognition Segments](recognition-segments.md).

 

 
