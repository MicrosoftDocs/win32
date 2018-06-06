---
Description: You can use the GetGlyphOutline function to retrieve the outline of a glyph from a TrueType font.
ms.assetid: 9b255dfa-3c1d-4707-927d-a2d5f4117f6a
title: Retrieving Character Outlines
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Character Outlines

You can use the [GetGlyphOutline](/windows/desktop/api/Wingdi/nf-wingdi-getglyphoutlinea) function to retrieve the outline of a glyph from a TrueType font. The glyph outline returned by the [**GetGlyphOutline**](https://msdn.microsoft.com/08f06007-5b21-44ab-b234-21a58c94ed4e) function is for a grid-fitted glyph. (A grid-fitted glyph has been modified so that its bitmap image conforms as closely as possible to the original design of the glyph.) If your application requires an unmodified glyph outline, request the glyph outline for a character in a font whose size is equal to the font's em units. (To create a font with this size, set the **lfHeight** member of the [LOGFONT](/windows/desktop/api/Wingdi/ns-wingdi-taglogfonta) structure to the negative of the value of the **ntmSizeEM** member of the [NEWTEXTMETRIC](/windows/desktop/api/Wingdi/ns-wingdi-tagnewtextmetrica) structure.)

[**GetGlyphOutline**](https://msdn.microsoft.com/08f06007-5b21-44ab-b234-21a58c94ed4e) returns the outline as a bitmap or as a series of polylines and splines. When an application retrieves a glyph outline as a series of polylines and splines, the information is returned in a [TTPOLYGONHEADER](/windows/desktop/api/Wingdi/ns-wingdi-tagttpolygonheader) structure followed by as many [TTPOLYCURVE](/windows/desktop/api/Wingdi/ns-wingdi-tagttpolycurve) structures as required to describe the glyph. All points are returned as [POINTFX](/windows/desktop/api/Wingdi/ns-wingdi-tagpointfx) structures and represent absolute positions, not relative moves. The starting point specified by the **pfxStart** member of the [**TTPOLYGONHEADER**](https://msdn.microsoft.com/eea54aeb-7847-4393-87fa-86de93017be8) structure is the point where the outline for a contour begins. The [**TTPOLYCURVE**](https://msdn.microsoft.com/59a26aec-786e-471b-8e08-ddffb04874d6) structures that follow can be either polyline records or spline records.

To render a TrueType character outline, you must use both the polyline and the spline records. The system can render both polylines and splines easily. Each polyline and spline record contains as many sequential points as possible, to minimize the number of records returned.

The starting point specified in the [**TTPOLYGONHEADER**](https://msdn.microsoft.com/eea54aeb-7847-4393-87fa-86de93017be8) structure is always on the outline of the glyph. The specified point serves as both the starting and ending points for the contour.

This section provides information on the following topics.

-   [Polyline Records](polyline-records.md)
-   [Spline Records](spline-records.md)

 

 



