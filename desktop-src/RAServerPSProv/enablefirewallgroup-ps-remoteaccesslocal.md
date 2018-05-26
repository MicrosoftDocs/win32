---
title: EnableFirewallGroup method of the PS\_RemoteAccessLocal class
description: This method enables the firewall group.
audience: developer
ms.assetid: d72d7c3f-4ec6-4535-8efa-d03c7ac66054
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableFirewallGroup method
- EnableFirewallGroup method, PS_RemoteAccessLocal class
- PS_RemoteAccessLocal class, EnableFirewallGroup method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.EnableFirewallGroup
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableFirewallGroup method of the PS\_RemoteAccessLocal class

This method enables the firewall group.

## Syntax


```mof
uint32 EnableFirewallGroup(
  [in] string  FirewallGroupName,
  [in] boolean bEnable
);
```



## Parameters

<dl> <dt>

*FirewallGroupName* \[in\]
</dt> <dd>

Name of the Firewall Rule group to Enable/Disable.

</dd> <dt>

*bEnable* \[in\]
</dt> <dd>

Boolean to indicate whether to Enable or Disable the Firewall Rule Group

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





