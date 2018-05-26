---
Description: Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated.
ms.assetid: 54a5009d-9893-4766-b9fd-7e7474b55949
title: PRINTPROVIDOR structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PRINTPROVIDOR structure

> \[!Warning\]
>
> Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

The PRINTPROVIDOR structure is used as a parameter to a print provider's [**InitializePrintProvidor**](initializeprintprovidor.md) function. All structure member values are supplied by the provider.

## Syntax


```C++
typedef struct _PRINTPROVIDOR {
  BOOL   (*fpOpenPrinter)(
      PWSTR pPrinterName, 
      PHANDLE phPrinter, 
      PPRINTER_DEFAULTS pDefault);
  BOOL   (*fpSetJob)(
      HANDLE hPrinter, 
      DWORD JobId, 
      DWORD Level, 
      LPBYTE pJob, 
      DWORD Command);
  BOOL   (*fpGetJob)(
      HANDLE hPrinter, 
      DWORD JobId, 
      DWORD Level, 
      LPBYTE pJob, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpEnumJobs)(
      HANDLE hPrinter, 
      DWORD FirstJob, 
      DWORD NoJobs, 
      DWORD Level, 
      LPBYTE pJob, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  HANDLE (*fpAddPrinter)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pPrinter);
  BOOL   (*fpDeletePrinter)(HANDLE hPrinter);
  BOOL   (*fpSetPrinter)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pPrinter, 
      DWORD Command);
  BOOL   (*fpGetPrinter)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pPrinter, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpEnumPrinters)(
      DWORD Flags, 
      LPWSTR Name, 
      DWORD Level, 
      LPBYTE pPrinterEnum, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpAddPrinterDriver)(
      LPWSTR Name, 
      DWORD Level, 
      LPBYTE pDriverInfo);
  BOOL   (*fpEnumPrinterDrivers)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pDriverInfo, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpGetPrinterDriver)(
      HANDLE hPrinter, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pDriverInfo, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpGetPrinterDriverDirectory)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pDriverDirectory, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpDeletePrinterDriver)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      LPWSTR pDriverName);
  BOOL   (*fpAddPrintProcessor)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      LPWSTR pPathName, 
      LPWSTR pPrintProcessorName);
  BOOL   (*fpEnumPrintProcessors)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pPrintProcessorInfo, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpGetPrintProcessorDirectory)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pPrintProcessorInfo, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpDeletePrintProcessor)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      LPWSTR pPrintProcessorName);
  BOOL   (*fpEnumPrintProcessorDatatypes)(
      LPWSTR pName, 
      LPWSTR pPrintProcessorName, 
      DWORD Level, 
      LPBYTE pDataypes, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  DWORD  (*fpStartDocPrinter)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pDocInfo);
  BOOL   (*fpStartPagePrinter)(HANDLE hPrinter);
  BOOL   (*fpWritePrinter)(
      HANDLE hPrinter, 
      LPVOID pBuf, 
      DWORD cbBuf, 
      LPDWORD pcWritten);
  BOOL   (*fpEndPagePrinter)(HANDLE hPrinter);
  BOOL   (*fpAbortPrinter)(HANDLE hPrinter);
  BOOL   (*fpReadPrinter)(
      HANDLE hPrinter, 
      LPVOID pBuf, 
      DWORD cbBuf, 
      LPDWORD pNoBytesRead);
  BOOL   (*fpEndDocPrinter)(HANDLE hPrinter);
  BOOL   (*fpAddJob)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pData, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpScheduleJob)(
      HANDLE hPrinter, 
      DWORD JobId);
  DWORD  (*fpGetPrinterData)(
      HANDLE hPrinter, 
      LPWSTR pValueName, 
      LPDWORD pType, 
      LPBYTE pData, 
      DWORD nSize, 
      LPDWORD pcbNeeded);
  DWORD  (*fpSetPrinterData)(
      HANDLE hPrinter, 
      LPWSTR pValueName, 
      DWORD Type, 
      LPBYTE pData, 
      DWORD cbData);
  DWORD  (*fpWaitForPrinterChange)(
      HANDLE hPrinter, 
      DWORD Flags);
  BOOL   (*fpClosePrinter)(HANDLE hPrinter);
  BOOL   (*fpAddForm)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pForm);
  BOOL   (*fpDeleteForm)(
      HANDLE hPrinter, 
      LPWSTR pFormName);
  BOOL   (*fpGetForm)(
      HANDLE hPrinter, 
      LPWSTR pFormName, 
      DWORD Level, 
      LPBYTE pForm, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded);
  BOOL   (*fpSetForm)(
      HANDLE hPrinter, 
      LPWSTR pFormName, 
      DWORD Level, 
      LPBYTE pForm);
  BOOL   (*fpEnumForms)(
      HANDLE hPrinter, 
      DWORD Level, 
      LPBYTE pForm, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpEnumMonitors)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pMonitors, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpEnumPorts)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pPorts, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpAddPort)(
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pMonitorName);
  BOOL   (*fpConfigurePort)(
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pPortName);
  BOOL   (*fpDeletePort)(
      LPWSTR pName, 
      HWND hWnd, 
      LPWSTR pPortName);
  HANDLE (*fpCreatePrinterIC)(
      HANDLE hPrinter, 
      LPDEVMODEW pDevMode);
  BOOL   (*fpPlayGdiScriptOnPrinterIC)(
      HANDLE hPrinterIC, 
      LPBYTE pIn, 
      DWORD cIn, 
      LPBYTE pOut, 
      DWORD cOut, 
      DWORD ul);
  BOOL   (*fpDeletePrinterIC)(HANDLE hPrinterIC);
  BOOL   (*fpAddPrinterConnection)(LPWSTR pName);
  BOOL   (*fpDeletePrinterConnection)(LPWSTR pName);
  DWORD  (*fpPrinterMessageBox)(
      HANDLE hPrinter, 
      DWORD Error, 
      HWND hWnd, 
      LPWSTR pText, 
      LPWSTR pCaption, 
      DWORD dwType);
  BOOL   (*fpAddMonitor)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pMonitorInfo);
  BOOL   (*fpDeleteMonitor)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      LPWSTR pMonitorName);
  BOOL   (*fpResetPrinter)(
      HANDLE hPrinter, 
      LPPRINTER_DEFAULTS pDefault);
  BOOL   (*fpGetPrinterDriverEx)(
      HANDLE hPrinter, 
      LPWSTR pEnvironment, 
      DWORD Level, 
      LPBYTE pDriverInfo, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      DWORD dwClientMajorVersion, 
      DWORD dwClientMinorVersion, 
      PDWORD pdwServerMajorVersion, 
      PDWORD pdwServerMinorVersion);
  BOOL   (*fpFindFirstPrinterChangeNotification)(
      HANDLE hPrinter, 
      DWORD fdwFlags, 
      DWORD fdwOptions, 
      HANDLE hNotify, 
      PDWORD pfdwStatus, 
      PVOID pPrinterNotifyOptions, 
      PVOID pPrinterNotifyInit);
  BOOL   (*fpFindClosePrinterChangeNotification)(HANDLE hPrinter);
  BOOL   (*fpAddPortEx)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE lpBuffer, 
      LPWSTR lpMonitorName);
  BOOL   (*fpShutDown)(LPVOID pvReserved);
  BOOL   (*fpRefreshPrinterChangeNotification)(
      HANDLE hPrinter, 
      DWORD Reserved, 
      PVOID pvReserved, 
      PVOID pPrinterNotifyInfo);
  BOOL   (*fpOpenPrinterEx)(
      LPWSTR pPrinterName, 
      LPHANDLE phPrinter, 
      LPPRINTER_DEFAULTS pDefault, 
      LPBYTE pClientInfo, 
      DWORD Level);
  HANDLE (*fpAddPrinterEx)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pPrinter, 
      LPBYTE pClientInfo, 
      DWORD ClientInfoLevel);
  BOOL   (*fpSetPort)(
      LPWSTR pName, 
      LPWSTR pPortName, 
      DWORD Level, 
      LPBYTE pPortInfo);
  DWORD  (*fpEnumPrinterData)(
      HANDLE hPrinter, 
      DWORD dwIndex, 
      LPWSTR pValueName, 
      DWORD cbValueName, 
      LPDWORD pcbValueName, 
      LPDWORD pType, 
      LPBYTE pData, 
      DWORD cbData, 
      LPDWORD pcbData);
  DWORD  (*fpDeletePrinterData)(
      HANDLE hPrinter, 
      LPWSTR pValueName);
  DWORD  (*fpClusterSplOpen)(
      LPCTSTR pszServer, 
      LPCTSTR pszResource, 
      PHANDLE phSpooler, 
      LPCTSTR pszName, 
      LPCTSTR pszAddress);
  DWORD  (*fpClusterSplClose)(HANDLE hSpooler);
  DWORD  (*fpClusterSplIsAlive)(HANDLE hSpooler);
  DWORD  (*fpSetPrinterDataEx)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName, 
      LPCWSTR pValueName, 
      DWORD Type, 
      LPBYTE pData, 
      DWORD cbData);
  DWORD  (*fpGetPrinterDataEx)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName, 
      LPCWSTR pValueName, 
      LPDWORD pType, 
      LPBYTE pData, 
      DWORD nSize, 
      LPDWORD pcbNeeded);
  DWORD  (*fpEnumPrinterDataEx)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName, 
      LPBYTE pEnumValues, 
      DWORD cbEnumValues, 
      LPDWORD pcbEnumValues, 
      LPDWORD pnEnumValues);
  DWORD  (*fpEnumPrinterKey)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName, 
      LPWSTR pSubkey, 
      DWORD cbSubkey, 
      LPDWORD pcbSubkey);
  DWORD  (*fpDeletePrinterDataEx)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName, 
      LPCWSTR pValueName);
  DWORD  (*fpDeletePrinterKey)(
      HANDLE hPrinter, 
      LPCWSTR pKeyName);
  BOOL   (*fpSeekPrinter)(
      HANDLE hPrinter, 
      LARGE_INTEGER liDistanceToMove, 
      PLARGE_INTEGER pliNewPointer, 
      DWORD dwMoveMethod, 
      BOOL bWrite);
  BOOL   (*fpDeletePrinterDriverEx)(
      LPWSTR pName, 
      LPWSTR pEnvironment, 
      LPWSTR pDriverName, 
      DWORD dwDeleteFlag, 
      DWORD dwVersionNum);
  BOOL   (*fpAddPerMachineConnection)(
      LPCWSTR pServer, 
      LPCWSTR pPrinterName, 
      LPCWSTR pPrintServer, 
      LPCWSTR pProvider);
  void   (*fpDeletePerMachineConnection)(
      LPCWSTR pServer, 
      LPCWSTR pPrinterName);
  BOOL   (*fpEnumPerMachineConnections)(
      LPCWSTR pServer, 
      LPBYTE pPrinterEnum, 
      DWORD cbBuf, 
      LPDWORD pcbNeeded, 
      LPDWORD pcReturned);
  BOOL   (*fpXcvData)(
      HANDLE hXcv, 
      LPCWSTR pszDataName, 
      PBYTE pInputData, 
      DWORD cbInputData, 
      PBYTE pOutputData, 
      DWORD cbOutputData, 
      PDWORD pcbOutputNeeded, 
      PDWORD pdwStatus);
  BOOL   (*fpAddPrinterDriverEx)(
      LPWSTR pName, 
      DWORD Level, 
      LPBYTE pDriverInfo, 
      DWORD dwFileCopyFlags);
  BOOL   (*fpSplReadPrinter)(
      HANDLE hPrinter, 
      LPBYTE* pBuf, 
      DWORD cbBuf);
  BOOL   (*fpDriverUnloadComplete)(LPWSTR pDriverFile);
  BOOL   (*fpGetSpoolFileInfo)(
      HANDLE hPrinter, 
      LPWSTR* pSpoolDir, 
      LPHANDLE phFile, 
      HANDLE hSpoolerProcess, 
      HANDLE hAppProcess);
  BOOL   (*fpCommitSpoolData)(
      HANDLE hPrinter, 
      DWORD cbCommit);
  BOOL   (*fpCloseSpoolFileHandle)(HANDLE hPrinter);
  BOOL   (*fpFlushPrinter)(
      HANDLE hPrinter, 
      LPBYTE pBuf, 
      DWORD cbBuf, 
      LPDWORD pcWritten, 
      DWORD cSleep);
  DWORD  (*fpSendRecvBidiData)(
      HANDLE hPrinter, 
      LPCWSTR pAction, 
      PBIDI_REQUEST_CONTAINER pReqData, 
      PBIDI_RESPONSE_CONTAINER* ppResData);
} PRINTPROVIDOR, *LPPRINTPROVIDOR;
```



