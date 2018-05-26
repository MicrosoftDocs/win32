---
title: CIM\_VirtualSystemMigrationCapabilities class
description: Represents the capabilities of a CIM\_VirtualSystemMigrationService object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 96bcb8b9-3716-4cc7-9eb1-54dd13d235fa
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_VirtualSystemMigrationCapabilities class
- CIM_VirtualSystemMigrationCapabilities class, described
topic_type:
- apiref
api_name:
- CIM_VirtualSystemMigrationCapabilities
- CIM_VirtualSystemMigrationCapabilities.Caption
- CIM_VirtualSystemMigrationCapabilities.Description
- CIM_VirtualSystemMigrationCapabilities.InstanceID
- CIM_VirtualSystemMigrationCapabilities.ElementName
- CIM_VirtualSystemMigrationCapabilities.SynchronousMethodsSupported
- CIM_VirtualSystemMigrationCapabilities.AsynchronousMethodsSupported
- CIM_VirtualSystemMigrationCapabilities.DestinationHostFormatsSupported
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_VirtualSystemMigrationCapabilities class

Represents the capabilities of a [**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md) object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Experimental, Abstract, Version("2.17.0"), UMLPackagePath("CIM::System::Virtualization")]
class CIM_VirtualSystemMigrationCapabilities : CIM_Capabilities
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
  uint16 SynchronousMethodsSupported[];
  uint16 AsynchronousMethodsSupported[];
  uint16 DestinationHostFormatsSupported[];
};
```

## Members

The **CIM\_VirtualSystemMigrationCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_VirtualSystemMigrationCapabilities** class has these properties.

<dl> <dt>

**AsynchronousMethodsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that indicates the [**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md) methods that are supported for asynchronous operations.

<dt>

<span id="MigrateVirtualSystemToHostSupported"></span><span id="migratevirtualsystemtohostsupported"></span><span id="MIGRATEVIRTUALSYSTEMTOHOSTSUPPORTED"></span>

<span id="MigrateVirtualSystemToHostSupported"></span><span id="migratevirtualsystemtohostsupported"></span><span id="MIGRATEVIRTUALSYSTEMTOHOSTSUPPORTED"></span>**MigrateVirtualSystemToHostSupported** (2)


</dt> <dd>

[**MigrateVirtualSystemToHost**](cim-virtualsystemmigrationservice-migratevirtualsystemtohost.md) is supported.

</dd> <dt>

<span id="MigrateVirtualSystemToSystemSupported"></span><span id="migratevirtualsystemtosystemsupported"></span><span id="MIGRATEVIRTUALSYSTEMTOSYSTEMSUPPORTED"></span>

<span id="MigrateVirtualSystemToSystemSupported"></span><span id="migratevirtualsystemtosystemsupported"></span><span id="MIGRATEVIRTUALSYSTEMTOSYSTEMSUPPORTED"></span>**MigrateVirtualSystemToSystemSupported** (3)


</dt> <dd>

[**MigrateVirtualSystemToSystem**](cim-virtualsystemmigrationservice-migratevirtualsystemtosystem.md) is supported.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DestinationHostFormatsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md).**MigrateVirtualSystemToHost(DestinationHost)**", "**CIM\_VirtualSystemMigrationService**.**CheckVirtualSystemIsMigratableToHost(DestinationHost)**")
</dt> </dl>

An array that contains the supported formats for the *DestinationHost* parameter of the [**MigrateVirtualSystemToHost**](cim-virtualsystemmigrationservice-migratevirtualsystemtohost.md) and [**CheckVirtualSystemIsMigratableToHost**](cim-virtualsystemmigrationservice-checkvirtualsystemismigratabletohost.md) methods for the [**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md) object.

<dt>

<span id="DomainNameFormatSupported"></span><span id="domainnameformatsupported"></span><span id="DOMAINNAMEFORMATSUPPORTED"></span>

<span id="DomainNameFormatSupported"></span><span id="domainnameformatsupported"></span><span id="DOMAINNAMEFORMATSUPPORTED"></span>**DomainNameFormatSupported** (2)


</dt> <dd>

*RFC 1035n3*   domain name text format.

</dd> <dt>

<span id="IPv4DottedDecimalFormatSupported"></span><span id="ipv4dotteddecimalformatsupported"></span><span id="IPV4DOTTEDDECIMALFORMATSUPPORTED"></span>

<span id="IPv4DottedDecimalFormatSupported"></span><span id="ipv4dotteddecimalformatsupported"></span><span id="IPV4DOTTEDDECIMALFORMATSUPPORTED"></span>**IPv4DottedDecimalFormatSupported** (3)


</dt> <dd>

*RFC 1208n4*   IPv4 dotted decimal format.

</dd> <dt>

<span id="IPv6TextFormatSupported"></span><span id="ipv6textformatsupported"></span><span id="IPV6TEXTFORMATSUPPORTED"></span>

<span id="IPv6TextFormatSupported"></span><span id="ipv6textformatsupported"></span><span id="IPV6TEXTFORMATSUPPORTED"></span>**IPv6TextFormatSupported** (4)


</dt> <dd>

*RFC 4291*   IPv6 text format.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> </dl>

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user friendly name for this class instance. In addition, the user friendly name can be used as a index property for a query. This value does not have to be unique within its namespace.

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This pattern is similar to the structure of schema class names. In addition, to ensure uniqueness, the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**SynchronousMethodsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that indicates the [**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md) methods that are supported for synchronous operations.

Enumeration of method identifiers whose implementation may be synchronous; that is, the operation may complete immediately and therefore the method may not return a job.

<dt>

<span id="MigrateVirtualSystemToHostSupported"></span><span id="migratevirtualsystemtohostsupported"></span><span id="MIGRATEVIRTUALSYSTEMTOHOSTSUPPORTED"></span>

<span id="MigrateVirtualSystemToHostSupported"></span><span id="migratevirtualsystemtohostsupported"></span><span id="MIGRATEVIRTUALSYSTEMTOHOSTSUPPORTED"></span>**MigrateVirtualSystemToHostSupported** (2)


</dt> <dd>

[**MigrateVirtualSystemToHost**](cim-virtualsystemmigrationservice-migratevirtualsystemtohost.md) is supported.

</dd> <dt>

<span id="MigrateVirtualSystemToSystemSupported"></span><span id="migratevirtualsystemtosystemsupported"></span><span id="MIGRATEVIRTUALSYSTEMTOSYSTEMSUPPORTED"></span>

<span id="MigrateVirtualSystemToSystemSupported"></span><span id="migratevirtualsystemtosystemsupported"></span><span id="MIGRATEVIRTUALSYSTEMTOSYSTEMSUPPORTED"></span>**MigrateVirtualSystemToSystemSupported** (3)


</dt> <dd>

[**MigrateVirtualSystemToSystem**](cim-virtualsystemmigrationservice-migratevirtualsystemtosystem.md) is supported.

</dd> <dt>

<span id="CheckVirtualSystemIsMigratableToHostSupported"></span><span id="checkvirtualsystemismigratabletohostsupported"></span><span id="CHECKVIRTUALSYSTEMISMIGRATABLETOHOSTSUPPORTED"></span>

<span id="CheckVirtualSystemIsMigratableToHostSupported"></span><span id="checkvirtualsystemismigratabletohostsupported"></span><span id="CHECKVIRTUALSYSTEMISMIGRATABLETOHOSTSUPPORTED"></span>**CheckVirtualSystemIsMigratableToHostSupported** (4)


</dt> <dd>

[**CheckVirtualSystemIsMigratableToHost**](cim-virtualsystemmigrationservice-checkvirtualsystemismigratabletohost.md) is supported.

</dd> <dt>

<span id="CheckVirtualSystemIsMigratableToSystemSupported"></span><span id="checkvirtualsystemismigratabletosystemsupported"></span><span id="CHECKVIRTUALSYSTEMISMIGRATABLETOSYSTEMSUPPORTED"></span>

<span id="CheckVirtualSystemIsMigratableToSystemSupported"></span><span id="checkvirtualsystemismigratabletosystemsupported"></span><span id="CHECKVIRTUALSYSTEMISMIGRATABLETOSYSTEMSUPPORTED"></span>**CheckVirtualSystemIsMigratableToSystemSupported** (5)


</dt> <dd>

[**CheckVirtualSystemIsMigratableToSystem**](cim-virtualsystemmigrationservice-checkvirtualsystemismigratabletosystem.md) is supported.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





