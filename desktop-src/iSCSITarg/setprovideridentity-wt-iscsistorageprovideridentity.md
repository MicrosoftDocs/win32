---
title: SetProviderIdentity method of the WT\_iSCSIStorageProviderIdentity class
description: This method sets the Identity under which the iSCSI Target storage providers will run as Out-Of-Proc components.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b41eb24f-1b34-4c40-b119-5f5719830ee6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetProviderIdentity method iSCSI Software Target API", "SetProviderIdentity method iSCSI Software Target API , WT_iSCSIStorageProviderIdentity class", "WT_iSCSIStorageProviderIdentity class iSCSI Software Target API , SetProviderIdentity method"]
topic_type:
- apiref
api_name:
- WT_iSCSIStorageProviderIdentity.SetProviderIdentity
api_location:
- StrgPrvdMgmt.dll
api_type:
- COM
---

# SetProviderIdentity method of the WT\_iSCSIStorageProviderIdentity class

This method sets the Identity under which the iSCSI Target storage providers will run as Out-Of-Proc components. This is a static method.

## Syntax


```mof
uint32 SetProviderIdentity(
  [in] string AppID,
  [in] string UserName,
  [in] string Password
);
```



## Parameters

<dl> <dt>

*AppID* \[in\]
</dt> <dd>

Specifies the [AppID](https://msdn.microsoft.com/library/windows/desktop/ms688754) for the DCOM object for iSCSI the storage provider.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

Specifies the username of the account under which the iSCSI storage provider will run.

</dd> <dt>

*Password* \[in\]
</dt> <dd>

Specifies the password for the account.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Wmi<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>StrgPrvdMgmt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StrgPrvdMgmt.dll</dt> </dl> |



## See also

<dl> <dt>

[**WT\_iSCSIStorageProviderIdentity**](wt-iscsistorageprovideridentity.md)
</dt> <dt>

[AppID Key](https://msdn.microsoft.com/library/windows/desktop/ms682359)
</dt> </dl>

 

 





