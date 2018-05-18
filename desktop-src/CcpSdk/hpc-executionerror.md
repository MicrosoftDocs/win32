---
Description: 'Handles errors that occur during a calculation for an Excel workbook on an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7D257F05-85E7-4AF9-B10C-88592AD45DDF'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'HPC\_ExecutionError method'
---

# HPC\_ExecutionError method

Handles errors that occur during a calculation for an Excel workbook on an HPC cluster.

## Syntax


```VB
Function HPC_ExecutionError( _
  ByVal errorMessage     As string, _
  ByVal errorDetails As string _
)
```



## Parameters

<dl> <dt>

*errorMessage* 
</dt> <dd>

String that specifies the error message.

</dd> <dt>

*errorDetails* 
</dt> <dd>

String that provides detailed information about the error.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

You optionally implement this macro for an Excel workbook for which you want to run calculations on an HPC cluster as part of the partition, calculate, and merge macro framework.

This macro is not required, but if you do not implement this macro, error messages are not visible to the user. Implement this macro to accept error messages and then display them to the user, handle them internally, or ignore them.

## Examples

For an example implementation of the **HPC\_ExecutionError** macro, see the macros in the VBASample.xlsm workbook that is included in the Excel\\ExcelRunner folder in the sample code package for the [Windows HPC Pack 2008 R2 SDK](http://go.microsoft.com/fwlink/p/?linkid=205875) (http://go.microsoft.com/fwlink/p/?linkid=205875).

## Requirements



|                    |                                              |
|--------------------|----------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 Client Utilities<br/> |



 

 




