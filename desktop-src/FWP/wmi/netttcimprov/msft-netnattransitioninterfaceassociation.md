---
description: Describes the association between NAT64 settings and inbound/outbound interfaces.
ms.assetid: 08e13338-f1ab-464f-88cb-cb99e72d1434
title: MSFT\_NetNatTransitionInterfaceAssociation class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetNatTransitionInterfaceAssociation
- MSFT_NetNatTransitionInterfaceAssociation.ManagedElement
- MSFT_NetNatTransitionInterfaceAssociation.SettingData
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetNatTransitionInterfaceAssociation class

Describes the association between NAT64 settings and inbound/outbound interfaces.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetNatTransitionInterfaceAssociation : CIM_ElementSettingData
{
  MSFT_NetAdapter                  REF ManagedElement;
  MSFT_NetNatTransitionSettingData REF SettingData;
};
```

## Members

The **MSFT\_NetNatTransitionInterfaceAssociation** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetNatTransitionInterfaceAssociation** class has these properties.

<dl> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetAdapter**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the network interface by which DNS queries are sent or received.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetNatTransitionSettingData**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Defines the NAT64 settings associated with this interface.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




