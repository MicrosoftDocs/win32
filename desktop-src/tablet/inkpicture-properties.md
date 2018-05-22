---
Description: 'This section contains Properties for the InkPicture Control.'
ms.assetid: 'd724c177-af57-4c99-94f2-c70904910b49'
title: InkPicture Properties
---

# InkPicture Properties

This section contains Properties for the InkPicture Control.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>AutoRedraw Property</strong>](inkpicture-autoredraw.md)</td>
<td>Gets or sets a value that specifies whether the [InkPicture](inkpicture-control-reference.md) control repaints when the window is invalidated (whether the [<strong>InkDisp</strong>](inkdisp-class.md) object currently associated with InkPicture control is automatically redrawn when the window associated with the InkPicture receives a WM_PAINT message).<br/></td>
</tr>
<tr class="even">
<td>[<strong>BackColor</strong>](inkpicture-backcolor.md)</td>
<td>Gets or sets the background color for the [InkPicture](inkpicture-control-reference.md) control. The default background color is the system window background color, which is typically white.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CollectingInk Property</strong>](inkpicture-collectingink.md)</td>
<td>Gets the value that specifies whether the [InkPicture](inkpicture-control-reference.md) control is collecting ink (run time only).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CollectionMode</strong>](inkpicture-collectionmode.md)</td>
<td>Gets or sets the collection mode that determines whether ink, gestures, or ink and gestures are recognized as the user writes.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Cursors Property</strong>](inkpicture-cursors.md)</td>
<td>Gets the [<strong>IInkCursors</strong>](iinkcursors.md) collection available for use in the [InkPicture](inkpicture-control-reference.md) control's inking region.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CustomStrokes</strong>](inkpicture-customstrokes.md)</td>
<td>Gets the [<strong>IInkCustomStrokes</strong>](iinkcustomstrokes.md) collection to be persisted with the ink (design-time only).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DefaultDrawingAttributes Property</strong>](inkpicture-defaultdrawingattributes.md)</td>
<td>Gets or sets the default [<strong>InkDrawingAttributes</strong>](inkdrawingattributes-class.md) collection to use when drawing and displaying ink (run time only).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DesiredPacketDescription Property</strong>](inkpicture-desiredpacketdescription.md)</td>
<td>Gets or sets the packet description of the [InkPicture](inkpicture-control-reference.md) control (run time only).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DynamicRendering Property</strong>](inkpicture-dynamicrendering.md)</td>
<td>Gets or sets the value that specifies whether the [InkPicture](inkpicture-control-reference.md) control dynamically renders the ink as it is collected.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EditingMode</strong>](inkpicture-editingmode.md)</td>
<td>Gets or sets a value that specifies whether the [InkPicture](inkpicture-control-reference.md) control is in ink mode, deletion mode, or selecting/editing mode.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Enabled</strong>](inkpicture-enabled.md)</td>
<td>Gets or sets a value that determines whether the [InkPicture](inkpicture-control-reference.md) control can respond to user-generated events.<br/>
<blockquote>
[!Note]<br />
This property is equivalent to the [<strong>InkEnabled</strong>](inkpicture-inkenabled.md) property.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>EraserMode</strong>](inkpicture-erasermode.md)</td>
<td>Gets or sets the value that specifies whether ink is erased by stroke or by point.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EraserWidth</strong>](inkpicture-eraserwidth.md)</td>
<td>Gets or sets the value that specifies the width of the eraser pen tip.<br/></td>
</tr>
<tr class="even">
<td>[<strong>hWnd</strong>](inkpicture-hwnd.md)</td>
<td>Gets the window handle to which the [InkPicture](inkpicture-control-reference.md) control is bound. (run time only)<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Ink</strong>](inkpicture-ink.md)</td>
<td>Gets or sets the [<strong>InkDisp</strong>](inkdisp-class.md) object that is associated with the [InkPicture](inkpicture-control-reference.md) control (run time only).<br/></td>
</tr>
<tr class="even">
<td>[<strong>InkEnabled</strong>](inkpicture-inkenabled.md)</td>
<td>Gets or sets a value that specifies whether the [InkPicture](inkpicture-control-reference.md) control collects pen input (in-air packets, cursor in range events, and so on).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MarginX Property</strong>](inkpicture-marginx.md)</td>
<td>Gets or sets the x-axis margin around the window rectangle in screen coordinates.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MarginY Property</strong>](inkpicture-marginy.md)</td>
<td>Gets or sets the y-axis margin around the window rectangle in screen coordinates.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MouseIcon Property</strong>](inkpicture-mouseicon.md)</td>
<td>Gets or sets the current custom mouse icon.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MousePointer Property</strong>](inkpicture-mousepointer.md)</td>
<td>Gets or sets a value that indicates the type of mouse pointer that appears when the mouse is over a particular part of the [InkPicture](inkpicture-control-reference.md) control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Picture</strong>](inkpicture-picture.md)</td>
<td>Gets the graphics file to appear on the [InkPicture](inkpicture-control-reference.md) control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>Renderer Property</strong>](inkpicture-renderer.md)</td>
<td>Gets or sets the [<strong>InkRenderer</strong>](inkrenderer-class.md) object that is used to draw ink on the [InkPicture](inkpicture-control-reference.md) control (run time only).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Selection</strong>](inkpicture-selection.md)</td>
<td>Gets the [InkStrokes](inkstrokes-collection.md) collection currently selected inside the [InkPicture](inkpicture-control-reference.md) control (run time only).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SizeMode</strong>](inkpicture-sizemode.md)</td>
<td>Gets or sets how the control handles image placement and sizing.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SupportHighContrastInk Property</strong>](inkpicture-supporthighcontrastink.md)</td>
<td>Gets a value that specifies whether ink is rendered as just one color, Color = COLOR_WINDOWTEXT (from the GetSystemMetrics call) when the system is in High Contrast mode.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SupportHighContrastSelectionUI</strong>](inkpicture-supporthighcontrastselectionui.md)</td>
<td>Gets or sets a value that specifies whether all selection user interfaces (selection bounding box and selection handles) are drawn in high contrast when the system is in High Contrast mode.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Tablet Property</strong>](inkpicture-tablet.md)</td>
<td>Gets the [<strong>IInkTablet</strong>](iinktablet.md) object that the [InkPicture](inkpicture-control-reference.md) control is currently using to collect input.<br/></td>
</tr>
</tbody>
</table>



 

 

 




