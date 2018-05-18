---
Description: 'Performs any initialization steps that are necessary before calculations for an Excel workbook are performed on an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5676DDC6-3328-46C3-87A0-4B1E5C50E678'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'HPC\_Initialize method'
---

# HPC\_Initialize method

Performs any initialization steps that are necessary before calculations for an Excel workbook are performed on an HPC cluster.

## Syntax


```VB
Function HPC_Initialize()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

You optionally implement this macro for an Excel workbook for which you want to run calculations on an HPC cluster as part of the partition, calculate, and merge macro framework.

When you run a calculation for an Excel workbook on an HPC cluster, the client library first calls the [**HPC\_GetVersion**](hpc-getversion.md) macro, and then it calls the **HPC\_Initialize** macro.

Implement this macro to perform the initialization tasks that are necessary for the entire calculation, such as resetting counter variables, clearing old results from the spreadsheet, turning off the display of updates to the workbook during the calculation, and opening external resources such as log files or database connections.

If you make changes to the spreadsheet in the [**HPC\_Merge**](hpc-merge.md) macro, you can improve the processing time by turning screen updates off in the **HPC\_Initialize** macro and then turning them back on in the [**HPC\_Finalize**](hpc-finalize.md) macro. Set the value of the [**Application.ScreenUpdating**](08fa0272-faeb-f8f2-c0f2-e001620cc838) property to turn screen updates on or off.

## Examples

For example implementations of the **HPC\_Initialize** macro, see the following resources:

-   [Accelerating Excel 2010 with Windows HPC Server 2008 R2: Building VBA applications and workbooks for a Windows HPC Cluster](http://go.microsoft.com/fwlink/p/?linkid=205876) (http://go.microsoft.com/fwlink/p/?linkid=205876)

-   The macros in the VBASample.xlsm workbook that is included in the Excel\\ExcelRunner folder in the sample code package for the [Windows HPC  Pack 2008 R2 SDK](http://go.microsoft.com/fwlink/p/?linkid=205875) (http://go.microsoft.com/fwlink/p/?linkid=205875)

## Requirements



|                    |                                              |
|--------------------|----------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 Client Utilities<br/> |



## See also

<dl> <dt>

[**HPC\_GetVersion**](hpc-getversion.md)
</dt> <dt>

[**HPC\_Finalize**](hpc-finalize.md)
</dt> </dl>

 

 




