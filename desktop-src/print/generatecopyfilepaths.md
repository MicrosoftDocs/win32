---
Description: A Point and Print DLL's GenerateCopyFilePaths function is used for modifying the source and destination paths used by print spoolers when they copy print queue-associated files to a print client.
ms.assetid: 61274493-1ec4-483b-85fa-f6087cf0631e
title: GenerateCopyFilePaths function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GenerateCopyFilePaths function

A Point and Print DLL's **GenerateCopyFilePaths** function is used for modifying the source and destination paths used by print spoolers when they copy print queue-associated files to a print client.

## Syntax


```C++
DWORD GenerateCopyFilePaths(
  _In_    LPCWSTR pszPrinterName,
  _In_    LPCWSTR pszDirectory,
  _In_    LPBYTE  pSplClientInfo,
  _In_    DWORD   dwLevel,
  _Inout_ LPWSTR  pszSourceDir,
  _Inout_ LPDWORD pcchSourceDirSize,
  _Inout_ LPWSTR  pszTargetDir,
  _Inout_ LPDWORD pcchTargetDirSize,
  _In_    DWORD   dwFlags
);
```



## Parameters

<dl> <dt>

*pszPrinterName* \[in\]
</dt> <dd>

Caller-supplied pointer to a string representing the name of the print queue.

</dd> <dt>

*pszDirectory* \[in\]
</dt> <dd>

Caller-supplied pointer to a string representing the value supplied for the server's **Directory** entry in the registry. For more information, see [Supporting Point and Print During Printer Installations](https://www.bing.com/search?q=Supporting+Point+and+Print+During+Printer+Installations).

</dd> <dt>

*pSplClientInfo* \[in\]
</dt> <dd>

Caller-supplied pointer to an [**SPLCLIENT\_INFO\_1**](splclient-info-1.md) structure.

</dd> <dt>

*dwLevel* \[in\]
</dt> <dd>

Caller-supplied value indicating the level number of the structure pointed to by *pSplClientInfo*. Must be 1.

</dd> <dt>

*pszSourceDir* \[in, out\]
</dt> <dd>

For input, receives a caller-supplied pointer to a string representing the complete server directory path (including server name) from which files are to be copied.

For output, the function can modify this string.

</dd> <dt>

*pcchSourceDirSize* \[in, out\]
</dt> <dd>

Caller-supplied address containing the length of the buffer pointed to by *pszSourceDir*. (Note that this is the buffer length, not the string length.)

</dd> <dt>

*pszTargetDir* \[in, out\]
</dt> <dd>

For input, receives a caller-supplied pointer to a string representing the client directory path to which files are to be copied. The following rules apply:

-   When the function is called on the server, this path is relative to PRINT$.

-   When the function is called on the client, the string contains a complete path.

For output, the function can modify this string.

</dd> <dt>

*pcchTargetDirSize* \[in, out\]
</dt> <dd>

Caller-supplied address containing the length of the buffer pointed to by *pszTargetDir*. (Note that this is the buffer length, not the string length.)

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Caller-supplied flag. Can be one of the following:

<dl> <dt>

<span id="COPYFILE_FLAG_CLIENT_SPOOLER"></span><span id="copyfile_flag_client_spooler"></span>COPYFILE\_FLAG\_CLIENT\_SPOOLER
</dt> <dd>

Indicates the function is being called by the client's spooler.

</dd> <dt>

<span id="COPYFILE_FLAG_SERVER_SPOOLER"></span><span id="copyfile_flag_server_spooler"></span>COPYFILE\_FLAG\_SERVER\_SPOOLER
</dt> <dd>

Indicates the function is being called by the server's spooler.

</dd> </dl> </dd> </dl>

## Return value

If the operation succeeds, the function should return **ERROR\_SUCCESS**. Otherwise, it should return an error code defined in winerror.h.

## Remarks

All [Point and Print DLLs](https://www.bing.com/search?q=Point+and+Print+DLLs) must export a **GenerateCopyFilePaths** function, which is called by the print spooler. Its purpose is to allow a Point and Print DLL to modify the source or destination directory path, or both, before the print spooler copies print queue-associated files from a server to a client. (The files are copied when a client connects to a print server. For a complete description of the steps involved in creating a Point and Print connection, see [Supporting Point and Print](https://www.bing.com/search?q=Supporting+Point+and+Print).)

A Point and Print DLL executes on both the server and the client. The **GenerateCopyFilePaths** function should check the *dwFlags* argument to determine where it is executing.

Typically, this function is used to provide compatibility when different versions of the operating system are executing on the client and server. For example if the function, when executing on the server, determines (by reading the [**SPLCLIENT\_INFO\_1**](splclient-info-1.md) structure) that its operating system is newer than the client's, it can modify the source and destination paths to be compatible with the client's older OS. On the other hand, if the function determines that the client's operating system is newer than the client's, it should probably do nothing on the server and perform modifications, if necessary, when executing on the client.

Arguments for the *pszSourceDir* and *pszTargetDir* parameters point to buffers containing strings that represent the current source and destination directory paths. If modifications to either of these strings is necessary, the function should make modifications in the supplied buffers. The maximum allowable string lengths are pointed to by the *pcchSourceDirSize* and *pcchTargetDirSize* arguments.

If no modifications to the source or destination directories are needed, the function should just return **ERROR\_SUCCESS**.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl>                                |
| Library<br/>         | <dl> <dt>Mscms.lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Mscms.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**SpoolerCopyFileEvent**](spoolercopyfileevent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GenerateCopyFilePaths%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





