---
Description: 'Provides the result of a command that is executed on a node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b51c6baa-331d-47c8-9a6b-f950f4c2eee5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: IExecutionResult interface
---

# IExecutionResult interface

Provides the result of a command that is executed on a node.

The following methods return this interface as elements of a collection:

-   [**ICluster::ExecuteCommand**](icluster-executecommand.md)
-   [**ICluster::ExecuteCommandWithPaging**](icluster-executecommandwithpaging.md)
-   [**ICluster::WaitForCommand**](icluster-waitforcommand.md)
-   [**ICluster::WaitForCommandWithPaging**](icluster-waitforcommandwithpaging.md)

## Members

The **IExecutionResult** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IExecutionResult** also has these types of members:

-   [Methods](#methods)

### Methods

The **IExecutionResult** interface has these methods.



| Method                                                   | Description                                                  |
|:---------------------------------------------------------|:-------------------------------------------------------------|
| [**get\_CommandId**](iexecutionresult-get-commandid.md) | Retrieves the identifier of the command that ran.<br/> |
| [**get\_ExitCode**](iexecutionresult-get-exitcode.md)   | Retrieves the exit code.<br/>                          |
| [**get\_NodeName**](iexecutionresult-get-nodename.md)   | Retrieves the node name.<br/>                          |
| [**get\_Output**](iexecutionresult-get-output.md)       | Retrieves the output.<br/>                             |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[CCP Interfaces](interfaces.md)
</dt> </dl>

 

 




