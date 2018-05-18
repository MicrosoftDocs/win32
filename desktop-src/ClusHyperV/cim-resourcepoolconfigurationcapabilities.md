---
title: CIM\_ResourcePoolConfigurationCapabilities class
description: Manages the capabilities of the CIM\_ResourcePoolConfigurationService instance for a CIM\_ResourcePool object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6a88579c-f024-43f9-96ad-8050b61644c7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_ResourcePoolConfigurationCapabilities class", "CIM_ResourcePoolConfigurationCapabilities class, described"]
topic_type:
- apiref
api_name:
- CIM_ResourcePoolConfigurationCapabilities
- CIM_ResourcePoolConfigurationCapabilities.Caption
- CIM_ResourcePoolConfigurationCapabilities.Description
- CIM_ResourcePoolConfigurationCapabilities.InstanceID
- CIM_ResourcePoolConfigurationCapabilities.ElementName
- CIM_ResourcePoolConfigurationCapabilities.AsynchronousMethodsSupported
- CIM_ResourcePoolConfigurationCapabilities.SynchronousMethodsSupported
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_ResourcePoolConfigurationCapabilities class

Manages the capabilities of the [**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md) instance for a [**CIM\_ResourcePool**](cim-resourcepool.md) object. Not all implementations support all methods of [**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md). Clients can use instances of **CIM\_ResourcePoolConfigurationCapabilities** to determine which methods are supported. The same method must not supported for both synchronous and asynchronous operations. Implementations must either perform asynchronously and use a job for long running operations, or perform synchronously until the operation completes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Core::Resource")]
class CIM_ResourcePoolConfigurationCapabilities : CIM_Capabilities
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
  uint32 AsynchronousMethodsSupported[];
  uint32 SynchronousMethodsSupported[];
};
```

## Members

The **CIM\_ResourcePoolConfigurationCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ResourcePoolConfigurationCapabilities** class has these properties.

<dl> <dt>

**AsynchronousMethodsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The methods of the configuration service that are supported for asynchronous operations.

<dt>

<span id="CreateResourcePool_is_supported"></span><span id="createresourcepool_is_supported"></span><span id="CREATERESOURCEPOOL_IS_SUPPORTED"></span>

<span id="CreateResourcePool_is_supported"></span><span id="createresourcepool_is_supported"></span><span id="CREATERESOURCEPOOL_IS_SUPPORTED"></span>**CreateResourcePool is supported** (2)


</dt> <dd>

[**CreateResourcePool**](cim-resourcepoolconfigurationservice-createresourcepool.md)

</dd> <dt>

<span id="CreateChild_ResourcePool_is_supported"></span><span id="createchild_resourcepool_is_supported"></span><span id="CREATECHILD_RESOURCEPOOL_IS_SUPPORTED"></span>

<span id="CreateChild_ResourcePool_is_supported"></span><span id="createchild_resourcepool_is_supported"></span><span id="CREATECHILD_RESOURCEPOOL_IS_SUPPORTED"></span>**CreateChild ResourcePool is supported** (3)


</dt> <dd>

[**CreateChildResourcePool**](cim-resourcepoolconfigurationservice-createchildresourcepool.md)

</dd> <dt>

<span id="DeleteResourcePool_is_supported"></span><span id="deleteresourcepool_is_supported"></span><span id="DELETERESOURCEPOOL_IS_SUPPORTED"></span>

<span id="DeleteResourcePool_is_supported"></span><span id="deleteresourcepool_is_supported"></span><span id="DELETERESOURCEPOOL_IS_SUPPORTED"></span>**DeleteResourcePool is supported** (4)


</dt> <dd>

[**DeleteResourcePool**](cim-resourcepoolconfigurationservice-deleteresourcepool.md)

</dd> <dt>

<span id="AddResourcesToResourcePool_is_supported"></span><span id="addresourcestoresourcepool_is_supported"></span><span id="ADDRESOURCESTORESOURCEPOOL_IS_SUPPORTED"></span>

<span id="AddResourcesToResourcePool_is_supported"></span><span id="addresourcestoresourcepool_is_supported"></span><span id="ADDRESOURCESTORESOURCEPOOL_IS_SUPPORTED"></span>**AddResourcesToResourcePool is supported** (5)


</dt> <dd>

[**AddResourcesToResourcePool**](cim-resourcepoolconfigurationservice-addresourcestoresourcepool.md)

</dd> <dt>

<span id="RemoveResourcesFromResourcePool_is_supported"></span><span id="removeresourcesfromresourcepool_is_supported"></span><span id="REMOVERESOURCESFROMRESOURCEPOOL_IS_SUPPORTED"></span>

<span id="RemoveResourcesFromResourcePool_is_supported"></span><span id="removeresourcesfromresourcepool_is_supported"></span><span id="REMOVERESOURCESFROMRESOURCEPOOL_IS_SUPPORTED"></span>**RemoveResourcesFromResourcePool is supported** (6)


</dt> <dd>

[**RemoveResourcesFromResourcePool**](cim-resourcepoolconfigurationservice-removeresourcesfromresourcepool.md)

</dd> <dt>

<span id="ChangeParentResourcePool_is_supported"></span><span id="changeparentresourcepool_is_supported"></span><span id="CHANGEPARENTRESOURCEPOOL_IS_SUPPORTED"></span>

<span id="ChangeParentResourcePool_is_supported"></span><span id="changeparentresourcepool_is_supported"></span><span id="CHANGEPARENTRESOURCEPOOL_IS_SUPPORTED"></span>**ChangeParentResourcePool is supported** (7)


</dt> <dd>

[**ChangeParentResourcePool**](cim-resourcepoolconfigurationservice-changeparentresourcepool.md)

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Vendor Reserved 32768..65535

</dd> </dl>

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

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The methods of the configuration service that are supported for synchronous operations.

<dt>

<span id="CreateResourcePool_is_supported"></span><span id="createresourcepool_is_supported"></span><span id="CREATERESOURCEPOOL_IS_SUPPORTED"></span>

<span id="CreateResourcePool_is_supported"></span><span id="createresourcepool_is_supported"></span><span id="CREATERESOURCEPOOL_IS_SUPPORTED"></span>**CreateResourcePool is supported** (2)


</dt> <dd>

[**CreateResourcePool**](cim-resourcepoolconfigurationservice-createresourcepool.md)

</dd> <dt>

<span id="CreateChild_ResourcePool_is_supported"></span><span id="createchild_resourcepool_is_supported"></span><span id="CREATECHILD_RESOURCEPOOL_IS_SUPPORTED"></span>

<span id="CreateChild_ResourcePool_is_supported"></span><span id="createchild_resourcepool_is_supported"></span><span id="CREATECHILD_RESOURCEPOOL_IS_SUPPORTED"></span>**CreateChild ResourcePool is supported** (3)


</dt> <dd>

[**CreateChildResourcePool**](cim-resourcepoolconfigurationservice-createchildresourcepool.md)

</dd> <dt>

<span id="DeleteResourcePool_is_supported"></span><span id="deleteresourcepool_is_supported"></span><span id="DELETERESOURCEPOOL_IS_SUPPORTED"></span>

<span id="DeleteResourcePool_is_supported"></span><span id="deleteresourcepool_is_supported"></span><span id="DELETERESOURCEPOOL_IS_SUPPORTED"></span>**DeleteResourcePool is supported** (4)


</dt> <dd>

[**DeleteResourcePool**](cim-resourcepoolconfigurationservice-deleteresourcepool.md)

</dd> <dt>

<span id="AddResourcesToResourcePool_is_supported"></span><span id="addresourcestoresourcepool_is_supported"></span><span id="ADDRESOURCESTORESOURCEPOOL_IS_SUPPORTED"></span>

<span id="AddResourcesToResourcePool_is_supported"></span><span id="addresourcestoresourcepool_is_supported"></span><span id="ADDRESOURCESTORESOURCEPOOL_IS_SUPPORTED"></span>**AddResourcesToResourcePool is supported** (5)


</dt> <dd>

[**AddResourcesToResourcePool**](cim-resourcepoolconfigurationservice-addresourcestoresourcepool.md)

</dd> <dt>

<span id="RemoveResourcesFromResourcePool_is_supported"></span><span id="removeresourcesfromresourcepool_is_supported"></span><span id="REMOVERESOURCESFROMRESOURCEPOOL_IS_SUPPORTED"></span>

<span id="RemoveResourcesFromResourcePool_is_supported"></span><span id="removeresourcesfromresourcepool_is_supported"></span><span id="REMOVERESOURCESFROMRESOURCEPOOL_IS_SUPPORTED"></span>**RemoveResourcesFromResourcePool is supported** (6)


</dt> <dd>

[**RemoveResourcesFromResourcePool**](cim-resourcepoolconfigurationservice-removeresourcesfromresourcepool.md)

</dd> <dt>

<span id="CIM_ChangeParentResourcePool_is_supported"></span><span id="cim_changeparentresourcepool_is_supported"></span><span id="CIM_CHANGEPARENTRESOURCEPOOL_IS_SUPPORTED"></span>

<span id="CIM_ChangeParentResourcePool_is_supported"></span><span id="cim_changeparentresourcepool_is_supported"></span><span id="CIM_CHANGEPARENTRESOURCEPOOL_IS_SUPPORTED"></span>**CIM\_ChangeParentResourcePool is supported** (7)


</dt> <dd>

[**ChangeParentResourcePool**](cim-resourcepoolconfigurationservice-changeparentresourcepool.md)

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





