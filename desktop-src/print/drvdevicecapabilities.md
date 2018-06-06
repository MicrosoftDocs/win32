---
Description: A printer interface DLL's DrvDeviceCapabilities function returns requested information about a printer's capabilities.
ms.assetid: a8ea236d-42f9-45c5-b2f6-035e0ba28f75
title: DrvDeviceCapabilities function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DrvDeviceCapabilities function

A printer interface DLL's **DrvDeviceCapabilities** function returns requested information about a printer's capabilities.

## Syntax


```C++
DWORD DrvDeviceCapabilities(
        HANDLE   hPrinter,
  _In_  PWSTR    pDeviceName,
        WORD     iDevCap,
  _Out_ PVOID    pvOutput,
  _In_  PDEVMODE pDevMode
);
```



## Parameters

<dl> <dt>

*hPrinter* 
</dt> <dd>

Caller-supplied printer handle.

</dd> <dt>

*pDeviceName* \[in\]
</dt> <dd>

Caller-supplied pointer to a printer name string.

</dd> <dt>

*iDevCap* 
</dt> <dd>

Caller-supplied bit flag indicating the information being requested. This can be one of the flags listed in the following table. (The flags are defined in header file Wingdi.h.)



| Flag                              | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DC\_BINADJUST<br/>          | Not used for NT-based operating systems.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DC\_BINNAMES<br/>           | The *pvOutput* parameter points to a buffer that the function should fill with an array of string buffers, each 24 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the name of a paper source bin.<br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/>                                                      |
| DC\_BINS<br/>               | The *pvOutput* parameter points to a buffer that the function should fill with a WORD array. Each array element should contain a DMBIN-prefixed constant (or customized value) representing a supported paper source bin.<br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/>                                                                                                        |
| DC\_COLLATE<br/>            | The *pvOutput* parameter is not used.<br/> The function's return value should be 1 if the printer supports collating; otherwise, the return value should be zero.<br/>                                                                                                                                                                                                                                                                                                                                                                      |
| DC\_COLORDEVICE<br/>        | The *pvOutput* parameter is not used.<br/> The function's return value should be 1 if the printer supports color printing; otherwise, the return value should be zero.<br/>                                                                                                                                                                                                                                                                                                                                                                 |
| DC\_COPIES<br/>             | The *pvOutput* parameter is not used.<br/> The function's return value should be the maximum number of copies the printer can support.<br/>                                                                                                                                                                                                                                                                                                                                                                                                 |
| DC\_DATATYPE\_PRODUCED<br/> | Not used for NT-based operating systems.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DC\_DRIVER<br/>             | The *pvOutput* parameter is not used.<br/> The function's return value should be the **dmDriverVersion** member of the driver's internal [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure.<br/>                                                                                                                                                                                                                                                                                                                                                   |
| DC\_DUPLEX<br/>             | The *pvOutput* parameter is not used.<br/> The function's return value should be 1 if the printer supports duplex printing; otherwise, the return value should be zero.<br/>                                                                                                                                                                                                                                                                                                                                                                |
| DC\_EMF\_COMPLIANT<br/>     | Not used for NT-based operating systems.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DC\_ENUMRESOLUTIONS<br/>    | The *pvOutput* parameter points to a buffer that the function should fill with a LONG array. For each resolution supported by the printer, the function should return two long words (one for the *x* dimension and one for the *y* dimension) of the resolution, in dots per inch.<br/> The function's return value should be the number of resolutions supported.<br/> If **pvOutput** is **NULL**, the function should just return the number of resolutions supported.<br/>                                                       |
| DC\_EXTRA<br/>              | The *pvOutput* parameter is not used.<br/> The function's return value should be the **dmDriverExtra** member of the driver's internal [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure.<br/>                                                                                                                                                                                                                                                                                                                                                     |
| DC\_FIELDS<br/>             | The *pvOutput* parameter is not used.<br/> The function's return value should be the **dmFields** member of the driver's internal [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure. The **dmFields** member indicates which members in the device-independent portion of the DEVMODEW structure are supported by the printer driver.<br/>                                                                                                                                                                                                         |
| DC\_FILEDEPENDENCIES<br/>   | The *pvOutput* parameter points to a buffer that the function should fill with an array of string buffers, each 64 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the name of a file that must be installed with the driver.<br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/>                           |
| DC\_MANUFACTURER<br/>       | Not used for NT-based operating systems.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DC\_MAXEXTENT<br/>          | The *pvOutput* parameter is not used.<br/> The function should return a POINTS structure (described in the Microsoft Windows SDK documentation). The structure should contain the maximum allowable values for the **dmPaperWidth** (*x* dimension) and **dmPaperLength** (*y* dimension) members of the printer's DEVMODEW structure.<br/>                                                                                                                                                                                                 |
| DC\_MEDIAREADY<br/>         | The *pvOutput* parameter points to a buffer that the function should fill with an array of string buffers, each 64 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the name of a paper form that is available for use.<br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/>                                  |
| DC\_MEDIATYPENAMES<br/>     | The *pvOutput* parameter points to a buffer that the function should fill with an array of string buffers, each 64 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the name of a supported media type. <br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should simply return the number of array elements required.<br/>                                               |
| DC\_MEDIATYPES<br/>         | The *pvOutput* parameter points to a buffer that the function should fill with a DWORD array. Each array element should contain a DMMEDIA-prefixed constant (see the [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure) or customized value representing a supported media type. <br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should simply return the number of array elements required.<br/>                                                     |
| DC\_MINEXTENT<br/>          | The *pvOutput* parameter is not used.<br/> The function should return a POINTS structure (described in the Windows SDK documentation). The structure should contain the minimum allowable values for the **dmPaperWidth** (*x* dimension) and **dmPaperLength** (*y* dimension) members of the printer's DEVMODEW structure.<br/>                                                                                                                                                                                                           |
| DC\_MODEL<br/>              | Not used for NT-based operating systems.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DC\_NUP<br/>                | The *pvOutput* parameter points to a buffer that the function should fill with a DWORD array. Each array element should contain an integer representing an N-up option (that is, each integer should represent a supported number of document pages per physical page).<br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/>                                                          |
| DC\_ORIENTATION<br/>        | The *pvOutput* parameter is not used.<br/> The function's return value should be the number of degrees of rotation required to produce landscape orientation from portrait orientation. A value of zero indicates landscape orientation is not supported.<br/>                                                                                                                                                                                                                                                                              |
| DC\_PAPERNAMES<br/>         | The *pvOutput* parameter points to a buffer that the function should fill with an array of string buffers, each 64 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the name of a paper form.<br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/>                                                            |
| DC\_PAPERS<br/>             | The *pvOutput* parameter points to a buffer that the function should fill with a WORD array. Each array element should contain a DMPAPER-prefixed constant (or customized value) representing a supported paper form.<br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/>                                                                                                            |
| DC\_PAPERSIZE<br/>          | The *pvOutput* parameter points to a buffer that the function should fill with a POINT array. Each array element should contain the *x* and *y* dimensions of a form's paper size, in 0.1 mm units, in portrait orientation.<br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/>                                                                                                     |
| DC\_PERSONALITY<br/>        | The *pvOutput* parameter points to a buffer that the function should fill with an array of string buffers, each 32 characters in length. Each string buffer in the array should contain a wide-character, NULL-terminated string specifying the printer description language supported by the printer (for example, L"HP-GL/2").<br/> The function's return value should be the number of elements in the returned array.<br/> If *pvOutput* is **NULL**, the function should just return the number of array elements required.<br/> |
| DC\_PRINTERMEM<br/>         | The *pvOutput* parameter is not used.<br/> The function's return value should be an integer representing the amount of available printer memory, in kilobytes.<br/>                                                                                                                                                                                                                                                                                                                                                                         |
| DC\_PRINTRATE<br/>          | The *pvOutput* parameter is not used.<br/> The function's return value should be an integer representing the print rate, in the units specified for DC\_PRINTRATEUNIT.<br/>                                                                                                                                                                                                                                                                                                                                                                 |
| DC\_PRINTRATEPPM<br/>       | The *pvOutput* parameter is not used.<br/> The function's return value should be an integer representing the print rate, in pages per minute.<br/>                                                                                                                                                                                                                                                                                                                                                                                          |
| DC\_PRINTRATEUNIT<br/>      | The *pvOutput* parameter is not used.<br/> The function's return value should identify the units used for specifying the value returned for DC\_PRINTRATE. One of the following constants must be specified: <br/> PRINTRATEUNIT\_PPM - pages/min.<br/> PRINTRATEUNIT\_CPS - chars./sec.<br/> PRINTRATEUNIT\_LPM - lines/min.<br/> PRINTRATEUNIT\_IPM - inches/min.<br/>                                                                                                                                            |
| DC\_SIZE<br/>               | The *pvOutput* parameter is not used.<br/> The function's return value should be the **dmSize** member of the driver's internal [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure.<br/>                                                                                                                                                                                                                                                                                                                                                            |
| DC\_STAPLE<br/>             | The *pvOutput* parameter is not used.<br/> The function's return value should be **TRUE** if the printer supports stapling, and **FALSE** if the printer does not support stapling.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| DC\_TRUETYPE<br/>           | The *pvOutput* parameter is not used.<br/> The function's return value can be zero, one, or more of the following flags:<br/> DCTT\_BITMAP: The device can print TrueType fonts as graphics.<br/> DCTT\_DOWNLOAD: The device can accept downloaded TrueType fonts.<br/> DCTT\_DOWNLOAD\_OUTLINE: (Windows 95/98/Me only) The device can download outline TrueType fonts.<br/> DCTT\_SUBDEV: The device can substitute device fonts for TrueType fonts.<br/>                                                         |
| DC\_VERSION<br/>            | The *pvOutput* parameter is not used.<br/> The function's return value should be the **dmSpecVersion** member of the driver's internal [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure.<br/>                                                                                                                                                                                                                                                                                                                                                     |



 

</dd> <dt>

*pvOutput* \[out\]
</dt> <dd>

A caller-supplied pointer to a buffer to receive function-supplied information. The buffer's use is dependent on the value received for the *iDevCap* parameter.

</dd> <dt>

*pDevMode* \[in\]
</dt> <dd>

A caller-supplied pointer to a [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure that describes the current print job characteristics. If this parameter is **NULL**, **DrvDeviceCapabilities** retrieves the current default initialization values for the specified printer driver, such as the user default DEVMODEW structure of the print queue.

</dd> </dl>

## Return value

The function's return value is dependent on the value received for the *iDevCap* parameter. If the received *iDevCap* value represents a capability that the driver does not support, or if an error is encountered, the function should return GDI\_ERROR.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvDeviceCapabilities%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




