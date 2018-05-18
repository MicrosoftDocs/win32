---
Description: Multimedia Streaming Objects
ms.assetid: '4f5460db-2670-41af-a57f-20cf706827e6'
title: Multimedia Streaming Objects
---

# Multimedia Streaming Objects

> [!Note]  
> This API is deprecated. New applications should not use it.

 

The following table describes the multimedia streaming objects.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>CLSID</th>
<th>Description</th>
<th>Interfaces supported</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CLSID_AMMediaTypeStream</td>
<td>Can create media samples for any DirectShow-supported data type</td>
<td><ul>
<li>[<strong>IAMMediaStream</strong>](iammediastream.md)</li>
<li>[<strong>IMediaStream</strong>](imediastream.md)</li>
<li>[<strong>IPin</strong>](ipin.md)</li>
<li>[<strong>IMemInputPin</strong>](imeminputpin.md)</li>
</ul></td>
</tr>
<tr class="even">
<td>CLSID_AMAudioData</td>
<td>Implementation of [<strong>IAudioData</strong>](iaudiodata.md) audio container object.</td>
<td><ul>
<li>[<strong>IAudioData</strong>](iaudiodata.md)</li>
</ul></td>
</tr>
<tr class="odd">
<td>CLSID_AMDirectDrawStream</td>
<td>DirectDraw media stream that can be added to a DirectShow multimedia stream.</td>
<td><ul>
<li>[<strong>IAMMediaStream</strong>](iammediastream.md)</li>
<li>[<strong>IMediaStream</strong>](imediastream.md)</li>
<li>[<strong>IDirectDrawMediaStream</strong>](idirectdrawmediastream.md)</li>
<li>[<strong>IPin</strong>](ipin.md)</li>
<li>[<strong>IMemInputPin</strong>](imeminputpin.md)</li>
</ul></td>
</tr>
<tr class="even">
<td>CLSID_AMMultiMediaStream</td>
<td>DirectShow implementation of multimedia stream.</td>
<td><ul>
<li>[<strong>IAMMultiMediaStream</strong>](iammultimediastream.md)</li>
<li>[<strong>IMultiMediaStream</strong>](imultimediastream.md)</li>
</ul></td>
</tr>
<tr class="odd">
<td>CLSID_MediaStreamFilter</td>
<td>Provides multimedia streaming functionality for the CLSID_AMMultiMediaStream object through the [<strong>IAMMultiMediaStream</strong>](iammultimediastream.md) interface.</td>
<td><ul>
<li>[<strong>IBaseFilter</strong>](ibasefilter.md)</li>
</ul></td>
</tr>
<tr class="even">
<td>N/A</td>
<td>Samples created by the CLSID_AMMediaTypeStream object.</td>
<td><ul>
<li>[<strong>IStreamSample</strong>](istreamsample.md)</li>
<li>[<strong>IMediaSample</strong>](imediasample.md)</li>
<li>[<strong>IMediaSample2</strong>](imediasample2.md)</li>
</ul></td>
</tr>
<tr class="odd">
<td>N/A</td>
<td>Samples created by the DirectDraw stream.</td>
<td><ul>
<li>[<strong>IStreamSample</strong>](istreamsample.md)</li>
<li>[<strong>IDirectDrawStreamSample</strong>](idirectdrawstreamsample.md)</li>
<li>[<strong>IMediaSample</strong>](imediasample.md)</li>
</ul></td>
</tr>
</tbody>
</table>



 

 

 



