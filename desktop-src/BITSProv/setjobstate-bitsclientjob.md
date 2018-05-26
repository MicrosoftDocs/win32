---
title: SetJobState method of the BitsClientJob class
description: The SetJobState method tries to change the state of a BITS transfer job.
ms.assetid: c35fa129-429b-47a2-80d2-e73c1fd9b100
keywords:
- SetJobState method
- SetJobState method, BitsClientJob class
- BitsClientJob class, SetJobState method
topic_type:
- apiref
api_name:
- BitsClientJob.SetJobState
api_location:
- Root\microsoft\bits
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetJobState method of the BitsClientJob class

The **SetJobState** method tries to change the state of a BITS transfer job.

## Syntax


```mof
uint32 SetJobState(
  [in] Uint16 JobState
);
```



## Parameters

<dl> <dt>

*JobState* \[in\]
</dt> <dd>

Specifies the action used to change the state of the BITS transfer job. The following actions are possible:



| Value                                                                        | Meaning                      |
|------------------------------------------------------------------------------|------------------------------|
| <dl> <dt>0</dt> </dl> | Cancel the job.<br/>   |
| <dl> <dt>1</dt> </dl> | Complete the job.<br/> |
| <dl> <dt>2</dt> </dl> | Resume the job.<br/>   |
| <dl> <dt>3</dt> </dl> | Suspend the job.<br/>  |



 

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsClientJob**](bitsclientjob.md)
</dt> </dl>

 

 





