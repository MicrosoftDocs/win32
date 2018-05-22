---
title: Visual Styles Reference
description: This section describes the following API elements used with Visual Styles.
ms.assetid: 'f1d01045-a296-4b39-bd42-1262ba4ad3d2'
---

# Visual Styles Reference

This section describes the following API elements used with [Visual Styles](themes-overview.md).

### Functions



| Topic                                                                                  | Contents                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BeginBufferedAnimation**](beginbufferedanimation.md)                               | Begins a buffered animation operation. The animation consists of a cross-fade between the contents of two buffers over a specified period of time. <br/>                                                                     |
| [**BeginBufferedPaint**](beginbufferedpaint.md)                                       | Begins a buffered paint operation.<br/>                                                                                                                                                                                      |
| [**BeginPanningFeedback**](beginpanningfeedback.md)                                   | Notifies the system to send feedback about a target window affected by panning gestures. <br/>                                                                                                                               |
| [**BufferedPaintClear**](bufferedpaintclear.md)                                       | Clears a specified rectangle in the buffer to ARGB = {0,0,0,0}.<br/>                                                                                                                                                         |
| [**BufferedPaintInit**](bufferedpaintinit.md)                                         | Initialize buffered painting for the current thread.<br/>                                                                                                                                                                    |
| [**BufferedPaintRenderAnimation**](bufferedpaintrenderanimation.md)                   | Paints the next frame of a buffered paint animation.<br/>                                                                                                                                                                    |
| [**BufferedPaintSetAlpha**](bufferedpaintsetalpha.md)                                 | Sets the alpha to a specified value in a given rectangle. The alpha controls the amount of transparency applied when blending with the buffer onto the destination target device context (DC). <br/>                         |
| [**BufferedPaintStopAllAnimations**](bufferedpaintstopallanimations.md)               | Stops all buffered animations for the given window.<br/>                                                                                                                                                                     |
| [**BufferedPaintUnInit**](bufferedpaintuninit.md)                                     | Closes down buffered painting for the current thread. Called once for each call to [**BufferedPaintInit**](bufferedpaintinit.md) after calls to [**BeginBufferedPaint**](beginbufferedpaint.md) are no longer needed.<br/> |
| [**CloseThemeData**](closethemedata.md)                                               | Closes the theme data handle.<br/>                                                                                                                                                                                           |
| [**DrawThemeBackground**](drawthemebackground.md)                                     | Draws the border and fill defined by the visual style for the specified control part.<br/>                                                                                                                                   |
| [**DrawThemeBackgroundEx**](drawthemebackgroundex.md)                                 | Draws the background image defined by the visual style for the specified control part.<br/>                                                                                                                                  |
| [**DrawThemeEdge**](drawthemeedge.md)                                                 | Draws one or more edges defined by the visual style of a rectangle.<br/>                                                                                                                                                     |
| [**DrawThemeIcon**](drawthemeicon.md)                                                 | Draws an image from an image list with the icon effect defined by the visual style.<br/>                                                                                                                                     |
| [**DrawThemeParentBackground**](drawthemeparentbackground.md)                         | Draws the part of a parent control that is covered by a partially-transparent or alpha-blended child control.<br/>                                                                                                           |
| [**DrawThemeParentBackgroundEx**](drawthemeparentbackgroundex.md)                     | Used by partially-transparent or alpha-blended child controls to draw the part of their parent in front of which they appear. Sends a WM\_ERASEBKGND message followed by a WM\_PRINTCLIENT.<br/>                             |
| [**DrawThemeText**](drawthemetext.md)                                                 | Draws text using the color and font defined by the visual style.<br/>                                                                                                                                                        |
| [**DrawThemeTextEx**](drawthemetextex.md)                                             | Draws text using the color and font defined by the visual style. Extends [**DrawThemeText**](drawthemetext.md) by allowing additional text format options.<br/>                                                             |
| [**EnableThemeDialogTexture**](enablethemedialogtexture.md)                           | Enables or disables the visual style of a dialog window's background.<br/>                                                                                                                                                   |
| [**EnableTheming**](enabletheming.md)                                                 | Enables or disables visual styles for the current user in the current and later sessions.<br/>                                                                                                                               |
| [**EndBufferedAnimation**](endbufferedanimation.md)                                   | Renders the first frame of a buffered animation operation and starts the animation timer.<br/>                                                                                                                               |
| [**EndBufferedPaint**](endbufferedpaint.md)                                           | Completes a buffered paint operation and frees the associated buffered paint handle.<br/>                                                                                                                                    |
| [**EndPanningFeedback**](endpanningfeedback.md)                                       | Terminates any existing animation that was in process or set up by [**BeginPanningFeedback**](beginpanningfeedback.md) and [**UpdatePanningFeedback**](updatepanningfeedback.md). <br/>                                    |
| [**GetBufferedPaintBits**](getbufferedpaintbits.md)                                   | Retrieves a pointer to the buffer bitmap if the buffer is a device-independent bitmap (DIB).<br/>                                                                                                                            |
| [**GetBufferedPaintDC**](getbufferedpaintdc.md)                                       | Gets the paint DC. This is the same value retrieved by [**BeginBufferedPaint**](beginbufferedpaint.md).<br/>                                                                                                                |
| [**GetBufferedPaintTargetDC**](getbufferedpainttargetdc.md)                           | Retrieves the target DC. <br/>                                                                                                                                                                                               |
| [**GetBufferedPaintTargetRect**](getbufferedpainttargetrect.md)                       | Retrieves the target rectangle specified by BeginBufferedPaint.<br/>                                                                                                                                                         |
| [**GetCurrentThemeName**](getcurrentthemename.md)                                     | Retrieves the name of the current visual style, and optionally retrieves the color scheme name and size name.<br/>                                                                                                           |
| [**GetThemeAppProperties**](getthemeappproperties.md)                                 | Retrieves the property flags that control how visual styles are applied in the current application.<br/>                                                                                                                     |
| [**GetThemeBackgroundContentRect**](getthemebackgroundcontentrect.md)                 | Retrieves the size of the content area for the background defined by the visual style.<br/>                                                                                                                                  |
| [**GetThemeBackgroundExtent**](getthemebackgroundextent.md)                           | Calculates the size and location of the background, defined by the visual style, given the content area.<br/>                                                                                                                |
| [**GetThemeBackgroundRegion**](getthemebackgroundregion.md)                           | Computes the region for a regular or partially transparent background that is bounded by a specified rectangle.<br/>                                                                                                         |
| [**GetThemeBitmap**](getthemebitmap.md)                                               | Retrieves the bitmap associated with a particular theme, part, state, and property.<br/>                                                                                                                                     |
| [**GetThemeBool**](getthemebool.md)                                                   | Retrieves the value of a **BOOL** property from the SysMetrics section of theme data.<br/>                                                                                                                                   |
| [**GetThemeColor**](getthemecolor.md)                                                 | Retrieves the value of a color property.<br/>                                                                                                                                                                                |
| [**GetThemeDocumentationProperty**](getthemedocumentationproperty.md)                 | Retrieves the value for a theme property from the documentation section of the specified theme file.<br/>                                                                                                                    |
| [**GetThemeEnumValue**](getthemeenumvalue.md)                                         | Retrieves the value of an enumerated type property.<br/>                                                                                                                                                                     |
| [**GetThemeFilename**](getthemefilename.md)                                           | Retrieves the value of a filename property.<br/>                                                                                                                                                                             |
| [**GetThemeFont**](getthemefont.md)                                                   | Retrieves the value of a font property. <br/>                                                                                                                                                                                |
| [**GetThemeInt**](getthemeint.md)                                                     | Retrieves the value of an **int** property.<br/>                                                                                                                                                                             |
| [**GetThemeIntList**](getthemeintlist.md)                                             | Retrieves a list of **int** data from a visual style.<br/>                                                                                                                                                                   |
| [**GetThemeMargins**](getthememargins.md)                                             | Retrieves the value of a [**MARGINS**](margins.md) property.<br/>                                                                                                                                                           |
| [**GetThemeMetric**](getthememetric.md)                                               | Retrieves the value of a metric property.<br/>                                                                                                                                                                               |
| [**GetThemePartSize**](getthemepartsize.md)                                           | Calculates the original size of the part defined by a visual style.<br/>                                                                                                                                                     |
| [**GetThemePosition**](getthemeposition.md)                                           | Retrieves the value of a position property.<br/>                                                                                                                                                                             |
| [**GetThemePropertyOrigin**](getthemepropertyorigin.md)                               | Retrieves the location of the theme property definition for a property. <br/>                                                                                                                                                |
| [**GetThemeRect**](getthemerect.md)                                                   | Retrieves the value of a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) property.<br/>                                                                                                                                                                 |
| [**GetThemeStream**](getthemestream.md)                                               | Retrieves a data stream corresponding to a specified theme, starting from a specified part, state, and property.<br/>                                                                                                        |
| [**GetThemeString**](getthemestring.md)                                               | Retrieves the value of a string property.<br/>                                                                                                                                                                               |
| [**GetThemeSysBool**](getthemesysbool.md)                                             | Retrieves the Boolean value of a system metric.<br/>                                                                                                                                                                         |
| [**GetThemeSysColor**](getthemesyscolor.md)                                           | Retrieves the value of a system color.<br/>                                                                                                                                                                                  |
| [**GetThemeSysColorBrush**](getthemesyscolorbrush.md)                                 | Retrieves a system color brush.<br/>                                                                                                                                                                                         |
| [**GetThemeSysFont**](getthemesysfont.md)                                             | Retrieves the [**LOGFONT**](https://msdn.microsoft.com/library/windows/desktop/dd145037) of a system font.<br/>                                                                                                                                                              |
| [**GetThemeSysInt**](getthemesysint.md)                                               | Retrieves the value of a system **int**. <br/>                                                                                                                                                                               |
| [**GetThemeSysSize**](getthemesyssize.md)                                             | Retrieves the value of a system size metric from theme data.<br/>                                                                                                                                                            |
| [**GetThemeSysString**](getthemesysstring.md)                                         | Retrieves the value of a system string. <br/>                                                                                                                                                                                |
| [**GetThemeTextExtent**](getthemetextextent.md)                                       | Calculates the size and location of the specified text when rendered in the visual style font.<br/>                                                                                                                          |
| [**GetThemeTextMetrics**](getthemetextmetrics.md)                                     | Retrieves information about the font specified by a visual style for a particular part.<br/>                                                                                                                                 |
| [**GetThemeTransitionDuration**](getthemetransitionduration.md)                       | Gets the duration for the specified transition.<br/>                                                                                                                                                                         |
| [**GetWindowTheme**](getwindowtheme.md)                                               | Retrieves a theme handle to a window that has visual styles applied.<br/>                                                                                                                                                    |
| [**HitTestThemeBackground**](hittestthemebackground.md)                               | Retrieves a hit test code for a point in the background specified by a visual style.<br/>                                                                                                                                    |
| [**IsAppThemed**](isappthemed.md)                                                     | Reports whether the current application's user interface displays using visual styles.<br/>                                                                                                                                  |
| [**IsCompositionActive**](iscompositionactive.md)                                     | Determines whether Desktop Window Manager (DWM) composition effects are available to the theme.<br/>                                                                                                                         |
| [**IsThemeActive**](isthemeactive.md)                                                 | Tests if a visual style for the current application is active.<br/>                                                                                                                                                          |
| [**IsThemeBackgroundPartiallyTransparent**](isthemebackgroundpartiallytransparent.md) | Retrieves whether the background specified by the visual style has transparent pieces or alpha-blended pieces.<br/>                                                                                                          |
| [**IsThemeDialogTextureEnabled**](isthemedialogtextureenabled.md)                     | Reports whether a specified dialog window supports background texturing.<br/>                                                                                                                                                |
| [**IsThemePartDefined**](isthemepartdefined.md)                                       | Retrieves whether a visual style has defined parameters for the specified part and state.<br/>                                                                                                                               |
| [**OpenThemeData**](openthemedata.md)                                                 | Opens the theme data for a window and its associated class.<br/>                                                                                                                                                             |
| [**OpenThemeDataEx**](openthemedataex.md)                                             | Opens the theme data associated with a window for specified theme classes.<br/>                                                                                                                                              |
| [**SetThemeAppProperties**](setthemeappproperties.md)                                 | Sets the flags that determine how visual styles are implemented in the calling application.<br/>                                                                                                                             |
| [**SetWindowTheme**](setwindowtheme.md)                                               | Causes a window to use a different set of visual style information than its class normally uses.<br/>                                                                                                                        |
| [**SetWindowThemeAttribute**](setwindowthemeattribute.md)                             | Sets attributes to control how visual styles are applied to a specified window.<br/>                                                                                                                                         |
| [**SetWindowThemeNonClientAttributes**](setwindowthemenonclientattributes.md)         | Sets non-client attributes to control how visual styles are applied to a specified window.<br/>                                                                                                                              |
| [**UpdatePanningFeedback**](updatepanningfeedback.md)                                 | Updates clients about state of a window resulting from a panning gesture. This function can only be called after a [**BeginPanningFeedback**](beginpanningfeedback.md) call.<br/>                                           |



 

### Visual Styles Structures



| Topic                                             | Contents                                                                                                                                                      |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BP\_ANIMATIONPARAMS**](bp-animationparams.md) | Defines animation parameters for the [**BP\_PAINTPARAMS**](bp-paintparams.md) structure used by [**BeginBufferedPaint**](beginbufferedpaint.md).<br/> |
| [**BP\_PAINTPARAMS**](bp-paintparams.md)         | Defines paint operation parameters for [**BeginBufferedPaint**](beginbufferedpaint.md).<br/>                                                           |
| [**DTBGOPTS**](dtbgopts.md)                      | Defines the options for the [**DrawThemeBackgroundEx**](drawthemebackgroundex.md) function.<br/>                                                       |
| [**DTTOPTS**](dttopts.md)                        | Defines the options for the [**DrawThemeTextEx**](drawthemetextex.md) function.<br/>                                                                   |
| [**INTLIST**](intlist.md)                        | Contains an array or list of **int** data items from a visual style.<br/>                                                                               |
| [**MARGINS**](margins.md)                        | Returned by the [**GetThemeMargins**](getthememargins.md) function to define the margins of windows that have visual styles applied.<br/>              |
| [**WTA\_OPTIONS**](wta-options.md)               | Defines options that are used to set window visual style attributes.<br/>                                                                               |



 

