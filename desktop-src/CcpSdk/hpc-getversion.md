---
Description: 'Gets the version of the macro framework that the Excel workbook uses to run calculations on an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '492EEC5C-71E4-4892-A9C8-906531D08AC6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'HPC\_GetVersion method'
---

# HPC\_GetVersion method

Gets the version of the macro framework that the Excel workbook uses to run calculations on an HPC cluster.

## Syntax


```VB
Function HPC_GetVersion() As String
```



## Parameters

This method has no parameters.

## Return value

A string with a format of *major\_version\_number*.*minor\_version\_number* that indicates the version of the macro framework that the Excel workbook uses to run calculations on an HPC cluster. For Windows HPC Server 2008 R2, this value should always be 1.0.

## Remarks

You implement this macro for an Excel workbook for which you want to run calculations on an HPC cluster as part of the partition, calculate, and merge macro framework.

When you run a calculation in an Excel workbook on an HPC cluster, the client library calls this macro first, before the library calls the [**HPC\_Initialize**](hpc-initialize.md) macro.

## Examples

For an example implementation of the **HPC\_GetVersion** macro, see the macros in the VBASample.xlsm workbook that is included in the Excel\\ExcelRunner folder in the sample code package for the [Windows HPC Pack 2008 R2 SDK](http://go.microsoft.com/fwlink/p/?linkid=205875) (http://go.microsoft.com/fwlink/p/?linkid=205875).

## Requirements



|                    |                                              |
|--------------------|----------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 Client Utilities<br/> |



## See also

<dl> <dt>

[**HPC\_Initialize**](hpc-initialize.md)
</dt> </dl>

 

 