## Members

<dl> <dt>

**fpOpenPrinter**
</dt> <dd>

(Required.) Pointer to the provider's **OpenPrinter** function, which is described in the Microsoft Windows SDK documentation. However, at the provider level, this function must supply one of the DWORD return values listed in the following table.



| Return value          | Definition                                                                                                                                                                                                     |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ROUTER\_SUCCESS       | The provider supports the specified printer and has opened it.                                                                                                                                                 |
| ROUTER\_STOP\_ROUTING | The provider supports the specified printer, but an error occurred and the printer could not be opened. It is assumed that no other provider can support the printer. The function must call **SetLastError**. |
| ROUTER\_UNKNOWN       | The provider does not support the specified printer. The function must call **SetLastError** and specify ERROR\_INVALID\_NAME.                                                                                 |



 

The router calls each provider until one of them returns ROUTER\_SUCCESS or ROUTER\_STOP\_ROUTING. If the provider returns ROUTER\_SUCCESS, it must also return a unique handle. (For more information, see Introduction to Print Providers.) The router first attempts to call the provider's OpenPrinterEx function. If that function is not supported, the router calls OpenPrinter.

</dd> <dt>

**fpSetJob**
</dt> <dd>

(Required.) Pointer to the provider's **SetJob** function (described in the Windows SDK documentation).

