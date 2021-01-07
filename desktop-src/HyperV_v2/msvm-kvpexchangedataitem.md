---
description: Represents a key/value pair.
ms.assetid: B13E9C5F-5B13-4EE5-AE5F-F51B61BDB9B7
title: Msvm_KvpExchangeDataItem class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Msvm_KvpExchangeDataItem
- Msvm_KvpExchangeDataItem.InstanceID
- Msvm_KvpExchangeDataItem.Caption
- Msvm_KvpExchangeDataItem.Description
- Msvm_KvpExchangeDataItem.ElementName
- Msvm_KvpExchangeDataItem.Source
- Msvm_KvpExchangeDataItem.Name
- Msvm_KvpExchangeDataItem.Data
api_type:
- DllExport
api_location:
- vmms.exe
---

# Msvm\_KvpExchangeDataItem class

Represents a key/value pair.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider")]
class Msvm_KvpExchangeDataItem : CIM_ManagedElement
{
  string InstanceID;
  string Caption = "Key-Value Pair Exchange Data Item";
  string Description = "Microsoft Key-Value Pair Exchange Data Item";
  string ElementName = "Key-Value Pair Exchange Data Item";
  uint16 Source;
  string Name;
  string Data;
};
```

## Members

The **Msvm\_KvpExchangeDataItem** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_KvpExchangeDataItem** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MAXLEN**](/windows/desktop/WmiSdk/standard-qualifiers) (1024)
</dt> </dl>

The value portion of the key/value pair.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MAXLEN**](/windows/desktop/WmiSdk/standard-qualifiers) (1024)
</dt> </dl>

The key portion of the key/value pair.



| Key                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>"CSDVersion"</dt> </dl>                 | A string that represents the latest service pack installed on the guest system. For example, "Service Pack 2". If no service pack has been installed, this string is empty.<br/>                                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>"FullyQualifiedDomainName"</dt> </dl>   | A string that represents the fully qualified DNS name that uniquely identifies the local computer. This name is a combination of the DNS host name and the DNS domain name, using the format *HostName*.*DomainName*. If the local computer is a node in a cluster, this value is the fully qualified DNS name of the cluster virtual server. This value matches the name returned by the [**GetComputerNameEx**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getcomputernameexa) function when the *NameType* parameter is "ComputerNameDnsFullyQualified".<br/> |
| <dl> <dt>"IntegrationServicesVersion"</dt> </dl> | A string representing the version of the Integration Services currently installed in the guest virtual machine (for example, "6.1.7000.0").<br/>                                                                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>"NetworkAddressIPv4"</dt> </dl>         | A string that contains a semicolon-delimited list of the IPv4 addresses currently assigned to the guest virtual machine. The list is automatically updated whenever a TCP/IP configuration change occurs on the guest virtual machine. Each address is represented in dot-decimal notation. <br/>                                                                                                                                                                                                                         |
| <dl> <dt>"NetworkAddressIPv6"</dt> </dl>         | A string that contains a semicolon-delimited list of the IPv6 addresses currently assigned to the guest virtual machine. The list is automatically updated whenever a TCP/IP configuration change occurs on the guest virtual machine. Each address is represented in colon-hexadecimal notation. The IPv4 and IPv6 lists are not guaranteed to be in sync at all times.<br/>                                                                                                                                             |
| <dl> <dt>"OSBuildNumber"</dt> </dl>              | A string that represents the build number of the operating system.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <dl> <dt>"OSEditionId"</dt> </dl>                | A string representing the edition (SKU) of the guest virtual machine operating system. For a list of possible values, see the [**GetProductInfo**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getproductinfo) function.<br/>                                                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>"OSName"</dt> </dl>                     | A string that represents the name of the operating system. This value comes from the following registry entry: **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**ProductName**<br/> <br/>                                                                                                                                                                                                                                                                                |
| <dl> <dt>"OSMajorVersion"</dt> </dl>             | A string that represents the major version number of the operating system.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <dl> <dt>"OSMinorVersion"</dt> </dl>             | A string that represents the minor version number of the operating system.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <dl> <dt>"OSPlatformId"</dt> </dl>               | A string that represents the operating system platform. The possible values of the **Data** property are "1" to indicate an unsupported Windows system and "2" to indicate a supported Windows system.<br/>                                                                                                                                                                                                                                                                                                               |
| <dl> <dt>"OSVersion"</dt> </dl>                  | A string that represents the operating system version. The format of this string is *MajorVersion*.*MinorVersion*.*BuildNumber*. For example, "5.2.3790" for Windows Server 2003.<br/>                                                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>"ProcessorArchitecture"</dt> </dl>      | A string that represents the processor architecture of the operating system. For a list of values, see the **wProcessorArchitecture** member of the [**SYSTEM\_INFO**](/windows/desktop/api/sysinfoapi/ns-sysinfoapi-system_info) structure.<br/>                                                                                                                                                                                                                                                                                                              |
| <dl> <dt>"ProductType"</dt> </dl>                | A string that represents the product type. For a list of values, see the **wProductType** member of the [**OSVERSIONINFOEX**](/windows/desktop/api/winnt/ns-winnt-osversioninfoexa) structure.<br/>                                                                                                                                                                                                                                                                                                                                                   |
| <dl> <dt>"RDPAddressIPv4"</dt> </dl>             | A string that contains a semicolon-delimited list of the IPv4 addresses that the guest virtual machine RDP stack is currently listening on. If the RDP stack is not currently running, the string will be empty. The list is automatically updated whenever a TCP/IP configuration change affects the RDP stack on the guest virtual machine. Each address is represented in dot-decimal notation.<br/>                                                                                                                   |
| <dl> <dt>"RDPAddressIPv6"</dt> </dl>             | A string that contains a semicolon-delimited list of the IPv6 addresses that the guest virtual machine RDP stack is currently listening on. If the RDP stack is not currently running, the string will be empty. The list is automatically updated whenever a TCP/IP configuration change affects the RDP stack on the guest virtual machine. Each address is represented in colon-hexadecimal notation.<br/>                                                                                                             |
| <dl> <dt>"ServicePackMajor"</dt> </dl>           | A string that represents the major version number of the latest service pack installed on the system.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>"ServicePackMinor"</dt> </dl>           | A string that represents the minor version number of the latest service pack installed on the system.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>"SuiteMask"</dt> </dl>                  | A string that represents the product suites available on the system. This string is a combination of any of the values of the **wSuiteMask** member of the [**OSVERSIONINFOEX**](/windows/desktop/api/winnt/ns-winnt-osversioninfoexa) structure.<br/>                                                                                                                                                                                                                                                                                                |



 

</dd> <dt>

**Source**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The source of the data.



| Value                                                                        | Meaning                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | "HostExchangeItems" when pushed by the host.<br/>                                                                                                                                                                                      |
| <dl> <dt>1</dt> </dl> | "GuestExchangeItems" when pushed by the guest virtual machine.<br/>                                                                                                                                                                    |
| <dl> <dt>2</dt> </dl> | "GuestIntrinsicExchangeItems" when automatically populated by the guest virtual machine.<br/>                                                                                                                                          |
| <dl> <dt>4</dt> </dl> | Indicates that the item is host-only and not shared with the guest virtual machine. Used with the **HostOnlyItems** property of the [**Msvm\_KvpExchangeComponentSettingData**](msvm-kvpexchangecomponentsettingdata.md) class. <br/> |



 

</dd> </dl>

## Remarks

Access to the **Msvm\_KvpExchangeDataItem** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dt>

[**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement)
</dt> </dl>

 

