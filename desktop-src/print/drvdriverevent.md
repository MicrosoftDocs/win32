---
Description: The print spooler calls a printer interface DLL's DrvDriverEvent function when the spooler processes driver-specific events that might require action by the printer driver.
ms.assetid: 84d1f438-b6ee-4199-89ae-9384601203b3
title: DrvDriverEvent function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DrvDriverEvent function

The print spooler calls a printer interface DLL's **DrvDriverEvent** function when the spooler processes driver-specific events that might require action by the printer driver.

## Syntax


```C++
BOOL DrvDriverEvent(
           DWORD  dwDriverEvent,
           DWORD  dwLevel,
  _In_opt_ LPBYTE pDriverInfo,
           LPARAM lParam
);
```



## Parameters

<dl> <dt>

*dwDriverEvent* 
</dt> <dd>

Caller-supplied bit flag indicating the event that has occurred. Valid flags are listed in the following table.



| Flag                                 | Definition                                     |
|--------------------------------------|------------------------------------------------|
| DRIVER\_EVENT\_DELETE<br/>     | The driver is being removed.<br/>        |
| DRIVER\_EVENT\_INITIALIZE<br/> | The driver has just been installed.<br/> |



 

</dd> <dt>

*dwLevel* 
</dt> <dd>

Caller-supplied value indicating the type of structure pointed to by the *pDriverInfo* parameter, as indicated in the following table.



| *dwLevel* Value | Structure pointed to by *pDriverInfo* |
|-----------------|---------------------------------------|
| 1<br/>    | DRIVER\_INFO\_1<br/>            |
| 2<br/>    | DRIVER\_INFO\_2<br/>            |
| 3<br/>    | DRIVER\_INFO\_3<br/>            |



 

<dl> <dd>

The DRIVER\_INFO\_*N* structures are described in the Microsoft Windows SDK documentation.

</dd> </dl> </dd> <dt>

*pDriverInfo* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a structure whose type is identified by the *dwLevel* parameter.

</dd> <dt>

*lParam* 
</dt> <dd>

Caller-supplied flags. See the following Remarks section.

</dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**. Otherwise, it should return **FALSE**.

## Remarks

The optional **DrvDriverEvent** function is called by the spooler's **AddPrinterDriverEx** and **DeletePrinterDriverEx** functions, which are described in the Windows SDK documentation.

The function's purpose is to allow a printer driver's [printer interface DLL](https://www.bing.com/search?q=printer+interface+DLL) to perform operations needed when the driver is installed or removed. A typical operation for this function to perform is to create or remove extra driver-specific files that are not specified as dependent files in a [printer INF file](https://www.bing.com/search?q=printer+INF+file).

If *dwDriverEvent* is DRIVER\_EVENT\_DELETE, the *lparam* parameter contains the flags that were specified for the **DeletePrinterDriverEx** function's *dwDeleteFlag* parameter. The *lparam* parameter is not used if *dwDriverEvent* is DRIVER\_EVENT\_INITIALIZE.

Because the **DrvDriverEvent** function is called in the context of the print spooler, it cannot display a user interface.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvDriverEvent%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




