---
title: HW\_PASSIVE\_INITIALIZE\_ROUTINE routine
description: The HwStorPassiveInitializeRoutine callback routine is called after the HwStorInitialize routine when the current IRQL is at PASSIVE\_LEVEL.
ms.assetid: 70f65a4e-0a98-4135-bb38-530c729538a3
keywords:
- HwStorPassiveInitializeRoutine routine Storage Devices
- HW_PASSIVE_INITIALIZE_ROUTINE
topic_type:
- apiref
api_name:
- HwStorPassiveInitializeRoutine
api_location:
- Storport.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HW\_PASSIVE\_INITIALIZE\_ROUTINE routine

The **HwStorPassiveInitializeRoutine** callback routine is called after the [**HwStorInitialize**](hwstorinitialize.md) routine when the current IRQL is at PASSIVE\_LEVEL. The **HwStorPassiveInitializeRoutine** callback is set by calling the [**StorPortEnablePassiveInitialization**](storportenablepassiveinitialization.md) routine. Initializing of the miniport's deferred procedure calls (DPCs) occurs in the **HwStorPassiveInitializeRoutine** callback.

## Syntax


```C++
HW_PASSIVE_INITIALIZE_ROUTINE HwStorPassiveInitializeRoutine;

BOOLEAN HwStorPassiveInitializeRoutine(
   IN PVOID HwDeviceExtension
)
{ ... }
```



## Parameters

<dl> <dt>

*HwDeviceExtension* 
</dt> <dd>

A pointer to a per-adapter storage area.

</dd> </dl>

## Return value

The **HwStorPassiveInitializeRoutine** routine returns **TRUE** if the miniport successfully initialized the processing of DPCs, or **FALSE** if the initialization process failed.

## Remarks

The **HwStorPassiveInitializeRoutine** routine should initialize any DPCs that the miniport driver will use. The port driver calls **HwStorPassiveInitializeRoutine** at PASSIVE\_LEVEL without any spin locks held. Interrupts are enabled while this routine is called.

The name **HwStorPassiveInitializeRoutine** is just a placeholder. The actual prototype for this callback routine is defined in *storport.h*as follows:


```
typedef
BOOLEAN
(*PHW_PASSIVE_INITIALIZE_ROUTINE) (
  _In_ PVOID DeviceExtension
  );
```



The port driver calls the **HwStorPassiveInitializeRoutine** routine at PASSIVE IRQL without acquiring any spin locks.

## Examples

To define an **HwStorPassiveInitializeRoutine** callback function, you must first provide a function declaration that identifies the type of callback function you re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps [Code Analysis for Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454182), [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV), and other verification tools find errors, and it s a requirement for writing drivers for the Windows operating system.

For example, to define a **HwStorPassiveInitializeRoutine** callback routine that is named *MyHwPassiveInitialize*, use the **HW\_PASSIVE\_INITIALIZE\_ROUTINE** type as shown in this code example:


```
HW_PASSIVE_INITIALIZE_ROUTINE MyHwPassiveInitialize;
```



Then, implement your callback routine as follows:


```
_Use_decl_annotations_
BOOLEAN
MyHwPassiveInitialize (
  _In_ PVOID  DeviceExtension
  );
  {
      ...
  }
```



The **HW\_PASSIVE\_INITIALIZE\_ROUTINE** function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the \_Use\_decl\_annotations\_ annotation to your function definition. The \_Use\_decl\_annotations\_ annotation ensures that the annotations that are applied to the **HW\_PASSIVE\_INITIALIZE\_ROUTINE** function type in the header file are used. For more information about the requirements for function declarations, see [Declaring Functions Using Function Role Types for Storport Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454209). For information about \_Use\_decl\_annotations\_, see [**Annotating Function Behavior**](https://msdn.microsoft.com/windows/desktop/c0aa268d-6fa3-4ced-a8c6-f7652b152e61).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | PASSIVE\_LEVEL (See Remarks section.)<br/>                                                                                        |



## See also

<dl> <dt>

[**StorPortEnablePassiveInitialization**](storportenablepassiveinitialization.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_PASSIVE_INITIALIZE_ROUTINE%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






