---
Description: 'Performs any necessary global cleanup tasks or post-calculation processing after the calculations for an Excel workbook complete on an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7565D2D7-E922-42B3-8CA6-D5F00BD4138C'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'HPC\_Finalize method'
---

# HPC\_Finalize method

Performs any necessary global cleanup tasks or post-calculation processing after the calculations for an Excel workbook complete on an HPC cluster.

## Syntax


```VB
Function HPC_Finalize()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

You optionally implement this macro for an Excel workbook for which you want to run calculations on an HPC cluster as part of the partition, calculate, and merge macro framework.

When you run a calculation for an Excel workbook on an HPC cluster, the client library calls this macro last, after the library calls all of the other macros.

Implement this macro to perform post-calculation processing and cleanup tasks, such as turning the display of updates to the workbook back on and closing external resources (such as log files or database connections).

## Examples

For example implementations of the **HPC\_Finalize** macro, see the following resources:

-   [Accelerating Excel 2010 with Windows HPC Server 2008 R2: Building VBA applications and workbooks for a Windows HPC Cluster](http://go.microsoft.com/fwlink/p/?linkid=205876) (http://go.microsoft.com/fwlink/p/?linkid=205876)

-   The macros in the VBASample.xlsm workbook that is included in the Excel\\ExcelRunner folder in the sample code package for the [Windows HPC Pack 2008 R2 SDK](http://go.microsoft.com/fwlink/p/?linkid=205875) (http://go.microsoft.com/fwlink/p/?linkid=205875)

## Requirements



|                    |                                              |
|--------------------|----------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 Client Utilities<br/> |



## See also

<dl> <dt>

[**HPC\_Initialize**](hpc-initialize.md)
</dt> </dl>

 

 




