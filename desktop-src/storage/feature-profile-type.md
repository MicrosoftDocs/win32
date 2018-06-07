---
title: FEATURE\_PROFILE\_TYPE enumeration
description: The FEATURE\_PROFILE\_TYPE enumeration provides a list of the profile names that are defined by the SCSI Multimedia - 4 (MMC-4) specification.
ms.assetid: 60cce78f-1025-41a7-861d-150ef28376cb
keywords:
- FEATURE_PROFILE_TYPE enumeration Storage Devices
- PFEATURE_PROFILE_TYPE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_PROFILE_TYPE
api_location:
- ntddmmc.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# FEATURE\_PROFILE\_TYPE enumeration

The FEATURE\_PROFILE\_TYPE enumeration provides a list of the profile names that are defined by the *SCSI Multimedia - 4 (MMC-4)* specification.

## Syntax


```C++
typedef enum _FEATURE_PROFILE_TYPE { 
  ProfileInvalid                = 0x0000,
  ProfileNonRemovableDisk       = 0x0001,
  ProfileRemovableDisk          = 0x0002,
  ProfileMOErasable             = 0x0003,
  ProfileMOWriteOnce            = 0x0004,
  ProfileAS_MO                  = 0x0005,
  ProfileCdrom                  = 0x0008,
  ProfileCdRecordable           = 0x0009,
  ProfileCdRewritable           = 0x000a,
  ProfileDvdRom                 = 0x0010,
  ProfileDvdRecordable          = 0x0011,
  ProfileDvdRam                 = 0x0012,
  ProfileDvdRewritable          = 0x0013,
  ProfileDvdRWSequential        = 0x0014,
  ProfileDvdDashRDualLayer      = 0x0015,
  ProfileDvdDashRLayerJump      = 0x0016,
  ProfileDvdPlusRW              = 0x001A,
  ProfileDvdPlusR               = 0x001B,
  ProfileDDCdrom                = 0x0020,
  ProfileDDCdRecordable         = 0x0021,
  ProfileDDCdRewritable         = 0x0022,
  ProfileDvdPlusRWDualLayer     = 0x002A,
  ProfileDvdPlusRDualLayer      = 0x002B,
  ProfileBDRom                  = 0x0040,
  ProfileBDRSequentialWritable  = 0x0041,
  ProfileBDRRandomWritable      = 0x0042,
  ProfileBDRewritable           = 0x0043,
  ProfileHDDVDRom               = 0x0050,
  ProfileHDDVDRecordable        = 0x0051,
  ProfileHDDVDRam               = 0x0052,
  ProfileHDDVDRewritable        = 0x0053,
  ProfileHDDVDRDualLayer        = 0x0058,
  ProfileHDDVDRWDualLayer       = 0x005A,
  ProfileNonStandard            = 0xffff
} FEATURE_PROFILE_TYPE, *PFEATURE_PROFILE_TYPE;
```



## Constants

<dl> <dt>

<span id="ProfileInvalid"></span><span id="profileinvalid"></span><span id="PROFILEINVALID"></span>**ProfileInvalid**
</dt> <dd>

Does not indicate a valid profile.

</dd> <dt>

<span id="ProfileNonRemovableDisk"></span><span id="profilenonremovabledisk"></span><span id="PROFILENONREMOVABLEDISK"></span>**ProfileNonRemovableDisk**
</dt> <dd>

Indicates the profile named "Nonremovable disk" by the *SCSI-3 Multimedia (MMC-3)* specification. This profile is used with devices that manage rewritable media and are capable of changing behavior.

</dd> <dt>

<span id="ProfileRemovableDisk"></span><span id="profileremovabledisk"></span><span id="PROFILEREMOVABLEDISK"></span>**ProfileRemovableDisk**
</dt> <dd>

Indicates the profile named "Removable disk" by the *MMC-3* specification. This profile is used with devices that manage rewritable, removable media.

</dd> <dt>

<span id="ProfileMOErasable"></span><span id="profilemoerasable"></span><span id="PROFILEMOERASABLE"></span>**ProfileMOErasable**
</dt> <dd>

Indicates the profile named "MO Erasable" by the *MMC-3* specification. This profile is used with devices that manage magneto-optical media and that have a sector-erase capability.

</dd> <dt>

<span id="ProfileMOWriteOnce"></span><span id="profilemowriteonce"></span><span id="PROFILEMOWRITEONCE"></span>**ProfileMOWriteOnce**
</dt> <dd>

Indicates the profile named "MO Write Once" by the *MMC-3* specification. This profile is used with devices that manage magneto-optical write-once media.

</dd> <dt>

