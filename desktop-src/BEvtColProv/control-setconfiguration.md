---
description: Set the new active configuration of the collector.
ms.assetid: 1979e657-a8f3-4eab-991c-a884bde10724
ms.tgt_platform: multiple
title: SetConfiguration method of the Control class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Control.SetConfiguration
api_type: 
- COM
api_location: 
- BEvtCol.exe
---

# SetConfiguration method of the Control class

Set the new active configuration of the collector.

## Syntax


```mof
Uint32 SetConfiguration(
  [in]  string Config,
  [in]  Uint32 OldTimestampLow,
  [in]  Uint32 OldTimestampHigh,
  [out] Uint32 NewTimestampLow,
  [out] Uint32 NewTimestampHigh,
  [out] string ErrorString,
  [out] string WarningString,
  [out] string InfoString,
  [out] uint32 ErrorType
);
```



## Parameters

<dl> <dt>

*Config* \[in\]
</dt> <dd>

The configuration to activate.

</dd> <dt>

*OldTimestampLow* \[in\]
</dt> <dd>

The low-order bits of a timestamp that indicates when the current active configuration was set. Atomicity checking is enabled if this property is not set to 0.

</dd> <dt>

*OldTimestampHigh* \[in\]
</dt> <dd>

The high-order bits of a timestamp that indicates when the current active configuration was set. Atomicity checking is enabled if this property is not set to 0.

</dd> <dt>

*NewTimestampLow* \[out\]
</dt> <dd>

When this method returns, this parameter contains the low-order bits of a timestamp that indicates when the new configuration was set. Atomicity checking is enabled if this property is not set to 0.

</dd> <dt>

*NewTimestampHigh* \[out\]
</dt> <dd>

When this method returns, this parameter contains the high-order bits of the timestamp that indicates when the new configuration was set. Atomicity checking is enabled if this property is not set to 0.

</dd> <dt>

*ErrorString* \[out\]
</dt> <dd>

When this method returns, if there was an error, this parameter contains the error description.

</dd> <dt>

*WarningString* \[out\]
</dt> <dd>

When this method returns, this parameter contains any warnings messages for the operation.

</dd> <dt>

*InfoString* \[out\]
</dt> <dd>

When this method returns, this parameter contains information for the new active configuration.

</dd> <dt>

*ErrorType* \[out\]
</dt> <dd>

When this method returns, if there was an error, this parameter indicates the error type.

<dt>

0
</dt> <dd>

The new configuration is missing.

</dd> <dt>

1
</dt> <dd>

The format of the new configuration is invalid.

</dd> <dt>

2
</dt> <dd>

The new configuration is invalid.

</dd> <dt>

3
</dt> <dd>

There was an error caused by an open socket.

</dd> <dt>

4
</dt> <dd>

There was a file write error.

</dd> <dt>

5
</dt> <dd>

There was an atomicity error.

</dd> </dl> </dd> </dl>

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

 

 




