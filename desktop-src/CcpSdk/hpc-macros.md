---
Description: 'HPC Services for Excel provides a framework of Visual Basic for Applications macros that you can implement for a Microsoft Excel workbook, and then use to perform calculations for the workbook on an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'C5249D82-7C3A-4906-9306-F6D887432F8B'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: HPC Macros
---

# HPC Macros

HPC Services for Excel provides a framework of Visual Basic for Applications macros that you can implement for a Microsoft Excel workbook, and then use to perform calculations for the workbook on an HPC cluster.

The following table describes the marcos in the macro framework that the HPC Services for Excel provides.



| Macro                                                        | Description                                                                                                                                                              |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**HPC\_Execute**](hpc-execute.md)<br/>               | Performs a single calculation step for an Excel workbook on a compute node in an HPC cluster.<br/>                                                                 |
| [**HPC\_ExecutionError**](hpc-executionerror.md)<br/> | Optional. Handles errors that occur during a calculation for an Excel workbook on an HPC cluster.<br/>                                                             |
| [**HPC\_Finalize**](hpc-finalize.md)<br/>             | Optional. Performs any necessary global cleanup tasks or post-calculation processing after the calculations for an Excel workbook complete on an HPC cluster.<br/> |
| [**HPC\_GetVersion**](hpc-getversion.md)<br/>         | Gets the version of the macro framework that the Excel workbook uses to run calculations on an HPC cluster.<br/>                                                   |
| [**HPC\_Initialize**](hpc-initialize.md)<br/>         | Optional. Performs any initialization steps that are necessary before calculations for an Excel workbook are performed on an HPC cluster.<br/>                     |
| [**HPC\_Merge**](hpc-merge.md)<br/>                   | Processes the result of a calculation step and inserts the processed result in the Excel workbook.<br/>                                                            |
| [**HPC\_Partition**](hpc-partition.md)<br/>           | Collects the information that you need to initiate a single calculation step for an Excel workbook on an HPC cluster.<br/>                                         |



 

 

 




