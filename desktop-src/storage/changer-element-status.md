---
title: CHANGER\_ELEMENT\_STATUS structure
description: The ChangerGetElementStatus routine returns status information in this structure.
ms.assetid: 3debcf76-bb84-48ec-933e-03e099ad764f
keywords:
- CHANGER_ELEMENT_STATUS structure Storage Devices
- PCHANGER_ELEMENT_STATUS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CHANGER_ELEMENT_STATUS
api_location:
- ntddchgr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CHANGER\_ELEMENT\_STATUS structure

The [**ChangerGetElementStatus**](changergetelementstatus.md) routine returns status information in this structure.

## Syntax


```C++
typedef struct _CHANGER_ELEMENT_STATUS {
  CHANGER_ELEMENT Element;
  CHANGER_ELEMENT SrcElementAddress;
  ULONG           Flags;
  ULONG           ExceptionCode;
  UCHAR           TargetId;
  UCHAR           Lun;
  USHORT          Reserved;
  UCHAR           PrimaryVolumeID[MAX_VOLUME_ID_SIZE];
  UCHAR           AlternateVolumeID[MAX_VOLUME_ID_SIZE];
} CHANGER_ELEMENT_STATUS, *PCHANGER_ELEMENT_STATUS;
```



## Members

<dl> <dt>

**Element**
</dt> <dd>

Specifies the element of type [**CHANGER\_ELEMENT**](changer-element.md) to which this structure refers.

</dd> <dt>

**SrcElementAddress**
</dt> <dd>

Specifies the element of type [**CHANGER\_ELEMENT**](changer-element.md) from which the media currently in this element was most recently moved. This member is valid only if ELEMENT\_STATUS\_SVALID is also set in **Flags**. This value must be a zero-based offset from the device-unique value.

</dd> <dt>

**Flags**
</dt> <dd>

Indicates the status of the element, which can be one or more of the following values.

<dl> <dt>

<span id="ELEMENT_STATUS_FULL"></span><span id="element_status_full"></span>ELEMENT\_STATUS\_FULL
</dt> <dd>

The element contains a piece of media. This flag is valid if **ElementType** in the **Element** member is **ChangerDrive**, **ChangerSlot**, or **ChangerTransport**. If **ElementType** is **ChangerIEPort**, this flag is valid only if CHANGER\_REPORT\_IEPORT\_STATE is also set in **Features0** of GET\_CHANGER\_PARAMETERS.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_IMPEXP"></span><span id="element_status_impexp"></span>ELEMENT\_STATUS\_IMPEXP
</dt> <dd>

The media in this element was placed there by an operator. This flag is valid only if **ElementType** in the **Element** member is **ChangerIEPort**.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_EXCEPT"></span><span id="element_status_except"></span>ELEMENT\_STATUS\_EXCEPT
</dt> <dd>

The element is in an abnormal state. Check the **ExceptionCode** member for more information.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_ACCESS"></span><span id="element_status_access"></span>ELEMENT\_STATUS\_ACCESS
</dt> <dd>

The changer's transport element can access the piece of media in this element. The miniclass driver clears this flag to indicate that the media is not accessible for one of the following reasons: If **ElementType** in the **Element** member is **ChangerSlot**, the slot is not present in the changer (for example, the magazine containing the slot has been physically removed). If **ElementType** is **ChangerDrive**, the drive is broken or has been removed. If **ElementType** is **ChangerIEPort**, the IEport is extended.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_EXENAB"></span><span id="element_status_exenab"></span>ELEMENT\_STATUS\_EXENAB
</dt> <dd>

The element supports export of media through the changer's IEport.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_INENAB"></span><span id="element_status_inenab"></span>ELEMENT\_STATUS\_INENAB
</dt> <dd>

The element supports import of media through the changer's IEport.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_LUN_VALID"></span><span id="element_status_lun_valid"></span>ELEMENT\_STATUS\_LUN\_VALID
</dt> <dd>

The device number in the **Lun** member is valid. This flag is valid only if **ElementType** in the **Element** member is **ChangerDrive**.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_ID_VALID"></span><span id="element_status_id_valid"></span>ELEMENT\_STATUS\_ID\_VALID
</dt> <dd>

The SCSI target ID in the **TargetID** member is valid. This flag is valid only if **ElementType** in the **Element** member is **ChangerDrive**.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_NOT_BUS"></span><span id="element_status_not_bus"></span>ELEMENT\_STATUS\_NOT\_BUS
</dt> <dd>

The drive at the address indicated by **Lun** and **TargetID** is on a different SCSI bus than the changer itself.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_INVERT"></span><span id="element_status_invert"></span>ELEMENT\_STATUS\_INVERT
</dt> <dd>

The media in the element was flipped. This flag is valid only if the ELEMENT\_STATUS\_SVALID flag is also set.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_SVALID"></span><span id="element_status_svalid"></span>ELEMENT\_STATUS\_SVALID
</dt> <dd>

The **SourceElement** member and ELEMENT\_STATUS\_INVERT flag are both valid.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_PVOLTAG"></span><span id="element_status_pvoltag"></span>ELEMENT\_STATUS\_PVOLTAG
</dt> <dd>

Primary volume information in the **PrimaryVolumeID** member is valid.

</dd> </dl>

<dl> <dt>

<span id="ELEMENT_STATUS_AVOLTAG"></span><span id="element_status_avoltag"></span>ELEMENT\_STATUS\_AVOLTAG
</dt> <dd>

