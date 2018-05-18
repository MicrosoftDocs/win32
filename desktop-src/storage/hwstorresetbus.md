---
title: HW\_RESET\_BUS routine
description: The HwStorResetBus routine is called by the port driver to clear error conditions.
ms.assetid: 'fda5291c-dd4e-4aa1-8dac-65cf4c4306ab'
keywords: ["HwStorResetBus routine Storage Devices", "HW_RESET_BUS"]
topic_type:
- apiref
api_name:
- HwStorResetBus
api_location:
- Storport.h
api_type:
- UserDefined
---

# HW\_RESET\_BUS routine

The **HwStorResetBus** routine is called by the port driver to clear error conditions.

## Syntax


```C++
HW_RESET_BUS HwStorResetBus;

BOOLEAN HwStorResetBus(
   IN PVOID DeviceExtension,
   IN ULONG PathId
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* 
</dt> <dd>

A pointer to the miniport driver's per HBA storage area.

</dd> <dt>

*PathId* 
</dt> <dd>

Identifies the SCSI bus to be reset.

</dd> </dl>

## Return value

If the bus is successfully reset, **HwStorResetBus** returns **TRUE**.

## Remarks

The name **HwStorResetBus** is just a placeholder. The actual prototype of this routine is defined in *Storport.h* as follows:


```
typedef
BOOLEAN
HW_RESET_BUS (
  _In_ PVOID  DeviceExtension,
  _In ULONG  PathId
  );
```



The port driver pauses all device IO queues for the adapter and then calls the **HwStorResetBus** routine at IRQL DISPATCH\_LEVEL after acquiring the StartIo spin lock. A miniport driver is responsible for completing SRBs received by [**HwStorStartIo**](hwstorstartio.md) for *PathId* during this routine and setting their status to SRB\_STATUS\_BUS\_RESET if necessary.

In addition to the StartIo spin lock being taken and subsequently released after **HwStorResetBus** returns, if the miniport has requested multiple channel support through PERF\_CONFIGURATION\_DATA, all channel tokens will be taken and, on return of the callback, released. This ensures that no IO’s are dispatched to [**HwStorStartIo**](hwstorstartio.md) during the reset bus phase.

## Examples

To define an **HwStorResetBus** callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps [Code Analysis for Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454182), [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.

For example, to define a **HwStorResetBus** callback routine that is named *MyHwResetBus*, use the **HW\_RESET\_BUS** type as shown in this code example:


```
HW_RESET_BUS MyHwResetBus;
```



Then, implement your callback routine as follows:


```
_Use_decl_annotations_
BOOLEAN
MyHwResetBus (
  _In_ PVOID  DeviceExtension,
  _In_ ULONG  PahtId
  );
  {
      ...
  }
```



The **HW\_RESET\_BUS** function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the \_Use\_decl\_annotations\_ annotation to your function definition. The \_Use\_decl\_annotations\_ annotation ensures that the annotations that are applied to the **HW\_RESET\_BUS** function type in the header file are used. For more information about the requirements for function declarations, see [Declaring Functions Using Function Role Types for Storport Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454209). For information about \_Use\_decl\_annotations\_, see [**Annotating Function Behavior**](c0aa268d-6fa3-4ced-a8c6-f7652b152e61).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | DISPATCH\_LEVEL (See Remarks section.)<br/>                                                                                       |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_RESET_BUS%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





