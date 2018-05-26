---
title: StorPortCompleteRequest routine
description: The StorPortCompleteRequest routine completes all outstanding requests setting the SRB status value to SrbStatus.
ms.assetid: 20ee0633-a743-46e8-a094-37099b8e4427
keywords:
- StorPortCompleteRequest routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortCompleteRequest
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortCompleteRequest routine

The **StorPortCompleteRequest** routine completes all outstanding requests setting the SRB status value to **SrbStatus**.

## Syntax


```C++
STORPORT_API VOID StorPortCompleteRequest(
  _In_ PVOID HwDeviceExtension,
  _In_ UCHAR PathId,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun,
  _In_ UCHAR SrbStatus
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*PathId* \[in\]
</dt> <dd>

Identifies the SCSI bus. A value of SP\_UNTAGGED indicates all buses controlled by the HBA.

</dd> <dt>

*TargetId* \[in\]
</dt> <dd>

Identifies the target controller or device on the given buses. A value of SP\_UNTAGGED indicates all targets on the bus.

</dd> <dt>

*Lun* \[in\]
</dt> <dd>

Identifies the logical unit for the given target controller or device. A value of SP\_UNTAGGED indicates all logical units for the given target controllers on the given buses. Full-duplex miniport drivers must not assign a value of SP\_UNTAGGED to this member.

</dd> <dt>

*SrbStatus* \[in\]
</dt> <dd>

Specifies the completion status to be set in the **SrbStatus**member of each SRB.

</dd> </dl>

## Return value

None

## Remarks

We do not recommend that writers of Storport miniport drivers use this particular Storport interface routine. Instead, the miniport driver should call StorPortNotification( RequestComplete ) for each outstanding request.

## Requirements



|                                 |                                                                                                                                            |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl>    |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                                 |
| Library<br/>              | <dl> <dt>Storport.lib</dt> </dl>                                                    |
| DDI compliance rules<br/> | [**StorPortCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/hh454261), [**StorPortDDIsPortOnly**](https://msdn.microsoft.com/library/windows/hardware/hh454262) |



## See also

<dl> <dt>

[**ScsiPortCompleteRequest**](scsiportcompleterequest.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortCompleteRequest%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






