---
Description: 'The job schema defines the elements and types that represent a job object and its tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a8148635-bd69-48bc-a90f-4078b6e8acd0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Job Schema
---

# Job Schema

The job schema defines the elements and types that represent a job object and its tasks.

You can use the schema to write an XML document that you then pass to the [**ICluster::CreateJobFromXml**](icluster-createjobfromxml.md) method to create a job object.

If you specify a submission or activation filter, CCP generates an XML document that defines the job and its tasks and passes the document to your filter.

The following pages define the job schema:

-   [Schema Elements](schema-job-elements.md)
-   [Schema Simple Types](schema-simple-types.md)
-   [Schema Complex Types](schema-job-complex-types.md)

The following is an example XML document.


```xsd
<?xml version="1.0" encoding="utf-8" ?> 
<Job xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
     xmlns="http://www.microsoft.com/ComputeCluster/"
     Name="job1" 
     IsExclusive="true">
  <ExtendedTerms>
    <Term>
      <Name>JobTerm1</Name> 
      <Value>1000</Value> 
    </Term>
  </ExtendedTerms>
  <Tasks>
    <Task Name="task1" CommandLine="Notepad.exe" IsExclusive="true">
      <EnvironmentVariables>
        <Variable>
          <Name>MyEnvVar</Name> 
          <Value>EnvVarVal</Value> 
        </Variable>
      </EnvironmentVariables>
      <ExtendedTerms>
        <Term>
          <Name>TaskTerm1</Name> 
          <Value>Value1</Value> 
        </Term>
      </ExtendedTerms>
    </Task>
  </Tasks>
</Job>
```



## Related topics

<dl> <dt>

[CCP Schemas](schemas.md)
</dt> </dl>

 

 



