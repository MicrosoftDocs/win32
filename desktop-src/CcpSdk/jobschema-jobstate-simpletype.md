---
Description: 'Defines the possible states of a job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '421df9cf-ff24-4734-8b5d-31ef6f347ad2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobState Simple Type
---

# JobState Simple Type

Defines the possible states of a job.

``` syntax
<xs:simpleType name="JobState">
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
            value="ExternalValidation"
         />
        <xs:enumeration
            value="Queued"
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

The **JobState** simple type defines the following values.



| Value              | Description                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------|
| Configuring        | The job is being configured.<br/>                                                                |
| Submitted          | The job was submitted to the scheduling queue.<br/>                                              |
| Validating         | The server is determining if the job can run. <br/>                                              |
| ExternalValidation | A submission filter is determining if the job can run. <br/>                                     |
| Queued             | The job passed validation and was added to the scheduling queue. <br/>                           |
| Running            | The job is running.<br/>                                                                         |
| Finishing          | The server is cleaning up the resources that were allocated to the job.<br/>                     |
| Finished           | The job successfully finished (all the tasks in the job finished successfully).<br/>             |
| Failed             | One or more of the tasks in the job failed or a system error occurred on the compute node. <br/> |
| Canceled           | The job was canceled.<br/>                                                                       |
| Canceling          | The job is in the process of being canceled. <br/>                                               |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




