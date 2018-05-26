---
Description: The DrvQueryColorProfile function allows a printer interface DLL to specify an ICC profile to use for color management.
ms.assetid: f6eec5a1-7d73-415f-84d9-1ec3f512abaf
title: DrvQueryColorProfile function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DrvQueryColorProfile function

The **DrvQueryColorProfile** function allows a printer interface DLL to specify an ICC profile to use for color management.

## Syntax


```C++
BOOL DrvQueryColorProfile(
        HANDLE    hPrinter,
  _In_  PDEVMODEW pdevmode,
        ULONG     ulQueryMode,
  _Out_ VOID      *pvProfileData,
  _Out_ ULONG     *pcbProfileData,
  _Out_ FLONG     *pflProfileData
);
```



## Parameters

<dl> <dt>

*hPrinter* 
</dt> <dd>

Caller-supplied printer handle.

</dd> <dt>

*pdevmode* \[in\]
</dt> <dd>

Caller-supplied pointer to a [**DEVMODEW**](display.devmodew) structure.

</dd> <dt>

*ulQueryMode* 
</dt> <dd>

One of the following caller-supplied bit flags, indicating the type of profile to be specified.



| Flag                          | Definition                                            |
|-------------------------------|-------------------------------------------------------|
| QCP\_DEVICEPROFILE<br/> | The caller is requesting a device profile.<br/> |
| QCP\_SOURCEPROFILE<br/> | The caller is requesting a source profile.<br/> |



 

</dd> <dt>

*pvProfileData* \[out\]
</dt> <dd>

Caller-supplied pointer to a buffer to receive profile information.

</dd> <dt>

*pcbProfileData* \[out\]
</dt> <dd>

Caller-supplied pointer to a value representing the size, in bytes, of the buffer pointed to by *pvProfileData*.

</dd> <dt>

*pflProfileData* \[out\]
</dt> <dd>

One of the following function-supplied bit flags, indicating the type of information the function is returning.



| Flag                          | Definition                                                                                                        |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------|
| QCP\_PROFILEDISK<br/>   | The function is returning the file name of an ICC profile in the buffer pointed to by *pvProfileData*.<br/> |
| QCP\_PROFILEMEMORY<br/> | The function is returning profile data in the buffer pointed to by *pvProfileData*.<br/>                    |



 

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**; otherwise, it returns **FALSE**.

## Remarks

A [printer interface DLL](print.printer_interface_dll) can optionally provide a **DrvQueryColorProfile** function. If the function is provided, GDI calls it if ICM has been enabled for a print job. The function's purpose is to determine and specify an ICC profile that is appropriate for use with the print job.

If a driver's printer interface DLL does not provide a **DrvQueryColorProfile** function, or if the function returns **FALSE**, GDI attempts to find a profile. For more information, see [Locating ICC Profiles](print.locating_icc_profiles).

If the output buffer size specified by *pcbProfileData* is too small, the driver should overwrite the size value supplied by *pcbProfileData* with the required buffer size, call SetLastError(ERROR\_INSUFFICIENT\_BUFFER), and return **FALSE**.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvQueryColorProfile%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




