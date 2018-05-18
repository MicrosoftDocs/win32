---
title: UFS\_UNIT\_CONFIG\_DESCRIPTOR structure
description: The UFS\_UNIT\_CONFIG\_DESCRIPTOR structure describes the user configurable parameters within the UFS\_CONFIG\_DESCRIPTOR.
ms.assetid: '09CBAD0A-CBDC-464E-908C-BF142D515969'
keywords: ["UFS_UNIT_CONFIG_DESCRIPTOR structure Storage Devices", "PUFS_UNIT_CONFIG_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- UFS_UNIT_CONFIG_DESCRIPTOR
api_location:
- Ufs.h
api_type:
- HeaderDef
---

# UFS\_UNIT\_CONFIG\_DESCRIPTOR structure

The **UFS\_UNIT\_CONFIG\_DESCRIPTOR** structure describes the user configurable parameters within the [**UFS\_CONFIG\_DESCRIPTOR**](ufs-config-descriptor.md).

## Syntax


```C++
typedef struct _UFS_UNIT_CONFIG_DESCRIPTOR {
  UCHAR bLUEnable;
  UCHAR bBootLunID;
  UCHAR bLUWriteProtect;
  UCHAR bMemoryType;
  UCHAR dNumAllocUnits[4];
  UCHAR bDataReliability;
  UCHAR bLogicalBlockSize;
  UCHAR bProvisioningType;
  UCHAR wContextCapabilities[2];
  UCHAR Reserved[3];
} UFS_UNIT_CONFIG_DESCRIPTOR, *PUFS_UNIT_CONFIG_DESCRIPTOR;
```



## Members

<dl> <dt>

**bLUEnable**
</dt> <dd>

Specifies if the logical unit is enabled.

</dd> <dt>

**bBootLunID**
</dt> <dd>

Specifies if the logical unit is a bootable logical unit.

</dd> <dt>

**bLUWriteProtect**
</dt> <dd>

Specifies if the Logical Unit is write protected.

</dd> <dt>

**bMemoryType**
</dt> <dd>

Specifies the Memory type of the device.



| Value            | Description                |
|------------------|----------------------------|
| 0x00             | Normal Memory type         |
| 0x01             | System code memory type    |
| 0x02             | Non-Persistent memory type |
| 0x03             | Enhanced memory type 1     |
| 0x04             | Enhanced memory type 2     |
| 0x05             | Enhanced memory type 3     |
| 0x06             | Enhanced memory type 4     |
| All other values | Reserved for future use.   |



 

</dd> <dt>

**dNumAllocUnits**
</dt> <dd>

Specifies the number of allocation units assigned to the logical unit.

</dd> <dt>

**bDataReliability**
</dt> <dd>

**bDataReliability** defines the device behavior when a power failure occurs during a write operation to the logical unit:



| Value            | Description                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| 0x00             | The logical unit is not protected. Logical unit's entire data may be lost as a result of a power failure during a write operation |
| 0x01             | The logical unit is protected. Logical unit's data is protected against power failure.                                            |
| All other values | Reserved for future use.                                                                                                          |



 

</dd> <dt>

**bLogicalBlockSize**
</dt> <dd>

Specifies the logical block size.

</dd> <dt>

**bProvisioningType**
</dt> <dd>

Specifies the provisioning type.



| Value            | Description                                                              |
|------------------|--------------------------------------------------------------------------|
| 0x00             | Thin Provisioning is disabled (default)                                  |
| 0x02             | Thin Provisioning is enabled and Thin Provisioning Read Zeros (TPRZ) = 0 |
| 0x03             | Thin Provisioning is enabled and TPRZ = 1                                |
| All other values | Reserved for future use.                                                 |



 

</dd> <dt>

**wContextCapabilities**
</dt> <dd>

Specifies the Context Capabilities.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ufs.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_UNIT_CONFIG_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





