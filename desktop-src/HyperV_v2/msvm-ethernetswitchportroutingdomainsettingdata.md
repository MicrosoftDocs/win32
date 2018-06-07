---
Description: Represents the routing domain setting data.
ms.assetid: 6216cc4e-b2aa-4344-b8fa-489b986c14be
title: Msvm\_EthernetSwitchPortRoutingDomainSettingData class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_EthernetSwitchPortRoutingDomainSettingData class

Represents the routing domain setting data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), UUID("BF874DF0-F729-4312-A0FA-194271B88990"), ExtensionId("11EC6134-128A-4A23-B12F-164184B48348"), InterfaceVersion("1"), InterfaceRevision("0"), DisplayName("Ethernet Switch Port Routing Domain Settings"), AMENDMENT]
class Msvm_EthernetSwitchPortRoutingDomainSettingData : Msvm_EthernetSwitchPortFeatureSettingData
{
  string RoutingDomainGuid = "";
  string RoutingDomainName = "";
  uint32 IsolationIdList[] = {};
  string IsolationIdNameList[] = {};
};
```

## Members

The **Msvm\_EthernetSwitchPortRoutingDomainSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_EthernetSwitchPortRoutingDomainSettingData** class has these properties.

<dl> <dt>

**IsolationIdList**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (3), [**Version**](https://msdn.microsoft.com/library/aa393650) (1), [**Revision**](https://msdn.microsoft.com/library/aa393650) (0)
</dt> </dl>

The VirtualSubnetId or VLAN IDs for the routing domains.

</dd> <dt>

**IsolationIdNameList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **WmiDataId** (4), [**Version**](https://msdn.microsoft.com/library/aa393650) (1), [**Revision**](https://msdn.microsoft.com/library/aa393650) (0)
</dt> </dl>

The VirtualSubnetId or VLAN friendly name array.

</dd> <dt>

**RoutingDomainGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (38), **WmiDataId** (1), [**Version**](https://msdn.microsoft.com/library/aa393650) (1), [**Revision**](https://msdn.microsoft.com/library/aa393650) (0)
</dt> </dl>

The routing domain GUID.

</dd> <dt>

**RoutingDomainName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (127), **WmiDataId** (2), [**Version**](https://msdn.microsoft.com/library/aa393650) (1), [**Revision**](https://msdn.microsoft.com/library/aa393650) (0)
</dt> </dl>

The routing domain friendly name.

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_EthernetSwitchPortFeatureSettingData**](msvm-ethernetswitchportfeaturesettingdata.md)
</dt> </dl>

 

 




