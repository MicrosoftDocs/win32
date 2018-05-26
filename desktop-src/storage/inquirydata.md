---
title: INQUIRYDATA structure
description: The INQUIRYDATA structure is used in conjunction with the TapeMiniExtensionInit and TapeMiniVerifyInquiry routines to report SCSI inquiry data associated with a tape device.
ms.assetid: 2389fb1e-b16a-4d0a-b347-8b8a0f1cf061
keywords:
- INQUIRYDATA structure Storage Devices
- PINQUIRYDATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- INQUIRYDATA
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

# INQUIRYDATA structure

The INQUIRYDATA structure is used in conjunction with the [**TapeMiniExtensionInit**](tapeminiextensioninit.md) and [**TapeMiniVerifyInquiry**](tapeminiverifyinquiry.md) routines to report SCSI inquiry data associated with a tape device.

## Syntax


```C++
typedef struct _INQUIRYDATA {
  UCHAR DeviceType  :5;
  UCHAR DeviceTypeQualifier  :3;
  UCHAR DeviceTypeModifier  :7;
  UCHAR RemovableMedia  :1;
  union {
    UCHAR  Versions;
    struct {
      UCHAR ANSIVersion  :3;
      UCHAR ECMAVersion  :3;
      UCHAR ISOVersion  :2;
    };
  };
  UCHAR ResponseDataFormat  :4;
  UCHAR HiSupport  :1;
  UCHAR NormACA  :1;
  UCHAR TerminateTask  :1;
  UCHAR AERC  :1;
  UCHAR AdditionalLength;
  UCHAR Reserved;
  UCHAR Addr16  :1;
  UCHAR Addr32  :1;
  UCHAR AckReqQ  :1;
  UCHAR MediumChanger  :1;
  UCHAR MultiPort  :1;
  UCHAR ReservedBit2  :1;
  UCHAR EnclosureServices  :1;
  UCHAR ReservedBit3  :1;
  UCHAR SoftReset  :1;
  UCHAR CommandQueue  :1;
  UCHAR TransferDisable  :1;
  UCHAR LinkedCommands  :1;
  UCHAR Synchronous  :1;
  UCHAR Wide16Bit  :1;
  UCHAR Wide32Bit  :1;
  UCHAR RelativeAddressing  :1;
  UCHAR VendorId[8];
  UCHAR ProductId[16];
  UCHAR ProductRevisionLevel[4];
  UCHAR VendorSpecific[20];
  UCHAR Reserved3[40];
} INQUIRYDATA, *PINQUIRYDATA;
```



## Members

<dl> <dt>

**DeviceType**
</dt> <dd>

