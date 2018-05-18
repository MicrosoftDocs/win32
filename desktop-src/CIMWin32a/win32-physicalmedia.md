---
title: Win32\_PhysicalMedia class
description: The Win32\_PhysicalMedia class represents any type of documentation or storage medium, such as tapes, CD ROMs, and so on.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f5d337ae-e948-42c0-9d86-236c42964a50'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Win32_PhysicalMedia class", "Win32_PhysicalMedia class, described"]
topic_type:
- apiref
api_name:
- Win32_PhysicalMedia
- Win32_PhysicalMedia.Caption
- Win32_PhysicalMedia.Description
- Win32_PhysicalMedia.InstallDate
- Win32_PhysicalMedia.Name
- Win32_PhysicalMedia.Status
- Win32_PhysicalMedia.CreationClassName
- Win32_PhysicalMedia.Manufacturer
- Win32_PhysicalMedia.Model
- Win32_PhysicalMedia.SKU
- Win32_PhysicalMedia.SerialNumber
- Win32_PhysicalMedia.Tag
- Win32_PhysicalMedia.Version
- Win32_PhysicalMedia.PartNumber
- Win32_PhysicalMedia.OtherIdentifyingInfo
- Win32_PhysicalMedia.PoweredOn
- Win32_PhysicalMedia.Removable
- Win32_PhysicalMedia.Replaceable
- Win32_PhysicalMedia.HotSwappable
- Win32_PhysicalMedia.Capacity
- Win32_PhysicalMedia.MediaType
- Win32_PhysicalMedia.MediaDescription
- Win32_PhysicalMedia.WriteProtectOn
- Win32_PhysicalMedia.CleanerMedia
api_location:
- Wmipcima.dll
api_type:
- DllExport
---

# Win32\_PhysicalMedia class

