---
description: The AddPrinter function adds a printer to the list of supported printers for a specified server.
ms.assetid: ffc4fee8-46c6-47ad-803d-623bf8efdefd
title: AddPrinter function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AddPrinter
- AddPrinterA
- AddPrinterW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# AddPrinter function

The **AddPrinter** function adds a printer to the list of supported printers for a specified server.

## Syntax


```C++
HANDLE AddPrinter(
  _In_ LPTSTR *pName,
  _In_ DWORD  Level,
  _In_ LPBYTE pPrinter
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server on which the printer should be installed. If this string is **NULL**, the printer is installed locally.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The version of the structure to which *pPrinter* points. This value must be 2.

</dd> <dt>

*pPrinter* \[in\]
</dt> <dd>

A pointer to a [**PRINTER\_INFO\_2**](printer-info-2.md) structure that contains information about the printer. You must specify non-**NULL** values for the **pPrinterName**, **pPortName**, **pDriverName**, and **pPrintProcessor** members of this structure before calling **AddPrinter**.

</dd> </dl>

## Return value

If the function succeeds, the return value is a handle (not thread safe) to a new printer object. When you are finished with the handle, pass it to the [**ClosePrinter**](closeprinter.md) function to close it.

If the function fails, the return value is **NULL**.

## Remarks

Do not call this method in [**DllMain**](/windows/desktop/Dlls/dllmain).

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The caller must have the [SeLoadDriverPrivilege](/windows/desktop/SecAuthZ/authorization-constants).

The returned handle is not thread safe. If callers need to use it concurrently on multiple threads, they must provide custom synchronization access to the printer handle using the [Synchronization Functions](/windows/desktop/Sync/synchronization-functions). To avoid writing custom code the application can open a printer handle on each thread, as needed.

The following are the members of the [**PRINTER\_INFO\_2**](printer-info-2.md) structure that can be set before the **AddPrinter** function is called:

-   **Attributes**
-   **pPrintProcessor**
-   **DefaultPriority**
-   **Priority**
-   **pComment**
-   **pSecurityDescriptor**
-   **pDatatype**
-   **pSepFile**
-   **pDevMode**
-   **pShareName**
-   **pLocation**
-   **StartTime**
-   **pParameters**
-   **UntilTime**

The **Status**, **cJobs**, and **AveragePPM** members of the [**PRINTER\_INFO\_2**](printer-info-2.md) structure are reserved for use by the [**GetPrinter**](getprinter.md) function. They must not be set before calling **AddPrinter**.

If **pSecurityDescriptor** is **NULL**, the system assigns a default security descriptor to the printer. The default security descriptor has the following permissions.



| Value                          | Description                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administrators and Power Users | Full control on the print queue. This means members of these groups can print, manage the queue (can delete the queue, change any setting of the queue, including the security descriptor), and manage the print jobs of all users (delete, pause, resume, restart jobs).Note that Power Users do not exist before Windows XP Professional.<br/> |
| Creator/Owner                  | Can manage own jobs. This means that user who submit jobs can manage (delete, pause, resume, restart) their own jobs.                                                                                                                                                                                                                                  |
| Everyone                       | Execute and standard read control. This means that members of the everyone group can print and read properties of the print queue.                                                                                                                                                                                                                     |



 

After an application creates a printer object with the **AddPrinter** function, it must use the [**PrinterProperties**](printerproperties.md) function to specify the correct settings for the printer driver associated with the printer object.

The **AddPrinter** function returns an error if a printer object with the same name already exists, unless that object is marked as pending deletion. In that case, the existing printer is not deleted, and the **AddPrinter** creation parameters are used to change the existing printer settings (as if the application had used the [**SetPrinter**](setprinter.md) function).

Use the [**EnumPrintProcessors**](enumprintprocessors.md) function to enumerate the set of print processors installed on a server. Use the [**EnumPrintProcessorDatatypes**](enumprintprocessordatatypes.md) function to enumerate the set of data types that a print processor supports. Use the [**EnumPorts**](enumports.md) function to enumerate the set of available ports. Use the [**EnumPrinterDrivers**](enumprinterdrivers.md) function to enumerate the installed printer drivers.

The caller of the **AddPrinter** function must have SERVER\_ACCESS\_ADMINISTER access to the server on which the printer is to be created. The handle returned by the function will have PRINTER\_ALL\_ACCESS permission, and can be used to perform administrative operations on the printer.

If the **DrvPrinterEvent** function is passed the PRINTER\_EVENT\_FLAG\_NO\_UI flag, the driver should not use a UI call during **DrvPrinterEvent**. To do UI-related jobs, the installer should either use the **VendorSetup** entry in the printer's .inf file or, for Plug and Play devices, the installer can use a device-specific co-installer. For more information about **VendorSetup**, see the Microsoft Windows Driver Development Kit (DDK).

The Internet Connection Firewall (ICF) blocks printer ports by default, but an exception for File and Print Sharing is enabled when you run **AddPrinter**.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **AddPrinterW** (Unicode) and **AddPrinterA** (ANSI)<br/>                                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**ClosePrinter**](closeprinter.md)
</dt> <dt>

[**DeletePrinter**](deleteprinter.md)
</dt> <dt>

[**EnumPorts**](enumports.md)
</dt> <dt>

[**EnumPrinterDrivers**](enumprinterdrivers.md)
</dt> <dt>

[**EnumPrintProcessors**](enumprintprocessors.md)
</dt> <dt>

[**EnumPrintProcessorDatatypes**](enumprintprocessordatatypes.md)
</dt> <dt>

[**GetPrinter**](getprinter.md)
</dt> <dt>

[**PRINTER\_INFO\_2**](printer-info-2.md)
</dt> <dt>

[**PrinterProperties**](printerproperties.md)
</dt> <dt>

[**SetPrinter**](setprinter.md)
</dt> </dl>

 