</dd> <dt>

**fpGetJob**
</dt> <dd>

(Required.) Pointer to the provider's **GetJob** function (described in the Windows SDK documentation).

</dd> <dt>

**fpEnumJobs**
</dt> <dd>

(Required.) Pointer to the provider's **EnumJobs** function (described in the Windows SDK documentation).

</dd> <dt>

**fpAddPrinter**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **AddPrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpDeletePrinter**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **DeletePrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpSetPrinter**
</dt> <dd>

(Required.) Pointer to the provider's **SetPrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpGetPrinter**
</dt> <dd>

(Required.) Pointer to the provider's **GetPrinter** function (described in the Windows SDK documentation). If you are [writing a network print provider](print.writing_a_network_print_provider) and **GetPrinter** is returning a PRINTER\_INFO\_2 structure, the function should supply only the cJobs and Status structure members. The [local print provider](print.local_print_provider) supplies the rest of the structure members.

</dd> <dt>

**fpEnumPrinters**
</dt> <dd>

(Required.) Pointer to the provider's **EnumPrinters** function (described in the Windows SDK documentation).

</dd> <dt>

**fpAddPrinterDriver**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **AddPrinterDriver** function (described in the Windows SDK documentation). If the provider does not support the specified driver or server, it should specify ERROR\_INVALID\_NAME to SetLastError before returning **FALSE**.

