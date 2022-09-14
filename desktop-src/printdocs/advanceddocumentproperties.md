---
description: The AdvancedDocumentProperties function displays a printer-configuration dialog box for the specified printer, allowing the user to configure that printer.
ms.assetid: 29e33f34-f6ec-4989-b076-e1fef8eb5bc4
title: AdvancedDocumentProperties function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AdvancedDocumentProperties
- AdvancedDocumentPropertiesA
- AdvancedDocumentPropertiesW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# AdvancedDocumentProperties function

The **AdvancedDocumentProperties** function displays a printer-configuration dialog box for the specified printer, allowing the user to configure that printer.

This function is a special case of the [**DocumentProperties**](documentproperties.md) function. For more details, see the Remarks section.

## Syntax


```C++
LONG AdvancedDocumentProperties(
  _In_  HWND     hWnd,
  _In_  HANDLE   hPrinter,
  _In_  LPTSTR   pDeviceName,
  _Out_ PDEVMODE pDevModeOutput,
  _In_  PDEVMODE pDevModeInput
);
```



## Parameters

<dl> <dt>

*hWnd* \[in\]
</dt> <dd>

A handle to the parent window of the printer-configuration dialog box.

</dd> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to a printer object. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*pDeviceName* \[in\]
</dt> <dd>

A pointer to a null-terminated string specifying the name of the device for which a printer-configuration dialog box should be displayed.

</dd> <dt>

*pDevModeOutput* \[out\]
</dt> <dd>

A pointer to a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure that will contain the configuration data specified by the user.

</dd> <dt>

*pDevModeInput* \[in\]
</dt> <dd>

A pointer to a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure that contains the configuration data used to initialize the controls of the printer-configuration dialog box.

</dd> </dl>

## Return value

If the [**DocumentProperties**](documentproperties.md) function with these parameters is successful, the return value of **AdvancedDocumentProperties** is 1. Otherwise, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

This function can only display the printer-configuration dialog box so a user can configure it. For more control, use [**DocumentProperties**](documentproperties.md). The input parameters for this function are passed directly to **DocumentProperties** and the *fMode* value is set to DM\_IN\_BUFFER \| DM\_IN\_PROMPT \| DM\_OUT\_BUFFER. Unlike **DocumentProperties**, this function only returns 1 or 0. Thus, you cannot determine the required size of [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) by setting *pDevMode* to zero.

An application can obtain the name pointed to by the *pDeviceName* parameter by calling the [**GetPrinter**](getprinter.md) function and then examining the **pPrinterName** member of the [**PRINTER\_INFO\_2**](printer-info-2.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **AdvancedDocumentPropertiesW** (Unicode) and **AdvancedDocumentPropertiesA** (ANSI)<br/>           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPrinter**](addprinter.md)
</dt> <dt>

[**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea)
</dt> <dt>

[**DocumentProperties**](documentproperties.md)
</dt> <dt>

[**GetPrinter**](getprinter.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**PRINTER\_INFO\_2**](printer-info-2.md)
</dt> </dl>

 

 




