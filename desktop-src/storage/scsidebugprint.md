---
title: ScsiDebugPrint routine
description: The ScsiDebugPrint routine prints debug information with a level of verbosity based on global values set in the kernel debugger or set in the registry and initialized when the system boots.
ms.assetid: bbf3ea14-1802-4433-9043-73bfc0c447bf
keywords:
- ScsiDebugPrint routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiDebugPrint
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScsiDebugPrint routine

The **ScsiDebugPrint** routine prints debug information with a level of verbosity based on global values set in the kernel debugger or set in the registry and initialized when the system boots.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiDebugPrint(
   ULONG  DebugPrintLevel,
   PCCHAR DebugMessage
);
```



## Parameters

<dl> <dt>

*DebugPrintLevel* 
</dt> <dd>

Contains a value between 0 and 3 that specifies the amount of verbosity. A value of 3 signifies the highest level of verbosity. A value of 0 signifies the lowest level. **ScsiDebugPrint** will print the message pointed to by *DebugMessage*, together with other debugging information. For information about how the meaning of *DebugPrintLevel* has changed in Windows XP and later operating systems, see the remarks section.

</dd> <dt>

*DebugMessage* 
</dt> <dd>

Pointer to the message to be printed.

</dd> </dl>

## Return value

None

## Remarks

Prior to Windows XP, the **ScsiDebugPrint** routine compared the value passed to it in the *DebugPrintLevel* parameter with the value of the global variable *ScsiDebug*.and printed the *DebugMessage* string and diagnostic output whenever *DebugPrintLevel* was less than or equal to *ScsiDebug*. If *DebugPrintLevel* was *greater* than *ScsiDebug*.**ScsiDebugPrint** did not print anything.

In Windows XP and later operating systems, **ScsiDebugPrint** no longer compares *DebugPrintLevel* to *ScsiDebug.* Instead, **ScsiDebugPrint** simply calls the routine [**DbgPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff543634) and passes it the *DebugMessage* pointer. Before **ScsiDebugPrint** calls **DbgPrintEx** it maps the value passed in *DebugPrintLevel* to a value used by **DbgPrintEx** as follows.



| Value in *DebugPrintLevel* | Value Passed to DbgPrintEx        |
|----------------------------|-----------------------------------|
| 0<br/>               | DPFLTR\_WARNING\_LEVEL<br/> |
| 1<br/>               | DPFLTR\_TRACE\_LEVEL<br/>   |
| 2<br/>               | DPFLTR\_TRACE\_LEVEL<br/>   |
| 3<br/>               | DPFLTR\_INFO\_LEVEL<br/>    |



 

To view the message pointed to by *DebugMessage* from the kernel debugger, use the component filter mask Kd\_ScsiMiniPort\_Mask. For more information about debugging masks, see [**DbgPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff543634).

**ScsiDebugPrint** only functions in checked builds. **ScsiDebugPrint** compiles to nothing in free builds.

## Requirements



|                            |                                                                                                                              |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                           |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h, Scsi.h, or Minitape.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                                      |



## See also

<dl> <dt>

[**DbgPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff543634)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiDebugPrint%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






