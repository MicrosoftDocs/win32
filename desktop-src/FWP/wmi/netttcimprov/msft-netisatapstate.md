---
description: Represents per-interface ISATAP Configuration settings.
ms.assetid: 0ff50d57-6442-4e54-bd62-d2dcee711f8a
title: MSFT\_NetISATAPState class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetISATAPState
- MSFT_NetISATAPState.ManagedElement
- MSFT_NetISATAPState.SettingData
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetISATAPState class

Represents per-interface ISATAP Configuration settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetISATAPState : CIM_ElementSettingData
{
  MSFT_NetIPInterface         REF ManagedElement;
  MSFT_NetISATAPConfiguration REF SettingData;
};
```

## Members

The **MSFT\_NetISATAPState** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetISATAPState** class has these properties.

<dl> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetIPInterface**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the ISATAP tunnel interface.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetISATAPConfiguration**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the ISATAP global settings associated with this interface.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




