---
title: SetByEnableAccounting method of the PS\_RemoteAccessAccounting class
description: This cmdlet does the following1. Enables inbox and Radius accounting (both external Radius and Windows accounting) and configures their settings2. Disables inbox and Radius accounting.
audience: developer
ms.assetid: 2be3bb8c-d28e-41f2-ad2a-ff1005ddda2b
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByEnableAccounting method
- SetByEnableAccounting method, PS_RemoteAccessAccounting class
- PS_RemoteAccessAccounting class, SetByEnableAccounting method
topic_type:
- apiref
api_name:
- PS_RemoteAccessAccounting.SetByEnableAccounting
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByEnableAccounting method of the PS\_RemoteAccessAccounting class

This cmdlet does the following1. Enables inbox and Radius accounting (both external Radius and Windows accounting) and configures their settings2. Disables inbox and Radius accounting.

## Syntax


```mof
uint32 SetByEnableAccounting(
  [in]  string                 RadiusServer,
  [in]  string                 SharedSecret,
  [in]  uint16                 RadiusPort,
  [in]  uint8                  RadiusScore,
  [in]  uint32                 RadiusTimeout,
  [in]  string                 AccountingOnOffMsg,
  [in]  string                 EnableAccountingType,
  [in]  string                 ComputerName,
  [in]  boolean                PassThru,
  [out] RemoteAccessAccounting cmdletOutput
);
```



## Parameters

<dl> <dt>

*RadiusServer* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the external RADIUS server that is used for accounting. This parameter can be configured only if the EnableAccountingType parameter is specified to be ExternalRadius

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Shared secret between the Remote Access server and the specified external RADIUS server which is required for successful communication between the two servers. Note that the secret is specified in clear text. This parameter can be configured only if the EnableAccountingType parameter is specified to be ExternalRadius

</dd> <dt>

*RadiusPort* \[in\]
</dt> <dd>

Indicates the port number on which the RADIUS server is accepting authentication requests. Default is 1813. This parameter can be configured only if the EnableAccountingType parameter is specified to be ExternalRadius

</dd> <dt>

*RadiusScore* \[in\]
</dt> <dd>

Indicates the initial score. The default is 30. This parameter can be configured only if the EnableAccountingType parameter is specified to be ExternalRadius

</dd> <dt>

*RadiusTimeout* \[in\]
</dt> <dd>

The value is specified in seconds. Default is 5 secs. This parameter can be configured only if the EnableAccountingType parameter is specified to be ExternalRadius

</dd> <dt>

*AccountingOnOffMsg* \[in\]
</dt> <dd>

Indicates whether the sending of accounting on/off messages should be enabled or disabled. Can take one of the following values 1. Enabled 2. Disabled By default it is disabled

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*EnableAccountingType* \[in\]
</dt> <dd>

Indicates the accounting type that needs to be enabled. Can take one of the following values 1. Inbox 2. ExternalRadius. When inbox accounting is enabled the store size is set to 12 months automatically. The Set-RemoteAccessInboxAccountingStore cmdlet is used to change the store size on individual Remote Access servers. ExternalRadius type can also be used to enable Windows Accounting or Accounting on the NPS installed locally on the same machine, as described in the cmdlet description section

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

1. Status of inbox accounting (Enabled, Disabled) and store limit 2. Status of RADIUS accounting (Disable, Windows, ExternalRadius, LocalNps) and list of RADIUS servers if it is ExternalRadius

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

 

 





