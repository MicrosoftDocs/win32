---
description: Describes the checksum offload data settings for a network adapter.
ms.assetid: 5b766937-6c37-4873-9de8-0fc29d969f67
title: MSFT\_NetAdapterChecksumOffloadSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterChecksumOffloadSettingData
- MSFT_NetAdapterChecksumOffloadSettingData.Caption
- MSFT_NetAdapterChecksumOffloadSettingData.Description
- MSFT_NetAdapterChecksumOffloadSettingData.ElementName
- MSFT_NetAdapterChecksumOffloadSettingData.InstanceID
- MSFT_NetAdapterChecksumOffloadSettingData.Name
- MSFT_NetAdapterChecksumOffloadSettingData.InterfaceDescription
- MSFT_NetAdapterChecksumOffloadSettingData.Source
- MSFT_NetAdapterChecksumOffloadSettingData.SystemName
- MSFT_NetAdapterChecksumOffloadSettingData.IpIPv4Enabled
- MSFT_NetAdapterChecksumOffloadSettingData.TcpIPv4Enabled
- MSFT_NetAdapterChecksumOffloadSettingData.TcpIPv6Enabled
- MSFT_NetAdapterChecksumOffloadSettingData.UdpIPv4Enabled
- MSFT_NetAdapterChecksumOffloadSettingData.UdpIPv6Enabled
- MSFT_NetAdapterChecksumOffloadSettingData.ChecksumOffloadHardwareCapabilities
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterChecksumOffloadSettingData class

Describes the checksum offload data settings for a network adapter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterChecksumOffloadSettingData : MSFT_NetAdapterSettingData
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
  string Name;
  string InterfaceDescription;
  uint32 Source;
  string SystemName;
  uint32 IpIPv4Enabled;
  uint32 TcpIPv4Enabled;
  uint32 TcpIPv6Enabled;
  uint32 UdpIPv4Enabled;
  uint32 UdpIPv6Enabled;
  string ChecksumOffloadHardwareCapabilities;
};
```

## Members

The **MSFT\_NetAdapterChecksumOffloadSettingData** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetAdapterChecksumOffloadSettingData** class has these methods.



| Method                                                               | Description                                                                       |
|:---------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**Disable**](disable-msft-netadapterchecksumoffloadsettingdata.md) | Disables the TCPIP checksum offload properties on the network adapter.<br/> |
| [**Enable**](enable-msft-netadapterchecksumoffloadsettingdata.md)   | Enables the TCPIP checksum offload properties on the network adapter.<br/>  |



 

### Properties

The **MSFT\_NetAdapterChecksumOffloadSettingData** class has these properties.

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

**ChecksumOffloadHardwareCapabilities**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The checksum offload hardware capabilities of the Adapter.

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

**IpIPv4Enabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if IP checksum offload is currently enabled for IPv4 packets on this Adapter.

<dl> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
</dt> <dt>

<span id="TxEnabled"></span><span id="txenabled"></span><span id="TXENABLED"></span>**TxEnabled** (1)
</dt> <dt>

<span id="RxEnabled"></span><span id="rxenabled"></span><span id="RXENABLED"></span>**RxEnabled** (2)
</dt> <dt>

<span id="RxTxEnabled_"></span><span id="rxtxenabled_"></span><span id="RXTXENABLED_"></span>**RxTxEnabled** (3)
</dt> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name, also known as Connection Name, "ifAlias", or InterfaceAlias, is a unique name assigned to the adapter during installation. The Name of the adapter can be changed by the administrator and is persisted across the boot or network adapter restart. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

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

**TcpIPv4Enabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if TCP checksum offload is currently enabled for IPv4 packets on this Adapter.

<dl> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
</dt> <dt>

<span id="TxEnabled"></span><span id="txenabled"></span><span id="TXENABLED"></span>**TxEnabled** (1)
</dt> <dt>

<span id="RxEnabled"></span><span id="rxenabled"></span><span id="RXENABLED"></span>**RxEnabled** (2)
</dt> <dt>

<span id="RxTxEnabled_"></span><span id="rxtxenabled_"></span><span id="RXTXENABLED_"></span>**RxTxEnabled** (3)
</dt> </dl>

</dd> <dt>

**TcpIPv6Enabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if TCP checksum offload is currently enabled for IPv6 packets on this Adapter.

<dl> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
</dt> <dt>

<span id="TxEnabled"></span><span id="txenabled"></span><span id="TXENABLED"></span>**TxEnabled** (1)
</dt> <dt>

<span id="RxEnabled"></span><span id="rxenabled"></span><span id="RXENABLED"></span>**RxEnabled** (2)
</dt> <dt>

<span id="RxTxEnabled_"></span><span id="rxtxenabled_"></span><span id="RXTXENABLED_"></span>**RxTxEnabled** (3)
</dt> </dl>

</dd> <dt>

**UdpIPv4Enabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if UDP checksum offload is currently enabled for IPv4 packets on this Adapter.

<dl> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
</dt> <dt>

<span id="TxEnabled"></span><span id="txenabled"></span><span id="TXENABLED"></span>**TxEnabled** (1)
</dt> <dt>

<span id="RxEnabled"></span><span id="rxenabled"></span><span id="RXENABLED"></span>**RxEnabled** (2)
</dt> <dt>

<span id="RxTxEnabled_"></span><span id="rxtxenabled_"></span><span id="RXTXENABLED_"></span>**RxTxEnabled** (3)
</dt> </dl>

</dd> <dt>

**UdpIPv6Enabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if UDP checksum offload is currently enabled for IPv6 packets on this Adapter.

<dl> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
</dt> <dt>

<span id="TxEnabled"></span><span id="txenabled"></span><span id="TXENABLED"></span>**TxEnabled** (1)
</dt> <dt>

<span id="RxEnabled"></span><span id="rxenabled"></span><span id="RXENABLED"></span>**RxEnabled** (2)
</dt> <dt>

<span id="RxTxEnabled_"></span><span id="rxtxenabled_"></span><span id="RXTXENABLED_"></span>**RxTxEnabled** (3)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

