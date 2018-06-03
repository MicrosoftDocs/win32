---
title: UFS\_GEOMETRY\_DESCRIPTOR structure
description: UFS\_GEOMETRY\_DESCRIPTOR describes a device's geometric parameters.
ms.assetid: DD3AEB66-E36B-4F18-AFEC-D344132D4B8C
keywords:
- UFS_GEOMETRY_DESCRIPTOR structure Storage Devices
- PUFS_GEOMETRY_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- UFS_GEOMETRY_DESCRIPTOR
api_location:
- Ufs.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# UFS\_GEOMETRY\_DESCRIPTOR structure

**UFS\_GEOMETRY\_DESCRIPTOR** describes a device's geometric parameters.

## Syntax


```C++
typedef struct _UFS_GEOMETRY_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR bMediaTechnology;
  UCHAR Reserved1;
  UCHAR  qTotalRawDeviceCapacity[8];
  UCHAR bMaxNumberLU;
  UCHAR dSegmentSize[4];
  UCHAR bAllocationUnitSize;
  UCHAR bMinAddrBlockSize;
  UCHAR bOptimalReadBlockSize;
  UCHAR bOptimalWriteBlockSize;
  UCHAR bMaxInBufferSize;
  UCHAR bMaxOutBufferSize;
  UCHAR bRPMB_ReadWriteSize;
  UCHAR bDynamicCapacityResourcePolicy;
  UCHAR bDataOrdering;
  UCHAR bMaxContexIDNumber;
  UCHAR bSysDataTagUnitSize;
  UCHAR bSysDataTagResSize;
  UCHAR bSupportedSecRTypes;
  UCHAR wSupportedMemoryTypes[2];
  UCHAR dSystemCodeMaxNAllocU[4];
  UCHAR wSystemCodeCapAdjFac[2];
  UCHAR dNonPersistMaxNAllocU[4];
  UCHAR wNonPersistCapAdjFac[2];
  UCHAR dEnhanced1MaxNAllocU[4];
  UCHAR wEnhanced1CapAdjFac[2];
  UCHAR dEnhanced2MaxNAllocU[4];
  UCHAR wEnhanced2CapAdjFac[2];
  UCHAR dEnhanced3MaxNAllocU[4];
  UCHAR wEnhanced3CapAdjFac[2];
  UCHAR dEnhanced4MaxNAllocU[4];
  UCHAR wEnhanced4CapAdjFac[2];
  UCHAR dOptimalLogicalBlockSize[4];
} UFS_GEOMETRY_DESCRIPTOR, *PUFS_GEOMETRY_DESCRIPTOR;
```



## Members

<dl> <dt>

**bLength**
</dt> <dd>

Specifies the length of the descriptor.

</dd> <dt>

**bDescriptorIDN**
</dt> <dd>

Specifies the type of the descriptor. This descriptor will have a value of **UFS\_DESC\_GEOMETRY\_IDN**.

</dd> <dt>

**bMediaTechnology**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

 **qTotalRawDeviceCapacity**
</dt> <dd>

Specifies the total raw device capacity. Expressed in units of 512 bytes.

</dd> <dt>

**bMaxNumberLU**
</dt> <dd>

Specifies the maximum number of logical unit(s) supported by the UFS (Universal Flash Storage). Contains one of the following values:



| Value        | Description              |
|--------------|--------------------------|
| 0x00         | 8 logical units.         |
| 0x01         | 32 logical units.        |
| Other Values | Reserved for future use. |



 

</dd> <dt>

**dSegmentSize**
</dt> <dd>

Specifies the segment size of the device in units of 512 bytes.

</dd> <dt>

**bAllocationUnitSize**
</dt> <dd>

Specifies the allocation unit size in number of segments.

</dd> <dt>

**bMinAddrBlockSize**
</dt> <dd>

Specifies the minimum addressable block size in units of 512 bytes. The minium size is 4 KB or a value of 0x08.

</dd> <dt>

**bOptimalReadBlockSize**
</dt> <dd>

Specifies the optimal read block size in units of 512 bytes.

</dd> <dt>

**bOptimalWriteBlockSize**
</dt> <dd>

Specifies the optimal write block size in units of 512 bytes. **bOptimalWriteBlockSize** is equal to or greater than **bMinAddrBlockSize**.

</dd> <dt>

**bMaxInBufferSize**
</dt> <dd>

Specifies the max size of the data-in buffer in units of 512 bytes. The minium size is 4 KB or a value of 0x08.

</dd> <dt>

**bMaxOutBufferSize**
</dt> <dd>

Specifies the max size of the data-out buffer in units of 512 bytes. The minium size is 4 KB or a value of 0x08.

</dd> <dt>

**bRPMB\_ReadWriteSize**
</dt> <dd>

Specifies the maximum number of Replay Protected Memory Block (RPMB) frames allowed in Security Protocol In and Security Protocol Out. Each frame is 256-bytes.

