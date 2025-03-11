---
description: Represents a routing compartment for the TCP/IP (Internet Protocol Suite) provider.
ms.assetid: 5a6cc84c-a879-4c3a-bf1c-a9e6ff35c350
title: MSFT\_NetCompartment class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetCompartment
- MSFT_NetCompartment.Caption
- MSFT_NetCompartment.Description
- MSFT_NetCompartment.InstanceID
- MSFT_NetCompartment.ElementName
- MSFT_NetCompartment.CompartmentId
- MSFT_NetCompartment.CompartmentGuid
- MSFT_NetCompartment.CompartmentDescription
- MSFT_NetCompartment.CompartmentType
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetCompartment class

Represents a routing compartment for the TCP/IP (Internet Protocol Suite) provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::Settings"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetCompartment : MSFT_NetSettingData
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
  uint32 CompartmentId;
  string CompartmentGuid;
  string CompartmentDescription;
  uint32 CompartmentType;
};
```

## Members

The **MSFT\_NetCompartment** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetCompartment** class has these properties.

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

**CompartmentDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user-friendly description of the routing compartment.

**Windows 8.1, Windows Server 2012 R2, Windows 8 and Windows Server 2012:  **

This property is not supported before Windows 10 and Windows Server 2016.

</dd> <dt>

**CompartmentGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Get the Globally Unique Identifier (GUID) of the routing compartment.

**Windows 8.1, Windows Server 2012 R2, Windows 8 and Windows Server 2012:  **

This property is not supported before Windows 10 and Windows Server 2016.

</dd> <dt>

**CompartmentId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the identifier of the routing compartment.

</dd> <dt>

**CompartmentType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the type of the routing compartment.

**Windows 8.1, Windows Server 2012 R2, Windows 8 and Windows Server 2012:  **

This property is not supported before Windows 10 and Windows Server 2016.

<dl> <dt>

<span id="Unspecified"></span><span id="unspecified"></span><span id="UNSPECIFIED"></span>**Unspecified** (0)
</dt> <dt>

<span id="Native"></span><span id="native"></span><span id="NATIVE"></span>**Native** (1)
</dt> <dt>

<span id="RoutingDomain"></span><span id="routingdomain"></span><span id="ROUTINGDOMAIN"></span>**RoutingDomain** (2)
</dt> </dl>

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
| Minimum supported client<br/> | Windows 8.1<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                       |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetSettingData**](msft-netsettingdata-nettcpip.md)
</dt> <dt>

[NetTCPIP Provider Classes](net-tcpip-classes.md)
</dt> </dl>

 

