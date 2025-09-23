---
description: Associates a network adapter with its Encapsulation Offload data.
ms.assetid: 6b04b889-94b1-4436-a781-638bc63811e5
title: MSFT\_NetAdapterEncapsulatedPacketTaskOffloadElementSetting class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadElementSetting
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadElementSetting.SettingData
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterEncapsulatedPacketTaskOffloadElementSetting class

Associates a network adapter with its Encapsulation Offload data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterEncapsulatedPacketTaskOffloadElementSetting : MSFT_NetAdapterElementSet
{
  MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData REF SettingData;
};
```

## Members

The **MSFT\_NetAdapterEncapsulatedPacketTaskOffloadElementSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterEncapsulatedPacketTaskOffloadElementSetting** class has these properties.

<dl> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetAdapterEncapsulatedPacketTaskOffloadSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The Encapsulated Packet Task Offload setting data for network adapter.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




