---
Description: The MONITOR structure is obsolete and is supported only for compatibility reasons.
ms.assetid: e9d833cd-29d6-4c71-ba90-8d7dcf934420
title: MONITOR structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MONITOR structure

The MONITOR structure is obsolete and is supported only for compatibility reasons. New print monitors should implement [**MONITOR2**](monitor2.md) so that they can be used with print server clusters.

The MONITOR structure contains pointers to the functions defined by print monitors.

## Syntax


```C++
typedef struct _MONITOR {
  BOOL  (WINAPI *pfnEnumPorts)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pPorts, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL  (WINAPI *pfnOpenPort)(
      LPWSTR pName, 
      PHANDLE pHandle);
  BOOL  (WINAPI *pfnOpenPortEx)(
      LPWSTR pPortName, 
      LPWSTR pPrinterName, 
      PHANDLE pHandle, 
      struct _MONITOR * pMonitor);
  BOOL  (WINAPI *pfnStartDocPort)(
      HANDLE hPort, 
      LPWSTR pPrinterName, 
      DWORD JobId, 
      DWORD Level, 
      LPBYTE pDocInfo);
  BOOL  (WINAPI *pfnWritePort)(
      HANDLE hPort, 
      LPBYTE pBuffer, 
      DWORD cbBuf, 
      LPDWORD pcbWritten);
  BOOL  (WINAPI *pfnReadPort)(
      HANDLE hPort, 
      LPBYTE pBuffer, 
      DWORD cbBuffer, 
      LPDWORD pcbRead);
  BOOL  (WINAPI *pfnEndDocPort)(HANDLE hPort);
  BOOL  (WINAPI *pfnClosePort)(HANDLE hPort);
  BOOL  (WINAPI *pfnAddPort)(
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pMonitorName);
  BOOL  (WINAPI *pfnAddPortEx)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE lpBuffer, 
      LPWSTR pMonitorName);
  BOOL  (WINAPI *pfnConfigurePort)(
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pPortName);
  BOOL  (WINAPI *pfnDeletePort)(
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pPortName);
  BOOL  (WINAPI *pfnGetPrinterDataFromPort)(
      HANDLE hPort, 
      DWORD ControlID, 
      LPWSTR pValueName, 
      LPWSTR lpInBuffer, 
      DWORD cbInBuffer, 
      LPWSTR lpOutBuffer, 
      DWORD cbOutBuffer, 
      LPDWORD lpcbReturned);
  BOOL  (WINAPI *pfnSetPortTimeOuts)(
      HANDLE hPort, 
      LPCOMMTIMEOUTS lpCTO, 
      DWORD reserved);
  BOOL  (WINAPI *pfnXcvOpenPort)(
      LPCWSTR pszObject, 
      ACCESS_MASK GrantedAccess, 
      PHANDLE phXcv);
  DWORD (WINAPI *pfnXcvDataPort)(
      HANDLE hXcv, 
      LPCWSTR pszDataName, 
      PBYTE pInputData, 
      DWORD cbInputData, 
      PBYTE pOutputData, 
      DWORD cbOutputData, 
      PDWORD pcbOutputNeeded);
  BOOL  (WINAPI *pfnXcvClosePort)(HANDLE hXcv);
} MONITOR, *LPMONITOR;
```



## Members

<dl> <dt>

**pfnEnumPorts**
</dt> <dd>

A port monitor server DLL's **EnumPorts** function enumerates the ports that the port monitor supports.

</dd> <dt>

**pfnOpenPort**
</dt> <dd>

Pointer to the print monitor's [**OpenPort**](https://www.bing.com/search?q=**OpenPort**) function.

</dd> <dt>

**pfnOpenPortEx**
</dt> <dd>

A language monitor's `OpenPortEx` function opens a printer port.

</dd> <dt>

**pfnStartDocPort**
</dt> <dd>

A print monitor's `StartDocPort` function performs the tasks required to start a print job on the specified port.

</dd> <dt>

**pfnWritePort**
</dt> <dd>

Pointer to the print monitor's [**WritePort**](https://www.bing.com/search?q=**WritePort**) function.

</dd> <dt>

**pfnReadPort**
</dt> <dd>

Pointer to the print monitor's [**ReadPort**](https://www.bing.com/search?q=**ReadPort**) function.

</dd> <dt>

**pfnEndDocPort**
</dt> <dd>

