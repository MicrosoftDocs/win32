---
Description: Multimedia Streaming Objects
ms.assetid: 4f5460db-2670-41af-a57f-20cf706827e6
title: Multimedia Streaming Objects
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<li>[<strong>IAMMediaStream</strong>](/windows/desktop/api/amstream/nn-amstream-iammediastream)</li>
<li>[<strong>IMediaStream</strong>](/windows/desktop/api/mmstream/nn-mmstream-imediastream)</li>
<li>[<strong>IPin</strong>](/windows/desktop/api/Strmif/nn-strmif-ipin)</li>
<li>[<strong>IMemInputPin</strong>](/windows/desktop/api/Strmif/nn-strmif-imeminputpin)</li>
</ul></td>
</tr>
<tr class="even">
<td>CLSID_AMAudioData</td>
<td>Implementation of [<strong>IAudioData</strong>](/windows/desktop/api/austream/nn-austream-iaudiodata) audio container object.</td>
<td><ul>
<li>[<strong>IAudioData</strong>](/windows/desktop/api/austream/nn-austream-iaudiodata)</li>
</ul></td>
</tr>
<tr class="odd">
<td>CLSID_AMDirectDrawStream</td>
<td>DirectDraw media stream that can be added to a DirectShow multimedia stream.</td>
<td><ul>
<li>[<strong>IAMMediaStream</strong>](/windows/desktop/api/amstream/nn-amstream-iammediastream)</li>
<li>[<strong>IMediaStream</strong>](/windows/desktop/api/mmstream/nn-mmstream-imediastream)</li>
<li>[<strong>IDirectDrawMediaStream</strong>](/windows/desktop/api/ddstream/nn-ddstream-idirectdrawmediastream)</li>
<li>[<strong>IPin</strong>](/windows/desktop/api/Strmif/nn-strmif-ipin)</li>
<li>[<strong>IMemInputPin</strong>](/windows/desktop/api/Strmif/nn-strmif-imeminputpin)</li>
</ul></td>
</tr>
<tr class="even">
<td>CLSID_AMMultiMediaStream</td>
<td>DirectShow implementation of multimedia stream.</td>
<td><ul>
<li>[<strong>IAMMultiMediaStream</strong>](/windows/desktop/api/amstream/nn-amstream-iammultimediastream)</li>
<li>[<strong>IMultiMediaStream</strong>](/windows/desktop/api/mmstream/nn-mmstream-imultimediastream)</li>
</ul></td>
</tr>
<tr class="odd">
<td>CLSID_MediaStreamFilter</td>
<td>Provides multimedia streaming functionality for the CLSID_AMMultiMediaStream object through the [<strong>IAMMultiMediaStream</strong>](/windows/desktop/api/amstream/nn-amstream-iammultimediastream) interface.</td>
<td><ul>
<li>[<strong>IBaseFilter</strong>](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)</li>
</ul></td>
</tr>
<tr class="even">
<td>N/A</td>
<td>Samples created by the CLSID_AMMediaTypeStream object.</td>
<td><ul>
<li>[<strong>IStreamSample</strong>](/windows/desktop/api/mmstream/nn-mmstream-istreamsample)</li>
<li>[<strong>IMediaSample</strong>](/windows/desktop/api/Strmif/nn-strmif-imediasample)</li>
<li>[<strong>IMediaSample2</strong>](/windows/desktop/api/Strmif/nn-strmif-imediasample2)</li>
</ul></td>
</tr>
<tr class="odd">
<td>N/A</td>
<td>Samples created by the DirectDraw stream.</td>
<td><ul>
<li>[<strong>IStreamSample</strong>](/windows/desktop/api/mmstream/nn-mmstream-istreamsample)</li>
<li>[<strong>IDirectDrawStreamSample</strong>](/windows/desktop/api/ddstream/nn-ddstream-idirectdrawstreamsample)</li>
<li>[<strong>IMediaSample</strong>](/windows/desktop/api/Strmif/nn-strmif-imediasample)</li>
</ul></td>
</tr>
</tbody>
</table>



 

 

 



