---
Description: 'Starts the calculation for the Excel workbook by using the partition, calculate, and merge model that Microsoft HPC Pack 2008 R2 Services for Excel 2010 uses to run calculations.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7A234F65-FD9A-4F3C-99E2-CF139A640FA7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExcelClient::Run method'
---

# IExcelClient::Run method

Starts the calculation for the Excel workbook by using the partition, calculate, and merge model that Microsoft HPC Pack 2008 R2 Services for Excel 2010 uses to run calculations. The calculation runs on the HPC cluster with the head node that you specified when you called the [**IExcelClient::OpenSession**](iexcelclient-opensession.md) method, unless you specify that the calculation should run on the local computer.

## Syntax


```C++
HRESULT Run(
  [in] VARIANT_BOOL executeLocally,
  [in] Boolean      executeLocally
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
<td><pre><code>Function Run( _
  ByVal executeLocally As VARIANT_BOOL, _
  ByVal executeLocally As Boolean _
) As HRESULT</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>*executeLocally* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | Indicates whether to run the Excel workbook calculation on the local computer.<br/> VARIANT\_TRUE indicates that the calculation should run on the local computer. VARIANT\_FALSE indicates that the calculation should run on the HPC cluster with the head node that you specified when you called the [**IExcelClient::OpenSession**](iexcelclient-opensession.md) method, and the calculation should run by using the partition, calculate, and merge model that Microsoft HPC Pack 2008 R2 Services for Excel 2010 uses to run calculations on an HPC cluster.<br/> |
| **VB**  | Indicates whether to run the Excel workbook calculation on the local computer.<br/> **True** indicates that the calculation should run on the local computer. **False** indicates that the calculation should run on the HPC cluster with the head node that you specified when you called the [**IExcelClient::OpenSession**](iexcelclient-opensession.md) method, and the calculation should run by using the partition, calculate, and merge model that Microsoft HPC Pack 2008 R2 Services for Excel 2010 uses to run calculations on an HPC cluster.<br/>           |

 </dd> </dl>

## Return value

### C++

Returns **S\_OK** unless an exception occurs.

## Remarks

You should call the [**IExcelClient::OpenSession**](iexcelclient-opensession.md) method before you call the **IExcelClient::Run** method if you want to run the calculations in the workbook on an HPC cluster. You must call the [**IExcelClient::Initialize**](iexcelclient-initialize.md) method before call the **IExcelClient::Run** method regardless of where you run the calculations in the workbook.

## Requirements



|                         |                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                       |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Excel.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IExcelClient**](iexcelclient.md)
</dt> <dt>

[**IExcelClient::OpenSession**](iexcelclient-opensession.md)
</dt> <dt>

[**IExcelClient::Initialize**](iexcelclient-initialize.md)
</dt> </dl>

 

 




