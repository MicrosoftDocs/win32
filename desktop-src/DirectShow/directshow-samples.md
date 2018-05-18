---
Description: DirectShow Samples
ms.assetid: '4166d5ca-5e02-49f6-bcb1-d448f8175a0c'
title: DirectShow Samples
---

# DirectShow Samples

The DirectShow samples are included with the [Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=62332). They are located under the path \[SDK Root\] \\Samples\\Multimedia\\DirectShow.

The following table lists all of the DirectShow samples provided in the Windows SDK. For instructions on how to build the samples, refer to the documentation provided in the Windows SDK.

If there is additional documentation for a sample, the first column of this table links to it.



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Sample</th>
<th>Area</th>
<th>Description</th>
<th>Additional Dependencies</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[DirectShow Base Classes](directshow-base-classes.md)</td>
<td>Base class library</td>
<td>C++ classes and utility functions designed for implementing DirectShow filters.</td>

</tr>
<tr class="even">
<td>[AmCap Sample](amcap-sample.md)</td>
<td>Capture</td>
<td>Video capture application.</td>
<td>strmbase.lib</td>
</tr>
<tr class="odd">
<td>[DVApp Sample](dvapp-sample.md)</td>
<td>Capture</td>
<td>Digital Video (DV) capture application.</td>

</tr>
<tr class="even">
<td>[PlayCap Sample](playcap-sample.md)</td>
<td>Capture</td>
<td>Simple capture application.</td>

</tr>
<tr class="odd">
<td>[DMO Demo Sample](dmo-demo-sample.md)</td>
<td>DMO</td>
<td>Streams audio data from a WAV file through an audio effect DMO.</td>
<td>DirectX SDK</td>
</tr>
<tr class="even">
<td>DVD Sample</td>
<td>DVD</td>
<td>Demonstrates basic DVD playback and navigation, plus advanced features such as parental level management, bookmarks, karaoke, and command synchronization.</td>

</tr>
<tr class="odd">
<td>[InfTee Filter Sample](inftee-filter-sample.md)</td>
<td>Filters, miscellaneous</td>
<td>Sample implementation of the [Infinite Pin Tee](infinite-pin-tee-filter.md) filter.</td>
<td>strmbase.lib</td>
</tr>
<tr class="even">
<td>[Metronome Filter Sample](metronome-filter-sample.md)</td>
<td>Filters, miscellaneous</td>
<td>Shows how to implement a reference clock.</td>
<td>strmbase.lib</td>
</tr>
<tr class="odd">
<td>[PSI Parser Filter Sample](psi-parser-filter-sample.md)</td>
<td>Filters, miscellaneous</td>
<td>Receives Program Specific Information (PSI) tables from an MPEG-2 transport stream and extracts program information.</td>
<td>strmbase.lib</td>
</tr>
<tr class="even">
<td>[Dump Filter Sample](dump-filter-sample.md)</td>
<td>Filters, renderer</td>
<td>Writes media samples receives to a text file.</td>
<td>strmbase.lib</td>
</tr>
<tr class="odd">
<td>SampVid Filter</td>
<td>Filters, renderer</td>
<td>Video renderer filter.</td>
<td>strmbase.lib</td>
</tr>
<tr class="even">
<td>[Scope Filter Sample](scope-filter-sample.md)</td>
<td>Filters, renderer</td>
<td>Displays sound data as wave forms.</td>
<td>strmbase.lib</td>
</tr>
<tr class="odd">
<td>[Async Filter Sample](async-filter-sample.md)</td>
<td>Filters, source</td>
<td>File reader filter that supports progressive download.</td>
<td>strmbase.lib</td>
</tr>
<tr class="even">
<td>[Ball Filter Sample](ball-filter-sample.md)</td>
<td>Filters, source</td>
<td>Video source filter that produces an image of a bouncing ball.</td>
<td>strmbase.lib</td>
</tr>
<tr class="odd">
<td>[Push Source Filters Sample](push-source-filters-sample.md)</td>
<td>Filters, source</td>
<td>Source filters that provide the following data as a video stream: A single bitmap, a set of bitmaps, a copy of the current desktop image.</td>
<td>strmbase.lib</td>
</tr>
<tr class="even">
<td>[Synth Filter Sample](synth-filter-sample.md)</td>
<td>Filters, source</td>
<td>Source filter that generates audio waveforms. This sample demonstrates dynamic graph building.</td>
<td>strmbase.lib</td>
</tr>
<tr class="odd">
<td>[EZRGB24 Filter Sample](ezrgb24-filter-sample.md)</td>
<td>Filters, transform</td>
<td>Image processing filter.</td>
<td>strmbase.lib</td>
</tr>
<tr class="even">
<td>[Gargle Filter Sample](gargle-filter-sample.md)</td>
<td>Filters, transform</td>
<td>Audio effect filter.</td>
<td>strmbase.lib</td>
</tr>
<tr class="odd">
<td>[WavDest Filter Sample](wavdest-filter-sample.md)</td>
<td>Filters, transform</td>
<td>Writes an audio stream to a WAV file.</td>
<td>strmbase.lib</td>
</tr>
<tr class="even">
<td>[DMOEnum Sample](dmoenum-sample.md)</td>
<td>Miscellaneous</td>
<td>Shows how to enumerate [DirectX Media Objects](directx-media-objects.md) (DMOs).</td>

