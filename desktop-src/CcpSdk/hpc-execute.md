---
Description: 'Performs a single calculation step for an Excel workbook on a compute node in an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'A5D6BAC7-4180-400D-B48C-C75AAC2874D7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'HPC\_Execute method'
---

# HPC\_Execute method

Performs a single calculation step for an Excel workbook on a compute node in an HPC cluster.

## Syntax


```VB
Function HPC_Execute( _
  ByVal data As any base type or Variant[] _
) As any base type or Variant[]
```



## Parameters

<dl> <dt>

*data* 
</dt> <dd>

Specifies the information that is needed to perform a single calculation step in the Excel workbook. This information establishes how the overall calculation is divided into individual calculation steps. For example, if you split up the calculation by rows, then this value could be the number of the row to use for the calculation.

The type of this parameter must match the return type for your implementation of the [**HPC\_Partition**](hpc-partition.md) macro.

</dd> </dl>

## Return value

Specifies the result of the single calculation step.

The type of this return value must match the type of the parameter that your implementation of the [**HPC\_Merge**](hpc-merge.md) macro takes.

## Remarks

You implement this macro for an Excel workbook for which you want to run calculations on an HPC cluster as part of the partition, calculate, and merge macro framework. This macro represents the calculate stage of that framework. The framework implements an iterative calculation model for the workbook, where different calculation steps are performed on different nodes in the HPC cluster. The calculate stage of the framework runs the individual calculation steps.

The HPC Services for Excel client library calls this macro multiple times for a workbook calculation, once for each calculation step. The client library calls this macro on the compute nodes of the HPC cluster, not on the client computer. When the calculation step runs on a compute node, HPC Services for Excel copies the workbook to the compute node.

The [**HPC\_Merge**](hpc-merge.md) macro does not necessarily receive results for the calculation steps from the **HPC\_Execute** macro in the same order that the [**HPC\_Partition**](hpc-partition.md) macro sent the data for those steps to the HPC cluster. The return value for the **HPC\_Execute** macro should include information about the location in the workbook for which the calculation was performed, so that the **HPC\_Merge** macro can update the appropriate location in the workbook.

## Examples

For example implementations of the **HPC\_Execute** macro, see the following resources:

-   [Accelerating Excel 2010 with Windows HPC Server 2008 R2: Building VBA applications and workbooks for a Windows HPC Cluster](http://go.microsoft.com/fwlink/p/?linkid=205876) (http://go.microsoft.com/fwlink/p/?linkid=205876)

-   The macros in the VBASample.xlsm workbook that is included in the Excel\\ExcelRunner folder in the sample code package for the [Windows HPC Pack 2008 R2 SDK](http://go.microsoft.com/fwlink/p/?linkid=205875) (http://go.microsoft.com/fwlink/p/?linkid=205875)

## Requirements



|                    |                                              |
|--------------------|----------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 Client Utilities<br/> |



## See also

<dl> <dt>

[**HPC\_Partition**](hpc-partition.md)
</dt> <dt>

[**HPC\_Merge**](hpc-merge.md)
</dt> </dl>

 

 




