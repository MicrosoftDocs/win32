---
title: GetProviderIdentity method of the WT\_iSCSIStorageProviderIdentity class
description: This method extracts the Identity currently configured for the specified AppID.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c6144f50-ead3-48fe-af01-11c3b699f07c
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetProviderIdentity method iSCSI Software Target API
- GetProviderIdentity method iSCSI Software Target API , WT_iSCSIStorageProviderIdentity class
- WT_iSCSIStorageProviderIdentity class iSCSI Software Target API , GetProviderIdentity method
topic_type:
- apiref
api_name:
- WT_iSCSIStorageProviderIdentity.GetProviderIdentity
api_location:
- StrgPrvdMgmt.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetProviderIdentity method of the WT\_iSCSIStorageProviderIdentity class

This method extracts the Identity currently configured for the specified AppID. This is a static method.

## Syntax


```mof
uint32 GetProviderIdentity(
  [in]  string AppID,
  [out] string UserName
);
```



## Parameters

<dl> <dt>

*AppID* \[in\]
</dt> <dd>

Specifies the [AppID](https://msdn.microsoft.com/library/windows/desktop/ms688754) for the DCOM object for iSCSI the storage provider.

</dd> <dt>

*UserName* \[out\]
</dt> <dd>

Receives the username of the account under which the iSCSI storage provider runs.

</dd> </dl>

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

[**WT\_iSCSIStorageProviderIdentity**](wt-iscsistorageprovideridentity.md)
</dt> <dt>

[AppID Key](https://msdn.microsoft.com/library/windows/desktop/ms682359)
</dt> </dl>

 

 





