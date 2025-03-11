---
description: This class represents the advanced properties of a network adapter stored in the registry.
ms.assetid: 5d459abe-beb1-42e9-b1fc-9d1538d997ed
title: MSFT\_NetAdapterAdvancedPropertySettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterAdvancedPropertySettingData
- MSFT_NetAdapterAdvancedPropertySettingData.Reset
- MSFT_NetAdapterAdvancedPropertySettingData.Caption
- MSFT_NetAdapterAdvancedPropertySettingData.Description
- MSFT_NetAdapterAdvancedPropertySettingData.ElementName
- MSFT_NetAdapterAdvancedPropertySettingData.InstanceID
- MSFT_NetAdapterAdvancedPropertySettingData.Name
- MSFT_NetAdapterAdvancedPropertySettingData.InterfaceDescription
- MSFT_NetAdapterAdvancedPropertySettingData.Source
- MSFT_NetAdapterAdvancedPropertySettingData.SystemName
- MSFT_NetAdapterAdvancedPropertySettingData.DisplayName
- MSFT_NetAdapterAdvancedPropertySettingData.DisplayValue
- MSFT_NetAdapterAdvancedPropertySettingData.DefaultDisplayValue
- MSFT_NetAdapterAdvancedPropertySettingData.DisplayParameterType
- MSFT_NetAdapterAdvancedPropertySettingData.Optional
- MSFT_NetAdapterAdvancedPropertySettingData.ValidRegistryValues
- MSFT_NetAdapterAdvancedPropertySettingData.ValidDisplayValues
- MSFT_NetAdapterAdvancedPropertySettingData.NumericParameterBaseValue
- MSFT_NetAdapterAdvancedPropertySettingData.NumericParameterMinValue
- MSFT_NetAdapterAdvancedPropertySettingData.NumericParameterMaxValue
- MSFT_NetAdapterAdvancedPropertySettingData.NumericParameterStepValue
- MSFT_NetAdapterAdvancedPropertySettingData.RegistryKeyword
- MSFT_NetAdapterAdvancedPropertySettingData.RegistryDataType
- MSFT_NetAdapterAdvancedPropertySettingData.RegistryValue
- MSFT_NetAdapterAdvancedPropertySettingData.DefaultRegistryValue
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterAdvancedPropertySettingData class

