---
description: Used to report status or error information in response to a SCSI Request Sense command.
ms.assetid: 43B2FE98-1468-4457-AB7D-3038C16E20B6
title: SENSE_DATA structure (Scsi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SENSE_DATA
api_type: 
- HeaderDef
api_location: 
- Scsi.h
---

# SENSE\_DATA structure

Used to report status or error information in response to a SCSI **Request Sense** command.

## Syntax


```C++
typedef struct _SENSE_DATA {
  UCHAR  ErrorCode  :7;
  UCHAR  Valid  :1;
  UCHAR  SegmentNumber;
  UCHAR  SenseKey  :4;
  UCHAR  Reserved  :1;
  UCHAR  IncorrectLength  :1;
  UCHAR  EndOfMedia  :1;
  UCHAR  FileMark  :1;
  UCHAR  Information[4];
  UCHAR  AdditionalSenseLength;
  UCHAR  CommandSpecificInformation[4];
  UCHAR  AdditionalSenseCode;
  UCHAR  AdditionalSenseCodeQualifier;
  UCHAR  FieldReplaceableUnitCode;
  UCHAR  SenseKeySpecific[3];
} SENSE_DATA, *PSENSE_DATA;
```



## Members

<dl> <dt>

**ErrorCode**
</dt> <dd>

The report type.



| Value                                                                           | Meaning                     |
|---------------------------------------------------------------------------------|-----------------------------|
| <dl> <dt>0x70</dt> </dl> | Current errors.<br/>  |
| <dl> <dt>0x71</dt> </dl> | Deferred errors.<br/> |



 

</dd> <dt>

**Valid**
</dt> <dd>

1 if the **Information** field is defined in a standard; otherwise the **Information** field is vendor-specific and not defined by a standard.

</dd> <dt>

**SegmentNumber**
</dt> <dd>

Obsolete.

</dd> <dt>

**SenseKey**
</dt> <dd>

Indicates the category of error.

<dl> <dt>

<span id="No_Sense"></span><span id="no_sense"></span><span id="NO_SENSE"></span>**No Sense** (0x0)
</dt> <dt>

<span id="Recovered_Error"></span><span id="recovered_error"></span><span id="RECOVERED_ERROR"></span>**Recovered Error** (0x1)
</dt> <dt>

<span id="Not_Ready"></span><span id="not_ready"></span><span id="NOT_READY"></span>**Not Ready** (0x2)
</dt> <dt>

<span id="Medium_Error"></span><span id="medium_error"></span><span id="MEDIUM_ERROR"></span>**Medium Error** (0x3)
</dt> <dt>

<span id="Hardware_Error"></span><span id="hardware_error"></span><span id="HARDWARE_ERROR"></span>**Hardware Error** (0x4)
</dt> <dt>

<span id="Illegal_Request"></span><span id="illegal_request"></span><span id="ILLEGAL_REQUEST"></span>**Illegal Request** (0x5)
</dt> <dt>

<span id="Unit_Attention"></span><span id="unit_attention"></span><span id="UNIT_ATTENTION"></span>**Unit Attention** (0x6)
</dt> <dt>

<span id="Data_Protect"></span><span id="data_protect"></span><span id="DATA_PROTECT"></span>**Data Protect** (0x7)
</dt> <dt>

<span id="Firmware_Error"></span><span id="firmware_error"></span><span id="FIRMWARE_ERROR"></span>**Firmware Error** (0x9)
</dt> <dt>

<span id="Aborted_Command"></span><span id="aborted_command"></span><span id="ABORTED_COMMAND"></span>**Aborted Command** (0xB)
</dt> <dt>

<span id="Equal"></span><span id="equal"></span><span id="EQUAL"></span>**Equal** (0xC)
</dt> <dt>

<span id="Volume_Overflow"></span><span id="volume_overflow"></span><span id="VOLUME_OVERFLOW"></span>**Volume Overflow** (0xD)
</dt> <dt>

<span id="Miscompare"></span><span id="miscompare"></span><span id="MISCOMPARE"></span>**Miscompare** (0xE)
</dt> </dl> </dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**IncorrectLength**
</dt> <dd>

1 if the requested logical block length does not match the logical block length of the data on the media.

</dd> <dt>

**EndOfMedia**
</dt> <dd>

1 if a sequential-access device has reached end-of-media, or a printer is out of paper.

</dd> <dt>

**FileMark**
</dt> <dd>

1 if the current command has reached a filemark or setmark. Only valid for sequential-access devices.

</dd> <dt>

**Information**
</dt> <dd>

Device-type or command specific data.

</dd> <dt>

**AdditionalSenseLength**
</dt> <dd>

The length in bytes of the remainder of the structure. The total length minus 7.

</dd> <dt>

**CommandSpecificInformation**
</dt> <dd>

Command-specific data. Values are defined in the appropriate command standard.

</dd> <dt>

**AdditionalSenseCode**
</dt> <dd>

Device specific code that describes the error reported in the **SenseKey** field.

</dd> <dt>

**AdditionalSenseCodeQualifier**
</dt> <dd>

Can contain additional detail about the **AdditionalSenseCode** field.

</dd> <dt>

**FieldReplaceableUnitCode**
</dt> <dd>

Vender-specific information about the component associated with this sense data.

</dd> <dt>

**SenseKeySpecific**
</dt> <dd>

The content and format of the sense key specific information is determined by the value of the **SenseKey** field.

</dd> </dl>

## Remarks

For more information about the sense data format, see [SCSI Request Sense Command](https://wikipedia.org/wiki/SCSI_command) (https://wikipedia.org/wiki/SCSI_command).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Scsi.h</dt> </dl> |



## See also

<dl> <dt>

[iSCSI Target Pass-Through](/powershell/module/iscsi)
</dt> <dt>

[SCSI\_PASS\_THROUGH\_DIRECT](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through_direct)
</dt> </dl>

 

 




