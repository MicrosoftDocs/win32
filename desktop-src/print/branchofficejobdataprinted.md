---
Description: Contains the necessary data for logging a branch office job completed event on a remote server. This is based on standard job-related data available to the spooler.
ms.assetid: 77737A33-9592-43A3-B12A-5BFDCA0209BE
title: BranchOfficeJobDataPrinted structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BranchOfficeJobDataPrinted structure

Contains the necessary data for logging a branch office job completed event on a remote server. This is based on standard job-related data available to the spooler.

## Syntax


```C++
typedef struct {
  DWORD    Status;
  LPWSTR   pDocumentName;
  LPWSTR   pUserName;
  LPWSTR   pMachineName;
  LPWSTR   pPrinterName;
  LPWSTR   pPortName;
  LONGLONG Size;
  DWORD    TotalPages;
} BranchOfficeJobDataPrinted, *PBranchOfficeJobDataPrinted;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

Specifies the current status, or the failure code for a JOB\_ERROR event.

</dd> <dt>

**pDocumentName**
</dt> <dd>

Specifies the name of the printed document.

</dd> <dt>

**pUserName**
</dt> <dd>

Specifies the user who submitted the job.

</dd> <dt>

**pMachineName**
</dt> <dd>

Specifies the name of the client machine printing the job

</dd> <dt>

**pPrinterName**
</dt> <dd>

Specifies the name of the print connection.

</dd> <dt>

**pPortName**
</dt> <dd>

Specifies the name of the port the job printed on.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the 64-bit size of the job.

</dd> <dt>

**TotalPages**
</dt> <dd>

Specifies the total number of pages in the job.

</dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BranchOfficeJobDataPrinted%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