</dd> <dt>

**bDynamicCapacityResourcePolicy**
</dt> <dd>

Specifies a device's spare blocks resource management policy. Contains one of the following values:



| Value | Description                                                  |
|-------|--------------------------------------------------------------|
| 0x00  | Spare blocks resource management policy is per logical unit. |
| 0x01  | Spare blocks resource management policy is per memory type.  |



 

</dd> <dt>

**bDataOrdering**
</dt> <dd>

Specifies if a device supports out-of-order data transfer. Contains one of the following values:



| Value            | Description                                  |
|------------------|----------------------------------------------|
| 0x00             | Out-of-order data transfer is not supported. |
| 0x01             | Out-of-order data transfer is supported.     |
| All other values | Reserved for future use.                     |



 

</dd> <dt>

**bMaxContexIDNumber**
</dt> <dd>

Specifies the max number of contexts supported by a device. This number must be greater than 5.

</dd> <dt>

**bSysDataTagUnitSize**
</dt> <dd>

Specifies the system data tag unit size.

</dd> <dt>

**bSysDataTagResSize**
</dt> <dd>

Specifies the maximum size in bytes allocated by the device to handle system data.

</dd> <dt>

**bSupportedSecRTypes**
</dt> <dd>

Specifies the supported Secure Removal types. The first 3 bits of the variable are flags that represent different supported Secure Removal types.



| Bit | Description                                                                                                           |
|-----|-----------------------------------------------------------------------------------------------------------------------|
| 0   | Information removed with an erase of the physical memory.                                                             |
| 1   | Information removed by overwriting the addressed locations with a single character followed by an erase.              |
| 2   | Information removed by overwriting the addressed locations with a character, its complement, then a random character. |
| 3   | Information removed using a vendor-defined mechanism.                                                                 |
| 4-7 | Reserved for future use.                                                                                              |



 

</dd> <dt>

**wSupportedMemoryTypes**
</dt> <dd>

Specifies the supported memory types in a bitmap.



| Bit  | Description                                |
|------|--------------------------------------------|
| 0    | A normal memory type is supported.         |
| 1    | A system code memory type is supported.    |
| 2    | A non-persistent memory type is supported. |
| 3    | Enhanced memory type 1 is supported.       |
| 4    | Enhanced memory type 2 is supported.       |
| 5    | Enhanced memory type 3 is supported.       |
| 6    | Enhanced memory type 4 is supported.       |
| 7-14 | Reserved for future use.                   |
| 15   | A RPMB memory type is supported.           |



 

</dd> <dt>

**dSystemCodeMaxNAllocU**
</dt> <dd>

Specifies the maximum number of allocation units for the System Code for a device.

</dd> <dt>

**wSystemCodeCapAdjFac**
</dt> <dd>

Species the Capacity Adjustment Factor for the System Code memory type.

</dd> <dt>

**dNonPersistMaxNAllocU**
</dt> <dd>

Species the maximum number of Allocation Units for a non-persistent memory type.

</dd> <dt>

**wNonPersistCapAdjFac**
</dt> <dd>

Specifies the capacity adjustment factor for the non-persistent memory type.

</dd> <dt>

**dEnhanced1MaxNAllocU**
</dt> <dd>

specifies the max number of Allocation Units for the enhanced memory type 1.

</dd> <dt>

**wEnhanced1CapAdjFac**
</dt> <dd>

specifies the Capacity Adjustment Factor for the enhanced memory type 1.

</dd> <dt>

**dEnhanced2MaxNAllocU**
</dt> <dd>

specifies the max number of Allocation Units for the enhanced memory type 2.

</dd> <dt>

**wEnhanced2CapAdjFac**
</dt> <dd>

specifies the Capacity Adjustment Factor for the enhanced memory type 2.

</dd> <dt>

**dEnhanced3MaxNAllocU**
</dt> <dd>

specifies the max number of Allocation Units for the enhanced memory type 3.

</dd> <dt>

**wEnhanced3CapAdjFac**
</dt> <dd>

specifies the Capacity Adjustment Factor for the enhanced memory type 3.

</dd> <dt>

**dEnhanced4MaxNAllocU**
</dt> <dd>

specifies the max number of Allocation Units for the enhanced memory type 4.

</dd> <dt>

**wEnhanced4CapAdjFac**
</dt> <dd>

specifies the Capacity Adjustment Factor for the enhanced memory type 4.

</dd> <dt>

**dOptimalLogicalBlockSize**
</dt> <dd>

Specifies the optimal logical block size.

</dd> </dl>

## Remarks

If the size of the data transferred exceeds the number of frames **bRPMB\_ReadWriteSize**, it will be done in multiple Security commands.

The Capacity Adjustment Factor value for a normal memory type is equal to 1.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ufs.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_GEOMETRY_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





