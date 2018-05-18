---
title: Msvm\_VirtualSystemResourceComponent class
description: Represents a virtual device service of the Microsoft Windows Hyper-V platform.
ms.assetid: '214f4645-8bb5-4b75-8e79-fece87bbd1bd'
keywords: ["Msvm_VirtualSystemResourceComponent class Hyper-V", "Msvm_VirtualSystemResourceComponent class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemResourceComponent
- Msvm_VirtualSystemResourceComponent.Name
- Msvm_VirtualSystemResourceComponent.CLSID
- Msvm_VirtualSystemResourceComponent.Context
- Msvm_VirtualSystemResourceComponent.Enabled
- Msvm_VirtualSystemResourceComponent.AdditionalClassNames
- Msvm_VirtualSystemResourceComponent.Type
- Msvm_VirtualSystemResourceComponent.HotAdd
- Msvm_VirtualSystemResourceComponent.HotRemove
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_VirtualSystemResourceComponent class

Represents a virtual device service of the Microsoft Windows Hyper-V platform.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_VirtualSystemResourceComponent : Msvm_VirtualizationComponent
{
  string  Name;
  string  CLSID;
  uint32  Context = 1;
  boolean Enabled = True;
  string  AdditionalClassNames[] = {};
  uint16  Type = 1;
  boolean HotAdd = FALSE;
  boolean HotRemove = FALSE;
};
```

## Members

The **Msvm\_VirtualSystemResourceComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemResourceComponent** class has these properties.

<dl> <dt>

**AdditionalClassNames**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

An array of strings containing additional non-association classes surfaced by this **Msvm\_VirtualSystemResourceComponent** instance. These classes must derive from neither [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) nor [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**CLSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A GUID that represents the class identifier of the service's COM object. This property is inherited from [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md).

</dd> <dt>

**Context**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The context in which the newly created object will run. This value is passed in the *dwClsContext* parameter to [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615). This property is inherited from [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md) and it is always set to 1.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If true, this instance is enabled and can be used to complete client requests. This property is inherited from [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md) and it is always set to **True**.

</dd> <dt>

**HotAdd**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this instance can be hot-added to a VM. The default is **FALSE**.

</dd> <dt>

**HotRemove**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this instance can be hot-removed from a VM. The default is **FALSE**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A language-neutral string that uniquely identifies the service. The following format is suggested to prevent naming conflicts: "vendor\|component\|version". For example, this name represents version 1.0 of the Microsoft Emulated Network Port Component: "Microsoft\|EmulatedNetworkPortComponent\|V1.0". This property is inherited from [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md).

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relationship of the WMI object that is described here with the virtual device.

<dt>

<span id="NotChangeable"></span><span id="notchangeable"></span><span id="NOTCHANGEABLE"></span>

<span id="NotChangeable"></span><span id="notchangeable"></span><span id="NOTCHANGEABLE"></span>**NotChangeable** (0)


</dt> <dd></dd> <dt>

<span id="Singleton"></span><span id="singleton"></span><span id="SINGLETON"></span>

<span id="Singleton"></span><span id="singleton"></span><span id="SINGLETON"></span>**Singleton** (1)


</dt> <dd>

Singleton is a top level WMI object that is tied 1:1 with a Virtual Device and can only exist once per VM. This is the default value.

</dd> <dt>

<span id="MultiInstance"></span><span id="multiinstance"></span><span id="MULTIINSTANCE"></span>

<span id="MultiInstance"></span><span id="multiinstance"></span><span id="MULTIINSTANCE"></span>**MultiInstance** (2)


</dt> <dd>

MultiInstance is a top level WMI object that can exist multiple times per VM and is tied 1:1 with a Virtual Device.

</dd> <dt>

<span id="Subdevice"></span><span id="subdevice"></span><span id="SUBDEVICE"></span>

<span id="Subdevice"></span><span id="subdevice"></span><span id="SUBDEVICE"></span>**Subdevice** (3)


</dt> <dd>

Subdevice is a WMI object that has not parent reference but is controlled by only one Virtual Device that can exist only once per VM. The WMI object though can exist multiples times.

</dd> </dl>

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemResourceComponent** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md)
</dt> <dt>

[Profile Registration Classes](profile-registration.md)
</dt> </dl>

 

 





