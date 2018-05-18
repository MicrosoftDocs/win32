---
title: UFS\_ATTRIBUTES\_DESCRIPTOR enumeration
description: UFS\_ATTRIBUTES\_DESCRIPTOR describes the different types of attributes used by Universal Flash Storage (UFS) descriptors.
ms.assetid: '695D8FE9-FADB-488F-A5F7-7715EAD48DD6'
keywords: ["UFS_ATTRIBUTES_DESCRIPTOR enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- UFS_ATTRIBUTES_DESCRIPTOR
api_location:
- Ufs.h
api_type:
- HeaderDef
---

# UFS\_ATTRIBUTES\_DESCRIPTOR enumeration

**UFS\_ATTRIBUTES\_DESCRIPTOR** describes the different types of attributes used by Universal Flash Storage (UFS) descriptors.

## Syntax


```C++
typedef enum _UFS_ATTRIBUTES_DESCRIPTOR { 
  UFS_bBootLunEn              = 0,
  UFS_Reserved01,
  UFS_bCurrentPowerMode,
  UFS_bActiveICCLevel,
  UFS_bOutOfOrderDataEn,
  UFS_bBackgroundOpStatus,
  UFS_bPurgeStatus,
  UFS_bMaxDataInSize,
  UFS_bMaxDataOutSize,
  UFS_dDynCapNeeded,
  UFS_bRefClkFreq,
  UFS_bConfigDescrLock,
  UFS_bMaxNumOfRTT,
  UFS_wExceptionEventControl,
  UFS_wExceptionEventStatus,
  UFS_dSecondsPassed,
  UFS_wContextConf,
  UFS_Obsolete,
  UFS_Reserved02,
  UFS_Reserved03,
  UFS_bDeviceFFUStatus,
  UFS_bPSAState,
  UFS_dPSADataSize
} UFS_ATTRIBUTES_DESCRIPTOR;
```



## Constants

<dl> <dt>

<span id="UFS_bBootLunEn"></span><span id="ufs_bbootlunen"></span><span id="UFS_BBOOTLUNEN"></span>**UFS\_bBootLunEn**
</dt> <dd>

Indicates if the Boot Logical Unit Number(LUN) is enabled.

</dd> <dt>

<span id="UFS_Reserved01"></span><span id="ufs_reserved01"></span><span id="UFS_RESERVED01"></span>**UFS\_Reserved01**
</dt> <dd>

Reserved for future use.

</dd> <dt>

<span id="UFS_bCurrentPowerMode"></span><span id="ufs_bcurrentpowermode"></span><span id="UFS_BCURRENTPOWERMODE"></span>**UFS\_bCurrentPowerMode**
</dt> <dd>

Indicates the current power mode. Contains one of the following values:



| Value            | Description                                                   |
|------------------|---------------------------------------------------------------|
| 0x00             | Idle power mode.                                              |
| 0x10             | Pre-Active power mode.                                        |
| 0x11             | Active power mode.                                            |
| 0x20             | Pre-Sleep power mode.                                         |
| 0x22             | Universal Flash Storage (UFS)-Sleep power mode.               |
| 0x30             | 40% to 50% of the device's estimated life time has been used. |
| 0x33             | 50% to 60% of the device's estimated life time has been used. |
| All other values | Reserved for future use.                                      |



 

</dd> <dt>

<span id="UFS_bActiveICCLevel"></span><span id="ufs_bactiveicclevel"></span><span id="UFS_BACTIVEICCLEVEL"></span>**UFS\_bActiveICCLevel**
</dt> <dd>

Specifies the maximum current consumption allowed during Active Mode. Value ranges from 0x00 to 0x0F.

</dd> <dt>

<span id="UFS_bOutOfOrderDataEn"></span><span id="ufs_boutoforderdataen"></span><span id="UFS_BOUTOFORDERDATAEN"></span>**UFS\_bOutOfOrderDataEn**
</dt> <dd>

Specifies if out-of-order data transfer is enabled

</dd> <dt>

<span id="UFS_bBackgroundOpStatus"></span><span id="ufs_bbackgroundopstatus"></span><span id="UFS_BBACKGROUNDOPSTATUS"></span>**UFS\_bBackgroundOpStatus**
</dt> <dd>

Specifies if the device has a need for background operations. Contains one of the following values:



| Value | Description                                                            |
|-------|------------------------------------------------------------------------|
| 0x00  | Device requires no background operations.                              |
| 0x01  | Device has a non-critical need of background operations.               |
| 0x02  | Device has a performance impacted-based need of background operations. |
| 0x03  | Device has a critical need of background operations.                   |



 

</dd> <dt>

<span id="UFS_bPurgeStatus"></span><span id="ufs_bpurgestatus"></span><span id="UFS_BPURGESTATUS"></span>**UFS\_bPurgeStatus**
</dt> <dd>

Specifies the current purge operation's status.

</dd> <dt>

<span id="UFS_bMaxDataInSize"></span><span id="ufs_bmaxdatainsize"></span><span id="UFS_BMAXDATAINSIZE"></span>**UFS\_bMaxDataInSize**
</dt> <dd>

Specifies the maximum data size in a DATA IN UFS Protocol Information Units (UPIU). This parameter can be written by the host only when all logical unit task queues are empty.

</dd> <dt>

<span id="UFS_bMaxDataOutSize"></span><span id="ufs_bmaxdataoutsize"></span><span id="UFS_BMAXDATAOUTSIZE"></span>**UFS\_bMaxDataOutSize**
</dt> <dd>

Specifies the maximum data-out size. This parameter can be written by the host only when all logical unit task queues are empty.

</dd> <dt>

<span id="UFS_dDynCapNeeded"></span><span id="ufs_ddyncapneeded"></span><span id="UFS_DDYNCAPNEEDED"></span>**UFS\_dDynCapNeeded**
</dt> <dd>

Specifies the dynamic capacity need.

</dd> <dt>

<span id="UFS_bRefClkFreq"></span><span id="ufs_brefclkfreq"></span><span id="UFS_BREFCLKFREQ"></span>**UFS\_bRefClkFreq**
</dt> <dd>

Specifies the reference clock frequency value.



| Value | Description |
|-------|-------------|
| 0x00  | 19.2 MHz    |
| 0x01  | 26 MHz      |
| 0x02  | 38.4 MHz    |
| 0x03  | 52 MHz      |



 

</dd> <dt>

<span id="UFS_bConfigDescrLock"></span><span id="ufs_bconfigdescrlock"></span><span id="UFS_BCONFIGDESCRLOCK"></span>**UFS\_bConfigDescrLock**
</dt> <dd>

Specifies if the configuration descriptor is locked.

</dd> <dt>

<span id="UFS_bMaxNumOfRTT"></span><span id="ufs_bmaxnumofrtt"></span><span id="UFS_BMAXNUMOFRTT"></span>**UFS\_bMaxNumOfRTT**
</dt> <dd>

Defines the current maximum number of outstanding READY TO TRANSFER UPIU’s (RTT's) that are allowed. This value can be set by the host.

</dd> <dt>

<span id="UFS_wExceptionEventControl"></span><span id="ufs_wexceptioneventcontrol"></span><span id="UFS_WEXCEPTIONEVENTCONTROL"></span>**UFS\_wExceptionEventControl**
</dt> <dd>

Specifies the Exception Event Controller. **UFS\_wExceptionEventControl** enables the setting of the **EVENT\_ALERT** bit in the Device Information field, which is contained in the RESPONSE UPIU.

</dd> <dt>

<span id="UFS_wExceptionEventStatus"></span><span id="ufs_wexceptioneventstatus"></span><span id="UFS_WEXCEPTIONEVENTSTATUS"></span>**UFS\_wExceptionEventStatus**
</dt> <dd>

Specifies a bitmap of each exception event status.A bit will be set only if the relevant event has occurred (regardless of the **UFS\_wExceptionEventControl** status). Contains the following bits:



| Bit     | Value              |
|---------|--------------------|
| 0       | DYNCAP\_NEEDED     |
| 1       | SYSPOOL\_EXHAUSTED |
| 2       | URGENT\_BKOPS      |
| 3 to 15 | Reserved.          |



 

</dd> <dt>

<span id="UFS_dSecondsPassed"></span><span id="ufs_dsecondspassed"></span><span id="UFS_DSECONDSPASSED"></span>**UFS\_dSecondsPassed**
</dt> <dd>

Specifies the time passed in seconds.

</dd> <dt>

<span id="UFS_wContextConf"></span><span id="ufs_wcontextconf"></span><span id="UFS_WCONTEXTCONF"></span>**UFS\_wContextConf**
</dt> <dd>

Specifies the context attribute.

</dd> <dt>

<span id="UFS_Obsolete"></span><span id="ufs_obsolete"></span><span id="UFS_OBSOLETE"></span>**UFS\_Obsolete**
</dt> <dd>

Obselete

</dd> <dt>

<span id="UFS_Reserved02"></span><span id="ufs_reserved02"></span><span id="UFS_RESERVED02"></span>**UFS\_Reserved02**
</dt> <dd>

Reserved for future use.

</dd> <dt>

<span id="UFS_Reserved03"></span><span id="ufs_reserved03"></span><span id="UFS_RESERVED03"></span>**UFS\_Reserved03**
</dt> <dd>

Reserved for future use.

</dd> <dt>

<span id="UFS_bDeviceFFUStatus"></span><span id="ufs_bdeviceffustatus"></span><span id="UFS_BDEVICEFFUSTATUS"></span>**UFS\_bDeviceFFUStatus**
</dt> <dd>

Specifies the Device Field Firmware Update (FFU) status.



| Value        | Description                       |
|--------------|-----------------------------------|
| 0x00         | No information on the FFU status. |
| 0x01         | Successful microcode update.      |
| 0x02         | Microcode corruption error.       |
| 0x03         | Internal error.                   |
| 0x04         | Microcode version mismatch.       |
| 0x05 to 0xFE | Reserved.                         |
| 0xFF         | General Error.                    |



 

</dd> <dt>

<span id="UFS_bPSAState"></span><span id="ufs_bpsastate"></span><span id="UFS_BPSASTATE"></span>**UFS\_bPSAState**
</dt> <dd>

Specifies the current Product State Awareness (PSA) State.



| Value | State            | Description                                                                                                                                                  |
|-------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00  | Off              | PSA feature is off.                                                                                                                                          |
| 0x01  | Pre-solder       | PSA feature is on and the device is in a pre-soldering state.                                                                                                |
| 0x02  | Loading Complete | The PSA feature is on. The host will set to this value after the host finished writing data during pre-soldering state.                                      |
| 0x03  | Soldered         | PSA feature is no longer available. Set by the Device to indicate it is in a post-soldering state. This attribute is locked after it is in ‘Soldered’ state. |



 

</dd> <dt>

<span id="UFS_dPSADataSize"></span><span id="ufs_dpsadatasize"></span><span id="UFS_DPSADATASIZE"></span>**UFS\_dPSADataSize**
</dt> <dd>

Specifies the amount of data that the host plans to load to all logical units with **bPSASensitive** set to 1.

</dd> </dl>

## Remarks

**UFS\_bCurrentPowerMode** is the only attribute the device is required to return in any power mode. If the device is not in Active power mode or Idle power mode, a **QUERY REQUEST UPIU** to access descriptors, flags, or attributes other than **bCurrentPowerMode** may fail.

**UFS\_bDeviceFFUStatu**s value is kept after power cycle, hardware reset or any other type of reset. This attribute may change value when a microcode activation event occurs.

**UFS\_bMaxDataInSize** is equal to **bMaxInBufferSize** when a UFS device is shipped.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ufs.h</dt> </dl> |



## See also

<dl> <dt>

[**UFS\_CONFIG\_DESCRIPTOR**](ufs-config-descriptor.md)
</dt> <dt>

[**UFS\_DEVICE\_HEALTH\_DESCRIPTOR**](ufs-device-health-descriptor.md)
</dt> <dt>

[**UFS\_DEVICE\_DESCRIPTOR**](ufs-device-descriptor.md)
</dt> <dt>

[**UFS\_GEOMETRY\_DESCRIPTOR**](ufs-geometry-descriptor.md)
</dt> <dt>

[**UFS\_INTERCONNECT\_DESCRIPTOR**](ufs-interconnect-descriptor.md)
</dt> <dt>

[**UFS\_POWER\_DESCRIPTOR**](ufs-power-descriptor.md)
</dt> <dt>

[**UFS\_RPMB\_UNIT\_DESCRIPTOR**](ufs-rpmb-unit-descriptor.md)
</dt> <dt>

[**UFS\_STRING\_DESCRIPTOR**](ufs-string-descriptor.md)
</dt> <dt>

[**UFS\_UNIT\_CONFIG\_DESCRIPTOR**](ufs-unit-config-descriptor.md)
</dt> <dt>

[**UFS\_UNIT\_DESCRIPTOR**](ufs-unit-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_ATTRIBUTES_DESCRIPTOR%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






