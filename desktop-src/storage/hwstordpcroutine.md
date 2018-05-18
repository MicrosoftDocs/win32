---
title: HW\_DPC\_ROUTINE routine
description: The HwStorDpcRoutine routine is a routine that is deferred for execution at DISPATCH IRQL by means of the deferred procedure call (DPC) mechanism.
ms.assetid: 'bc646191-e405-49e2-8793-0c0b81e52f50'
keywords: ["HwStorDpcRoutine routine Storage Devices", "HW_DPC_ROUTINE"]
topic_type:
- apiref
api_name:
- HwStorDpcRoutine
api_location:
- Storport.h
api_type:
- UserDefined
---

# HW\_DPC\_ROUTINE routine

The **HwStorDpcRoutine** routine is a routine that is deferred for execution at DISPATCH IRQL by means of the deferred procedure call (DPC) mechanism.

## Syntax


```C++
HW_DPC_ROUTINE HwStorDpcRoutine;

VOID HwStorDpcRoutine(
   IN PSTOR_DPC Dpc,
   IN PVOID     HwDeviceExtension,
   IN PVOID     SystemArgument1,
   IN PVOID     SystemArgument2
)
{ ... }
```



## Parameters

<dl> <dt>

*Dpc* 
</dt> <dd>

A pointer to a Storport DPC context.

</dd> <dt>

*HwDeviceExtension* 
</dt> <dd>

A pointer to the per-adapter device extension.

</dd> <dt>

*SystemArgument1* 
</dt> <dd>

A pointer to caller-supplied information.

</dd> <dt>

*SystemArgument2* 
</dt> <dd>

A pointer to caller-supplied information.

</dd> </dl>

## Return value

None.

## Remarks

When a miniport driver calls [**StorPortInitializeDpc**](storportinitializedpc.md) to initialize a DPC it must load the *HwDpcRoutine* parameter of the **StorPortInitializeDpc** routine with a pointer to the **HwStorDpcRoutine** routine.

Any particular instance of a DPC routine is guaranteed to be synchronized with other instances of the DPC routine. A DPC routine can synchronize itself with the [**HwStorStartIo**](hwstorstartio.md) routine or with the [**HwStorInterrupt**](hwstorinterrupt.md) routine by acquiring the appropriate spin lock with a call to [**StorPortAcquireSpinLock**](storportacquirespinlock.md). For more information about the management of spin locks within DPC routines, see [**StorPortIssueDpc**](storportissuedpc.md).

The name **HwStorDpcRoutine** is just a placeholder. The actual prototype of this routine is defined in *storport.h* as follows:


```
typedef
BOOLEAN
HW_DPC_ROUTINE (
  _In_  PSTOR_DPC Dpc,
  _In_  PVOID HwDeviceExtension,
  _In_opt_  PVOID SystemArgument1,
  _In_opt_  PVOID SystemArgument2
  );
```



The port driver calls the **HwStorDpcRoutine** routine at DISPATCH IRQL.

## Examples

To define an **HwStorDpcRoutine** callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps [Code Analysis for Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454182), [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.

For example, to define a **HwStorDpcRoutine** callback routine that is named *MyHwDpcRoutine*, use the **HW\_DPC\_ROUTINE** type as shown in this code example:


```
HW_DPC_ROUTINE MyHwDpcRoutine;
```



Then, implement your callback routine as follows:


```
_Use_decl_annotations_
BOOLEAN
MyHwDpcRoutine (
  _In_  PSTOR_DPC Dpc,
  _In_  PVOID HwDeviceExtension,
  _In_opt_  PVOID SystemArgument1,
  _In_opt_  PVOID SystemArgument2
  );
  {
      ...
  }
```



The **HW\_DPC\_ROUTINE** function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the \_Use\_decl\_annotations\_ annotation to your function definition. The \_Use\_decl\_annotations\_ annotation ensures that the annotations that are applied to the **HW\_DPC\_ROUTINE** function type in the header file are used. For more information about the requirements for function declarations, see [Declaring Functions Using Function Role Types for Storport Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454209). For information about \_Use\_decl\_annotations\_, see [**Annotating Function Behavior**](c0aa268d-6fa3-4ced-a8c6-f7652b152e61).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | DISPATCH\_LEVEL (See Remarks section.)<br/>                                                                                       |



## See also

<dl> <dt>

[**HwStorInterrupt**](hwstorinterrupt.md)
</dt> <dt>

[**HwStorStartIo**](hwstorstartio.md)
</dt> <dt>

[**StorPortAcquireSpinLock**](storportacquirespinlock.md)
</dt> <dt>

[**StorPortInitializeDpc**](storportinitializedpc.md)
</dt> <dt>

[**StorPortIssueDpc**](storportissuedpc.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_DPC_ROUTINE%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






