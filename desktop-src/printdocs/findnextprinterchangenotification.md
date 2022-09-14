---
description: The FindNextPrinterChangeNotification function retrieves information about the most recent change notification for a change notification object associated with a printer or print server.
ms.assetid: ea7774ae-361f-41e4-bbc6-3f100028b22a
title: FindNextPrinterChangeNotification function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FindNextPrinterChangeNotification
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# FindNextPrinterChangeNotification function

The **FindNextPrinterChangeNotification** function retrieves information about the most recent change notification for a change notification object associated with a printer or print server. Call this function when a wait operation on the change notification object is satisfied.

The function also resets the change notification object to the not-signaled state. You can then use the object in another wait operation to continue monitoring the printer or print server. The operating system will set the object to the signaled state the next time one of a specified set of changes occurs to the printer or print server. The [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md) function creates the change notification object and specifies the set of changes to be monitored.

## Syntax


```C++
BOOL FindNextPrinterChangeNotification(
  _In_      HANDLE hChange,
  _Out_opt_ PDWORD pdwChange,
  _In_opt_  LPVOID pPrinterNotifyOptions,
  _Out_opt_ LPVOID *ppPrinterNotifyInfo
);
```



## Parameters

<dl> <dt>

*hChange* \[in\]
</dt> <dd>

A handle to a change notification object associated with a printer or print server. You obtain such a handle by calling the [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md) function. The operating system sets this change notification object to the signaled state when it detects one of the changes specified in the object's change notification filter.

</dd> <dt>

*pdwChange* \[out, optional\]
</dt> <dd>

A pointer to a variable whose bits are set to indicate the changes that occurred to cause the most recent notification. The bit flags that might be set correspond to those specified in the *fdwFilter* parameter of the [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md) call. The system sets one or more of the following bit flags.



