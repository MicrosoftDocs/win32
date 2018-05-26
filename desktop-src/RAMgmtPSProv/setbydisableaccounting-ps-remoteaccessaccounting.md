---
title: SetByDisableAccounting method of the PS\_RemoteAccessAccounting class
description: This cmdlet does the following1. Enables inbox and RADIUS accounting (both external RADIUS and Windows accounting) and configures their settings2. Disables inbox and RADIUS accounting.
audience: developer
ms.assetid: e1132a4a-2085-4724-8b7a-feef13713ae9
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByDisableAccounting method
- SetByDisableAccounting method, PS_RemoteAccessAccounting class
- PS_RemoteAccessAccounting class, SetByDisableAccounting method
topic_type:
- apiref
api_name:
- PS_RemoteAccessAccounting.SetByDisableAccounting
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByDisableAccounting method of the PS\_RemoteAccessAccounting class

This cmdlet does the following1. Enables inbox and RADIUS accounting (both external RADIUS and Windows accounting) and configures their settings2. Disables inbox and RADIUS accounting.

## Syntax


```mof
uint32 SetByDisableAccounting(
  [in]  string                 DisableAccountingType,
  [in]  string                 ComputerName,
  [in]  boolean                PassThru,
  [out] RemoteAccessAccounting cmdletOutput
);
```



## Parameters

<dl> <dt>

*DisableAccountingType* \[in\]
</dt> <dd>

Indicates the accounting type that has to be disabled. Can take one of the following values. 1. Inbox 2. ExternalRadius

<dt>

<span id="Inbox"></span><span id="inbox"></span><span id="INBOX"></span>

**Inbox** ("Inbox")


</dt> <dd></dd> <dt>

<span id="ExternalRadius"></span><span id="externalradius"></span><span id="EXTERNALRADIUS"></span>

**ExternalRadius** ("ExternalRadius")


</dt> <dd></dd> </dl> </dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the object that represents the accounting configuration for Remote Access. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Status of inbox accounting (Enable, Disable) and store limit 2. Status of RADIUS accounting (Disable, Windows, ExternalRadius, LocalNps) and list of RADIUS servers if it is ExternalRadius

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessAccounting**](ps-remoteaccessaccounting.md)
</dt> </dl>

 

 





