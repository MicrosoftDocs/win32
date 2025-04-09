---
description: Represents a set of global DNS client settings.
ms.assetid: fb50dbb6-084c-4ff4-98a7-93a0fe97d031
title: MSFT\_DNSClientGlobalSetting class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_DNSClientGlobalSetting
- MSFT_DNSClientGlobalSetting.Caption
- MSFT_DNSClientGlobalSetting.Description
- MSFT_DNSClientGlobalSetting.InstanceId
- MSFT_DNSClientGlobalSetting.ElementName
- MSFT_DNSClientGlobalSetting.ProtocolIFType
- MSFT_DNSClientGlobalSetting.AddressOrigin
- MSFT_DNSClientGlobalSetting.AppendPrimarySuffixes
- MSFT_DNSClientGlobalSetting.AppendParentSuffixes
- MSFT_DNSClientGlobalSetting.DNSSuffixesToAppend
- MSFT_DNSClientGlobalSetting.UseSuffixSearchList
- MSFT_DNSClientGlobalSetting.UseDevolution
- MSFT_DNSClientGlobalSetting.SuffixSearchList
- MSFT_DNSClientGlobalSetting.DevolutionLevel
api_type: 
- DllExport
api_location: 
- DnsClientCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_DNSClientGlobalSetting class

Represents a set of global DNS client settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_DNSClientGlobalSetting : CIM_DNSGeneralSettingData
{
  string  Caption;
  string  Description;
  string  InstanceId;
  string  ElementName;
  uint16  ProtocolIFType;
  uint16  AddressOrigin;
  boolean AppendPrimarySuffixes;
  boolean AppendParentSuffixes;
  string  DNSSuffixesToAppend[];
  boolean UseSuffixSearchList;
  boolean UseDevolution;
  string  SuffixSearchList[];
  uint32  DevolutionLevel;
};
```

## Members

The **MSFT\_DNSClientGlobalSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DNSClientGlobalSetting** class has these properties.

<dl> <dt>

**AddressOrigin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Override** (AddressOrigin)
</dt> </dl>

Gets a value that specifies the structure of the IP endpoint address for DNS clients.

This property is inherited from **CIM\_DNSGeneralSettingData**.

This property can contain one of the following values. The default value is "2" (not applicable).



| Value                                                                                | Meaning                    |
|--------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0 1</dt> </dl>       | DMTF Reserved<br/>   |
| <dl> <dt>2</dt> </dl>         | Not Applicable<br/>  |
| <dl> <dt>3 32767</dt> </dl>   | DMTF Reserved<br/>   |
| <dl> <dt>32768 ...</dt> </dl> | Vendor Reserved<br/> |



 

</dd> <dt>

**AppendParentSuffixes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_DNSProtocolEndpoint.AppendParentSuffixes)
</dt> </dl>

Gets and sets a value that indicates whether DNS clients should append the parent domain suffix to a target name before the name is resolved.

This property is inherited from **CIM\_DNSGeneralSettingData**.

</dd> <dt>

**AppendPrimarySuffixes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_DNSProtocolEndpoint.AppendPrimarySuffixes)
</dt> </dl>

Gets and sets a value that indicates whether DNS clients should append the primary domain suffix to a target name before the name is resolved.

This property is inherited from **CIM\_DNSGeneralSettingData**.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (64), [**Dynamic**](/windows/win32/wmisdk/standard-wmi-qualifiers)
</dt> </dl>

Gets the short description of the client settings.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Override** (Description)
</dt> </dl>

Gets a description of the client settings.

This property is inherited from the **CIM\_ManagedElement** class.

</dd> <dt>

**DevolutionLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the devolution level to use when DNS devolution is enabled.

</dd> <dt>

**DNSSuffixesToAppend**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_DNSProtocolEndpoint.DNSSuffixesToAppend)
</dt> </dl>

Gets and sets an array that contains the DNS suffixes to append when a host name is resolved.

This property is inherited from **CIM\_DNSGeneralSettingData**.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user-friendly name of the client settings.

This property is inherited from **CIM\_SettingData**.

</dd> <dt>

**InstanceId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the unique identifier of this object. The ID must be unique within the scope of the instantiating namespace.

This property is inherited from **CIM\_SettingData**.

</dd> <dt>

**ProtocolIFType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ModelCorrespondence** (CIM\_ProtocolEndpoint.ProtocolIFType)
</dt> </dl>

Gets the IP version for DNS clients.

This property is inherited from **CIM\_IPAssignmentSettingData**.



| Value                                                                                | Meaning                    |
|--------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0</dt> </dl>         | Unknown<br/>         |
| <dl> <dt>1 4095</dt> </dl>    | DMTF Reserved<br/>   |
| <dl> <dt>4096</dt> </dl>      | IPv4<br/>            |
| <dl> <dt>4097</dt> </dl>      | IPv6<br/>            |
| <dl> <dt>32768 ...</dt> </dl> | Vendor Reserved<br/> |



 

</dd> <dt>

**SuffixSearchList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets an array that contains a global suffix search list.

</dd> <dt>

**UseDevolution**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether DNS clients use DNS devolution when the **AppendParentSuffixes** property is set to **true**.

</dd> <dt>

**UseSuffixSearchList**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether DNS clients use the global suffix search list when the **AppendPrimarySuffixes** property is set to **true**.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                              |
| MOF<br/>                      | <dl> <dt>DnsClientCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientCim.dll</dt> </dl> |



## See also

<dl> <dt>

[Dnsclientcim Provider Classes](dns-client-classes.md)
</dt> </dl>

 