A print monitor's **EndDocPort** function performs the tasks required to end a print job on the specified port.

</dd> <dt>

**pfnClosePort**
</dt> <dd>

Pointer to the print monitor's [**ClosePort**](https://www.bing.com/search?q=**ClosePort**) function.

</dd> <dt>

**pfnAddPort**
</dt> <dd>

The [**AddPort**](https://www.bing.com/search?q=**AddPort**) function is obsolete and is for use only with Windows NT 4.0 and previous versions.

[**AddPort**](https://www.bing.com/search?q=**AddPort**) creates a port and adds it to the list of ports currently supported by the specified monitor in the spooler environment.

</dd> <dt>

**pfnAddPortEx**
</dt> <dd>

(Obsolete. Must be **NULL**.) Pointer to the print monitor's [**AddPortEx**](https://www.bing.com/search?q=**AddPortEx**) function. (Port monitors only.)

</dd> <dt>

**pfnConfigurePort**
</dt> <dd>

The [**ConfigurePort**](https://www.bing.com/search?q=**ConfigurePort**) function is obsolete and is for use only with Windows NT 4.0 and previous versions. For later versions of Windows, use [**ConfigurePortUI**](https://www.bing.com/search?q=**ConfigurePortUI**).

[**ConfigurePort**](https://www.bing.com/search?q=**ConfigurePort**) is a port management function that configures the specified port.

</dd> <dt>

**pfnDeletePort**
</dt> <dd>

The **DeletePort** function is obsolete and is for use only with Windows NT 4.0 and previous versions.

**DeletePort** deletes a port from the monitor's environment.

</dd> <dt>

**pfnGetPrinterDataFromPort**
</dt> <dd>

A port monitor's **GetPrinterDataFromPort** function obtains status information from a bidirectional printer and returns it to the caller.

</dd> <dt>

**pfnSetPortTimeOuts**
</dt> <dd>

A port monitor server DLL's `SetPortTimeOuts` function sets port time-out values for an open port.

</dd> <dt>

**pfnXcvOpenPort**
</dt> <dd>

Pointer to the print monitor's [**XcvOpenPort**](https://www.bing.com/search?q=**XcvOpenPort**) function. (Port monitors only.)

</dd> <dt>

**pfnXcvDataPort**
</dt> <dd>

Pointer to the print monitor's [**XcvDataPort**](https://www.bing.com/search?q=**XcvDataPort**) function. (Port monitors only.)

</dd> <dt>

**pfnXcvClosePort**
</dt> <dd>

Pointer to the print monitor's [**XcvClosePort**](https://www.bing.com/search?q=**XcvClosePort**) function. (Port monitors only.)

</dd> </dl>

## Remarks

The following table describes each member in more detail.



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Callback</td>
<td>Prototype</td>
<td>Parameters</td>
<td>Return values</td>
</tr>
<tr class="even">
<td>AddPort</td>
<td><span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>typedef BOOL ( WINAPI *pfnAddPort)(
  _In_ HANDLE hMonitor,
  _In_ LPWSTR pName,
  _In_ HWND   hWnd,
  _In_ LPWSTR pMonitorName
);</code></pre></td>
</tr>
</tbody>
</table>
</td>
<td><ul>
<li><p><em>hMonitor [in]</em></p>
<p>Caller supplied monitor instance handle. This is the handle returned by the monitor's InitializePrintMonitor2 function. (This parameter does not exist if the print monitor supports InitializePrintMonitor2 instead of InitializePrintMonitor2.)</p></li>
<li><p><em>pName [in]</em></p>
<p>Pointer to a null-terminated string that specifies the name of the server to which the port is connected. If pName is NULL, the port is local.</p></li>
<li><p><em>hWnd [in]</em></p>
<p>Handle to the parent window of the dialog box in which the port name will be entered.</p></li>
<li><p><em>pMonitorName [in]</em></p>
<p>Pointer to a null-terminated string that specifies the monitor associated with the port.</p></li>
</ul></td>
<td>The return value is TRUE if the function is successful, and FALSE otherwise.</td>
</tr>
<tr class="odd">
<td>ConfigurePort</td>
<td><div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>typedef BOOL ( WINAPI *pfnConfigurePort)(
  _In_ HANDLE hMonitor,
  _In_ LPWSTR pName,
  _In_ HWND   hWnd,
  _In_ LPWSTR pPortName
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
<td><ul>
<li><p><em>hMonitor [in]</em></p>
<p>Caller supplied monitor instance handle. This is the handle returned by the monitor's InitializePrintMonitor2 function. (This parameter does not exist if the print monitor supports InitializePrintMonitor instead of InitializePrintMonitor2.)</p></li>
<li><p><em>pName [in]</em></p>
<p>Pointer to a null-terminated string that specifies the name of the server on which the given port exists. If this string is NULL, the port is local.</p></li>
<li><p><em>hWnd [in]</em></p>
<p>Handle to the parent window of the dialog box in which the configuration information will be entered.</p></li>
<li><p><em>pPortName [in]</em></p>
<p>Pointer to a null-terminated string that specifies the name of the port to be configured.</p></li>
</ul></td>
<td>The return value is TRUE if the function is successful.</td>
</tr>
<tr class="even">
<td>DeletePort</td>
<td><div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>pfnDeletePort DeletePort;

BOOL WINAPI DeletePort(
  _In_ HANDLE hMonitor,
  _In_ LPWSTR pName,
  _In_ HWND   hWnd,
  _In_ LPWSTR pPortName
)</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
<td><ul>
<li><p><em>hMonitor [in]</em></p>
<p>Caller supplied monitor instance handle. This is the handle returned by the monitor's InitializePrintMonitor2 function. (This parameter does not exist if the print monitor supports InitializePrintMonitor instead of InitializePrintMonitor2.)</p></li>
<li><p><em>pName [in]</em></p>
<p>Pointer to a null-terminated string that specifies the name of the server on which the port to be deleted exists. If this parameter is NULL, the port is local.</p></li>
<li><p><em>hWnd [in]</em></p>
<p>Handle to the parent window of the port-deletion dialog box.</p></li>
<li><p><em>pPortName [in]</em></p>
<p>Pointer to a null-terminated string that names the port to be deleted.</p></li>
</ul></td>
<td>The return value is TRUE if the function is successful.</td>
</tr>
<tr class="odd">
<td>EndDocPort</td>
<td><div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>typedef BOOL ( WINAPI *pfnEndDocPort)(
  _In_ HANDLE hPort
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
<td><ul>
<li><p><em>hPort [in]</em></p>
<p>Caller-supplied port handle.</p></li>
</ul></td>
<td>If the operation succeeds, the function should return TRUE. Otherwise it should return FALSE.</td>
</tr>
<tr class="even">
<td>EnumPorts</td>
<td><div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>typedef BOOL ( WINAPI *pfnEnumPorts)(
  _In_     HANDLE  hMonitor,
  _In_opt_ LPWSTR  pName,
  _In_     DWORD   Level,
  _Out_    LPBYTE  pPorts,
  _In_     DWORD   cbBuf,
  _Out_    LPDWORD pcbNeeded,
  _Out_    LPDWORD pcReturned
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
<td><ul>
<li><p><em>hMonitor [in]</em></p>
<p>Caller supplied monitor instance handle. This is the handle returned by the monitor's InitializePrintMonitor2 function. (This parameter does not exist if the print monitor supports InitializePrintMonitor instead of InitializePrintMonitor2.)</p></li>
<li><p><em>pName [in, optional]</em></p>
<p>Caller-supplied pointer to a string containing the name of the server whose ports are to be enumerated. A NULL pointer represents the system on which the port monitor server DLL is executing.</p></li>
<li><p><em>Level [in]</em></p>
<p>Caller-supplied value indicating the type of structures to be returned in the buffer pointed to by pPorts. Possible values are 1: PORT_INFO_1 or 2: PORT_INFO_2.</p></li>
<li><p><em>pPorts [out]</em></p>
<p>Caller-supplied pointer to a buffer to receive port information. Returned information must consist of an array of PORT_INFO_1 or PORT_INFO_2 structures, followed by the strings pointed to by structure members. These structures are described in the Microsoft Windows SDK documentation.</p></li>
<li><p><em>cbBuf [in]</em></p>
<p>Caller-supplied size, in bytes, of the buffer pointed to by pPorts.</p></li>
<li><p><em>pcbNeeded [out]</em></p>
<p>Caller-supplied pointer to a location to receive the buffer size, in bytes, required to contain all returned information.</p></li>
<li><p><em>pcReturned [out]</em></p>
<p>Caller-supplied pointer to a location to receive the number enumerated ports.</p></li>
</ul></td>
<td>If the operation succeeds, the function should return TRUE. Otherwise it should return FALSE.</td>
</tr>
<tr class="odd">
<td>GetPrinterDataFromPort</td>
<td><div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>pfnGetPrinterDataFromPort GetPrinterDataFromPort;

BOOL WINAPI GetPrinterDataFromPort(
  _In_  HANDLE  hPort,
  _In_  DWORD   ControlID,
  _In_  LPWSTR  pValueName,
  _In_  LPWSTR  lpInBuffer,
  _In_  DWORD   cbInBuffer,
  _Out_ LPWSTR  lpOutBuffer,
  _In_  DWORD   cbOutBuffer,
  _Out_ LPDWORD lpcbReturned
)</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
<td><ul>
<li><p><em>hPort [in]</em></p>
<p>Caller-supplied port handle.</p></li>
<li><p><em>ControlID [in]</em></p>
<p>Caller-supplied device I/O control code. A value of zero indicates a value name is supplied by pValueName.</p></li>
<li><p><em>pValueName [in]</em></p>
<p>Caller-supplied pointer to a string identifying the information being requested. Valid only if ControlID is zero.</p></li>
<li><p><em>lpInBuffer [in]</em></p>
<p>Caller-supplied pointer to a buffer containing input data. Used only if ControlID is nonzero.</p></li>
<li><p><em>cbInBuffer [in]</em></p>
<p>Caller-supplied size, in bytes, of the buffer pointed to by lpInBuffer.</p></li>
<li><p><em>lpOutBuffer [out]</em></p>
<p>Caller-supplied pointer to a buffer to receive the requested data.</p></li>
<li><p><em>cbOutBuffer [in]</em></p>
<p>Caller-supplied size, in bytes, of the buffer pointed to by lpOutBuffer.</p></li>
<li><p><em>lpcbReturned [out]</em></p>
<p>Caller-supplied pointer to a location to receive the number of bytes written into the buffer pointed to by lpOutBuffer.</p></li>
</ul></td>
<td>If the operation succeeds, the function should return TRUE. Otherwise it should return FALSE.</td>
</tr>
<tr class="even">
<td>OpenPortEx</td>
<td><div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>pfnOpenPortEx OpenPortEx;

BOOL WINAPI OpenPortEx(
  _In_  HANDLE           hMonitor,
  _In_  HANDLE           hMonitorPort,
  _In_  LPWSTR           pPortName,
  _In_  LPWSTR           pPrinterName,
  _Out_ PHANDLE          pHandle,
  _In_  struct _MONITOR2 *pMonitor
)</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
<td><ul>
<li><p><em>hMonitor [in]</em></p>
<p>Caller supplied language monitor instance handle. This is the handle returned by the monitor's InitializePrintMonitor2 function. (This parameter does not exist if the print monitor supports InitializePrintMonitor instead of InitializePrintMonitor2.) In a cluster environment, there can be multiple instances of language monitors.</p></li>
<li><p><em>hMonitorPort [in]</em></p>
<p>Caller supplied port monitor instance handle. This is the handle returned by the monitor's InitializePrintMonitor2 function. (This parameter does not exist if the print monitor supports InitializePrintMonitor instead of InitializePrintMonitor2.) A language monitor must use this handle when it calls functions in the port monitor's MONITOR2 structure.</p></li>
<li><p><em>pPortName [in]</em></p>
<p>Caller-supplied pointer to a string containing the name of the port to be opened.</p></li>
<li><p><em>pPrinterName [in]</em></p>
<p>Caller-supplied pointer to a string containing the name of the printer that is connected to the port.</p></li>
<li><p><em>pHandle [out]</em></p>
<p>Caller-supplied pointer to a location to receive a port handle.</p></li>
<li><p><em>pMonitor [in]</em></p>
<p>Caller-supplied pointer to the MONITOR2 structure returned by a port monitor's InitializePrintMonitor2 function.</p></li>
</ul></td>
<td>If the operation succeeds, the function should return TRUE. Otherwise it should return FALSE.</td>
</tr>
<tr class="odd">
<td>SetPortTimeOuts</td>
<td><div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>BOOL (WINAPI *pfnSetPortTimeOuts)
    (
    _In_ HANDLE  hPort,
    _In_ LPCOMMTIMEOUTS lpCTO,
    _In_ DWORD   reserved    // must be set to 0
    );</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
<td><ul>
<li><p><em>hPort [in]</em></p>
<p>Caller-supplied handle to the open port on which to set the time-out values.</p></li>
<li><p><em>lpCTO [in]</em></p>
<p>Caller-supplied pointer to a COMMTIMEOUTS structure (described in the Microsoft Windows SDK documentation).</p></li>
<li><p><em>reserved [in]</em></p>
<p>Reserved for future use. Must be set to zero.</p></li>
</ul></td>
<td>If the operation succeeds, the function should return TRUE. Otherwise it should return FALSE.</td>
</tr>
<tr class="even">
<td>StartDocPort</td>
<td><div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>typedef BOOL ( WINAPI *pfnStartDocPort)(
  _In_ HANDLE hPort,
  _In_ LPWSTR pPrinterName,
  _In_ DWORD  JobId,
  _In_ DWORD  Level,
  _In_ LPBYTE pDocInfo
);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
<td><ul>
<li><p><em>hPort [in]</em></p>
<p>Caller-supplied port handle.</p></li>
<li><p><em>pPrinterName [in]</em></p>
<p>Caller-supplied pointer to a string containing the printer name.</p></li>
<li><p><em>JobId [in]</em></p>
<p>Caller-supplied, spooler-assigned job identifier.</p></li>
<li><p><em>Level [in]</em></p>
<p>Caller-supplied value indicating the type of structure pointed to by pDocInfo. Possible values are 1: DOC_INFO_1 or 2: DOC_INFO_2.</p></li>
<li><p><em>pDocInfo [in]</em></p>
<p>Caller-supplied pointer to a DOC_INFO_1 or DOC_INFO_2 structure. These structures are described in the Microsoft Windows SDK documentation.</p></li>
</ul></td>
<td>If the operation succeeds, the function should return TRUE. Otherwise it should return FALSE</td>
</tr>
</tbody>
</table>



 

The spooler calls [**AddPort**](https://www.bing.com/search?q=**AddPort**) when it receives an application request to add a port to its environment. The spooler forwards the call to the named port monitor on the named server.

[**AddPort**](https://www.bing.com/search?q=**AddPort**) allows a port to be added interactively. A monitor should prompt a user to enter the port name in a dialog box on the window associated with *hWnd*. **AddPort** should validate the entered port name by calling the Win32 EnumPorts function to ensure that no duplicate port names are added to the spooler environment. A monitor should also verify that the port is one that it supports.

The spooler does not support remote [**AddPort**](https://www.bing.com/search?q=**AddPort**) calls. Consequently, **AddPort** implementations can ignore the *pName* and *pMonitorName* parameters.

The spooler calls [**ConfigurePort**](https://www.bing.com/search?q=**ConfigurePort**) so a port monitor can perform port configuration. **ConfigurePort** can offer a dialog box to obtain some or all of the necessary port configuration information from the user.

The spooler does not support remote [**ConfigurePort**](https://www.bing.com/search?q=**ConfigurePort**) calls; consequently, monitors can ignore the *pName* parameter.

The spooler calls **DeletePort** so a port monitor can delete a port from the monitor's environment. The monitor should delete the specified port from its state. The spooler will not call **DeletePort** on a monitor as long as a port is open.

Applications can delete local and remote ports. The printer UI displays a confirmation message box before the spooler calls **DeletePort**, so a monitor should ignore the *hWnd* parameter and not display another dialog box.

[Language monitors](https://www.bing.com/search?q=Language monitors) and port monitor server DLLs are required to define an **EndDocPort** function and include the function's address in a [**MONITOR2**](monitor2.md) structure.

The handle received as the function's hPort argument is the port handle that the monitor's [**OpenPort**](https://www.bing.com/search?q=**OpenPort**) or [**OpenPortEx**](https://www.bing.com/search?q=**OpenPortEx**) function supplied.

A language monitor's **EndDocPort** function typically calls the associated port monitor's **EndDocPort** function. It should also notify the spooler when the printing device has finished the job by calling **SetJob** (described in the Microsoft Windows SDK documentation), specifying a command of JOB\_CONTROL\_LAST\_PAGE\_EJECTED. Language monitors for bidirectional printers should not call **SetJob** until the printer has sent notification that the job is really finished.

A port monitor server DLL's **EndDocPort** function typically calls the **CloseHandle** function, described in the Windows SDK documentation, to close the handle that was previously obtained by calling [**CreateFile**](https://msdn.microsoft.com/windows/desktop/80a96083-4de9-4422-9705-b8ad2b6cbd1b) from within [**StartDocPort**](https://www.bing.com/search?q=**StartDocPort**). It should also notify the spooler when the printing device has finished the job, by calling **SetJob**, specifying a command of JOB\_CONTROL\_SENT\_TO\_PRINTER. (If a spooler is communicating with the port through a language monitor, it doesn't consider the job complete until the language monitor sends JOB\_CONTROL\_LAST\_PAGE\_EJECTED.)

The **EndDocPort** function should free all resources that were allocated by the **StartDocPort** function.

You might want to modify the **EndDocPort** function's behavior if the user has deleted or restarted the print job. The function can call **GetJob**, described in the Windows SDK documentation, and check for a status of JOB\_STATUS\_DELETING or JOB\_STATUS\_RESTART, to see if either of these events has occurred.

Port monitor server DLLs are required to define an **EnumPorts** function and include the function's address in a [**MONITOR2**](monitor2.md) structure. Language monitors do not export this function.

The purpose of the **EnumPorts** function is to enumerate the ports currently supported by a print monitor. These ports are ones that were previously specified to the monitor's [**AddPortUI**](addportui.md) or [**AddPortEx**](https://www.bing.com/search?q=**AddPortEx**) function.

The **EnumPorts** function should fill the buffer pointed to by *pPort* with an array of PORT\_INFO\_1 or PORT\_INFO\_2 structures. Then starting in a memory location following the last array element, the function must load all the strings pointed to by the array's structure members. Refer to localmon.dll, a [sample port monitor](https://www.bing.com/search?q=sample port monitor), for an example of how to do this. The function must also return the number of structures supplied (that is, the number of supported ports) by placing the number in the location pointed to by *pcReturned*.

The caller specifies the size of the supplied buffer in *cbBuf*. If the buffer is too small, the function should place the required buffer size in the location pointed to by *pcbNeeded*, call **SetLastError** (described in the Microsoft Windows SDK documentation) specifying ERROR\_INSUFFICIENT\_BUFFER, and return **FALSE**.

If *Level* contains an invalid level number, the function should call **SetLastError** specifying ERROR\_INVALID\_LEVEL, and return **FALSE**. Some port monitors only support a level value of 1.

The port monitor must support localization of strings pointed to by the **pMonitorName** and **pDescription** members of the PORT\_INFO\_2 structure. These strings should be defined in resource files and obtained by calling **LoadString** (described in the Windows SDK documentation).

The **fPortType** member of the PORT\_INFO\_2 structure is not used with NT-based operating systems.

[Language monitors](https://www.bing.com/search?q=Language monitors) and port monitor server DLLs can optionally define a **GetPrinterDataFromPort** function and include the function's address in a [**MONITOR2**](monitor2.md) structure.

The function is meant for use with bidirectional printers, and can be used in the following two ways:

-   As a means for requesting a language monitor to poll the printer port, to obtain the current value of printer-specific information that is stored in the registry.

-   As a means for requesting a port monitor to send an I/O control code to the port driver.

If a language monitor's **GetPrinterDataFromPort** function receives a string pointer in *pValueName*, it should return a value in the supplied output buffer. Typically, the string represents a registry value name, and the spooler calls **GetPrinterDataFromPort** when an application calls the **GetPrinterData** function (described in the Microsoft Windows SDK documentation).

The language monitor's responsibility is to send a command to the printer hardware by calling the port monitor's [**WritePort**](https://www.bing.com/search?q=**WritePort**) function, and reading the response by calling [**ReadPort**](https://www.bing.com/search?q=**ReadPort**), to obtain the needed value. For example, pjlmon.dll, the [sample language monitor](https://www.bing.com/search?q=sample language monitor), can return values for a port's "Installed Memory" and "Available Memory" registry value names.

After the spooler calls **GetPrinterDataFromPort** to obtain a registry value, it updates the registry with the new value.

Typically, port monitors do not support calls to **GetPrinterDataFromPort** that include a string pointer in *pValueName*.

If a language monitor's **GetPrinterDataFromPort** function receives a nonzero I/O control code in *ControlID*, it should just call the associated port monitor's **GetPrinterDataFromPort** function and return the result. The *Kernel-Mode Drivers Reference* lists I/O control codes for parallel and serial ports.

When a port monitor's **GetPrinterDataFromPort** function receives a nonzero I/O control code in *ControlID*, it should call **DeviceIOControl** (described in the Windows SDK documentation) to pass the control code to the kernel-mode port driver. The *lpInBuffer*, *cbInBuffer*, *lpOutBuffer*, *cbOutBuffer*, and *lpcbReturned* parameter values should also be passed to **DeviceIOControl**.

Language monitors are required to define an `OpenPortEx` function and include its address in a [**MONITOR2**](monitor2.md) structure. The `OpenPortEx` function is called by the print spooler when a print queue is being connected to a port.

The `OpenPortEx` function's primary purpose is to return a port handle that the caller can use as an input argument for subsequent calls to the language monitor's [**StartDocPort**](https://www.bing.com/search?q=**StartDocPort**), [**WritePort**](https://www.bing.com/search?q=**WritePort**), [**ReadPort**](https://www.bing.com/search?q=**ReadPort**), [**EndDocPort**](https://www.bing.com/search?q=**EndDocPort**), and [**GetPrinterDataFromPort**](https://www.bing.com/search?q=**GetPrinterDataFromPort**) functions. Because a language monitor typically implements these functions by calling the equivalent functions in its associated port monitor, a language monitor typically obtains a port handle by calling the port monitor's [**OpenPort**](https://www.bing.com/search?q=**OpenPort**) function. For more information see [Language and Port Monitor Interaction](https://www.bing.com/search?q=Language and Port Monitor Interaction).

The `OpenPortEx` function's *pMonitor* parameter is a pointer to the port monitor's [**MONITOR2**](monitor2.md) structure. This structure contains pointers to the port monitor's callable functions. The `OpenPortEx` function should check the structure to verify that all required function pointers are non-**NULL**. If the structure is valid, the function should copy it into local storage. Otherwise `OpenPortEx` should call **SetLastError**, specifying ERROR\_INVALID\_PRINT\_MONITOR, and return **FALSE**.

Print monitor functions that accept a port handle as input do not also accept a monitor handle. Therefore, the `OpenPortEx` function must store the received monitor handle in a location that can be referenced by the port handle. This allows the functions that accept a port handle to reference the monitor handle.

A port monitor server DLL's `SetPortTimeOuts` function allows a language monitor to specify port time-out values for an open port. The function is optional, and must be provided only if the port monitor controls a port that allows the modification of port time-out values. If the function is defined, its address must be included in a [**MONITOR2**](monitor2.md) structure.

The function is called by pjlmon.dll, the [sample language monitor](https://www.bing.com/search?q=sample language monitor), and you can write a customized language monitor that calls it. The print spooler does not call `SetPortTimeOuts`.

The port monitor should initialize the port's time-out values from within its [**OpenPort**](https://www.bing.com/search?q=**OpenPort**) function.

[Language monitors](https://www.bing.com/search?q=Language monitors) and port monitor server DLLs are required to define a `StartDocPort` function and include the function's address in a [**MONITOR2**](monitor2.md) structure.

The handle received as the function's *hPort* argument is the port handle that the monitor's [**OpenPort**](https://www.bing.com/search?q=**OpenPort**) or [**OpenPortEx**](https://www.bing.com/search?q=**OpenPortEx**) function supplied.

A language monitor's `StartDocPort` function typically calls the associated port monitor's `StartDocPort` function.

A port monitor server DLL's `StartDocPort` function typically calls the [**CreateFile**](https://msdn.microsoft.com/windows/desktop/80a96083-4de9-4422-9705-b8ad2b6cbd1b) function, described in the Windows SDK documentation, to create a connection to the kernel-mode port driver.

If necessary, the port monitor should prevent other processes from using the specified port until [**EndDocPort**](https://www.bing.com/search?q=**EndDocPort**) is called. For example, a port monitor for a COM port must ensure that, while a spooler is sending printer data to the port, another application does not assume the port is connected to a particular communications device and then attempt to communicate with that device. This cautionary note does not apply to the local print provider, which guarantees that it never calls `StartDocPort` twice in succession without an intervening call to **EndDocPort**, but it does apply to print providers that do not make this guarantee.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**MONITORUI**](monitorui.md)
</dt> <dt>

[**MONITOR2**](monitor2.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20MONITOR%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





