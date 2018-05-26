---
Description: A Point and Print DLLs SpoolerCopyFileEvent function receives notifications of events associated with copying print queue-associated files to a print client, when the client connects to a print server.
ms.assetid: 39e9b596-7726-439c-8ad9-a987fdfd3860
title: SpoolerCopyFileEvent function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SpoolerCopyFileEvent function

A Point and Print DLL's `SpoolerCopyFileEvent` function receives notifications of events associated with copying print queue-associated files to a print client, when the client connects to a print server.

## Syntax


```C++
BOOL SpoolerCopyFileEvent(
  _In_ LPWSTR pszPrinterName,
  _In_ LPWSTR pszKey,
  _In_ DWORD  dwCopyFileEvent
);
```



## Parameters

<dl> <dt>

*pszPrinterName* \[in\]
</dt> <dd>

Caller-supplied pointer to a string representing the printer name.

</dd> <dt>

*pszKey* \[in\]
</dt> <dd>

Caller-supplied pointer to a string representing a subkey under the printer's **CopyFiles** registry key. This subkey identifies the component to which the Point and Print DLL belongs.

</dd> <dt>

*dwCopyFileEvent* \[in\]
</dt> <dd>

Caller-supplied flag that identifies the event being reported. Valid flag values are contained in the following table.



| Flag                                                    | When Received                                                                                                                           | Where Received                                                                                                     |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| COPYFILE\_EVENT\_ADD\_PRINTER\_CONNECTION<br/>    | After a client application has called **AddPrinterConnection**.<br/>                                                              | Client copy of `SpoolerCopyFileEvent`. The calling context is the client application.<br/>                   |
| COPYFILE\_EVENT\_DELETE\_PRINTER<br/>             | After a call to **DeletePrinter** has been made.<br/>                                                                             | Client copy of `SpoolerCopyFileEvent`. The calling context is the client's spooler.<br/>                     |
| COPYFILE\_EVENT\_DELETE\_PRINTER\_CONNECTION<br/> | After a client application has called **DeletePrinterConnection**.<br/>                                                           | Client copy of `SpoolerCopyFileEvent`. The calling context is the client application.<br/>                   |
| COPYFILE\_EVENT\_FILES\_CHANGED<br/>              | After the client has downloaded the files specified under the **pszKey** subkey of the printer's **CopyFiles** registry key.<br/> | Client copy of `SpoolerCopyFileEvent`. The calling context is the client's spooler.<br/>                     |
| COPYFILE\_EVENT\_SET\_PRINTER\_DATAEX<br/>        | After a call to **SetPrinterDataEx** has been processed on the server.<br/>                                                       | Server copy of `SpoolerCopyFileEvent`. The calling context is the client application, by impersonation.<br/> |



 

</dd> </dl>

## Return value

If the function encounters errors, the function should return **FALSE**. Otherwise, it should return **TRUE**.

## Remarks

All [Point and Print DLLs](print.point_and_print_dlls) must export a `SpoolerCopyFileEvent` function, which is called by the print spooler. Its purpose is to allow a Point and Print DLL to be notified of events related to the downloading of print queue-associated files, from a print server to a client system, when an application on the client connects to the server. For a complete description of the steps involved in creating a Point and Print connection, see [Supporting Point and Print](print.supporting_point_and_print).

A Point and Print DLL executes on both the server and the client. The `SpoolerCopyFileEvent` function can determine where it is executing by reading the contents of *dwCopyFileEvent*, which supplies a flag indicating the event. The function should process the event and return. If no processing is necessary, the function should just return **TRUE**.

If *dwCopyFileEvent* is COPYFILE\_EVENT\_ADD\_PRINTER\_CONNECTION or COPYFILE\_EVENT\_ADD\_PRINTER\_CONNECTION, the string supplied by *pszPrinterName* includes the server name.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl>                                |
| Library<br/>         | <dl> <dt>Mscms.lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Mscms.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**GenerateCopyFilePaths**](generatecopyfilepaths.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SpoolerCopyFileEvent%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





