---
title: Property Identifiers (Windows Controls)
description: This topic contains information about defined values that are used to retrieve properties of visual styles. The definitions are found in Vssym32.h.
ms.assetid: b0e22022-fea9-43d1-8ef0-7a1c518760f1
ms.topic: article
ms.date: 05/31/2018
---

# Property Identifiers (Windows Controls)

This topic contains information about defined values that are used to retrieve properties of visual styles. The definitions are found in Vssym32.h.

## Property Types

The following table lists the primitive property types. The values in the first column are not normally used by applications but provide a means of classifying property identifiers.



| Data Type       | Description                              | Returned Type                          | Retrieval Function                                                                                                     |
|-----------------|------------------------------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| TMT\_BOOL       | **TRUE** or **FALSE**                    | Boolean                                | [**GetThemeBool**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemebool), [**GetThemeSysBool**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemesysbool)                                       |
| TMT\_COLOR      | RGB color value                          | [**COLORREF**](/windows/desktop/gdi/colorref) structure | [**GetThemeColor**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemecolor), [**GetThemeSysColor**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemesyscolor)                                   |
| TMT\_DISKSTREAM | Disk stream                              | **HINSTANCE**                          | [**GetThemeStream**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemestream)                                                                               |
| TMT\_ENUM       | Enumerated value                         | Enumeration                            | [**GetThemeEnumValue**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemeenumvalue).                                                                        |
| TMT\_FILENAME   | Filename relative to the theme directory | **WCHAR** array                        | [**GetThemeFilename**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemefilename)                                                                           |
| TMT\_FONT       | Font description                         | [**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta) structure   | [**GetThemeFont**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemefont), [**GetThemeSysFont**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemesysfont)                                       |
| TMT\_HBITMAP    | Bitmap                                   | **HBITMAP** handle                     | [**GetThemeBitmap**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemebitmap)                                                                               |
| TMT\_INT        | Signed number                            | Integer                                | [**GetThemeInt**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemeint), [**GetThemeSysInt**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemesysint), [**GetThemeMetric**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthememetric) |
| TMT\_INTLIST    | List of integers                         | [**INTLIST**](/windows/desktop/api/UxTheme/ns-uxtheme-intlist) structure   | [**GetThemeIntList**](/windows/desktop/api/UxTheme/nf-uxtheme-getthemeintlist)                                                                             |
| TMT\_MARGINS    | Margins: left, top, right, and bottom    | [**MARGINS**](/windows/desktop/api/Uxtheme/ns-uxtheme-margins) structure   | [**GetThemeMargins**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthememargins)                                                                             |
| TMT\_POSITION   | Location of an item                      | [**POINT**](/previous-versions//dd162805(v=vs.85)) structure       | [**GetThemePosition**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemeposition)                                                                           |
| TMT\_RECT       | Size and location of a rectangle         | [**RECT**](/previous-versions//dd162897(v=vs.85)) structure         | [**GetThemeRect**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemerect)                                                                                   |
| TMT\_SIZE       | Size of an item                          | [**SIZE**](/previous-versions//dd145106(v=vs.85)) structure         | [**GetThemePartSize**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemepartsize)                                                                           |
| TMT\_STRING     | Unicode string                           | **WCHAR** array                        | [**GetThemeString**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemestring), [**GetThemeSysString**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemesysstring)                               |



 

## Property IDs

The following are the defined values for theme properties, grouped by data type.

**TMT\_BOOL**



| ID                        | Notes                                                                                                                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TMT\_ALWAYSSHOWSIZINGBAR  | **TRUE** if the sizing bar associated with the part and state should always be shown.                                                                                                                           |
| TMT\_AUTOSIZE             | **TRUE** if the nonclient caption area associated with the part and state vary with text width.                                                                                                                 |
| TMT\_BGFILL               | **TRUE** if true-sized images associated with the part and state are to be drawn on the background fill.                                                                                                        |
| TMT\_BORDERONLY           | **TRUE** if the image associated with the part and state should only have its border drawn.                                                                                                                     |
| TMT\_COMPOSITED           | **TRUE** if the control associated with the part and state will handle its own compositing of images.                                                                                                           |
| TMT\_COMPOSITEDOPAQUE     |                                                                                                                                                                                                                 |
| TMT\_DRAWBORDERS          |                                                                                                                                                                                                                 |
| TMT\_FLATMENUS            | See [**GetThemeSysBool**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemesysbool).                                                                                                                                                                 |
| TMT\_GLYPHONLY            | **TRUE** if the glyph associated with the part and state should be drawn without a background.                                                                                                                  |
| TMT\_GLYPHTRANSPARENT     | **TRUE** if the glyph associated with the part and state have transparent areas. See [**GetThemeColor**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemecolor) for the definition of the TMT\_GLYPHCOLOR value that defines the transparent color. |
| TMT\_INTEGRALSIZING       | **TRUE** if the truesize image or border associated with the part and state must be sized to a factor of 2.                                                                                                     |
| TMT\_LOCALIZEDMIRRORIMAGE |                                                                                                                                                                                                                 |
| TMT\_MIRRORIMAGE          | **TRUE** if the image associated with the part and state should be flipped if the window is being viewed in right-to-left reading mode.                                                                         |
| TMT\_NOETCHEDEFFECT       |                                                                                                                                                                                                                 |
| TMT\_SCALEDBACKGROUND     |                                                                                                                                                                                                                 |
| TMT\_SOURCEGROW           | **TRUE** if the image associated with the part and state will scale larger in size if necessary.                                                                                                                |
| TMT\_SOURCESHRINK         | **TRUE** if the image associated with the part and state will scale smaller in size if necessary.                                                                                                               |
| TMT\_TEXTAPPLYOVERLAY     |                                                                                                                                                                                                                 |
| TMT\_TEXTGLOW             |                                                                                                                                                                                                                 |
| TMT\_TEXTITALIC           |                                                                                                                                                                                                                 |
| TMT\_TRANSPARENT          |                                                                                                                                                                                                                 |
| TMT\_UNIFORMSIZING        | **TRUE** if the image associated with the part and state must have equal height and width.                                                                                                                      |
| TMT\_USERPICTURE          | **TRUE** if the image associated with the part and state is based on the current user.                                                                                                                          |



 

**TMT\_COLOR**



| ID                           | Notes                                                                                                                                                                                          |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TMT\_ACCENTCOLORHINT         | The color used as an accent color hint for custom controls.                                                                                                                                    |
| TMT\_ACTIVEBORDER            |                                                                                                                                                                                                |
| TMT\_ACTIVECAPTION           |                                                                                                                                                                                                |
| TMT\_APPWORKSPACE            |                                                                                                                                                                                                |
| TMT\_BACKGROUND              |                                                                                                                                                                                                |
| TMT\_BLENDCOLOR              | The color used as a blend color.                                                                                                                                                               |
| TMT\_BODYTEXTCOLOR           |                                                                                                                                                                                                |
| TMT\_BORDERCOLOR             | The color of the border associated with the part and state.                                                                                                                                    |
| TMT\_BORDERCOLORHINT         | The color used as a border color hint for custom controls.                                                                                                                                     |
| TMT\_BTNFACE                 |                                                                                                                                                                                                |
| TMT\_BTNHIGHLIGHT            |                                                                                                                                                                                                |
| TMT\_BTNSHADOW               |                                                                                                                                                                                                |
| TMT\_BTNTEXT                 |                                                                                                                                                                                                |
| TMT\_BUTTONALTERNATEFACE     |                                                                                                                                                                                                |
| TMT\_CAPTIONTEXT             |                                                                                                                                                                                                |
| TMT\_DKSHADOW3D              |                                                                                                                                                                                                |
| TMT\_EDGEDKSHADOWCOLOR       | The dark shadow color of the edge associated with this part and state.                                                                                                                         |
| TMT\_EDGEFILLCOLOR           | The fill color of the edge associated with this part and state.                                                                                                                                |
| TMT\_EDGEHIGHLIGHTCOLOR      | The highlight color of the edge associated with this part and state.                                                                                                                           |
| TMT\_EDGELIGHTCOLOR          | The light color of the edge associated with this part and state.                                                                                                                               |
| TMT\_EDGESHADOWCOLOR         | The shadow color of the edge associated with this part and state.                                                                                                                              |
| TMT\_FILLCOLOR               | The color of the background fill associated with the part and state.                                                                                                                           |
| TMT\_FILLCOLORHINT           | The color used as a fill color hint for custom controls.                                                                                                                                       |
| TMT\_FROMCOLOR1              |                                                                                                                                                                                                |
| TMT\_FROMCOLOR2              |                                                                                                                                                                                                |
| TMT\_FROMCOLOR3              |                                                                                                                                                                                                |
| TMT\_FROMCOLOR4              |                                                                                                                                                                                                |
| TMT\_FROMCOLOR5              |                                                                                                                                                                                                |
| TMT\_GLOWCOLOR               | The color of the glow produced by calling [**DrawThemeIcon**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemeicon) using this part and state.                                                                                    |
| TMT\_GLYPHTEXTCOLOR          | The color that the font-based glyph associated with this part and state will use.                                                                                                              |
| TMT\_GLYPHTRANSPARENTCOLOR   | The transparent glyph color associated with this part and state. If the TMT\_GLYPHTRANSPARENT value for this part and state is **TRUE**, parts of the glyph that use this color are not drawn. |
| TMT\_GRADIENTACTIVECAPTION   |                                                                                                                                                                                                |
| TMT\_GRADIENTCOLOR1          | The first color of the gradient associated with this part and state.                                                                                                                           |
| TMT\_GRADIENTCOLOR2          | The second color of the gradient.                                                                                                                                                              |
| TMT\_GRADIENTCOLOR3          | The third color of the gradient.                                                                                                                                                               |
| TMT\_GRADIENTCOLOR4          | The fourth color of the gradient.                                                                                                                                                              |
| TMT\_GRADIENTCOLOR5          | The fifth color of the gradient.                                                                                                                                                               |
| TMT\_GRADIENTINACTIVECAPTION |                                                                                                                                                                                                |
| TMT\_GRAYTEXT                |                                                                                                                                                                                                |
| TMT\_HEADING1TEXTCOLOR       |                                                                                                                                                                                                |
| TMT\_HEADING2TEXTCOLOR       |                                                                                                                                                                                                |
| TMT\_HIGHLIGHT               |                                                                                                                                                                                                |
| TMT\_HIGHLIGHTTEXT           |                                                                                                                                                                                                |
| TMT\_HOTTRACKING             |                                                                                                                                                                                                |
| TMT\_INACTIVEBORDER          |                                                                                                                                                                                                |
| TMT\_INACTIVECAPTION         |                                                                                                                                                                                                |
| TMT\_INACTIVECAPTIONTEXT     |                                                                                                                                                                                                |
| TMT\_INFOBK                  |                                                                                                                                                                                                |
| TMT\_INFOTEXT                |                                                                                                                                                                                                |
| TMT\_LIGHT3D                 |                                                                                                                                                                                                |
| TMT\_MENU                    |                                                                                                                                                                                                |
| TMT\_MENUBAR                 |                                                                                                                                                                                                |
| TMT\_MENUHILIGHT             |                                                                                                                                                                                                |
| TMT\_MENUTEXT                |                                                                                                                                                                                                |
| TMT\_SCROLLBAR               |                                                                                                                                                                                                |
| TMT\_SHADOWCOLOR             | The color of the shadow drawn underneath text associated with this part and state.                                                                                                             |
| TMT\_TEXTBORDERCOLOR         | The color of the text border associated with this part and state.                                                                                                                              |
| TMT\_TEXTCOLOR               | The color of the text associated with this part and state.                                                                                                                                     |
| TMT\_TEXTCOLORHINT           |                                                                                                                                                                                                |
| TMT\_TEXTSHADOWCOLOR         | The color of the text shadow associated with this part and state.                                                                                                                              |
| TMT\_TRANSPARENTCOLOR        | The transparent color associated with this part and state. If the TMT\_TRANSPARENT value for this part and state is **TRUE**, parts of the graphic that use this color are not drawn.          |
| TMT\_WINDOW                  |                                                                                                                                                                                                |
| TMT\_WINDOWFRAME             |                                                                                                                                                                                                |
| TMT\_WINDOWTEXT              |                                                                                                                                                                                                |



 

**TMT\_DISKSTREAM**



| ID              | Notes |
|-----------------|-------|
| TMT\_ATLASIMAGE |       |



 

**TMT\_ENUM**



| Enumeration         | Property Values                                                                                                                                                                                                                                            | Notes                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| BGTYPE              | BT\_IMAGEFILE, BT\_BORDERFILL                                                                                                                                                                                                                              | The basic drawing type for this part.                                                                                                                |
| BORDERTYPE          | BT\_RECT, BT\_ROUNDRECT, BT\_ELLIPSE                                                                                                                                                                                                                       | The type of border drawn if this part is a border fill.                                                                                              |
| CONTENTALIGNMENT    | CA\_LEFT, CA\_CENTER, CA\_RIGHT                                                                                                                                                                                                                            | The alignment of text in the caption associated with this part.                                                                                      |
| FILLTYPE            | FT\_SOLID, FT\_VERTGRADIENT, FT\_HORZGRADIENT, FT\_RADIALGRADIENT, FT\_TILEIMAGE                                                                                                                                                                           | The type of fill shape drawn if this part is a border fill.                                                                                          |
| GLYPHTYPE           | GT\_NONE, GT\_IMAGEGLYPH, GT\_FONTGLYPH                                                                                                                                                                                                                    | The type of glyph drawn on this part.                                                                                                                |
| GLYPHFONTSIZINGTYPE | GFST\_NONE, GFST\_SIZE, GFST\_DPI                                                                                                                                                                                                                          | The type of method used to select between different-sized glyphs.                                                                                    |
| HALIGN              | HA\_LEFT, HA\_CENTER, HA\_RIGHT                                                                                                                                                                                                                            | The horizontal alignment if this part uses a true-size image.                                                                                        |
| ICONEFFECT          | ICE\_NONE, ICE\_GLOW, ICE\_SHADOW, ICE\_PULSE, ICE\_ALPHA                                                                                                                                                                                                  | The type of effect to be displayed when this part is drawn using [**DrawThemeIcon**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemeicon).                                             |
| IMAGELAYOUT         | IL\_VERTICAL, IL\_HORIZONTAL                                                                                                                                                                                                                               | The type of alignment used when multiple images are drawn.                                                                                           |
| IMAGESELECTTYPE     | IST\_NONE, IST\_SIZE, IST\_DPI                                                                                                                                                                                                                             | The type of method used to select between sized images for this part. See the TMT\_IMAGEFILE1 value of [**GetThemeFilename**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemefilename). |
| OFFSETTYPE          | OT\_TOPLEFT, OT\_TOPRIGHT, OT\_TOPMIDDLE, OT\_BOTTOMLEFT, OT\_BOTTOMRIGHT, OT\_BOTTOMMIDDLE, OT\_MIDDLELEFT, OT\_MIDDLERIGHT, OT\_LEFTOFCAPTION, OT\_RIGHTOFCAPTION, OT\_LEFTOFLASTBUTTON, OT\_RIGHTOFLASTBUTTON, OT\_ABOVELASTBUTTON, OT\_BELOWLASTBUTTON | The alignment of this part on the window.                                                                                                            |
| SIZINGTYPE          | ST\_TRUESIZE, ST\_STRETCH, ST\_TILE, ST\_TILEHORZ, ST\_TILEVERT, ST\_TILECENTER                                                                                                                                                                            | The method used to size an image if this part uses an image file.                                                                                    |
| TEXTSHADOWTYPE      | TST\_NONE, TST\_SINGLE, TST\_CONTINUOUS                                                                                                                                                                                                                    | The type of shadow effect to draw behind text associated with this part.                                                                             |
| TRUESIZESCALINGTYPE | TSST\_NONE, TSST\_SIZE, TSST\_DPI                                                                                                                                                                                                                          | The type of scaling used if this part uses a true-sized image.                                                                                       |
| VALIGN              | VA\_TOP, VA\_CENTER, VA\_BOTTOM                                                                                                                                                                                                                            | The vertical alignment if this part uses a true-size image.                                                                                          |



 

**TMT\_FILENAME**



| ID                  | Notes                                                                                                                                        |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| TMT\_GLYPHIMAGEFILE | The filename for the glyph image associated with this part and state.                                                                        |
| TMT\_IMAGEFILE      | The filename of the image associated with this part and state, or the base filename for multiple images associated with this part and state. |
| TMT\_IMAGEFILE1     | The filename of the first scaled image associated with this part and state, for support of different resolutions.                            |
| TMT\_IMAGEFILE2     | The filename of the second scaled image.                                                                                                     |
| TMT\_IMAGEFILE3     | The filename of the third scaled image.                                                                                                      |
| TMT\_IMAGEFILE4     | The filename of the fourth scaled image.                                                                                                     |
| TMT\_IMAGEFILE5     | The filename of the fifth scaled image.                                                                                                      |



 

**TMT\_FONT**



| ID                    | Notes                                                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------|
| TMT\_BODYFONT         |                                                                                                      |
| TMT\_CAPTIONFONT      |                                                                                                      |
| TMT\_GLYPHFONT        | The font that the glyph associated with this part will be drawn with, if font-based glyphs are used. |
| TMT\_HEADING1FONT     |                                                                                                      |
| TMT\_HEADING2FONT     |                                                                                                      |
| TMT\_ICONTITLEFONT    |                                                                                                      |
| TMT\_MENUFONT         |                                                                                                      |
| TMT\_MSGBOXFONT       |                                                                                                      |
| TMT\_SMALLCAPTIONFONT |                                                                                                      |
| TMT\_STATUSFONT       |                                                                                                      |



 

**TMT\_INT**



| ID                       | Notes                                                                                                                                                                                                            |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TMT\_ALPHALEVEL          | The alpha value (0-255) used for [**DrawThemeIcon**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemeicon).                                                                                                                                         |
| TMT\_ALPHATHRESHOLD      | The minimum alpha value (0-255) that a pixel must have to be considered opaque.                                                                                                                                  |
| TMT\_ANIMATIONDELAY      |                                                                                                                                                                                                                  |
| TMT\_ANIMATIONDURATION   |                                                                                                                                                                                                                  |
| TMT\_BORDERSIZE          | The thickness of the border drawn if this part uses a border fill.                                                                                                                                               |
| TMT\_CHARSET             |                                                                                                                                                                                                                  |
| TMT\_COLORIZATIONCOLOR   |                                                                                                                                                                                                                  |
| TMT\_COLORIZATIONOPACITY |                                                                                                                                                                                                                  |
| TMT\_FRAMESPERSECOND     |                                                                                                                                                                                                                  |
| TMT\_FROMHUE1            |                                                                                                                                                                                                                  |
| TMT\_FROMHUE2            |                                                                                                                                                                                                                  |
| TMT\_FROMHUE3            |                                                                                                                                                                                                                  |
| TMT\_FROMHUE4            |                                                                                                                                                                                                                  |
| TMT\_FROMHUE5            |                                                                                                                                                                                                                  |
| TMT\_GLOWINTENSITY       |                                                                                                                                                                                                                  |
| TMT\_GLYPHINDEX          | The character index into the selected font that will be used for the glyph, if the part uses a font-based glyph.                                                                                                 |
| TMT\_GRADIENTRATIO1      | The amount of the first gradient color (TMT\_GRADIENTCOLOR1) to use in drawing the part. This value can be from 0 to 255, but this value plus the values of each of the GRADIENTRATIO values must add up to 255. |
| TMT\_GRADIENTRATIO2      | The amount of the second gradient color (TMT\_GRADIENTCOLOR2) to use in drawing the part.                                                                                                                        |
| TMT\_GRADIENTRATIO3      | The amount of the third gradient color (TMT\_GRADIENTCOLOR3) to use in drawing the part.                                                                                                                         |
| TMT\_GRADIENTRATIO4      | The amount of the fourth gradient color (TMT\_GRADIENTCOLOR4) to use in drawing the part.                                                                                                                        |
| TMT\_GRADIENTRATIO5      | The amount of the fifth gradient color (TMT\_GRADIENTCOLOR5) to use in drawing the part.                                                                                                                         |
| TMT\_HEIGHT              | The height of the part.                                                                                                                                                                                          |
| TMT\_IMAGECOUNT          | The number of state images present in an image file.                                                                                                                                                             |
| TMT\_MINCOLORDEPTH       |                                                                                                                                                                                                                  |
| TMT\_MINDPI1             | The minimum dots per inch (dpi) that the first image file was designed for.                                                                                                                                      |
| TMT\_MINDPI2             | The minimum dpi that the second image file was designed for.                                                                                                                                                     |
| TMT\_MINDPI3             | The minimum dpi that the third image file was designed for.                                                                                                                                                      |
| TMT\_MINDPI4             | The minimum dpi that the fourth image file was designed for.                                                                                                                                                     |
| TMT\_MINDPI5             | The minimum dpi that the fifth image file was designed for.                                                                                                                                                      |
| TMT\_OPACITY             |                                                                                                                                                                                                                  |
| TMT\_PIXELSPERFRAME      |                                                                                                                                                                                                                  |
| TMT\_PROGRESSCHUNKSIZE   | The size of the progress control "chunk" shapes that define how far an operation has progressed.                                                                                                                 |
| TMT\_PROGRESSSPACESIZE   | The total size of all of the progress control "chunks".                                                                                                                                                          |
| TMT\_ROUNDCORNERHEIGHT   | The roundness (0 to 100 percent) of the part's corners.                                                                                                                                                          |
| TMT\_ROUNDCORNERWIDTH    | The roundness (0 to 100 percent) of the part's corners.                                                                                                                                                          |
| TMT\_SATURATION          | The amount of saturation (0-255) to apply to an icon drawn using [**DrawThemeIcon**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemeicon).                                                                                                         |
| TMT\_TEXTBORDERSIZE      | The thickness of the border drawn around text characters.                                                                                                                                                        |
| TMT\_TEXTGLOWSIZE        |                                                                                                                                                                                                                  |
| TMT\_TOCOLOR1            |                                                                                                                                                                                                                  |
| TMT\_TOCOLOR2            |                                                                                                                                                                                                                  |
| TMT\_TOCOLOR3            |                                                                                                                                                                                                                  |
| TMT\_TOCOLOR4            |                                                                                                                                                                                                                  |
| TMT\_TOCOLOR5            |                                                                                                                                                                                                                  |
| TMT\_TOHUE1              |                                                                                                                                                                                                                  |
| TMT\_TOHUE2              |                                                                                                                                                                                                                  |
| TMT\_TOHUE3              |                                                                                                                                                                                                                  |
| TMT\_TOHUE4              |                                                                                                                                                                                                                  |
| TMT\_TOHUE5              |                                                                                                                                                                                                                  |
| TMT\_TRUESIZESTRETCHMARK | The percentage of a true-size image's original size at which the image will be stretched.                                                                                                                        |
| TMT\_WIDTH               | The width of the part.                                                                                                                                                                                           |



 

**TMT\_INTLIST**



| ID                       | Notes |
|--------------------------|-------|
| TMT\_TRANSITIONDURATIONS |       |



 

**TMT\_MARGINS**



| ID                  | Notes                                                                   |
|---------------------|-------------------------------------------------------------------------|
| TMT\_CAPTIONMARGINS | The margins that define where caption text may be placed within a part. |
| TMT\_CONTENTMARGINS | The margins that define where content may be placed within a part.      |
| TMT\_SIZINGMARGINS  | The margins used for sizing a non-true-size image.                      |



 

**TMT\_POSITION**



| ID                    | Notes                                                                                                        |
|-----------------------|--------------------------------------------------------------------------------------------------------------|
| TMT\_MINSIZE          | The minimum size that the normal image file can be used for before moving to the next smallest image file.   |
| TMT\_MINSIZE1         | The minimum size that the first small image file can be used for.                                            |
| TMT\_MINSIZE2         | The minimum size that the second small image file can be used for.                                           |
| TMT\_MINSIZE3         | The minimum size that the third small image file can be used for.                                            |
| TMT\_MINSIZE4         | The minimum size that the fourth small image file can be used for.                                           |
| TMT\_MINSIZE5         | The minimum size that the fifth small image file can be used for.                                            |
| TMT\_NORMALSIZE       | The size of the normal image associated with this part.                                                      |
| TMT\_OFFSET           | The position offset from the alignment for this part. The alignment is defined by the TMT\_OFFSETTYPE value. |
| TMT\_TEXTSHADOWOFFSET | The offset from the text at which text shadows are drawn.                                                    |



 

**TMT\_RECT**



| ID                       | Notes                         |
|--------------------------|-------------------------------|
| TMT\_ANIMATIONBUTTONRECT |                               |
| TMT\_ATLASRECT           |                               |
| TMT\_CUSTOMSPLITRECT     |                               |
| TMT\_DEFAULTPANESIZE     | The default size of the part. |



 

**TMT\_SIZE**



| ID                      | Notes                     |
|-------------------------|---------------------------|
| TMT\_CAPTIONBARHEIGHT   | Caption bar height.       |
| TMT\_CAPTIONBARWIDTH    | Caption bar width.        |
| TMT\_MENUBARHEIGHT      | Menu bar height.          |
| TMT\_MENUBARWIDTH       | Menu bar width.           |
| TMT\_PADDEDBORDERWIDTH  | Padded border width.      |
| TMT\_SCROLLBARHEIGHT    | Scroll bar height.        |
| TMT\_SCROLLBARWIDTH     | Scroll bar width.         |
| TMT\_SIZINGBORDERWIDTH  | Width of a sizing border. |
| TMT\_SMCAPTIONBARHEIGHT | Caption bar height.       |
| TMT\_SMCAPTIONBARWIDTH  | Caption bar width.        |



 

**TMT\_STRING**



| ID                   | Notes                                               |
|----------------------|-----------------------------------------------------|
| TMT\_ALIAS           |                                                     |
| TMT\_ATLASINPUTIMAGE |                                                     |
| TMT\_AUTHOR          |                                                     |
| TMT\_CLASSICVALUE    |                                                     |
| TMT\_COLORSCHEMES    |                                                     |
| TMT\_COMPANY         |                                                     |
| TMT\_COPYRIGHT       |                                                     |
| TMT\_CSSNAME         | See [**GetThemeSysString**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemesysstring). |
| TMT\_DESCRIPTION     |                                                     |
| TMT\_DISPLAYNAME     |                                                     |
| TMT\_LASTUPDATED     |                                                     |
| TMT\_SIZES           |                                                     |
| TMT\_TEXT            | The text displayed by the part.                     |
| TMT\_TOOLTIP         |                                                     |
| TMT\_URL             |                                                     |
| TMT\_VERSION         |                                                     |
| TMT\_XMLNAME         | See [**GetThemeSysString**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemesysstring). |
| TMT\_NAME            |                                                     |



 

 

 
