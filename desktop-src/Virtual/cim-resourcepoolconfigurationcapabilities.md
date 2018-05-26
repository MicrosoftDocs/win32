---
title: CIM\_ResourcePoolConfigurationCapabilities class
description: Manages the capabilities of the CIM\_ResourcePoolConfigurationService instance for a CIM\_ResourcePool object.
ms.assetid: 77e8d94f-671c-49b5-bd16-0957e1f992a3
keywords:
- CIM_ResourcePoolConfigurationCapabilities class Hyper-V
- CIM_ResourcePoolConfigurationCapabilities class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_ResourcePoolConfigurationCapabilities
- CIM_ResourcePoolConfigurationCapabilities.Caption
- CIM_ResourcePoolConfigurationCapabilities.Description
- CIM_ResourcePoolConfigurationCapabilities.InstanceID
- CIM_ResourcePoolConfigurationCapabilities.ElementName
- CIM_ResourcePoolConfigurationCapabilities.SupportedSyncMethods
- CIM_ResourcePoolConfigurationCapabilities.SupportedAsyncMethods
api_location:
- Root\virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_ResourcePoolConfigurationCapabilities class

Manages the capabilities of the [**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md) instance for a [**CIM\_ResourcePool**](cim-resourcepool.md) object. Not all implementations support all methods of [**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md). Clients can use instances of **CIM\_ResourcePoolConfigurationCapabilities** to determine which methods are supported. The same method must not supported for both synchronous and asynchronous operations. Implementations must either perform asynchronously and use a job for long running operations, or perform synchronously until the operation completes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Experimental, Version("2.13.0"), AMENDMENT]
class CIM_ResourcePoolConfigurationCapabilities : CIM_Capabilities
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
  uint32 SupportedSyncMethods[];
  uint32 SupportedAsyncMethods[];
};
```

## Members

The **CIM\_ResourcePoolConfigurationCapabilities** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_ResourcePoolConfigurationCapabilities** class has these methods.



| Method                                                                                     | Description                                                                                                                                                                                                        |
|:-------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateGoalSettings**](cim-resourcepoolconfigurationcapabilities-creategoalsettings.md) | Creates a set of supported SettingData elements, from two sets of SettingData elements, provided by the caller.<br/> This method is inherited from [**CIM\_Capabilities**](cim-capabilities.md).<br/> |



 

### Properties

The **CIM\_ResourcePoolConfigurationCapabilities** class has these properties.

<dl> <dt>

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

**SupportedAsyncMethods**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The supported async methods.

<dt>

<span id="CreateResourcePool_is_supported"></span><span id="createresourcepool_is_supported"></span><span id="CREATERESOURCEPOOL_IS_SUPPORTED"></span>

**CreateResourcePool is supported** (2)


</dt> <dd></dd> <dt>

<span id="CreateSubResourcePool_is_supported"></span><span id="createsubresourcepool_is_supported"></span><span id="CREATESUBRESOURCEPOOL_IS_SUPPORTED"></span>

**CreateSubResourcePool is supported** (3)


</dt> <dd></dd> <dt>

<span id="DeleteResourcePool_is_supported"></span><span id="deleteresourcepool_is_supported"></span><span id="DELETERESOURCEPOOL_IS_SUPPORTED"></span>

**DeleteResourcePool is supported** (4)


</dt> <dd></dd> <dt>

<span id="AddResourcesToResourcePool_is_supported"></span><span id="addresourcestoresourcepool_is_supported"></span><span id="ADDRESOURCESTORESOURCEPOOL_IS_SUPPORTED"></span>

**AddResourcesToResourcePool is supported** (5)


</dt> <dd></dd> <dt>

<span id="RemoveResourcesFromResourcePool_is_supported"></span><span id="removeresourcesfromresourcepool_is_supported"></span><span id="REMOVERESOURCESFROMRESOURCEPOOL_IS_SUPPORTED"></span>

**RemoveResourcesFromResourcePool is supported** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..65535)


</dt> <dd></dd> </dl>

</dd> <dt>

**SupportedSyncMethods**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The supported sync methods.

<dt>

<span id="CreateResourcePool_is_supported"></span><span id="createresourcepool_is_supported"></span><span id="CREATERESOURCEPOOL_IS_SUPPORTED"></span>

**CreateResourcePool is supported** (2)


</dt> <dd></dd> <dt>

<span id="CreateSubResourcePool_is_supported"></span><span id="createsubresourcepool_is_supported"></span><span id="CREATESUBRESOURCEPOOL_IS_SUPPORTED"></span>

**CreateSubResourcePool is supported** (3)


</dt> <dd></dd> <dt>

<span id="DeleteResourcePool_is_supported"></span><span id="deleteresourcepool_is_supported"></span><span id="DELETERESOURCEPOOL_IS_SUPPORTED"></span>

**DeleteResourcePool is supported** (4)


</dt> <dd></dd> <dt>

<span id="AddResourcesToResourcePool_is_supported"></span><span id="addresourcestoresourcepool_is_supported"></span><span id="ADDRESOURCESTORESOURCEPOOL_IS_SUPPORTED"></span>

**AddResourcesToResourcePool is supported** (5)


</dt> <dd></dd> <dt>

<span id="RemoveResourcesFromResourcePool_is_supported"></span><span id="removeresourcesfromresourcepool_is_supported"></span><span id="REMOVERESOURCESFROMRESOURCEPOOL_IS_SUPPORTED"></span>

**RemoveResourcesFromResourcePool is supported** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..65535)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> </dl>

 

 





