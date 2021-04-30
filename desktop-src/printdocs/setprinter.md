---
description: The SetPrinter function sets the data for a specified printer or sets the state of the specified printer by pausing printing, resuming printing, or clearing all print jobs.
ms.assetid: 'ade367c5-20d6-4da9-bb52-ce6768cf7537'
title: SetPrinter function (WinSpool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetPrinter
- SetPrinterA
- SetPrinterW
api_type: 
- DllExport
api_location: 
- WinSpool.drv
- Ext-MS-Win-printer-WinSpool-l1-1-0.dll
- Ext-MS-Win-printer-WinSpool-l1-1-1.dll
- Ext-MS-Win-Printer-WinSpool-l1-1-2.dll
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# SetPrinter function

The **SetPrinter** function sets the data for a specified printer or sets the state of the specified printer by pausing printing, resuming printing, or clearing all print jobs.

## Syntax


```C++
BOOL SetPrinter(
  _In_ HANDLE hPrinter,
  _In_ DWORD  Level,
  _In_ LPBYTE pPrinter,
  _In_ DWORD  Command
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer. Use the [**OpenPrinter**](openprinter.md), [**OpenPrinter2**](openprinter2.md), or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The type of data that the function stores into the buffer pointed to by *pPrinter*. If the *Command* parameter is not equal to zero, the *Level* parameter must be zero.

This value can be 0, 2, 3, 4, 5, 6, 7, 8, or 9.

</dd> <dt>

*pPrinter* \[in\]
</dt> <dd>

A pointer to a buffer containing data to set for the printer, or containing information for the command specified by the *Command* parameter. The type of data in the buffer is determined by the value of *Level*.



| Level                                                                                                | Structure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | If the *Command* parameter is **PRINTER\_CONTROL\_SET\_STATUS**, *pPrinter* must contain a **DWORD** value that specifies the new printer status to set. For a list of the possible status values, see the **Status** member of the [**PRINTER\_INFO\_2**](printer-info-2.md) structure. Note that **PRINTER\_STATUS\_PAUSED** and **PRINTER\_STATUS\_PENDING\_DELETION** are not valid status values to set.<br/> If *Level* is 0, but the *Command* parameter is not **PRINTER\_CONTROL\_SET\_STATUS**, *pPrinter* must be **NULL**.<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | A [**PRINTER\_INFO\_2**](printer-info-2.md) structure containing detailed information about the printer.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | A [**PRINTER\_INFO\_3**](printer-info-3.md) structure containing the printer's security information.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | A [**PRINTER\_INFO\_4**](printer-info-4.md) structure containing minimal printer information, including the name of the printer, the name of the server, and whether the printer is remote or local.<br/>                                                                                                                                                                                                                                                                                                                                         |
| <span id="5"></span><dl> <dt>**5**</dt> </dl> | A [**PRINTER\_INFO\_5**](printer-info-5.md) structure containing printer information such as printer attributes and time-out settings.<br/>                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="6"></span><dl> <dt>**6**</dt> </dl> | A [**PRINTER\_INFO\_6**](printer-info-6.md) structure specifying the status value of a printer.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="7"></span><dl> <dt>**7**</dt> </dl> | A [**PRINTER\_INFO\_7**](printer-info-7.md) structure. The *dwAction* member of this structure indicates whether **SetPrinter** should publish, unpublish, re-publish, or update the printer's data in the directory service.<br/>                                                                                                                                                                                                                                                                                                                |
| <span id="8"></span><dl> <dt>**8**</dt> </dl> | A [**PRINTER\_INFO\_8**](printer-info-8.md) structure specifying the global default printer settings.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="9"></span><dl> <dt>**9**</dt> </dl> | A [**PRINTER\_INFO\_9**](printer-info-9.md) structure specifying the per-user default printer settings.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

</dd> <dt>

*Command* \[in\]
</dt> <dd>

The action to perform.

If the *Level* parameter is nonzero, set the value of this parameter to zero. In this case, the printer retains its current state and the function reconfigures the printer data as specified by the *Level* and *pPrinter* parameters.

If the *Level* parameter is zero, set the value of this parameter to one of the following values.



| Value                                                                                                                                                                                                  | Meaning                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PRINTER_CONTROL_PAUSE"></span><span id="printer_control_pause"></span><dl> <dt>**PRINTER\_CONTROL\_PAUSE**</dt> </dl>                 | Pause the printer.<br/>                                                                                                                       |
| <span id="PRINTER_CONTROL_PURGE"></span><span id="printer_control_purge"></span><dl> <dt>**PRINTER\_CONTROL\_PURGE**</dt> </dl>                 | Delete all print jobs in the printer.<br/>                                                                                                    |
| <span id="PRINTER_CONTROL_RESUME"></span><span id="printer_control_resume"></span><dl> <dt>**PRINTER\_CONTROL\_RESUME**</dt> </dl>              | Resume a paused printer.<br/>                                                                                                                 |
| <span id="PRINTER_CONTROL_SET_STATUS"></span><span id="printer_control_set_status"></span><dl> <dt>**PRINTER\_CONTROL\_SET\_STATUS**</dt> </dl> | Set the printer status.<br/> Set the *pPrinter* parameter to a pointer to a **DWORD** value that specifies the new printer status.<br/> |



 

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

If *Level* is 7 and the publish action failed, **SetPrinter** returns **ERROR\_IO\_PENDING** and attempts to complete the action in the background. If *Level* is 7 and the update action failed, **SetPrinter** returns **ERROR\_FILE\_NOT\_FOUND**.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

You cannot use **SetPrinter** to change the default printer.

To modify the current printer settings, call the [**GetPrinter**](getprinter.md) function to retrieve the current settings into a [**PRINTER\_INFO\_2**](printer-info-2.md) structure, modify the members of that structure as necessary, and then call **SetPrinter**.

The **SetPrinter** function ignores the **pServerName**, **AveragePPM**, **Status**, and **cJobs** members of a [**PRINTER\_INFO\_2**](printer-info-2.md) structure.

Pausing a printer suspends scheduling of all print jobs for that printer, except for the one print job that may be currently printing. Print jobs can be submitted to a paused printer, but no jobs will be scheduled to print on that printer until printing is resumed. If a printer is cleared, all print jobs for that printer are deleted, except for the current print job.

If you use **SetPrinter** to modify the default [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure for a printer (globally setting the printer defaults), you must first call the [**DocumentProperties**](documentproperties.md) function to validate the **DEVMODE** structure.

For the [**PRINTER\_INFO\_2**](printer-info-2.md) and [**PRINTER\_INFO\_3**](printer-info-3.md) structures that contain a pointer to a security descriptor, the function can set only those components of the security descriptor that the caller has permission to modify. To set particular security descriptor components, you must specify the necessary access rights when you call the [**OpenPrinter**](openprinter.md) or [**OpenPrinter2**](openprinter2.md) function to retrieve a handle to the printer. The following table shows the access rights required to modify the various security descriptor components.



| Access permission            | Security descriptor component             |
|------------------------------|-------------------------------------------|
| **WRITE\_OWNER**             | Owner<br/> Primary group<br/> |
| **WRITE\_DAC**               | Discretionary access-control list (DACL)  |
| **ACCESS\_SYSTEM\_SECURITY** | System access-control list (SACL)         |



 

If the security descriptor contains a component that the caller does not have the access right to modify, **SetPrinter** fails. Those components of a security descriptor that you don't want to modify should be **NULL** or not be present, as appropriate. If you do not want to modify the security descriptor, and are calling **SetPrinter** with a [**PRINTER\_INFO\_2**](printer-info-2.md) structure, set the **pSecurityDescriptor** member of that structure to **NULL**.

The Internet Connection Firewall (ICF) blocks printer ports by default, but an exception for File and Print Sharing can be enabled. If **SetPrinter** is called by a machine admin, it enables the exception. If it is called by a non-admin and the exception has not already been enabled, the call fails.

You can use level 7 with the [**PRINTER\_INFO\_7**](printer-info-7.md) structure to publish, unpublish, or update directory service data for the printer. The directory service data for a printer includes all the data stored under the SPLDS\_\* keys by calls to the [**SetPrinterDataEx**](setprinterdataex.md) function for the printer. Before calling **SetPrinter**, set the **pszObjectGUID** member of **PRINTER\_INFO\_7** to **NULL** and set the *dwAction* member to one of the following values.



| Value                             | Description                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DSPRINT\_PUBLISH**<br/>   | Publishes the directory service data.<br/>                                                                                                                                                                                                                                                                                                                                        |
| **DSPRINT\_REPUBLISH**<br/> | The directory service data for the printer is unpublished and then published again, refreshing all properties in the published printer. Re-publishing also changes the GUID of the published printer. Use this value if you suspect the printer's published data has been corrupted.<br/>                                                                                         |
| **DSPRINT\_UNPUBLISH**<br/> | Unpublishes the directory service data.<br/>                                                                                                                                                                                                                                                                                                                                      |
| **DSPRINT\_UPDATE**<br/>    | Updates the directory service data. This is the same as **DSPRINT\_PUBLISH**, except that **SetPrinter** fails with **ERROR\_FILE\_NOT\_FOUND** if the printer is not already published.<br/> Use **DSPRINT\_UPDATE** to update published properties but not force publishing. Printer drivers should always use **DSPRINT\_UPDATE** rather than **DSPRINT\_PUBLISH**.<br/> |



 

**DSPRINT\_PENDING** is not a valid *dwAction* value for **SetPrinter**.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>WinSpool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>WinSpool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>WinSpool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **SetPrinterW** (Unicode) and **SetPrinterA** (ANSI)<br/>                                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPrinter**](addprinter.md)
</dt> <dt>

[**GetPrinter**](getprinter.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**OpenPrinter2**](openprinter2.md)
</dt> <dt>

[**PRINTER\_INFO\_2**](printer-info-2.md)
</dt> <dt>

[**PRINTER\_INFO\_3**](printer-info-3.md)
</dt> <dt>

[**PRINTER\_INFO\_4**](printer-info-4.md)
</dt> <dt>

[**PRINTER\_INFO\_5**](printer-info-5.md)
</dt> <dt>

[**PRINTER\_INFO\_6**](printer-info-6.md)
</dt> <dt>

[**PRINTER\_INFO\_7**](printer-info-7.md)
</dt> <dt>

[**PRINTER\_INFO\_8**](printer-info-8.md)
</dt> <dt>

[**PRINTER\_INFO\_9**](printer-info-9.md)
</dt> <dt>

[**SetPrinterDataEx**](setprinterdataex.md)
</dt> </dl>

 

 