</tr>
<tr class="odd">
<td>[Mapper Sample](mapper-sample.md)</td>
<td>Miscellaneous</td>
<td>Shows how to use the [Filter Mapper](filter-mapper.md) to find filters in the registry.</td>

</tr>
<tr class="even">
<td>SysEnum Sample</td>
<td>Miscellaneous</td>
<td>Demonstrates using the [System Device Enumerator](system-device-enumerator.md) to enumerate devices and filters.</td>

</tr>
<tr class="odd">
<td>[CutScene Sample](cutscene-sample.md)</td>
<td>Playback</td>
<td>Plays a video file in full-screen mode.</td>

</tr>
<tr class="even">
<td>DDrawXCL Sample</td>
<td>Playback</td>
<td>Plays video in DirectDraw exclusive full-screen mode, using the [<strong>IDDrawExclModeVideo</strong>](iddrawexclmodevideo.md) interface on the [Overlay Mixer](overlay-mixer-filter.md) filter.</td>

</tr>
<tr class="odd">
<td>DShowPlayer Sample</td>
<td>Playback</td>
<td>Video playback application.</td>

</tr>
<tr class="even">
<td>EVRPlayer Sample</td>
<td>Playback</td>
<td>Demonstrates how to use the DirectShow EVR filter.
<blockquote>
[!Note]<br />
Requires Windows Vista or later.
</blockquote>
<br/> <br/> This sample is available in the Windows SDK for Windows Server 2008 or later.<br/></td>
<td>strmbase.lib</td>
</tr>
<tr class="odd">
<td>Texture3D9 Sample</td>
<td>Playback</td>
<td>Draws video on a Microsoft DirectX 9.0 texture surface.</td>
<td>strmbase.lib, DirectX SDK</td>
</tr>
<tr class="even">
<td>[Ticker Sample](ticker-sample.md)</td>
<td>VMR-9</td>
<td>Uses the VMR-9 to blend video and text.</td>

</tr>
<tr class="odd">
<td>VMR9Allocator Sample</td>
<td>VMR-9</td>
<td>Implements a custom allocator-presenter for the VMR-9.</td>
<td>strmbase.lib</td>
</tr>
<tr class="even">
<td>VMR9Compositor Sample</td>
<td>VMR-9</td>
<td>Implements a custom mixer for the VMR-9.</td>

</tr>
<tr class="odd">
<td>[VMRPlayer Sample](vmrplayer-sample.md)</td>
<td>VMR-9</td>
<td>Uses the VMR-9 to blend one or two running videos and a static image.</td>

</tr>
<tr class="even">
<td>Watermark Sample</td>
<td>VMR-9</td>
<td>Blends a static bitmap onto a video during playback, using the VMR-9.</td>

</tr>
<tr class="odd">
<td>[Windowless Sample](windowless-sample.md)</td>
<td>VMR-9</td>
<td>Demonstrates windowless mode in the VMR-9.</td>

</tr>
</tbody>
</table>



 

## Additional Dependencies

Some of the samples link to the DirectShow base class library. To build these samples, you must first build the base class library. For more information, see [DirectShow Base Classes](directshow-base-classes.md). The base class library is required for all of the sample filters.

A few of the samples also require the DirectX SDK, in addition to the Windows SDK. To build these samples, you must install the DirectX SDK and set the %DXSDK\_DIR% environment variable equal to your DirectX SDK installation path.

Many of the DirectShow samples use a set of common headers and source files located in the directrory \[SDK Root\]\\Samples\\Multimedia\\DirectShow\\Common. If you copy a sample folder to another directory, make sure to copy the Common folder as well.

## Related topics

<dl> <dt>

[Setting Up the Build Environment](setting-up-the-build-environment.md)
</dt> </dl>

 

 




