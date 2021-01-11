---
description: Compare the argument with the active configuration of the collector.
ms.assetid: 8decb674-c905-4eb6-9f78-7bc7b99db908
ms.tgt_platform: multiple
title: IsConfigurationEqual method of the Control class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Control.IsConfigurationEqual
api_type: 
- COM
api_location: 
- BEvtCol.exe
---

# IsConfigurationEqual method of the Control class

Compare the argument with the active configuration of the collector.

## Syntax


```mof
Uint32 IsConfigurationEqual(
  [in] string Config
);
```



## Parameters

<dl> <dt>

*Config* \[in\]
</dt> <dd>

The configuration to compare to the active configuration.

</dd> </dl>

## Return value

<dl> <dt>


</dt> <dd>

0

Failure

</dd> <dt>


</dt> <dd>

1

Success

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\BootEventCollector<br/>                                              |
| MOF<br/>                      | <dl> <dt>BootEventCollectorWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>BEvtCol.exe</dt> </dl>               |



## See also

<dl> <dt>

[**Control**](control.md)
</dt> </dl>

 

 




