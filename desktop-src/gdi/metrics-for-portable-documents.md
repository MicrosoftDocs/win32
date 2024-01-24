---
description: The following table specifies the most important font metrics for applications that require portable documents and the functions that allow an application to retrieve them.
ms.assetid: 61f6d244-7397-42af-af58-0ab9d07bf19e
title: Metrics for Portable Documents
ms.topic: article
ms.date: 05/31/2018
---

# Metrics for Portable Documents

The following table specifies the most important font metrics for applications that require portable documents and the functions that allow an application to retrieve them.



| Function                                               | Metric                | Use                                                                                                          |
|--------------------------------------------------------|-----------------------|--------------------------------------------------------------------------------------------------------------|
| [**EnumFontFamilies**](/windows/desktop/api/Wingdi/nf-wingdi-enumfontfamiliesa)           | **ntmSizeEM**         | Retrieval of design metrics; conversion to device metrics.                                                   |
| [**GetCharABCWidths**](/windows/desktop/api/Wingdi/nf-wingdi-getcharabcwidthsa)           | **ABCWidths**         | Accurate placement of characters at the start and end of margins, picture boundaries, and other text breaks. |
| [**GetCharWidth32**](/windows/desktop/api/Wingdi/nf-wingdi-getcharwidth32a)               | **AdvanceWidths**     | Placement of characters on a line.                                                                           |
| [**GetOutlineTextMetrics**](/windows/desktop/api/Wingdi/nf-wingdi-getoutlinetextmetricsa) | **otmfsType**         | Font-embedding bits.                                                                                         |
|                                                        | **otmsCharSlopeRise** | Y-component for slope of cursor for italic fonts.                                                            |
|                                                        | **otmsCharSlopeRun**  | X-component for slope of cursor for italic fonts.                                                            |
|                                                        | **otmAscent**         | Line spacing.                                                                                                |
|                                                        | **otmDescent**        | Line spacing.                                                                                                |
|                                                        | **otmLineGap**        | Line spacing.                                                                                                |
|                                                        | **otmpFamilyName**    | Font identification.                                                                                         |
|                                                        | **otmpStyleName**     | Font identification.                                                                                         |
|                                                        | **otmpFullName**      | Font identification (typically, family and style name).                                                      |



 

The **otmsCharSlopeRise**, **otmsCharSlopeRun**, **otmAscent**, **otmDescent**, and **otmLineGap** members of the [OUTLINETEXTMETRIC](/windows/desktop/api/Wingdi/ns-wingdi-outlinetextmetrica) structure are scaled or transformed to correspond to the current device mode and physical height (as specified in the **tmHeight** member of the [NEWTEXTMETRIC](/windows/win32/api/wingdi/ns-wingdi-newtextmetrica) structure).

Font identification is important in those instances when an application must select the same font, for example, when a document is reopened or moved to a different operating system. The font mapper always selects the correct font when an application requests a font by full name. The family and style names provide input to the standard font dialog box, which ensures that the selection bars are properly placed.

The **otmsCharSlopeRise** and **otmsCharSlopeRun** values are used to produce a close approximation of the main italic angle of the font. For typical roman fonts, **otmsCharSlopeRise** is 1 and **otmsCharSlopeRun** is 0. For italic fonts, the values attempt to approximate the sine and cosine of the main italic angle of the font (in counterclockwise degrees past vertical); note that the italic angle for upright fonts is 0. Because these values are not expressed in design units, they should not be converted into device units.

The character placement and line spacing metrics enable an application to compute device-independent line breaks that are portable across screens, printers, typesetters, and even platforms.

**To perform device-independent page layout**

1.  Normalize all design metrics to a common ultra-high resolution (UHR) value (for example, 65,536 DPI); this prevents round-off errors.
2.  Compute line breaks based on UHR metrics and physical page width; this yields a starting point and an ending point of a line within the text stream.
3.  Compute the device page width in device units (for example, pixels).
4.  Fit each line of text into the device page width, using the line breaks computed in step 2.
5.  Compute page breaks by using UHR metrics and the physical page length; this yields the number of lines per page.
6.  Compute the line heights in device units.
7.  Fit the lines of text onto the page, using the lines per page from step 5 and the line heights from step 6.

If all applications adopt these techniques, developers can virtually guarantee that documents moved from one application to another will retain their original appearance and format.

 

 



