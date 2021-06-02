---
description: Several registry settings are available to modify CRM behavior to assist with troubleshooting and development.
ms.assetid: c4e68451-fb8a-45b5-9968-7d5a6418dfe8
title: COM+ CRM Registry Settings
ms.topic: article
ms.date: 05/31/2018
---

# COM+ CRM Registry Settings

Several registry settings are available to modify CRM behavior to assist with troubleshooting and development. All of these registry settings, which are listed and described in the following table, are optional; none are required for normal operation of the CRM.

All CRM registry settings are under **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\COM3\\CRM**. Create the **CRM** key under the **COM3** key if it is not already there.



| CRM registry settings                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **VTRACE1**<br/>                 | REG\_DWORD value. Setting this value to anything other than zero enables debug trace messages on warnings or errors. These messages can be seen in the debugger output window. This value should be set for development only and not during normal deployment. This value is read when any CRM server application starts up.<br/>                                                                                                                                                                                                                                                   |
| **IgnoreCompensatorErrors**<br/> | REG\_DWORD value. Setting this value to anything other than zero allows the CRM infrastructure to ignore all errors returned from CRM Compensators. If recovery is failing due to an error from a CRM Compensator, setting this value allows recovery to be completed. This value is read when any CRM server application starts up.<br/>                                                                                                                                                                                                                                           |
| **CheckpointIntervalInSec**<br/> | REG\_DWORD value. This is the checkpoint interval in seconds. The default checkpoint interval is 30 seconds. Checkpoints are used to reclaim space from the CRM log file. Increasing the checkpoint interval may increase performance, but at the expense of increased recovery time and a larger CRM log file. This value is read when any CRM server application starts up.<br/>                                                                                                                                                                                                  |
| **InitialLogFileSizeInKB**<br/>  | REG\_DWORD value. This is the initial CRM log file size in kilobytes. The default CRM log file size is 1024 KB (1 MB). The CRM log file automatically expands to meet the transaction load imposed upon it, but if heavy loads are anticipated, it might be necessary to increase this value. This value is read when any CRM enabled COM+ server application starts up, but if the CRM log file already exists for a CRM server application, this value is ignored for that server application.<br/>                                                                               |
| **RecoveryTraceEnabled**<br/>    | REG\_DWORD value. Setting this value to anything other than zero enables a recovery trace. The recovery trace is a text file that has the same name as the CRM log file and the following additional extension: .recoverytrace.txt. <br/> This file is located in the same directory as the CRM log file. The recovery trace provides a trace of CRM activity during recovery, which can be used for problem diagnosis. This value is read when any CRM server application starts up. However, a unique recovery trace file is produced for each CRM server application.<br/> |



 

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> </dl>

 

 




