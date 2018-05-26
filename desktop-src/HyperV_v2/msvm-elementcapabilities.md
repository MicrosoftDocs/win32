---
Description: Represents the association between managed elements and their capabilities.
ms.assetid: F083E6D2-CC74-4DAD-8FF7-3FE3CA4EEFFF
title: Msvm\_ElementCapabilities class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_ElementCapabilities class

Represents the association between managed elements and their capabilities.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ElementCapabilities : CIM_ElementCapabilities
{
  CIM_ManagedElement REF ManagedElement;
  CIM_Capabilities   REF Capabilities;
  uint16                 Characteristics[];
};
```

## Members

The **Msvm\_ElementCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ElementCapabilities** class has these properties.

<dl> <dt>

**Capabilities**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Capabilities**](https://msdn.microsoft.com/library/cc136806)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The capabilities object associated with the element. This property is inherited from [**CIM\_ElementCapabilities**](https://msdn.microsoft.com/library/mt446044).

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides descriptive information about the capabilities. This property is inherited from [**CIM\_ElementCapabilities**](https://msdn.microsoft.com/library/mt446044).



| Value                                                                                                                                                                                                                       | Meaning                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="Default"></span><span id="default"></span><span id="DEFAULT"></span><dl> <dt>**Default**</dt> <dt>2</dt> </dl> | The associated capabilities represent the default capabilities of the managed element.<br/> |
| <span id="Current"></span><span id="current"></span><span id="CURRENT"></span><dl> <dt>**Current**</dt> <dt>3</dt> </dl> | The associated capabilities represent the current capabilities of the managed element.<br/> |



 

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Min** ( 1 )
</dt> </dl>

The managed element. This property is inherited from [**CIM\_ElementCapabilities**](https://msdn.microsoft.com/library/mt446044).

</dd> </dl>

## Remarks

Access to the **Msvm\_ElementCapabilities** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ElementCapabilities**](cim-elementcapabilities.md)
</dt> <dt>

[**CIM\_ElementCapabilities**](https://msdn.microsoft.com/library/mt446044)
</dt> <dt>

[**Msvm\_ElementCapabilities (V1)**](https://msdn.microsoft.com/library/cc136833)
</dt> </dl>

 

 




