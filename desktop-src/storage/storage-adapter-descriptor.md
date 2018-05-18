---
title: STORAGE\_ADAPTER\_DESCRIPTOR structure
description: The STORAGE\_ADAPTER\_DESCRIPTOR structure is used in conjunction with the IOCTL\_STORAGE\_QUERY\_PROPERTY request to retrieve the storage adapter descriptor data for a device.
ms.assetid: '83ef2a1a-f95e-4b05-8911-e5e900192630'
keywords: ["STORAGE_ADAPTER_DESCRIPTOR structure Storage Devices", "PSTORAGE_ADAPTER_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_ADAPTER_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_ADAPTER\_DESCRIPTOR structure

The **STORAGE\_ADAPTER\_DESCRIPTOR** structure is used in conjunction with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to retrieve the storage adapter descriptor data for a device.

## Syntax


```C++
typedef struct _STORAGE_ADAPTER_DESCRIPTOR {
  ULONG   Version;
  ULONG   Size;
  ULONG   MaximumTransferLength;
  ULONG   MaximumPhysicalPages;
  ULONG   AlignmentMask;
  BOOLEAN AdapterUsesPio;
  BOOLEAN AdapterScansDown;
  BOOLEAN CommandQueueing;
  BOOLEAN AcceleratedTransfer;
  UCHAR   BusType;
  USHORT  BusMajorVersion;
  USHORT  BusMinorVersion;
  UCHAR   SrbType;
  UCHAR   AddressType;
} STORAGE_ADAPTER_DESCRIPTOR, *PSTORAGE_ADAPTER_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the version of the structure **STORAGE\_ADAPTER\_DESCRIPTOR**. The value of this member will change as members are added to the structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the descriptor, in bytes.

</dd> <dt>

**MaximumTransferLength**
</dt> <dd>

Specifies the maximum number of bytes the host bus adapter (HBA) can transfer in a single operation.

</dd> <dt>

**MaximumPhysicalPages**
</dt> <dd>

Specifies the maximum number of discontinuous physical pages the HBA can manage in a single transfer (in other words, the extent of its scatter/gather support).

</dd> <dt>

**AlignmentMask**
</dt> <dd>

Specifies the HBA's alignment requirements for transfers. A storage class driver sets the **AlignmentRequirement** field in its device objects to this value. The alignment mask indicates alignment restrictions for buffers required by the HBA for transfer operations. The valid mask values are 0 (byte aligned), 1 (word aligned), 3 (DWORD aligned), and 7 (double DWORD aligned).

</dd> <dt>

**AdapterUsesPio**
</dt> <dd>

Indicates when **TRUE** that the HBA uses Programmed Input/Output (PIO) and requires the use of system-space virtual addresses mapped to physical memory for data buffers. When **FALSE**, the HBA does not use PIO.

</dd> <dt>

**AdapterScansDown**
</dt> <dd>

Indicates when **TRUE** that the HBA scans down for BIOS devices, that is, the HBA begins scanning with the highest device number rather than the lowest. When **FALSE**, the HBA begins scanning with the lowest device number. This member is reserved for legacy miniport drivers.

</dd> <dt>

**CommandQueueing**
</dt> <dd>

Indicates when **TRUE** that the HBA supports SCSI-tagged queuing and/or per-logical-unit internal queues, or the non-SCSI equivalent. When **FALSE**, the HBA neither supports SCSI-tagged queuing nor per-logical-unit internal queues.

</dd> <dt>

**AcceleratedTransfer**
</dt> <dd>

Indicates when **TRUE** that the HBA supports synchronous transfers as a way of speeding up I/O. When **FALSE**, the HBA does not support synchronous transfers as a way of speeding up I/O.

</dd> <dt>

**BusType**
</dt> <dd>

Specifies a value of type [**STORAGE\_BUS\_TYPE**](storage-bus-type.md) that indicates the type of bus to which the device is connected.

</dd> <dt>

**BusMajorVersion**
</dt> <dd>

Specifies the major version number, if any, of the HBA.

</dd> <dt>

**BusMinorVersion**
</dt> <dd>

Specifies the minor version number, if any, of the HBA.

</dd> <dt>

**SrbType**
</dt> <dd>

Specifies the SCSI request block (SRB) type used by the HBA.



| Value                                                                                                                                                                                                               | Meaning                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="SRB_TYPE_SCSI_REQUEST_BLOCK"></span><span id="srb_type_scsi_request_block"></span><dl> <dt>**SRB\_TYPE\_SCSI\_REQUEST\_BLOCK**</dt> </dl>          | The HBA uses SCSI request blocks.<br/>          |
| <span id="SRB_TYPE_STORAGE_REQUEST_BLOCK"></span><span id="srb_type_storage_request_block"></span><dl> <dt>**SRB\_TYPE\_STORAGE\_REQUEST\_BLOCK**</dt> </dl> | The HBA uses extended SCSI request blocks.<br/> |



 

This member is valid starting with Windows 8.

</dd> <dt>

**AddressType**
</dt> <dd>

Specifies the address type of the HBA.



| Value                                                                                                                                                                                               | Meaning                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="STORAGE_ADDRESS_TYPE_BTL8"></span><span id="storage_address_type_btl8"></span><dl> <dt>**STORAGE\_ADDRESS\_TYPE\_BTL8**</dt> </dl> | The HBA uses 8-bit bus, target, and LUN addressing.<br/> |



 

This member is valid starting with Windows 8.

</dd> </dl>

## Remarks

Storage class drivers issue a device-control request with the I/O control code [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to retrieve this structure, which contains configuration information from the HBA for data transfer operations. The structure can be retrieved either from the device object for the bus or from a functional device object (FDO), which forwards the request to the underlying bus.

If excessive protocol errors occur on an HBA that supports synchronous transfers (**AcceleratedTransfer** is **TRUE**), the storage class driver can disable synchronous transfers by setting SRB\_FLAGS\_DISABLE\_SYNCH\_TRANSFER in SRBs.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)
</dt> <dt>

[**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md)
</dt> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_DESCRIPTOR\_HEADER**](storage-descriptor-header.md)
</dt> <dt>

[**STORAGE\_DEVICE\_ID\_DESCRIPTOR**](storage-device-id-descriptor.md)
</dt> <dt>

[**STORAGE\_ADAPTER\_DESCRIPTOR**](storage-adapter-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_ADAPTER_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






