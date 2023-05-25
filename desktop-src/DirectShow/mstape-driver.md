---
description: MSTape Driver
ms.assetid: aa59f322-09b1-4b0a-be6f-d865c20f76e5
title: MSTape Driver
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MSTape Driver

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic applies to Windows XP or later.

The MSTape driver supports D-VHS and MPEG camcorder devices. It is exposed to applications as the [WDM Video Capture](wdm-video-capture-filter.md) filter. Its functionality is similar to that of [MSDV](msdv-driver.md), the DV camcorder driver:

-   It appears in the "Video Capture Sources" (CLSID\_VideoInputDeviceCategory) and "WDM Streaming Rendering Devices" (AM\_KSCATEGORY\_RENDER) filter categories.
-   An application can create an instance of the filter using the [**ICreateDevEnum**](/windows/desktop/api/Strmif/nn-strmif-icreatedevenum) interface.
-   It has an output pin for capture and transport from the device, and an input pin for transport to the device. Only one pin can be connected at time.

**Media Types**

The input pin supports one media type.



| Label | Value |
|--------------|------------------------------------------------------------|
| Major Type   | MEDIATYPE\_Stream                                          |
| Subtype      | MEDIASUBTYPE\_MPEG2\_TRANSPORT\_STRIDE                     |
| Sample Size  | 192 x 256                                                  |
| Format Block | [**MPEG2\_TRANSPORT\_STRIDE**](mpeg2-transport-stride.md) |



 

The output pin supports two media types.



| Label | Value |
|--------------|----------------------------------------|
| Major Type   | MEDIATYPE\_Stream                      |
| Subtype      | MEDIASUBTYPE\_MPEG2\_TRANSPORT\_STRIDE |
| Sample Size  | 192 x 256                              |
| Format Block | MPEG2\_TRANSPORT\_STRIDE               |



 



| Label | Value |
|--------------|----------------------------------------|
| Major Type   | MEDIATYPE\_Stream                      |
| Subtype      | MEDIASUBTYPE\_MPEG2\_TRANSPORT\_STRIDE |
| Sample Size  | 188 x 256                              |
| Format Block | **NULL**                               |



 

**Device Information**

The driver dynamically reads information from the device configuration ROM. The application can retrieve this information by binding the device moniker to a property bag and calling the **IPropertyBag::Read** method.



| Property            | Description                                                                                                                                                                         | Data type           |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| UniqueID\_Low       | Unique ID of the device (low **DWORD**).                                                                                                                                            | **long** (VT\_I4)   |
| UniqueID\_High      | Unique ID of the device (high **DWORD**)                                                                                                                                            | **long**            |
| VendorID            | Vendor ID.                                                                                                                                                                          | **long**            |
| ModelID             | Model ID.                                                                                                                                                                           | **long**            |
| VendorText          | Vendor name.                                                                                                                                                                        | **BSTR** (VT\_BSTR) |
| ModelText           | Device model name.                                                                                                                                                                  | **BSTR**            |
| UnitModelText       | Unit model name; may be the same as ModelText.                                                                                                                                      | **BSTR**            |
| DeviceOPcr0Payload  | oPCR (Output Plug Control) payload. Example: 146 quadlets.                                                                                                                          | **long**            |
| DeviceOPcr0DataRate | oPCR data rate. Examples: 0 (S100), 1 (S200), or 2 (S400).                                                                                                                          | **long**            |
| DeviceClassGUID     | GUID that identifies the device driver. For MSTape, this value is `{8C0F6AF2-0EDB-44C1-8AEB-59040BD830ED}`. This GUID is defined as MSTapeDeviceGUID in the header file Xprtdefs.h. | **BSTR**            |
| Description         | A description of the device, taken from the INF file. This string usually contains the brand name of the device.                                                                    | **BSTR**            |



 

The device ID is a 64-bit integer. The low **DWORD** is stored in the UniqueID\_Low property, and the high **DWORD** is stored in the UniqueID\_High property.

For more information about device monikers, see [Using the System Device Enumerator](using-the-system-device-enumerator.md).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> </dl>

 

 



