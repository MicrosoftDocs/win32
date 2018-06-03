---
Description: The MONITOR2 structure contains pointers to the functions defined by print monitors.
ms.assetid: 73348405-0cc1-412a-b9b1-cfcc300190d7
title: MONITOR2 structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MONITOR2 structure

The MONITOR2 structure contains pointers to the functions defined by print monitors.

## Syntax


```C++
typedef struct _MONITOR2 {
  DWORD cbSize;
  BOOL  (WINAPI *pfnEnumPorts)(
      HANDLE hMonitor, 
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pPorts, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL  (WINAPI *pfnOpenPort)(
      HANDLE hMonitor, 
      LPWSTR pName, 
      PHANDLE pHandle);
  BOOL  (WINAPI *pfnOpenPortEx)(
      HANDLE hMonitor, 
      HANDLE hMonitorPort, 
      LPWSTR pPortName, 
      LPWSTR pPrinterName, 
      PHANDLE pHandle, 
      struct _MONITOR2 * pMonitor2);
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
      HANDLE hMonitor, 
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pMonitorName);
  BOOL  (WINAPI *pfnAddPortEx)(
      HANDLE hMonitor, 
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE lpBuffer, 
      LPWSTR pMonitorName);
  BOOL  (WINAPI *pfnConfigurePort)(
      HANDLE hMonitor, 
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pPortName);
  BOOL  (WINAPI *pfnDeletePort)(
      HANDLE hMonitor, 
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
      HANDLE hMonitor, 
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
  VOID  (WINAPI *pfnShutdown)(HANDLE hMonitor);
  DWORD (WINAPI *pfnSendRecvBidiDataFromPort)(
      HANDLE hPort, 
      DWORD dwAccessBit, 
      LPCWSTR pAction, 
      PBIDI_REQUEST_CONTAINER pReqData, 
      PBIDI_RESPONSE_CONTAINER* ppResData);
} MONITOR2, *PMONITOR2, *LPMONITOR2;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Specifies the size, in bytes, of the MONITOR2 structure.

</dd> <dt>

**pfnEnumPorts**
</dt> <dd>

A port monitor server DLL's **EnumPorts** function enumerates the ports that the port monitor supports.

</dd> <dt>

**pfnOpenPort**
</dt> <dd>

Pointer to the print monitor's **OpenPort** function.

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

Pointer to the print monitor's **WritePort** function.

</dd> <dt>

**pfnReadPort**
</dt> <dd>

Pointer to the print monitor's **ReadPort** function.

</dd> <dt>

**pfnEndDocPort**
</dt> <dd>

A print monitor's **EndDocPort** function performs the tasks required to end a print job on the specified port.

</dd> <dt>

**pfnClosePort**
</dt> <dd>

Pointer to the print monitor's **ClosePort** function.

</dd> <dt>

**pfnAddPort**
</dt> <dd>

The [**AddPort**](https://www.bing.com/search?q=**AddPort**) function is obsolete and is for use only with Windows NT 4.0 and previous versions.

[**AddPort**](https://www.bing.com/search?q=**AddPort**) creates a port and adds it to the list of ports currently supported by the specified monitor in the spooler environment.

</dd> <dt>

**pfnAddPortEx**
</dt> <dd>

(Obsolete. Must be **NULL**.) Pointer to the print monitor's **AddPortEx** function. (Port monitors only.)

</dd> <dt>

**pfnConfigurePort**
</dt> <dd>

The **ConfigurePort** function is obsolete and is for use only with Windows NT 4.0 and previous versions. For later versions of Windows, use **ConfigurePortUI**.

**ConfigurePort** is a port management function that configures the specified port.

</dd> <dt>

**pfnDeletePort**
</dt> <dd>

The **DeletePort** function is obsolete and is for use only with Windows NT 4.0 and previous versions.

**DeletePort** deletes a port from the monitor's environment.

</dd> <dt>

**pfnGetPrinterDataFromPort**
</dt> <dd>

Pointer to the print monitor's **GetPrinterDataFromPort** function.

</dd> <dt>

**pfnSetPortTimeOuts**
</dt> <dd>

A port monitor server DLL's `SetPortTimeOuts` function sets port time-out values for an open port.

</dd> <dt>

**pfnXcvOpenPort**
</dt> <dd>

Pointer to the print monitor's **XcvOpenPort** function. (Port monitors only.)

</dd> <dt>

**pfnXcvDataPort**
</dt> <dd>

Pointer to the print monitor's **XcvDataPort** function. (Port monitors only.)

</dd> <dt>

**pfnXcvClosePort**
</dt> <dd>

Pointer to the print monitor's **XcvClosePort** function. (Port monitors only.)

</dd> <dt>

**pfnShutdown**
</dt> <dd>

Pointer to the print monitor's **Shutdown** function.

</dd> <dt>

**pfnSendRecvBidiDataFromPort**
</dt> <dd>

Pointer to the print monitor's **SendRecvBidiDataFromPort** function.

</dd> </dl>

## Remarks

Each language monitor and each port monitor server DLL must provide a MONITOR2 structure. The monitor must supply values for all structure members, and specify the structure's address as the return value for its [**InitializePrintMonitor2**](initializeprintmonitor2.md) function.

If a function is not defined, its pointer must be **NULL**.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**InitializePrintMonitor2**](initializeprintmonitor2.md)
</dt> <dt>

[**MONITORUI**](monitorui.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20MONITOR2%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