</dd> <dt>

**fpEnumPrinterDrivers**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **EnumPrinterDrivers** function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR\_INVALID\_NAME to SetLastError before returning **FALSE**.

</dd> <dt>

**fpGetPrinterDriver**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **GetPrinterDriver** function (described in the Windows SDK documentation). The router first attempts to call the provider's **GetPrinterDriverEx** function. If that function is not supported, the router calls **GetPrinterDriver**.

</dd> <dt>

**fpGetPrinterDriverDirectory**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **GetPrinterDriverDirectory** function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR\_INVALID\_NAME to **SetLastError** before returning **FALSE**.

</dd> <dt>

**fpDeletePrinterDriver**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **DeletePrinterDriver** function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR\_INVALID\_NAME to **SetLastError** before returning **FALSE**.

</dd> <dt>

**fpAddPrintProcessor**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **AddPrintProcessor** function (described in the Windows SDK documentation).

</dd> <dt>

**fpEnumPrintProcessors**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **EnumPrintProcessors** function (described in the Windows SDK documentation).

</dd> <dt>

**fpGetPrintProcessorDirectory**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **GetPrintProcessorDirectory** function (described in the Windows SDK documentation).

</dd> <dt>

**fpDeletePrintProcessor**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **DeletePrintProcessor** function (described in the Windows SDK documentation).

</dd> <dt>

**fpEnumPrintProcessorDatatypes**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **EnumPrintProcessorDatatypes** function (described in the Windows SDK documentation).

</dd> <dt>

**fpStartDocPrinter**
</dt> <dd>

(Required.) Pointer to the provider's **StartDocPrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpStartPagePrinter**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **StartPagePrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpWritePrinter**
</dt> <dd>

(Required.) Pointer to the provider's **WritePrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpEndPagePrinter**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **EndPagePrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpAbortPrinter**
</dt> <dd>

(Required.) Pointer to the provider's **AbortPrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpReadPrinter**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **ReadPrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpEndDocPrinter**
</dt> <dd>

