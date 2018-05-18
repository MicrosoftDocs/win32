---
title: SES\_CONFIGURATION\_DIAGNOSTIC\_PAGE structure
description: TBD.
ms.assetid: '0FD748D6-F598-44D1-A8D3-E63764CB90C6'
keywords: ["SES_CONFIGURATION_DIAGNOSTIC_PAGE structure Storage Devices", "PSES_CONFIGURATION_DIAGNOSTIC_PAGE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SES_CONFIGURATION_DIAGNOSTIC_PAGE
api_location:
- scsi.h
api_type:
- HeaderDef
---

# SES\_CONFIGURATION\_DIAGNOSTIC\_PAGE structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

TBD

## Syntax


```C++
typedef struct _SES_CONFIGURATION_DIAGNOSTIC_PAGE {
  UCHAR                    PageCode;
  UCHAR                    NumberOfSecondarySubEnclosures;
  UCHAR                    PageLength[2];
  UCHAR                    GenerationCode[4];
  SES_ENCLOSURE_DESCRIPTOR Descriptors[ANYSIZE_ARRAY];
} SES_CONFIGURATION_DIAGNOSTIC_PAGE, *PSES_CONFIGURATION_DIAGNOSTIC_PAGE;
```



## Members

<dl> <dt>

**PageCode**
</dt> <dd>

Specifies the diagnostic page being sent or requested based on the value. For a Microcode Control diagnostic page, the value should be 0x01.

</dd> <dt>

**NumberOfSecondarySubEnclosures**
</dt> <dd>

Specifies the number of separate subenclosures included in the enclosure descriptor list, not including the primary subenclosure. If this is set to zero, only the primary subenclosure exists.

</dd> <dt>

**PageLength**
</dt> <dd>

Specifies the length of the diagnostic page, in bytes.

</dd> <dt>

**GenerationCode**
</dt> <dd>

Specifies the value of the generation code.

</dd> <dt>

**Descriptors**
</dt> <dd>

Specifies the enclosure descriptors for the primary and secondary enclosures. The primary enclosure is the first index.

</dd> </dl>

## Requirements



|                    |                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 10, version 1709 and later versions of Windows.<br/>                                      |
| Header<br/>  | <dl> <dt>Scsi.h (include Minitape.h or Storport.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SES_CONFIGURATION_DIAGNOSTIC_PAGE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





