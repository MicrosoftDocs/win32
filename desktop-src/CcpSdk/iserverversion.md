---
Description: 'Contains the file version information for the HPC server assembly.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8419dc50-d750-42b7-9410-f3be6de99749'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IServerVersion interface
---

# IServerVersion interface

Contains the file version information for the HPC server assembly.

To get this interface, call the [**IScheduler::GetServerVersion**](ischeduler-getserverversion.md) method.

## Members

The **IServerVersion** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IServerVersion** also has these types of members:

-   [Properties](#properties)

### Properties

The **IServerVersion** interface has these properties.



| Property                                                         | Access type          | Description                                                                                      |
|:-----------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------|
| [**Build**](iserverversion-build.md)<br/>                 | Read-only<br/> | Retrieves the build component of the version number.<br/>                                  |
| [**Major**](iserverversion-major.md)<br/>                 | Read-only<br/> | Retrieves the major component of the version number.<br/>                                  |
| [**MajorRevision**](iserverversion-majorrevision.md)<br/> | Read-only<br/> | Retrieves the high 16 bits of the [**Revision**](iserverversion-revision.md) number.<br/> |
| [**Minor**](iserverversion-minor.md)<br/>                 | Read-only<br/> | Retrieves the minor component of the version number.<br/>                                  |
| [**MinorRevision**](iserverversion-minorrevision.md)<br/> | Read-only<br/> | Retrieves the low 16 bits of the [**Revision**](iserverversion-revision.md) number.<br/>  |
| [**Revision**](iserverversion-revision.md)<br/>           | Read-only<br/> | Retrieves the revision component of the version number.<br/>                               |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> </dl>

 

 