(Required.) Pointer to the provider's **EndDocPrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpAddJob**
</dt> <dd>

(Required.) Pointer to the provider's **AddJob** function (described in the Windows SDK documentation).

</dd> <dt>

**fpScheduleJob**
</dt> <dd>

(Required.) Pointer to the provider's **ScheduleJob** function (described in the Windows SDK documentation).

</dd> <dt>

**fpGetPrinterData**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **GetPrinterData** function (described in the Windows SDK documentation).

</dd> <dt>

**fpSetPrinterData**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **SetPrinterData** function (described in the Windows SDK documentation).

</dd> <dt>

**fpWaitForPrinterChange**
</dt> <dd>

Obsolete. Must be **NULL**.

</dd> <dt>

**fpClosePrinter**
</dt> <dd>

(Required.) Pointer to the provider's **ClosePrinter** function (described in the Windows SDK documentation). If a printer change notification object has been created, then the router calls the provider's FindClosePrinterChangeNotification function (described in the Windows SDK documentation) before calling ClosePrinter.

</dd> <dt>

**fpAddForm**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **AddForm** function (described in the Windows SDK documentation).

</dd> <dt>

**fpDeleteForm**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **DeleteForm** function (described in the Windows SDK documentation).

</dd> <dt>

**fpGetForm**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **GetForm** function (described in the Windows SDK documentation).

</dd> <dt>

**fpSetForm**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **SetForm** function (described in the Windows SDK documentation).

</dd> <dt>

**fpEnumForms**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **EnumForms** function (described in the Windows SDK documentation).

</dd> <dt>

**fpEnumMonitors**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **EnumMonitors** function, which is described in the Windows SDK documentation. However, at the provider level this function must supply one of the DWORD return values listed in the following table.



| Return value          | Definition                                                                                                        |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| ROUTER\_SUCCESS       | The provider has enumerated the monitors on the specified server.                                                 |
| ROUTER\_STOP\_ROUTING | The provider has enumerated the monitors on the specified server, and the router should not call other providers. |
| ROUTER\_UNKNOWN       | The provider does not support the specified server.                                                               |



 

</dd> <dt>**fpEnumPorts**</dt> <dd> 

| Return value          | Definition                                                                                                     |
|-----------------------|----------------------------------------------------------------------------------------------------------------|
| ROUTER\_SUCCESS       | The provider has enumerated the ports on the specified server.                                                 |
| ROUTER\_STOP\_ROUTING | The provider has enumerated the ports on the specified server, and the router should not call other providers. |
| ROUTER\_UNKNOWN       | The provider does not support the specified server.                                                            |



 

</dd> <dt>

**fpAddPort**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **AddPort** function (described in the Windows SDK documentation). If the provider does not support the specified port, it must supply ERROR\_NOT\_SUPPORTED to SetLastError before returning **FALSE**.

</dd> <dt>

**fpConfigurePort**
</dt> <dd>

(Required.) Pointer to the provider's **ConfigurePort** function (described in the Windows SDK documentation). If the function supplies ERROR\_NOT\_SUPPORTED, ERROR\_INVALID\_NAME, or ERROR\_UNKNOWN\_PORT to SetLastError, the router will attempt to call another provider.

</dd> <dt>

**fpDeletePort**
</dt> <dd>

(Required.) Pointer to the provider's **DeletePort** function (described in the Windows SDK documentation). If the provider does not support the specified port, it must supply ERROR\_NOT\_SUPPORTED to SetLastError before returning **FALSE**.

</dd> <dt>

**fpCreatePrinterIC**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpPlayGdiScriptOnPrinterIC**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpDeletePrinterIC**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpAddPrinterConnection**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **AddPrinterConnection** function (described in the Windows SDK documentation).

</dd> <dt>

**fpDeletePrinterConnection**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **DeletePrinterConnection** function (described in the Windows SDK documentation).

</dd> <dt>

**fpPrinterMessageBox**
</dt> <dd>

Not used. Must be **NULL**.

</dd> <dt>

**fpAddMonitor**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **AddMonitor** function (described in the Windows SDK documentation). If the provider does not support the specified monitor, it must supply ERROR\_INVALID\_NAME to SetLastError before returning **FALSE**.

</dd> <dt>

**fpDeleteMonitor**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **DeleteMonitor** function (described in the Windows SDK documentation). If the provider does not support the specified monitor, it must supply ERROR\_INVALID\_NAME to SetLastError before returning **FALSE**.

