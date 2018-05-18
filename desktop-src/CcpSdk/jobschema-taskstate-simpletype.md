---
Description: 'Defines the possible states of a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8a6abae9-2302-4243-a4a5-9dd158260de8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: TaskState Simple Type
---

# TaskState Simple Type

Defines the possible states of a task.

``` syntax
<xs:simpleType name="TaskState">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="Configuring"
         />
        <xs:enumeration
            value="Submitted"
         />
        <xs:enumeration
            value="Validating"
         />
        <xs:enumeration
            value="Queued"
         />
        <xs:enumeration
            value="Dispatching"
         />
        <xs:enumeration
            value="Running"
         />
        <xs:enumeration
            value="Finishing"
         />
        <xs:enumeration
            value="Finished"
         />
        <xs:enumeration
            value="Failed"
         />
        <xs:enumeration
            value="Canceled"
         />
        <xs:enumeration
            value="Canceling"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **TaskState** simple type defines the following values.



| Value       | Description                                                                                        |
|-------------|----------------------------------------------------------------------------------------------------|
| Configuring | The task is being configured.<br/>                                                           |
| Submitted   | The task was added to the scheduling queue.<br/>                                             |
| Validating  | The scheduler is determining if the task is correctly configured and can run.<br/>           |
| Queued      | The task passed validation and was added to the scheduling queue.<br/>                       |
| Dispatching | The scheduler is in the process of sending the task to the node to run.<br/>                 |
| Running     | The task is running.<br/>                                                                    |
| Finishing   | The node is cleaning up the resources that were allocated to the task.<br/>                  |
| Finished    | The task successfully finished.<br/>                                                         |
| Failed      | The task failed, the job was canceled, or a system error occurred on the compute node. <br/> |
| Canceled    | The task was canceled.<br/>                                                                  |
| Canceling   | The task is in the process of being canceled.<br/>                                           |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