### Enumerated Types



| Topic                                                        | Contents                                                                                                               |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**PROPERTYORIGIN**](propertyorigin.md)                     | Returned by [**GetThemePropertyOrigin**](getthemepropertyorigin.md) to specify where a property was found.<br/> |
| [**THEMESIZE**](theme-size.md)                              | Identifies the size of the visual style part to retrieve. <br/>                                                  |
| [**TM\_PROPS**](tm-props.md)                                | Not currently supported.<br/>                                                                                    |
| [**WINDOWTHEMEATTRIBUTETYPE**](windowthemeattributetype.md) | Specifies the type of visual style attribute to set on a window.<br/>                                            |



 

### Visual Styles Topics



| Topic                                                                            | Contents                                                                                                                                                                                  |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Aero Style Classes, Parts, and States](aero-style-classes-parts-and-states.md) | Describes the classes, parts, and states supported by the Aero theme, which defines the visual styles that Windows Vista uses by default<br/>                                       |
| [Theme File Format](themesfileformat-overview.md)                               | Discusses the format of Theme (.theme) files. <br/>                                                                                                                                 |
| [Format Values](theme-format-values.md)                                         | Lists the values that are used with the *dwTextFlags* parameter of the [**DrawThemeText**](drawthemetext.md) and [**GetThemeTextExtent**](getthemetextextent.md) functions. <br/> |
| [Hit Test Options](theme-hit-test-options.md)                                   | Lists the option values that are used with the *dwOptions* parameter of the [**HitTestThemeBackground**](hittestthemebackground.md) function. <br/>                                |
| [Hit Test Return Values](theme-hit-test-retval.md)                              | Lists the hit test code values that are returned in the *pwHitTestCode* parameter of the [**HitTestThemeBackground**](hittestthemebackground.md) function. <br/>                   |
| [Parts and States](parts-and-states.md)                                         | Describes the parts and states that you use to change the appearance of controls when visual styles are enabled. <br/>                                                              |
| [Property Identifiers](property-typedefs.md)                                    | Contains information about defined values that are used to retrieve properties of visual styles. <br/>                                                                              |



 

 

 





