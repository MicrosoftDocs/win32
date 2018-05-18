---
title: InstallByMultiTenant method of the PS\_RemoteAccess class
description: Installs DirectAccess and multi-tenant site-to-site (S2S) VPN.
audience: developer
ms.assetid: 'cf22774b-47ce-42f5-9e09-4a691eab114c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["InstallByMultiTenant method", "InstallByMultiTenant method, PS_RemoteAccess class", "PS_RemoteAccess class, InstallByMultiTenant method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccess.InstallByMultiTenant
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# InstallByMultiTenant method of the PS\_RemoteAccess class

Installs DirectAccess and multi-tenant site-to-site (S2S) VPN.

## Syntax


```mof
uint32 InstallByMultiTenant(
  [in]  string             ComputerName,
  [in]  boolean            MultiTenancy,
  [in]  string             VpnType,
  [in]  string             MsgAuthenticator,
  [in]  boolean            PassThru,
  [in]  uint16             RadiusPort,
  [in]  uint8              RadiusScore,
  [in]  string             RadiusServer,
  [in]  uint32             RadiusTimeout,
  [in]  string             SharedSecret,
  [in]  uint64             CapacityKbps,
  [out] RemoteAccessCommon cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The IP address or hostname of the computer that is to run the Remote Access server tasks.

</dd> <dt>

*MultiTenancy* \[in\]
</dt> <dd>

Indicates whether to install the VPN as a multi-tenant service. **True** to install the the VPN as a multi-tenant service; otherwise **false**.

</dd> <dt>

*VpnType* \[in\]
</dt> <dd>

**Windows Server 2012 R2:** This parameter is not available before Windows Server 2016.

The type of VPN to configure.

</dd> <dt>

*MsgAuthenticator* \[in\]
</dt> <dd>

Indicates whether to enable the message authenticator for a Remote Authentication Dial In User Service (RADIUS) server. You can set this parameter to one of the following values. By default, this parameter is set to disabled.

<dt>

Enabled
</dt> <dd>

Enables the message authenticator.

</dd> <dt>

Disabled
</dt> <dd>

Disables the message authenticator.

</dd> </dl> </dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the *cmdletOutput* parameter returns an object. **True** to return an object; otherwise **false**. By default, *cmdletOutput* does not return an object.

</dd> <dt>

*RadiusPort* \[in\]
</dt> <dd>

The port number on which the RADIUS server accepts authentication requests. The default port is 1812.

</dd> <dt>

*RadiusScore* \[in\]
</dt> <dd>

Indicates the initial score of the RADIUS server. The default score is 30.

</dd> <dt>

*RadiusServer* \[in\]
</dt> <dd>

The IP address or hostname of the RADIUS server.

</dd> <dt>

*RadiusTimeout* \[in\]
</dt> <dd>

The timeout value for the RADIUS server, in seconds. The default value is 5.

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

The shared secret between the Remote Access server and the RADIUS server.

</dd> <dt>

*CapacityKbps* \[in\]
</dt> <dd>

The bandwidth capacity of the remote access configuration.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**RemoteAccessCommon**](remoteaccesscommon.md) object that receives the information for the installed Remote Access features.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccess**](ps-remoteaccess.md)
</dt> </dl>

 

 





