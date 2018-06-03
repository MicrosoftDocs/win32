---
title: NetworkControllerClusterConfiguration class
description: Describes the configuration information for a network controller cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 44fd9c69-4875-4a6b-9bfb-0b9d3b902c6c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NetworkControllerClusterConfiguration class
- NetworkControllerClusterConfiguration class, described
topic_type:
- apiref
api_name:
- NetworkControllerClusterConfiguration
- NetworkControllerClusterConfiguration.Version
- NetworkControllerClusterConfiguration.ServiceFabricVersion
- NetworkControllerClusterConfiguration.NodeList
- NetworkControllerClusterConfiguration.ClusterAuthentication
- NetworkControllerClusterConfiguration.ClusterSpn
- NetworkControllerClusterConfiguration.ClusterGmsaAccountName
- NetworkControllerClusterConfiguration.ClusterAdminSecurityGroup
- NetworkControllerClusterConfiguration.IsNCDeployed
- NetworkControllerClusterConfiguration.DiagnosticInfo
- NetworkControllerClusterConfiguration.EncryptionCertificateRawData
- NetworkControllerClusterConfiguration.ImageStorePSK
- NetworkControllerClusterConfiguration.IsInitialClusterUpgrade
- NetworkControllerClusterConfiguration.EnableUpdates
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NetworkControllerClusterConfiguration class

Describes the configuration information for a network controller cluster.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("NcServerPSProvider"), AMENDMENT]
class NetworkControllerClusterConfiguration
{
  string                           Version;
  string                           ServiceFabricVersion;
  NetworkControllerNodeClusterInfo NodeList[];
  string                           ClusterAuthentication;
  string                           ClusterSpn;
  string                           ClusterGmsaAccountName;
  string                           ClusterAdminSecurityGroup;
  boolean                          IsNCDeployed;
  NetworkControllerDiagnosticInfo  DiagnosticInfo;
  uint8                            EncryptionCertificateRawData[];
  string                           ImageStorePSK;
  boolean                          IsInitialClusterUpgrade;
  boolean                          EnableUpdates;
};
```

## Members

The **NetworkControllerClusterConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **NetworkControllerClusterConfiguration** class has these properties.

<dl> <dt>

**ClusterAdminSecurityGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the security group in "fqdn\\SGName" format.

</dd> <dt>

**ClusterAuthentication**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the cluster authentication type.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="Windows"></span><span id="windows"></span><span id="WINDOWS"></span>

**Windows** ("Windows")


</dt> <dd></dd> <dt>

<span id="x509"></span><span id="X509"></span>

**x509** ("x509")


</dt> <dd></dd> </dl>

</dd> <dt>

**ClusterGmsaAccountName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the gMSA account in which context cluster will run in fqdn\\AccountName format.

</dd> <dt>

**ClusterSpn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Service Principal Name (SPN) under which cluster is running.

</dd> <dt>

**DiagnosticInfo**
</dt> <dd> <dl> <dt>

Data type: **NetworkControllerDiagnosticInfo**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**NetworkControllerDiagnosticInfo**](networkcontrollerdiagnosticinfo.md)")
</dt> </dl>

Gets a [**NetworkControllerDiagnosticInfo**](networkcontrollerdiagnosticinfo.md) object containing diagnostic information.

</dd> <dt>

**EnableUpdates**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Enable Network Controller update

</dd> <dt>

**EncryptionCertificateRawData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Octetstring**
</dt> </dl>

Contains the credential Encryption certificate.

</dd> <dt>

**ImageStorePSK**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Image Store PSK.

</dd> <dt>

**IsInitialClusterUpgrade**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Is Initial Cluster Upgrade.

</dd> <dt>

**IsNCDeployed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Returns **true** if a Network Controller application deployed on cluster; otherwise, **false**.

</dd> <dt>

**NodeList**
</dt> <dd> <dl> <dt>

Data type: **NetworkControllerNodeClusterInfo** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**NetworkControllerNodeClusterInfo**](networkcontrollernodeclusterinfo.md)")
</dt> </dl>

Gets a list of [**NetworkControllerNodeClusterInfo**](networkcontrollernodeclusterinfo.md) objects containing cluster nodes.

</dd> <dt>

**ServiceFabricVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the service fabric deployed.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the version of the cluster deployment.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 





