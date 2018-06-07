---
Description: This section contains Properties for the InkPicture Control.
ms.assetid: d724c177-af57-4c99-94f2-c70904910b49
title: InkPicture Properties
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<td>[<strong>AutoRedraw Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_autoredraw)</td>
<td>Gets or sets a value that specifies whether the [InkPicture](inkpicture-control-reference.md) control repaints when the window is invalidated (whether the [<strong>InkDisp</strong>](/windows/desktop/api/msinkaut/) object currently associated with InkPicture control is automatically redrawn when the window associated with the InkPicture receives a WM_PAINT message).<br/></td>
</tr>
<tr class="even">
<td>[<strong>BackColor</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_backcolor)</td>
<td>Gets or sets the background color for the [InkPicture](inkpicture-control-reference.md) control. The default background color is the system window background color, which is typically white.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CollectingInk Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_collectingink)</td>
<td>Gets the value that specifies whether the [InkPicture](inkpicture-control-reference.md) control is collecting ink (run time only).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CollectionMode</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_collectionmode)</td>
<td>Gets or sets the collection mode that determines whether ink, gestures, or ink and gestures are recognized as the user writes.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Cursors Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_cursors)</td>
<td>Gets the [<strong>IInkCursors</strong>](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursors) collection available for use in the [InkPicture](inkpicture-control-reference.md) control's inking region.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CustomStrokes</strong>](/windows/desktop/api/msinkaut/)</td>
<td>Gets the [<strong>IInkCustomStrokes</strong>](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcustomstrokes) collection to be persisted with the ink (design-time only).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DefaultDrawingAttributes Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_defaultdrawingattributes)</td>
<td>Gets or sets the default [<strong>InkDrawingAttributes</strong>](/windows/desktop/api/msinkaut/) collection to use when drawing and displaying ink (run time only).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DesiredPacketDescription Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_desiredpacketdescription)</td>
<td>Gets or sets the packet description of the [InkPicture](inkpicture-control-reference.md) control (run time only).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DynamicRendering Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_dynamicrendering)</td>
<td>Gets or sets the value that specifies whether the [InkPicture](inkpicture-control-reference.md) control dynamically renders the ink as it is collected.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EditingMode</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_editingmode)</td>
<td>Gets or sets a value that specifies whether the [InkPicture](inkpicture-control-reference.md) control is in ink mode, deletion mode, or selecting/editing mode.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Enabled</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_enabled)</td>
<td>Gets or sets a value that determines whether the [InkPicture](inkpicture-control-reference.md) control can respond to user-generated events.<br/>
<blockquote>
[!Note]<br />
This property is equivalent to the [<strong>InkEnabled</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_inkenabled) property.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>EraserMode</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_erasermode)</td>
<td>Gets or sets the value that specifies whether ink is erased by stroke or by point.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EraserWidth</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_eraserwidth)</td>
<td>Gets or sets the value that specifies the width of the eraser pen tip.<br/></td>
</tr>
<tr class="even">
<td>[<strong>hWnd</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_hwnd)</td>
<td>Gets the window handle to which the [InkPicture](inkpicture-control-reference.md) control is bound. (run time only)<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Ink</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_ink)</td>
<td>Gets or sets the [<strong>InkDisp</strong>](/windows/desktop/api/msinkaut/) object that is associated with the [InkPicture](inkpicture-control-reference.md) control (run time only).<br/></td>
</tr>
<tr class="even">
<td>[<strong>InkEnabled</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_inkenabled)</td>
<td>Gets or sets a value that specifies whether the [InkPicture](inkpicture-control-reference.md) control collects pen input (in-air packets, cursor in range events, and so on).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MarginX Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_marginx)</td>
<td>Gets or sets the x-axis margin around the window rectangle in screen coordinates.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MarginY Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_marginy)</td>
<td>Gets or sets the y-axis margin around the window rectangle in screen coordinates.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MouseIcon Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_mouseicon)</td>
<td>Gets or sets the current custom mouse icon.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MousePointer Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_mousepointer)</td>
<td>Gets or sets a value that indicates the type of mouse pointer that appears when the mouse is over a particular part of the [InkPicture](inkpicture-control-reference.md) control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Picture</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_picture)</td>
<td>Gets the graphics file to appear on the [InkPicture](inkpicture-control-reference.md) control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>Renderer Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_renderer)</td>
<td>Gets or sets the [<strong>InkRenderer</strong>](/windows/desktop/api/msinkaut/) object that is used to draw ink on the [InkPicture](inkpicture-control-reference.md) control (run time only).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Selection</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_selection)</td>
<td>Gets the [InkStrokes](/windows/desktop/api/msinkaut/) collection currently selected inside the [InkPicture](inkpicture-control-reference.md) control (run time only).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SizeMode</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_sizemode)</td>
<td>Gets or sets how the control handles image placement and sizing.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SupportHighContrastInk Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_supporthighcontrastink)</td>
<td>Gets a value that specifies whether ink is rendered as just one color, Color = COLOR_WINDOWTEXT (from the GetSystemMetrics call) when the system is in High Contrast mode.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SupportHighContrastSelectionUI</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_supporthighcontrastselectionui)</td>
<td>Gets or sets a value that specifies whether all selection user interfaces (selection bounding box and selection handles) are drawn in high contrast when the system is in High Contrast mode.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Tablet Property</strong>](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_tablet)</td>
<td>Gets the [<strong>IInkTablet</strong>](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet) object that the [InkPicture](inkpicture-control-reference.md) control is currently using to collect input.<br/></td>
</tr>
</tbody>
</table>



 

 

 




