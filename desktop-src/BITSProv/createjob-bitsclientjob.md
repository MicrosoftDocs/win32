---
title: CreateJob method of the BitsClientJob class
description: The CreateJob method creates a BITS transfer job with the specified parameters. Default values are used for optional parameters if values are not specified.
ms.assetid: 'be86f7a1-2dc9-4376-8cde-2b2eb527859b'
keywords: ["CreateJob method", "CreateJob method, BitsClientJob class", "BitsClientJob class, CreateJob method"]
topic_type:
- apiref
api_name:
- BitsClientJob.CreateJob
api_location:
- Root\microsoft\bits
api_type:
- COM
---

# CreateJob method of the BitsClientJob class

The **CreateJob** method creates a BITS transfer job with the specified parameters. Default values are used for optional parameters if values are not specified.

## Syntax


```mof
uint32 CreateJob(
  [in]           string  DisplayName,
  [in]           string  RemoteUrl,
  [in]           string  LocalFile,
  [in, optional] uint16  ServiceAccount,
  [in, optional] uint16  Type,
  [in, optional] boolean Suspend,
  [in, optional] string  Description,
  [out]          string  JobId
);
```



## Parameters

<dl> <dt>

*DisplayName* \[in\]
</dt> <dd>

Specifies the name of the BITS transfer job.

</dd> <dt>

*RemoteUrl* \[in\]
</dt> <dd>

Specifies the name of the remote file in the BITS transfer job.

</dd> <dt>

*LocalFile* \[in\]
</dt> <dd>

Specifies the name of the local file in the BITS transfer job.

</dd> <dt>

*ServiceAccount* \[in, optional\]
</dt> <dd>

Defines the context in which the BITS transfer job is created. The following values are possible:



| Value                                                                        | Meaning                             |
|------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>0</dt> </dl> | LocalSystem<br/>              |
| <dl> <dt>1</dt> </dl> | LocalService<br/>             |
| <dl> <dt>2</dt> </dl> | NetworkService (default)<br/> |



 

</dd> <dt>

*Type* \[in, optional\]
</dt> <dd>

Specifies the type of BITS transfer job. This parameter can be set to one of the following values:



| Value                                                                        | Meaning                       |
|------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>0</dt> </dl> | Download (default)<br/> |
| <dl> <dt>1</dt> </dl> | Upload<br/>             |



 

</dd> <dt>

*Suspend* \[in, optional\]
</dt> <dd>

Specifies the BITS transfer job state immediately after creation. This parameter can be set to one of the following values:



| Value                                                                                                                                | Meaning                                   |
|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Suspend<br/>                        |
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Transfer immediately (default)<br/> |



 

</dd> <dt>

*Description* \[in, optional\]
</dt> <dd>

Specifies the job description.

</dd> <dt>

*JobId* \[out\]
</dt> <dd>

Specifies the job identifier.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsClientJob**](bitsclientjob.md)
</dt> </dl>

 

 





