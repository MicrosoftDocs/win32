---
Description: 'A port monitor UI DLL''s DeletePortUI function deletes a printer port.'
ms.assetid: 'a556ec29-9149-4185-b4b3-9aae803e62f7'
title: DeletePortUI function
---

# DeletePortUI function

A port monitor UI DLL's **DeletePortUI** function deletes a printer port.

## Syntax


```C++
BOOL WINAPI pfnDeletePortUI(
  _In_opt_ PCWSTR pszServer,
  _In_     HWND   hWnd,
  _In_     PCWSTR pszPortName
);
```



## Parameters

<dl> <dt>

*pszServer* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a string representing a server name, or **NULL** if the printer is local. (The port monitor can ignore this parameter.)

</dd> <dt>

*hWnd* \[in\]
</dt> <dd>

Caller-supplied handle of the window that should be used as the parent for dialog boxes. If **NULL**, no dialog boxes should be displayed.

</dd> <dt>

*pszPortName* \[in\]
</dt> <dd>

Caller-supplied pointer to a string representing the name of the port to be deleted.

</dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**. Otherwise it should return **FALSE**. If the operation is canceled by the user or is unsupported, the function should call SetLastError(ERROR\_CANCELLED), then return **FALSE**.

## Remarks

Port monitor UI DLLs are required to define a **DeletePortUI** function and include the function's address in a [**MONITORUI**](monitorui.md) structure.

The spooler calls **DeletePortUI** from within its **DeletePort** function. The arguments received by **DeletePortUI** are the arguments received by **DeletePort**. (The **DeletePort** function is described in the Microsoft Windows SDK documentation.)

The function should perform the following operations:

1.  Call **OpenPrinter**, specifying a printer name with the following format:<dl> **\\\\***ServerName***\\,XcvPort***PortName*  
    </dl>

    where *ServerName* and *PortName* are the server and port names received as **DeletePortUI** function arguments.

    The call to **OpenPrinter** requires a PRINTER\_DEFAULTS structure, which is described in the Windows SDK documentation. The structure's **DesiredAccess** member must be set to SERVER\_ACCESS\_ADMINISTER. Its **pDatatype** and **pDevMode** members can be **NULL**.

    This call causes the print monitor server DLL's [**XcvOpenPort**](print.xcvopenport) function to be called.

2.  Call [**XcvData**](print.xcvdata), specifying the following input arguments:

    -   The handle received from **OpenPrinter**
    -   The port name received as a function argument
    -   A data name string of "DeletePort"

    This call causes the server DLL's [**XcvClosePort**](print.xcvcloseport) function to be called.

3.  If user interaction is required, obtain information from the user by displaying a dialog box and then call [**XcvData**](print.xcvdata), specifying customized data name strings, to send the information to the server DLL. The **XcvData** call causes the server's [**XcvDataPort**](print.xcvdataport) function to be called.

4.  Call **ClosePrinter**, specifying the handle received from **OpenPrinter**. This causes the server DLL's [**XcvClosePort**](print.xcvcloseport) function to be called.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**XcvOpenPort**](print.xcvopenport)
</dt> <dt>

[**XcvClosePort**](print.xcvcloseport)
</dt> <dt>

[**XcvData**](print.xcvdata)
</dt> <dt>

[**XcvDataPort**](print.xcvdataport)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DeletePortUI%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





