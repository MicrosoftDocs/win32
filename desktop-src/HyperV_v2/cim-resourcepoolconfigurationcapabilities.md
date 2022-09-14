---
description: Manages the capabilities of the CIM\_ResourcePoolConfigurationService instance for a CIM\_ResourcePool object.
ms.assetid: bd2eb4da-8ecd-4adb-b657-837c8da4dcdc
title: CIM_ResourcePoolConfigurationCapabilities class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ResourcePoolConfigurationCapabilities
- CIM_ResourcePoolConfigurationCapabilities.AsynchronousMethodsSupported
- CIM_ResourcePoolConfigurationCapabilities.SynchronousMethodsSupported
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_ResourcePoolConfigurationCapabilities class

Manages the capabilities of the [**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md) instance for a [**CIM\_ResourcePool**](cim-resourcepool.md) object.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Core::Resource")]
class CIM_ResourcePoolConfigurationCapabilities : CIM_Capabilities
{
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

**CreateResourcePool is supported** (2)


</dt> <dd></dd> <dt>

<span id="CreateChild_ResourcePool_is_supported"></span><span id="createchild_resourcepool_is_supported"></span><span id="CREATECHILD_RESOURCEPOOL_IS_SUPPORTED"></span>

**CreateChild ResourcePool is supported** (3)


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

<span id="ChangeParentResourcePool_is_supported"></span><span id="changeparentresourcepool_is_supported"></span><span id="CHANGEPARENTRESOURCEPOOL_IS_SUPPORTED"></span>

**ChangeParentResourcePool is supported** (7)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..65535)


</dt> <dd></dd> </dl>

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

**CreateResourcePool is supported** (2)


</dt> <dd></dd> <dt>

<span id="CreateChild_ResourcePool_is_supported"></span><span id="createchild_resourcepool_is_supported"></span><span id="CREATECHILD_RESOURCEPOOL_IS_SUPPORTED"></span>

**CreateChild ResourcePool is supported** (3)


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

<span id="CIM_ChangeParentResourcePool_is_supported"></span><span id="cim_changeparentresourcepool_is_supported"></span><span id="CIM_CHANGEPARENTRESOURCEPOOL_IS_SUPPORTED"></span>

**CIM\_ChangeParentResourcePool is supported** (7)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..65535)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> </dl>

 

 




