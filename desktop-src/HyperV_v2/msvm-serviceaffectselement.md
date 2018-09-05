---
Description: Associates a virtual machine instance with the management service that controls its state.
ms.assetid: 12EB3951-74D4-477F-8B55-69FAA3B14631
title: Msvm_ServiceAffectsElement class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ServiceAffectsElement
- Msvm_ServiceAffectsElement.AffectedElement
- Msvm_ServiceAffectsElement.AffectingElement
- Msvm_ServiceAffectsElement.ElementEffects
- Msvm_ServiceAffectsElement.OtherElementEffectsDescriptions
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ServiceAffectsElement class

Associates a virtual machine instance with the management service that controls its state.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ServiceAffectsElement : CIM_ServiceAffectsElement
{
  CIM_ManagedElement REF AffectedElement;
  CIM_Service        REF AffectingElement;
  uint16                 ElementEffects[] = 5;
  string                 OtherElementEffectsDescriptions[];
};
```

## Members

The **Msvm\_ServiceAffectsElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ServiceAffectsElement** class has these properties.

<dl> <dt>

**AffectedElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the virtual machine. This property is inherited from [**CIM\_ServiceAffectsElement**](https://msdn.microsoft.com/library/cc136907).

</dd> <dt>

**AffectingElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Service**](https://msdn.microsoft.com/library/aa388442)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the service that controls the virtual machine. This property is inherited from [**CIM\_ServiceAffectsElement**](https://msdn.microsoft.com/library/cc136907).

</dd> <dt>

**ElementEffects**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the type of control that the association represents. This property is inherited from [**CIM\_ServiceAffectsElement**](https://msdn.microsoft.com/library/cc136907), and it is always set to the following value.



| Value                                                                        | Meaning            |
|------------------------------------------------------------------------------|--------------------|
| <dl> <dt>5</dt> </dl> | Manages<br/> |



 

</dd> <dt>

**OtherElementEffectsDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The details for the type of association at the corresponding array position in the **ElementAffects** property array. This information is required if **ElementAffects** is set to 1 (Other). This property is inherited from [**CIM\_ServiceAffectsElement**](https://msdn.microsoft.com/library/cc136907), and it is always set to **Null**.

</dd> </dl>

## Remarks

Access to the **Msvm\_ServiceAffectsElement** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md)
</dt> <dt>

[**CIM\_ServiceAffectsElement**](https://msdn.microsoft.com/library/cc136907)
</dt> </dl>

 

 




