---
description: If the current configuration is a result of the Undo/Redo/Restore, marks it as if it has been set explicitly, so that the history will preserve the time when it was set, and a backup file will be created for it on the next configuration change.
ms.assetid: 1b3d398a-c7f9-4e21-9e43-1245a13fe564
ms.tgt_platform: multiple
title: Checkpoint method of the Control class (Srrestoreptapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Control.Checkpoint
api_type: 
- COM
api_location: 
- BEvtCol.exe
---

# Checkpoint method of the Control class

If the current configuration is a result of the Undo/Redo/Restore, marks it as if it has been set explicitly, so that the history will preserve the time when it was set, and a backup file will be created for it on the next configuration change. If the current configuration was already set explicitly, has no effect.

## Syntax


```mof
Uint32 Checkpoint(
  [in]  Uint32 OldTimestampLow,
  [in]  Uint32 OldTimestampHigh,
  [out] string ErrorString,
  [out] string WarningString,
  [out] string InfoString,
  [out] uint32 ErrorType
);
```



## Parameters

<dl> <dt>

*OldTimestampLow* \[in\]
</dt> <dd>

The timestamp of when the current configuration was set. If not 0, enables the atomicity check: the action will be applied only if the timestamp of the old configuration matches (i.e. the configuration was not changed in between). This is the low part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

*OldTimestampHigh* \[in\]
</dt> <dd>

The timestamp of when the current configuration was set. If not 0, enables the atomicity check: the action will be applied only if the timestamp of the old configuration matches (i.e. the configuration was not changed in between). This is the high part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

*ErrorString* \[out\]
</dt> <dd>

The text string with explanation of the error.

</dd> <dt>

*WarningString* \[out\]
</dt> <dd>

The text string with warnings.

</dd> <dt>

*InfoString* \[out\]
</dt> <dd>

The text string with information about the configuration.

</dd> <dt>

*ErrorType* \[out\]
</dt> <dd>

The type of the error. Note that 0 or absent indicates success.

<dt>

0
</dt> <dd>

Success.

</dd> <dt>

1
</dt> <dd>

bad argument format

</dd> <dt>

2
</dt> <dd>

bad argument value

</dd> <dt>

3
</dt> <dd>

resource (socket) open error

</dd> <dt>

4
</dt> <dd>

persistence (file write) error

</dd> <dt>

5
</dt> <dd>

atomicity error (the old timestamp didn't match)

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
| Header<br/>                   | <dl> <dt>Srrestoreptapi.h</dt> </dl>          |
| MOF<br/>                      | <dl> <dt>BootEventCollectorWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>BEvtCol.exe</dt> </dl>               |



## See also

<dl> <dt>

[**Control**](control.md)
</dt> </dl>

 

