---
description: Represents a virtual device service of the Microsoft Windows Hyper-V platform.
ms.assetid: 865D83E1-0FC6-4F96-94BB-AA5116890127
title: Msvm_VirtualSystemResourceComponent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
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
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualSystemResourceComponent class

Represents a virtual device service of the Microsoft Windows Hyper-V platform.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
class Msvm_VirtualSystemResourceComponent : Msvm_VirtualizationComponent
{
  string  Name;
  string  CLSID;
  uint32  Context = 1;
  boolean Enabled = True;
  string  AdditionalClassNames[];
  uint16  Type = 1;
  boolean HotAdd = False;
  boolean HotRemove = False;
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
</dt> </dl>

An array of strings containing additional non-association classes surfaced by this **Msvm\_VirtualSystemResourceComponent** instance. These classes must derive from neither [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice) nor [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

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

The context in which the newly created object will run. This value is passed in the *dwClsContext* parameter to [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance). This property is inherited from [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md), and it is always set to 1.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if this instance is enabled and can be used to complete client requests; otherwise, **False**. This property is inherited from [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md), and it is always set to **True**.

</dd> <dt>

**HotAdd**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if this instance can be hot-added to a virtual machine; otherwise, **False**. The default is **False**.

</dd> <dt>

**HotRemove**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if this instance can be hot-removed from a virtual machine; otherwise, **False**. The default is **False**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
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



| Value                                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="_Not_Changeable_"></span><span id="_not_changeable_"></span><span id="_NOT_CHANGEABLE_"></span><dl> <dt>**"Not Changeable"**</dt> <dt>0</dt> </dl> |                                                                                                                                                                                                                |
| <span id="_Singleton_"></span><span id="_singleton_"></span><span id="_SINGLETON_"></span><dl> <dt>**"Singleton"**</dt> <dt>1</dt> </dl>                     | Singleton is a top level WMI object that is tied 1:1 with a Virtual Device and can only exist once per virtual machine. This is the default value.<br/>                                                  |
| <span id="_MultiInstance_"></span><span id="_multiinstance_"></span><span id="_MULTIINSTANCE_"></span><dl> <dt>**"MultiInstance"**</dt> <dt>2</dt> </dl>     | MultiInstance is a top level WMI object that can exist multiple times per virtual machine and is tied 1:1 with a Virtual Device.<br/>                                                                    |
| <span id="_Subdevice_"></span><span id="_subdevice_"></span><span id="_SUBDEVICE_"></span><dl> <dt>**"Subdevice"**</dt> <dt>3</dt> </dl>                     | Subdevice is a WMI object that has not parent reference but is controlled by only one Virtual Device that can exist only once per virtual machine. The WMI object though can exist multiples times.<br/> |



 

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemResourceComponent** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| End of client support<br/>    | Windows 8.1<br/>                                                                                  |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualizationComponent**](/windows/desktop/HyperV_v2/msvm-virtualizationcomponent)
</dt> <dt>

[**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md)
</dt> </dl>

 

