---
description: Shows how to use DXVA Video Processing.
ms.assetid: 1465bd41-94f9-4e19-8236-00e7a2d6f54a
title: DXVA2_VideoProc Sample
ms.topic: article
ms.date: 05/31/2018
---

# DXVA2\_VideoProc Sample

Shows how to use [DXVA Video Processing](dxva-video-processing.md).

This sample programmatically generates video with a primary stream and a substream. The primary stream displays SMPTE color bars, and the substream is a semi-transparent rectangle. The video is then processed and displayed using a DXVA video processor. The user can change the planar alpha values, source and destination rectangles, color adjustments, and color space.

![screenshot of the dxva2\-videoproc sample](images/dxva2-videoproc.png)

## APIs Demonstrated

This sample demonstrates the following DXVA interfaces:

-   [**IDirectXVideoProcessorService**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideoprocessorservice)
-   [**IDirectXVideoProcessor**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideoprocessor)

## Usage

The DXVA2\_VideoProc sample builds a Windows application.

Command line options:



| Option | Description                                                                          |
|--------|--------------------------------------------------------------------------------------|
| -hh    | Forces the application to use a hardware Direct3D device and a hardware DXVA device. |
| -hs    | Forces the application to use a hardware Direct3D device and a software DXVA device. |
| -ss    | Forces the application to use a software Direct3D device and a software DXVA device. |



 

Keyboard commands:



| Key       | Description                                             |
|-----------|---------------------------------------------------------|
| ALT+ENTER | Switch between windowed mode and full-screen mode.      |
| F1–F8     | Enter one of the modes shown in the following table.    |
| END       | Enable or disable debugging logging for dropped frames. |
| HOME      | Reset a parameter to its initial value.                 |



 

Each of the function keys F1 through F8 switches to a mode in which the arrow keys can be used to adjust a particular rendering parameter. In addition, the color of the substream changes.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>F1</td>
<td>Adjust the alpha values.<br/>
<ul>
<li>UP: Increase the planar alpha of both streams.</li>
<li>DOWN: Decrease the planar alpha of both streams.</li>
<li>RIGHT: Increase the pixel alpha of the substream.</li>
<li>LEFT: Decrease the pixel alpha of the substream.</li>
</ul>
Substream color: White<br/></td>
</tr>
<tr class="even">
<td>F2</td>
<td>Adjust the primary stream's source area (zoom).<br/>
<ul>
<li>UP: Increase vertically (zoom in).</li>
<li>DOWN: Decrease vertically (zoom out).</li>
<li>RIGHT: Increase horizontally (zoom in).</li>
<li>LEFT: Decrease horizontally (zoom out).</li>
</ul>
Substream color: Red<br/></td>
</tr>
<tr class="odd">
<td>F3</td>
<td>Move the primary stream's source area.<br/>
<ul>
<li>UP: Move up.</li>
<li>DOWN: Move down.</li>
<li>RIGHT: Move right.</li>
<li>LEFT: Move left.</li>
</ul>
Substream color: Yellow<br/></td>
</tr>
<tr class="even">
<td>F4</td>
<td>Adjust the primary stream's destination area.<br/>
<ul>
<li>UP: Increase vertically.</li>
<li>DOWN: Decrease vertically.</li>
<li>RIGHT: Increase horizontally.</li>
<li>LEFT: Decrease horizontally.</li>
</ul>
Substream color: Green<br/></td>
</tr>
<tr class="odd">
<td>F5</td>
<td>Move the primary stream's destination area.<br/>
<ul>
<li>UP: Move up.</li>
<li>DOWN: Move down.</li>
<li>RIGHT: Move right.</li>
<li>LEFT: Move left.</li>
</ul>
Substream color: Cyan<br/></td>
</tr>
<tr class="even">
<td>F6</td>
<td>Change background color or color space.<br/>
<ul>
<li>UP, DOWN: Cycle through color spaces.</li>
<li>RIGHT, LEFT: Cycle through background colors.</li>
</ul>
Substream color: Blue<br/></td>
</tr>
<tr class="odd">
<td>F7</td>
<td>Adjust brightness and contrast.<br/>
<ul>
<li>UP: Increase brightness.</li>
<li>DOWN: Decrease brightness.</li>
<li>RIGHT: Increase contrast.</li>
<li>LEFT: Decrease contrast.</li>
</ul>
Substream color: Magenta<br/></td>
</tr>
<tr class="even">
<td>F8</td>
<td>Adjust hue and saturation.<br/>
<ul>
<li>UP: Increase hue.</li>
<li>DOWN: Decrease hue.</li>
<li>RIGHT: Increase saturation.</li>
<li>LEFT: Decrease saturation.</li>
</ul>
Substream color: Black<br/></td>
</tr>
</tbody>
</table>



 

In each mode, pressing the HOME key resets the parameters for that mode to their initial values.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/evrpresenter).

## Related topics

<dl> <dt>

[DirectX Video Acceleration 2.0](directx-video-acceleration-2-0.md)
</dt> <dt>

[DXVA Video Processing](dxva-video-processing.md)
</dt> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> </dl>

 

 




