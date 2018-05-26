---
title: GET\_CHANGER\_PARAMETERS structure
description: Retrieves the characteristics of the changer.
ms.assetid: c9a47406-5dd2-4cda-b241-3a439406ac75
keywords:
- GET_CHANGER_PARAMETERS structure Storage Devices
- PGET_CHANGER_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- GET_CHANGER_PARAMETERS
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

# GET\_CHANGER\_PARAMETERS structure

Retrieves the characteristics of the changer.

## Syntax


```C++
typedef struct _GET_CHANGER_PARAMETERS {
  ULONG  Size;
  USHORT NumberTransportElements;
  USHORT NumberStorageElements;
  USHORT NumberCleanerSlots;
  USHORT NumberIEElements;
  USHORT NumberDataTransferElements;
  USHORT NumberOfDoors;
  USHORT FirstSlotNumber;
  USHORT FirstDriveNumber;
  USHORT FirstTransportNumber;
  USHORT FirstIEPortNumber;
  USHORT FirstCleanerSlotAddress;
  USHORT MagazineSize;
  ULONG  DriveCleanTimeout;
  ULONG  Features0;
  ULONG  Features1;
  UCHAR  MoveFromTransport;
  UCHAR  MoveFromSlot;
  UCHAR  MoveFromIePort;
  UCHAR  MoveFromDrive;
  UCHAR  ExchangeFromTransport;
  UCHAR  ExchangeFromSlot;
  UCHAR  ExchangeFromIePort;
  UCHAR  ExchangeFromDrive;
  UCHAR  LockUnlockCapabilities;
  UCHAR  PositionCapabilities;
  UCHAR  Reserved1[2];
  ULONG  Reserved2[2];
} GET_CHANGER_PARAMETERS, *PGET_CHANGER_PARAMETERS;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The size of this structure in bytes. Set to **sizeof**(GET\_CHANGER\_PARAMETERS). In effect, this member indicates the version of this structure being used by the miniclass driver.

</dd> <dt>

**NumberTransportElements**
</dt> <dd>

Indicates the number of transport elements in the changer. For a SCSI changer, this is defined in the element address page. This value is almost always 1, because most changers have a single transport element, which can have one or two picker mechanisms. A changer that has two picker mechanisms on its transport must not be represented as having two transports, because pickers cannot be addressed individually. High-end media libraries can have dual and multiple transport elements for fault tolerance.

</dd> <dt>

**NumberStorageElements**
</dt> <dd>

Indicates the number of storage elements (slots) in the changer. For a SCSI changer, this is defined in the element address page. This value represents the maximum number of slots available for this changer, including those in removable magazines, whether the magazines are installed. If **NumberCleanerSlots** is 1, then **NumberStorageElements** is 1 less than the maximum number of slots in the changer.

</dd> <dt>

**NumberCleanerSlots**
</dt> <dd>

Indicates the number of storage elements (slots) for cleaner cartridges in the changer. For a SCSI changer, this value is not reported in mode sense data, so the miniclass driver must provide it. The miniclass driver should set **NumberCleanerSlots** to 1 only if the operator's guide for the changer identifies a specific slot as a cleaner slot. If **NumberCleanerSlots** is 1, then **FirstCleanerSlotAddress** indicates the zero-based address of the slot in which a drive cleaner should be inserted. If the changer does not support drive cleaning by programmatically moving the cleaner cartridge from its slot to a drive, the miniclass driver must set **NumberCleanerSlots** to 0. **NumberCleanerSlots** must not be greater than 1.

</dd> <dt>

**NumberIEElements**
</dt> <dd>

Indicates the number of IEport elements the changer has for inserting and ejecting of media. For a SCSI changer, this is defined in the element address page. An IEport element must not be part of the storage element (slot) space, and it must be possible to transport media between the IEport and a slot using a MOVE MEDIUM SCSI command. If the changer has a door and not a true IEport, the miniclass driver must set **NumberIEElements** to 0.

</dd> <dt>

**NumberDataTransferElements**
</dt> <dd>

Indicates the number of data transfer elements (drives) in the changer. For a SCSI changer, this is defined in the element address page. Unlike **NumberStorageElements**, which indicates the total number of possible slots whether the slots are actually present, **NumberDataTransferElements** indicates the number of drives that are actually present in the changer.

</dd> <dt>

**NumberOfDoors**
</dt> <dd>

Indicates the number of doors that the changer has. For a SCSI changer, this value is not reported in mode sense data, so the miniclass driver must provide it. A door provides access to all media in the changer at once, unlike an IEport which provides access to one or more, but not all, media. A changer's door can be a physical front door or a single magazine that contains all media. If a changer supports only an IEport for inserting and ejecting media, the **NumberOfDoors** must be 0.

</dd> <dt>

**FirstSlotNumber**
</dt> <dd>

Indicates the number used by the changer vendor to identify the first storage element (slot) in the changer to the end user, either by marking a magazine or by defining a slot numbering scheme in the changer's operators guide. **FirstSlotNumber** is typically 0 or 1, but it can be the first address in a consecutive range of slot addresses defined by the vendor.

</dd> <dt>

**FirstDriveNumber**
</dt> <dd>

Indicates the number used by the changer vendor to identify the first data transfer element (drive) in the changer to the end user. **FirstDriveNumber** is typically 0 or 1, but it can be the first address in a consecutive range of drive addresses defined by the vendor.

</dd> <dt>

**FirstTransportNumber**
</dt> <dd>

Indicates the number used by the changer vendor to identify the first (and usually only) transport element in the changer to the end user. **FirstTransportNumber** is typically 0 or 1, but it can be the first address in a consecutive range of transport addresses defined by the vendor.

</dd> <dt>

**FirstIEPortNumber**
</dt> <dd>

Indicates the number used by the changer vendor to identify the first (and usually only) IEport in the changer to the end user. **FirstIEPortNumber** is typically 0 or 1, but it can be the first address in a consecutive range of IEport addresses defined by the vendor. If **NumberIEElements** is 0, **FirstIEPortNumber** must also be 0.

</dd> <dt>

**FirstCleanerSlotAddress**
</dt> <dd>

Indicates the number used by the changer vendor to identify the first (and only) slot address assigned to a drive cleaner cartridge to the end user. This must be the value defined by the vendor in the changer's operators guide. For example, if a changer has 8 slots numbered 1 through 8 and its operator's guide designates slot 8 as the drive cleaner slot, **FirstSlotNumber** would be 1 and **FirstCleanerSlotAddress** would be 8. If the same 8 slots were numbered 0 through 7, **FirstSlotNumber** would be 0 and **FirstCleanerSlotAddress** would be 7. If **NumberCleanerSlots** is 0, **FirstCleanerSlotAddress** must be 0.

</dd> <dt>

**MagazineSize**
</dt> <dd>

Indicates the number of slots in the removable magazines in the changer. This member is valid only if CHANGER\_CARTRIDGE\_MAGAZINE is set in **Features0**.

</dd> <dt>

**DriveCleanTimeout**
</dt> <dd>

Indicates twice the maximum number of seconds a cleaning is expected to take. The changer's drives should be cleaned by its cleaner cartridge in half the time specified by **DriveCleanTimeout**. For example, if a drive is typically cleaned in 300 seconds (5 minutes), **DriveCleanTimeout** should be set to 600.

</dd> <dt>

**Features0**
</dt> <dd>

Indicates the features supported by the changer. This member can have one or more of the following values bitwise ORed together.

<dl> <dt>

<span id="CHANGER_BAR_CODE_SCANNER_INSTALLED"></span><span id="changer_bar_code_scanner_installed"></span>CHANGER\_BAR\_CODE\_SCANNER\_INSTALLED
</dt> <dd>

The changer supports a bar code reader and the reader is installed. A miniclass driver must not hardcode this flag unless the changer's bar code reader is always installed. If the bar code reader is optional, the miniclass driver must determine whether the reader is actually installed and set the flag accordingly.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_INIT_ELEM_STAT_WITH_RANGE"></span><span id="changer_init_elem_stat_with_range"></span>CHANGER\_INIT\_ELEM\_STAT\_WITH\_RANGE
</dt> <dd>

The changer can initialize elements within a specified range. For a SCSI changer, this flag indicates whether the changer supports the INITIALIZE ELEMENT STATUS WITH RANGE SCSI command.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_CLOSE_IEPORT"></span><span id="changer_close_ieport"></span>CHANGER\_CLOSE\_IEPORT
</dt> <dd>

The changer has an IEport and can retract the IEport programmatically.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_OPEN_IEPORT"></span><span id="changer_open_ieport"></span>CHANGER\_OPEN\_IEPORT
</dt> <dd>

The changer has an IEport and can extend the IEport programmatically.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_STATUS_NON_VOLATILE"></span><span id="changer_status_non_volatile"></span>CHANGER\_STATUS\_NON\_VOLATILE
</dt> <dd>

The changer uses nonvolatile memory for element status information.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_EXCHANGE_MEDIA"></span><span id="changer_exchange_media"></span>CHANGER\_EXCHANGE\_MEDIA
</dt> <dd>

Supports EXCHANGE MEDIUM SCSI command either by handling two volumes at a time or by using other changer elements to emulate this capability.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_CLEANER_SLOT"></span><span id="changer_cleaner_slot"></span>CHANGER\_CLEANER\_SLOT
</dt> <dd>

Indicates that the changer has a specific slot designated for a cleaner cartridge. If this flag is set, **NumberCleanerSlots** must be one and **FirstCleanerSlotAddress** must specify the address of the cleaner slot. This bit can only be set if CHANGER\_DRIVE\_CLEANING\_REQUIRED is set and CHANGER\_CLEANER\_OPS\_NOT\_SUPPORTED is reset.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_LOCK_UNLOCK"></span><span id="changer_lock_unlock"></span>CHANGER\_LOCK\_UNLOCK
</dt> <dd>

The changer's door, IEport, or keypad can be locked or unlocked programmatically. If this flag is set, **LockUnlockCapabilities** indicates which elements can be locked or unlocked.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_CARTRIDGE_MAGAZINE"></span><span id="changer_cartridge_magazine"></span>CHANGER\_CARTRIDGE\_MAGAZINE
</dt> <dd>

The changer uses removable cartridge magazines for some or all storage slots.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_MEDIUM_FLIP"></span><span id="changer_medium_flip"></span>CHANGER\_MEDIUM\_FLIP
</dt> <dd>

The changer's transport element supports flipping (rotating) media. For a SCSI changer, this flag reflects the rotate bit in the transport geometry parameters page.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_POSITION_TO_ELEMENT"></span><span id="changer_position_to_element"></span>CHANGER\_POSITION\_TO\_ELEMENT
</dt> <dd>

The changer can position the transport to a particular destination. For a SCSI changer, this flag indicates whether the changer supports the POSITION TO ELEMENT SCSI command. If this flag is set, **PositionCapabilities** indicates the elements to which the transport can be positioned.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_REPORT_IEPORT_STATE"></span><span id="changer_report_ieport_state"></span>CHANGER\_REPORT\_IEPORT\_STATE
</dt> <dd>

The changer can report whether media is present in the IEport. Such a changer must have a sensor in the IEport to detect the presence or absence of media.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_STORAGE_DRIVE"></span><span id="changer_storage_drive"></span>CHANGER\_STORAGE\_DRIVE
</dt> <dd>

The changer can use a drive as an independent storage element; that is, it can store media in the drive without reading it. For a SCSI changer, this flag reflects the state of the DT bit in the device capabilities page.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_STORAGE_IEPORT"></span><span id="changer_storage_ieport"></span>CHANGER\_STORAGE\_IEPORT
</dt> <dd>

The changer can use an IEport as an independent storage element. For a SCSI changer, this flag reflects the state of the I/E bit in the device capabilities page.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_STORAGE_SLOT"></span><span id="changer_storage_slot"></span>CHANGER\_STORAGE\_SLOT
</dt> <dd>

The changer can use a slot as an independent storage element for media. For a SCSI changer, this flag reflects the state of the ST bit in the device capabilities page. Slots are the normal storage location for media, so the changer must support this functionality.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_STORAGE_TRANSPORT"></span><span id="changer_storage_transport"></span>CHANGER\_STORAGE\_TRANSPORT
</dt> <dd>

The changer can use a transport as an independent storage element. For a SCSI changer, this flag reflects the state of the MT bit in the device capabilities page.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_DRIVE_CLEANING_REQUIRED"></span><span id="changer_drive_cleaning_required"></span>CHANGER\_DRIVE\_CLEANING\_REQUIRED
</dt> <dd>

Indicates that the changer's drives might periodically report sense codes that indicate that the drive requires cleaning.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_PREDISMOUNT_EJECT_REQUIRED"></span><span id="changer_predismount_eject_required"></span>CHANGER\_PREDISMOUNT\_EJECT\_REQUIRED
</dt> <dd>

The changer requires an explicit command issued through a mass storage driver (tape, disk, or CD-ROM, for example) to eject media from a drive before the changer can move the media from a drive to a slot. If the changer ejects media automatically, the miniclass driver should clear this flag.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_CLEANER_ACCESS_NOT_VALID"></span><span id="changer_cleaner_access_not_valid"></span>CHANGER\_CLEANER\_ACCESS\_NOT\_VALID
</dt> <dd>

The ELEMENT\_STATUS\_ACCESS flag in a CHANGER\_ELEMENT\_STATUS structure for a data transport element is invalid when the transport element contains a cleaning cartridge.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_DRIVE_EMPTY_ON_DOOR_ACCESS"></span><span id="changer_drive_empty_on_door_access"></span>CHANGER\_DRIVE\_EMPTY\_ON\_DOOR\_ACCESS
</dt> <dd>

The changer requires all drives to be empty (dismounted) before they can be accessed through its door. The miniclass driver should set this flag if the changer has static-sensitive drives that could be affected by an operator gaining access to the inside of the changer, or if the changer automatically ejects media from its drives when the operator attempts to physically open the door.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_VOLUME_IDENTIFICATION"></span><span id="changer_volume_identification"></span>CHANGER\_VOLUME\_IDENTIFICATION
</dt> <dd>

The changer supports volume identification. For a SCSI changer, this flag indicates whether the changer supports the SEND VOLUME TAG and REQUEST VOLUME ELEMENT ADDRESS SCSI commands.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_VOLUME_SEARCH"></span><span id="changer_volume_search"></span>CHANGER\_VOLUME\_SEARCH
</dt> <dd>

The changer can search for volume information. For a SCSI changer, this flag indicates whether the changer supports the supports the SEND VOLUME TAG SCSI SCSI command with a send action code of TRANSLATE.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_VOLUME_ASSERT"></span><span id="changer_volume_assert"></span>CHANGER\_VOLUME\_ASSERT
</dt> <dd>

The changer can verify volume information. For a SCSI changer, this flag indicates whether the changer supports the SEND VOLUME TAG SCSI command with a send action code of ASSERT.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_VOLUME_REPLACE"></span><span id="changer_volume_replace"></span>CHANGER\_VOLUME\_REPLACE
</dt> <dd>

The changer can replace volume information. For a SCSI changer, this flag indicates whether the changer supports the SEND VOLUME TAG SCSI command with a send action code of REPLACE.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_VOLUME_UNDEFINE"></span><span id="changer_volume_undefine"></span>CHANGER\_VOLUME\_UNDEFINE
</dt> <dd>

The changer can clear existing volume information. For a SCSI changer, this flag indicates whether the changer supports the supports the SEND VOLUME TAG SCSI command with a send action code of UNDEFINE.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_SERIAL_NUMBER_VALID"></span><span id="changer_serial_number_valid"></span>CHANGER\_SERIAL\_NUMBER\_VALID
</dt> <dd>

The serial number reported by GetProductData is valid and unique for all changers of this type. Serial numbers are not guaranteed to be unique across vendor and product lines. If the changer's serial number is unique according to this definition, the miniclass driver should set this flag and set SerialNumber in CHANGER\_PRODUCT\_DATA to the serial number.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_PREMOUNT_EJECT_REQUIRED"></span><span id="changer_premount_eject_required"></span>CHANGER\_PREMOUNT\_EJECT\_REQUIRED
</dt> <dd>

The changer requires an explicit command issued through a mass storage driver to eject a drive mechanism before the changer can move media from a slot to the drive. For example, a changer with CD-ROM drives might require the tray to be presented to the robotic transport so a piece of media could be loaded onto the tray during a mount operation. If the changer ejects the mechanism automatically, the miniclass driver should clear this flag.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_DEVICE_REINITIALIZE_CAPABLE"></span><span id="changer_device_reinitialize_capable"></span>CHANGER\_DEVICE\_REINITIALIZE\_CAPABLE
</dt> <dd>

The changer can recalibrate its transport element in response to an explicit command. The changer class driver calls **ChangerReinitializeUnit** to initiate recalibration.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_KEYPAD_ENABLE_DISABLE"></span><span id="changer_keypad_enable_disable"></span>CHANGER\_KEYPAD\_ENABLE\_DISABLE
</dt> <dd>

The changer keypad can be enabled and disabled programmatically.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_RESERVED_BIT"></span><span id="changer_reserved_bit"></span>CHANGER\_RESERVED\_BIT
</dt> <dd>

Reserved to indicate **Features1** flags.

</dd> </dl> </dd> <dt>

**Features1**
</dt> <dd>

Indicates additional features supported by the changer. This member can have one or more of the following values bitwise ORed together.

<dl> <dt>

<span id="CHANGER_PREDISMOUNT_ALIGN_TO_SLOT"></span><span id="changer_predismount_align_to_slot"></span>CHANGER\_PREDISMOUNT\_ALIGN\_TO\_SLOT
</dt> <dd>

Indicates that the transport must be moved to the destination slot before moving the media from a drive to the slot. The bit CHANGER\_PREDISMOUNT\_ALIGN\_TO\_DRIVE must be reset if this is set.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_PREDISMOUNT_ALIGN_TO_DRIVE"></span><span id="changer_predismount_align_to_drive"></span>CHANGER\_PREDISMOUNT\_ALIGN\_TO\_DRIVE
</dt> <dd>

Indicates that the transport must be moved to the drive before moving media from the drive to a slot. The bit CHANGER\_PREDISMOUNT\_ALIGN\_TO\_SLOT must be reset if this is set.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_CLEANER_AUTODISMOUNT"></span><span id="changer_cleaner_autodismount"></span>CHANGER\_CLEANER\_AUTODISMOUNT
</dt> <dd>

Indicates that the changer will move the cleaning cartridge back to its original slot automatically, after cleaning is finished. This bit can only be set if CHANGER\_DRIVE\_CLEANING\_REQUIRED is set and CHANGER\_CLEANER\_OPS\_NOT\_SUPPORTED is reset.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_TRUE_EXCHANGE_CAPABLE"></span><span id="changer_true_exchange_capable"></span>CHANGER\_TRUE\_EXCHANGE\_CAPABLE
</dt> <dd>

Device can manipulate two volumes at a time without using additional changer elements.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_SLOTS_USE_TRAYS"></span><span id="changer_slots_use_trays"></span>CHANGER\_SLOTS\_USE\_TRAYS
</dt> <dd>

The changer uses removable trays in its slots, which require the media to be placed in a tray and the tray moved to the desired position.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_RTN_MEDIA_TO_ORIGINAL_ADDR"></span><span id="changer_rtn_media_to_original_addr"></span>CHANGER\_RTN\_MEDIA\_TO\_ORIGINAL\_ADDR
</dt> <dd>

Indicates that when moving volume from drive to slot, volume must go back into the same slot from which it was previously moved to the drive.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_CLEANER_OPS_NOT_SUPPORTED"></span><span id="changer_cleaner_ops_not_supported"></span>CHANGER\_CLEANER\_OPS\_NOT\_SUPPORTED
</dt> <dd>

Indicates that the changer's transport cannot be programmatically commanded by software above the changer driver to move a cleaning cartridge to a dirty drive. This bit can be set only if the CHANGER\_DRIVE\_CLEANING\_REQUIRED bit is set. If this bit is set then both CHANGER\_CLEANER\_AUTODISMOUNT and CHANGER\_CLEANER\_SLOT must be reset.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_IEPORT_USER_CONTROL_OPEN"></span><span id="changer_ieport_user_control_open"></span>CHANGER\_IEPORT\_USER\_CONTROL\_OPEN
</dt> <dd>

The changer requires the user to manually open a closed IEport.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_IEPORT_USER_CONTROL_CLOSE"></span><span id="changer_ieport_user_control_close"></span>CHANGER\_IEPORT\_USER\_CONTROL\_CLOSE
</dt> <dd>

The changer requires the user to manually close an open IEport.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_MOVE_EXTENDS_IEPORT"></span><span id="changer_move_extends_ieport"></span>CHANGER\_MOVE\_EXTENDS\_IEPORT
</dt> <dd>

The changer will extend the tray automatically whenever a command is issued to move media to an IEport.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_MOVE_RETRACTS_IEPORT"></span><span id="changer_move_retracts_ieport"></span>CHANGER\_MOVE\_RETRACTS\_IEPORT
</dt> <dd>

The changer will retract the tray automatically whenever a command is issued to move media from an IEport.

</dd> </dl> </dd> <dt>

**MoveFromTransport**
</dt> <dd>

Indicates whether the changer supports moving a piece of media from a transport element to another transport element, a storage slot, an IEport, or a drive. For a SCSI changer, this is defined in the device capabilities page. The transport is not typically the source or destination for moving or exchanging media.

<dl> <dd>

Callers can use the following masks to determine whether the changer can move media to a given element.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_TO_TRANSPORT"></span><span id="changer_to_transport"></span>CHANGER\_TO\_TRANSPORT
</dt> <dd>

The changer can carry out the operation from the specified element to a transport.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_TO_SLOT"></span><span id="changer_to_slot"></span>CHANGER\_TO\_SLOT
</dt> <dd>

The changer can carry out the operation from the specified element to a storage slot.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_TO_IEPORT"></span><span id="changer_to_ieport"></span>CHANGER\_TO\_IEPORT
</dt> <dd>

The changer can carry out the operation from the specified element to an IEport.

</dd> </dl>

<dl> <dt>

<span id="CHANGER_TO_DRIVE"></span><span id="changer_to_drive"></span>CHANGER\_TO\_DRIVE
</dt> <dd>

The changer can carry out the operation from the specified element to a drive.

</dd> </dl> </dd> <dt>

**MoveFromSlot**
</dt> <dd>

Indicates whether the changer supports moving medium from a storage slot to a transport element, another storage slot, an IEport, or a drive. Callers can use the masks described under **MoveFromTransport** to determine whether the changer supports the move.

</dd> <dt>

**MoveFromIePort**
</dt> <dd>

Indicates whether the changer supports moving medium from an IEport to a transport element, a storage slot, another IEport, or a drive. For a SCSI changer, this is defined in the device capabilities page. Callers can use the masks described under **MoveFromTransport** to determine whether the changer supports the move

</dd> <dt>

**MoveFromDrive**
</dt> <dd>

Indicates whether the changer supports moving medium from a drive to a transport element, a storage slot, an IEport, or another drive. Callers can use the masks described under **MoveFromTransport** to determine whether the changer supports the move.

</dd> <dt>

**ExchangeFromTransport**
</dt> <dd>

Indicates whether the changer supports exchanging medium between a transport element and another transport element, a storage slot, an IEport, or a drive. Callers can use the masks described under **MoveFromTransport** to determine whether the changer supports the exchange.

</dd> <dt>

**ExchangeFromSlot**
</dt> <dd>

Indicates whether the changer supports exchanging medium between a storage slot and a transport element, another storage slot, an IEport, or a drive. Callers can use the masks described under **MoveFromTransport** to determine whether the changer supports the exchange.

</dd> <dt>

**ExchangeFromIePort**
</dt> <dd>

Indicates whether the changer supports exchanging medium between an IEport and a transport element, a storage slot, another IEport, or a drive. Callers can use the masks described under **MoveFromTransport** to determine whether the changer supports the exchange.

</dd> <dt>

**ExchangeFromDrive**
</dt> <dd>

Indicates whether the changer supports exchanging medium between a drive and a transport element, a storage slot, an IEport, or another drive. Callers can use the masks described under **MoveFromTransport** to determine whether the changer supports the exchange.

</dd> <dt>

**LockUnlockCapabilities**
</dt> <dd>

Indicates which elements of a changer can be locked or unlocked programmatically. This member is valid only if CHANGER\_LOCK\_UNLOCK is set in **Features0**.

Callers can use the following masks to determine whether the changer can lock or unlock a particular element.

<dl> <dt>

<span id="LOCK_UNLOCK_IEPORT"></span><span id="lock_unlock_ieport"></span>LOCK\_UNLOCK\_IEPORT
</dt> <dd>

The changer can lock or unlock its IEport(s).

</dd> <dt>

<span id="LOCK_UNLOCK_DOOR"></span><span id="lock_unlock_door"></span>LOCK\_UNLOCK\_DOOR
</dt> <dd>

The changer can lock or unlock its door.

</dd> <dt>

<span id="LOCK_UNLOCK_KEYPAD"></span><span id="lock_unlock_keypad"></span>LOCK\_UNLOCK\_KEYPAD
</dt> <dd>

The changer can lock or unlock its keypad.

</dd> </dl> </dd> <dt>

**PositionCapabilities**
</dt> <dd>

Indicates the elements to which a changer can position its transport. Callers can use the masks described under **MoveFromTransport** to determine whether the changer supports positioning the transport to a particular element. This member is valid only if CHANGER\_POSITION\_TO\_ELEMENT is set in **Features0**.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Remarks

**GET\_CHANGER\_PARAMETERS** contains the parameters of a changer. The changer miniclass driver allocates and fills in this structure when requested by the changer class driver.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**ChangerGetParameters**](changergetparameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GET_CHANGER_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






