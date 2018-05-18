---
title: SES\_DOWNLOAD\_MICROCODE\_STATUS\_DIAGNOSTIC\_PAGE structure
description: The Download Microcode Status diagnostic page includes information about the status of one or more download microcode operations.
ms.assetid: '4572040b-c234-4281-b9d7-14d7f2bb7506'
keywords: ["SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE structure Storage Devices", "PSES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE
api_location:
- scsi.h
api_type:
- HeaderDef
---

# SES\_DOWNLOAD\_MICROCODE\_STATUS\_DIAGNOSTIC\_PAGE structure

The Download Microcode Status diagnostic page includes information about the status of one or more download microcode operations.

## Syntax


```C++
typedef struct _SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE {
  UCHAR                                    PageCode;
  UCHAR                                    NumberOfSecondarySubEnclosures;
  UCHAR                                    PageLength[2];
  UCHAR                                    GenerationCode[4];
  SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR Descriptors[ANYSIZE_ARRAY];
} SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE, *PSES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE;
```



## Members

<dl> <dt>

**PageCode**
</dt> <dd>

Indicates the diagnostic page being sent or requested. . The value of this is 0x0E.

</dd> <dt>

**NumberOfSecondarySubEnclosures**
</dt> <dd>

Indicates the number of download microcode status descriptors in *Descriptors*, not including the primary [**SES\_DOWNLOAD\_MICROCODE\_STATUS\_DESCRIPTOR**](storage-_ses_download_microcode_status_descriptor). This value shall be set to the same value as the *NumberOfSecondarySubEnclosures* field in the [**SES\_CONFIGURATION\_DIAGNOSTIC\_PAGE**](ses-configuration-diagnostic-page.md) structure.

</dd> <dt>

**PageLength**
</dt> <dd>

Indicates the number of bytes that follow in the diagnostic page.

</dd> <dt>

**GenerationCode**
</dt> <dd>

Indicates the value of the generation code

</dd> <dt>

**Descriptors**
</dt> <dd>

Contains a [**SES\_DOWNLOAD\_MICROCODE\_STATUS\_DESCRIPTOR**](storage-_ses_download_microcode_status_descriptor) for each download microcode operation where status is being reported.

</dd> </dl>

## Requirements



|                    |                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 10, version 1709 and later versions of Windows.<br/>                                      |
| Header<br/>  | <dl> <dt>Scsi.h (include Minitape.h or Storport.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