| Value                                                                                                                                                                                                                                             | Meaning                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <span id="PRINTER_CHANGE_ADD_FORM"></span><span id="printer_change_add_form"></span><dl> <dt>**PRINTER\_CHANGE\_ADD\_FORM**</dt> </dl>                                                     | A form was added to the server.<br/>                |
| <span id="PRINTER_CHANGE_ADD_JOB"></span><span id="printer_change_add_job"></span><dl> <dt>**PRINTER\_CHANGE\_ADD\_JOB**</dt> </dl>                                                        | A print job was sent to the printer.<br/>           |
| <span id="PRINTER_CHANGE_ADD_PORT"></span><span id="printer_change_add_port"></span><dl> <dt>**PRINTER\_CHANGE\_ADD\_PORT**</dt> </dl>                                                     | A port or monitor was added to the server.<br/>     |
| <span id="PRINTER_CHANGE_ADD_PRINT_PROCESSOR"></span><span id="printer_change_add_print_processor"></span><dl> <dt>**PRINTER\_CHANGE\_ADD\_PRINT\_PROCESSOR**</dt> </dl>                   | A print processor was added to the server.<br/>     |
| <span id="PRINTER_CHANGE_ADD_PRINTER"></span><span id="printer_change_add_printer"></span><dl> <dt>**PRINTER\_CHANGE\_ADD\_PRINTER**</dt> </dl>                                            | A printer was added to the server.<br/>             |
| <span id="PRINTER_CHANGE_ADD_PRINTER_DRIVER"></span><span id="printer_change_add_printer_driver"></span><dl> <dt>**PRINTER\_CHANGE\_ADD\_PRINTER\_DRIVER**</dt> </dl>                      | A printer driver was added to the server.<br/>      |
| <span id="PRINTER_CHANGE_CONFIGURE_PORT"></span><span id="printer_change_configure_port"></span><dl> <dt>**PRINTER\_CHANGE\_CONFIGURE\_PORT**</dt> </dl>                                   | A port was configured on the server.<br/>           |
| <span id="PRINTER_CHANGE_DELETE_FORM"></span><span id="printer_change_delete_form"></span><dl> <dt>**PRINTER\_CHANGE\_DELETE\_FORM**</dt> </dl>                                            | A form was deleted from the server.<br/>            |
| <span id="PRINTER_CHANGE_DELETE_JOB"></span><span id="printer_change_delete_job"></span><dl> <dt>**PRINTER\_CHANGE\_DELETE\_JOB**</dt> </dl>                                               | A job was deleted.<br/>                             |
| <span id="PRINTER_CHANGE_DELETE_PORT"></span><span id="printer_change_delete_port"></span><dl> <dt>**PRINTER\_CHANGE\_DELETE\_PORT**</dt> </dl>                                            | A port or monitor was deleted from the server.<br/> |
| <span id="PRINTER_CHANGE_DELETE_PRINT_PROCESSOR"></span><span id="printer_change_delete_print_processor"></span><dl> <dt>**PRINTER\_CHANGE\_DELETE\_PRINT\_PROCESSOR**</dt> </dl>          | A print processor was deleted from the server.<br/> |
| <span id="PRINTER_CHANGE_DELETE_PRINTER"></span><span id="printer_change_delete_printer"></span><dl> <dt>**PRINTER\_CHANGE\_DELETE\_PRINTER**</dt> </dl>                                   | A printer was deleted.<br/>                         |
| <span id="PRINTER_CHANGE_DELETE_PRINTER_DRIVER"></span><span id="printer_change_delete_printer_driver"></span><dl> <dt>**PRINTER\_CHANGE\_DELETE\_PRINTER\_DRIVER**</dt> </dl>             | A printer driver was deleted from the server.<br/>  |
| <span id="PRINTER_CHANGE_FAILED_CONNECTION_PRINTER"></span><span id="printer_change_failed_connection_printer"></span><dl> <dt>**PRINTER\_CHANGE\_FAILED\_CONNECTION\_PRINTER**</dt> </dl> | A printer connection has failed.<br/>               |
| <span id="PRINTER_CHANGE_SET_FORM"></span><span id="printer_change_set_form"></span><dl> <dt>**PRINTER\_CHANGE\_SET\_FORM**</dt> </dl>                                                     | A form was set on the server.<br/>                  |
| <span id="PRINTER_CHANGE_SET_JOB"></span><span id="printer_change_set_job"></span><dl> <dt>**PRINTER\_CHANGE\_SET\_JOB**</dt> </dl>                                                        | A job was set.<br/>                                 |
| <span id="PRINTER_CHANGE_SET_PRINTER"></span><span id="printer_change_set_printer"></span><dl> <dt>**PRINTER\_CHANGE\_SET\_PRINTER**</dt> </dl>                                            | A printer was set.<br/>                             |
| <span id="PRINTER_CHANGE_SET_PRINTER_DRIVER"></span><span id="printer_change_set_printer_driver"></span><dl> <dt>**PRINTER\_CHANGE\_SET\_PRINTER\_DRIVER**</dt> </dl>                      | A printer driver was set.<br/>                      |
| <span id="PRINTER_CHANGE_WRITE_JOB"></span><span id="printer_change_write_job"></span><dl> <dt>**PRINTER\_CHANGE\_WRITE\_JOB**</dt> </dl>                                                  | Job data was written.<br/>                          |
| <span id="PRINTER_CHANGE_TIMEOUT"></span><span id="printer_change_timeout"></span><dl> <dt>**PRINTER\_CHANGE\_TIMEOUT**</dt> </dl>                                                         | The job timed out.<br/>                             |
| <span id="PRINTER_CHANGE_SERVER"></span><span id="printer_change_server"></span><dl> <dt>**PRINTER\_CHANGE\_SERVER**</dt> </dl>                                                            | Windows 7: A change occurred on the server.<br/>    |



 

</dd> <dt>

*pPrinterNotifyOptions* \[in, optional\]
</dt> <dd>

A pointer to a [**PRINTER\_NOTIFY\_OPTIONS**](printer-notify-options.md) structure. Set the **Flags** member of this structure to **PRINTER\_NOTIFY\_OPTIONS\_REFRESH**, to cause the function to return the current data for all monitored printer information fields. The function ignores all other members of the structure. This parameter can be **NULL**.

</dd> <dt>

*ppPrinterNotifyInfo* \[out, optional\]
</dt> <dd>

A pointer to a pointer variable that receives a pointer to a system-allocated, read-only buffer. Call the [**FreePrinterNotifyInfo**](freeprinternotifyinfo.md) function to free the buffer when you are finished with it. This parameter can be **NULL** if no information is required.

The buffer contains a [**PRINTER\_NOTIFY\_INFO**](printer-notify-info.md) structure, which contains an array of [**PRINTER\_NOTIFY\_INFO\_DATA**](printer-notify-info-data.md) structures. Each element of the array contains information about one of the fields specified in the *pPrinterNotifyOptions* parameter of the [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md) call. Typically, the function provides data only for the fields that changed to cause the most recent notification. However, if the structure pointed to by the *pPrinterNotifyOptions* parameter specifies **PRINTER\_NOTIFY\_OPTIONS\_REFRESH**, the function provides data for all monitored fields.

