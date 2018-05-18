---
title: SES\_DOWNLOAD\_MICROCODE\_CONTROL\_DIAGNOSTIC\_PAGE structure
description: The SES\_DOWNLOAD\_MICROCODE\_CONTROL\_DIAGNOSTIC\_PAGE structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process.
ms.assetid: '09c2746f-cfe4-41dc-82ce-0b7e0c348897'
keywords: ["SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure Storage Devices", "PSES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE
api_location:
- scsi.h
api_type:
- HeaderDef
---

# SES\_DOWNLOAD\_MICROCODE\_CONTROL\_DIAGNOSTIC\_PAGE structure

The **SES\_DOWNLOAD\_MICROCODE\_CONTROL\_DIAGNOSTIC\_PAGE** structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process.

## Syntax


```C++
typedef struct _SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE {
  UCHAR  PageCode;
  UCHAR  SubEnclosureId;
  UCHAR  PageLength[2];
  UCHAR  ExpectedGenerationCode[4];
  UCHAR  Mode;
  UCHAR  Reserved[2];
  UCHAR  BufferID;
  UCHAR  BufferOffset[4];
  UCHAR  ImageLength[4];
  UCHAR  DataLength[4];
  UCHAR  Data[ANYSIZE_ARRAY];
} SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE, *PSES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE;
```



## Members

<dl> <dt>

**PageCode**
</dt> <dd>

Specifies the diagnostic page being sent or requested based on the value. For a Microcode Control diagnostic page, the value should be 0x0E.

</dd> <dt>

**SubEnclosureId**
</dt> <dd>

Specifies the sub enclosure to which the application client is sending the microcode image. If the value does not match a valid SUBENCLOSURE\_IDENTIFIER field value found in the [**SES\_CONFIGURATION\_DIAGNOSTIC\_PAGE**](ses-configuration-diagnostic-page.md), then the enclosure services process shall abort the download microcode operation with a status of 0x80.

</dd> <dt>

**PageLength**
</dt> <dd>

Specifies the number of bytes that follow in the diagnostic page.

</dd> <dt>

**ExpectedGenerationCode**
</dt> <dd>

Specifies the expected value of the generation code. If this parameter is not set to the current generation code, then the enclosure services process shall abort the download microcode operation with a status of 0x80.

</dd> <dt>

**Mode**
</dt> <dd>

Specifies which mode to download the microcode with.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="Download_microcode_with_offsets__save__and_activate"></span><span id="download_microcode_with_offsets__save__and_activate"></span><span id="DOWNLOAD_MICROCODE_WITH_OFFSETS__SAVE__AND_ACTIVATE"></span><dl> <dt><strong>Download microcode with offsets, save, and activate</strong></dt> <dt>0x07</dt> </dl></td>
<td>After the last SEND DIAGNOSTIC command delivers a Download Microcode Control diagnostic page to the subenclosure completes, the enclosure services process shall verify the complete microcode image (e.g., perform a vendor specific checksum) and save the new microcode image into nonvolatile storage.<br/> If there are no errors in the microcode image or in the save operation, then the enclosure services process shall perform one of the following actions:
<ul>
<li>Set the <em>Status</em> field in [<strong>SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</strong>](storage-_ses_download_microcode_status_descriptor) to 0x10, if requested, and activate the new microcode image after either returning the Download Microcode Status diagnostic page, power on, or for standalone enclosure services processes, a hard reset.</li>
<li>Set the <em>Status</em> field in [<strong>SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</strong>](storage-_ses_download_microcode_status_descriptor) to 0x11, if requested, and for standalone enclosure services processes only, activate the new microcode image after either power on or hard reset.</li>
<li>Set the <em>Status</em> field in [<strong>SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</strong>](storage-_ses_download_microcode_status_descriptor) to 0x12, if requested, and activate the new microcode image after power on.</li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td><span id="Download_microcode_with_offsets__save__and_defer_activate"></span><span id="download_microcode_with_offsets__save__and_defer_activate"></span><span id="DOWNLOAD_MICROCODE_WITH_OFFSETS__SAVE__AND_DEFER_ACTIVATE"></span><dl> <dt><strong>Download microcode with offsets, save, and defer activate</strong></dt> <dt>0x0E</dt> </dl></td>
<td>After the last SEND DIAGNOSTIC command delivering a <strong>SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE</strong> to the subenclosure completes, the enclosure services process shall verify the complete microcode image (e.g., perform a vendor specific checksum), save the new microcode image into nonvolatile storage (e.g., flash ROM), and defer activation of the new microcode. <br/> If there are no errors in the microcode image or in the save operation, then the enclosure services process shall set the <em>Status</em> field in [<strong>SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</strong>](storage-_ses_download_microcode_status_descriptor) to 0x13 in the [<strong>SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE</strong>](storage-_ses_download_microcode_status_diagnostic_page), if requested, and activate the new microcode after either:<br/>
<ul>
<li>Processing this structure with the <em>Mode</em> field set to 0x0F (i.e., Activate deferred microcode)</li>
<li>A power on</li>
<li>A hard reset</li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="Activate_deferred_microcode"></span><span id="activate_deferred_microcode"></span><span id="ACTIVATE_DEFERRED_MICROCODE"></span><dl> <dt><strong>Activate deferred microcode</strong></dt> <dt>0x0F</dt> </dl></td>
<td>After the SEND DIAGNOSTIC command specifying this mode completes, the enclosure services process shall activate the deferred microcode image, if any. <br/></td>
</tr>
<tr class="even">
<td><span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span><dl> <dt><strong>Reserved</strong></dt> <dt>All other values</dt> </dl></td>
<td>Reserved for future use.<br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**BufferID**
</dt> <dd>

Specifies a specific buffer within the enclosure services process to receive the microcode image. The enclosure services process assigns vendor specific buffer ID codes to buffers (e.g., the main firmware image may be stored in buffer 00h and a backup firmware image may be stored in buffer 01h). The enclosure services process shall support a buffer ID value of 00h. If more than one buffer is supported, then the enclosure services process shall assign additional buffer ID codes contiguously, beginning with 01h. If the enclosure services process receives an unsupported buffer ID code, then it shall abort the download microcode operation and set the *Status* field in [**SES\_DOWNLOAD\_MICROCODE\_STATUS\_DESCRIPTOR**](storage-_ses_download_microcode_status_descriptor) to 0x80 in the [**SES\_DOWNLOAD\_MICROCODE\_STATUS\_DIAGNOSTIC\_PAGE**](storage-_ses_download_microcode_status_diagnostic_page) structure.

</dd> <dt>

**BufferOffset**
</dt> <dd>

Specifies the offset in bytes within the buffer to which the microcode data is written in multiples of four. The enclosure services process may require that this field be contiguously increasing in consecutive SEND DIAGNOSTIC commands.

</dd> <dt>

**ImageLength**
</dt> <dd>

specifies the total number of bytes in the microcode image the application intends to send to the specified *BufferID*.

</dd> <dt>

**DataLength**
</dt> <dd>

Specifies the length of *Data*, in bytes.

</dd> <dt>

**Data**
</dt> <dd>

Contains part of the vendor specific microcode image.

</dd> </dl>

## Requirements



|                    |                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 10, version 1709 and later versions of Windows.<br/>                                      |
| Header<br/>  | <dl> <dt>Scsi.h (include Minitape.h or Storport.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





