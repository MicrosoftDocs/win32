---
Description: 'The MSFT\_NetVirtualizationGlobalSettingData class represents the global settings and state of the WNV module for Hyper-V Network Virtualization.'
ms.assetid: '2c8976fa-6263-4fcc-b576-0e70c461cc71'
title: 'MSFT\_NetVirtualizationGlobalSettingData class'
---

# MSFT\_NetVirtualizationGlobalSettingData class

The MSFT\_NetVirtualizationGlobalSettingData class represents the global settings and state of the WNV module for Hyper-V Network Virtualization.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetVirtualizationGlobalSettingData : MSFT_NetSettingData
{
  uint8 RoutingRule;
};
```

## Members

The **MSFT\_NetVirtualizationGlobalSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetVirtualizationGlobalSettingData** class has these properties.

<dl> <dt>

**RoutingRule**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The encapsulation type used by the WNV module on this host for forwarding packets to gateways.

<dl> <dt>

<span id="0_"></span>**0** (EncapsulationTypeGre )
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>NetWNV.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetWNV.dll</dt> </dl> |



 

 




