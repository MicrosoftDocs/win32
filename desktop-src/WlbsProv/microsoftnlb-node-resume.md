---
title: Resume method of the MicrosoftNLB\_Node class
description: Resumes cluster operations on the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e8a3ac15-8dbf-4b6d-8022-d8956f0a6e80
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Resume method
- Resume method, MicrosoftNLB_Node class
- MicrosoftNLB_Node class, Resume method
topic_type:
- apiref
api_name:
- MicrosoftNLB_Node.Resume
api_location:
- WlbsProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Resume method of the MicrosoftNLB\_Node class

Resumes cluster operations on the [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly).

## Syntax


```mof
uint32 Resume();
```



## Parameters

This method has no parameters.

## Return value

This method returns a **uint32** set to one of the [standard return values](standard-return-values.md).

<dl> <dt>

**WLBS\_OK** (1000)
</dt> <dt>

**WLBS\_ALREADY** (1001)
</dt> </dl>

## Remarks

This method will fail if called on an instance of a [**MicrosoftNLB\_Node**](https://msdn.microsoft.com/library/aa371151) object that represents a remote node.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftNLB\_Node**](https://msdn.microsoft.com/library/aa371151)
</dt> <dt>

[**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)
</dt> <dt>

[**MicrosoftNLB\_Node**](microsoftnlb-node.md)
</dt> </dl>

 

 





