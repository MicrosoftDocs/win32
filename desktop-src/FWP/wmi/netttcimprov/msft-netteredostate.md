---
description: Represents per-interface Teredo Configuration settings.
ms.assetid: a19722da-ddfe-4a38-9703-0507dcc6f184
title: MSFT\_NetTeredoState class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetTeredoState
- MSFT_NetTeredoState.ManagedElement
- MSFT_NetTeredoState.SettingData
- MSFT_NetTeredoState.State
- MSFT_NetTeredoState.Error
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetTeredoState class

Represents per-interface Teredo Configuration settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetTeredoState : CIM_ElementSettingData
{
  MSFT_NetIPInterface         REF ManagedElement;
  MSFT_NetTeredoConfiguration REF SettingData;
  string                          State;
  string                          Error;
};
```

## Members

The **MSFT\_NetTeredoState** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetTeredoState** class has these properties.

<dl> <dt>

**Error**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the error of the Teredo interface.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetIPInterface**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the Teredo tunnel interface.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetTeredoConfiguration**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the Teredo global settings associated with this interface.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the state of the Teredo interface.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