<span id="ProfileAS_MO"></span><span id="profileas_mo"></span><span id="PROFILEAS_MO"></span>**ProfileAS\_MO**
</dt> <dd>

Indicates the profile named "AS-MO" by the *MMC-3* specification. This profile is used with devices that implement Advance Storage technology and manage magneto-optical media.

</dd> <dt>

<span id="ProfileCdrom"></span><span id="profilecdrom"></span><span id="PROFILECDROM"></span>**ProfileCdrom**
</dt> <dd>

Indicates the profile named "CD-ROM" by the *MMC-3* specification. This profile is used with devices that manage read-only compact disc media.

</dd> <dt>

<span id="ProfileCdRecordable"></span><span id="profilecdrecordable"></span><span id="PROFILECDRECORDABLE"></span>**ProfileCdRecordable**
</dt> <dd>

Indicates the profile named "CD-R" by the *MMC-3* specification. This profile is used with devices that manage write-once compact disc media.

</dd> <dt>

<span id="ProfileCdRewritable"></span><span id="profilecdrewritable"></span><span id="PROFILECDREWRITABLE"></span>**ProfileCdRewritable**
</dt> <dd>

Indicates the profile named "CD-RW" by the *MMC-3* specification. This profile is used with devices that manage rewritable compact disc media.

</dd> <dt>

<span id="ProfileDvdRom"></span><span id="profiledvdrom"></span><span id="PROFILEDVDROM"></span>**ProfileDvdRom**
</dt> <dd>

Indicates the profile named "DVD-ROM" by the *MMC-3* specification. This profile is used with devices that manage read-only DVD media.

</dd> <dt>

<span id="ProfileDvdRecordable"></span><span id="profiledvdrecordable"></span><span id="PROFILEDVDRECORDABLE"></span>**ProfileDvdRecordable**
</dt> <dd>

Indicates the profile named "DVD-R" by the *MMC-3* specification. This profile is used with devices that manage write-once DVD media and operate in sequential recording mode.

</dd> <dt>

<span id="ProfileDvdRam"></span><span id="profiledvdram"></span><span id="PROFILEDVDRAM"></span>**ProfileDvdRam**
</dt> <dd>

Indicates the profile named "DVD-RAM or DVD+RW" by the *MMC-3* specification. This profile is used with devices that manage rewritable DVD media.

</dd> <dt>

<span id="ProfileDvdRewritable"></span><span id="profiledvdrewritable"></span><span id="PROFILEDVDREWRITABLE"></span>**ProfileDvdRewritable**
</dt> <dd>

Indicates the profile named "DVD-RW Restricted Overwrite" by the *MMC-3* specification. This profile is used with devices that manage rerecordable DVD media and operate in packet-writing mode.

</dd> <dt>

<span id="ProfileDvdRWSequential"></span><span id="profiledvdrwsequential"></span><span id="PROFILEDVDRWSEQUENTIAL"></span>**ProfileDvdRWSequential**
</dt> <dd>

Indicates the profile named "DVD-RW Sequential Recording" by the *MMC-3* specification. This profile is used with devices that implement a series of features associated with sequential recording, such as the features "Incremental Streaming Writable" and "Real-Time Streaming". For a full list of the features supported with this profile, see the *MMC-3* specification.

</dd> <dt>

<span id="ProfileDvdDashRDualLayer"></span><span id="profiledvddashrduallayer"></span><span id="PROFILEDVDDASHRDUALLAYER"></span>**ProfileDvdDashRDualLayer**
</dt> <dd></dd> <dt>

<span id="ProfileDvdDashRLayerJump"></span><span id="profiledvddashrlayerjump"></span><span id="PROFILEDVDDASHRLAYERJUMP"></span>**ProfileDvdDashRLayerJump**
</dt> <dd>

Reserved 0x0017 - 0x0019

</dd> <dt>

<span id="ProfileDvdPlusRW"></span><span id="profiledvdplusrw"></span><span id="PROFILEDVDPLUSRW"></span>**ProfileDvdPlusRW**
</dt> <dd>

Indicates the profile named "DVD+RW" by the *MMC-3* specification. This profile is used with devices that implement a series of features required to manage DVD media that is both readable and writable. For a full list of the features supported with this profile, see the *MMC-3* specification.

</dd> <dt>

<span id="ProfileDvdPlusR"></span><span id="profiledvdplusr"></span><span id="PROFILEDVDPLUSR"></span>**ProfileDvdPlusR**
</dt> <dd>

Reserved 0x001C - 001F

</dd> <dt>

<span id="ProfileDDCdrom"></span><span id="profileddcdrom"></span><span id="PROFILEDDCDROM"></span>**ProfileDDCdrom**
</dt> <dd>

