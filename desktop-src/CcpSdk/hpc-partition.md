---
Description: 'Collects the information that you need to initiate a single calculation step for an Excel workbook on an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4CEFB80B-8D2B-4EBD-A9B2-AEA9E35DB7EE'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'HPC\_Partition method'
---

# HPC\_Partition method

Collects the information that you need to initiate a single calculation step for an Excel workbook on an HPC cluster.

## Syntax


```VB
Function HPC_Partition() As any base type or Variant[]
```



## Parameters

This method has no parameters.

## Return value

Specifies the information that is needed to perform a single calculation step in the Excel workbook. For example, if you want to split up the calculation by rows, then this return value could be the number of the row to use for the calculation.

When the last calculation step is complete, this macro should return **Null**.

The type of this return value must match the type of the parameter that your implementation of the [**HPC\_Execute**](hpc-execute.md) macro takes.

## Remarks

You implement this macro for an Excel workbook for which you want to run calculations on an HPC cluster as part of the partition, calculate, and merge macro framework. This macro represents the partition stage of that framework. The framework implements an iterative calculation model for the workbook, where different calculation steps are performed on different nodes in the HPC cluster. The partition stage of the framework establishes how the overall calculation is split into individual calculation steps.

The HPC Services for Excel client library calls this macro multiple times for a workbook calculation, once for each calculation step.

This macro runs on the client computer. When the return value of this macro is sent to the [**HPC\_Execute**](hpc-execute.md) macro, that information is sent through the HPC Job Scheduler Service from the client computer to the compute node that performs the calculation step. This data transmission occurs asynchronously, so that **HPC\_Execute** does not necessarily complete one calculation step before the next iteration of **HPC\_Partition** sends the information for the subsequent step.

To improve performance, you should minimize the work that you perform in the **HPC\_Partition** macro, including the calculation and display tasks. For example, you should open external resources such as log files and database connections in the [**HPC\_Initialize**](hpc-initialize.md) macro rather than in the **HPC\_Partition** macro. You should also avoid reading large sets of data in the **HPC\_Partition** macro.

## Examples

For example implementations of the **HPC\_Partition** macro, see the following resources:

-   [Accelerating Excel 2010 with Windows HPC Server 2008 R2: Building VBA applications and workbooks for a Windows HPC Cluster](http://go.microsoft.com/fwlink/p/?linkid=205876) (http://go.microsoft.com/fwlink/p/?linkid=205876)

-   The macros in the VBASample.xlsm workbook that is included in the Excel\\ExcelRunner folder in the sample code package for the [Windows HPC Pack 2008 R2 SDK](http://go.microsoft.com/fwlink/p/?linkid=205875) (http://go.microsoft.com/fwlink/p/?linkid=205875)

## Requirements



|                    |                                              |
|--------------------|----------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 Client Utilities<br/> |



## See also

<dl> <dt>

[**HPC\_Execute**](hpc-execute.md)
</dt> <dt>

[**HPC\_Merge**](hpc-merge.md)
</dt> </dl>

 

 




