---
title: SES\_DOWNLOAD\_MICROCODE\_STATUS\_DESCRIPTOR structure
description: The SES\_DOWNLOAD\_MICROCODE\_STATUS\_DESCRIPTOR structure specifies the status and additional status of a download microcode.
ms.assetid: af686e7a-9426-4151-8ac4-d95ae1689b4c
keywords:
- SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure Storage Devices
- PSES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR
api_location:
- scsi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SES\_DOWNLOAD\_MICROCODE\_STATUS\_DESCRIPTOR structure

The **SES\_DOWNLOAD\_MICROCODE\_STATUS\_DESCRIPTOR** structure specifies the status and additional status of a download microcode.

## Syntax


```C++
typedef struct _SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR {
  UCHAR  Reserved1;
  UCHAR  SubEnclosureId;
  UCHAR  Status;
  UCHAR  AdditionalStatus;
  UCHAR  MaximumImageSize[4];
  UCHAR  Reserved2[3];
  UCHAR  ExpectedBufferId;
  UCHAR  ExpectedBufferOffset;
} SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR, *PSES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR;
```



## Members

<dl> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**SubEnclosureId**
</dt> <dd>

Specifies the subenclosure to which the download microcode status descriptor applies to.

</dd> <dt>

**Status**
</dt> <dd>

Specifies the status of download microcode operations for the subenclosure. After reporting a code indicating completion, the enclosure services process shall set this field to 0x00 and shall set the *AdditionalStatus* field to 0x00. Status may can contain one of the following values:



| Value                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0x00</dt> </dl>          | No download microcode operation is in progress.<br/>                                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>0x01</dt> </dl>          | Download microcode operation is in progress. The enclosure services process has received one or more Download Microcode Control diagnostic pages and is awaiting additional microcode data.<br/>                                                                                                                                                                                              |
| <dl> <dt>0x02</dt> </dl>          | Download microcode operation data transfer is complete, currently updating nonvolatile storage.<br/>                                                                                                                                                                                                                                                                                          |
| <dl> <dt>0x03</dt> </dl>          | The enclosure services process is currently updating nonvolatile storage with deferred microcode.<br/>                                                                                                                                                                                                                                                                                        |
| <dl> <dt>0x04 to 0x0F</dt> </dl>  | Reserved for codes indicating interim status<br/>                                                                                                                                                                                                                                                                                                                                             |
| <dl> <dt>0x10</dt> </dl>          | Download microcode operation complete with no error. The enclosure services process begins using the new microcode after returning this status.<br/>                                                                                                                                                                                                                                          |
| <dl> <dt>0x11</dt> </dl>          | Download microcode operation complete with no error. The enclosure services process (e.g., a standalone enclosure services process) begins using the new microcode after the next hard reset or power on.<br/>                                                                                                                                                                                |
| <dl> <dt>0x12</dt> </dl>          | Download microcode operation complete with no error. The enclosure services process (e.g., an attached enclosure services process) begins using the new microcode after the next power on.<br/>                                                                                                                                                                                               |
| <dl> <dt>0x13</dt> </dl>          | Download microcode operation complete with no error. The enclosure services process (e.g., an attached enclosure services process) begins using the new microcode after either processing a [**SES\_DOWNLOAD\_MICROCODE\_CONTROL\_DIAGNOSTIC\_PAGE**](storage-_ses_download_microcode_control_diagnostic_page) specifying the activate deferred microcode mode, hard reset, or power on.<br/> |
| <dl> <dt>0x14 to 0x6F</dt> </dl>  | Reserved for codes indicating no error.<br/>                                                                                                                                                                                                                                                                                                                                                  |
| <dl> <dt>0x70 to 0x7F</dt> </dl>  | Vendor specific<br/>                                                                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>0x80</dt> </dl>          | Error in one or more of the Download Microcode Control diagnostic page fields. <br/>                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>0x81</dt> </dl>          | Specifies a Microcode image error.<br/>                                                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>0x82</dt> </dl>          | Download microcode timeout. The enclosure services process may discard microcode data after a vendor specific amount of time, if it does not receive the entire microcode image.<br/>                                                                                                                                                                                                         |
| <dl> <dt>0x83</dt> </dl>          | Internal error in the download microcode operation. New microcode image is needed before a hard reset or power on<br/>                                                                                                                                                                                                                                                                        |
| <dl> <dt>0x84</dt> </dl>          | Internal error in the download microcode operation. Hard reset and power on safe<br/>                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>0x00</dt> </dl>          | Processed a [**SES\_DOWNLOAD\_MICROCODE\_CONTROL\_DIAGNOSTIC\_PAGE**](storage-_ses_download_microcode_control_diagnostic_page) with the *Mode* field set to 0x0F (i.e., activate deferred microcode), if there is no deferred microcode.<br/>                                                                                                                                                 |
| <dl> <dt>0x86 to 0x0EF</dt> </dl> | Reserved for codes indicating errors.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>0xF0 to 0xFF</dt> </dl>  | Vendor Specific<br/>                                                                                                                                                                                                                                                                                                                                                                          |



 

</dd> <dt>

**AdditionalStatus**
</dt> <dd>

Provides an additional status value for certain values of *Status* .

</dd> <dt>

**MaximumImageSize**
</dt> <dd>

Indicates the maximum size in bytes of the microcode image that the enclosure services process accepts. The image may be delivered using one or more [**SES\_DOWNLOAD\_MICROCODE\_CONTROL\_DIAGNOSTIC\_PAGE**](storage-_ses_download_microcode_control_diagnostic_page).

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**ExpectedBufferId**
</dt> <dd>

Indicates the next value that the enclosure services process expects in the *BufferId* field in [**SES\_DOWNLOAD\_MICROCODE\_CONTROL\_DIAGNOSTIC\_PAGE**](storage-_ses_download_microcode_control_diagnostic_page).

</dd> <dt>

**ExpectedBufferOffset**
</dt> <dd>

Indicates the next value that the enclosure services process expects in the *BufferOffset* field in [**SES\_DOWNLOAD\_MICROCODE\_CONTROL\_DIAGNOSTIC\_PAGE**](storage-_ses_download_microcode_control_diagnostic_page). If the enclosure services process accepts arbitrary *BufferOffset* values, then it shall set *ExpectedBufferOffset* to 0xFFFFFFFF.

</dd> </dl>

## Requirements



|                    |                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 10, version 1709 and later versions of Windows.<br/>                                      |
| Header<br/>  | <dl> <dt>Scsi.h (include Minitape.h or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**SES\_DOWNLOAD\_MICROCODE\_CONTROL\_DIAGNOSTIC\_PAGE**](storage-_ses_download_microcode_control_diagnostic_page)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






