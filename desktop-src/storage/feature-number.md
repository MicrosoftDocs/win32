---
title: FEATURE\_NUMBER enumeration
description: The FEATURE\_NUMBER enumeration provides a list of the features that are defined by the SCSI Multimedia - 4 (MMC-4) specification.
ms.assetid: 'f139da57-1527-476d-8e9f-0b96876adecf'
keywords: ["FEATURE_NUMBER enumeration Storage Devices", "PFEATURE_NUMBER enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- FEATURE_NUMBER
api_location:
- ntddmmc.h
api_type:
- HeaderDef
---

# FEATURE\_NUMBER enumeration

The FEATURE\_NUMBER enumeration provides a list of the features that are defined by the *SCSI Multimedia - 4 (MMC-4)* specification.

## Syntax


```C++
typedef enum _FEATURE_NUMBER { 
  FeatureProfileList                   = 0x0000,
  FeatureCore                          = 0x0001,
  FeatureMorphing                      = 0x0002,
  FeatureRemovableMedium               = 0x0003,
  FeatureWriteProtect                  = 0x0004,
  FeatureRandomReadable                = 0x0010,
  FeatureMultiRead                     = 0x001D,
  FeatureCdRead                        = 0x001E,
  FeatureDvdRead                       = 0x001F,
  FeatureRandomWritable                = 0x0020,
  FeatureIncrementalStreamingWritable  = 0x0021,
  FeatureSectorErasable                = 0x0022,
  FeatureFormattable                   = 0x0023,
  FeatureDefectManagement              = 0x0024,
  FeatureWriteOnce                     = 0x0025,
  FeatureRestrictedOverwrite           = 0x0026,
  FeatureCdrwCAVWrite                  = 0x0027,
  FeatureMrw                           = 0x0028,
  FeatureEnhancedDefectReporting       = 0x0029,
  FeatureDvdPlusRW                     = 0x002A,
  FeatureDvdPlusR                      = 0x002B,
  FeatureRigidRestrictedOverwrite      = 0x002C,
  FeatureCdTrackAtOnce                 = 0x002D,
  FeatureCdMastering                   = 0x002E,
  FeatureDvdRecordableWrite            = 0x002F,
  FeatureDDCDRead                      = 0x0030,
  FeatureDDCDRWrite                    = 0x0031,
  FeatureDDCDRWWrite                   = 0x0032,
  FeatureLayerJumpRecording            = 0x0033,
  FeatureCDRWMediaWriteSupport         = 0x0037,
  FeatureBDRPseudoOverwrite            = 0x0038,
  FeatureDvdPlusRWDualLayer            = 0x003A,
  FeatureDvdPlusRDualLayer             = 0x003B,
  FeatureBDRead                        = 0x0040,
  FeatureBDWrite                       = 0x0041,
  FeatureTSR                           = 0x0042,
  FeatureHDDVDRead                     = 0x0050,
  FeatureHDDVDWrite                    = 0x0051,
  FeatureHybridDisc                    = 0x0080,
  FeaturePowerManagement               = 0x0100,
  FeatureSMART                         = 0x0101,
  FeatureEmbeddedChanger               = 0x0102,
  FeatureCDAudioAnalogPlay             = 0x0103,
  FeatureMicrocodeUpgrade              = 0x0104,
  FeatureTimeout                       = 0x0105,
  FeatureDvdCSS                        = 0x0106,
  FeatureRealTimeStreaming             = 0x0107,
  FeatureLogicalUnitSerialNumber       = 0x0108,
  FeatureMediaSerialNumber             = 0x0109,
  FeatureDiscControlBlocks             = 0x010A,
  FeatureDvdCPRM                       = 0x010B,
  FeatureFirmwareDate                  = 0x010C,
  FeatureAACS                          = 0x010D,
  FeatureVCPS                          = 0x0110
} FEATURE_NUMBER, *PFEATURE_NUMBER;
```



## Constants

<dl> <dt>

<span id="FeatureProfileList"></span><span id="featureprofilelist"></span><span id="FEATUREPROFILELIST"></span>**FeatureProfileList**
</dt> <dd>

Indicates the feature named "Profile List" by the *MMC-3* specification. This feature provides a list of all profiles supported by the device.

</dd> <dt>

<span id="FeatureCore"></span><span id="featurecore"></span><span id="FEATURECORE"></span>**FeatureCore**
</dt> <dd>

Indicates the feature named "Core" by the *MMC-3* specification. This feature encompasses the basic functionality which is mandatory for all devices that support the *MMC-3* standard. See the *MMC-3* specification for a description of the capabilities included in the Core feature.

</dd> <dt>

<span id="FeatureMorphing"></span><span id="featuremorphing"></span><span id="FEATUREMORPHING"></span>**FeatureMorphing**
</dt> <dd>

Indicates the feature named "Morphing" by the *MMC-3* specification. Devices that support this feature can notify the initiator of operational changes and allow the initiator to prevent operational changes.

</dd> <dt>

<span id="FeatureRemovableMedium"></span><span id="featureremovablemedium"></span><span id="FEATUREREMOVABLEMEDIUM"></span>**FeatureRemovableMedium**
</dt> <dd>

Indicates the feature named "Removable Medium" by the *MMC-3* specification. Devices that support this feature allow the medium to be removed from the device. They also can communicate to the initiator that the user wants to eject the medium or has inserted a new medium.

</dd> <dt>

<span id="FeatureWriteProtect"></span><span id="featurewriteprotect"></span><span id="FEATUREWRITEPROTECT"></span>**FeatureWriteProtect**
</dt> <dd>

Indicates the feature named "Write Protect" by the *MMC-3* specification. Devices that support this feature allow the initiator to change the write-protection state of the media programmatically.

</dd> <dt>

<span id="FeatureRandomReadable"></span><span id="featurerandomreadable"></span><span id="FEATURERANDOMREADABLE"></span>**FeatureRandomReadable**
</dt> <dd>

Indicates the feature named "Random Readable" by the *MMC-3* specification. Devices that support this feature allow the initiator to read blocks of data on the disk at random locations. These devices do not require that the initiator address disk locations in any particular order.

</dd> <dt>

<span id="FeatureMultiRead"></span><span id="featuremultiread"></span><span id="FEATUREMULTIREAD"></span>**FeatureMultiRead**
</dt> <dd>

Indicates the feature named "MultiRead," originally defined by the Optical Storage Technology Association (OSTA) and incorporated into the *MMC-3* specification. Devices that support this feature can read all CD media types.

</dd> <dt>

<span id="FeatureCdRead"></span><span id="featurecdread"></span><span id="FEATURECDREAD"></span>**FeatureCdRead**
</dt> <dd>

Indicates the feature named "CD Read" by the *MMC-3* specification. Devices that support this feature can read CD-specific information from the media and can read user data from all types of CD blocks.

</dd> <dt>

<span id="FeatureDvdRead"></span><span id="featuredvdread"></span><span id="FEATUREDVDREAD"></span>**FeatureDvdRead**
</dt> <dd>

Indicates the feature named "DVD Read" by the *MMC-3* specification. Devices that support this feature can read DVD-specific information from the media.

</dd> <dt>

<span id="FeatureRandomWritable"></span><span id="featurerandomwritable"></span><span id="FEATURERANDOMWRITABLE"></span>**FeatureRandomWritable**
</dt> <dd>

Indicates the feature named "Random Writable" by the *MMC-3* specification. Devices that support this feature can write blocks of data to random locations on the disk. These devices do not require that the initiator address disk locations in any particular order.

</dd> <dt>

<span id="FeatureIncrementalStreamingWritable"></span><span id="featureincrementalstreamingwritable"></span><span id="FEATUREINCREMENTALSTREAMINGWRITABLE"></span>**FeatureIncrementalStreamingWritable**
</dt> <dd>

Indicates the feature named "Incremental Streaming Writable" by the *MMC-3* specification. Devices that support this feature can append data to a limited number of locations on the media.

</dd> <dt>

<span id="FeatureSectorErasable"></span><span id="featuresectorerasable"></span><span id="FEATURESECTORERASABLE"></span>**FeatureSectorErasable**
</dt> <dd>

Indicates the feature named "Sector Erasable" by the *MMC-3* specification. Devices that support this feature require an erase pass before overwriting existing data.

</dd> <dt>

<span id="FeatureFormattable"></span><span id="featureformattable"></span><span id="FEATUREFORMATTABLE"></span>**FeatureFormattable**
</dt> <dd>

Indicates the feature named "Formattable" by the *MMC-3* specification. Devices that support this feature can format media into logical blocks.

</dd> <dt>

<span id="FeatureDefectManagement"></span><span id="featuredefectmanagement"></span><span id="FEATUREDEFECTMANAGEMENT"></span>**FeatureDefectManagement**
</dt> <dd>

Indicates the feature named "Defect Management" by the *MMC-3* specification. Devices that support this feature are able to provide contiguous address space that is guaranteed to be defect free.

</dd> <dt>

<span id="FeatureWriteOnce"></span><span id="featurewriteonce"></span><span id="FEATUREWRITEONCE"></span>**FeatureWriteOnce**
</dt> <dd>

Indicates the feature named "Write Once" by the *MMC-3* specification. Devices that support this feature can write to any previously unused logical block.

</dd> <dt>

<span id="FeatureRestrictedOverwrite"></span><span id="featurerestrictedoverwrite"></span><span id="FEATURERESTRICTEDOVERWRITE"></span>**FeatureRestrictedOverwrite**
</dt> <dd>

Indicates the feature named "Restricted Overwrite" by the *MMC-3* specification. Devices that support this feature are limited in regard to which logical blocks they can overwrite at any given time.

</dd> <dt>

<span id="FeatureCdrwCAVWrite"></span><span id="featurecdrwcavwrite"></span><span id="FEATURECDRWCAVWRITE"></span>**FeatureCdrwCAVWrite**
</dt> <dd>

Indicates the feature named "CD-RW CAV Write" by the *MMC-3* specification. Devices that support this feature can perform writes on CD-RW media in CAV mode.

</dd> <dt>

<span id="FeatureMrw"></span><span id="featuremrw"></span><span id="FEATUREMRW"></span>**FeatureMrw**
</dt> <dd>

Indicates the feature named "MRW" by the *MMC-3* specification. Devices that support this feature can recognize, read and optionally write MRW formatted media.

</dd> <dt>

<span id="FeatureEnhancedDefectReporting"></span><span id="featureenhanceddefectreporting"></span><span id="FEATUREENHANCEDDEFECTREPORTING"></span>**FeatureEnhancedDefectReporting**
</dt> <dd></dd> <dt>

<span id="FeatureDvdPlusRW"></span><span id="featuredvdplusrw"></span><span id="FEATUREDVDPLUSRW"></span>**FeatureDvdPlusRW**
</dt> <dd>

Indicates the feature named "DVD+RW" by the *MMC-3* specification. Devices that support this feature can recognize, read and optionally write DVD+RW media.

</dd> <dt>

<span id="FeatureDvdPlusR"></span><span id="featuredvdplusr"></span><span id="FEATUREDVDPLUSR"></span>**FeatureDvdPlusR**
</dt> <dd></dd> <dt>

<span id="FeatureRigidRestrictedOverwrite"></span><span id="featurerigidrestrictedoverwrite"></span><span id="FEATURERIGIDRESTRICTEDOVERWRITE"></span>**FeatureRigidRestrictedOverwrite**
</dt> <dd>

Indicates the feature named "DVD-RW Restricted Overwrite" by the *MMC-3* specification. Devices that support this feature can only write on block boundaries. These devices cannot perform read or write operations that transfer less than a block of data.

</dd> <dt>

<span id="FeatureCdTrackAtOnce"></span><span id="featurecdtrackatonce"></span><span id="FEATURECDTRACKATONCE"></span>**FeatureCdTrackAtOnce**
</dt> <dd>

Indicates the feature named "CD Track at Once" by the *MMC-3* specification. Devices that support this feature can write data to a CD track.

</dd> <dt>

<span id="FeatureCdMastering"></span><span id="featurecdmastering"></span><span id="FEATURECDMASTERING"></span>**FeatureCdMastering**
</dt> <dd>

Indicates the feature named "CD Mastering" by the *MMC-3* specification. Devices that support this feature can write to a CD in either "Session-at-Once" mode or raw mode.

</dd> <dt>

<span id="FeatureDvdRecordableWrite"></span><span id="featuredvdrecordablewrite"></span><span id="FEATUREDVDRECORDABLEWRITE"></span>**FeatureDvdRecordableWrite**
</dt> <dd>

Indicates the feature named "DVD-R Write" by the *MMC-3* specification. Devices that support this feature can write data to a write-once DVD media in "Disc-at-Once" mode.

</dd> <dt>

<span id="FeatureDDCDRead"></span><span id="featureddcdread"></span><span id="FEATUREDDCDREAD"></span>**FeatureDDCDRead**
</dt> <dd>

Indicates the feature named "DDCD Read" by the *MMC-3* specification. Devices that support this feature can read user data from DDCD blocks.

</dd> <dt>

<span id="FeatureDDCDRWrite"></span><span id="featureddcdrwrite"></span><span id="FEATUREDDCDRWRITE"></span>**FeatureDDCDRWrite**
</dt> <dd>

Indicates the feature named "DDCD-R Write" by the *MMC-3* specification. Devices that support this feature can read and write DDCD-R media.

</dd> <dt>

<span id="FeatureDDCDRWWrite"></span><span id="featureddcdrwwrite"></span><span id="FEATUREDDCDRWWRITE"></span>**FeatureDDCDRWWrite**
</dt> <dd>

Indicates the feature named "DDCD-RW Write" by the *MMC-3* specification. Devices that support this feature can read and write DDCD-RW media.

</dd> <dt>

<span id="FeatureLayerJumpRecording"></span><span id="featurelayerjumprecording"></span><span id="FEATURELAYERJUMPRECORDING"></span>**FeatureLayerJumpRecording**
</dt> <dd>

Reserved 0x0034 - 0x0036

</dd> <dt>

<span id="FeatureCDRWMediaWriteSupport"></span><span id="featurecdrwmediawritesupport"></span><span id="FEATURECDRWMEDIAWRITESUPPORT"></span>**FeatureCDRWMediaWriteSupport**
</dt> <dd></dd> <dt>

<span id="FeatureBDRPseudoOverwrite"></span><span id="featurebdrpseudooverwrite"></span><span id="FEATUREBDRPSEUDOOVERWRITE"></span>**FeatureBDRPseudoOverwrite**
</dt> <dd>

Reserved 0x0039

</dd> <dt>

<span id="FeatureDvdPlusRWDualLayer"></span><span id="featuredvdplusrwduallayer"></span><span id="FEATUREDVDPLUSRWDUALLAYER"></span>**FeatureDvdPlusRWDualLayer**
</dt> <dd></dd> <dt>

<span id="FeatureDvdPlusRDualLayer"></span><span id="featuredvdplusrduallayer"></span><span id="FEATUREDVDPLUSRDUALLAYER"></span>**FeatureDvdPlusRDualLayer**
</dt> <dd>

Reserved 0x003c - 0x003f

</dd> <dt>

<span id="FeatureBDRead"></span><span id="featurebdread"></span><span id="FEATUREBDREAD"></span>**FeatureBDRead**
</dt> <dd></dd> <dt>

<span id="FeatureBDWrite"></span><span id="featurebdwrite"></span><span id="FEATUREBDWRITE"></span>**FeatureBDWrite**
</dt> <dd></dd> <dt>

<span id="FeatureTSR"></span><span id="featuretsr"></span><span id="FEATURETSR"></span>**FeatureTSR**
</dt> <dd>

Reserved 0x0043 - 0x004f

</dd> <dt>

<span id="FeatureHDDVDRead"></span><span id="featurehddvdread"></span><span id="FEATUREHDDVDREAD"></span>**FeatureHDDVDRead**
</dt> <dd></dd> <dt>

<span id="FeatureHDDVDWrite"></span><span id="featurehddvdwrite"></span><span id="FEATUREHDDVDWRITE"></span>**FeatureHDDVDWrite**
</dt> <dd>

Reserved 0x0052 - 0x007f

</dd> <dt>

<span id="FeatureHybridDisc"></span><span id="featurehybriddisc"></span><span id="FEATUREHYBRIDDISC"></span>**FeatureHybridDisc**
</dt> <dd>

Reserved 0x0081 - 0x00ff

</dd> <dt>

<span id="FeaturePowerManagement"></span><span id="featurepowermanagement"></span><span id="FEATUREPOWERMANAGEMENT"></span>**FeaturePowerManagement**
</dt> <dd>

Indicates the feature named "Power Management" by the *MMC-3* specification. Devices that support this feature can perform both initiator and logical-unit directed power management.

</dd> <dt>

<span id="FeatureSMART"></span><span id="featuresmart"></span><span id="FEATURESMART"></span>**FeatureSMART**
</dt> <dd>

Indicates the feature named "S.M.A.R.T." by the *MMC-3* specification. Devices that support this feature support Self-Monitoring Analysis and Reporting Technology (SMART).

</dd> <dt>

<span id="FeatureEmbeddedChanger"></span><span id="featureembeddedchanger"></span><span id="FEATUREEMBEDDEDCHANGER"></span>**FeatureEmbeddedChanger**
</dt> <dd>

Indicates the feature named "Embedded Changer" by the *MMC-3* specification. Devices that support this feature can move media back and forth between a media storage area and the mechanism that actually accesses the media.

</dd> <dt>

<span id="FeatureCDAudioAnalogPlay"></span><span id="featurecdaudioanalogplay"></span><span id="FEATURECDAUDIOANALOGPLAY"></span>**FeatureCDAudioAnalogPlay**
</dt> <dd>

Indicates the feature named "CD Audio External Play" by the *MMC-3* specification. Devices that support this feature can play CD audio data and channel it directly to an external output.

</dd> <dt>

<span id="FeatureMicrocodeUpgrade"></span><span id="featuremicrocodeupgrade"></span><span id="FEATUREMICROCODEUPGRADE"></span>**FeatureMicrocodeUpgrade**
</dt> <dd>

Indicates the feature named "Microcode Upgrade" by the *MMC-3* specification. Devices that support this feature can upgrade their internal microcode by means of a published interface.

</dd> <dt>

<span id="FeatureTimeout"></span><span id="featuretimeout"></span><span id="FEATURETIMEOUT"></span>**FeatureTimeout**
</dt> <dd>

Indicates the feature named "Time-Out" by the *MMC-3* specification. Devices that have this feature must respond to commands within a set time period. When these devices cannot complete commands in the allotted time, they complete the commands with an error.

</dd> <dt>

<span id="FeatureDvdCSS"></span><span id="featuredvdcss"></span><span id="FEATUREDVDCSS"></span>**FeatureDvdCSS**
</dt> <dd>

Indicates the feature named "DVD-CSS" by the *MMC-3* specification. Devices that support this feature can perform DVD Content Scrambling System (DVD-CSS) authentication and key management.

</dd> <dt>

<span id="FeatureRealTimeStreaming"></span><span id="featurerealtimestreaming"></span><span id="FEATUREREALTIMESTREAMING"></span>**FeatureRealTimeStreaming**
</dt> <dd>

Indicates the feature named "Real Time Streaming" by the *MMC-3* specification. Devices that support this feature allow the initiator to specify the performance level of the device within certain limits allowed by the device. These devices must also indicate to the initiator whether they support stream playback operations.

</dd> <dt>

<span id="FeatureLogicalUnitSerialNumber"></span><span id="featurelogicalunitserialnumber"></span><span id="FEATURELOGICALUNITSERIALNUMBER"></span>**FeatureLogicalUnitSerialNumber**
</dt> <dd>

Indicates the feature named "Device Serial Number" by the *MMC-3* specification. Devices that support this feature can furnish the initiator with a serial number that uniquely identifies the device.

</dd> <dt>

<span id="FeatureMediaSerialNumber"></span><span id="featuremediaserialnumber"></span><span id="FEATUREMEDIASERIALNUMBER"></span>**FeatureMediaSerialNumber**
</dt> <dd></dd> <dt>

<span id="FeatureDiscControlBlocks"></span><span id="featuredisccontrolblocks"></span><span id="FEATUREDISCCONTROLBLOCKS"></span>**FeatureDiscControlBlocks**
</dt> <dd>

Indicates the feature named "Disc Control Blocks" by the *MMC-3* specification. Devices that support this feature can read or write Disc Control Blocks.

</dd> <dt>

<span id="FeatureDvdCPRM"></span><span id="featuredvdcprm"></span><span id="FEATUREDVDCPRM"></span>**FeatureDvdCPRM**
</dt> <dd>

Indicates the feature named "DVD CPRM" by the *MMC-3* specification. Devices that support this feature can perform DVD Content Protection for Recordable Media (CPRM) authentication and key management.

</dd> <dt>

<span id="FeatureFirmwareDate"></span><span id="featurefirmwaredate"></span><span id="FEATUREFIRMWAREDATE"></span>**FeatureFirmwareDate**
</dt> <dd></dd> <dt>

<span id="FeatureAACS"></span><span id="featureaacs"></span><span id="FEATUREAACS"></span>**FeatureAACS**
</dt> <dd>

Reserved 0x010e - 0x010f

</dd> <dt>

<span id="FeatureVCPS"></span><span id="featurevcps"></span><span id="FEATUREVCPS"></span>**FeatureVCPS**
</dt> <dd>

Reserved 0x0111 - 0xfeff

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_NUMBER%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






