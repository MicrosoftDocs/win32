---
description: The following functions are used with embedded Microsoft OpenType fonts.
ms.assetid: 8f47d7a5-db45-4a41-8af2-9fc6b373a531
title: Font Embedding Functions
ms.topic: article
ms.date: 05/31/2018
---

# Font Embedding Functions

The following functions are used with embedded Microsoft OpenType fonts.



| Function                                                                   | Description                                                                                                                                              |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*CFP\_ALLOCPROC*](/windows/desktop/api/FontSub/nc-fontsub-cfp_allocproc)                                      | Application-provided memory allocation function for CreateFontPackage and MergeFontPackage.                                                              |
| [*CFP\_FREEPROC*](/windows/desktop/api/FontSub/nc-fontsub-cfp_freeproc)                                        | Application-provided memory deallocation function for CreateFontPackage and MergeFontPackage.                                                            |
| [*CFP\_REALLOCPROC*](/windows/desktop/api/FontSub/nc-fontsub-cfp_reallocproc)                                  | Application-provided memory reallocation function for CreateFontPackage and MergeFontPackage.                                                            |
| [**CreateFontPackage**](/windows/desktop/api/FontSub/nf-fontsub-createfontpackage)                             | Creates a more compact version of a specified TrueType font, in order to pass it to a printer. The resulting font may be subsetted, compressed, or both. |
| [**MergeFontPackage**](/windows/desktop/api/FontSub/nf-fontsub-mergefontpackage)                               | Merges subset fonts created by CreateFontPackage.                                                                                                        |
| [*READEMBEDPROC*](/previous-versions//dd162894(v=vs.85))                                       | Client-provided callback function to read stream contents from a buffer.                                                                                 |
| [**TTCharToUnicode**](/windows/desktop/api/T2embapi/nf-t2embapi-ttchartounicode)                                 | Converts an array of 8-bit character code values to 16-bit Unicode values.                                                                               |
| [**TTDeleteEmbeddedFont**](/windows/desktop/api/T2embapi/nf-t2embapi-ttdeleteembeddedfont)                       | Releases memory used by an embedded font.                                                                                                                |
| [**TTEmbedFont**](/windows/desktop/api/T2embapi/nf-t2embapi-ttembedfont)                                         | Creates a font structure containing a subsetted wide character (16-bit) font, using a device context as the font-embedding information source.           |
| [**TTEmbedFontEx**](/windows/desktop/api/T2embapi/nf-t2embapi-ttembedfontex)                                     | Creates a font structure containing the subsetted UCS-4 character (32-bit) font, using a device context as the font-embedding information source.        |
| [**TTEmbedFontFromFileA**](/windows/desktop/api/T2embapi/nf-t2embapi-ttembedfontfromfilea)                       | Creates a font structure containing a subsetted wide-character (16-bit) font, using a file as the font-embedding information source.                     |
| [**TTEnableEmbeddingForFacename**](/windows/desktop/api/T2embapi/nf-t2embapi-ttenableembeddingforfacename)       | Adds or removes facenames from the typeface exclusion list.                                                                                              |
| [**TTGetEmbeddedFontInfo**](/windows/desktop/api/T2embapi/nf-t2embapi-ttgetembeddedfontinfo)                     | Retrieves information about an embedded font.                                                                                                            |
| [**TTGetEmbeddingType**](/windows/desktop/api/T2embapi/nf-t2embapi-ttgetembeddingtype)                           | Returns embedding privileges of a font.                                                                                                                  |
| [**TTGetNewFontName**](/windows/desktop/api/T2embapi/nf-t2embapi-ttgetnewfontname)                               | Creates a new name for an installed embedded font.                                                                                                       |
| [**TTIsEmbeddingEnabled**](/windows/desktop/api/T2embapi/nf-t2embapi-ttisembeddingenabled)                       | Determines if the typeface exclusion list contains a specified font.                                                                                     |
| [**TTIsEmbeddingEnabledForFacename**](/windows/desktop/api/T2embapi/nf-t2embapi-ttisembeddingenabledforfacename) | Determines whether embedding is enabled for a specified font.                                                                                            |
| [**TTLoadEmbeddedFont**](/windows/desktop/api/T2embapi/nf-t2embapi-ttloadembeddedfont)                           | Reads the embedded font from the document stream and installs it. Also allows a client to further restrict embedding privileges of the font.             |
| [**TTRunValidationTests**](/windows/desktop/api/T2embapi/nf-t2embapi-ttrunvalidationtests)                       | Validates part or all glyph data of a wide-character (16-bit) font, in the size range specified.                                                         |
| [**TTRunValidationTestsEx**](/windows/desktop/api/T2embapi/nf-t2embapi-ttrunvalidationtestsex)                   | UCS-4 version of TTRunValidationTests.                                                                                                                   |
| [*WRITEEMBEDPROC*](/previous-versions//dd145225(v=vs.85))                                     | Client-provided callback function to write stream contents to a buffer.                                                                                  |



 

 

 
