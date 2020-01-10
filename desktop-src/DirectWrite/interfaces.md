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
| [**IDWriteAsyncResult**](https://msdn.microsoft.com/library/Mt807681(v=VS.85).aspx) | Represents the result of an asynchronous operation. A client can use the interface to wait for the operation to complete, and to get the result.  |
| [**IDWriteBitmapRenderTarget**](https://msdn.microsoft.com/library/Dd368165(v=VS.85).aspx) | Encapsulates a 32-bit device independent bitmap and device context, which can be used for rendering glyphs. |
| [**IDWriteBitmapRenderTarget1**](https://msdn.microsoft.com/library/Hh780398(v=VS.85).aspx) | Encapsulates a 32-bit device independent bitmap and device context, which you can use for rendering glyphs. |
| [**IDWriteColorGlyphRunEnumerator**](idwritecolorglyphrunenumerator.md) | This interface allows the application to enumerate through the color glyph runs. |
| [**IDWriteColorGlyphRunEnumerator1**](https://msdn.microsoft.com/library/Mt725314(v=VS.85).aspx) | Enumerator for an ordered collection of color glyph runs. |
| [**IDWriteFactory**](https://msdn.microsoft.com/library/Dd368183(v=VS.85).aspx) | Used to create all subsequent DirectWrite objects. This interface is the root factory interface for all DirectWrite objects. |
| [**IDWriteFactory1**](https://msdn.microsoft.com/library/Hh780401(v=VS.85).aspx) | The root factory interface for all [DirectWrite](direct-write-portal.md) objects. |
| [**IDWriteFactory2**](idwritefactory2.md) | The root factory interface for all [DirectWrite](direct-write-portal.md) objects. |
| [**IDWriteFactory3**](https://msdn.microsoft.com/library/Dn890753(v=VS.85).aspx) | The root factory interface for all [DirectWrite](direct-write-portal.md) objects. |
| [**IDWriteFactory4**](https://msdn.microsoft.com/library/Mt725315(v=VS.85).aspx) | The root factory interface for all DirectWrite objects. |
| [**IDWriteFactory5**](https://msdn.microsoft.com/library/Mt807684(v=VS.85).aspx) | The root factory interface for all DirectWrite objects. |
| [**IDWriteFactory6**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory6) | This represents a factory object from which all DirectWrite objects are created. **IDWriteFactory6** adds new facilities for working with fonts and font resources. |
| [**IDWriteFactory7**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory7) | This interface represents a factory object from which all DirectWrite objects are created. **IDWriteFactory7** adds new facilities for working with system fonts. |
| [**IDWriteFont**](https://msdn.microsoft.com/library/Dd368213(v=VS.85).aspx) | Represents a physical font in a font collection. This interface is used to create font faces from physical fonts, or to retrieve information such as font face metrics or face names from existing font faces. |
| [**IDWriteFont1**](https://msdn.microsoft.com/library/Hh780404(v=VS.85).aspx) | Represents a physical font in a font collection. |
| [**IDWriteFont2**](idwritefont2.md) | Represents a physical font in a font collection. |
| [**IDWriteFont3**](https://msdn.microsoft.com/library/Dn890766(v=VS.85).aspx) | Represents a font in a font collection. |
| [**IDWriteFontCollection**](https://msdn.microsoft.com/library/Dd368214(v=VS.85).aspx) | An object that encapsulates a set of fonts, such as the set of fonts installed on the system, or the set of fonts in a particular directory. The font collection API can be used to discover what font families and fonts are available, and to obtain some metadata about the fonts. |
| [**IDWriteFontCollection1**](https://msdn.microsoft.com/library/Dn933224(v=VS.85).aspx) | An object that encapsulates a set of fonts, such as the set of fonts installed on the system, or the set of fonts in a particular directory. The font collection API can be used to discover what font families and fonts are available, and to obtain some metadata about the fonts. |
| [**IDWriteFontCollection2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontcollection2) | This interface encapsulates a set of fonts, such as the set of fonts installed on the system, or the set of fonts in a particular directory. |
| [**IDWriteFontCollection3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontcollection3) | This interface encapsulates a set of fonts, such as the set of fonts installed on the system, or the set of fonts in a particular directory. |
| [**IDWriteFontCollectionLoader**](https://msdn.microsoft.com/library/Dd368215(v=VS.85).aspx) | Used to construct a collection of fonts given a particular type of key.  |
| [**IDWriteFontDownloadListener**](https://msdn.microsoft.com/library/Dn890775(v=VS.85).aspx) | Application-defined callback interface that receives notifications from the font download queue ([**IDWriteFontDownloadQueue**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadqueue) interface). Callbacks will occur on the downloading thread, and objects must be prepared to handle calls on their methods from other threads at any time. |
| [**IDWriteFontDownloadQueue**](https://msdn.microsoft.com/library/Dn890778(v=VS.85).aspx) | Interface that enqueues download requests for remote fonts, characters, glyphs, and font fragments.  |
| [**IDWriteFontFace**](https://msdn.microsoft.com/library/Dd370983(v=VS.85).aspx) | This interface exposes various font data such as metrics, names, and glyph outlines. It contains font face type, appropriate file references, and face identification data. |
| [**IDWriteFontFace1**](https://msdn.microsoft.com/library/Hh780409(v=VS.85).aspx) | Contains font face type, appropriate file references, and face identification data.  |
| [**IDWriteFontFace2**](https://msdn.microsoft.com/library/Dn280454(v=VS.85).aspx) | This interface contains font face type, appropriate file references, and face identification data. It adds the ability to check whether a color rendering path is potentially necessary.  |
| [**IDWriteFontFace3**](https://msdn.microsoft.com/library/Dn894561(v=VS.85).aspx) | Contains font face type, appropriate file references, and face identification data. |
| [**IDWriteFontFace4**](https://msdn.microsoft.com/library/Mt725320(v=VS.85).aspx) | Contains font face type, appropriate file references, and face identification data. |
| [**IDWriteFontFace5**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontface5) | This interface contains font face type, appropriate file references, and face identification data. It adds new facilities such as comparing two font faces, retrieving font axis values, and retrieving the underlying font resource. |
| [**IDWriteFontFaceReference**](https://msdn.microsoft.com/library/Dn894576(v=VS.85).aspx) | Represents a reference to a font face. A uniquely identifying reference to a font, from which you can create a font face to query font metrics and use for rendering. A font face reference consists of a font file, font face index, and font face simulation. The file data may or may not be physically present on the local machine yet.  |
| [**IDWriteFontFaceReference1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference1) | Represents a reference to a font face. A uniquely identifying reference to a font, from which you can create a font face to query font metrics and use for rendering. |
| [**IDWriteFontFallback**](https://msdn.microsoft.com/library/Dn280474(v=VS.85).aspx) | Allows you to access fallback fonts from the font list. |
| [**IDWriteFontFallbackBuilder**](idwritefontfallbackbuilder.md) | Allows you to create Unicode font fallback mappings and create a font fall back object from those mappings. |
| [**IDWriteFontFamily**](https://msdn.microsoft.com/library/Dd371042(v=VS.85).aspx) | Represents a family of related fonts. |
| [**IDWriteFontFamily1**](https://msdn.microsoft.com/library/Dn894590(v=VS.85).aspx) | Represents a family of related fonts. |
| [**IDWriteFontFamily2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfamily2) | Represents a family of related fonts. **IDWriteFontFamily2** adds new facilities, including retrieving fonts by font axis values. |
| [**IDWriteFontFile**](https://msdn.microsoft.com/library/Dd371060(v=VS.85).aspx) | Represents a font file. Applications such as font managers or font viewers can call [**IDWriteFontFile::Analyze**](https://msdn.microsoft.com/library/Dd371099(v=VS.85).aspx) to find out if a particular file is a font file, and whether it is a font type that is supported by the font system. |
| [**IDWriteFontFileEnumerator**](https://msdn.microsoft.com/library/Dd371063(v=VS.85).aspx) | Encapsulates a collection of font files. The font system uses this interface to enumerate font files when building a font collection. |
| [**IDWriteFontFileLoader**](https://msdn.microsoft.com/library/Dd371075(v=VS.85).aspx) | Handles loading font file resources of a particular type from a font file reference key into a font file stream object.  |
| [**IDWriteFontFileStream**](https://msdn.microsoft.com/library/Dd371081(v=VS.85).aspx) | Loads font file data from a custom font file loader.  |
| [**IDWriteFontList**](https://msdn.microsoft.com/library/Dd371120(v=VS.85).aspx) | Represents a list of fonts. |
| [**IDWriteFontList1**](https://msdn.microsoft.com/library/Dn894594(v=VS.85).aspx) | Represents a list of fonts. |
| [**IDWriteFontList2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontlist2) | Represents a list of fonts. **IDWriteFontList2** adds new facilities, including retrieving the underlying font set used by the list. |
| [**IDWriteFontResource**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontresource) | nn-dwrite_3-idwritefontresource |
| [**IDWriteFontSet**](https://msdn.microsoft.com/library/Dn933235(v=VS.85).aspx) | Represents a font set. |
| [**IDWriteFontSet1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset1) | Represents a font set. |
| [**IDWriteFontSet2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset2) | Represents a font set. |
| [**IDWriteFontSet3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset3) | Represents a font set. |
| [**IDWriteFontSetBuilder**](https://msdn.microsoft.com/library/Dn933236(v=VS.85).aspx) | Contains methods for building a font set. |
| [**IDWriteFontSetBuilder1**](https://msdn.microsoft.com/library/Mt807690(v=VS.85).aspx) | Contains methods for building a font set. |
| [**IDWriteFontSetBuilder2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder2) | Contains methods for building a font set. |
| [**IDWriteGdiInterop**](https://msdn.microsoft.com/library/Dd371172(v=VS.85).aspx) | Provides interoperability with GDI, such as methods to convert a font face to a LOGFONT structure, or to convert a GDI font description into a font face. It is also used to create bitmap render target objects. |
| [**IDWriteGdiInterop1**](https://msdn.microsoft.com/library/Dn958415(v=VS.85).aspx) | Provides interoperability with GDI, such as methods to convert a font face to a LOGFONT structure, or to convert a GDI font description into a font face. It is also used to create bitmap render target objects. |
| [**IDWriteGeometrySink**](idwritegeometrysink.md) | [**IDWriteGeometrySink**](idwritegeometrysink.md) is a **typedef** of the [**ID2D1SimplifiedGeometrySink**](/windows/win32/api/d2d1/nn-d2d1-id2d1simplifiedgeometrysink) interface. Please see the [**ID2D1SimplifiedGeometrySink**](/windows/win32/api/d2d1/nn-d2d1-id2d1simplifiedgeometrysink) reference page for more information. |
| [**IDWriteGlyphRunAnalysis**](https://msdn.microsoft.com/library/Dd371188(v=VS.85).aspx) | Contains low-level information used to render a glyph run. |
| [**IDWriteInlineObject**](https://msdn.microsoft.com/library/Dd371221(v=VS.85).aspx) | Wraps an application-defined inline graphic, allowing DWrite to query metrics as if the graphic were a glyph inline with the text. |
| [**IDWriteInMemoryFontFileLoader**](https://msdn.microsoft.com/library/Mt807692(v=VS.85).aspx) | Represents a font file loader that can access in-memory fonts. |
| [**IDWriteLocalFontFileLoader**](idwritelocalfontfileloader.md) | A built-in implementation of the [**IDWriteFontFileLoader**](https://msdn.microsoft.com/library/Dd371075(v=VS.85).aspx) interface, that operates on local font files and exposes local font file information from the font file reference key. Font file references created using [**CreateFontFileReference**](https://msdn.microsoft.com/library/Dd368197(v=VS.85).aspx) use this font file loader. |
| [**IDWriteLocalizedStrings**](https://msdn.microsoft.com/library/Dd371250(v=VS.85).aspx) | Represents a collection of strings indexed by locale name. |
| [**IDWriteNumberSubstitution**](/windows/win32/DirectWrite/idwritenumbersubstitution) | Holds the appropriate digits and numeric punctuation for a specified locale. |
| [**IDWritePixelSnapping**](https://msdn.microsoft.com/library/Dd371274(v=VS.85).aspx) | Defines the pixel snapping properties such as pixels per DIP(device-independent pixel) and the current transform matrix of a text renderer. |
| [**IDWriteRemoteFontFileLoader**](https://msdn.microsoft.com/library/Mt807695(v=VS.85).aspx) | Represents a font file loader that can access remote (i.e., downloadable) fonts.  |
| [**IDWriteRemoteFontFileStream**](https://msdn.microsoft.com/library/Mt807699(v=VS.85).aspx) | Represents a font file stream, parts of which may be non-local.  |
| [**IDWriteRenderingParams**](https://msdn.microsoft.com/library/Dd371285(v=VS.85).aspx) | Represents text rendering settings such as ClearType level, enhanced contrast, and gamma correction for glyph rasterization and filtering. An application typically obtains a rendering parameters object by calling the [**IDWriteFactory::CreateMonitorRenderingParams**](https://msdn.microsoft.com/library/Dd368199(v=VS.85).aspx) method. |
| [**IDWriteRenderingParams1**](https://msdn.microsoft.com/library/Hh780422(v=VS.85).aspx) | Represents text rendering settings for glyph rasterization and filtering. |
| [**IDWriteRenderingParams2**](https://msdn.microsoft.com/library/Dn900387(v=VS.85).aspx) | Represents text rendering settings for glyph rasterization and filtering. |
| [**IDWriteRenderingParams3**](https://msdn.microsoft.com/library/Dn900389(v=VS.85).aspx) | Represents text rendering settings for glyph rasterization and filtering. |
| [**IDWriteStringList**](https://msdn.microsoft.com/library/Dn958421(v=VS.85).aspx) | Represents a collection of strings indexed by number. |
| [**IDWriteTextAnalysisSink**](https://msdn.microsoft.com/library/Dd371303(v=VS.85).aspx) | This interface is implemented by the text analyzer's client to receive the output of a given text analysis.  |
| [**IDWriteTextAnalysisSink1**](https://msdn.microsoft.com/library/Hh780424(v=VS.85).aspx) | The interface you implement to receive the output of the text analyzers. |
| [**IDWriteTextAnalysisSource**](https://msdn.microsoft.com/library/Dd371318(v=VS.85).aspx) | Implemented by the text analyzer's client to provide text to the analyzer. It allows the separation between the logical view of text as a continuous stream of characters identifiable by unique text positions, and the actual memory layout of potentially discrete blocks of text in the client's backing store.  |
| [**IDWriteTextAnalysisSource1**](https://msdn.microsoft.com/library/Hh780426(v=VS.85).aspx) | The interface you implement to provide needed information to the text analyzer, like the text and associated text properties. |
| [**IDWriteTextAnalyzer**](https://msdn.microsoft.com/library/Dd316607(v=VS.85).aspx) | Analyzes various text properties for complex script processing such as bidirectional (bidi) support for languages like Arabic, determination of line break opportunities, glyph placement, and number substitution. |
| [**IDWriteTextAnalyzer1**](https://msdn.microsoft.com/library/Hh780428(v=VS.85).aspx) | Analyzes various text properties for complex script processing. |
| [**IDWriteTextAnalyzer2**](idwritetextanalyzer2.md) | Analyzes various text properties for complex script processing. |
| [**IDWriteTextFormat**](https://msdn.microsoft.com/library/Dd316628(v=VS.85).aspx) | The [**IDWriteTextFormat**](https://msdn.microsoft.com/library/Dd316628(v=VS.85).aspx) interface describes the font and paragraph properties used to format text, and it describes locale information.  |
| [**IDWriteTextFormat1**](idwritetextformat1.md) | Describes the font and paragraph properties used to format text, and it describes locale information.  |
| [**IDWriteTextFormat2**](idwritetextformat2.md) | Describes the font and paragraph properties used to format text, and it describes locale information.  |
| [**IDWriteTextFormat3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritetextformat3) | Describes the font and paragraph properties used to format text, and it describes locale information. |
| [**IDWriteTextLayout**](https://msdn.microsoft.com/library/Dd316718(v=VS.85).aspx) | The [**IDWriteTextLayout**](https://msdn.microsoft.com/library/Dd316718(v=VS.85).aspx) interface represents a block of text after it has been fully analyzed and formatted. |
| [**IDWriteTextLayout1**](https://msdn.microsoft.com/library/Hh780438(v=VS.85).aspx) | Represents a block of text after it has been fully analyzed and formatted. |
| [**IDWriteTextLayout2**](idwritetextlayout2.md) | Represents a block of text after it has been fully analyzed and formatted. |
| [**IDWriteTextLayout3**](idwritetextlayout3.md) | Represents a block of text after it has been fully analyzed and formatted.  |
| [**IDWriteTextRenderer**](https://msdn.microsoft.com/library/Dd371523(v=VS.85).aspx) | Represents a set of application-defined callbacks that perform rendering of text, inline objects, and decorations such as underlines. |
| [**IDWriteTextRenderer1**](https://msdn.microsoft.com/library/Dn280513(v=VS.85).aspx) | Represents a set of application-defined callbacks that perform rendering of text, inline objects, and decorations such as underlines.  |
| [**IDWriteTypography**](https://msdn.microsoft.com/library/Dd371541(v=VS.85).aspx) | Represents a font typography setting. |