Specifies the type of device. For a complete list of symbolic constants that indicate the various device types, see [Specifying Device Types](https://msdn.microsoft.com/library/windows/hardware/ff563821).

</dd> <dt>

**DeviceTypeQualifier**
</dt> <dd>

Indicates whether the device is present or not. The values that this member can take are as follows:



| Value                                        | Meaning                                                                             |
|----------------------------------------------|-------------------------------------------------------------------------------------|
| DEVICE\_QUALIFIER\_ACTIVE<br/>         | The operating system supports the device, and the device is present.<br/>     |
| DEVICE\_QUALIFIER\_NOT\_ACTIVE<br/>    | The operating system supports the device, but the device is not present.<br/> |
| DEVICE\_QUALIFIER\_NOT\_SUPPORTED<br/> | The operating system does not support this device. <br/>                      |



 

</dd> <dt>

**DeviceTypeModifier**
</dt> <dd>

Specifies the device type modifier, if any, as defined by SCSI. If no device type modifier exists, this member is zero.

</dd> <dt>

**RemovableMedia**
</dt> <dd>

Indicates, when **TRUE**, that the media is removable, and when **FALSE** that the media is not removable.

</dd> <dt>

**Versions**
</dt> <dd>

Indicates the version of the inquiry data standard that this data conforms to. For more information about the version values allowed in this field, see the *SCSI Primary Commands - 2 (SPC-2)* specification.

</dd> <dt>

**ANSIVersion**
</dt> <dd>

Indicates the ANSI version of the inquiry data standard that this data conforms to. For more information about the version values allowed in this field, see the *SCSI Primary Commands - 2 (SPC-2)* specification.

</dd> <dt>

**ECMAVersion**
</dt> <dd>

Indicates the ECMA version of the inquiry data standard that this data conforms to. For more information about the version values allowed in this field, see the *SCSI Primary Commands - 2 (SPC-2)* specification.

</dd> <dt>

**ISOVersion**
</dt> <dd>

Indicates the ISO version of the inquiry data standard that this data conforms to. For more information about the version values allowed in this field, see the *SCSI Primary Commands - 2 (SPC-2)* specification.

</dd> <dt>

**ResponseDataFormat**
</dt> <dd>

Indicates the SCSI standard that governs the response data format. The value of this member must be 2.

</dd> <dt>

**HiSupport**
</dt> <dd>

Indicates, when zero, that the target does not use the hierarchical addressing model to assign LUNs to logical units. A value of 1 indicates the target uses the hierarchical addressing model to assign LUNs to logical units.

</dd> <dt>

**NormACA**
</dt> <dd>

Indicates, when set to one, that the operating system supports setting the NACA bit to one in the control byte of the command descriptor block (CDB). A value of zero indicates that the system does not support setting the NACA bit to one. For more information about the function of the NACA bit and the control byte in a CDB, see the *SCSI Primary Commands - 2 (SPC-2)* specification.

</dd> <dt>

**TerminateTask**
</dt> <dd>

Indicates, when set to one, that the target device supports the SCSI TERMINATE TASK task management function. A value of zero indicates that the target device does not support the TERMINATE TASK task management function.

</dd> <dt>

**AERC**
</dt> <dd>

Indicates, when set to one, that the target device supports the asynchronous event reporting capability. A value of zero indicates that the target device does not support asynchronous event reports. Details of the asynchronous event reporting support are protocol-specific. For more information about asynchronous even reporting, see the *SCSI Primary Commands - 2 (SPC-2)* specification.

</dd> <dt>

**AdditionalLength**
</dt> <dd>

Specifies the length in bytes of the parameters of the command descriptor block (CDB).

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**Addr16**
</dt> <dd>

Indicates, when set to one, that the target supports 16-bit wide SCSI addresses. A value of zero indicates that the device does not support 32-bit wide SCSI addresses.

</dd> <dt>

**Addr32**
</dt> <dd>

Indicates, when set to one, that the target supports 32-bit wide SCSI addresses. A value of zero indicates that the device does not support 32-bit wide SCSI addresses.

</dd> <dt>

**AckReqQ**
</dt> <dd>

Indicates, when set to one, that the target supports a request and acknowledge data transfer handshake on the secondary bus. A value of zero indicates that the target does not support this function.

</dd> <dt>

**MediumChanger**
</dt> <dd>

Indicates, when set to one, that the device is embedded within or attached to a medium transport element. A value of zero indicates that the device is not embedded within or attached to a medium transport element.

</dd> <dt>

**MultiPort**
</dt> <dd>

Indicates, when set to one, that the target device is a multiport (2 or more ports) device that conforms to the SCSI-3 multiport device requirements. A value of zero indicates that this device has a single port and does not implement the multiport requirements.

</dd> <dt>

**ReservedBit2**
</dt> <dd>

Reserved.

</dd> <dt>

**EnclosureServices**
</dt> <dd>

Indicates, when set to one, that the device contains an embedded enclosure services component. A value of zero indicates that the device does not contain an embedded enclosure services component.

</dd> <dt>

**ReservedBit3**
</dt> <dd>

Reserved.

</dd> <dt>

**SoftReset**
</dt> <dd>

Indicates, when set to one, that the target device supports soft resets. A value of zero indicates that the target does not support soft resets.

</dd> <dt>

**CommandQueue**
</dt> <dd>

Indicates, when set to one, that the target device supports command queuing for this logical unit. However, a value of zero does not necessarily indicate that the target device does not support command queuing. The meaning of these values depends on the values present in the SCSI inquiry data. For information about the meaning of the command queuing bit, see the *SCSI Primary Commands - 2 (SPC-2)* specification.

</dd> <dt>

**TransferDisable**
</dt> <dd>

Indicates, when set to one, that the target supports the SCSI CONTINUE TASK and TARGET TRANSFER DISABLE messages. A value of zero indicates that the device does not support one or both of these messages. For more information about the CONTINUE TASK and TARGET TRANSFER DISABLE messages, see the *SCSI Primary Commands - 2 (SPC-2)* specification.

</dd> <dt>

**LinkedCommands**
</dt> <dd>

Indicates, when set to one, that the operating system supports linked commands. A value of zero indicates the operating system does not support linked commands.

</dd> <dt>

**Synchronous**
</dt> <dd>

Indicates, when set to one, that the target supports synchronous data transfer. A value of zero indicates that the target does not support synchronous data transfer.

</dd> <dt>

**Wide16Bit**
</dt> <dd>

Indicates, when set to one, that the target supports 16-bit wide data transfers. A value of zero indicates that the device does not support 16-bit wide data transfers.

</dd> <dt>

**Wide32Bit**
</dt> <dd>

Indicates, when set to one, that the target supports 32-bit wide data transfers. A value of zero indicates that the device does not support 32-bit wide data transfers.

</dd> <dt>

**RelativeAddressing**
</dt> <dd>

Indicates, when set to one, that the operating system supports the relative addressing mode. A value of zero indicates the operating system does not support relative addressing.

</dd> <dt>

**VendorId**
</dt> <dd>

Contains eight bytes of ASCII data that identifies the vendor of the product.

</dd> <dt>

**ProductId**
</dt> <dd>

Contains sixteen bytes of ASCII data that indicates the product ID, as defined by the vendor. The data shall be left-aligned within this field and the unused bytes filled with ASCII blanks.

</dd> <dt>

**ProductRevisionLevel**
</dt> <dd>

Contains four bytes of ASCII data that indicates the product revision level, as defined by the vendor.

</dd> <dt>

**VendorSpecific**
</dt> <dd>

Contains 20 bytes of vendor-specific data.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> </dl>

## Requirements



|                   |                                                                                                                               |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Scsi.h (include Scsi.h, Minitape.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**TapeMiniExtensionInit**](tapeminiextensioninit.md)
</dt> <dt>

[**TapeMiniVerifyInquiry**](tapeminiverifyinquiry.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20INQUIRYDATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






