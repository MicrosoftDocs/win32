---
description: Serves as a base class for classes that provide access to network settings, including MSFT\_NetCompartment and MSFT\_NetOffloadGlobalSetting.
ms.assetid: eef60c3e-4481-49f8-8dc7-73804e92f1b5
title: MSFT\_NetSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSettingData
- MSFT_NetSettingData.Caption
- MSFT_NetSettingData.Description
- MSFT_NetSettingData.InstanceID
- MSFT_NetSettingData.ElementName
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetSettingData class

Serves as a base class for classes that provide access to network settings, including [**MSFT\_NetCompartment**](msft-netcompartment.md) and [**MSFT\_NetOffloadGlobalSetting**](msft-netoffloadglobalsetting.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetSettingData : CIM_SettingData
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
};
```

## Members

The **MSFT\_NetSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetSettingData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (64)
</dt> </dl>

Contains a short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
</dt> </dl>

The user-friendly name for this instance. In addition, the user-friendly name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier)
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing Namespace.

> \[!Important\]In order to ensure uniqueness within the Namespace, the value of **InstanceID** should be constructed in the following pattern:
>
> *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity defining the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This is similar to the structure of Schema class names. In addition, to ensure uniqueness the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefor the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the preceding pattern is not used, the defining entity must assure that the resultant **InstanceID** is not re-used across any **InstanceID**s produced by this or other providers for this Namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SettingData**](./cim-settingdata.md)
</dt> <dt>

[NetTCPIP Provider Classes](net-tcpip-classes.md)
</dt> <dt>

[**MSFT\_NetCompartment**](msft-netcompartment.md)
</dt> <dt>

[**MSFT\_NetOffloadGlobalSetting**](msft-netoffloadglobalsetting.md)
</dt> </dl>

 