</dd> <dt>

**fpResetPrinter**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **ResetPrinter** function (described in the Windows SDK documentation).

</dd> <dt>

**fpGetPrinterDriverEx**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **GetPrinterDriverEx** function (described in the Windows SDK documentation). If GetPrinterDriverEx is not supported, the router attempts to call GetPrinterDriver.

</dd> <dt>

**fpFindFirstPrinterChangeNotification**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **FindFirstPrinterChangeNotification** function (described in the Windows SDK documentation).

</dd> <dt>

**fpFindClosePrinterChangeNotification**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **FindClosePrinterChangeNotification** function (described in the Windows SDK documentation).

</dd> <dt>

**fpAddPortEx**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **AddPortEx** function (described in the Windows SDK documentation). If the provider does not support the specified port, it must supply ERROR\_NOT\_SUPPORTED to SetLastError before returning **FALSE**.

</dd> <dt>

**fpShutDown**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpRefreshPrinterChangeNotification**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **RefreshPrinterChangeNotification** function.

</dd> <dt>

**fpOpenPrinterEx**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpAddPrinterEx**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpSetPort**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **SetPort** function (described in the Windows SDK documentation). If the function supplies ERROR\_NOT\_SUPPORTED, ERROR\_INVALID\_NAME, or ERROR\_UNKNOWN\_PORT to **SetLastError**, the router will attempt to call another provider.

</dd> <dt>

**fpEnumPrinterData**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **EnumPrinterData** function (described in the Windows SDK documentation).

</dd> <dt>

**fpDeletePrinterData**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **DeletePrinterData** function (described in the Windows SDK documentation).

</dd> <dt>

**fpClusterSplOpen**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpClusterSplClose**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpClusterSplIsAlive**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpSetPrinterDataEx**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **SetPrinterDataEx** function (described in the Windows SDK documentation).

</dd> <dt>

**fpGetPrinterDataEx**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **GetPrinterDataEx** function (described in the Windows SDK documentation).

</dd> <dt>

**fpEnumPrinterDataEx**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **EnumPrinterDataEx** function (described in the Windows SDK documentation).

</dd> <dt>

**fpEnumPrinterKey**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **EnumPrinterKey** function (described in the Windows SDK documentation).

</dd> <dt>

**fpDeletePrinterDataEx**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **DeletePrinterDataEx** function (described in the Windows SDK documentation).

</dd> <dt>

**fpDeletePrinterKey**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **DeletePrinterKey** function (described in the Windows SDK documentation).

</dd> <dt>

**fpSeekPrinter**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpDeletePrinterDriverEx**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's DeletePrinterDriverEx function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR\_INVALID\_NAME to **SetLastError** before returning **FALSE**.

</dd> <dt>

**fpAddPerMachineConnection**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpDeletePerMachineConnection**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpEnumPerMachineConnections**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpXcvData**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **XcvData** function.

</dd> <dt>

**fpAddPrinterDriverEx**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **AddPrinterDriverEx** function (described in the Windows SDK documentation). If the provider does not support the specified server, it should specify ERROR\_INVALID\_NAME to SetLastError before returning **FALSE**.

</dd> <dt>

**fpSplReadPrinter**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpDriverUnloadComplete**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpGetSpoolFileInfo**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpCommitSpoolData**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpCloseSpoolFileHandle**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpFlushPrinter**
</dt> <dd>

For internal use only. Must be **NULL**.

</dd> <dt>

**fpSendRecvBidiData**
</dt> <dd>

(Optional. Can be **NULL**.) Pointer to the provider's **SendRecvBidiData** function. If this parameter is **NULL**, it means that the provider does not support bidi communication.

</dd> </dl>

## Remarks

Function pointers are listed in the order they are specified within the PRINTPROVIDOR structure. To see function descriptions grouped by related capabilities, see [Functions Defined by Print Providers](print.functions_defined_by_print_providers).

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**InitializePrintProvidor**](initializeprintprovidor.md)
</dt> <dt>

[**FindFirstPrinterChangeNotification**](print.findfirstprinterchangenotification)
</dt> <dt>

[**RefreshPrinterChangeNotification**](print.refreshprinterchangenotification)
</dt> <dt>

[**XcvData**](print.xcvdata)
</dt> <dt>

[**SendRecvBidiData**](print.sendrecvbididata)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PRINTPROVIDOR%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





