---
title: AddFile method of the BitsClientJob class
description: The AddFile method adds a file to an existing BITS transfer job.
ms.assetid: 9eb1009f-395e-42cf-a981-f219dafc0584
keywords:
- AddFile method
- AddFile method, BitsClientJob class
- BitsClientJob class, AddFile method
topic_type:
- apiref
api_name:
- BitsClientJob.AddFile
api_location:
- Root\microsoft\bits
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddFile method of the BitsClientJob class

The **AddFile** method adds a file to an existing BITS transfer job.

## Syntax


```mof
uint32 AddFile(
  [in] string remoteUrl,
  [in] string localFile
);
```



## Parameters

<dl> <dt>

*remoteUrl* \[in\]
</dt> <dd>

Specifies the remote URL for the file transfer.

</dd> <dt>

*localFile* \[in\]
</dt> <dd>

Specifies the local file for the file transfer.

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

 

 





