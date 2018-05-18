---
title: MSFT\_DtcAdvancedSettingTask class
description: Manages DTC instance specific properties in the registry.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd96bb979-826d-4fe2-a620-ccd953060e5f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_DtcAdvancedSettingTask class", "MSFT_DtcAdvancedSettingTask class, described"]
topic_type:
- apiref
api_name:
- MSFT_DtcAdvancedSettingTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
---

# MSFT\_DtcAdvancedSettingTask class

Manages DTC instance specific properties in the registry.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcAdvancedSettingTask
{
};
```

## Members

The **MSFT\_DtcAdvancedSettingTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcAdvancedSettingTask** class has these methods.



| Method                                         | Description                                                              |
|:-----------------------------------------------|:-------------------------------------------------------------------------|
| [**Get**](get-msft-dtcadvancedsettingtask.md) | Retrieves a DTC instance specific property from the registry.<br/> |
| [**Set**](set-msft-dtcadvancedsettingtask.md) | Updates a DTC instance specific property in the registry.<br/>     |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Distributed Transaction Coordinator WMI Provider](distributed-transaction-coordinator-wmi-provider-portal.md)
</dt> </dl>

 

 