This class represents the advanced properties of a network adapter stored in the registry.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterAdvancedPropertySettingData : MSFT_NetAdapterSettingData
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  string  Name;
  string  InterfaceDescription;
  uint32  Source;
  string  SystemName;
  string  DisplayName;
  string  DisplayValue;
  string  DefaultDisplayValue;
  uint32  DisplayParameterType;
  boolean Optional;
  string  ValidRegistryValues[];
  string  ValidDisplayValues[];
  string  NumericParameterBaseValue;
  string  NumericParameterMinValue;
  string  NumericParameterMaxValue;
  string  NumericParameterStepValue;
  string  RegistryKeyword;
  uint32  RegistryDataType;
  string  RegistryValue[];
  string  DefaultRegistryValue;
};
```

## Members

The **MSFT\_NetAdapterAdvancedPropertySettingData** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetAdapterAdvancedPropertySettingData** class has these methods.



| Method    | Description                                                                                |
|:----------|:-------------------------------------------------------------------------------------------|
| **Reset** | Resets the advanced property of a network adapter to its factory default value.<br/> |



 

### Properties

The **MSFT\_NetAdapterAdvancedPropertySettingData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 64 )
</dt> </dl>

A short textual description of the object. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**DefaultDisplayValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The description for the default value of the parameter. This property is only valid if the parameter is displayed in user interface.

</dd> <dt>

**DefaultRegistryValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default registry value for the parameter. This property is only valid if the parameter is displayed in user interface.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The property description in user interface. This property is only valid if the parameter is displayed in user interface.

</dd> <dt>

**DisplayParameterType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the type of the parameter. The "int", "long", "word", and "dword" types specify a numeric parameter; "edit" and "enum" types specify a text parameter. Note that the values for all the parameters that are displayed in the user interface, including numeric parameters, are stored in the registry as REG\_SZ (null-terminated string) data type. This property is only valid if the parameter is displayed in user interface.

<dl> <dt>

<span id="int"></span><span id="INT"></span>**int** (1)
</dt> <dt>

<span id="long"></span><span id="LONG"></span>**long** (2)
</dt> <dt>

<span id="word"></span><span id="WORD"></span>**word** (3)
</dt> <dt>

<span id="dword"></span><span id="DWORD"></span>**dword** (4)
</dt> <dt>

<span id="enum"></span><span id="ENUM"></span>**enum** (5)
</dt> <dt>

<span id="edit"></span><span id="EDIT"></span>**edit** (6)
</dt> </dl>

</dd> <dt>

**DisplayValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The description for the current value of the property. This property is only valid if the parameter is displayed in user interface.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property enables each instance to define a display name in addition to its key properties, identity data, and description information. Be aware that the Name property of ManagedSystemElement is also defined as a display name. However, it is often subclassed to be a Key. The same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: *OrgID*:*LocalID* Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the *SchemaName*\_*ClassName* structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above preferred algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. For DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to CIM.

This property inherits from [**CIM\_SettingData**](/previous-versions/windows/desktop/ipamserverpsprov/cim-settingdata).

</dd> <dt>

**InterfaceDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Interface Description, also known as "ifDesc" or display name is a unique name assigned to the network adapter during installation. This name cannot be changed and is persisted as long as the network adapter is not uninstalled. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name, also known as Connection Name, "ifAlias", or InterfaceAlias, is a unique name assigned to the adapter during installation. The Name of the adapter can be changed by the administrator and is persisted across the boot or network adapter restart. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**NumericParameterBaseValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The "Base" used in representing a numeric parameter. This property is only valid if the parameter is displayed in user interface.

</dd> <dt>

**NumericParameterMaxValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum value of a numeric parameter. This property is only valid if the parameter is displayed in user interface.

</dd> <dt>

**NumericParameterMinValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum value of a numeric parameter. This property is only valid if the parameter is displayed in user interface.

</dd> <dt>

**NumericParameterStepValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The "Step" value of a numeric parameter. This property is only valid if the parameter is displayed in user interface.

</dd> <dt>

**Optional**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If True, specifying this parameter is optional. Otherwise it is mandatory. This property is only valid if the parameter is displayed in user interface.

</dd> <dt>

**RegistryDataType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Registry keyword data type. For parameters displayed in user interface, this value is always REG\_SZ even if the parameter is a numeric parameter.

<dl> <dt>

<span id="REG_SZ"></span><span id="reg_sz"></span>**REG\_SZ** (1)
</dt> <dt>

<span id="REG_DWORD"></span><span id="reg_dword"></span>**REG\_DWORD** (4)
</dt> <dt>

<span id="REG_MULTI_SZ"></span><span id="reg_multi_sz"></span>**REG\_MULTI\_SZ** (7)
</dt> <dt>

<span id="REG_QWORD_"></span><span id="reg_qword_"></span>**REG\_QWORD** (11)
</dt> </dl>

</dd> <dt>

**RegistryKeyword**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Registry keyword name of the parameter. Registry keywords may be associated with a parameter displayed in user interface. Some registry keywords are not associated to any parameter displayed in user interface.

</dd> <dt>

**RegistryValue**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Current value of the registry keyword. For a parameter that is displayed in user interface and is of "enum" type, this is a value in EnumParameterRegistryValues array and not the description for the current value of the parameter.

</dd> <dt>

**Source**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The source of the setting data. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Device"></span><span id="device"></span><span id="DEVICE"></span>**Device** (2)
</dt> <dt>

<span id="Persistent_storage"></span><span id="persistent_storage"></span><span id="PERSISTENT_STORAGE"></span>**Persistent storage** (3)
</dt> </dl>

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The scoping System\\'s Name. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**ValidDisplayValues**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of strings representing the descriptions for the registry keyword values used in EnumParameterRegistryValues. This property is only valid if the parameter is displayed in user interface.

</dd> <dt>

**ValidRegistryValues**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of integers specifying the registry keyword values used to represent a parameter of the "enum" type. This property is only valid if the parameter is displayed in user interface.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

