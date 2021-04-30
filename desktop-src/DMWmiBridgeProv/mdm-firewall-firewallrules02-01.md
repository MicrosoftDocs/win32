---
title: MDM_Firewall_FirewallRules02_01 class
description: The MDM\_Firewall\_FirewallRules02\_01 class is used to configure the Windows Defender Firewall settings.
ms.assetid: b09cbd98-152e-486c-acb5-4e1d83e5f8e2
keywords:
- MDM_Firewall_FirewallRules02_01 class
- MDM_Firewall_FirewallRules02_01 class, described
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MDM_Firewall_FirewallRules02_01
- MDM_Firewall_FirewallRules02_01.InstanceID
- MDM_Firewall_FirewallRules02_01.ParentID
- MDM_Firewall_FirewallRules02_01.IcmpTypesAndCodes
- MDM_Firewall_FirewallRules02_01.FriendlyName
api_type: 
- DllExport
api_location: 
- DMWmiBridgeProv.dll
---

# MDM\_Firewall\_FirewallRules02\_01 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The MDM\_Firewall\_FirewallRules02\_01 class is used to configure the Windows Defender Firewall settings.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv1")]
class MDM_Firewall_FirewallRules02_01
{
  string  InstanceID;
  string  ParentID;
  sint32  Protocol;
  string  LocalPortRanges;
  string  RemotePortRanges;
  string  LocalAddressRanges;
  string  RemoteAddressRanges;
  string  Description;
  boolean Enabled;
  sint32  Profiles;
  string  Direction;
  string  InterfaceTypes;
  string  IcmpTypesAndCodes;
  boolean EdgeTraversal;
  string  LocalUserAuthorizedList;
  string  Status;
  string  FriendlyName;
  string  Name;
};
```

## Members

The **MDM\_Firewall\_FirewallRules02\_01** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Firewall\_FirewallRules02\_01** class has these properties.

<dl> <dt>

[Description](/windows/client-management/mdm/firewall-csp#description)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Direction](/windows/client-management/mdm/firewall-csp#direction)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[EdgeTraversal](/windows/client-management/mdm/firewall-csp#edgetraversal)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Enabled](/windows/client-management/mdm/firewall-csp#enabled)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

</dd> <dt>

**IcmpTypesAndCodes**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

</dd> <dt>

[InterfaceTypes](/windows/client-management/mdm/firewall-csp#interfacetypes)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LocalAddressRanges](/windows/client-management/mdm/firewall-csp#localaddressranges)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LocalPortRanges](/windows/client-management/mdm/firewall-csp#localportranges)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LocalUserAuthorizedList](/windows/client-management/mdm/firewall-csp#localuserauthorizedlist)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Name](/windows/client-management/mdm/firewall-csp#name)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

</dd> <dt>

[Profiles](/windows/client-management/mdm/firewall-csp#profiles)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Protocol](/windows/client-management/mdm/firewall-csp#protocol)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[RemoteAddressRanges](/windows/client-management/mdm/firewall-csp#remoteaddressranges)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[RemotePortRanges](/windows/client-management/mdm/firewall-csp#remoteportranges)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Status](/windows/client-management/mdm/firewall-csp#status)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | None supported<br/>                                                                       |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                              |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv1.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl>  |



 

