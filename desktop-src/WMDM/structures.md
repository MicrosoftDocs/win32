---
title: WMDM structures
description: This article includes reference articles about structures defined by Windows Media Device Manager, such as _BITMAPINFOHEADER and MTP_COMMAND_DATA_IN.
ms.assetid: 3068359f-5ac0-41e0-a09b-283b439527a0
keywords:
- Windows Media Device Manager,structures
- Device Manager,structures
- programming reference,structures
- reference for Windows Media Device Manager,structures
ms.topic: article
ms.date: 05/31/2018
---

# WMDM structures

Windows Media Device Manager defines the following structures.



| Structure                                                   | Description                                                                                                                                                                                                                                              |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_BITMAPINFOHEADER**](-bitmapinfoheader.md)             | Defines the format of video frame.                                                                                                                                                                                                                       |
| [**MTP\_COMMAND\_DATA\_IN**](/windows/desktop/api/MtpExt/ns-mtpext-mtp_command_data_in)       | Contains Media Transport Protocol (MTP) custom commands that are sent to the device by using the [**IWMDMDevice3::DeviceIoControl**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-deviceiocontrol) method.                                                                           |
| [**MTP\_COMMAND\_DATA\_OUT**](/windows/desktop/api/MtpExt/ns-mtpext-mtp_command_data_out)     | Contains Media Transport Protocol (MTP) responses that are filled by the device driver.                                                                                                                                                                  |
| [**OPAQUECOMMAND**](opaquecommand.md)                      | Contains data for commands that are passed through Windows Media Device Manager to a device but are not intended to be acted upon by Windows Media Device Manager.                                                                                       |
| [**\_VIDEOINFOHEADER**](-videoinfoheader.md)               | Defines the format of a video stream.                                                                                                                                                                                                                    |
| [**\_WAVEFORMATEX**](-waveformatex.md)                     | Defines the format of waveform-audio data.                                                                                                                                                                                                               |
| [**WMDM\_FORMAT\_CAPABILITY**](wmdm-format-capability.md)  | Describes the capabilities of a device for a particular format. This structure contains a set of property configurations in an array of [**WMDM\_PROP\_CONFIG**](wmdm-prop-config.md) structures.                                                       |
| [**WMDM\_PROP\_CONFIG**](wmdm-prop-config.md)              | Describes a set of compatible property values across all the properties supported by the device for a particular format. This structure contains a number of property descriptions in an array of [**WMDM\_PROP\_DESC**](wmdm-prop-desc.md) structures. |
| [**WMDM\_PROP\_DESC**](wmdm-prop-desc.md)                  | Describes valid values of a property in a particular property configuration.                                                                                                                                                                             |
| [**WMDM\_PROP\_VALUES\_ENUM**](wmdm-prop-values-enum.md)   | Contains an enumerated set of valid values for a particular property in a particular property configuration.                                                                                                                                             |
| [**WMDM\_PROP\_VALUES\_RANGE**](wmdm-prop-values-range.md) | Describes range of valid values for a particular property in a particular property configuration.                                                                                                                                                        |
| [**WMDMDATETIME**](wmdmdatetime.md)                        | Contains a date and time.                                                                                                                                                                                                                                |
| [**WMDMID**](wmdmid.md)                                    | Describes serial numbers and group IDs.                                                                                                                                                                                                                  |
| [**WMDMMetadataView**](wmdmmetadataview.md)                | Defines the metadata view.                                                                                                                                                                                                                               |
| [**WMDMRIGHTS**](wmdmrights.md)                            | Describes content-use rights.                                                                                                                                                                                                                            |
| [**WMFILECAPABILITIES**](wmfilecapabilities.md)            | Describes a MIME type.                                                                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




