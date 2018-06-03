---
title: MSFT\_DtcAdvancedHostSettingTask class
description: Manages DTC host level properties in the registry.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0c98f0b1-c448-4dbf-a019-5283917aa70c
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DtcAdvancedHostSettingTask class
- MSFT_DtcAdvancedHostSettingTask class, described
topic_type:
- apiref
api_name:
- MSFT_DtcAdvancedHostSettingTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DtcAdvancedHostSettingTask class

Manages DTC host level properties in the registry.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcAdvancedHostSettingTask
{
};
```

## Members

The **MSFT\_DtcAdvancedHostSettingTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcAdvancedHostSettingTask** class has these methods.



| Method                                             | Description                                                       |
|:---------------------------------------------------|:------------------------------------------------------------------|
| [**Get**](get-msft-dtcadvancedhostsettingtask.md) | Retrieves a DTC host level property from the registry.<br/> |
| [**Set**](set-msft-dtcadvancedhostsettingtask.md) | Updates a DTC host level property in the registry.<br/>     |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Distributed Transaction Coordinator WMI Provider](distributed-transaction-coordinator-wmi-provider-portal.md)
</dt> </dl>

 

 





