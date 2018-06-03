---
Description: A port monitor UI DLL's AddPortUI function adds a printer port, then obtains port configuration information from the user and sends it to the port monitor server DLL.
ms.assetid: 8305ab0c-0783-4597-9e2c-dfd9cbc843d1
title: AddPortUI function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddPortUI function

A port monitor UI DLL's **AddPortUI** function adds a printer port, then obtains port configuration information from the user and sends it to the port monitor server DLL.

## Syntax


```C++
BOOL WINAPI pfnAddPortUI(
  _In_opt_  PCWSTR pszServer,
  _In_      HWND   hWnd,
  _In_      PCWSTR pszPortNameIn,
  _Out_opt_ PWSTR  *ppszPortNameOut
);
```



## Parameters

<dl> <dt>

*pszServer* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a string representing a server name, or **NULL** if the printer is local.

</dd> <dt>

*hWnd* \[in\]
</dt> <dd>

Caller-supplied handle of the window that should be used as the parent for dialog boxes. If **NULL**, no dialog boxes should be displayed.

</dd> <dt>

*pszPortNameIn* \[in\]
</dt> <dd>

Caller-supplied pointer to a string representing the name of the monitor. Can be **NULL**.

</dd> <dt>

*ppszPortNameOut* \[out, optional\]
</dt> <dd>

Caller-supplied pointer to a location to receive a port name string. Can be **NULL**, in which case a name is not returned.

</dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**. Otherwise SetLastError should be called to specify an error code, and the function should return **FALSE**. If the operation is canceled by the user or is unsupported, the function should call SetLastError(ERROR\_CANCELLED), then return **FALSE**.

## Remarks

Port monitor UI DLLs are required to define an **AddPortUI** function and include the function's address in a [**MONITORUI**](monitorui.md) structure.

The spooler calls **AddPortUI** from within its AddPort function. The first three arguments received by **AddPortUI** are the arguments received by AddPort. (The AddPort function is described in the Microsoft Windows SDK documentation.)

The function should perform the following operations:

1.  Call OpenPrinter, specifying a printer name with the following format:<dl> \\\\*ServerName*\\,XcvMonitor*MonitorName*  
    </dl>

    where *ServerName* and *MonitorName* are the server and monitor names received as **AddPortUI** function arguments.

    The call to OpenPrinter requires a PRINTER\_DEFAULTS structure, which is described in the Windows SDK documentation. The structure's **DesiredAccess** member must be set to SERVER\_ACCESS\_ADMINISTER. Its **pDatatype** and **pDevMode** members can be **NULL**.

    This call causes the print monitor server DLL's [**XcvOpenPort**](https://www.bing.com/search?q=**XcvOpenPort**) function to be called.

2.  Obtain a port name from the user by displaying a dialog box.

3.  Call [**XcvData**](https://www.bing.com/search?q=**XcvData**), specifying the following input arguments:

    -   The handle received from OpenPrinter
    -   The port name received from the user
    -   A customized data name string, such as "PortExists"

    This call causes the server DLL's [**XcvDataPort**](https://www.bing.com/search?q=**XcvDataPort**) function to be called. The **XcvDataPort** function should return a value that indicates whether the specified port name has already been used. If it has, the UI DLL should request another name from the user and call [**XcvData**](https://www.bing.com/search?q=**XcvData**) again.

4.  After a valid new port name has been received, call [**XcvData**](https://www.bing.com/search?q=**XcvData**) again, this time specifying the following input arguments:

    -   The handle received from OpenPrinter
    -   The validated port name received from the user
    -   A data name string of "AddPort"

    This call causes the server DLL's [**XcvDataPort**](https://www.bing.com/search?q=**XcvDataPort**) function to be called again.

5.  Obtain port configuration parameters from the user by displaying a dialog box.

6.  Call [**XcvData**](https://www.bing.com/search?q=**XcvData**) one or more times, specifying customized data name strings, to send each configuration parameter to the server DLL. Each **XcvData** call causes the server's [**XcvDataPort**](https://www.bing.com/search?q=**XcvDataPort**) function to be called.

7.  Call ClosePrinter, specifying the handle received from OpenPrinter. This causes the server DLL's [**XcvClosePort**](https://www.bing.com/search?q=**XcvClosePort**) function to be called.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**MONITORUI**](monitorui.md)
</dt> <dt>

[**XcvOpenPort**](https://www.bing.com/search?q=**XcvOpenPort**)
</dt> <dt>

[**XcvClosePort**](https://www.bing.com/search?q=**XcvClosePort**)
</dt> <dt>

[**XcvData**](https://www.bing.com/search?q=**XcvData**)
</dt> <dt>

[**XcvDataPort**](https://www.bing.com/search?q=**XcvDataPort**)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20AddPortUI%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





