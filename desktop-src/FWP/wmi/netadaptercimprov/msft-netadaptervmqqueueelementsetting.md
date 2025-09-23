---
description: Associates a network adapter with the setting data of its VMQ queues.
ms.assetid: cae3b336-4555-4bbe-8bd2-48eab2427a97
title: MSFT\_NetAdapterVmqQueueElementSetting class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterVmqQueueElementSetting
- MSFT_NetAdapterVmqQueueElementSetting.SettingData
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterVmqQueueElementSetting class

Associates a network adapter with the setting data of its VMQ queues.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterVmqQueueElementSetting : MSFT_NetAdapterElementSettingData
{
  MSFT_NetAdapterVmqQueueSettingData REF SettingData;
};
```

## Members

The **MSFT\_NetAdapterVmqQueueElementSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterVmqQueueElementSetting** class has these properties.

<dl> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetAdapterVmqQueueSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The VMQ Queue setting data for the network adapter.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




