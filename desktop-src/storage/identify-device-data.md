---
title: IDENTIFY\_DEVICE\_DATA structure
description: The IDENTIFY\_DEVICE\_DATA structure contains the data retrieved by an ATA identify device data command (0xEC).Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: '7f2edd6f-16bf-47a6-8546-7871435a56ac'
keywords: ["IDENTIFY_DEVICE_DATA structure Storage Devices", "PIDENTIFY_DEVICE_DATA structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- IDENTIFY_DEVICE_DATA
api_location:
- ata.h
api_type:
- HeaderDef
---

# IDENTIFY\_DEVICE\_DATA structure

The IDENTIFY\_DEVICE\_DATA structure contains the data retrieved by an ATA identify device data command (0xEC).

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDENTIFY_DEVICE_DATA {
  struct {
    USHORT Reserved1  :1;
    USHORT Retired3  :1;
    USHORT ResponseIncomplete  :1;
    USHORT Retired2  :3;
    USHORT FixedDevice  :1;
    USHORT RemovableMedia  :1;
    USHORT Retired1  :7;
    USHORT DeviceType  :1;
  } GeneralConfiguration;
  USHORT NumCylinders;
  USHORT ReservedWord2;
  USHORT NumHeads;
  USHORT Retired1[2];
  USHORT NumSectorsPerTrack;
  USHORT VendorUnique1[3];
  UCHAR  SerialNumber[20];
  USHORT Retired2[2];
  USHORT Obsolete1;
  UCHAR  FirmwareRevision[8];
  UCHAR  ModelNumber[40];
  UCHAR  MaximumBlockTransfer;
  UCHAR  VendorUnique2;
  USHORT ReservedWord48;
  struct {
    UCHAR  ReservedByte49;
    UCHAR  DmaSupported  :1;
    UCHAR  LbaSupported  :1;
    UCHAR  IordyDisable  :1;
    UCHAR  IordySupported  :1;
    UCHAR  Reserved1  :1;
    UCHAR  StandybyTimerSupport  :1;
    UCHAR  Reserved2  :2;
    USHORT ReservedWord50;
  } Capabilities;
  USHORT ObsoleteWords51[2];
  USHORT TranslationFieldsValid  :3;
  USHORT Reserved3  :13;
  USHORT NumberOfCurrentCylinders;
  USHORT NumberOfCurrentHeads;
  USHORT CurrentSectorsPerTrack;
  ULONG  CurrentSectorCapacity;
  UCHAR  CurrentMultiSectorSetting;
  UCHAR  MultiSectorSettingValid  :1;
  UCHAR  ReservedByte59  :7;
  ULONG  UserAddressableSectors;
  USHORT ObsoleteWord62;
  USHORT MultiWordDMASupport  :8;
  USHORT MultiWordDMAActive  :8;
  USHORT AdvancedPIOModes  :8;
  USHORT ReservedByte64  :8;
  USHORT MinimumMWXferCycleTime;
  USHORT RecommendedMWXferCycleTime;
  USHORT MinimumPIOCycleTime;
  USHORT MinimumPIOCycleTimeIORDY;
  USHORT ReservedWords69[6];
  USHORT QueueDepth  :5;
  USHORT ReservedWord75  :11;
  USHORT ReservedWords76[4];
  USHORT MajorRevision;
  USHORT MinorRevision;
  struct {
    USHORT SmartCommands  :1;
    USHORT SecurityMode  :1;
    USHORT RemovableMediaFeature  :1;
    USHORT PowerManagement  :1;
    USHORT Reserved1  :1;
    USHORT WriteCache  :1;
    USHORT LookAhead  :1;
    USHORT ReleaseInterrupt  :1;
    USHORT ServiceInterrupt  :1;
    USHORT DeviceReset  :1;
    USHORT HostProtectedArea  :1;
    USHORT Obsolete1  :1;
    USHORT WriteBuffer  :1;
    USHORT ReadBuffer  :1;
    USHORT Nop  :1;
    USHORT Obsolete2  :1;
    USHORT DownloadMicrocode  :1;
    USHORT DmaQueued  :1;
    USHORT Cfa  :1;
    USHORT AdvancedPm  :1;
    USHORT Msn  :1;
    USHORT PowerUpInStandby  :1;
    USHORT ManualPowerUp  :1;
    USHORT Reserved2  :1;
    USHORT SetMax  :1;
    USHORT Acoustics  :1;
    USHORT BigLba  :1;
    USHORT DeviceConfigOverlay  :1;
    USHORT FlushCache  :1;
    USHORT FlushCacheExt  :1;
    USHORT Resrved3  :2;
    USHORT SmartErrorLog  :1;
    USHORT SmartSelfTest  :1;
    USHORT MediaSerialNumber  :1;
    USHORT MediaCardPassThrough  :1;
    USHORT StreamingFeature  :1;
    USHORT GpLogging  :1;
    USHORT WriteFua  :1;
    USHORT WriteQueuedFua  :1;
    USHORT WWN64Bit  :1;
    USHORT URGReadStream  :1;
    USHORT URGWriteStream  :1;
    USHORT ReservedForTechReport  :2;
    USHORT IdleWithUnloadFeature  :1;
    USHORT Reserved4  :2;
  } CommandSetSupport;
  struct {
    USHORT SmartCommands  :1;
    USHORT SecurityMode  :1;
    USHORT RemovableMediaFeature  :1;
    USHORT PowerManagement  :1;
    USHORT Reserved1  :1;
    USHORT WriteCache  :1;
    USHORT LookAhead  :1;
    USHORT ReleaseInterrupt  :1;
    USHORT ServiceInterrupt  :1;
    USHORT DeviceReset  :1;
    USHORT HostProtectedArea  :1;
    USHORT Obsolete1  :1;
    USHORT WriteBuffer  :1;
    USHORT ReadBuffer  :1;
    USHORT Nop  :1;
    USHORT Obsolete2  :1;
    USHORT DownloadMicrocode  :1;
    USHORT DmaQueued  :1;
    USHORT Cfa  :1;
    USHORT AdvancedPm  :1;
    USHORT Msn  :1;
    USHORT PowerUpInStandby  :1;
    USHORT ManualPowerUp  :1;
    USHORT Reserved2  :1;
    USHORT SetMax  :1;
    USHORT Acoustics  :1;
    USHORT BigLba  :1;
    USHORT DeviceConfigOverlay  :1;
    USHORT FlushCache  :1;
    USHORT FlushCacheExt  :1;
    USHORT Resrved3  :2;
    USHORT SmartErrorLog  :1;
    USHORT SmartSelfTest  :1;
    USHORT MediaSerialNumber  :1;
    USHORT MediaCardPassThrough  :1;
    USHORT StreamingFeature  :1;
    USHORT GpLogging  :1;
    USHORT WriteFua  :1;
    USHORT WriteQueuedFua  :1;
    USHORT WWN64Bit  :1;
    USHORT URGReadStream  :1;
    USHORT URGWriteStream  :1;
    USHORT ReservedForTechReport  :2;
    USHORT IdleWithUnloadFeature  :1;
    USHORT Reserved4  :2;
  } CommandSetActive;
  USHORT UltraDMASupport  :8;
  USHORT UltraDMAActive  :8;
  USHORT ReservedWord89[4];
  USHORT HardwareResetResult;
  USHORT CurrentAcousticValue  :8;
  USHORT RecommendedAcousticValue  :8;
  USHORT ReservedWord95[5];
  ULONG  Max48BitLBA[2];
  USHORT StreamingTransferTime;
  USHORT ReservedWord105;
  struct {
    USHORT LogicalSectorsPerPhysicalSector  :4;
    USHORT Reserved0  :8;
    USHORT LogicalSectorLongerThan256Words  :1;
    USHORT MultipleLogicalSectorsPerPhysicalSector  :1;
    USHORT Reserved1  :2;
  } PhysicalLogicalSectorSize;
  USHORT InterSeekDelay;
  USHORT WorldWideName[4];
  USHORT ReservedForWorldWideName128[4];
  USHORT ReservedForTlcTechnicalReport;
  USHORT WordsPerLogicalSector[2];
  struct {
    USHORT ReservedForDrqTechnicalReport  :1;
    USHORT WriteReadVerifySupported  :1;
    USHORT Reserved01  :11;
    USHORT Reserved1  :2;
  } CommandSetSupportExt;
  struct {
    USHORT ReservedForDrqTechnicalReport  :1;
    USHORT WriteReadVerifyEnabled  :1;
    USHORT Reserved01  :11;
    USHORT Reserved1  :2;
  } CommandSetActiveExt;
  USHORT ReservedForExpandedSupportandActive[6];
  USHORT MsnSupport  :2;
  USHORT ReservedWord1274  :14;
  struct {
    USHORT SecuritySupported  :1;
    USHORT SecurityEnabled  :1;
    USHORT SecurityLocked  :1;
    USHORT SecurityFrozen  :1;
    USHORT SecurityCountExpired  :1;
    USHORT EnhancedSecurityEraseSupported  :1;
    USHORT Reserved0  :2;
    USHORT SecurityLevel  :1;
    USHORT Reserved1  :7;
  } SecurityStatus;
  USHORT ReservedWord129[31];
  struct {
    USHORT MaximumCurrentInMA2  :12;
    USHORT CfaPowerMode1Disabled  :1;
    USHORT CfaPowerMode1Required  :1;
    USHORT Reserved0  :1;
    USHORT Word160Supported  :1;
  } CfaPowerModel;
  USHORT ReservedForCfaWord161[8];
  struct {
    USHORT SupportsTrim  :1;
    USHORT Reserved0  :15;
  } DataSetManagementFeature;
  USHORT ReservedForCfaWord170[6];
  USHORT CurrentMediaSerialNumber[30];
  USHORT ReservedWord206;
  USHORT ReservedWord207[2];
  struct {
    USHORT AlignmentOfLogicalWithinPhysical  :14;
    USHORT Word209Supported  :1;
    USHORT Reserved0  :1;
  } BlockAlignment;
  USHORT WriteReadVerifySectorCountMode3Only[2];
  USHORT WriteReadVerifySectorCountMode2Only[2];
  struct {
    USHORT NVCachePowerModeEnabled  :1;
    USHORT Reserved0  :3;
    USHORT NVCacheFeatureSetEnabled  :1;
    USHORT Reserved1  :3;
    USHORT NVCachePowerModeVersion  :4;
    USHORT NVCacheFeatureSetVersion  :4;
  } NVCacheCapabilities;
  USHORT NVCacheSizeLSW;
  USHORT NVCacheSizeMSW;
  USHORT NominalMediaRotationRate;
  USHORT ReservedWord218;
  struct {
    UCHAR NVCacheEstimatedTimeToSpinUpInSeconds;
    UCHAR Reserved;
  } NVCacheOptions;
  USHORT ReservedWord220[35];
  USHORT Signature  :8;
  USHORT CheckSum  :8;
} IDENTIFY_DEVICE_DATA, *PIDENTIFY_DEVICE_DATA;
```



## Members

<dl> <dt>

**GeneralConfiguration**
</dt> <dd> <dl> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Retired3**
</dt> <dd>

This member is no longer used.

</dd> <dt>

**ResponseIncomplete**
</dt> <dd>

Indicates that the response was incomplete.

</dd> <dt>

**Retired2**
</dt> <dd>

This member is no longer used.

</dd> <dt>

**FixedDevice**
</dt> <dd>

Indicates when set to 1 that the device is fixed.

</dd> <dt>

**RemovableMedia**
</dt> <dd>

Indicates when set to 1 that the media is removable.

</dd> <dt>

**Retired1**
</dt> <dd>

This member is no longer used.

</dd> <dt>

**DeviceType**
</dt> <dd>

Indicates when set to 1 that the device is an ATA device.

</dd> </dl> </dd> <dt>

**NumCylinders**
</dt> <dd>

Indicates the number of cylinders on the device.

</dd> <dt>

**ReservedWord2**
</dt> <dd>

Reserved.

</dd> <dt>

**NumHeads**
</dt> <dd>

Number of logical heads on the device.

</dd> <dt>

**Retired1**
</dt> <dd>

This member is no longer used.

</dd> <dt>

**NumSectorsPerTrack**
</dt> <dd>

Indicates the number of sectors per track.

</dd> <dt>

**VendorUnique1**
</dt> <dd>

Contains the first ID of the device's vendor.

</dd> <dt>

**SerialNumber**
</dt> <dd>

Contains the serial number of the device.

</dd> <dt>

**Retired2**
</dt> <dd>

This member is no longer used.

</dd> <dt>

**Obsolete1**
</dt> <dd>

This member is obsolete. Do not use.

</dd> <dt>

**FirmwareRevision**
</dt> <dd>

Contains the revision number of the device's firmware.

</dd> <dt>

**ModelNumber**
</dt> <dd>

Contains the device's model number.

</dd> <dt>

**MaximumBlockTransfer**
</dt> <dd>

Contains the maximum number of blocks allowed in a single transfer.

</dd> <dt>

**VendorUnique2**
</dt> <dd>

Contains the second ID of the device's vendor.

</dd> <dt>

**ReservedWord48**
</dt> <dd>

Reserved.

</dd> <dt>

**Capabilities**
</dt> <dd> <dl> <dt>

**ReservedByte49**
</dt> <dd>

Reserved.

</dd> <dt>

**DmaSupported**
</dt> <dd>

Indicates that the device supports DMA operations.

</dd> <dt>

**LbaSupported**
</dt> <dd>

Indicates that the device supports logical block addressing.

</dd> <dt>

**IordyDisable**
</dt> <dd>

Indicates when set to 1 that I/O channel ready is disabled for the device.

</dd> <dt>

**IordySupported**
</dt> <dd>

Indicates when set to 1 that I/O channel ready is supported by the device.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**StandybyTimerSupport**
</dt> <dd>

Indicates when set to 1 that the device supports standby timers.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**ReservedWord50**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**ObsoleteWords51**
</dt> <dd>

This member is obsolete. Do not use.

</dd> <dt>

**TranslationFieldsValid**
</dt> <dd>

Contains a bitfield whose bits indicate which of the bytes in the identify data package contain valid address translation information. For more information about how this bitfield is defined, see the *ATA/ATAPI specification*.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> <dt>

**NumberOfCurrentCylinders**
</dt> <dd>

Indicates the number of cylinders on the device.

</dd> <dt>

**NumberOfCurrentHeads**
</dt> <dd>

Indicates the number of heads on the device.

</dd> <dt>

**CurrentSectorsPerTrack**
</dt> <dd>

Indicates the number of sectors per track.

</dd> <dt>

**CurrentSectorCapacity**
</dt> <dd>

Indicates the number of sectors on the device.

</dd> <dt>

**CurrentMultiSectorSetting**
</dt> <dd>

Indicates the multisector setting.

</dd> <dt>

**MultiSectorSettingValid**
</dt> <dd>

Indicates when **TRUE** that the multisector setting is valid.

</dd> <dt>

**ReservedByte59**
</dt> <dd>

Reserved.

</dd> <dt>

**UserAddressableSectors**
</dt> <dd>

Indicates the total number of user-addressable sectors.

</dd> <dt>

**ObsoleteWord62**
</dt> <dd>

This member is obsolete. Do not use.

</dd> <dt>

**MultiWordDMASupport**
</dt> <dd>

Indicates which DMA modes the device supports.

</dd> <dt>

**MultiWordDMAActive**
</dt> <dd>

Indicates which DMA modes are currently selected.

</dd> <dt>

**AdvancedPIOModes**
</dt> <dd></dd> <dt>

**ReservedByte64**
</dt> <dd>

Reserved.

</dd> <dt>

**MinimumMWXferCycleTime**
</dt> <dd>

Indicates the minimum multiword DMA transfer cycle time per word.

</dd> <dt>

**RecommendedMWXferCycleTime**
</dt> <dd>

Indicates the recommended multiword DMA transfer cycle time per word.

</dd> <dt>

**MinimumPIOCycleTime**
</dt> <dd>

Indicates the minimum PIO transfer cycle time without flow control.

</dd> <dt>

**MinimumPIOCycleTimeIORDY**
</dt> <dd>

Indicates the minimum PIO transfer cycle time with IORDY flow control.

</dd> <dt>

**ReservedWords69**
</dt> <dd>

Reserved.

</dd> <dt>

**QueueDepth**
</dt> <dd>

Indicates the maximum queue depth.

</dd> <dt>

**ReservedWord75**
</dt> <dd>

Reserved.

</dd> <dt>

**ReservedWords76**
</dt> <dd>

Reserved.

</dd> <dt>

**MajorRevision**
</dt> <dd>

Indicates the device's major revision number.

</dd> <dt>

**MinorRevision**
</dt> <dd>

Indicates the device's minor revision number.

</dd> <dt>

**CommandSetSupport**
</dt> <dd> <dl> <dt>

**SmartCommands**
</dt> <dd>

Indicates when **TRUE** that the device supports the SMART feature set.

</dd> <dt>

**SecurityMode**
</dt> <dd>

Indicates when **TRUE** that the device supports the security mode feature set.

</dd> <dt>

**PowerManagement**
</dt> <dd>

Indicates when **TRUE** that the device supports the mandatory power management feature set.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**WriteCache**
</dt> <dd>

Indicates when **TRUE** that the device supports a write cache.

</dd> <dt>

**LookAhead**
</dt> <dd>

Indicates when **TRUE** that the device supports lookahead.

</dd> <dt>

**ReleaseInterrupt**
</dt> <dd>

Indicates when **TRUE** that the device supports release interrupt.

</dd> <dt>

**ServiceInterrupt**
</dt> <dd>

Indicates when **TRUE** that the device supports service interrupt.

</dd> <dt>

**DeviceReset**
</dt> <dd>

Indicates when **TRUE** that the device supports the device reset command.

</dd> <dt>

**HostProtectedArea**
</dt> <dd>

Indicates when **TRUE** that the device supports the host protected area feature set.

</dd> <dt>

**Obsolete1**
</dt> <dd>

This member is obsolete. Do not use.

</dd> <dt>

**WriteBuffer**
</dt> <dd>

Indicates when **TRUE** that the device supports the write buffer command.

</dd> <dt>

**ReadBuffer**
</dt> <dd>

Indicates when **TRUE** that the device supports the read buffer command.

</dd> <dt>

**Nop**
</dt> <dd>

Indicates when **TRUE** that the device supports the NOP command.

</dd> <dt>

**Obsolete2**
</dt> <dd>

Obsolete. Do not use.

</dd> <dt>

**DownloadMicrocode**
</dt> <dd>

Indicates when **TRUE** that the device supports the DOWNLOAD MICROCODE command.

</dd> <dt>

**DmaQueued**
</dt> <dd>

Indicates when **TRUE** that the device supports READ/WRITE DMA QUEUED command.

</dd> <dt>

**Cfa**
</dt> <dd>

Indicates when **TRUE** that the device supports the CFA feature set.

</dd> <dt>

**AdvancedPm**
</dt> <dd>

Indicates when **TRUE** that the device supports the advanced power management feature set.

</dd> <dt>

**Msn**
</dt> <dd>

Indicates when **TRUE** that the device supports the media status notification feature set.

</dd> <dt>

**PowerUpInStandby**
</dt> <dd>

Indicates when **TRUE** that the device supports power-up in standby feature set.

</dd> <dt>

**ManualPowerUp**
</dt> <dd>

Indicates when **TRUE** that the device supports the SET FEATURES subcommand required to spin up the device after power-up.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**SetMax**
</dt> <dd>

Indicates when **TRUE** that the device supports the SET MAX security extension command.

</dd> <dt>

**Acoustics**
</dt> <dd>

Indicates when **TRUE** that the device supports the automatic acoustic management feature set.

</dd> <dt>

**BigLba**
</dt> <dd>

Indicates when **TRUE** that the device supports the 48-bit address feature set.

</dd> <dt>

**Resrved3**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**CommandSetActive**
</dt> <dd> <dl> <dt>


</dt> <dt>


</dt> </dl> <dl> <dt>

**SmartCommands**
</dt> <dd>

Indicates when **TRUE** that the device supports the SMART feature set.

</dd> <dt>

**SecurityMode**
</dt> <dd>

Indicates when **TRUE** that the device supports the security mode feature set.

</dd> <dt>

**PowerManagement**
</dt> <dd>

Indicates when **TRUE** that the device supports the mandatory power management feature set.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**WriteCache**
</dt> <dd>

Indicates when **TRUE** that the device supports a write cache.

</dd> <dt>

**LookAhead**
</dt> <dd>

Indicates when **TRUE** that the device supports lookahead.

</dd> <dt>

**ReleaseInterrupt**
</dt> <dd>

Indicates when **TRUE** that the device supports release interrupt.

</dd> <dt>

**ServiceInterrupt**
</dt> <dd>

Indicates when **TRUE** that the device supports service interrupt.

</dd> <dt>

**DeviceReset**
</dt> <dd>

Indicates when **TRUE** that the device supports the device reset command.

</dd> <dt>

**HostProtectedArea**
</dt> <dd>

Indicates when **TRUE** that the device supports the host protected area feature set.

</dd> <dt>

**Obsolete1**
</dt> <dd>

This member is obsolete. Do not use.

</dd> <dt>

**WriteBuffer**
</dt> <dd>

Indicates when **TRUE** that the device supports the write buffer command.

</dd> <dt>

**ReadBuffer**
</dt> <dd>

Indicates when **TRUE** that the device supports the read buffer command.

</dd> <dt>

**Nop**
</dt> <dd>

Indicates when **TRUE** that the device supports the NOP command.

</dd> <dt>

**Obsolete2**
</dt> <dd>

Obsolete. Do not use.

</dd> <dt>

**DownloadMicrocode**
</dt> <dd>

Indicates when **TRUE** that the device supports the DOWNLOAD MICROCODE command.

</dd> <dt>

**DmaQueued**
</dt> <dd>

Indicates when **TRUE** that the device supports READ/WRITE DMA QUEUED command.

</dd> <dt>

**Cfa**
</dt> <dd>

Indicates when **TRUE** that the device supports the CFA feature set.

</dd> <dt>

**AdvancedPm**
</dt> <dd>

Indicates when **TRUE** that the device supports the advanced power management feature set.

</dd> <dt>

**Msn**
</dt> <dd>

Indicates when **TRUE** that the device supports the media status notification feature set.

</dd> <dt>

**PowerUpInStandby**
</dt> <dd>

Indicates when **TRUE** that the device supports power-up in standby feature set.

</dd> <dt>

**ManualPowerUp**
</dt> <dd>

Indicates when **TRUE** that the device supports the SET FEATURES subcommand required to spin up the device after power-up.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**SetMax**
</dt> <dd>

Indicates when **TRUE** that the device supports the SET MAX security extension command.

</dd> <dt>

**Acoustics**
</dt> <dd>

Indicates when **TRUE** that the device supports the automatic acoustic management feature set.

</dd> <dt>

**BigLba**
</dt> <dd>

Indicates when **TRUE** that the device supports the 48-bit address feature set.

</dd> <dt>

**Resrved3**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**UltraDMASupport**
</dt> <dd>

Contains a bitmap indicating which ultraDMA modes the device supports.

</dd> <dt>

**UltraDMAActive**
</dt> <dd>

Contains a bitmap indicating which ultraDMA modes are selected.

</dd> <dt>

**ReservedWord89**
</dt> <dd>

Reserved.

</dd> <dt>

**HardwareResetResult**
</dt> <dd>

Indicates the result of a hardware reset. For more information about the values assigned to this member, see the *ATA/ATAP specification*.

</dd> <dt>

**CurrentAcousticValue**
</dt> <dd>

Indicates the current acoustic management value.

</dd> <dt>

**RecommendedAcousticValue**
</dt> <dd>

Contain the device vendor's recommended acoustic management value.

</dd> <dt>

**ReservedWord95**
</dt> <dd>

Reserved.

</dd> <dt>

**Max48BitLBA**
</dt> <dd>

Contains the maximum user LBA for the 48-bit address feature set.

</dd> <dt>

**StreamingTransferTime**
</dt> <dd></dd> <dt>

**ReservedWord105**
</dt> <dd></dd> <dt>

**PhysicalLogicalSectorSize**
</dt> <dd> <dl> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**InterSeekDelay**
</dt> <dd></dd> <dt>

**WorldWideName**
</dt> <dd></dd> <dt>

**ReservedForWorldWideName128**
</dt> <dd></dd> <dt>

**ReservedForTlcTechnicalReport**
</dt> <dd></dd> <dt>

**WordsPerLogicalSector**
</dt> <dd></dd> <dt>

**CommandSetSupportExt**
</dt> <dd> <dl> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**CommandSetActiveExt**
</dt> <dd> <dl> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**ReservedForExpandedSupportandActive**
</dt> <dd></dd> <dt>

**MsnSupport**
</dt> <dd>

Indicates when **TRUE** that the device supports media status notification.

</dd> <dt>

**ReservedWord1274**
</dt> <dd></dd> <dt>

**SecurityStatus**
</dt> <dd>

Contains a bitmap that indicates the security status. For more information about the meaning of each individual bit, see the *ATA/ATAPI specification*.

<dl> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**ReservedWord129**
</dt> <dd>

Reserved.

</dd> <dt>

**CfaPowerModel**
</dt> <dd> <dl></dl> </dd> <dt>

**ReservedForCfaWord161**
</dt> <dd>

Words 161-168

</dd> <dt>

**DataSetManagementFeature**
</dt> <dd> <dl></dl> </dd> <dt>

**ReservedForCfaWord170**
</dt> <dd>

Words 170-175

</dd> <dt>

**CurrentMediaSerialNumber**
</dt> <dd>

Words 176-205

</dd> <dt>

**ReservedWord206**
</dt> <dd>

Word 206

</dd> <dt>

**ReservedWord207**
</dt> <dd>

Words 207-208

</dd> <dt>

**BlockAlignment**
</dt> <dd> <dl></dl> </dd> <dt>

**WriteReadVerifySectorCountMode3Only**
</dt> <dd>

Words 210-211

</dd> <dt>

**WriteReadVerifySectorCountMode2Only**
</dt> <dd>

Words 212-213

</dd> <dt>

**NVCacheCapabilities**
</dt> <dd> <dl> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**NVCacheSizeLSW**
</dt> <dd></dd> <dt>

**NVCacheSizeMSW**
</dt> <dd></dd> <dt>

**NominalMediaRotationRate**
</dt> <dd></dd> <dt>

**ReservedWord218**
</dt> <dd></dd> <dt>

**NVCacheOptions**
</dt> <dd> <dl></dl> </dd> <dt>

**ReservedWord220**
</dt> <dd>

Words 220-254

</dd> <dt>

**Signature**
</dt> <dd>

Indicates the disk signature.

</dd> <dt>

**CheckSum**
</dt> <dd>

Indicates the checksum.

</dd> </dl>

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ata.h (include Irb.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDENTIFY_DEVICE_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





