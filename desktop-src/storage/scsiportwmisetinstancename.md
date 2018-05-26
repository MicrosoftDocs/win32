---
title: ScsiPortWmiSetInstanceName routine
description: The ScsiPortWmiSetInstanceName routine updates the WNODE\_ALL\_DATA structure within the request context to specify the position and length of an instance name.
ms.assetid: f624959f-e232-4918-8f0b-f232471c2c67
keywords:
- ScsiPortWmiSetInstanceName routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortWmiSetInstanceName
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

# ScsiPortWmiSetInstanceName routine

The **ScsiPortWmiSetInstanceName** routine updates the [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372) structure within the request context to specify the position and length of an instance name.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PWCHAR ScsiPortWmiSetInstanceName(
  _In_    PSCSIWMI_REQUEST_CONTEXT RequestContext,
  _In_    ULONG                    InstanceIndex,
  _In_    ULONG                    InstanceNameLength,
  _Out_   PULONG                   BufferAvail,
  _Inout_ PULONG                   SizeNeeded
);
```



## Parameters

<dl> <dt>

*RequestContext* \[in\]
</dt> <dd>

Pointer to a structure of type [**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md) that contains the request context for a WMI SRB.

</dd> <dt>

*InstanceIndex* \[in\]
</dt> <dd>

Contains an index that indicates the instance for which the position and length of the instance name are to be specified.

</dd> <dt>

*InstanceNameLength* \[in\]
</dt> <dd>

Specifies the size in bytes of the instance name.

</dd> <dt>

*BufferAvail* \[out\]
</dt> <dd>

Must contain, on input, the number of bytes of buffer space in the [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372) structure that can be used for describing instance names and data. On return, this member contains the number of bytes of buffer space that remain.

There are three SCSI Port WMI routines that return a value for the available buffer size in their *BufferAvail* parameter:

[**ScsiPortWmiSetInstanceCount**](scsiportwmisetinstancecount.md)

[**ScsiPortWmiSetData**](scsiportwmisetdata.md)

**ScsiPortWmiSetInstanceName**

The miniport driver must call **ScsiPortWmiSetInstanceCount** first, but after **ScsiPortWmiSetInstanceCount** has been called, it does not matter in what order the minidriver calls **ScsiPortWmiSetData** and **ScsiPortWmiSetInstanceName**. When calling either **ScsiPortWmiSetData** or **ScsiPortWmiSetInstanceName**, the value passed to the routine in its *BufferAvail* parameter must be the same as the value returned in the *BufferAvail* parameter by the most recently called SCSI Port WMI routine. For instance, suppose the minidriver calls **ScsiPortWmiSetInstanceCount** first, and this routine returns a value of 1,000 in its *BufferAvail* parameter. Next, the minidriver calls **ScsiPortWmiSetData** which returns a value of 500 in its *BufferAvail* parameter. Finally, the minidriver calls **ScsiPortWmiSetInstanceName** which returns a value of 200 in its *BufferAvail* parameter. The initial value of 1,000 must be passed to **ScsiPortWmiSetData** in *BufferAvail*, and the value of 500 must be passed to **ScsiPortWmiSetInstanceName**.

If there is not enough memory available to add an instance name of length *InstanceNameLength*, a zero will be returned in the *BufferAvail* member.

</dd> <dt>

*SizeNeeded* \[in, out\]
</dt> <dd>

Indicates, on input, the number of bytes needed to describe the WNODE *before* adding the descriptive data for the instance specified by *InstanceIndex*. On return, this member will contain the size of the entire WNODE, including the data for the new instance.

</dd> </dl>

## Return value

The **ScsiPortWmiSetInstanceCount** routine returns a pointer to the buffer where the caller can store the name of the instance specified in *InstanceIndex*. If **ScsiPortWmiSetInstanceCount** cannot allocate enough memory for the instance name, or if the WNODE contained within the request context is not of type [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372), **ScsiPortWmiSetData** returns **NULL**.

## Remarks

The minidriver must call [**ScsiPortWmiSetInstanceCount**](scsiportwmisetinstancecount.md) before calling **ScsiPortWmiSetInstanceName**.

The parameter **RequestContext** points to a request context structure, [**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md), that contains information associated with a [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI) SCSI request block (SRB). The request context structure, in turn, contains one of the [WMI WNODE\_XXX Structures](https://msdn.microsoft.com/library/windows/hardware/ff566371) used by the WMI system to pass data between user-mode data consumers and kernel-mode data providers such as drivers.

The **ScsiPortWmiSetInstanceName** routine requires the WNODE structure that is defined within the request context to be of type [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372). This is because **ScsiPortWmiSetInstanceName** can set aside an instance name area for any of the instances associated with a WMI data block. Unlike the [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) structure which contains information about a single instance, the WNODE\_ALL\_DATA structure contains an array of pointers to buffer areas for different instances, and **ScsiPortWmiSetInstanceCount** initializes this array, so that each buffer of instance data can be accessed individually.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortWmiSetInstanceName%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






