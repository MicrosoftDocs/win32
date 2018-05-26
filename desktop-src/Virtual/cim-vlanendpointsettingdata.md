---
title: CIM\_VLANEndpointSettingData class
description: Represents configuration data for a VLAN endpoint.
ms.assetid: b0782c62-940d-4ea0-9203-bc7bc12f0911
keywords:
- CIM_VLANEndpointSettingData class Hyper-V
- CIM_VLANEndpointSettingData class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_VLANEndpointSettingData
- CIM_VLANEndpointSettingData.Caption
- CIM_VLANEndpointSettingData.Description
- CIM_VLANEndpointSettingData.InstanceID
- CIM_VLANEndpointSettingData.ElementName
- CIM_VLANEndpointSettingData.PruneEligibleVLANList
- CIM_VLANEndpointSettingData.NativeVLAN
- CIM_VLANEndpointSettingData.DefaultVLAN
- CIM_VLANEndpointSettingData.TrunkedVLANList
- CIM_VLANEndpointSettingData.AccessVLAN
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

# CIM\_VLANEndpointSettingData class

Represents configuration data for a VLAN endpoint.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

> [!Note]  
> The configuration data is associated with an endpoint through the [**CIM\_ElementSettingData**](cim-elementsettingdata.md) class.

 

## Syntax

``` syntax
[Abstract, Experimental, Version("2.11.0"), AMENDMENT]
class CIM_VLANEndpointSettingData : CIM_SettingData
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
  uint16 PruneEligibleVLANList[];
  uint16 NativeVLAN;
  uint16 DefaultVLAN;
  uint16 TrunkedVLANList[];
  uint16 AccessVLAN;
};
```

## Members

The **CIM\_VLANEndpointSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_VLANEndpointSettingData** class has these properties.

<dl> <dt>

**AccessVLAN**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**")
</dt> </dl>

The access VLAN for the endpoint.

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

**DefaultVLAN**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**")
</dt> </dl>

The default value for the native VLAN on the trunk endpoint.

> [!Note]  
> This property is only used when the VLAN endpoint is operating in trunking mode, which is specified in the **OperationalEndpointMode** property.

 

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

The user-friendly name for an instance of this class. In addition, the user-friendly name can be used as an index for a search or query. The name does not have to be unique within a namespace.

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> -   *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID** property, or be a registered ID that is assigned by a recognized global authority.
> -   *OrgID* must not contain a colon. The first colon in **InstanceID** must be between the *OrgID* and*LocalID*.
> -   *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
> -   If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
> -   For DMTF defined instances, the pattern must be used with the *OrgID* set to "CIM".

 

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**NativeVLAN**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**")
</dt> </dl>

The VLAN ID that is used to tag untagged traffic received on the trunk endpoint.

> [!Note]  
> This property is only used when the VLAN endpoint is operating in trunking mode, which is specified in the **SwitchEndpointMode** property.

 

</dd> <dt>

**PruneEligibleVLANList**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**")
</dt> </dl>

An array that contains IDs of VLANs that the system may remove from the trunk endpoint.

> [!Note]  
> This property is only used when the VLAN endpoint is operating in trunking mode, which is specified in the **OperationalEndpointMode** property.

 

</dd> <dt>

**TrunkedVLANList**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**")
</dt> </dl>

An array that contains IDs of VLAN endpoints with trunking enabled.

> [!Note]  
> This property is only used when the VLAN endpoint is operating in trunking mode, which is specified in the **OperationalEndpointMode** property.

 

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

[**CIM\_SettingData**](cim-settingdata.md)
</dt> </dl>

 

 