The **Win32\_PhysicalMedia** class represents any type of documentation or storage medium, such as tapes, CD ROMs, and so on. To obtain the characteristics of the media in a CD drive, such as whether it is writeable, use [**Win32\_CDROMDrive**](https://msdn.microsoft.com/library/aa394081) and the **Capabilities** property.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32a"), UUID("{BF253431-1E4D-4F57-00E7-64B2CACC801E}"), AMENDMENT]
class Win32_PhysicalMedia : CIM_PhysicalMedia
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  string   CreationClassName;
  string   Manufacturer;
  string   Model;
  string   SKU;
  string   SerialNumber = NULL;
  string   Tag = NULL;
  string   Version;
  string   PartNumber;
  string   OtherIdentifyingInfo;
  boolean  PoweredOn;
  boolean  Removable;
  boolean  Replaceable;
  boolean  HotSwappable;
  uint64   Capacity;
  uint16   MediaType;
  string   MediaDescription;
  boolean  WriteProtectOn;
  boolean  CleanerMedia;
};
```

## Members

The **Win32\_PhysicalMedia** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PhysicalMedia** class has these properties.

<dl> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("bytes")
</dt> </dl>

Number of bytes that can be read from or written to this physical media component. This property does not apply to "Hard Copy" or cleaner media. Data compression should not be assumed as it would increase the value of this property. For tapes, it should be assumed that no filemarks or blank space areas are recorded on the media.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short, one-line textual description of the object.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**CleanerMedia**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the physical media is used for cleaning purposes and not data storage.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with other key properties of this class, **CreationClassName** allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the object.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**HotSwappable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this physical media component can be replaced with a physically different but equivalent one while the containing package has the power applied. For example, a fan component may be designed to be hot-swapped. All components that can be hot-swapped are inherently removable and replaceable.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When the object was installed. This property does not require a value to indicate that the object is installed.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the organization responsible for producing the physical element. This can be the entity from whom the element is purchased, but this is not necessarily the case as this information is contained in the **Vendor** property.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**MediaDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalMedia.MediaType")
</dt> </dl>

Additional detail related to the **MediaType** property. For example, if **MediaType** has the value 3 (QIC Cartridge) the **MediaDescription** property can indicate whether the tape is wide or quarter inch.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**MediaType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalMedia.MediaDescription")
</dt> </dl>

The type of the media, as an enumerated integer. The **MediaDescription** property provides a more explicit definition of the media type.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

The following list lists the possible values.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="Tape_Cartridge"></span><span id="tape_cartridge"></span><span id="TAPE_CARTRIDGE"></span>

<span id="Tape_Cartridge"></span><span id="tape_cartridge"></span><span id="TAPE_CARTRIDGE"></span>**Tape Cartridge** (2)


</dt> <dd></dd> <dt>

<span id="QIC_Cartridge"></span><span id="qic_cartridge"></span><span id="QIC_CARTRIDGE"></span>

<span id="QIC_Cartridge"></span><span id="qic_cartridge"></span><span id="QIC_CARTRIDGE"></span>**QIC Cartridge** (3)


</dt> <dd></dd> <dt>

<span id="AIT_Cartridge"></span><span id="ait_cartridge"></span><span id="AIT_CARTRIDGE"></span>

<span id="AIT_Cartridge"></span><span id="ait_cartridge"></span><span id="AIT_CARTRIDGE"></span>**AIT Cartridge** (4)


</dt> <dd></dd> <dt>

<span id="DTF_Cartridge"></span><span id="dtf_cartridge"></span><span id="DTF_CARTRIDGE"></span>

<span id="DTF_Cartridge"></span><span id="dtf_cartridge"></span><span id="DTF_CARTRIDGE"></span>**DTF Cartridge** (5)


</dt> <dd></dd> <dt>

<span id="DAT_Cartridge"></span><span id="dat_cartridge"></span><span id="DAT_CARTRIDGE"></span>

<span id="DAT_Cartridge"></span><span id="dat_cartridge"></span><span id="DAT_CARTRIDGE"></span>**DAT Cartridge** (6)


</dt> <dd></dd> <dt>

<span id="8mm_Tape_Cartridge"></span><span id="8mm_tape_cartridge"></span><span id="8MM_TAPE_CARTRIDGE"></span>

<span id="8mm_Tape_Cartridge"></span><span id="8mm_tape_cartridge"></span><span id="8MM_TAPE_CARTRIDGE"></span>**8mm Tape Cartridge** (7)


</dt> <dd></dd> <dt>

<span id="19mm_Tape_Cartridge"></span><span id="19mm_tape_cartridge"></span><span id="19MM_TAPE_CARTRIDGE"></span>

<span id="19mm_Tape_Cartridge"></span><span id="19mm_tape_cartridge"></span><span id="19MM_TAPE_CARTRIDGE"></span>**19mm Tape Cartridge** (8)


</dt> <dd></dd> <dt>

<span id="DLT_Cartridge"></span><span id="dlt_cartridge"></span><span id="DLT_CARTRIDGE"></span>

<span id="DLT_Cartridge"></span><span id="dlt_cartridge"></span><span id="DLT_CARTRIDGE"></span>**DLT Cartridge** (9)


</dt> <dd></dd> <dt>

<span id="Half-Inch_Magnetic_Tape_Cartridge"></span><span id="half-inch_magnetic_tape_cartridge"></span><span id="HALF-INCH_MAGNETIC_TAPE_CARTRIDGE"></span>

<span id="Half-Inch_Magnetic_Tape_Cartridge"></span><span id="half-inch_magnetic_tape_cartridge"></span><span id="HALF-INCH_MAGNETIC_TAPE_CARTRIDGE"></span>**Half-Inch Magnetic Tape Cartridge** (10)


</dt> <dd></dd> <dt>

<span id="Cartridge_Disk"></span><span id="cartridge_disk"></span><span id="CARTRIDGE_DISK"></span>

<span id="Cartridge_Disk"></span><span id="cartridge_disk"></span><span id="CARTRIDGE_DISK"></span>**Cartridge Disk** (11)


</dt> <dd></dd> <dt>

<span id="JAZ_Disk"></span><span id="jaz_disk"></span><span id="JAZ_DISK"></span>

<span id="JAZ_Disk"></span><span id="jaz_disk"></span><span id="JAZ_DISK"></span>**JAZ Disk** (12)


</dt> <dd></dd> <dt>

<span id="ZIP_Disk"></span><span id="zip_disk"></span><span id="ZIP_DISK"></span>

<span id="ZIP_Disk"></span><span id="zip_disk"></span><span id="ZIP_DISK"></span>**ZIP Disk** (13)


</dt> <dd></dd> <dt>

<span id="SyQuest_Disk"></span><span id="syquest_disk"></span><span id="SYQUEST_DISK"></span>

<span id="SyQuest_Disk"></span><span id="syquest_disk"></span><span id="SYQUEST_DISK"></span>**SyQuest Disk** (14)


</dt> <dd></dd> <dt>

<span id="Winchester_Removable_Disk"></span><span id="winchester_removable_disk"></span><span id="WINCHESTER_REMOVABLE_DISK"></span>

<span id="Winchester_Removable_Disk"></span><span id="winchester_removable_disk"></span><span id="WINCHESTER_REMOVABLE_DISK"></span>**Winchester Removable Disk** (15)


</dt> <dd></dd> <dt>

<span id="CD-ROM"></span><span id="cd-rom"></span>

<span id="CD-ROM"></span><span id="cd-rom"></span>**CD-ROM** (16)


</dt> <dd>

CD ROM

</dd> <dt>

<span id="CD-ROM_XA"></span><span id="cd-rom_xa"></span>

<span id="CD-ROM_XA"></span><span id="cd-rom_xa"></span>**CD-ROM/XA** (17)


</dt> <dd>

CD ROM/XA

</dd> <dt>

<span id="CD-I"></span><span id="cd-i"></span>

<span id="CD-I"></span><span id="cd-i"></span>**CD-I** (18)


</dt> <dd></dd> <dt>

<span id="CD_Recordable"></span><span id="cd_recordable"></span><span id="CD_RECORDABLE"></span>

<span id="CD_Recordable"></span><span id="cd_recordable"></span><span id="CD_RECORDABLE"></span>**CD Recordable** (19)


</dt> <dd></dd> <dt>

<span id="WORM"></span><span id="worm"></span>

<span id="WORM"></span><span id="worm"></span>**WORM** (20)


</dt> <dd></dd> <dt>

<span id="Magneto-Optical"></span><span id="magneto-optical"></span><span id="MAGNETO-OPTICAL"></span>

<span id="Magneto-Optical"></span><span id="magneto-optical"></span><span id="MAGNETO-OPTICAL"></span>**Magneto-Optical** (21)


</dt> <dd></dd> <dt>

<span id="DVD"></span><span id="dvd"></span>

<span id="DVD"></span><span id="dvd"></span>**DVD** (22)


</dt> <dd></dd> <dt>

<span id="DVD_RW"></span><span id="dvd_rw"></span>

<span id="DVD_RW"></span><span id="dvd_rw"></span>**DVD+RW** (23)


</dt> <dd></dd> <dt>

<span id="DVD-RAM"></span><span id="dvd-ram"></span>

<span id="DVD-RAM"></span><span id="dvd-ram"></span>**DVD-RAM** (24)


</dt> <dd></dd> <dt>

<span id="DVD-ROM"></span><span id="dvd-rom"></span>

<span id="DVD-ROM"></span><span id="dvd-rom"></span>**DVD-ROM** (25)


</dt> <dd></dd> <dt>

<span id="DVD-Video"></span><span id="dvd-video"></span><span id="DVD-VIDEO"></span>

<span id="DVD-Video"></span><span id="dvd-video"></span><span id="DVD-VIDEO"></span>**DVD-Video** (26)


</dt> <dd></dd> <dt>

<span id="Divx"></span><span id="divx"></span><span id="DIVX"></span>

<span id="Divx"></span><span id="divx"></span><span id="DIVX"></span>**Divx** (27)


</dt> <dd></dd> <dt>

<span id="Floppy_Diskette"></span><span id="floppy_diskette"></span><span id="FLOPPY_DISKETTE"></span>

<span id="Floppy_Diskette"></span><span id="floppy_diskette"></span><span id="FLOPPY_DISKETTE"></span>**Floppy/Diskette** (28)


</dt> <dd></dd> <dt>

<span id="Hard_Disk"></span><span id="hard_disk"></span><span id="HARD_DISK"></span>

<span id="Hard_Disk"></span><span id="hard_disk"></span><span id="HARD_DISK"></span>**Hard Disk** (29)


</dt> <dd></dd> <dt>

<span id="Memory_Card"></span><span id="memory_card"></span><span id="MEMORY_CARD"></span>

<span id="Memory_Card"></span><span id="memory_card"></span><span id="MEMORY_CARD"></span>**Memory Card** (30)


</dt> <dd></dd> <dt>

<span id="Hard_Copy"></span><span id="hard_copy"></span><span id="HARD_COPY"></span>

<span id="Hard_Copy"></span><span id="hard_copy"></span><span id="HARD_COPY"></span>**Hard Copy** (31)


</dt> <dd></dd> <dt>

<span id="Clik_Disk"></span><span id="clik_disk"></span><span id="CLIK_DISK"></span>

<span id="Clik_Disk"></span><span id="clik_disk"></span><span id="CLIK_DISK"></span>**Clik Disk** (32)


</dt> <dd></dd> <dt>

<span id="CD-RW"></span><span id="cd-rw"></span>

<span id="CD-RW"></span><span id="cd-rw"></span>**CD-RW** (33)


</dt> <dd></dd> <dt>

<span id="CD-DA"></span><span id="cd-da"></span>

<span id="CD-DA"></span><span id="cd-da"></span>**CD-DA** (34)


</dt> <dd></dd> <dt>

<span id="CD_"></span><span id="cd_"></span>

<span id="CD_"></span><span id="cd_"></span>**CD+** (35)


</dt> <dd></dd> <dt>

<span id="DVD_Recordable"></span><span id="dvd_recordable"></span><span id="DVD_RECORDABLE"></span>

<span id="DVD_Recordable"></span><span id="dvd_recordable"></span><span id="DVD_RECORDABLE"></span>**DVD Recordable** (36)


</dt> <dd></dd> <dt>

<span id="DVD-RW"></span><span id="dvd-rw"></span>

<span id="DVD-RW"></span><span id="dvd-rw"></span>**DVD-RW** (37)


</dt> <dd></dd> <dt>

<span id="DVD-Audio"></span><span id="dvd-audio"></span><span id="DVD-AUDIO"></span>

<span id="DVD-Audio"></span><span id="dvd-audio"></span><span id="DVD-AUDIO"></span>**DVD-Audio** (38)


</dt> <dd></dd> <dt>

<span id="DVD-5"></span><span id="dvd-5"></span>

<span id="DVD-5"></span><span id="dvd-5"></span>**DVD-5** (39)


</dt> <dd></dd> <dt>

<span id="DVD-9"></span><span id="dvd-9"></span>

<span id="DVD-9"></span><span id="dvd-9"></span>**DVD-9** (40)


</dt> <dd></dd> <dt>

<span id="DVD-10"></span><span id="dvd-10"></span>

<span id="DVD-10"></span><span id="dvd-10"></span>**DVD-10** (41)


</dt> <dd></dd> <dt>

<span id="DVD-18"></span><span id="dvd-18"></span>

<span id="DVD-18"></span><span id="dvd-18"></span>**DVD-18** (42)


</dt> <dd></dd> <dt>

<span id="Magneto-Optical_Rewriteable"></span><span id="magneto-optical_rewriteable"></span><span id="MAGNETO-OPTICAL_REWRITEABLE"></span>

<span id="Magneto-Optical_Rewriteable"></span><span id="magneto-optical_rewriteable"></span><span id="MAGNETO-OPTICAL_REWRITEABLE"></span>**Magneto-Optical Rewriteable** (43)


</dt> <dd></dd> <dt>

<span id="Magneto-Optical_Write_Once"></span><span id="magneto-optical_write_once"></span><span id="MAGNETO-OPTICAL_WRITE_ONCE"></span>

<span id="Magneto-Optical_Write_Once"></span><span id="magneto-optical_write_once"></span><span id="MAGNETO-OPTICAL_WRITE_ONCE"></span>**Magneto-Optical Write Once** (44)


</dt> <dd></dd> <dt>

<span id="Magneto-Optical_Rewriteable__LIMDOW_"></span><span id="magneto-optical_rewriteable__limdow_"></span><span id="MAGNETO-OPTICAL_REWRITEABLE__LIMDOW_"></span>

<span id="Magneto-Optical_Rewriteable__LIMDOW_"></span><span id="magneto-optical_rewriteable__limdow_"></span><span id="MAGNETO-OPTICAL_REWRITEABLE__LIMDOW_"></span>**Magneto-Optical Rewriteable (LIMDOW)** (45)


</dt> <dd></dd> <dt>

<span id="Phase_Change_Write_Once"></span><span id="phase_change_write_once"></span><span id="PHASE_CHANGE_WRITE_ONCE"></span>

<span id="Phase_Change_Write_Once"></span><span id="phase_change_write_once"></span><span id="PHASE_CHANGE_WRITE_ONCE"></span>**Phase Change Write Once** (46)


</dt> <dd></dd> <dt>

<span id="Phase_Change_Rewriteable"></span><span id="phase_change_rewriteable"></span><span id="PHASE_CHANGE_REWRITEABLE"></span>

<span id="Phase_Change_Rewriteable"></span><span id="phase_change_rewriteable"></span><span id="PHASE_CHANGE_REWRITEABLE"></span>**Phase Change Rewriteable** (47)


</dt> <dd></dd> <dt>

<span id="Phase_Change_Dual_Rewriteable"></span><span id="phase_change_dual_rewriteable"></span><span id="PHASE_CHANGE_DUAL_REWRITEABLE"></span>

<span id="Phase_Change_Dual_Rewriteable"></span><span id="phase_change_dual_rewriteable"></span><span id="PHASE_CHANGE_DUAL_REWRITEABLE"></span>**Phase Change Dual Rewriteable** (48)


</dt> <dd></dd> <dt>

<span id="Ablative_Write_Once"></span><span id="ablative_write_once"></span><span id="ABLATIVE_WRITE_ONCE"></span>

<span id="Ablative_Write_Once"></span><span id="ablative_write_once"></span><span id="ABLATIVE_WRITE_ONCE"></span>**Ablative Write Once** (49)


</dt> <dd></dd> <dt>

<span id="Near_Field_Recording"></span><span id="near_field_recording"></span><span id="NEAR_FIELD_RECORDING"></span>

<span id="Near_Field_Recording"></span><span id="near_field_recording"></span><span id="NEAR_FIELD_RECORDING"></span>**Near Field Recording** (50)


</dt> <dd></dd> <dt>

<span id="MiniQic"></span><span id="miniqic"></span><span id="MINIQIC"></span>

<span id="MiniQic"></span><span id="miniqic"></span><span id="MINIQIC"></span>**MiniQic** (51)


</dt> <dd></dd> <dt>

<span id="Travan"></span><span id="travan"></span><span id="TRAVAN"></span>

<span id="Travan"></span><span id="travan"></span><span id="TRAVAN"></span>**Travan** (52)


</dt> <dd></dd> <dt>

<span id="8mm_Metal_Particle"></span><span id="8mm_metal_particle"></span><span id="8MM_METAL_PARTICLE"></span>

<span id="8mm_Metal_Particle"></span><span id="8mm_metal_particle"></span><span id="8MM_METAL_PARTICLE"></span>**8mm Metal Particle** (53)


</dt> <dd></dd> <dt>

<span id="8mm_Advanced_Metal_Evaporate"></span><span id="8mm_advanced_metal_evaporate"></span><span id="8MM_ADVANCED_METAL_EVAPORATE"></span>

<span id="8mm_Advanced_Metal_Evaporate"></span><span id="8mm_advanced_metal_evaporate"></span><span id="8MM_ADVANCED_METAL_EVAPORATE"></span>**8mm Advanced Metal Evaporate** (54)


</dt> <dd></dd> <dt>

<span id="NCTP"></span><span id="nctp"></span>

<span id="NCTP"></span><span id="nctp"></span>**NCTP** (55)


</dt> <dd></dd> <dt>

<span id="LTO_Ultrium"></span><span id="lto_ultrium"></span><span id="LTO_ULTRIUM"></span>

<span id="LTO_Ultrium"></span><span id="lto_ultrium"></span><span id="LTO_ULTRIUM"></span>**LTO Ultrium** (56)


</dt> <dd></dd> <dt>

<span id="LTO_Accelis"></span><span id="lto_accelis"></span><span id="LTO_ACCELIS"></span>

<span id="LTO_Accelis"></span><span id="lto_accelis"></span><span id="LTO_ACCELIS"></span>**LTO Accelis** (57)


</dt> <dd></dd> <dt>

<span id="9_Track_Tape"></span><span id="9_track_tape"></span><span id="9_TRACK_TAPE"></span>

<span id="9_Track_Tape"></span><span id="9_track_tape"></span><span id="9_TRACK_TAPE"></span>**9 Track Tape** (58)


</dt> <dd></dd> <dt>

<span id="18_Track_Tape"></span><span id="18_track_tape"></span><span id="18_TRACK_TAPE"></span>

<span id="18_Track_Tape"></span><span id="18_track_tape"></span><span id="18_TRACK_TAPE"></span>**18 Track Tape** (59)


</dt> <dd></dd> <dt>

<span id="36_Track_Tape"></span><span id="36_track_tape"></span><span id="36_TRACK_TAPE"></span>

<span id="36_Track_Tape"></span><span id="36_track_tape"></span><span id="36_TRACK_TAPE"></span>**36 Track Tape** (60)


</dt> <dd></dd> <dt>

<span id="Magstar_3590"></span><span id="magstar_3590"></span><span id="MAGSTAR_3590"></span>

<span id="Magstar_3590"></span><span id="magstar_3590"></span><span id="MAGSTAR_3590"></span>**Magstar 3590** (61)


</dt> <dd></dd> <dt>

<span id="Magstar_MP"></span><span id="magstar_mp"></span><span id="MAGSTAR_MP"></span>

<span id="Magstar_MP"></span><span id="magstar_mp"></span><span id="MAGSTAR_MP"></span>**Magstar MP** (62)


</dt> <dd></dd> <dt>

<span id="D2_Tape"></span><span id="d2_tape"></span><span id="D2_TAPE"></span>

<span id="D2_Tape"></span><span id="d2_tape"></span><span id="D2_TAPE"></span>**D2 Tape** (63)


</dt> <dd></dd> <dt>

<span id="Tape_-_DST_Small"></span><span id="tape_-_dst_small"></span><span id="TAPE_-_DST_SMALL"></span>

<span id="Tape_-_DST_Small"></span><span id="tape_-_dst_small"></span><span id="TAPE_-_DST_SMALL"></span>**Tape - DST Small** (64)


</dt> <dd></dd> <dt>

<span id="Tape_-_DST_Medium"></span><span id="tape_-_dst_medium"></span><span id="TAPE_-_DST_MEDIUM"></span>

<span id="Tape_-_DST_Medium"></span><span id="tape_-_dst_medium"></span><span id="TAPE_-_DST_MEDIUM"></span>**Tape - DST Medium** (65)


</dt> <dd></dd> <dt>

<span id="Tape_-_DST_Large"></span><span id="tape_-_dst_large"></span><span id="TAPE_-_DST_LARGE"></span>

<span id="Tape_-_DST_Large"></span><span id="tape_-_dst_large"></span><span id="TAPE_-_DST_LARGE"></span>**Tape - DST Large** (66)


</dt> <dd></dd> </dl>

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name by which the physical element is generally known.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, the **Name** property can be overridden to be a [**Key**](https://msdn.microsoft.com/library/aa393650) property.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional data, beyond asset tag information, that can be used to identify a physical element. One example is bar code data associated with an element that also has an asset tag. Note that if only bar code data is available, is unique, and it can be used as an element key, this property is **NULL** and the bar code data used is the class key in the **Tag** property.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**PartNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Part number assigned by the manufacturer of the physical element.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**PoweredOn**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE** the physical element is powered on.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**Removable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the physical component is designed to be taken in and out of the physical container in which it is normally found, without impairing the function of the overall packaging. A component can still be removable if the power must be "off" to perform the removal. If power can be "on" and the component removed, the element is removable and can be hot-swapped.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**Replaceable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this physical media component can be replaced with a physically different one. For example, some computer systems allow the main processor chip to be upgraded to one of a higher clock rating. In this case, the processor is said to be replaceable. All removable components are inherently replaceable.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SerialNumber"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("")
</dt> </dl>

Manufacturer-allocated number used to identify the physical media. The default value is **NULL**.

Example: WD-WM3493798728

</dd> <dt>

**SKU**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Stock keeping unit number for this physical element.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses are "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates that an element may function properly at the present, but predicts a failure in the near future. For example, a SMART-enabled hard disk drive. Nonoperational statuses can also be specified. These are, "Error", "Starting", "Stopping," and "Service". The "Service" status applies to administrative work, such as mirror-resilvering of a disk or reload of a user permissions list. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

The values are:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> <dt>

**Tag**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Tag"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("")
</dt> </dl>

Uniquely identifies the physical media in the system.

Example: PHYSICALDRIVE0

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version of the physical element.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> <dt>

**WriteProtectOn**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the media is currently write protected by some kind of physical mechanism, such as a protect tab on a floppy disk.

This property is inherited from [**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PhysicalMedia**](https://msdn.microsoft.com/library/aa387967)
</dt> <dt>

[Computer System Hardware Classes](https://msdn.microsoft.com/library/aa389273)
</dt> </dl>

 

 





