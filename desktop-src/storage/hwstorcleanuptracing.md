---
title: HwStorCleanupTracing routine
description: The HwStorCleanupTracing callback routine allows the Storport virtual miniport driver to stop tracing and to free any related resources.
ms.assetid: 878a7c4f-8584-4de2-9a32-f1c358d9b27f
keywords:
- HwStorCleanupTracing routine Storage Devices
- HW_CLEANUP_TRACING
topic_type:
- apiref
api_name:
- HwStorCleanupTracing
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

# HwStorCleanupTracing routine

The **HwStorCleanupTracing** callback routine allows the Storport virtual miniport driver to stop tracing and to free any related resources.

## Syntax


```C++
HW_CLEANUP_TRACING HwStorCleanupTracing;

VOID HwStorCleanupTracing(
   IN PVOID Arg1
)
{ ... }
```



## Parameters

<dl> <dt>

*Arg1* 
</dt> <dd>

A pointer to the driver object.

</dd> </dl>

## Return value

None

## Remarks

The name **HwStorCleanupTracing** is placeholder text for the actual routine name. The actual prototype of this routine is defined in Storport.h as follows:


```
typedef
VOID
HW_CLEANUP_TRACING (
  IN PVOID  Arg1
  );
```



The port driver calls the Storport virtual miniport's **HwStorCleanupTracing** at PASSIVE\_LEVEL.

## Examples

To define an **HwStorCleanupTracing** callback function, you must first provide a function declaration that identifies the type of callback function you re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps [Code Analysis for Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454182), [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV), and other verification tools find errors, and it s a requirement for writing drivers for the Windows operating system.

For example, to define a **HwStorCleanupTracing** callback routine that is named *MyHwCleanupTracing*, use the **HW\_CLEANUP\_TRACING** type as shown in this code example:


```
HW_CLEANUP_TRACING MyHwCleanupTracing;
```



Then, implement your callback routine as follows:


```
_Use_decl_annotations_
VOID
MyHwCleanupTracing (
  _In_ PVOID  Arg1
  );
  {
      ...
  }
```



The **HW\_CLEANUP\_TRACING** function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the \_Use\_decl\_annotations\_ annotation to your function definition. The \_Use\_decl\_annotations\_ annotation ensures that the annotations that are applied to the **HW\_CLEANUP\_TRACING** function type in the header file are used. For more information about the requirements for function declarations, see [Declaring Functions Using Function Role Types for Storport Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454209). For information about \_Use\_decl\_annotations\_, see [**Annotating Function Behavior**](https://msdn.microsoft.com/windows/desktop/c0aa268d-6fa3-4ced-a8c6-f7652b152e61).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HwStorCleanupTracing%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





