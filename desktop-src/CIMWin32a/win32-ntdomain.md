---
title: Win32\_NTDomain class
description: The Win32\_NTDomain \ 32; WMI class represents a Windows domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b7fb748c-8e4f-4d4b-bf52-e2a4b6c3cf2f
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_NTDomain class
- Win32_NTDomain class, described
topic_type:
- apiref
api_name:
- Win32_NTDomain
- Win32_NTDomain.Caption
- Win32_NTDomain.CreationClassName
- Win32_NTDomain.Description
- Win32_NTDomain.InstallDate
- Win32_NTDomain.Name
- Win32_NTDomain.PrimaryOwnerContact
- Win32_NTDomain.PrimaryOwnerName
- Win32_NTDomain.Status
- Win32_NTDomain.ClientSiteName
- Win32_NTDomain.DcSiteName
- Win32_NTDomain.DNSForestName
- Win32_NTDomain.DomainControllerAddress
- Win32_NTDomain.DomainControllerAddressType
- Win32_NTDomain.DomainControllerName
- Win32_NTDomain.DomainGUID
- Win32_NTDomain.DomainName
- Win32_NTDomain.DSDirectoryServiceFlag
- Win32_NTDomain.DSDnsControllerFlag
- Win32_NTDomain.DSDnsDomainFlag
- Win32_NTDomain.DSDnsForestFlag
- Win32_NTDomain.DSGlobalCatalogFlag
- Win32_NTDomain.DSKerberosDistributionCenterFlag
- Win32_NTDomain.DSPrimaryDomainControllerFlag
- Win32_NTDomain.DSTimeServiceFlag
- Win32_NTDomain.DSWritableFlag
- Win32_NTDomain.NameFormat
- Win32_NTDomain.Roles
api_location:
- Wmipcima.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_NTDomain class

The **Win32\_NTDomain** [WMI class](https://msdn.microsoft.com/library/aa393244) represents a Windows domain.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32a"), UUID("78F4FA18-EE46-4D4C-AB9B-8CC0D42B7038"), AMENDMENT]
class Win32_NTDomain : CIM_System
{
  string   Caption;
  string   CreationClassName;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   PrimaryOwnerContact;
  string   PrimaryOwnerName;
  string   Status;
  string   ClientSiteName;
  string   DcSiteName;
  string   DNSForestName;
  string   DomainControllerAddress;
  sint32   DomainControllerAddressType;
  string   DomainControllerName;
  string   DomainGUID;
  string   DomainName;
  boolean  DSDirectoryServiceFlag;
  boolean  DSDnsControllerFlag;
  boolean  DSDnsDomainFlag;
  boolean  DSDnsForestFlag;
  boolean  DSGlobalCatalogFlag;
  boolean  DSKerberosDistributionCenterFlag;
  boolean  DSPrimaryDomainControllerFlag;
  boolean  DSTimeServiceFlag;
  boolean  DSWritableFlag;
  string   NameFormat;
  string   Roles[];
};
```

## Members

The **Win32\_NTDomain** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NTDomain** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**ClientSiteName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the site where the domain controller is configured. This value can be **NULL**.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503).

</dd> <dt>

**DcSiteName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the site where the domain controller is located. This value can be **NULL**.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**DNSForestName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the root of the DNS tree.

</dd> <dt>

**DomainControllerAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Address of the discovered domain controller.

</dd> <dt>

**DomainControllerAddressType**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of address specified in the **DomainControllerAddress** property.

<dt>

<span id="DS_INET_ADDRESS"></span><span id="ds_inet_address"></span>

**DS\_INET\_ADDRESS** (1)


</dt> <dd></dd> <dt>

<span id="DS_NETBIOS_ADDRESS"></span><span id="ds_netbios_address"></span>

**DS\_NETBIOS\_ADDRESS** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**DomainControllerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Computer name for the discovered domain controller.

</dd> <dt>

**DomainGUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Globally unique identifier (**GUID**) of the domain controller. This property is 0 (zero) if the domain controller does not have a **GUID**.

</dd> <dt>

**DomainName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the domain.

Example: microsoft.com

</dd> <dt>

**DSDirectoryServiceFlag**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the domain controller is a directory service server.

</dd> <dt>

**DSDnsControllerFlag**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the Domain Controller Name is in DNS format.

Example: www.mynode.com or 135.5.33.19

</dd> <dt>

**DSDnsDomainFlag**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the **DomainName** value is in DNS format.

</dd> <dt>

**DSDnsForestFlag**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the **DNSForestName** value is in Domain Name System (DNS) format.

</dd> <dt>

**DSGlobalCatalogFlag**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the domain controller is a Global Catalog server for the **DNSForestName** value.

</dd> <dt>

**DSKerberosDistributionCenterFlag**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the domain controller is a Kerberos Key Distribution Center for the domain.

</dd> <dt>

**DSPrimaryDomainControllerFlag**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the domain controller is the Primary Domain Controller.

</dd> <dt>

**DSTimeServiceFlag**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the domain is running the Windows Time service.

</dd> <dt>

**DSWritableFlag**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the domain controller hosts a writeable DS or security accounts manager (SAM).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name"), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Label by which the object is known.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Format to generate the system name using the subclass heuristic.

This property is inherited from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503).

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

How the primary system owner can be reached (for example, phone number or email address).

This property is inherited from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503).

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Name of the primary system owner.

This property is inherited from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503).

</dd> <dt>

**Roles**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings that specify the roles the computer system plays in the IT environment. Values are defined by the IT environment in which the computer system resides. For example, for an instance of a networking system, this property might contain the string, "Switch" or "Bridge".

This property is inherited from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **Win32\_NTDomain** class is derived from [**CIM\_System**](https://msdn.microsoft.com/library/aa388503). You can use this class to list all of the domains that can be discovered from the local computer. However, the number of domains that the provider can discover is limited by permissions, trust relationships, and network latency. To discover to which domain a particular computer belongs, you can query the [**Win32\_ComputerSystem**](https://msdn.microsoft.com/library/aa394102) instance on that computer, and then check the **Domain** property.

## Examples

The [List Domain Information Using WMI](https://Gallery.TechNet.Microsoft.Com/fd6ef110-011f-4799-b923-59c35d0d52df) VBScript code sample on TechNet Gallery uses **Win32\_NTDomain** to retrieve information about domains discovered on the network.

The following PowerShell code sample describes how to query for **Win32\_NTDomain**.


```PowerShell
get-wmiobject | win32_ntDomain
```



On a Windows Server 2008 VM-based test system, the previous code produces the following output:

``` syntax
ClientSiteName          : Default-First-Site-Name
DcSiteName              : Default-First-Site-Name
Description             : GKTRAIN
DnsForestName           : gktrain.net
DomainControllerAddress : \\10.10.1.61
DomainControllerName    : \\DC1
DomainName              : GKTRAIN
Roles                   :
Status                  : OK
```

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_System**](https://msdn.microsoft.com/library/aa388503)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





