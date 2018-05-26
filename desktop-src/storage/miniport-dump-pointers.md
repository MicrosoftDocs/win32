---
title: MINIPORT\_DUMP\_POINTERS structure
description: A Storport miniport driver uses this structure to support the SCSI\_REQUEST\_BLOCK (SRB) function code SRB\_FUNCTION\_DUMP\_POINTERS.
ms.assetid: a61da8e7-6db0-4d89-bf68-8fa74c284720
keywords:
- MINIPORT_DUMP_POINTERS structure Storage Devices
- PMINIPORT_DUMP_POINTERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MINIPORT_DUMP_POINTERS
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MINIPORT\_DUMP\_POINTERS structure

A Storport miniport driver uses this structure to support the [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) (SRB) function code SRB\_FUNCTION\_DUMP\_POINTERS. When a miniport driver receives this kind of SRB, the **DataBuffer** SRB member points to a **MINIPORT\_DUMP\_POINTERS** structure. This SRB is sent to the miniport driver that is used to control the disk that holds the crash dump data after the SRB was returned from the miniport driver's [**HwStorInitialize**](hwstorinitialize.md) routine. Virtual miniport drivers are required to support SRB\_FUNCTION\_DUMP\_POINTERS.

## Syntax


```C++
typedef struct _MINIPORT_DUMP_POINTERS {
  USHORT                 Version;
  USHORT                 Size;
  WCHAR                  DriverName[DUMP_MINIPORT_NAME_LENGTH];
  struct _ADAPTER_OBJECT  *AdapterObject;
  PVOID                  MappedRegisterBase;
  ULONG                  CommonBufferSize;
  PVOID                  MiniportPrivateDumpData;
  ULONG                  SystemIoBusNumber;
  INTERFACE_TYPE         AdapterInterfaceType;
  ULONG                  MaximumTransferLength;
  ULONG                  NumberOfPhysicalBreaks;
  ULONG                  AlignmentMask;
  ULONG                  NumberOfAccessRanges;
  ACCESS_RANGE           (*AccessRanges)[];
  UCHAR                  NumberOfBuses;
  BOOLEAN                Master;
  BOOLEAN                MapBuffers;
  UCHAR                  MaximumNumberOfTargets;
} MINIPORT_DUMP_POINTERS, *PMINIPORT_DUMP_POINTERS;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Set to DUMP\_MINIPORT\_VERSION\_1.

</dd> <dt>

**Size**
</dt> <dd>

Set to sizeof(MINIPORT\_DUMP\_POINTERS).

</dd> <dt>

**DriverName**
</dt> <dd>

The wide-character name of the miniport driver without path information (for example, Miniport.sys).

</dd> <dt>

**AdapterObject**
</dt> <dd>

Set to **NULL**.

</dd> <dt>

**MappedRegisterBase**
</dt> <dd>

Set to zero.

</dd> <dt>

**CommonBufferSize**
</dt> <dd>

The size of the common buffer that is required. The size must not be greater than 64 KB (65,536 bytes).

</dd> <dt>

**MiniportPrivateDumpData**
</dt> <dd>

The context that is to be passed to the miniport driver's [**HwStorFindAdapter**](hwstorfindadapter.md) routine during the crash dump. The context is passed in the **Reserved** member or, starting with Windows 8, the **MiniportDumpData** member of the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure.

</dd> <dt>

**SystemIoBusNumber**
</dt> <dd>

Specifies the system-assigned number of the I/O bus to which the HBA is connected. The Storport driver initializes this member. Miniport drivers that work with the Storport driver must not change this member. For more information, see the **SystemIoBusNumber** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

**AdapterInterfaceType**
</dt> <dd>

Identifies the I/O bus interface. The Storport driver initializes this member. Miniport drivers that work with the Storport driver must not modify this member. For more information, see the **AdapterInterfaceType** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

**MaximumTransferLength**
</dt> <dd>

Specifies the maximum number of bytes the HBA can transfer in a single transfer operation in crashdump mode. By default, the value of this member is SP\_UNINITIALIZED\_VALUE, which indicates an unlimited maximum transfer size. This value is specific to the dump operation of the miniport and may differ from the value in the **MaximumTransferLength** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

**NumberOfPhysicalBreaks**
</dt> <dd>

Specifies the maximum number of breaks between address ranges that a data buffer can have to create scatter/gather lists. In other words, the number of scatter/gather list entries that the adapter can support minus one. For more information, see the **NumberOfPhysicalBreaks** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

**AlignmentMask**
</dt> <dd>

Contains a mask that indicates the alignment restrictions for buffers that are required by the HBA for transfer operations. Valid mask values are also restricted by characteristics of the memory managers on different versions of the Microsoft Windows operating systems. The valid mask values are 0 (byte aligned), 0x1 (word aligned), 0x3 (DWORD aligned), and 0x7 (double DWORD aligned). The miniport driver should set this mask if the HBA supports scatter/gather. The same considerations apply to the **AlignmentMask** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

**NumberOfAccessRanges**
</dt> <dd>

Specifies the number of **AccessRanges** elements in the array. For more information, see the **NumberOfAccessRanges** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

**(\*AccessRanges)**
</dt> <dd>

A pointer to an array of ACCESS\_RANGE-type elements. The Storport driver initializes this member. Miniport drivers that work with the Storport driver must not change this member. For more information, see the **AccessRanges** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

**NumberOfBuses**
</dt> <dd>

Specifies the number of buses that are controlled by the adapter. By default, the value of this member is zero. For more information, see the **NumberOfBuses** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

**Master**
</dt> <dd>

Indicates, when **TRUE**, that the HBA is a bus master. The Storport driver initializes this member to **TRUE**, because its miniport drivers must support bus-mastering DMA. Miniport drivers that work with the Storport driver must not change this value. For more information, see the **Master** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> <dt>

**MapBuffers**
</dt> <dd>

Indicates whether the Storport driver maps SRB data buffer addresses to system virtual addresses. For more information, see the **MapBuffers** member of [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md).

</dd> <dt>

**MaximumNumberOfTargets**
</dt> <dd>

Specifies the number of target peripherals that the adapter can control. For more information, see the **MaximumNumberOfTargets** member of [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md).

</dd> </dl>

## Remarks

Starting with Windows 8, physical minport drivers can optionally support SRB\_FUNCTION\_DUMP\_POINTERS. If a physical miniport supports this function, it must set the STOR\_FEATURE\_DUMP\_POINTERS flag in the **FeatureSupport** member of the [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md) structure before calling [**StorPortInitialize**](storportinitialize.md). Physical miniports are required to set at least the **Version** and **Size** members of **MINIPORT\_DUMP\_POINTERS**. Also, if different from the value given in [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md), the **MaximumTransferLength** member is required for a physical miniport.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**HwStorInitialize**](hwstorinitialize.md)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MINIPORT_DUMP_POINTERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






