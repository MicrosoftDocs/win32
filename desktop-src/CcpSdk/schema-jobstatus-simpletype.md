---
Description: 'Defines the job status values.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2947c85e-d4db-4f77-a15e-08694a8c0b5b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobStatus Simple Type
---

# JobStatus Simple Type

Defines the job status values.

``` syntax
<xs:simpleType name="JobStatus">
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

The **JobStatus** simple type defines the following values.



| Value        | Description                                                                |
|--------------|----------------------------------------------------------------------------|
| NotSubmitted | The job has not been submitted.<br/>                                 |
| Queued       | The job has been successfully submitted.<br/>                        |
| Running      | The job is running.<br/>                                             |
| Finished     | The job has finished.<br/>                                           |
| Failed       | The job has failed due to an application error or a node error.<br/> |
| Cancelled    | The job was canceled.<br/>                                           |



## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Simple Types](schema-simple-types.md)
</dt> </dl>

 

 




