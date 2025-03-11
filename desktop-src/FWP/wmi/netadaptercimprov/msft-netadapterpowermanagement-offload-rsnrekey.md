---
description: MSFT\_NetAdapterPowerManagement\_Offload\_RsnRekey contains parameters for offloading the RSN Rekey protocol.
ms.assetid: 599814d3-d073-426f-b3da-a72f2ef6468f
title: MSFT\_NetAdapterPowerManagement\_Offload\_RsnRekey class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterPowerManagement_Offload_RsnRekey
- MSFT_NetAdapterPowerManagement_Offload_RsnRekey.KCK
- MSFT_NetAdapterPowerManagement_Offload_RsnRekey.KEK
- MSFT_NetAdapterPowerManagement_Offload_RsnRekey.ReplayCounter
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterPowerManagement\_Offload\_RsnRekey class

MSFT\_NetAdapterPowerManagement\_Offload\_RsnRekey contains parameters for offloading the RSN Rekey protocol.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterPowerManagement_Offload_RsnRekey : MSFT_NetAdapterPowerManagement_Offloa
{
  uint8  KCK[];
  uint8  KEK[];
  uint64 ReplayCounter;
};
```

## Members

The **MSFT\_NetAdapterPowerManagement\_Offload\_RsnRekey** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterPowerManagement\_Offload\_RsnRekey** class has these properties.

<dl> <dt>

**KCK**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the key confirmation key (KCK).

</dd> <dt>

**KEK**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the key encryption key (KEK).

</dd> <dt>

**ReplayCounter**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the replay counter.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




