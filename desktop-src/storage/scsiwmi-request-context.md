---
title: SCSIWMI\_REQUEST\_CONTEXT structure
description: A SCSIWMI\_REQUEST\_CONTEXT structure contains context information for a WMI SRB.
ms.assetid: 524150d8-d4a7-4b61-89c4-0074c938559b
keywords:
- SCSIWMI_REQUEST_CONTEXT structure Storage Devices
- PSCSIWMI_REQUEST_CONTEXT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SCSIWMI_REQUEST_CONTEXT
api_location:
- scsiwmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# SCSIWMI\_REQUEST\_CONTEXT structure

A SCSIWMI\_REQUEST\_CONTEXT structure contains context information for a WMI SRB.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct {
  PVOID  UserContext;
  ULONG  BufferSize;
  PUCHAR Buffer;
  UCHAR  MinorFunction;
  UCHAR  ReturnStatus;
  ULONG  ReturnSize;
} SCSIWMI_REQUEST_CONTEXT, *PSCSIWMI_REQUEST_CONTEXT;
```



## Members

<dl> <dt>

**UserContext**
</dt> <dd>

Points to a miniport driver buffer that contains any data the miniport driver requires to process the SRB. This can be a pointer to the miniport driver's HW\_DEVICE\_EXTENSION structure or some other buffer.

</dd> <dt>

**BufferSize**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**Buffer**
</dt> <dd> <dl> <dt>

Pointer to a structure of type WNODE\_XXX. For more information about these sorts of structures, see [WMI WNODE\_XXX Structures](https://msdn.microsoft.com/library/windows/hardware/ff566371). 
</dt> <dt>

This member is set by [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md). Miniport drivers should not assign values to this member. 
</dt> </dl> </dd> <dt>

**MinorFunction**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**ReturnStatus**
</dt> <dd>

Indicates the return status of the SRB. This member is not valid until after the miniport driver has called [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md) to update the request context.

</dd> <dt>

**ReturnSize**
</dt> <dd>

Indicates the number of bytes of data transferred for the SRB. This member is not valid until after the miniport driver has called [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md) to update the request context.

</dd> </dl>

## Remarks

When the miniport driver receives an SRB in which the **Function** member is set to SRB\_FUNCTION\_WMI, it calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with request parameters, including a pointer to a request context. **ScsiPortWmiDispatchFunction** passes the request context to the miniport driver's appropriate **HwScsiWmi*Xxx*** routine.

When the miniport driver is done processing the SRB and prior to completing the SRB, the miniport driver should call [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md) to update the **ReturnStatus** and **ReturnSize** members of the request context. The miniport driver updates the SRB's data transfer length and status to these values by calling [**ScsiPortWmiGetReturnSize**](scsiportwmigetreturnsize.md) and [**ScsiPortWmiGetReturnStatus**](scsiportwmigetreturnstatus.md). respectively.

A request context must remain valid throughout the processing of an SRB. If the SRB can pend, the miniport driver must allocate the SCSIWMI\_REQUEST\_CONTEXT structure from the SRB extension so it remains valid until the SRB completes. For nonpending SRBs the structure can be allocated from a stack frame that does not go out of scope.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Scsiwmi.h (include Scsiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md)
</dt> <dt>

[**ScsiPortWmiGetReturnSize**](scsiportwmigetreturnsize.md)
</dt> <dt>

[**ScsiPortWmiGetReturnStatus**](scsiportwmigetreturnstatus.md)
</dt> <dt>

[**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSIWMI_REQUEST_CONTEXT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






