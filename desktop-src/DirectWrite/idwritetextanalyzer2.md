---
title: IDWriteTextAnalyzer2 interface
description: Analyzes various text properties for complex script processing.
ms.assetid: '62DF6E71-F99D-47E9-A9BE-2A481A60AEDD'
keywords: ["IDWriteTextAnalyzer2 interface Direct Write", "IDWriteTextAnalyzer2 interface Direct Write , described"]
topic_type:
- apiref
api_name:
- IDWriteTextAnalyzer2
api_location:
- dwrite.dll
api_type:
- COM
---

# IDWriteTextAnalyzer2 interface

Analyzes various text properties for complex script processing.

## Members

The **IDWriteTextAnalyzer2** interface inherits from [**IDWriteTextAnalyzer1**](idwritetextanalyzer1.md). **IDWriteTextAnalyzer2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDWriteTextAnalyzer2** interface has these methods.



| Method                                                                                    | Description                                                                             |
|:------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| [**CheckTypographicFeature**](idwritetextanalyzer2-checktypographicfeature.md)           | Checks if a typographic feature is available for a glyph or a set of glyphs.<br/> |
| [**GetGlyphOrientationTransform**](idwritetextanalyzer2-getglyphorientationtransform.md) | Returns 2x3 transform matrix for the respective angle to draw the glyph run.<br/> |
| [**GetTypographicFeatures**](idwritetextanalyzer2-gettypographicfeatures.md)             | Returns a complete list of OpenType features available for a script or font.<br/> |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



## See also

<dl> <dt>

[**IDWriteTextAnalyzer1**](idwritetextanalyzer1.md)
</dt> </dl>

 

 





