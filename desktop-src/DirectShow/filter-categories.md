---
description: The following tables list the CLSIDs for the DirectShow filter categories.
ms.assetid: cab4e2c9-eab9-4836-adfc-870490ca5b6b
title: Filter Categories
ms.topic: article
ms.date: 05/31/2018
---

# Filter Categories

The following tables list the CLSIDs for the DirectShow filter categories.

-   [DirectShow Filter Categories](#directshow-filter-categories)
-   [Other Filter Categories](#other-filter-categories)
-   [DirectShow Filter Meta-Category](#directshow-filter-meta-category)
-   [DMO Categories](#dmo-categories)
-   [Related topics](#related-topics)

## DirectShow Filter Categories

The categories listed here are enumerated by the [Filter Mapper](filter-mapper.md). By default, however, the Filter Mapper ignores categories with merits of MERIT\_DO\_NOT\_USE or less. For more information, see [**IFilterMapper2::EnumMatchingFilters**](/windows/desktop/api/Strmif/nf-strmif-ifiltermapper2-enummatchingfilters). All of the categories listed here can also be enumerated with the [System Device Enumerator](system-device-enumerator.md).

The following categories are declared in Uuids.h. Include the header file Dshow.h.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Friendly Name</th>
<th>CLSID</th>
<th>Merit</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Audio Capture Sources</td>
<td><strong>CLSID_AudioInputDeviceCategory</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="even">
<td>Audio Compressors</td>
<td><strong>CLSID_AudioCompressorCategory</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="odd">
<td>Audio Renderers</td>
<td><strong>CLSID_AudioRendererCategory</strong></td>
<td><strong>MERIT_NORMAL</strong></td>
</tr>
<tr class="even">
<td>Device Control Filters</td>
<td><strong>CLSID_DeviceControlCategory</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="odd">
<td>DirectShow Filters</td>
<td><strong>CLSID_LegacyAmFilterCategory</strong></td>
<td><strong>MERIT_NORMAL</strong></td>
</tr>
<tr class="even">
<td>External Renderers</td>
<td><strong>CLSID_TransmitCategory</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="odd">
<td>Midi Renderers</td>
<td><strong>CLSID_MidiRendererCategory</strong></td>
<td><strong>MERIT_NORMAL</strong></td>
</tr>
<tr class="even">
<td>Video Capture Sources</td>
<td><strong>CLSID_VideoInputDeviceCategory</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="odd">
<td>Video Compressors</td>
<td><strong>CLSID_VideoCompressorCategory</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="even">
<td>WDM Stream Decompression Devices</td>
<td><strong>CLSID_DVDHWDecodersCategory</strong>
<blockquote>
[!Note]<br />
This category contains hardware DVD decoders.
</blockquote>
<br/></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="odd">
<td>WDM Streaming Capture Devices</td>
<td><strong>AM_KSCATEGORY_CAPTURE</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="even">
<td>WDM Streaming Crossbar Devices</td>
<td><strong>AM_KSCATEGORY_CROSSBAR</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="odd">
<td>WDM Streaming Rendering Devices</td>
<td><strong>AM_KSCATEGORY_RENDER</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="even">
<td>WDM Streaming Tee/Splitter Devices</td>
<td><strong>AM_KSCATEGORY_SPLITTER</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="odd">
<td>WDM Streaming TV Audio Devices</td>
<td><strong>AM_KSCATEGORY_TVAUDIO</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="even">
<td>WDM Streaming TV Tuner Devices</td>
<td><strong>AM_KSCATEGORY_TVTUNER</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
<tr class="odd">
<td>WDM Streaming VBI Codecs</td>
<td><strong>AM_KSCATEGORY_VBICODEC</strong></td>
<td><strong>MERIT_DO_NOT_USE</strong></td>
</tr>
</tbody>
</table>



 

The following categories are declared in the header file Ks.h.



| Friendly Name                          | CLSID                                   | Merit                   |
|----------------------------------------|-----------------------------------------|-------------------------|
| WDM Streaming Communication Transforms | **KSCATEGORY\_COMMUNICATIONSTRANSFORM** | **MERIT\_DO\_NOT\_USE** |
| WDM Streaming Data Transforms          | **KSCATEGORY\_DATATRANSFORM**           | **MERIT\_DO\_NOT\_USE** |
| WDM Streaming Interface Transforms     | **KSCATEGORY\_INTERFACETRANSFORM**      | **MERIT\_DO\_NOT\_USE** |
| WDM Streaming Mixer Devices            | **KSCATEGORY\_MIXER**                   | **MERIT\_DO\_NOT\_USE** |



 

The following categories are declared in the header file Bdamedia.h. Include the following header files: ks.h, ksmedia.h, and bdamedia.h.



| Friendly Name                       | CLSID                                       | Merit                   |
|-------------------------------------|---------------------------------------------|-------------------------|
| BDA Network Providers               | **KSCATEGORY\_BDA\_NETWORK\_PROVIDER**      | **MERIT\_NORMAL**       |
| BDA Receiver Components             | **KSCATEGORY\_BDA\_RECEIVER\_COMPONENT**    | **MERIT\_DO\_NOT\_USE** |
| BDA Rendering Filters               | **KSCATEGORY\_IP\_SINK**                    | **MERIT\_DO\_NOT\_USE** |
| BDA Source Filters                  | **KSCATEGORY\_BDA\_NETWORK\_TUNER**         | **MERIT\_DO\_NOT\_USE** |
| BDA Transport Information Renderers | **KSCATEGORY\_BDA\_TRANSPORT\_INFORMATION** | **MERIT\_NORMAL**       |



 

> [!Note]  
> Decoders are registered under the "DirectShow Filters" category (CLSID\_LegacyAmFilterCategory).

 

## Other Filter Categories

The categories listed here can be enumerated with the System Device Enumerator, but are not visible to the Filter Mapper and are not used by [Intelligent Connect](intelligent-connect.md).

The following categories are declared in the header file Qedit.h.



| Friendly Name            | CLID                             | Merit                   |
|--------------------------|----------------------------------|-------------------------|
| Video Effects (1 input)  | **CLSID\_VideoEffects1Category** | **MERIT\_DO\_NOT\_USE** |
| Video Effects (2 inputs) | **CLSID\_VideoEffects2Category** | **MERIT\_DO\_NOT\_USE** |



 

These categories contain video effects and transitions for [DirectShow Editing Services](directshow-editing-services.md):

-   "Video Effects (1 input)" contains video effects.
-   "Video Effects (2 input)" contains video transitions.

For more information, see [Enumerating Effects and Transitions](enumerating-effects-and-transitions.md).

The following categories are declared in the header file Uuids.h. Include the header file Dshow.h.



| Friendly Name       | CLID                                | Merit                   |
|---------------------|-------------------------------------|-------------------------|
| EncAPI Encoders     | **CLSID\_MediaEncoderCategory**     | **MERIT\_DO\_NOT\_USE** |
| EncAPI Multiplexers | **CLSID\_MediaMultiplexerCategory** | **MERIT\_DO\_NOT\_USE** |



 

## DirectShow Filter Meta-Category



| Friendly Name                 | CLSID                            | Merit          |
|-------------------------------|----------------------------------|----------------|
| ActiveMovie Filter Categories | **CLSID\_ActiveMovieCategories** | Not applicable |



 

This meta-category contains a list of filter categories. If a filter category does not appear within this list, the [Filter Mapper](filter-mapper.md) ignores the category, which means the filter is not available for [Intelligent Connect](intelligent-connect.md).

To enumerate the list of filter categories, call [**ICreateDevEnum::CreateClassEnumerator**](/windows/desktop/api/Strmif/nf-strmif-icreatedevenum-createclassenumerator) with the value CLSID\_ActiveMovieCategories. The monikers returned by this method support the following properties.



| Property Name  | Description                                                                            |
|----------------|----------------------------------------------------------------------------------------|
| "FriendlyName" | Category name (VT\_BSTR).                                                              |
| "Merit"        | Category merit (VT\_I4). If this property is absent, treat as **MERIT\_DO\_NOT\_USE**. |
| "CLSID"        | Category CLSID (VT\_BSTR).                                                             |



 

To add a new filter category to this list, call [**IFilterMapper2::CreateCategory**](/windows/desktop/api/Strmif/nf-strmif-ifiltermapper2-createcategory).

## DMO Categories

DirectX Media Objects (DMOs) use a different enumeration mechanism from DirectShow filters. For more information, see [Registering a DMO](registering-a-dmo.md). However, you can use the System Device Enumerator to enumerate DMO categories. The monikers bind to the [DMO Wrapper Filter](dmo-wrapper-filter.md) and automatically initialize the filter with the DMO.

In addition, some of the DMO categories are mapped to DirectShow filter categories for the purposes of intelligent connect:



| DMO Category                    | DirectShow Equivalent              |
|---------------------------------|------------------------------------|
| **DMOCATEGORY\_AUDIO\_ENCODER** | **CLSID\_AudioCompressorCategory** |
| **DMOCATEGORY\_AUDIO\_DECODER** | **CLSID\_LegacyAmFilterCategory**  |
| **DMOCATEGORY\_VIDEO\_ENCODER** | **CLSID\_VideoCompressorCategory** |
| **DMOCATEGORY\_VIDEO\_DECODER** | **CLSID\_LegacyAmFilterCategory**  |



 

Note that the video effect and audio effect categories are not mapped to any DirectShow categories.

## Related topics

<dl> <dt>

[Constants and GUIDs](constants-and-guids.md)
</dt> <dt>

[Enumerating Devices and Filters](enumerating-devices-and-filters.md)
</dt> <dt>

[Intelligent Connect](intelligent-connect.md)
</dt> <dt>

[Layout of the Registry Keys](layout-of-the-registry-keys.md)
</dt> <dt>

[Using the Filter Mapper](using-the-filter-mapper.md)
</dt> <dt>

[Using the System Device Enumerator](using-the-system-device-enumerator.md)
</dt> </dl>

 

 




