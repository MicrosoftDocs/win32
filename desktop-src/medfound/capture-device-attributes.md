---
description: Capture Device Attributes
ms.assetid: dd24671a-0689-4490-8d18-2a33ed461e9d
title: Capture Device Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Capture Device Attributes

The following attributes are related to capture devices:



| Attribute                                                                                                                     | Description                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [MF\_DEVSOURCE\_ATTRIBUTE\_FRIENDLY\_NAME](mf-devsource-attribute-friendly-name.md)                                          | The device's display name.                                                          |
| [MF\_DEVSOURCE\_ATTRIBUTE\_MEDIA\_TYPE](mf-devsource-attribute-media-type.md)                                                | The device's output format.                                                         |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE](mf-devsource-attribute-source-type.md)                                              | The type of device, such as audio capture or video capture.                         |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_ENDPOINT\_ID](mf-devsource-attribute-source-type-audcap-endpoint-id.md)     | The endpoint ID for an audio capture device.                                        |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_AUDCAP\_ROLE](mf-devsource-attribute-source-type-audcap-role.md)                    | The device role for an audio capture device.                                        |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_CATEGORY](mf-devsource-attribute-source-type-vidcap-category.md)            | The device category for a video device.                                             |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_HW\_SOURCE](mf-devsource-attribute-source-type-vidcap-hw-source.md)         | Specifies whether a video capture source is a hardware device or a software device. |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_MAX\_BUFFERS](mf-devsource-attribute-source-type-vidcap-max-buffers.md)     | Specifies the maximum number of frames that the video capture source will buffer.   |
| [MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_SYMBOLIC\_LINK](mf-devsource-attribute-source-type-vidcap-symbolic-link.md) | The symbolic link for a video capture driver.                                       |
| [MFT\_HW\_TIMESTAMP\_WITH\_QPC\_Attribute](mft-hw-timestamp-with-qpc-attribute.md)                                           | Specifies whether the device source uses the system time for time stamps.           |



 

These attributes are used with the following functions:

-   [**MFCreateDeviceSource**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatedevicesource)
-   [**MFCreateDeviceSourceActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatedevicesourceactivate)
-   [**MFEnumDeviceSources**](/windows/desktop/api/mfidl/nf-mfidl-mfenumdevicesources)

## Related topics

<dl> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 



