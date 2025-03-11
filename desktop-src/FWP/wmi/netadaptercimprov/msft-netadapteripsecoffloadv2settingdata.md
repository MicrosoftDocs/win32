---
description: IPsec Task Offload v2 settings for a network adapter.
ms.assetid: 195f4ab2-6dc0-4d14-9194-a76ba0f2b163
title: MSFT\_NetAdapterIPsecOffloadV2SettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterIPsecOffloadV2SettingData
- MSFT_NetAdapterIPsecOffloadV2SettingData.Caption
- MSFT_NetAdapterIPsecOffloadV2SettingData.Description
- MSFT_NetAdapterIPsecOffloadV2SettingData.ElementName
- MSFT_NetAdapterIPsecOffloadV2SettingData.InstanceID
- MSFT_NetAdapterIPsecOffloadV2SettingData.Name
- MSFT_NetAdapterIPsecOffloadV2SettingData.InterfaceDescription
- MSFT_NetAdapterIPsecOffloadV2SettingData.Source
- MSFT_NetAdapterIPsecOffloadV2SettingData.SystemName
- MSFT_NetAdapterIPsecOffloadV2SettingData.Enabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.IPv6Supported
- MSFT_NetAdapterIPsecOffloadV2SettingData.IPv4OptionsSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.IPv6NonIPsecExtensionHeadersSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.AhSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.EspSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.AhEspCombinedSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.TransportSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.TunnelSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.LsoSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.UdpEspSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.AuthenticationAlgorithmsSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.EncryptionAlgorithmsSupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.SaOffloadCapacitySupported
- MSFT_NetAdapterIPsecOffloadV2SettingData.IPv6Enabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.IPv4OptionsEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.IPv6NonIPsecExtensionHeadersEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.AhEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.EspEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.AhEspCombinedEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.TransportEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.TunnelEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.LsoEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.UdpEspEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.AuthenticationAlgorithmsEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.EncryptionAlgorithmsEnabled
- MSFT_NetAdapterIPsecOffloadV2SettingData.SaOffloadCapacityEnabled
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterIPsecOffloadV2SettingData class

IPsec Task Offload v2 settings for a network adapter

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterIPsecOffloadV2SettingData : MSFT_NetAdapterSettingData
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  string  Name;
  string  InterfaceDescription;
  uint32  Source;
  string  SystemName;
  boolean Enabled;
  boolean IPv6Supported;
  boolean IPv4OptionsSupported;
  boolean IPv6NonIPsecExtensionHeadersSupported;
  boolean AhSupported;
  boolean EspSupported;
  boolean AhEspCombinedSupported;
  boolean TransportSupported;
  boolean TunnelSupported;
  boolean LsoSupported;
  uint32  UdpEspSupported;
  uint32  AuthenticationAlgorithmsSupported;
  uint32  EncryptionAlgorithmsSupported;
  uint32  SaOffloadCapacitySupported;
  boolean IPv6Enabled;
  boolean IPv4OptionsEnabled;
  boolean IPv6NonIPsecExtensionHeadersEnabled;
  boolean AhEnabled;
  boolean EspEnabled;
  boolean AhEspCombinedEnabled;
  boolean TransportEnabled;
  boolean TunnelEnabled;
  boolean LsoEnabled;
  uint32  UdpEspEnabled;
  uint32  AuthenticationAlgorithmsEnabled;
  uint32  EncryptionAlgorithmsEnabled;
  uint32  SaOffloadCapacityEnabled;
};
```

## Members

The **MSFT\_NetAdapterIPsecOffloadV2SettingData** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetAdapterIPsecOffloadV2SettingData** class has these methods.



| Method                                                              | Description                                                                 |
|:--------------------------------------------------------------------|:----------------------------------------------------------------------------|
| [**Disable**](disable-msft-netadapteripsecoffloadv2settingdata.md) | Disable IPsec Task Offload v2 on the network adapter.<br/>            |
| [**Enable**](enable-msft-netadapteripsecoffloadv2settingdata.md)   | Enable IPsec Task Offload v2 on the network adapter.<br/>             |
| [**Set**](set-msft-netadapteripsecoffloadv2settingdata.md)         | Set the IPsec Task Offload v2 properties on the network adapter.<br/> |



 

### Properties

The **MSFT\_NetAdapterIPsecOffloadV2SettingData** class has these properties.

<dl> <dt>

**AhEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

AH enabled.

</dd> <dt>

**AhEspCombinedEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Both AH and ESP combined enabled.

</dd> <dt>

**AhEspCombinedSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports both Ah and Esp.

</dd> <dt>

**AhSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports Ah.

</dd> <dt>

**AuthenticationAlgorithmsEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Authentication Algorithms enabled.

</dd> <dt>

**AuthenticationAlgorithmsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports authentication algorithms.

</dd> <dt>

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

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property enables each instance to define a display name in addition to its key properties, identity data, and description information. Be aware that the Name property of ManagedSystemElement is also defined as a display name. However, it is often subclassed to be a Key. The same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enabled.

</dd> <dt>

**EncryptionAlgorithmsEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Encryption algorithms enabled.

</dd> <dt>

**EncryptionAlgorithmsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports encryption algorithms.

</dd> <dt>

**EspEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ESP enabled.

</dd> <dt>

**EspSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports Esp.

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

**IPv4OptionsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPv4 options enabled.

</dd> <dt>

**IPv4OptionsSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports IPv4 options.

</dd> <dt>

**IPv6Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPv6 enabled.

</dd> <dt>

**IPv6NonIPsecExtensionHeadersEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPv6 non-IP security extension headers enabled.

</dd> <dt>

**IPv6NonIPsecExtensionHeadersSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports IPv6 non-IP security extension headers.

</dd> <dt>

**IPv6Supported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports IPv6.

</dd> <dt>

**LsoEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

LSO enabled.

</dd> <dt>

**LsoSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports Lso.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name, also known as Connection Name, "ifAlias", or InterfaceAlias, is a unique name assigned to the adapter during installation. The Name of the adapter can be changed by the administrator and is persisted across the boot or network adapter restart. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**SaOffloadCapacityEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SA offload capacity enabled.

</dd> <dt>

**SaOffloadCapacitySupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ammount of SA offload capacity supported.

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

**TransportEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Transport enabled.

</dd> <dt>

**TransportSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports transport.

</dd> <dt>

**TunnelEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Tunnel enabled.

</dd> <dt>

**TunnelSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports tunnel.

</dd> <dt>

**UdpEspEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

UDP and ESP enabled.

</dd> <dt>

**UdpEspSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supports UDP and ESP.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

