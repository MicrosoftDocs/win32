---
Description: A printer interface DLLs DrvPrinterEvent function is called by the print spooler when processing printer-specific events that might require action by the printer driver.
ms.assetid: 7566f92d-0e25-44bf-a2b3-587bb11a7d03
title: DrvPrinterEvent function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DrvPrinterEvent function

A printer interface DLL's **DrvPrinterEvent** function is called by the print spooler when processing printer-specific events that might require action by the printer driver.

## Syntax


```C++
BOOL DrvPrinterEvent(
  _In_ LPWSTR pPrinterName,
       int    DriverEvent,
       DWORD  Flags,
       LPARAM lParam
);
```



## Parameters

<dl> <dt>

*pPrinterName* \[in\]
</dt> <dd>

Caller-supplied pointer to a NULL-terminated printer name string. The string format can be \\\\*Machine*\\*PrinterName* to specify a remote printer, or *PrinterName* to specify a local printer.

</dd> <dt>

*DriverEvent* 
</dt> <dd>

Caller-supplied event code identifying the event. The following event codes are defined:



| Event Code                                       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRINTER\_EVENT\_ADD\_CONNECTION<br/>       | The spooler has just finished processing a call to its **AddPrinterConnection** function (described in the Microsoft Windows SDK documentation), which allows a client user to connect to a previously created remote printer.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PRINTER\_EVENT\_ATTRIBUTES\_CHANGED<br/>   | The attribute bits for a printer have changed. In response to an application's call to the **SetPrinter** function (described in the Windows SDK documentation), the spooler calls the printer driver's **DrvPrinterEvent** function, passing the event code in the call. When this event code is used, the *lParam* parameter points to a [**PRINTER\_EVENT\_ATTRIBUTES\_INFO**](printer-event-attributes-info.md) structure that describes the old and the new attributes.<br/>                                                                                                                                                                                                                                                                                                               |
| PRINTER\_EVENT\_CACHE\_DELETE<br/>         | The spooler is deleting the client's file cache.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PRINTER\_EVENT\_CACHE\_REFRESH<br/>        | The spooler is updating the client's cached files.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PRINTER\_EVENT\_CONFIGURATION\_CHANGE<br/> | Reserved.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PRINTER\_EVENT\_CONFIGURATION\_UPDATE<br/> | The printer configuration has changed. When this event code is used, the *lParam* parameter points to a Unicode string that contains a notification formatted according the Bidi Notification Schema.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PRINTER\_EVENT\_DELETE\_CONNECTION<br/>    | The spooler has just finished processing a call to its **DeletePrinterConnection** function (described in the Windows SDK documentation), which allows a client user to remove a printer connection.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PRINTER\_EVENT\_DELETE<br/>                | The spooler has just finished processing a call to its **DeletePrinter** function (described in the Windows SDK documentation), which allows an administrator to delete a printer instance.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PRINTER\_EVENT\_INITIALIZE<br/>            | The spooler has just finished processing a call to its **AddPrinter** function, which allows an administrator to make a printer available on a server, or its **SetPrinter** function, which allows an administrator to modify a printer's state. **AddPrinter** and **SetPrinter** are described in the Windows SDK documentation.<br/> In a client-side rendering connection, the client computer has just added the GUID printer.<br/> The PRINTER\_EVENT\_INITIALIZE event specifies a **NULL** lParam parameter value for **DrvPrinterEvent** calls on Windows Vista and earlier releases. For Windows 7 and later releases, the lParam parameter is a user token handle. The print drivers may use the returned token handle to query user data or impersonate the user. <br/> |



 

</dd> <dt>

*Flags* 
</dt> <dd>

Caller-supplied bit flag, defined as follows:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRINTER_EVENT_FLAG_NO_UI<br/></td>
<td>If set, the function <strong>mustnot</strong> display a user interface. During the installation of a print processor, print monitor, or printer driver, the only way in which a user interface is permitted is through the use of the <strong>VendorSetup</strong> directive. See [Printer INF File Entries](print.printer_inf_file_entries) and [Customized Printer Setup Operations](print.customized_printer_setup_operations) for more information.<br/>
<blockquote>
[!Important]<br />
: Be aware that <strong>VendorSetup</strong> is now deprecated and should not be used by any <em>new</em> v3 or v4 drivers that you develop. This information about <strong>VendorSetup</strong> is provided for reference only, or for the maintenance of existing v3 drivers that already use this INF directive.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

*lParam* 
</dt> <dd>

Not used unless the *DriverEvent* parameter is set to PRINTER\_EVENT\_ATTRIBUTES\_CHANGED. In this case, *lParam* contains the address of a PRINTER\_EVENT\_ATTRIBUTES\_INFO structure. (See the preceding description of the *DriverEvent* parameter.) For all other values of the *DriverEvent* parameter, the *lParam* parameter is **NULL**.

</dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**; otherwise, it should return **FALSE**. Currently, however, the only time the function's return value is checked is when the spooler has called **DrvPrinterEvent** during processing of the **AddPrinter** function, with *DriverEvent* set to PRINTER\_EVENT\_INITIALIZE. If **DrvPrinterEvent** returns **FALSE** in this case, the spooler does not create the printer and instead causes **AddPrinter** to fail.

## Remarks

All [printer interface DLLs](print.printer_interface_dll) must provide a **DrvPrinterEvent** function, and the function must support the PRINTER\_EVENT\_INITIALIZE event code. Support for all other event codes is optional.

Registry settings stored when handling a PRINTER\_EVENT\_INITIALIZE event should be stored under the HKEY\_LOCAL\_MACHINE key by calling **SetPrinterData**. For the PRINTER\_EVENT\_INITIALIZE and PRINTER\_EVENT\_DELETE event codes, the spooler verifies that the caller has administrative privilege and calls **DrvPrinterEvent** while impersonating the caller.

In contrast, if you need to store settings in the registry when handling a PRINTER\_EVENT\_ADD\_CONNECTION event, the printer interface DLL should write them under the HKEY\_CURRENT\_USER key so that they are stored on a per-user basis. Then if a user with a roaming profile logs onto another system, the connection follows the user. The **DrvPrinterEvent** function is called only when the user first makes the connection, and not when the user subsequently logs onto other systems using the roaming profile.

For the PRINTER\_EVENT\_ADD\_CONNECTION and PRINTER\_EVENT\_DELETE\_CONNECTION event codes, the **DrvPrinterEvent** function's execution context is the calling application (usually the Print Folder), and the function can display a user interface. For all other event codes, the execution context is the print spooler and a user interface cannot be displayed.

An example of a driver that might display a user interface when a connection is made is a FAX driver, which could prompt the user for the name and telephone number of the user (FAX sender), and save the information until the connection is deleted.

An example of the type of file that might be stored in a client cache is a large font-metrics file that contains too much information to be written to the registry. When the **DrvPrinterEvent** function's event code is PRINTER\_EVENT\_CACHE\_REFRESH, the printer interface DLL can reload the file from the server to ensure the cache is up to date.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvPrinterEvent%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




