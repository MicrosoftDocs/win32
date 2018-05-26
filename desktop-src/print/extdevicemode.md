---
Description: The ExtDeviceMode function is provided only for compatibility with 16-bit applications.
ms.assetid: dade9d25-7143-4566-adc1-0c97cb508c07
title: ExtDeviceMode function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ExtDeviceMode function

The **ExtDeviceMode** function is provided only for compatibility with 16-bit applications. Printer drivers without this requirement should instead use the **DocumentProperties** function, which is described in the Microsoft Windows SDK documentation.

The **ExtDeviceMode** function retrieves or modifies printer initialization information for a given graphics driver, or displays a driver-supplied printer-configuration property sheet for the specified printer.

## Syntax


```C++
LONG ExtDeviceMode(
  _In_opt_ HWND       hWnd,
  _In_opt_ HANDLE     hInst,
  _Inout_  LPDEVMODEA pDevModeOutput,
  _In_opt_ LPSTR      pDeviceName,
  _In_opt_ LPSTR      pPort,
  _In_opt_ LPDEVMODEA pDevModeInput,
  _In_opt_ LPSTR      pProfile,
           DWORD      fMode
);
```



## Parameters

<dl> <dt>

*hWnd* \[in, optional\]
</dt> <dd>

Handle to the parent window for the printer-configuration property sheet.

</dd> <dt>

*hInst* \[in, optional\]
</dt> <dd>

Not used. Handle to the module instance of the device driver.

</dd> <dt>

*pDevModeOutput* \[in, out\]
</dt> <dd>

Pointer to the DEVMODE structure that receives the printer configuration data supplied in the buffer pointed to by the *pDevModeInput* parameter.

</dd> <dt>

*pDeviceName* \[in, optional\]
</dt> <dd>

Pointer to a NULL-terminated string that contains the name of the device for which the printer configuration property sheet is displayed.

</dd> <dt>

*pPort* \[in, optional\]
</dt> <dd>

Pointer to a NULL-terminated string that contains the name of the port to which the device is connected, such as LPT1.

</dd> <dt>

*pDevModeInput* \[in, optional\]
</dt> <dd>

Pointer to the DEVMODE structure that the operating system uses to initialize the property sheet fields.

This parameter is used only if the DM\_IN\_BUFFER flag is set in the *fMode* parameter. If DM\_IN\_BUFFER is not set, the operating system uses the printer's default DEVMODE structure.

</dd> <dt>

*pProfile* \[in, optional\]
</dt> <dd>

Not used. Pointer to a NULL-terminated string that contains the name of the initialization file in which initialization information is recorded and read from.

</dd> <dt>

*fMode* 
</dt> <dd>

Specifies the operations that the function performs. If this parameter is zero, the **ExtDeviceMode** function returns the number of bytes required by the printer driver's DEVMODE structure. Otherwise, this parameter can be set to one or more of the following flag values.



| Flag                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DM\_COPY<br/>       | Write the driver's current settings to the DEVMODE structure pointed to by the *pDevModeOutput* parameter. The calling application must allocate a buffer large enough to contain the information. If this flag is not set, *pDevModeOutput* can be **NULL**.<br/>                                                                                                                                                                                                                      |
| DM\_IN\_BUFFER<br/> | Merge the printer driver's current print settings with the settings in the DEVMODE structure pointed to by the *pDevModeInput* parameter. This occurs before prompting, copying, or updating. The function updates the structure only for those members specified by the DEVMODE structure's **dmFields** member. In cases of conflict during the merge, the settings in the DEVMODE structure pointed to by *pDevModeInput* override the printer driver's current print settings.<br/> |
| DM\_UPDATE<br/>     | Display a property sheet to allow the user to modify printer properties, and then write the driver's current "per user" settings to the user's hive in the registry. <br/>                                                                                                                                                                                                                                                                                                              |



 

</dd> </dl>

## Return value

If the *wMode* parameter is zero, the function returns the size, in bytes, of the DEVMODE structure required to contain the printer-driver initialization data. Note that this value can be larger than the size of a DEVMODE structure if the printer driver appends private data to the structure. If the function displays the initialization-dialog box, the return value is either IDOK or IDCANCEL, depending on which button the user chose. If the function does not display the dialog box and was successful, the return value is IDOK. The return value is less than zero if the function failed.

## Remarks

The **ExtDeviceMode** function calls the **DocumentProperties** function (described in the Windows SDK documentation) to display a property sheet that allows a user to select printer options such as paper size, paper orientation, and output quality. Printer drivers written for Windows 3.x and Windows 9x use this function.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Winspool.lib</dt> </dl>                    |
| DLL<br/>             | <dl> <dt>WinSpool.drv</dt> </dl>                    |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ExtDeviceMode%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




