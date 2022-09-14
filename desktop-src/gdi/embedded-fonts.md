---
description: Embedding a font is the technique of bundling a document and the fonts it contains into a file for transmission to another computer.
ms.assetid: ded409f1-5bd9-411b-b905-fc49c484786a
title: Embedded Fonts
ms.topic: article
ms.date: 05/31/2018
---

# Embedded Fonts

Embedding a font is the technique of bundling a document and the fonts it contains into a file for transmission to another computer. Embedding a font guarantees that a font specified in a transmitted file will be present on the computer receiving the file. Not all fonts can be moved from computer to computer, however, since most fonts are licensed to only one computer at a time. Only TrueType and OpenType fonts can be embedded.

Applications should embed a font in a document only when requested by a user. An application cannot be distributed along with documents that contain embedded fonts, nor can an application itself contain an embedded font. Whenever an application distributes a font, in any format, the proprietary rights of the owner of the font must be acknowledged.

It may be a violation of a font vendor's proprietary rights or user license agreement to embed any fonts where embedding is not permitted or to fail to observe the following guidelines on embedding fonts. A font's license may give only read/write permission for a font to be installed and used on the destination computer. Or the license may give read-only permission. Read-only permission allows a document to be viewed and printed (but not modified) by the destination computer; documents with read-only embedded fonts are themselves read-only. Read-only embedded fonts may not be unbundled from the document and installed on the destination computer.

An application can determine the license status by calling the [**GetOutlineTextMetrics**](/windows/desktop/api/Wingdi/nf-wingdi-getoutlinetextmetricsa) function and examining the **otmfsType** member of the [**OUTLINETEXTMETRIC**](/windows/desktop/api/Wingdi/ns-wingdi-outlinetextmetrica) structure. If bit 1 of **otmfsType** is set, embedding is not permitted for the font. If bit 1 is clear, the font can be embedded. If bit 2 is set, the embedding is read-only.

To embed a TrueType font, an application can use the [**GetFontData**](/windows/desktop/api/Wingdi/nf-wingdi-getfontdata) function to read the font file. Setting the *dwTable* and *dwOffset* parameters of [**GetFontData**](/windows/win32/api/wingdi/nf-wingdi-getfontdata) to 0L and the *cbData* parameter to 1L ensures that the application reads the entire font file from the beginning.

Several functions are available to embed OpenType fonts depending on the character width and where the font data resides. To embed an OpenType Unicode font that resides in a device context, an application can use [**TTEmbedFont**](/windows/desktop/api/T2embapi/nf-t2embapi-ttembedfont). To embed an OpenType UCS-4 font that resides in a device context, an application can use [**TTEmbedFontEx**](/windows/desktop/api/T2embapi/nf-t2embapi-ttembedfontex). To embed an OpenType Unicode font that resides in a font file, an application can use [**TTEmbedFontFromFile**](/windows/desktop/api/T2embapi/nf-t2embapi-ttembedfontfromfilea). For additional information on OpenType font embedding, see the [Font Embedding Reference](font-embedding-reference.md).

After an application retrieves the font data, it can store the data with the document by using any applicable format. Most applications build a font directory in the document, listing the embedded fonts and whether the embedding is read/write or read-only. An application can use the **otmpStyleName** and **otmFamilyName** members of the [**OUTLINETEXTMETRIC**](/windows/win32/api/wingdi/ns-wingdi-outlinetextmetrica) structure to identify the font.

If the read-only bit is set for the embedded font, applications must encrypt the font data before storing it with the document. The encryption method need not be complicated; for example, using the XOR operator to combine the font data with an application-defined constant is adequate and fast.

 

 
