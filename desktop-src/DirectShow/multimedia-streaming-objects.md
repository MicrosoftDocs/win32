---
Description: Multimedia Streaming Objects
ms.assetid: 4f5460db-2670-41af-a57f-20cf706827e6
title: Multimedia Streaming Objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<li>[<strong>IAMMediaStream</strong>](/windows/win32/amstream/nn-amstream-iammediastream?branch=master)</li>
<li>[<strong>IMediaStream</strong>](/windows/win32/mmstream/nn-mmstream-imediastream?branch=master)</li>
<li>[<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master)</li>
<li>[<strong>IMemInputPin</strong>](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master)</li>
</ul></td>
</tr>
<tr class="even">
<td>CLSID_AMAudioData</td>
<td>Implementation of [<strong>IAudioData</strong>](/windows/win32/austream/nn-austream-iaudiodata?branch=master) audio container object.</td>
<td><ul>
<li>[<strong>IAudioData</strong>](/windows/win32/austream/nn-austream-iaudiodata?branch=master)</li>
</ul></td>
</tr>
<tr class="odd">
<td>CLSID_AMDirectDrawStream</td>
<td>DirectDraw media stream that can be added to a DirectShow multimedia stream.</td>
<td><ul>
<li>[<strong>IAMMediaStream</strong>](/windows/win32/amstream/nn-amstream-iammediastream?branch=master)</li>
<li>[<strong>IMediaStream</strong>](/windows/win32/mmstream/nn-mmstream-imediastream?branch=master)</li>
<li>[<strong>IDirectDrawMediaStream</strong>](/windows/win32/ddstream/nn-ddstream-idirectdrawmediastream?branch=master)</li>
<li>[<strong>IPin</strong>](/windows/win32/Strmif/nn-strmif-ipin?branch=master)</li>
<li>[<strong>IMemInputPin</strong>](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master)</li>
</ul></td>
</tr>
<tr class="even">
<td>CLSID_AMMultiMediaStream</td>
<td>DirectShow implementation of multimedia stream.</td>
<td><ul>
<li>[<strong>IAMMultiMediaStream</strong>](/windows/win32/amstream/nn-amstream-iammultimediastream?branch=master)</li>
<li>[<strong>IMultiMediaStream</strong>](/windows/win32/mmstream/nn-mmstream-imultimediastream?branch=master)</li>
</ul></td>
</tr>
<tr class="odd">
<td>CLSID_MediaStreamFilter</td>
<td>Provides multimedia streaming functionality for the CLSID_AMMultiMediaStream object through the [<strong>IAMMultiMediaStream</strong>](/windows/win32/amstream/nn-amstream-iammultimediastream?branch=master) interface.</td>
<td><ul>
<li>[<strong>IBaseFilter</strong>](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master)</li>
</ul></td>
</tr>
<tr class="even">
<td>N/A</td>
<td>Samples created by the CLSID_AMMediaTypeStream object.</td>
<td><ul>
<li>[<strong>IStreamSample</strong>](/windows/win32/mmstream/nn-mmstream-istreamsample?branch=master)</li>
<li>[<strong>IMediaSample</strong>](/windows/win32/Strmif/nn-strmif-imediasample?branch=master)</li>
<li>[<strong>IMediaSample2</strong>](/windows/win32/Strmif/nn-strmif-imediasample2?branch=master)</li>
</ul></td>
</tr>
<tr class="odd">
<td>N/A</td>
<td>Samples created by the DirectDraw stream.</td>
<td><ul>
<li>[<strong>IStreamSample</strong>](/windows/win32/mmstream/nn-mmstream-istreamsample?branch=master)</li>
<li>[<strong>IDirectDrawStreamSample</strong>](/windows/win32/ddstream/nn-ddstream-idirectdrawstreamsample?branch=master)</li>
<li>[<strong>IMediaSample</strong>](/windows/win32/Strmif/nn-strmif-imediasample?branch=master)</li>
</ul></td>
</tr>
</tbody>
</table>



 

 

 



