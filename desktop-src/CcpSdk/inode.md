---
Description: 'Contains information about a compute node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '55a824be-0b17-4280-a68c-a12a7c5f78c9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: INode interface
---

# INode interface

Contains information about a compute node.

To get this interface, call the [**ICluster::get\_ComputeNodes**](icluster-get-computenodes.md) method.

## Members

The **INode** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INode** also has these types of members:

-   [Methods](#methods)

### Methods

The **INode** interface has these methods.



| Method                                                                  | Description                                                      |
|:------------------------------------------------------------------------|:-----------------------------------------------------------------|
| [**get\_Memory**](inode-get-memory.md)                                 | Retrieves the size of available memory, in kilobytes.<br/> |
| [**get\_Name**](inode-get-name.md)                                     | Retrieves the name of the compute node.<br/>               |
| [**get\_NumberOfIdleProcessors**](inode-get-numberofidleprocessors.md) | Retrieves the number of idle processors.<br/>              |
| [**get\_NumberOfProcessors**](inode-get-numberofprocessors.md)         | Retrieves the number of processors.<br/>                   |
| [**get\_ProcessorArchitecture**](inode-get-processorarchitecture.md)   | Retrieves the processor architecture.<br/>                 |
| [**get\_ProcessorSpeed**](inode-get-processorspeed.md)                 | Retrieves the processor speed, in megahertz (MHz).<br/>    |
| [**get\_Status**](inode-get-status.md)                                 | Retrieves the current status of the head node.<br/>        |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[Compute Cluster Architecture](compute-cluster-architecture.md)
</dt> <dt>

[CCP Interfaces](interfaces.md)
</dt> </dl>

 

 