Alternate volume information in the **AlternateVolumeID** member is valid.

</dd> </dl> </dd> <dt>

**ExceptionCode**
</dt> <dd>

Indicates that the element is in an abnormal state. This member is valid only if ELEMENT\_STATUS\_EXCEPT is set in **Flags**. **ExceptionCode** can be set to one of the following values.

<dl> <dt>

<span id="ERROR_LABEL_UNREADABLE"></span><span id="error_label_unreadable"></span>ERROR\_LABEL\_UNREADABLE
</dt> <dd>

The changer's bar code reader could not read the bar code label on the piece of media in this element, because the media is missing, damaged, improperly positioned, or upside down.

</dd> </dl>

<dl> <dt>

<span id="ERROR_LABEL_QUESTIONABLE"></span><span id="error_label_questionable"></span>ERROR\_LABEL\_QUESTIONABLE
</dt> <dd>

The label might be invalid due to a unit attention condition.

</dd> </dl>

<dl> <dt>

<span id="ERROR_SLOT_NOT_PRESENT"></span><span id="error_slot_not_present"></span>ERROR\_SLOT\_NOT\_PRESENT
</dt> <dd>

The slot at this element address is currently not installed in the changer. A miniclass driver sets this code for each slot in a removable magazine to indicate that the magazine has been removed.

</dd> </dl>

<dl> <dt>

<span id="ERROR_DRIVE_NOT_INSTALLED"></span><span id="error_drive_not_installed"></span>ERROR\_DRIVE\_NOT\_INSTALLED
</dt> <dd>

The drive at this element address is absent. If a changer can continue to operate without the drive, its miniclass driver sets ERROR\_DRIVE\_NOT\_INSTALLED for the drive.

</dd> </dl>

<dl> <dt>

<span id="ERROR_TRAY_MALFUNCTION"></span><span id="error_tray_malfunction"></span>ERROR\_TRAY\_MALFUNCTION
</dt> <dd>

The drive at this element address has a tray that must be extended to load or remove media, and the tray is not extending as required.

</dd> </dl>

<dl> <dt>

<span id="ERROR_UNHANDLED_ERROR"></span><span id="error_unhandled_error"></span>ERROR\_UNHANDLED\_ERROR
</dt> <dd>

Unknown error condition.

</dd> </dl> </dd> <dt>

**TargetId**
</dt> <dd>

Specifies the SCSI target ID of the drive at this element address for a SCSI changer. This member is valid only if **ElementType** in the **Element** member is **ChangerDrive** and ELEMENT\_STATUS\_ID\_VALID is set in **Flags**.

</dd> <dt>

**Lun**
</dt> <dd>

Specifies the SCSI device number of the drive at this element address. This member is valid only if **ElementType** in the **Element** member is **ChangerDrive** and ELEMENT\_STATUS\_LUN\_VALID is set in **Flags**.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use. The value of this member must be zero.

</dd> <dt>

**PrimaryVolumeID**
</dt> <dd>

Specifies the primary volume identifier for the media. If the changer supports a bar code reader and the reader is installed (as indicated by CHANGER\_BAR\_CODE\_SCANNER\_INSTALLED in **Features0** of GET\_CHANGER\_PARAMETERS), the miniclass driver must set **PrimaryVolumeID** to the bar code of the media. If the changer does not support a bar code reader, the miniclass driver should set **PrimaryVolumeID** to the value previously assigned to the media using the **ChangerQueryVolumeTags** routine with an ASSERT\_PRIMARY or REPLACE\_PRIMARY action. This member is valid only if ELEMENT\_STATUS\_PVOLTAG is also set in **Flags**. If the volume identifier is missing or unreadable, the miniclass driver should clear this flag and set the appropriate error status. This identifier must be no larger than MAX\_VOLUME\_ID\_SIZE bytes.

</dd> <dt>

**AlternateVolumeID**
</dt> <dd>

Specifies alternate volume identification for the media. This member is valid for two-sided media only, and pertains to the ID of the inverted side. It never represents a bar code. The miniclass driver must set **AlternateVolumeID** to the value previously assigned to the media using the **ChangerQueryVolumeTags** routine with an ASSERT\_ALTERNATE or REPLACE\_ALTERNATE action. The identifier must be no larger than MAX\_VOLUME\_ID\_SIZE bytes and is valid only if ELEMENT\_STATUS\_AVOLTAG is also set in **Flags**.

</dd> </dl>

## Remarks

For most element types, changer miniclass drivers use CHANGER\_ELEMENT\_STATUS to report the status of specified elements to the changer class driver. Some elements of type **ChangerDrive**, however, return product information data. If the device provides product information, the miniclass driver will report the element status data in a structure of type [**CHANGER\_ELEMENT\_STATUS\_EX**](changer-element-status-ex.md) instead of using CHANGER\_ELEMENT\_STATUS. The miniclass driver indicates that product information is present by setting ELEMENT\_STATUS\_PRODUCT\_DATA in the **Flags** member of the structure.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> <dt>

[**ChangerGetElementStatus**](changergetelementstatus.md)
</dt> <dt>

[**ChangerQueryVolumeTags**](changerqueryvolumetags.md)
</dt> <dt>

[**CHANGER\_ELEMENT\_STATUS\_EX**](changer-element-status-ex.md)
</dt> <dt>

[**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](ioctl-changer-get-element-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_ELEMENT_STATUS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






