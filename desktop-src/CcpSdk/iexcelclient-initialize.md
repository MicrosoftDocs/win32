---
Description: 'Initializes the Excel SOA client by creating a new instance of the ExcelDriver class to interact with the Excel workbook that is represented by the specified Microsoft.Office.Interop.Excel.Workbook object.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'C8FD0FA7-3DEC-4B95-915F-337EABDFE141'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExcelClient::Initialize method'
---

# IExcelClient::Initialize method

Initializes the Excel SOA client by creating a new instance of the [ExcelDriver](https://msdn.microsoft.com/library/microsoft.hpc.excel.exceldriver.aspx) class to interact with the Excel workbook that is represented by the specified [Microsoft.Office.Interop.Excel.Workbook](https://msdn.microsoft.com/library/microsoft.office.interop.excel.workbook.aspx) object.

## Syntax


```C++
HRESULT Initialize(
  [in] IUnknown *excelWorkbook,
  [in] Unknown  excelWorkbook
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Function Initialize( _
  ByVal excelWorkbook As IUnknown, _
  ByVal excelWorkbook As Unknown _
) As HRESULT</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>*excelWorkbook* \[in\]</dt> <dd> 

|         |                                                                                                             |
|---------|-------------------------------------------------------------------------------------------------------------|
| **C++** | The Excel workbook for which the Excel SOA client should submit calculations to the HPC cluster.<br/> |
| **VB**  | The Excel workbook for which the Excel SOA client should submit calculations to the HPC cluster.<br/> |

 </dd> </dl>

## Return value

### C++

Returns **S\_OK** unless an exception occurs.

## Remarks

An exception can occur when you call the **IExcelClient.Initialize** method in PowerShell, because PowerShell does not correctly wrap the [**Workbook**](8c00aa60-c974-eed3-0812-3c9625eb0d4c) object that the [**Workbooks.Open**](1d1c3fca-ae1a-0a91-65a2-6f3f0fb308a0) method returns as an [Microsoft.Office.Interop.Excel.Workbook](https://msdn.microsoft.com/library/microsoft.office.interop.excel.workbook.aspx) type. To ensure that PowerShell provides a **Workbook** object to the **IExcelClient.Initialize** method, use the [Type.GetTypeFromCLSID](https://msdn.microsoft.com/library/system.type.gettypefromclsid.aspx) method to get the [Microsoft.Office.Interop.Excel.WorkbookClass](https://msdn.microsoft.com/library/microsoft.office.interop.excel.workbookclass.aspx) type, and create a wrapper of that type to pass to **IExcelClient.Initialize**.

The following example shows how to correctly create a wrapper for a workbook and pass it to the **IExcelClient.Initialize** method by using PowerShell.


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

[**IExcelClient**](iexcelclient.md)
</dt> </dl>

 

 




