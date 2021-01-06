---
description: Control of the collector instance. Requires the Administrator (BA) privileges.
ms.assetid: 83b485b2-b03b-4882-a3ff-187eac299755
ms.tgt_platform: multiple
title: Control class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Control
api_type: 
- DllExport
api_location: 
- BEvtCol.exe
---

# Control class

Control of the collector instance. Requires the Administrator (BA) privileges.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("BootEventCollectorWmiProvider"), AMENDMENT]
class Control
{
};
```

## Members

The **Control** class has these types of members:

-   [Methods](#methods)

### Methods

The **Control** class has these methods.



| Method                                                         | Description                                                                                                                                                                                                                                                                                                                                                               |
|:---------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Checkpoint**](control-checkpoint.md)                       | If the current configuration is a result of the Undo/Redo/Restore, marks it as if it has been set explicitly, so that the history will preserve the time when it was set, and a backup file will be created for it on the next configuration change. If the current configuration was already set explicitly, has no effect. Returns 1 on success, 0 on error.<br/> |
| [**DumpDiagnostics**](control-dumpdiagnostics.md)             | Dump the diagnostic information into the log.<br/>                                                                                                                                                                                                                                                                                                                  |
| [**FastShutdown**](control-fastshutdown.md)                   | Stop the collector quickly, discarding all the queued data.<br/>                                                                                                                                                                                                                                                                                                    |
| [**Flush**](control-flush.md)                                 | Flush the forwarder buffers.<br/>                                                                                                                                                                                                                                                                                                                                   |
| [**GetConfiguration**](control-getconfiguration.md)           | Read the active configuration of the collector.<br/>                                                                                                                                                                                                                                                                                                                |
| [**IsConfigurationEqual**](control-isconfigurationequal.md)   | Compare the argument with the active configuration of the collector. Returns 1 if they match, 0 if they don't.<br/>                                                                                                                                                                                                                                                 |
| [**ListBackups**](control-listbackups.md)                     | Return the list of the saved backup configuration files that can be restored.<br/>                                                                                                                                                                                                                                                                                  |
| [**Redo**](control-redo.md)                                   | Reset the active configuration of the collector from the later backup file (determined by going forward from the current original timestamp). If the configuration has been undone, this means redoing the undone change. Returns 1 on success, 0 on error.<br/>                                                                                                    |
| [**RestoreFile**](control-restorefile.md)                     | Restore the active configuration of the collector from a backup file. Returns 1 on success, 0 on error.<br/>                                                                                                                                                                                                                                                        |
| [**RestoreFromTime**](control-restorefromtime.md)             | Restore the active configuration of the collector from a backup file, selected by a timestamp. Returns 1 on success, 0 on error.<br/>                                                                                                                                                                                                                               |
| [**SetConfiguration**](control-setconfiguration.md)           | Set the new active configuration of the collector. Returns 1 on success, 0 on error.<br/>                                                                                                                                                                                                                                                                           |
| [**Shutdown**](control-shutdown.md)                           | Stop the collector. If the collector is running as a service, stopping the service is the better approach.<br/>                                                                                                                                                                                                                                                     |
| [**Undo**](control-undo.md)                                   | Restore the active configuration of the collector from the previous backup file (determined by going back from the current original timestamp). If the configuration has been just set, this means undoing that change. The consecutive calls will undo to the earlier and earlier configurations. Returns 1 on success, 0 on error.<br/>                           |
| [**ValidateConfiguration**](control-validateconfiguration.md) | Validate a configuration text for correctness without setting it active. Returns 1 on success, 0 on error.<br/>                                                                                                                                                                                                                                                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\BootEventCollector<br/>                                              |
| MOF<br/>                      | <dl> <dt>BootEventCollectorWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>BEvtCol.exe</dt> </dl>               |



 

 




