---
title: DirectWrite interfaces
description: Lists the interfaces defined by DirectWrite.
ms.assetid: 7075e771-ce34-4426-8c07-13e85ff4d453
keywords:
- DirectWrite,interfaces
ms.topic: article
ms.date: 05/31/2018
---

# DirectWrite interfaces

DirectWrite defines the following interfaces.

## In this section

| Topic | Description |
|-|-|
| [**IDWriteAsyncResult**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteasyncresult) | Represents the result of an asynchronous operation. A client can use the interface to wait for the operation to complete, and to get the result.  |
| [**IDWriteBitmapRenderTarget**](/windows/win32/api/dwrite/nn-dwrite-idwritebitmaprendertarget) | Encapsulates a 32-bit device independent bitmap and device context, which can be used for rendering glyphs. |
| [**IDWriteBitmapRenderTarget1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritebitmaprendertarget1) | Encapsulates a 32-bit device independent bitmap and device context, which you can use for rendering glyphs. |
| [**IDWriteBitmapRenderTarget2**](./dwrite_3/nn-dwrite_3-idwritebitmaprendertarget2.md) | Encapsulates a 32-bit device independent bitmap and device context, which can be used for rendering glyphs. |
| [**IDWriteColorGlyphRunEnumerator**](idwritecolorglyphrunenumerator.md) | This interface allows the application to enumerate through the color glyph runs. |
| [**IDWriteColorGlyphRunEnumerator1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritecolorglyphrunenumerator1) | Enumerator for an ordered collection of color glyph runs. |
| [**IDWriteFactory**](/windows/win32/api/dwrite/nn-dwrite-idwritefactory) | Used to create all subsequent DirectWrite objects. This interface is the root factory interface for all DirectWrite objects. |
| [**IDWriteFactory1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefactory1) | The root factory interface for all [DirectWrite](direct-write-portal.md) objects. |
| [**IDWriteFactory2**](idwritefactory2.md) | The root factory interface for all [DirectWrite](direct-write-portal.md) objects. |
| [**IDWriteFactory3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory3) | The root factory interface for all [DirectWrite](direct-write-portal.md) objects. |
| [**IDWriteFactory4**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory4) | The root factory interface for all DirectWrite objects. |
| [**IDWriteFactory5**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory5) | The root factory interface for all DirectWrite objects. |
| [**IDWriteFactory6**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory6) | This represents a factory object from which all DirectWrite objects are created. **IDWriteFactory6** adds new facilities for working with fonts and font resources. |
| [**IDWriteFactory7**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory7) | This interface represents a factory object from which all DirectWrite objects are created. **IDWriteFactory7** adds new facilities for working with system fonts. |
| [**IDWriteFont**](/windows/win32/api/dwrite/nn-dwrite-idwritefont) | Represents a physical font in a font collection. This interface is used to create font faces from physical fonts, or to retrieve information such as font face metrics or face names from existing font faces. |
| [**IDWriteFont1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefont1) | Represents a physical font in a font collection. |
| [**IDWriteFont2**](idwritefont2.md) | Represents a physical font in a font collection. |
| [**IDWriteFont3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefont3) | Represents a font in a font collection. |
| [**IDWriteFontCollection**](/windows/win32/api/dwrite/nn-dwrite-idwritefontcollection) | An object that encapsulates a set of fonts, such as the set of fonts installed on the system, or the set of fonts in a particular directory. The font collection API can be used to discover what font families and fonts are available, and to obtain some metadata about the fonts. |
| [**IDWriteFontCollection1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontcollection1) | An object that encapsulates a set of fonts, such as the set of fonts installed on the system, or the set of fonts in a particular directory. The font collection API can be used to discover what font families and fonts are available, and to obtain some metadata about the fonts. |
| [**IDWriteFontCollection2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontcollection2) | This interface encapsulates a set of fonts, such as the set of fonts installed on the system, or the set of fonts in a particular directory. |
| [**IDWriteFontCollection3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontcollection3) | This interface encapsulates a set of fonts, such as the set of fonts installed on the system, or the set of fonts in a particular directory. |
| [**IDWriteFontCollectionLoader**](/windows/win32/api/dwrite/nn-dwrite-idwritefontcollectionloader) | Used to construct a collection of fonts given a particular type of key.  |
| [**IDWriteFontDownloadListener**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadlistener) | Application-defined callback interface that receives notifications from the font download queue ([**IDWriteFontDownloadQueue**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadqueue) interface). Callbacks will occur on the downloading thread, and objects must be prepared to handle calls on their methods from other threads at any time. |
| [**IDWriteFontDownloadQueue**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadqueue) | Interface that enqueues download requests for remote fonts, characters, glyphs, and font fragments.  |
| [**IDWriteFontFace**](/windows/win32/api/dwrite/nn-dwrite-idwritefontface) | This interface exposes various font data such as metrics, names, and glyph outlines. It contains font face type, appropriate file references, and face identification data. |
| [**IDWriteFontFace1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefontface1) | Contains font face type, appropriate file references, and face identification data.  |
| [**IDWriteFontFace2**](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritefontface2) | This interface contains font face type, appropriate file references, and face identification data. It adds the ability to check whether a color rendering path is potentially necessary.  |
| [**IDWriteFontFace3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontface3) | Contains font face type, appropriate file references, and face identification data. |
| [**IDWriteFontFace4**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontface4) | Contains font face type, appropriate file references, and face identification data. |
| [**IDWriteFontFace5**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontface5) | This interface contains font face type, appropriate file references, and face identification data. It adds new facilities such as comparing two font faces, retrieving font axis values, and retrieving the underlying font resource. |
| [**IDWriteFontFaceReference**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference) | Represents a reference to a font face. A uniquely identifying reference to a font, from which you can create a font face to query font metrics and use for rendering. A font face reference consists of a font file, font face index, and font face simulation. The file data may or may not be physically present on the local machine yet.  |
| [**IDWriteFontFaceReference1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference1) | Represents a reference to a font face. A uniquely identifying reference to a font, from which you can create a font face to query font metrics and use for rendering. |
| [**IDWriteFontFallback**](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritefontfallback) | Allows you to access fallback fonts from the font list. |
| [**IDWriteFontFallbackBuilder**](idwritefontfallbackbuilder.md) | Allows you to create Unicode font fallback mappings and create a font fall back object from those mappings. |
| [**IDWriteFontFamily**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfamily) | Represents a family of related fonts. |
| [**IDWriteFontFamily1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfamily1) | Represents a family of related fonts. |
| [**IDWriteFontFamily2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfamily2) | Represents a family of related fonts. **IDWriteFontFamily2** adds new facilities, including retrieving fonts by font axis values. |
| [**IDWriteFontFile**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile) | Represents a font file. Applications such as font managers or font viewers can call [**IDWriteFontFile::Analyze**](/windows/win32/api/dwrite/nf-dwrite-idwritefontfile-analyze) to find out if a particular file is a font file, and whether it is a font type that is supported by the font system. |
| [**IDWriteFontFileEnumerator**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfileenumerator) | Encapsulates a collection of font files. The font system uses this interface to enumerate font files when building a font collection. |
| [**IDWriteFontFileLoader**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfileloader) | Handles loading font file resources of a particular type from a font file reference key into a font file stream object.  |
| [**IDWriteFontFileStream**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfilestream) | Loads font file data from a custom font file loader.  |
| [**IDWriteFontList**](/windows/win32/api/dwrite/nn-dwrite-idwritefontlist) | Represents a list of fonts. |
| [**IDWriteFontList1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontlist1) | Represents a list of fonts. |
| [**IDWriteFontList2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontlist2) | Represents a list of fonts. **IDWriteFontList2** adds new facilities, including retrieving the underlying font set used by the list. |
| [**IDWriteFontResource**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontresource) | nn-dwrite_3-idwritefontresource |
| [**IDWriteFontSet**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset) | Represents a font set. |
| [**IDWriteFontSet1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset1) | Represents a font set. |
| [**IDWriteFontSet2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset2) | Represents a font set. |
| [**IDWriteFontSet3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset3) | Represents a font set. |
| [**IDWriteFontSetBuilder**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder) | Contains methods for building a font set. |
| [**IDWriteFontSetBuilder1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder1) | Contains methods for building a font set. |
| [**IDWriteFontSetBuilder2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder2) | Contains methods for building a font set. |
| [**IDWriteGdiInterop**](/windows/win32/api/dwrite/nn-dwrite-idwritegdiinterop) | Provides interoperability with GDI, such as methods to convert a font face to a LOGFONT structure, or to convert a GDI font description into a font face. It is also used to create bitmap render target objects. |
| [**IDWriteGdiInterop1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritegdiinterop1) | Provides interoperability with GDI, such as methods to convert a font face to a LOGFONT structure, or to convert a GDI font description into a font face. It is also used to create bitmap render target objects. |
| [**IDWriteGeometrySink**](idwritegeometrysink.md) | [**IDWriteGeometrySink**](idwritegeometrysink.md) is a **typedef** of the [**ID2D1SimplifiedGeometrySink**](/windows/win32/api/d2d1/nn-d2d1-id2d1simplifiedgeometrysink) interface. Please see the [**ID2D1SimplifiedGeometrySink**](/windows/win32/api/d2d1/nn-d2d1-id2d1simplifiedgeometrysink) reference page for more information. |
| [**IDWriteGlyphRunAnalysis**](/windows/win32/api/dwrite/nn-dwrite-idwriteglyphrunanalysis) | Contains low-level information used to render a glyph run. |
| [**IDWriteInlineObject**](/windows/win32/api/dwrite/nn-dwrite-idwriteinlineobject) | Wraps an application-defined inline graphic, allowing DWrite to query metrics as if the graphic were a glyph inline with the text. |
| [**IDWriteInMemoryFontFileLoader**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteinmemoryfontfileloader) | Represents a font file loader that can access in-memory fonts. |
| [**IDWriteLocalFontFileLoader**](idwritelocalfontfileloader.md) | A built-in implementation of the [**IDWriteFontFileLoader**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfileloader) interface, that operates on local font files and exposes local font file information from the font file reference key. Font file references created using [**CreateFontFileReference**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-createfontfilereference) use this font file loader. |
| [**IDWriteLocalizedStrings**](/windows/win32/api/dwrite/nn-dwrite-idwritelocalizedstrings) | Represents a collection of strings indexed by locale name. |
| [**IDWriteNumberSubstitution**](./idwritenumbersubstitution.md) | Holds the appropriate digits and numeric punctuation for a specified locale. |
| [**IDWritePixelSnapping**](/windows/win32/api/dwrite/nn-dwrite-idwritepixelsnapping) | Defines the pixel snapping properties such as pixels per DIP(device-independent pixel) and the current transform matrix of a text renderer. |
| [**IDWriteRemoteFontFileLoader**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteremotefontfileloader) | Represents a font file loader that can access remote (i.e., downloadable) fonts.  |
| [**IDWriteRemoteFontFileStream**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteremotefontfilestream) | Represents a font file stream, parts of which may be non-local.  |
| [**IDWriteRenderingParams**](/windows/win32/api/dwrite/nn-dwrite-idwriterenderingparams) | Represents text rendering settings such as ClearType level, enhanced contrast, and gamma correction for glyph rasterization and filtering. An application typically obtains a rendering parameters object by calling the [**IDWriteFactory::CreateMonitorRenderingParams**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-createmonitorrenderingparams) method. |
| [**IDWriteRenderingParams1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwriterenderingparams1) | Represents text rendering settings for glyph rasterization and filtering. |
| [**IDWriteRenderingParams2**](/windows/win32/api/dwrite_2/nn-dwrite_2-idwriterenderingparams2) | Represents text rendering settings for glyph rasterization and filtering. |
| [**IDWriteRenderingParams3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriterenderingparams3) | Represents text rendering settings for glyph rasterization and filtering. |
| [**IDWriteStringList**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritestringlist) | Represents a collection of strings indexed by number. |
| [**IDWriteTextAnalysisSink**](/windows/win32/api/dwrite/nn-dwrite-idwritetextanalysissink) | This interface is implemented by the text analyzer's client to receive the output of a given text analysis.  |
| [**IDWriteTextAnalysisSink1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextanalysissink1) | The interface you implement to receive the output of the text analyzers. |
| [**IDWriteTextAnalysisSource**](/windows/win32/api/dwrite/nn-dwrite-idwritetextanalysissource) | Implemented by the text analyzer's client to provide text to the analyzer. It allows the separation between the logical view of text as a continuous stream of characters identifiable by unique text positions, and the actual memory layout of potentially discrete blocks of text in the client's backing store.  |
| [**IDWriteTextAnalysisSource1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextanalysissource1) | The interface you implement to provide needed information to the text analyzer, like the text and associated text properties. |
| [**IDWriteTextAnalyzer**](/windows/win32/api/dwrite/nn-dwrite-idwritetextanalyzer) | Analyzes various text properties for complex script processing such as bidirectional (bidi) support for languages like Arabic, determination of line break opportunities, glyph placement, and number substitution. |
| [**IDWriteTextAnalyzer1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextanalyzer1) | Analyzes various text properties for complex script processing. |
| [**IDWriteTextAnalyzer2**](idwritetextanalyzer2.md) | Analyzes various text properties for complex script processing. |
| [**IDWriteTextFormat**](/windows/win32/api/dwrite/nn-dwrite-idwritetextformat) | The [**IDWriteTextFormat**](/windows/win32/api/dwrite/nn-dwrite-idwritetextformat) interface describes the font and paragraph properties used to format text, and it describes locale information.  |
| [**IDWriteTextFormat1**](idwritetextformat1.md) | Describes the font and paragraph properties used to format text, and it describes locale information.  |
| [**IDWriteTextFormat2**](idwritetextformat2.md) | Describes the font and paragraph properties used to format text, and it describes locale information.  |
| [**IDWriteTextFormat3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritetextformat3) | Describes the font and paragraph properties used to format text, and it describes locale information. |
| [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) | The [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) interface represents a block of text after it has been fully analyzed and formatted. |
| [**IDWriteTextLayout1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextlayout1) | Represents a block of text after it has been fully analyzed and formatted. |
| [**IDWriteTextLayout2**](idwritetextlayout2.md) | Represents a block of text after it has been fully analyzed and formatted. |
| [**IDWriteTextLayout3**](idwritetextlayout3.md) | Represents a block of text after it has been fully analyzed and formatted.  |
| [**IDWriteTextRenderer**](/windows/win32/api/dwrite/nn-dwrite-idwritetextrenderer) | Represents a set of application-defined callbacks that perform rendering of text, inline objects, and decorations such as underlines. |
| [**IDWriteTextRenderer1**](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritetextrenderer1) | Represents a set of application-defined callbacks that perform rendering of text, inline objects, and decorations such as underlines.  |
| [**IDWriteTypography**](/windows/win32/api/dwrite/nn-dwrite-idwritetypography) | Represents a font typography setting. |