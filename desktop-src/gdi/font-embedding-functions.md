---
Description: The following functions are used with embedded Microsoft OpenType fonts.
ms.assetid: 8f47d7a5-db45-4a41-8af2-9fc6b373a531
title: Font Embedding Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Font Embedding Functions

The following functions are used with embedded Microsoft OpenType fonts.



| Function                                                                   | Description                                                                                                                                              |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*CFP\_ALLOCPROC*](/windows/win32/FontSub/nc-fontsub-cfp_allocproc?branch=master)                                      | Application-provided memory allocation function for CreateFontPackage and MergeFontPackage.                                                              |
| [*CFP\_FREEPROC*](/windows/win32/FontSub/nc-fontsub-cfp_freeproc?branch=master)                                        | Application-provided memory deallocation function for CreateFontPackage and MergeFontPackage.                                                            |
| [*CFP\_REALLOCPROC*](/windows/win32/FontSub/nc-fontsub-cfp_reallocproc?branch=master)                                  | Application-provided memory reallocation function for CreateFontPackage and MergeFontPackage.                                                            |
| [**CreateFontPackage**](/windows/win32/FontSub/nf-fontsub-createfontpackage?branch=master)                             | Creates a more compact version of a specified TrueType font, in order to pass it to a printer. The resulting font may be subsetted, compressed, or both. |
| [**MergeFontPackage**](/windows/win32/FontSub/nf-fontsub-mergefontpackage?branch=master)                               | Merges subset fonts created by CreateFontPackage.                                                                                                        |
| [*READEMBEDPROC*](/windows/win32/T2embapi/?branch=master)                                       | Client-provided callback function to read stream contents from a buffer.                                                                                 |
| [**TTCharToUnicode**](/windows/win32/T2embapi/nf-t2embapi-ttchartounicode?branch=master)                                 | Converts an array of 8-bit character code values to 16-bit Unicode values.                                                                               |
| [**TTDeleteEmbeddedFont**](/windows/win32/T2embapi/nf-t2embapi-ttdeleteembeddedfont?branch=master)                       | Releases memory used by an embedded font.                                                                                                                |
| [**TTEmbedFont**](/windows/win32/T2embapi/nf-t2embapi-ttembedfont?branch=master)                                         | Creates a font structure containing a subsetted wide character (16-bit) font, using a device context as the font-embedding information source.           |
| [**TTEmbedFontEx**](/windows/win32/T2embapi/nf-t2embapi-ttembedfontex?branch=master)                                     | Creates a font structure containing the subsetted UCS-4 character (32-bit) font, using a device context as the font-embedding information source.        |
| [**TTEmbedFontFromFileA**](/windows/win32/T2embapi/nf-t2embapi-ttembedfontfromfilea?branch=master)                       | Creates a font structure containing a subsetted wide-character (16-bit) font, using a file as the font-embedding information source.                     |
| [**TTEnableEmbeddingForFacename**](/windows/win32/T2embapi/nf-t2embapi-ttenableembeddingforfacename?branch=master)       | Adds or removes facenames from the typeface exclusion list.                                                                                              |
| [**TTGetEmbeddedFontInfo**](/windows/win32/T2embapi/nf-t2embapi-ttgetembeddedfontinfo?branch=master)                     | Retrieves information about an embedded font.                                                                                                            |
| [**TTGetEmbeddingType**](/windows/win32/T2embapi/nf-t2embapi-ttgetembeddingtype?branch=master)                           | Returns embedding privileges of a font.                                                                                                                  |
| [**TTGetNewFontName**](/windows/win32/T2embapi/nf-t2embapi-ttgetnewfontname?branch=master)                               | Creates a new name for an installed embedded font.                                                                                                       |
| [**TTIsEmbeddingEnabled**](/windows/win32/T2embapi/nf-t2embapi-ttisembeddingenabled?branch=master)                       | Determines if the typeface exclusion list contains a specified font.                                                                                     |
| [**TTIsEmbeddingEnabledForFacename**](/windows/win32/T2embapi/nf-t2embapi-ttisembeddingenabledforfacename?branch=master) | Determines whether embedding is enabled for a specified font.                                                                                            |
| [**TTLoadEmbeddedFont**](/windows/win32/T2embapi/nf-t2embapi-ttloadembeddedfont?branch=master)                           | Reads the embedded font from the document stream and installs it. Also allows a client to further restrict embedding privileges of the font.             |
| [**TTRunValidationTests**](/windows/win32/T2embapi/nf-t2embapi-ttrunvalidationtests?branch=master)                       | Validates part or all glyph data of a wide-character (16-bit) font, in the size range specified.                                                         |
| [**TTRunValidationTestsEx**](/windows/win32/T2embapi/nf-t2embapi-ttrunvalidationtestsex?branch=master)                   | UCS-4 version of TTRunValidationTests.                                                                                                                   |
| [*WRITEEMBEDPROC*](/windows/win32/T2embapi/?branch=master)                                     | Client-provided callback function to write stream contents to a buffer.                                                                                  |



 

 

 



