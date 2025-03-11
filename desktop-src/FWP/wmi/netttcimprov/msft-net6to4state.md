---
description: Represents per-interface 6to4 Configuration settings.
ms.assetid: 744d28d6-459c-4d98-8132-eec52a226613
title: MSFT\_Net6to4State class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_Net6to4State
- MSFT_Net6to4State.ManagedElement
- MSFT_Net6to4State.SettingData
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_Net6to4State class

Represents per-interface 6to4 Configuration settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_Net6to4State : CIM_ElementSettingData
{
  MSFT_NetIPInterface       REF ManagedElement;
  MSFT_Net6to4Configuration REF SettingData;
};
```

## Members

The **MSFT\_Net6to4State** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_Net6to4State** class has these properties.

<dl> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetIPInterface**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the 6to4 tunnel interface.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_Net6to4Configuration**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the 6to4 global settings associated with the interface.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




