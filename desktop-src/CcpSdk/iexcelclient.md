---
Description: 'Represents an engine that implements the partition, calculate, and merge model that Microsoft HPC Pack 2008 R2 Services for Excel 2010 uses to run calculations in a workbook in parallel on an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'FABA59DA-BEB0-4ABC-8A24-6967CDFFEBD4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IExcelClient interface
---

# IExcelClient interface

Represents an engine that implements the partition, calculate, and merge model that Microsoft HPC Pack 2008 R2 Services for Excel 2010 uses to run calculations in a workbook in parallel on an HPC cluster. The workbook must implement the callback macro framework.

## Members

The **IExcelClient** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IExcelClient** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IExcelClient** interface has these methods.



| Method                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:--------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cancel**](iexcelclient-cancel.md)             | Cancels any currently running Excel calculations without closing the SOA session.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| [**CloseSession**](iexcelclient-closesession.md) | Closes the session that you opened by calling the [**IExcelClient::OpenSession**](iexcelclient-opensession.md) method (subject to the optionally specified time-out period), and closes all instances of Excel that are running on the compute nodes. <br/>                                                                                                                                                                              |
| [**Dispose**](iexcelclient-dispose.md)           | Releases all of the resources that the object allocated.<br/>                                                                                                                                                                                                                                                                                                                                                                             |
| [**Initialize**](iexcelclient-initialize.md)     | Initializes the Excel SOA client by creating a new instance of the ExcelDriver class to interact with the Excel workbook that is represented by the specified Microsoft.Office.Interop.Excel.Workbook object.<br/>                                                                                                                                                                                                                        |
| [**OpenSession**](iexcelclient-opensession.md)   | Starts a new SOA session that uses the specified resource settings to perform calculations from the specified Excel workbook on the HPC cluster with the specified head node.<br/>                                                                                                                                                                                                                                                        |
| [**Run**](iexcelclient-run.md)                   | Starts the calculation for the Excel workbook by using the partition, calculate, and merge model that Microsoft HPC Pack 2008 R2 Services for Excel 2010 uses to run calculations. The calculation runs on the HPC cluster with the head node that you specified when you called the [**IExcelClient::OpenSession**](iexcelclient-opensession.md) method, unless you specify that the calculation should run on the local computer.<br/> |



 

### Properties

The **IExcelClient** interface has these properties.



| Property                                           | Access type          | Description                                  |
|:---------------------------------------------------|:---------------------|:---------------------------------------------|
| [**Version**](iexcelclient-version.md)<br/> | Read-only<br/> | The version of the Excel client. <br/> |



 

## Remarks

When you use this interface in Windows PowerShell, an exception can occur when you call the [**IExcelClient.Initialize**](iexcelclient-initialize.md) method, because Windows PowerShell does not correctly wrap the [**Workbook**](8c00aa60-c974-eed3-0812-3c9625eb0d4c) object that the [**Workbooks.Open**](1d1c3fca-ae1a-0a91-65a2-6f3f0fb308a0) method returns as an [Microsoft.Office.Interop.Excel.Workbook](https://msdn.microsoft.com/library/microsoft.office.interop.excel.workbook.aspx) type. To ensure that Windows PowerShell provides a **Workbook** object to the **IExcelClient.Initialize** method, use the [Type.GetTypeFromCLSID](https://msdn.microsoft.com/library/system.type.gettypefromclsid.aspx) method to get the [Microsoft.Office.Interop.Excel.WorkbookClass](https://msdn.microsoft.com/library/microsoft.office.interop.excel.workbookclass.aspx) type, and then create a wrapper of that type to pass to **IExcelClient.Initialize**.

The following example shows how to correctly create a wrapper for a workbook and pass it to the [**IExcelClient.Initialize**](iexcelclient-initialize.md) method by using PowerShell.


```PowerShell
# Open an Excel instance and open a workbook.
$excel = new-object -comobject Excel.Application
$excel.visible = $true
$workbook = $excel.Workbooks.Open( MyWorkbook.xlsm  )

# Get the workbook type using the class identifier (CLSID) for WorkbookClass.
$workbookType = [Type]::GetTypeFromCLSID("00020819-0000-0000-C000-000000000046")
$wrappedWorkbook = [System.Runtime.Interopservices.Marshal]::CreateWrapperOfType($workbook, $workbookType)

$excelclient = new-object -comobject Microsoft.Hpc.Excel.Com.ExcelClient
$excelclient.Initialize( $wrappedWorkbook )
```



## Requirements



|                         |                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                       |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Excel.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> </dl>

 

 




