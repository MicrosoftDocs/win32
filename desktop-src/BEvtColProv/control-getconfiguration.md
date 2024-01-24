---
description: Read the active configuration of the collector.
ms.assetid: ea26142d-5dcd-466d-b9df-5349f58a190f
ms.tgt_platform: multiple
title: GetConfiguration method of the Control class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Control.GetConfiguration
api_type: 
- COM
api_location: 
- BEvtCol.exe
---

# GetConfiguration method of the Control class

Read the active configuration of the collector.

## Syntax


```mof
Uint32 GetConfiguration(
  [out] Uint32 TimestampLow,
  [out] Uint32 TimestampHigh
);
```



## Parameters

<dl> <dt>

*TimestampLow* \[out\]
</dt> <dd>

When this method returns, this parameter contains the low-order bits of a timestamp that indicates when the configuration was set.

</dd> <dt>

*TimestampHigh* \[out\]
</dt> <dd>

When this method returns, this parameter contains the high-order bits of a timestamp that indicates when the configuration was set.

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

 

 