Indicates the profile named "DDCD-ROM" by the *MMC-3* specification. This profile is used with devices that can read "DDCD specific structure." For a full list of the features supported with this profile, see the *MMC-3* specification.

</dd> <dt>

<span id="ProfileDDCdRecordable"></span><span id="profileddcdrecordable"></span><span id="PROFILEDDCDRECORDABLE"></span>**ProfileDDCdRecordable**
</dt> <dd>

Indicates the profile named "DDCD-R" by the *MMC-3* specification. This profile is used with devices that can read "DDCD-R specific structure." For a full list of the features supported with this profile, see the *MMC-3* specification.

</dd> <dt>

<span id="ProfileDDCdRewritable"></span><span id="profileddcdrewritable"></span><span id="PROFILEDDCDREWRITABLE"></span>**ProfileDDCdRewritable**
</dt> <dd>

Indicates the profile named "DDCD-RW" by the *MMC-3* specification. This profile is used with devices that can read "DDCD-RW specific structure." For a full list of the features supported with this profile, see the *MMC-3* specification.

</dd> <dt>

<span id="ProfileDvdPlusRWDualLayer"></span><span id="profiledvdplusrwduallayer"></span><span id="PROFILEDVDPLUSRWDUALLAYER"></span>**ProfileDvdPlusRWDualLayer**
</dt> <dd></dd> <dt>

<span id="ProfileDvdPlusRDualLayer"></span><span id="profiledvdplusrduallayer"></span><span id="PROFILEDVDPLUSRDUALLAYER"></span>**ProfileDvdPlusRDualLayer**
</dt> <dd>

Reserved 0x002C - 0x003F

</dd> <dt>

<span id="ProfileBDRom"></span><span id="profilebdrom"></span><span id="PROFILEBDROM"></span>**ProfileBDRom**
</dt> <dd></dd> <dt>

<span id="ProfileBDRSequentialWritable"></span><span id="profilebdrsequentialwritable"></span><span id="PROFILEBDRSEQUENTIALWRITABLE"></span>**ProfileBDRSequentialWritable**
</dt> <dd>

BD-R 'SRM'

</dd> <dt>

<span id="ProfileBDRRandomWritable"></span><span id="profilebdrrandomwritable"></span><span id="PROFILEBDRRANDOMWRITABLE"></span>**ProfileBDRRandomWritable**
</dt> <dd>

BD-R 'RRM'

</dd> <dt>

<span id="ProfileBDRewritable"></span><span id="profilebdrewritable"></span><span id="PROFILEBDREWRITABLE"></span>**ProfileBDRewritable**
</dt> <dd>

Reserved 0x0044 - 0x004F

</dd> <dt>

<span id="ProfileHDDVDRom"></span><span id="profilehddvdrom"></span><span id="PROFILEHDDVDROM"></span>**ProfileHDDVDRom**
</dt> <dd></dd> <dt>

<span id="ProfileHDDVDRecordable"></span><span id="profilehddvdrecordable"></span><span id="PROFILEHDDVDRECORDABLE"></span>**ProfileHDDVDRecordable**
</dt> <dd></dd> <dt>

<span id="ProfileHDDVDRam"></span><span id="profilehddvdram"></span><span id="PROFILEHDDVDRAM"></span>**ProfileHDDVDRam**
</dt> <dd></dd> <dt>

<span id="ProfileHDDVDRewritable"></span><span id="profilehddvdrewritable"></span><span id="PROFILEHDDVDREWRITABLE"></span>**ProfileHDDVDRewritable**
</dt> <dd>

Reserved 0x0054 - 0x0057

</dd> <dt>

<span id="ProfileHDDVDRDualLayer"></span><span id="profilehddvdrduallayer"></span><span id="PROFILEHDDVDRDUALLAYER"></span>**ProfileHDDVDRDualLayer**
</dt> <dd>

Reserved 0x0059 - 0x0059

</dd> <dt>

<span id="ProfileHDDVDRWDualLayer"></span><span id="profilehddvdrwduallayer"></span><span id="PROFILEHDDVDRWDUALLAYER"></span>**ProfileHDDVDRWDualLayer**
</dt> <dd>

Reserved 0x005B - 0xfffe

</dd> <dt>

<span id="ProfileNonStandard"></span><span id="profilenonstandard"></span><span id="PROFILENONSTANDARD"></span>**ProfileNonStandard**
</dt> <dd>

Indicates that the device does not conform to any profile.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_DATA\_PROFILE\_LIST**](feature-data-profile-list.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_PROFILE_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






