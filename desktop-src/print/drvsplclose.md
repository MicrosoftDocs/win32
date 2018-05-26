---
Description: .
ms.assetid: bd5f0bf2-ccb8-446c-b1e5-2e32538ebfbd
title: DrvSplClose function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DrvSplClose function

## Syntax


```C++
VOID WINAPI DrvSplClose(
   HANDLE hDriver
);
```



## Parameters

<dl> <dt>

*hDriver* 
</dt> <dd></dd> </dl>

## Return value

This function does not return a value.

## 

The **DrvSplClose** function is obsolete, and is supported only so that user-mode rendering DLLs, optionally supplied with Windows NT 4.0 drivers, will execute under Windows 2000 and later. Use [**DrvDocumentEvent**](drvdocumentevent.md) instead of this function.

The **DrvSplClose** function enables a user-mode rendering DLL to deallocate resources.

### Comments

To supply user-mode image-rendering code for printers, see [Choosing User Mode or Kernel Mode](print.choosing_user_mode_or_kernel_mode).

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvSplClose%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




