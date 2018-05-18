---
Description: 'Defines property values used by the command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8958c63a-b60e-464b-919a-c49f068a50f9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ICommandInfo interface
---

# ICommandInfo interface

Defines property values used by the command.

To get this interface, call the [**IScheduler::CreateCommandInfo**](ischeduler-createcommandinfo.md) method.

## Members

The **ICommandInfo** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ICommandInfo** also has these types of members:

-   [Properties](#properties)

### Properties

The **ICommandInfo** interface has these properties.



| Property                                                                     | Access type          | Description                                                                   |
|:-----------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------|
| [**EnvironmentVariables**](icommandinfo-environmentvariables.md)<br/> | Read-only<br/> | Retrieves the environment variables used by the command.<br/>           |
| [**StdIn**](icommandinfo-stdin.md)<br/>                               | Read-only<br/> | Retrieves the path to the standard input file used by the command.<br/> |
| [**WorkingDirectory**](icommandinfo-workingdirectory.md)<br/>         | Read-only<br/> | Retrieves the startup directory for the command.<br/>                   |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**IRemoteCommand**](iremotecommand.md)
</dt> </dl>

 

 




