---
Description: 'Processes the result of a calculation step and inserts the processed result in the Excel workbook.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'F1B8F445-4FEF-4C93-8B48-BD75419F19AB'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'HPC\_Merge method'
---

# HPC\_Merge method

Processes the result of a calculation step and inserts the processed result in the Excel workbook.

## Syntax


```VB
Function HPC_Merge( _
  ByVal data As any base type or VARIANT[] _
)
```



## Parameters

<dl> <dt>

*data* 
</dt> <dd>

Specifies the result of a single calculation step in the Excel workbook.

The type of this parameter must match the return type for your implementation of the [**HPC\_Execute**](hpc-execute.md) macro.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

You implement this macro for an Excel workbook for which you want to run calculations on an HPC cluster as part of the partition, calculate, and merge macro framework. This macro represents the merge stage of that framework. The framework implements an iterative calculation model for the workbook, where different calculation steps are performed on different nodes in the HPC cluster. The merge stage of the framework processes the result of a calculation step, and then it updates the Excel workbook with that result.

The HPC Services for Excel client library calls this macro multiple times for a workbook calculation, once for each calculation step.

This macro runs on the client computer. The HPC Services for Excel client library calls this macro once for each time the client library calls [**HPC\_Partition**](hpc-partition.md), but the client library does not necessarily call the **HPC\_Merge** macro before the next call to **HPC\_Partition**.

The **HPC\_Merge** macro also does not necessarily receive results for the calculation steps in the same order that the [**HPC\_Partition**](hpc-partition.md) macro sent the data for those steps to the HPC cluster. The return value for the [**HPC\_Execute**](hpc-execute.md) macro should include information about the location in the workbook for which the calculation was performed, so that the **HPC\_Merge** macro can update the appropriate location in the workbook.

To improve performance, you should minimize the work that you perform in the **HPC\_Merge** macro, including the calculation and display tasks. For example, you should close external resources such as log files and database connections in the [**HPC\_Finalize**](hpc-finalize.md) macro rather than in the **HPC\_Merge** macro.

## Examples

For example implementations of the **HPC\_Merge** macro, see the following resources:

-   [Accelerating Excel 2010 with Windows HPC Server 2008 R2: Building VBA applications and workbooks for a Windows HPC Cluster](http://go.microsoft.com/fwlink/p/?linkid=205876) (http://go.microsoft.com/fwlink/p/?linkid=205876)

-   The macros in the VBASample.xlsm workbook that is included in the Excel\\ExcelRunner folder in the sample code package for the [Windows HPC Pack 2008 R2 SDK](http://go.microsoft.com/fwlink/p/?linkid=205875) (http://go.microsoft.com/fwlink/p/?linkid=205875).

## Requirements



|                    |                                              |
|--------------------|----------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 Client Utilities<br/> |



## See also

<dl> <dt>

[**HPC\_Partition**](hpc-partition.md)
</dt> <dt>

[**HPC\_Execute**](hpc-execute.md)
</dt> </dl>

 

 




