---
title: IDEREGS structure
description: The IDEREGS structure is used to report the contents of the IDE controller registers.
ms.assetid: 20897336-e032-4aa7-be5f-47704c6d1d12
keywords:
- IDEREGS structure Storage Devices
- PIDEREGS structure pointer Storage Devices
- LPIDEREGS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IDEREGS
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IDEREGS structure

The IDEREGS structure is used to report the contents of the IDE controller registers.

## Syntax


```C++
typedef struct _IDEREGS {
  UCHAR bFeaturesReg;
  UCHAR bSectorCountReg;
  UCHAR bSectorNumberReg;
  UCHAR bCylLowReg;
  UCHAR bCylHighReg;
  UCHAR bDriveHeadReg;
  UCHAR bCommandReg;
  UCHAR bReserved;
} IDEREGS, *PIDEREGS, *LPIDEREGS;
```



## Members

<dl> <dt>

**bFeaturesReg**
</dt> <dd>

Holds the contents of the Features register. This register is used to specify Self-Monitoring Analysis and Reporting Technology (SMART) commands. This member can hold any of the following values:



| Feature                                   | Meaning                                                                                                                                                    |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| READ\_ATTRIBUTES<br/>               | Retrieve the device attributes<br/>                                                                                                                  |
| READ\_THRESHOLDS.<br/>              | Retrieve threshold values that indicate when a drive is about to fail.<br/>                                                                          |
| ENABLE\_DISABLE\_AUTOSAVE.<br/>     | Enables the optional attribute autosave feature of the device when set to 1. Disables this feature when set to 0..<br/>                              |
| SAVE\_ATTRIBUTE\_VALUES.<br/>       | Instructs the device to save its attribute values to the device's non-volatile memory.<br/>                                                          |
| EXECUTE\_OFFLINE\_DIAGS<br/>        | Causes the device to begin collecting SMART data in off-line mode or execute a self-diagnostic test routine in either captive or off-line mode.<br/> |
| SMART\_READ\_LOG<br/>               | Retrieves the indicated log.<br/>                                                                                                                    |
| SMART\_WRITE\_LOG<br/>              | Writes the indicated number of 512-byte data sectors to the indicated log.<br/>                                                                      |
| ENABLE\_SMART<br/>                  | Enables SMART functionality on the device.<br/>                                                                                                      |
| DISABLE\_SMART<br/>                 | Disables SMART functionality on the device.<br/>                                                                                                     |
| RETURN\_SMART\_STATUS<br/>          | Retrieves the reliability status of the device.<br/>                                                                                                 |
| ENABLE\_DISABLE\_AUTO\_OFFLINE<br/> | Enables offline mode when set to 1. Disables offline mode when 0.<br/>                                                                               |



 

</dd> <dt>

**bSectorCountReg**
</dt> <dd>

Holds the contents of the sector count register. IDE sector count register.

</dd> <dt>

**bSectorNumberReg**
</dt> <dd>

Holds the contents of the sector number register.

</dd> <dt>

**bCylLowReg**
</dt> <dd>

Holds the contents of the IDE low-order cylinder register.

</dd> <dt>

**bCylHighReg**
</dt> <dd>

Holds the contents of the IDE high-order cylinder register.

</dd> <dt>

**bDriveHeadReg**
</dt> <dd>

Holds the contents of the IDE drive/head register.

</dd> <dt>

**bCommandReg**
</dt> <dd>

Holds the contents of the IDE command register.

</dd> <dt>

**bReserved**
</dt> <dd>

Reserved for future use. Should always be zero.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**ATA\_PASS\_THROUGH\_EX**](ata-pass-through-ex.md)
</dt> <dt>

[**ATA\_PASS\_THROUGH\_DIRECT**](ata-pass-through-direct.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDEREGS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






