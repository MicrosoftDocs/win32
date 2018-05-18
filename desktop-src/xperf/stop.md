---
title: stop
description: Displays the trace stop options.
ms.assetid: '24349126-5a54-4939-bc4c-e3f241ec2b93'
keywords: ["stop Windows Performance Analyzer"]
topic_type:
- apiref
api_name:
- stop
api_type:
- NA
---

# stop

Displays the trace stop options.

``` syntax
xperf [-stop [LoggerNames]| [ProfileFileName!ProfileName|SessionName merged.etl]]|
      [-stopall]|
      [-cancel ProfileFileName!ProfileName|SessionName [NoDelete]] [-d merged.etl] [-heap|-critsec]
```

### Examples

The following table shows examples of the **stop** options.



| Command                                                                               | Meaning                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **-stop** LoggerNames\|ProfileFileName!ProfileName\|SessionName merged.etl<br/> | Turn off loggers specified in LoggerNames. Or turns off loggers in profile ProfileName defined in file ProfileFileName and merge the ETL files to merged.etl. Or Turns off logger SessionName defined in file ProfileFileName and merge the ETL file to merged.etl.<br/>  |
| **-StopAll**<br/>                                                               | Turn off all logging sessions.<br/>                                                                                                                                                                                                                                       |
| **-cancel** ProfileFileName!ProfileName\|SessionName \[NoDelete\]<br/>          | Turn off loggers in profile ProfileName defined in file ProfileFileName and delete the trace files. Or Turns off logger SessionName defined in file ProfileFileName and merge the ETL file to merged.etl. If NoDelete is specified than trace files are not deleted.<br/> |
| **-d** MergedETL <br/>                                                          | Merge the ETL files of stopped logging sessions into MergedETL; if no session is stopped explicitly, the "NT Kernel Logger" stopped implicitly.<br/>                                                                                                                      |
| **-BootTrace off**<br/>                                                         | Turn off boot trace.<br/>                                                                                                                                                                                                                                                 |
| **-heap**<br/>                                                                  | Stop heap tracing.<br/>                                                                                                                                                                                                                                                   |
| **-critsec**<br/>                                                               | Stop CritSec tracing.<br/>                                                                                                                                                                                                                                                |



 

> [!Note]  
> Currently only one of heap tracing and critical section tracing can be active at same time. Therefore, **-heap** and **-critsec** are mutually exclusive. If LoggerNames are not given, or **-d** is specified with neither **-stop** nor **-stopall** present, the kernel logger will be stopped.

 

 

 





