---
Description: 'Defines the task status values.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fce18d54-c7dd-452f-9e75-2c47463acbed'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: TaskStatus Simple Type
---

# TaskStatus Simple Type

Defines the task status values.

``` syntax
<xs:simpleType name="TaskStatus">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="NotSubmitted"
         />
        <xs:enumeration
            value="Queued"
         />
        <xs:enumeration
            value="Running"
         />
        <xs:enumeration
            value="Finished"
         />
        <xs:enumeration
            value="Failed"
         />
        <xs:enumeration
            value="Cancelled"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **TaskStatus** simple type defines the following values.



| Value        | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| NotSubmitted | The parent job has not been submitted.<br/>                           |
| Queued       | The parent job has been successfully submitted.<br/>                  |
| Running      | The task is running.<br/>                                             |
| Finished     | The task has finished.<br/>                                           |
| Failed       | The task has failed due to an application error or a node error.<br/> |
| Cancelled    | The task was canceled.<br/>                                           |



## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Simple Types](schema-simple-types.md)
</dt> </dl>

 

 




