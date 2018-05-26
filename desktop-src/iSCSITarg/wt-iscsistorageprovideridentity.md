---
title: WT\_iSCSIStorageProviderIdentity class
description: This class supports the iSCSIStorageProviderIdentity noun.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4f0c42e5-9288-4cdf-880e-0a34deacfbd8
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_iSCSIStorageProviderIdentity class iSCSI Software Target API
- WT_iSCSIStorageProviderIdentity class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_iSCSIStorageProviderIdentity
api_location:
- StrgPrvdMgmt.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WT\_iSCSIStorageProviderIdentity class

This class supports the iSCSIStorageProviderIdentity noun.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_iSCSIStorageProviderIdentity
{
};
```

## Members

The **WT\_iSCSIStorageProviderIdentity** class has these types of members:

-   [Methods](#methods)

### Methods

The **WT\_iSCSIStorageProviderIdentity** class has these methods.



| Method                                                                             | Description                                                                                                                    |
|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**GetProviderIdentity**](getprovideridentity-wt-iscsistorageprovideridentity.md) | This method extracts the Identity currently configured for the specified [AppID](https://msdn.microsoft.com/library/windows/desktop/ms688754).<br/>                        |
| [**SetProviderIdentity**](setprovideridentity-wt-iscsistorageprovideridentity.md) | This method sets the Identity under which the iSCSI Target storage providers will run as Out-Of-Process components.<br/> |



 

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Wmi<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>StrgPrvdMgmt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StrgPrvdMgmt.dll</dt> </dl> |



## See also

<dl> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





