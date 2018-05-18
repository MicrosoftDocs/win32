---
title: MDM\_Policy\_Config01\_AppVirtualization02 class
description: The MDM\_Policy\_Config01\_AppVirtualization02 class configures the available app virtualization policies.
ms.assetid: 'd270704c-8652-4f97-89f7-fcb6e68ee6fe'
keywords: ["MDM_Policy_Config01_AppVirtualization02 class", "MDM_Policy_Config01_AppVirtualization02 class, described"]
topic_type:
- apiref
api_name:
- MDM_Policy_Config01_AppVirtualization02
- MDM_Policy_Config01_AppVirtualization02.InstanceID
- MDM_Policy_Config01_AppVirtualization02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
---

# MDM\_Policy\_Config01\_AppVirtualization02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The MDM\_Policy\_Config01\_AppVirtualization02 class configures the available app virtualization policies.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_Policy_Config01_AppVirtualization02
{
  string InstanceID;
  string ParentID;
  string AllowAppVClient;
  string AllowDynamicVirtualization;
  string AllowPackageCleanup;
  string AllowPackageScripts;
  string AllowPublishingRefreshUX;
  string AllowReportingServer;
  string AllowRoamingFileExclusions;
  string AllowRoamingRegistryExclusions;
  string AllowStreamingAutoload;
  string ClientCoexistenceAllowMigrationmode;
  string IntegrationAllowRootGlobal;
  string IntegrationAllowRootUser;
  string PublishingAllowServer1;
  string PublishingAllowServer2;
  string PublishingAllowServer3;
  string PublishingAllowServer4;
  string PublishingAllowServer5;
  string StreamingAllowCertificateFilterForClient_SSL;
  string StreamingAllowHighCostLaunch;
  string StreamingAllowLocationProvider;
  string StreamingAllowPackageInstallationRoot;
  string StreamingAllowPackageSourceRoot;
  string StreamingAllowReestablishmentInterval;
  string StreamingAllowReestablishmentRetries;
  string StreamingSharedContentStoreMode;
  string StreamingSupportBranchCache;
  string StreamingVerifyCertificateRevocationList;
  string VirtualComponentsAllowList;
};
```

## Members

The **MDM\_Policy\_Config01\_AppVirtualization02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Policy\_Config01\_AppVirtualization02** class has these properties.

<dl> <dt>

[AllowAppVClient](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-allowappvclient)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowDynamicVirtualization](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-allowdynamicvirtualization)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPackageCleanup](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-allowpackagecleanup)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPackageScripts](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-allowpackagescripts)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowPublishingRefreshUX](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-allowpublishingrefreshux)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowReportingServer](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-allowreportingserver)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowRoamingFileExclusions](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-allowroamingfileexclusions)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowRoamingRegistryExclusions](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-allowroamingregistryexclusions)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowStreamingAutoload](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-allowstreamingautoload)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[ClientCoexistenceAllowMigrationmode](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-clientcoexistenceallowmigrationmode)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

</dd> <dt>

[IntegrationAllowRootGlobal](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-integrationallowrootglobal)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[IntegrationAllowRootUser](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-integrationallowrootuser)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

</dd> <dt>

[PublishingAllowServer1](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-publishingallowserver1)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[PublishingAllowServer2](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-publishingallowserver2)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[PublishingAllowServer3](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-publishingallowserver3)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[PublishingAllowServer4](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-publishingallowserver4)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[PublishingAllowServer5](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-publishingallowserver5)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StreamingAllowCertificateFilterForClient\_SSL](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-streamingallowcertificatefilterforclient-ssl)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StreamingAllowHighCostLaunch](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-streamingallowhighcostlaunch)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StreamingAllowLocationProvider](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-streamingallowlocationprovider)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StreamingAllowPackageInstallationRoot](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-streamingallowpackageinstallationroot)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StreamingAllowPackageSourceRoot](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-streamingallowpackagesourceroot)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StreamingAllowReestablishmentInterval](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-streamingallowreestablishmentinterval)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StreamingAllowReestablishmentRetries](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-streamingallowreestablishmentretries)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StreamingSharedContentStoreMode](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-streamingsharedcontentstoremode)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StreamingSupportBranchCache](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-streamingsupportbranchcache)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[StreamingVerifyCertificateRevocationList](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-streamingverifycertificaterevocationlist)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[VirtualComponentsAllowList](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-appvirtualization#appvirtualization-virtualcomponentsallowlist)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



 

 





