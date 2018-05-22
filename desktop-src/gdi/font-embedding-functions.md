---
Description: 'The following functions are used with embedded Microsoft OpenType fonts.'
ms.assetid: '8f47d7a5-db45-4a41-8af2-9fc6b373a531'
title: Font Embedding Functions
---

# Font Embedding Functions

The following functions are used with embedded Microsoft OpenType fonts.



| Function                                                                   | Description                                                                                                                                              |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*CFP\_ALLOCPROC*](cfp-allocproc.md)                                      | Application-provided memory allocation function for CreateFontPackage and MergeFontPackage.                                                              |
| [*CFP\_FREEPROC*](cfp-freeproc.md)                                        | Application-provided memory deallocation function for CreateFontPackage and MergeFontPackage.                                                            |
| [*CFP\_REALLOCPROC*](cfp-reallocproc.md)                                  | Application-provided memory reallocation function for CreateFontPackage and MergeFontPackage.                                                            |
| [**CreateFontPackage**](createfontpackage.md)                             | Creates a more compact version of a specified TrueType font, in order to pass it to a printer. The resulting font may be subsetted, compressed, or both. |
| [**MergeFontPackage**](mergefontpackage.md)                               | Merges subset fonts created by CreateFontPackage.                                                                                                        |
| [*READEMBEDPROC*](readembedproc.md)                                       | Client-provided callback function to read stream contents from a buffer.                                                                                 |
| [**TTCharToUnicode**](ttchartounicode.md)                                 | Converts an array of 8-bit character code values to 16-bit Unicode values.                                                                               |
| [**TTDeleteEmbeddedFont**](ttdeleteembeddedfont.md)                       | Releases memory used by an embedded font.                                                                                                                |
| [**TTEmbedFont**](ttembedfont.md)                                         | Creates a font structure containing a subsetted wide character (16-bit) font, using a device context as the font-embedding information source.           |
| [**TTEmbedFontEx**](ttembedfontex.md)                                     | Creates a font structure containing the subsetted UCS-4 character (32-bit) font, using a device context as the font-embedding information source.        |
| [**TTEmbedFontFromFileA**](ttembedfontfromfilea.md)                       | Creates a font structure containing a subsetted wide-character (16-bit) font, using a file as the font-embedding information source.                     |
| [**TTEnableEmbeddingForFacename**](ttenableembeddingforfacename.md)       | Adds or removes facenames from the typeface exclusion list.                                                                                              |
| [**TTGetEmbeddedFontInfo**](ttgetembeddedfontinfo.md)                     | Retrieves information about an embedded font.                                                                                                            |
| [**TTGetEmbeddingType**](ttgetembeddingtype.md)                           | Returns embedding privileges of a font.                                                                                                                  |
| [**TTGetNewFontName**](ttgetnewfontname.md)                               | Creates a new name for an installed embedded font.                                                                                                       |
| [**TTIsEmbeddingEnabled**](ttisembeddingenabled.md)                       | Determines if the typeface exclusion list contains a specified font.                                                                                     |
| [**TTIsEmbeddingEnabledForFacename**](ttisembeddingenabledforfacename.md) | Determines whether embedding is enabled for a specified font.                                                                                            |
| [**TTLoadEmbeddedFont**](ttloadembeddedfont.md)                           | Reads the embedded font from the document stream and installs it. Also allows a client to further restrict embedding privileges of the font.             |
| [**TTRunValidationTests**](ttrunvalidationtests.md)                       | Validates part or all glyph data of a wide-character (16-bit) font, in the size range specified.                                                         |
| [**TTRunValidationTestsEx**](ttrunvalidationtestsex.md)                   | UCS-4 version of TTRunValidationTests.                                                                                                                   |
| [*WRITEEMBEDPROC*](writeembedproc.md)                                     | Client-provided callback function to write stream contents to a buffer.                                                                                  |



 

 

 



