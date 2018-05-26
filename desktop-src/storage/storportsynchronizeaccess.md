---
title: StorPortSynchronizeAccess routine
description: The StorPortSynchronizeAccess routine provides synchronized access to a miniport drivers device extension.
ms.assetid: eece67ed-faff-4166-8fa0-d501df9c1363
keywords:
- StorPortSynchronizeAccess routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortSynchronizeAccess
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

# StorPortSynchronizeAccess routine

The **StorPortSynchronizeAccess** routine provides synchronized access to a miniport driver's device extension.

## Syntax


```C++
STORPORT_API BOOLEAN StorPortSynchronizeAccess(
  _In_     PVOID                     HwDeviceExtension,
  _In_     PSTOR_SYNCHRONIZED_ACCESS SynchronizedAccessRoutine,
  _In_opt_ PVOID                     Context
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*SynchronizedAccessRoutine* \[in\]
</dt> <dd>

Pointer to a caller-supplied routine whose execution is to be synchronized with the execution of the ISR associated with the interrupt objects. For a prototype of this routine, see the Remarks section later in this topic.

</dd> <dt>

*Context* \[in, optional\]
</dt> <dd>

Pointer to a context area to be passed to the caller-supplied callback routine when it is called.

</dd> </dl>

## Return value

The return value from *SynchronizedAccessRoutine*.

## Remarks

Miniport drivers that operate in full-duplex mode, and that access information that is shared between their [**HwStorStartIo**](hwstorstartio.md) routine and interrupt-service routine, must use this routine to access the shared data in a synchronized manner.

The miniport driver passes a callback routine to **StorPortSynchronizeAccess**, and **StorPortSynchronizeAccess** calls it after guaranteeing exclusive access to sensitive data structures. The miniport driver's callback routine must conform to the following prototype:


```
typedef
BOOLEAN
(* PSTOR_SYNCHRONIZED_ACCESS) (
  IN PVOID HwDeviceExtension,
 IN PVOID Context
  );
```



where *HwDeviceExtension* is a pointer to the hardware device extension, and *Context* is just a pointer to the same context information that the caller supplied when calling **StorPortSynchronizeAccess**.

For more information, see [Synchronized Access within Unsynchronized Miniport Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff567610).

For more information about synchronization routines, see [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortSynchronizeAccess%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






