---
title: Structures
description: Structures
ms.assetid: '3068359f-5ac0-41e0-a09b-283b439527a0'
keywords: ["Windows Media Device Manager,structures", "Device Manager,structures", "programming reference,structures", "reference for Windows Media Device Manager,structures"]
---

# Structures

Windows Media Device Manager defines the following structures.



| Structure                                                   | Description                                                                                                                                                                                                                                              |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_BITMAPINFOHEADER**](-bitmapinfoheader.md)             | Defines the format of video frame.                                                                                                                                                                                                                       |
| [**MTP\_COMMAND\_DATA\_IN**](mtp-command-data-in.md)       | Contains Media Transport Protocol (MTP) custom commands that are sent to the device by using the [**IWMDMDevice3::DeviceIoControl**](iwmdmdevice3-deviceiocontrol.md) method.                                                                           |
| [**MTP\_COMMAND\_DATA\_OUT**](mtp-command-data-out.md)     | Contains Media Transport Protocol (MTP) responses that are filled by the device driver.                                                                                                                                                                  |
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

 

 




