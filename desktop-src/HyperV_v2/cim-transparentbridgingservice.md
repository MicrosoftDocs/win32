---
description: Represents the transparent bridging aspect of a CIM\_SwitchService object.
ms.assetid: 24f650ab-22a1-41c8-8498-c6c30e63c83c
title: CIM_TransparentBridgingService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_TransparentBridgingService
- CIM_TransparentBridgingService.AgingTime
- CIM_TransparentBridgingService.FID
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_TransparentBridgingService class

Represents the transparent bridging aspect of a [**CIM\_SwitchService**](cim-switchservice.md) object.

## Syntax

``` syntax
[Abstract, Version("2.7.0"), UMLPackagePath("CIM::Network::SwitchingBridging"), AMENDMENT]
class CIM_TransparentBridgingService : CIM_ForwardingService
{
  uint32 AgingTime = 300;
  uint32 FID;
};
```

## Members

The **CIM\_TransparentBridgingService** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_TransparentBridgingService** class has these properties.

<dl> <dt>

**AgingTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Seconds"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIB.IETF\|BRIDGE-MIB.dot1dTpAgingTime")
</dt> </dl>

The timeout period, in seconds, for aging out dynamically learned forwarding information. The 802.1D-1990 standard recommends a default of 300 seconds.

</dd> <dt>

**FID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Filtering Database Identifier used by VLAN-aware switches that have more than one filtering database.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ForwardingService**](cim-forwardingservice.md)
</dt> </dl>

 

