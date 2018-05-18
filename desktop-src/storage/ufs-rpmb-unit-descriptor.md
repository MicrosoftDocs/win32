---
title: UFS\_RPMB\_UNIT\_DESCRIPTOR structure
description: The UFS\_RPMB\_UNIT\_DESCRIPTOR structure describes the contents of a Replay Protected Memory Block (RBMB) Unit.
ms.assetid: '19A066BD-1099-475C-BF81-F1BE7C7778E5'
keywords: ["UFS_RPMB_UNIT_DESCRIPTOR structure Storage Devices", "PUFS_RPMB_UNIT_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- UFS_RPMB_UNIT_DESCRIPTOR
api_location:
- Ufs.h
api_type:
- HeaderDef
---

# UFS\_RPMB\_UNIT\_DESCRIPTOR structure

The **UFS\_RPMB\_UNIT\_DESCRIPTOR** structure describes the contents of a Replay Protected Memory Block (RBMB) Unit.

## Syntax


```C++
typedef struct _UFS_RPMB_UNIT_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR bUnitIndex;
  UCHAR bLUEnable;
  UCHAR bBootLUNID;
  UCHAR bLUWriteProtect;
  UCHAR bLUQueueDepth;
  UCHAR bPSASensitive;
  UCHAR bMemoryType;
  UCHAR Reserved;
  UCHAR  bLogicalBlockSize;
  UCHAR qLogicalBlockCount[8];
  UCHAR dEraseBlockSize[4];
  UCHAR bProvisioningType;
  UCHAR qPhyMemResourceCount[8];
  UCHAR Reserved[3];
} UFS_RPMB_UNIT_DESCRIPTOR, *PUFS_RPMB_UNIT_DESCRIPTOR;
```



## Members

<dl> <dt>

**bLength**
</dt> <dd>

Specifies the length, in bytes, of this descriptor.

</dd> <dt>

**bDescriptorIDN**
</dt> <dd>

Specifies the type of the descriptor. This descriptor will have a value of **UFS\_DESC\_UNIT\_IDN**.

</dd> <dt>

**bUnitIndex**
</dt> <dd>

Specifies unit index

</dd> <dt>

**bLUEnable**
</dt> <dd>

Specifies if the logic unit number (LUN) is enabled. If **bLUEnable** is equal to 0x00, the logical unit is disabled.

</dd> <dt>

**bBootLUNID**
</dt> <dd>

Specifies the boot LUN id.

</dd> <dt>

**bLUWriteProtect**
</dt> <dd>

Specifies if the logical unit is write-protected. Contains one of the following values:



| Value | Description                                      |
|-------|--------------------------------------------------|
| 0x00  | The logical unit is not write protected.         |
| 0x01  | The logical unit is write protected.             |
| 0x02  | The logical unit is permanently write protected. |



 

</dd> <dt>

**bLUQueueDepth**
</dt> <dd>

Specifies the logical unit queue depth. Can be any value from 0x00 to 0xff.

</dd> <dt>

**bPSASensitive**
</dt> <dd>

Specifies if the logical unit is sensitive to soldering. Contains one of the following values:



| Value | Description                                     |
|-------|-------------------------------------------------|
| 0x00  | The logical unit is not sensitive to soldering. |
| 0x01  | The logical unit is sensitive to soldering.     |



 

</dd> <dt>

**bMemoryType**
</dt> <dd>

Specifies the desired memory type. Equal to 0x0F.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

 **bLogicalBlockSize**
</dt> <dd>

Specifies the logical block size of the descriptor.

</dd> <dt>

**qLogicalBlockCount**
</dt> <dd>

Specifies the total number of addressable logical blocks in the logical unit.

</dd> <dt>

**dEraseBlockSize**
</dt> <dd>

Specifies the erase block size.

</dd> <dt>

**bProvisioningType**
</dt> <dd>

Specifies the provisioning type.

</dd> <dt>

**qPhyMemResourceCount**
</dt> <dd>

Specifies the total physical memory resources available in the logical unit.

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



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_RPMB_UNIT_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





