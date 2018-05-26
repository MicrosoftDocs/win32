---
title: ScsiPortWmiSetInstanceCount function
description: The ScsiPortWmiSetInstanceCount specifies the number of instances for which data buffers must be set aside within the WNODE\_ALL\_DATA structure in the request context.
ms.assetid: 0de2c766-cd3c-46ff-bb78-f1e4c37af2c0
keywords:
- ScsiPortWmiSetInstanceCount function Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortWmiSetInstanceCount
api_location:
- scsiwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ScsiPortWmiSetInstanceCount function

The **ScsiPortWmiSetInstanceCount** specifies the number of instances for which data buffers must be set aside within the [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372) structure in the request context.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN ScsiPortWmiSetInstanceCount(
  _In_  PSCSIWMI_REQUEST_CONTEXT RequestContext,
  _In_  ULONG                    InstanceCount,
  _Out_ PULONG                   BufferAvail,
  _Out_ PULONG                   SizeNeeded
);
```



## Parameters

<dl> <dt>

*RequestContext* \[in\]
</dt> <dd>

Pointer to a structure of type [**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md) that contains the request context for a WMI SRB.

</dd> <dt>

*InstanceCount* \[in\]
</dt> <dd>

Contains the number of instances for which the minidriver will provide data.

</dd> <dt>

*BufferAvail* \[out\]
</dt> <dd>

Contains, on return, the number of bytes of buffer space available for describing instance names and data. The value that is returned in this member can be passed to routines [**ScsiPortWmiSetData**](scsiportwmisetdata.md) and [**ScsiPortWmiSetInstanceName**](scsiportwmisetinstancename.md) in the *BufferAvail* parameter of those routines.

The **ScsiPortWmiSetInstanceCount** routine initializes an array of pointers to data buffers, with one array element for each instance. If there is not enough memory available in the WNODE to initialize an array of size *InstanceCount*, a zero will be returned in this member.

</dd> <dt>

*SizeNeeded* \[out\]
</dt> <dd>

Indicates, on input, the number of bytes needed to describe the entire WNODE *before* configuring the internal arrays in the WNODE. On return, this member will contain the size of the entire WNODE, including the newly initialized arrays within the WNODE.

</dd> </dl>

## Return value

The **ScsiPortWmiSetInstanceCount** routine returns **TRUE** if the operation succeeds and **FALSE** if the WNODE contained within the request context is not of type [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372).

## Remarks

The minidriver must call **ScsiPortWmiSetInstanceCount** before calling either [**ScsiPortWmiSetData**](scsiportwmisetdata.md) or [**ScsiPortWmiSetInstanceName**](scsiportwmisetinstancename.md). The minidriver should only call **ScsiPortWmiSetInstanceCount** once.

The parameter **RequestContext** points to a request context structure, [**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md), that contains information associated with a [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI) SCSI request block (SRB). The request context structure, in turn, contains one of the [WMI WNODE\_XXX Structures](https://msdn.microsoft.com/library/windows/hardware/ff566371) used by the WMI system to pass data between user-mode data consumers and kernel-mode data providers such as drivers.

The **ScsiPortWmiSetInstanceCount** routine requires the WNODE structure that is defined within the request context to be of type [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372). This is because **ScsiPortWmiSetInstanceCount** sets aside a data area that will hold information for multiple instances associated with a WMI data block. Unlike the [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) structure which contains information about a single instance, the WNODE\_ALL\_DATA structure contains an array of pointers to buffer areas for different instances, and **ScsiPortWmiSetInstanceCount** initializes this array, so that each buffer of instance data can be accessed individually using an instance index.

The memory allocated for the request context must remain valid until after the miniport driver calls **ScsiPortWmiPostProcess**, and **ScsiPortWmiPostProcess** returns the final SRB status and buffer size. If the SRB can pend, the memory for the request context should be allocated from the SRB extension. If the SRB cannot pend, the memory can be allocated from a stack frame that does not go out of scope.

## Requirements



|                            |                                                                                                                     |
|----------------------------|---------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                  |
| Header<br/>          | <dl> <dt>Scsiwmi.h (include Miniport.h or Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md)
</dt> <dt>

[**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377)
</dt> <dt>

[**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortWmiSetInstanceCount%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






