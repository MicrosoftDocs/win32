---
title: Enable method of the PS\_DAMultiSite class
description: Enables and configures a multisite deployment, and adds the first entry point. A prerequisite check is performed for multi-site deployment requirements.
audience: developer
ms.assetid: 50784b4d-bbae-4e25-8e6c-43cef544dfec
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Enable method
- Enable method, PS_DAMultiSite class
- PS_DAMultiSite class, Enable method
topic_type:
- apiref
api_name:
- PS_DAMultiSite.Enable
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enable method of the PS\_DAMultiSite class

Enables and configures a multisite deployment, and adds the first entry point. A prerequisite check is performed for multi-site deployment requirements.

## Syntax


```mof
uint32 Enable(
  [in]  string      ComputerName,
  [in]  string      EntryPointName,
  [in]  string      GslbFqdn,
  [in]  string      ManualEntryPointSelectionAllowed,
  [in]  string      Name,
  [in]  string      GslbIP,
  [in]  boolean     Force,
  [in]  boolean     PassThru,
  [out] DAMultiSite cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Name or IP address of a remote access server that will be included in the multisite deployment. If no value is specified the name of the local remote access server on which the cmdlet runs is used.

</dd> <dt>

*EntryPointName* \[in\]
</dt> <dd>

The name of the first entry point in the multisite deployment. Current DirectAccess servers will be used for the first entrypoint.

</dd> <dt>

*GslbFqdn* \[in\]
</dt> <dd>

FQDN of a global server load balancer

</dd> <dt>

*ManualEntryPointSelectionAllowed* \[in\]
</dt> <dd>

Specifies whether clients running operating systems later than Windows 7 can manually select the entry point to which they connect. Can be set as Enabled or Disabled. By default this feature is enabled.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl> </dd> <dt>

*Name* \[in\]
</dt> <dd>

The friendly name used to identify the multisite deployment.

</dd> <dt>

*GslbIP* \[in\]
</dt> <dd>

The IPv4 or IPv6 address of the entry point server, or the VIP of entry point server cluster, to be used for global load balancing.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Suppresses the option to allow a user to override a setting. (ShouldContinue prompts).

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifying PassThru returns the [**PS\_DAMultiSite**](ps-damultisite.md) object which contains the entire multisite configuration. This cmdlet doesn't generate an object by default.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Multisite deployment name. 2. Multisite deployment entrypoints, each of the entrypoint has the list of servers associated with it. 3. Global load balancing FQDN (if defined). 4. Whether remote access clients can manually select an entry point.

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

[**PS\_DAMultiSite**](ps-damultisite.md)
</dt> </dl>

 

 