If the **PRINTER\_NOTIFY\_INFO\_DISCARDED** bit is set in the **Flags** member of the [**PRINTER\_NOTIFY\_INFO**](printer-notify-info.md) structure, an overflow or error occurred, and notifications may have been lost. In this case, no additional notifications will be sent until you make a second **FindNextPrinterChangeNotification** call that specifies **PRINTER\_NOTIFY\_OPTIONS\_REFRESH**.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

Call the **FindNextPrinterChangeNotification** function after a wait operation on a notification object created by [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md) has been satisfied. Calling **FindNextPrinterChangeNotification** lets you obtain information about the change that satisfied the wait operation, and resets the notification object so it can be signaled when the next change occurs.

With one exception, do not call the **FindNextPrinterChangeNotification** function if the change notification object is not in the signaled state. If a wait function returns the value **WAIT\_TIMEOUT**, the change object is not in the signaled state. Call the **FindNextPrinterChangeNotification** function only if the wait function succeeds without timing out. The exception is when **FindNextPrinterChangeNotification** is called with the **PRINTER\_NOTIFY\_OPTIONS\_REFRESH** bit set in the *pPrinterNotifyOptions* parameter. Note that even when this flag is set, it is still possible for the **PRINTER\_NOTIFY\_INFO\_DISCARDED** flag to be set in the *ppPrinterNotifyInfo* parameter.

To continue monitoring the printer or print server for changes, repeat the cycle of calling one of the [wait functions](/windows/desktop/Sync/wait-functions) , and then calling the **FindNextPrinterChangeNotification** function to examine the change and reset the notification object.

**FindNextPrinterChangeNotification** may combine multiple changes to the same printer information field into a single notification. When this occurs, the function typically collapses all changes for the field into a single entry in the array of [**PRINTER\_NOTIFY\_INFO\_DATA**](printer-notify-info-data.md) structures in *ppPrinterNotifyInfo*; the single entry reports only the most current information. However, for some job and printer information fields, the function can return multiple array entries for the same field. In this case, the last array entry for the field reports the current data, and the earlier entries contain the data for the intermediate stages.

When you no longer need the change notification object, close it by calling the [**FindClosePrinterChangeNotification**](findcloseprinterchangenotification.md) function.

> [!Note]  
> In Windows XP with Service Pack 2 (SP2) and later, the Internet Connection Firewall (ICF) blocks printer ports by default, but an exception for File and Print Sharing can be enabled. If a user makes a printer connection to another machine, and the exception is not enabled, then the user will not receive printer change notifications from the server. A machine admin will have to enable exception.

 

## Examples

The following code sample illustrates how you might monitor printer status by using these functions.


```C++
// Get change notification handle for the printer   
chgObject = FindFirstPrinterChangeNotification( 
                hPrinter, 
                PRINTER_CHANGE_JOB, 
                0, 
                NULL); 

if (chgObject != INVALID_HANDLE_VALUE) {
    while (bKeepMonitoring) {
        // Wait for the change notification 
        WaitForSingleObject(chgObject, INFINITE);

        fcnreturn = FindNextPrinterChangeNotification(
                        chgObject, 
                        pdwChange, 
                        NULL, 
                        NULL);

        if (fcnreturn) {
            // Check value of *pdwChange and 
            //  deal with the indicated change 
        }
        // Insert some mechanism to stop monitoring
        //  such as: 
        //
        // if (something happens) {
        //     bKeepMonitoring = false; 
        // }
        //
    }
    // Close Printer Change Notification handle when finished. 
    FindClosePrinterChangeNotification(chgObject);
} else {
    // Unable to open printer change notification handle 
    dwStatus = GetLastError();
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**FindClosePrinterChangeNotification**](findcloseprinterchangenotification.md)
</dt> <dt>

[**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md)
</dt> <dt>

[**PRINTER\_NOTIFY\_INFO**](printer-notify-info.md)
</dt> <dt>

[**PRINTER\_NOTIFY\_INFO\_DATA**](printer-notify-info-data.md)
</dt> <dt>

[**PRINTER\_NOTIFY\_OPTIONS**](printer-notify-options.md)
</dt> </dl>

 

