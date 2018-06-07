---
Description: A printer interface DLL's DrvConvertDevMode function converts a printer's DEVMODEW structure from one version to another.
ms.assetid: eb0402a8-22ce-417f-9b19-25b357451307
title: DrvConvertDevMode function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DrvConvertDevMode function

A printer interface DLL's **DrvConvertDevMode** function converts a printer's [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure from one version to another.

## Syntax


```C++
BOOL DrvConvertDevMode(
  _In_    LPTSTR   pPrinterName,
  _In_    PDEVMODE pdmIn,
  _Out_   PDEVMODE pdmOut,
  _Inout_ PLONG    pcbNeeded,
  _In_    DWORD    fMode
);
```



## Parameters

<dl> <dt>

*pPrinterName* \[in\]
</dt> <dd>

Caller-supplied pointer to a printer name string. For more information about this parameter, see the following Remarks section.

</dd> <dt>

*pdmIn* \[in\]
</dt> <dd>

Caller-supplied pointer to an input DEVMODEW structure. If *fMode* is CDM\_DRIVER\_DEFAULT, this pointer is **NULL**.

</dd> <dt>

*pdmOut* \[out\]
</dt> <dd>

Caller-supplied pointer to a buffer to receive an output DEVMODEW structure. If *fMode* is CDM\_CONVERT the buffer contains, on input, a valid DEVMODEW structure indicating the target driver version.

</dd> <dt>

*pcbNeeded* \[in, out\]
</dt> <dd>

Caller-supplied pointer to the size, in bytes, of the buffer pointed to by *pdmOut*. On output, the printer interface DLL should overwrite the received size value with the actual size of the converted DEVMODEW structure. If the received buffer is too small, the printer interface DLL should overwrite the received size value with the required buffer size.

</dd> <dt>

*fMode* \[in\]
</dt> <dd>

Caller-supplied bit flag indicating the type of operation to be performed. This can be one of the following flags:

<dl> <dt>

<span id="CDM_CONVERT"></span><span id="cdm_convert"></span>CDM\_CONVERT
</dt> <dd>

The function should convert the contents of the input DEVMODEW structure (pointed to by *pdmIn*) into a new DEVMODEW structure, and place the result in the DEVMODEW structure pointed to by *pdmOut*. The initial contents of the received output DEVMODEW structure (pointed to by *pdmOut*) should be used to determine the output version.

</dd> </dl>

<dl> <dt>

<span id="CDM_CONVERT351"></span><span id="cdm_convert351"></span>CDM\_CONVERT351
</dt> <dd>

The function should convert the contents of the input DEVMODEW structure (pointed to by *pdmIn*), creating an output DEVMODEW structure that is compatible with Windows NT 3.51, and place the result in the DEVMODEW structure pointed to by *pdmOut*.

If the driver does not support a DEVMODEW structure for Windows NT 3.51, the function should convert the input DEVMODEW to the current version.

</dd> </dl>

<dl> <dt>

<span id="CDM_DRIVER_DEFAULT"></span><span id="cdm_driver_default"></span>CDM\_DRIVER\_DEFAULT
</dt> <dd>

The function should copy the current version of its default DEVMODEW structure to the buffer pointed to by *pdmOut*.

</dd> </dl> </dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**; otherwise, it should call SetLastError to set an error code, and return **FALSE**.

## Remarks

In a client/server environment, a client might be running one version of the operating system or printer driver while the server (spooler) is running another, which means a printer's DEVMODEW structure definition might be inconsistent between the client and server. The **DrvConvertDevMode** function must be capable of performing conversions from one version of the printer's DEVMODEW structure to another.

When converting from one DEVMODEW version to another, both public and private DEVMODEW members must be included.

The printer name pointed to by *pPrinterName* can be used as an input argument to the **OpenPrinter** function (described in the Microsoft Windows SDK documentation), which can be called to obtain stored default values when the CDM\_DRIVER\_DEFAULT flag is received. Note that the printer name string must be not be modified in any way prior to a call to **OpenPrinter**. In addition, a call to **OpenPrinter** must be in the same thread as was used to call **DrvConvertDevMode**.

The function should verify that both *pdmIn* and *pdmOut* (if applicable) point to valid DEVMODEW structures. If they do not, the function should call SetLastError(ERROR\_INVALID\_PARAMETER) and return **FALSE**. If the output DEVMODEW size specified by *pcbNeeded* is too small, the driver should overwrite the size value supplied by *pcbNeeded* with the required buffer size, call SetLastError(ERROR\_INSUFFICIENT\_BUFFER), and return **FALSE**.

The **DrvConvertDevMode** function runs in the spooler's context and must therefore not display a user interface.

When **DrvConvertDevMode** is called with a **NULL** DEVMODEW structure pointer in the *pdmOut* parameter to get the buffer size, the driver is expected to set the last error to ERROR\_INSUFFICIENT\_BUFFER. If the last error is not set to this value, the spooler assumes a general error.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvConvertDevMode%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




