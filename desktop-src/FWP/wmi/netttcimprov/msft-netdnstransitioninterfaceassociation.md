---
description: Describes the association between DNS64 settings and accept/send interfaces.
ms.assetid: 32403f94-8b69-40cc-9b3e-1e8d0fcb9e2f
title: MSFT\_NetDnsTransitionInterfaceAssociation class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetDnsTransitionInterfaceAssociation
- MSFT_NetDnsTransitionInterfaceAssociation.ManagedElement
- MSFT_NetDnsTransitionInterfaceAssociation.SettingData
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetDnsTransitionInterfaceAssociation class

Describes the association between DNS64 settings and accept/send interfaces.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetDnsTransitionInterfaceAssociation : CIM_ElementSettingData
{
  MSFT_NetAdapter                  REF ManagedElement;
  MSFT_NetDnsTransitionSettingData REF SettingData;
};
```

## Members

The **MSFT\_NetDnsTransitionInterfaceAssociation** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetDnsTransitionInterfaceAssociation** class has these properties.

<dl> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetAdapter**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the network interface on which DNS queries are sent or received.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetDnsTransitionSettingData**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the DNS64 settings associated with this interface.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




