---
description: Represents the settings for offloading features for Microsoft TCP/IP WMI v2 provider.
ms.assetid: e9e57c03-097e-4df2-9cc6-82fef81cb056
title: MSFT\_NetOffloadGlobalSetting class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetOffloadGlobalSetting
- MSFT_NetOffloadGlobalSetting.Caption
- MSFT_NetOffloadGlobalSetting.Description
- MSFT_NetOffloadGlobalSetting.InstanceID
- MSFT_NetOffloadGlobalSetting.ElementName
- MSFT_NetOffloadGlobalSetting.ReceiveSideScaling
- MSFT_NetOffloadGlobalSetting.ReceiveSegmentCoalescing
- MSFT_NetOffloadGlobalSetting.Chimney
- MSFT_NetOffloadGlobalSetting.TaskOffload
- MSFT_NetOffloadGlobalSetting.NetworkDirect
- MSFT_NetOffloadGlobalSetting.PacketCoalescingFilter
- MSFT_NetOffloadGlobalSetting.NetworkDirectAcrossIPSubnets
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetOffloadGlobalSetting class

Represents the settings for offloading features for Microsoft TCP/IP WMI v2 provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::Settings"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetOffloadGlobalSetting : MSFT_NetSettingData
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
  uint8  ReceiveSideScaling;
  uint8  ReceiveSegmentCoalescing;
  uint8  Chimney;
  uint8  TaskOffload;
  uint8  NetworkDirect;
  uint8  PacketCoalescingFilter;
  uint8  NetworkDirectAcrossIPSubnets;
};
```

## Members

The **MSFT\_NetOffloadGlobalSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetOffloadGlobalSetting** class has these properties.

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

**Chimney**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to turn on TCP chimney offload. For information on TCP chimney offload, see [TCP Chimney Offload](/previous-versions/windows/hardware/network/ndis-tcp-chimney-offload).



| Value                                                                                                                                                                                                                               | Meaning                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl>     | TCP chimney offload is turned off.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>         | TCP chimney offload is turned on.<br/>  |
| <span id="Automatic"></span><span id="automatic"></span><span id="AUTOMATIC"></span><dl> <dt>**Automatic**</dt> <dt>2</dt> </dl> |                                               |



 

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

</dd> <dt>

**NetworkDirect**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to turn on NetworkDirect.



| Value                                                                                                                                                                                                                           | Meaning                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | NetworkDirect is turned off.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | NetworkDirect is turned on.<br/>  |



 

</dd> <dt>

**NetworkDirectAcrossIPSubnets**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to allow NetworkDirect connectivity outside of the local IP subnet.



| Value                                                                                                                                                                                                                       | Meaning                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <span id="Blocked"></span><span id="blocked"></span><span id="BLOCKED"></span><dl> <dt>**Blocked**</dt> <dt>0</dt> </dl> | NetworkDirect connectivity outside of the local IP subnet is not allowed.<br/> |
| <span id="Allowed"></span><span id="allowed"></span><span id="ALLOWED"></span><dl> <dt>**Allowed**</dt> <dt>1</dt> </dl> | NetworkDirect connectivity outside of the local IP subnet is allowed.<br/>     |



 

</dd> <dt>

**PacketCoalescingFilter**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to turn on packet coalescing filters. For information about packet coalescing, see [NDIS Packet Coalescing](/windows-hardware/drivers/network/ndis-packet-coalescing).



| Value                                                                                                                                                                                                                           | Meaning                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Packet coalescing filters are turned off.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Packet coalescing filters are turned on.<br/>  |



 

</dd> <dt>

**ReceiveSegmentCoalescing**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to turn on receive segment coalescing (RSC). For information about RSC, see [Receive Segment Coalescing](https://msdn.microsoft.com/library/windows/hardware/jj853324).



| Value                                                                                                                                                                                                                           | Meaning                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | RSC is turned off.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | RSC is turned on.<br/>  |



 

</dd> <dt>

**ReceiveSideScaling**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to turn on receive side scaling (RSS). For more information about RSS, see [Receive Side Scaling](/windows-hardware/drivers/network/receive-side-scaling-version-2-rssv2-).



| Value                                                                                                                                                                                                                           | Meaning                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | RSS is turned off.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | RSS is turned on.<br/>  |



 

</dd> <dt>

**TaskOffload**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to turn on TCP/IP task offload. For information about TCP/IP task offload, see [TCP/IP Task Offload](/windows-hardware/drivers/network/task-offload).



| Value                                                                                                                                                                                                                           | Meaning                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | TCP/IP task offload is turned off.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | TCP/IP task offload is turned on.<br/>  |



 

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

[**MSFT\_NetSettingData**](msft-netsettingdata-nettcpip.md)
</dt> <dt>

[Receive Side Scaling](/windows-hardware/drivers/network/receive-side-scaling-version-2-rssv2-)
</dt> <dt>

[Receive Segment Coalescing](https://msdn.microsoft.com/library/windows/hardware/jj853324)
</dt> <dt>

[TCP Chimney Offload](/previous-versions/windows/hardware/network/ndis-tcp-chimney-offload)
</dt> <dt>

[TCP/IP Task Offload](/windows-hardware/drivers/network/task-offload)
</dt> <dt>

[NDIS Packet Coalescing](/windows-hardware/drivers/network/ndis-packet-coalescing)
</dt> </dl>

 

