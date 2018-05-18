---
title: UFS\_CONFIG\_DESCRIPTOR structure
description: The UFS\_CONFIG\_DESCRIPTOR structure describes the modifiable values of the default device configuration set by the manufacturer.
ms.assetid: 'B65A2268-6959-4630-97DA-C0CFD37D9174'
keywords: ["UFS_CONFIG_DESCRIPTOR structure Storage Devices", "PUFS_CONFIG_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- UFS_CONFIG_DESCRIPTOR
api_location:
- Ufs.h
api_type:
- HeaderDef
---

# UFS\_CONFIG\_DESCRIPTOR structure

The **UFS\_CONFIG\_DESCRIPTOR** structure describes the modifiable values of the default device configuration set by the manufacturer.

## Syntax


```C++
typedef struct _UFS_CONFIG_DESCRIPTOR {
  UCHAR                       bLength;
  UCHAR                       bDescriptorIDN;
  UCHAR                       Reserved1;
  UCHAR                       bBootEnable;
  UCHAR                       bDescrAccessEn;
  UCHAR                       bInitPowerMode;
  UCHAR                       bHighPriorityLUN;
  UCHAR                       bSecureRemovalType;
  UCHAR                        bInitActiveICCLevel;
  UCHAR                       wPeriodicRTCUpdate[2];
  UCHAR                        Reserved2[5];
   UFS_UNIT_CONFIG_DESCRIPTOR UnitConfig[UFS_MAX_NUM_LU];
} UFS_CONFIG_DESCRIPTOR, *PUFS_CONFIG_DESCRIPTOR;
```



## Members

<dl> <dt>

**bLength**
</dt> <dd>

Specifies the size, in bytes, of this descriptor.

</dd> <dt>

**bDescriptorIDN**
</dt> <dd>

Specifies the Configuration Descriptor Type Identifier. This descriptor will have a value of **UFS\_DESC\_CONFIGURATION\_IDN**.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**bBootEnable**
</dt> <dd>

Specifies if a device's boot feature is enabled.

</dd> <dt>

**bDescrAccessEn**
</dt> <dd>

Enables access to the Device Descriptor after the partial initialization phase of the boot sequence.

</dd> <dt>

**bInitPowerMode**
</dt> <dd>

Specifies the power mode after device initialization or hardware reset.

</dd> <dt>

**bHighPriorityLUN**
</dt> <dd>

**bHighPriorityLUN** configures the high priority logical unit.

</dd> <dt>

**bSecureRemovalType**
</dt> <dd>

Configures the secure removal type.

</dd> <dt>

 **bInitActiveICCLevel**
</dt> <dd>

Configures the ICC level in Active mode after device initialization or hardware reset.

</dd> <dt>

**wPeriodicRTCUpdate**
</dt> <dd>

Specifies the frequency and method of real-time clock updates.

</dd> <dt>

 **Reserved2**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**UnitConfig**
</dt> <dd>

Contains the configurable parameters of the Unit Descriptor.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ufs.h</dt> </dl> |



## See also

<dl> <dt>

[**UFS\_UNIT\_CONFIG\_DESCRIPTOR**](ufs-unit-config-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_CONFIG_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






