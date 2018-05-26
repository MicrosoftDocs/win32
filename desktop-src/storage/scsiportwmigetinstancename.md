---
title: ScsiPortWmiGetInstanceName routine
description: The ScsiPortWmiGetInstanceName routine returns a pointer to the instance name associated with the indicated the Windows Management Instrumentation (WMI) SCSI Request Block (SRB).
ms.assetid: ff2ebd1c-d0ac-47a7-90d4-0b49259784c1
keywords:
- ScsiPortWmiGetInstanceName routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortWmiGetInstanceName
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

# ScsiPortWmiGetInstanceName routine

The **ScsiPortWmiGetInstanceName** routine returns a pointer to the instance name associated with the indicated the [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI) SCSI Request Block (SRB).

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PWCHAR ScsiPortWmiGetInstanceName(
  _In_ PSCSIWMI_REQUEST_CONTEXT RequestContext
);
```



## Parameters

<dl> <dt>

*RequestContext* \[in\]
</dt> <dd>

Pointer to a structure of type [**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md) that contains the request context for a WMI SRB.

</dd> </dl>

## Return value

Pointer to a counted string containing the instance name associated with the indicated SRB. If the SRB type is one that does not use an instance name, **ScsiPortWmiGetInstanceName** returns **NULL**.

## Remarks

The parameter **RequestContext** points to a request context structure, [**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md), that contains information associated with a [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI) SCSI request block (SRB). The request context structure, in turn, contains one of the [WMI WNODE\_XXX Structures](https://msdn.microsoft.com/library/windows/hardware/ff566371) that is used by the WMI system to pass data between user-mode data consumers and kernel-mode data providers such as drivers.

The WNODE\_XXX structure contained in the request context holds an instance name associated with the WMI SRB. The miniport driver calls **ScsiPortWmiGetInstanceName** to extract this instance name from the request context.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortWmiGetInstanceName%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






