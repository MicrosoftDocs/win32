---
title: StorPortDebugPrint routine
description: The StorPortDebugPrint routine prints a debug string to the kernel debugger, if the debugger is attached.
ms.assetid: '46845a10-c44b-4d11-b82e-986bfc066b97'
keywords: ["StorPortDebugPrint routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortDebugPrint
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
---

# StorPortDebugPrint routine

The **StorPortDebugPrint** routine prints a debug string to the kernel debugger, if the debugger is attached.

## Syntax


```C++
VOID StorPortDebugPrint(
   IN ULONG  DebugPrintLevel,
   IN PCCHAR DebugMessage
);
```



## Parameters

<dl> <dt>

*DebugPrintLevel* 
</dt> <dd>

Indicates the amount of debug information that will be displayed.

</dd> <dt>

*DebugMessage* 
</dt> <dd>

Pointer to the debug message to be printed.

</dd> </dl>

## Return value

None

## Remarks

To see these debug strings, the driver writer must set nt!Kd\_STORMINIPORT\_Mask. This follows the new system-wide debug print mechanism.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortDebugPrint%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





