---
title: Import method of the Win32_TSGatewayServer class
description: Imports a given configuration to the Remote Desktop Gateway (RD Gateway) server.
ms.assetid: d849afb9-f6cb-41e6-aab5-e47b30a5581f
ms.tgt_platform: multiple
keywords:
- Import method Remote Desktop Services
- Import method Remote Desktop Services , Win32_TSGatewayServer class
- Win32_TSGatewayServer class Remote Desktop Services , Import method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServer.Import
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Import method of the Win32\_TSGatewayServer class

Imports a given configuration to the Remote Desktop Gateway (RD Gateway) server.

## Syntax


```mof
uint32 Import(
  [in]  uint32 ImportType,
  [in]  string XmlString,
  [in]  uint32 MergeOrReplace,
  [out] string LogString
);
```



## Parameters

<dl> <dt>

*ImportType* \[in\]
</dt> <dd>

The content to import. Set the import type by setting the corresponding bits in the *ImportType* parameter. You can set multiple import types. For example, if the 0 bit is set, Remote Desktop Services connection authorization policies (RD CAPs) will be imported. If both the 0 and the 2nd bit is set, both RD CAPs and Remote Desktop Services resource authorization policies (RD RAPs) will be imported.

<dt>

<span id="Import_all_CAPs"></span><span id="import_all_caps"></span><span id="IMPORT_ALL_CAPS"></span>

<span id="Import_all_CAPs"></span><span id="import_all_caps"></span><span id="IMPORT_ALL_CAPS"></span>**Import all CAPs** (1)


</dt> <dd>

Import all RD CAPs.

</dd> <dt>

<span id="Import_all_Radius_Servers"></span><span id="import_all_radius_servers"></span><span id="IMPORT_ALL_RADIUS_SERVERS"></span>

<span id="Import_all_Radius_Servers"></span><span id="import_all_radius_servers"></span><span id="IMPORT_ALL_RADIUS_SERVERS"></span>**Import all Radius Servers** (2)


</dt> <dd>

Import a list of all Network Policy Server (NPS) servers.

</dd> <dt>

<span id="Import_all_RAPs"></span><span id="import_all_raps"></span><span id="IMPORT_ALL_RAPS"></span>

<span id="Import_all_RAPs"></span><span id="import_all_raps"></span><span id="IMPORT_ALL_RAPS"></span>**Import all RAPs** (4)


</dt> <dd>

Import all RD RAPs.

</dd> <dt>

<span id="Import_all_RGs"></span><span id="import_all_rgs"></span><span id="IMPORT_ALL_RGS"></span>

<span id="Import_all_RGs"></span><span id="import_all_rgs"></span><span id="IMPORT_ALL_RGS"></span>**Import all RGs** (8)


</dt> <dd>

Import all resource groups.

</dd> <dt>

<span id="Import_all_LoadBalancing_Servers"></span><span id="import_all_loadbalancing_servers"></span><span id="IMPORT_ALL_LOADBALANCING_SERVERS"></span>

<span id="Import_all_LoadBalancing_Servers"></span><span id="import_all_loadbalancing_servers"></span><span id="IMPORT_ALL_LOADBALANCING_SERVERS"></span>**Import all LoadBalancing Servers** (16)


</dt> <dd>

Import a list of all load-balancing servers.

</dd> <dt>

<span id="Import_all_Server_Settings"></span><span id="import_all_server_settings"></span><span id="IMPORT_ALL_SERVER_SETTINGS"></span>

<span id="Import_all_Server_Settings"></span><span id="import_all_server_settings"></span><span id="IMPORT_ALL_SERVER_SETTINGS"></span>**Import all Server Settings** (32)


</dt> <dd>

Import all RD Gateway-related server settings.

</dd> <dt>

<span id="Import_all_Health_Policies"></span><span id="import_all_health_policies"></span><span id="IMPORT_ALL_HEALTH_POLICIES"></span>

<span id="Import_all_Health_Policies"></span><span id="import_all_health_policies"></span><span id="IMPORT_ALL_HEALTH_POLICIES"></span>**Import all Health Policies** (64)


</dt> <dd>

Import all health policies.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is not supported before Windows Server 2016.

</dd> </dl> </dd> <dt>

*XmlString* \[in\]
</dt> <dd>

The configuration as an XML string.

</dd> <dt>

*MergeOrReplace* \[in\]
</dt> <dd>

Indicates whether to merge or replace data when a conflict occurs.

> [!Note]  
> Merge is not yet implemented. Therefore, this parameter value is ignored.

 

</dd> <dt>

*LogString* \[out\]
</dt> <dd>

The log information that is generated during the import operation.

</dd> </dl>

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayServer**](win32-tsgatewayserver.md)
</dt> </dl>

 

