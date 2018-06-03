---
title: DVMount method of the WT\_Snapshot class
description: Mounts the current shadow copy in read-only mode on the local iSCSI Target server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 63db0989-065c-4d01-ab6e-d93f4a4bb3cd
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DVMount method iSCSI Software Target API
- DVMount method iSCSI Software Target API , WT_Snapshot class
- WT_Snapshot class iSCSI Software Target API , DVMount method
topic_type:
- apiref
api_name:
- WT_Snapshot.DVMount
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DVMount method of the WT\_Snapshot class

Mounts the current shadow copy in read-only mode on the local iSCSI Target server.

**Windows Server 2012 R2:** This method is deprecated. Use iSCSI loopback instead.

## Syntax


```mof
void DVMount();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If there is another shadow copy of the virtual disk that is also mounted, this method will dismount it before mounting the shadow copy.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Snapshot**](wt-snapshot.md)
</dt> </dl>

 

 





