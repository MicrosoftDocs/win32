---
description: Reset the active configuration of the collector from the later backup file (determined by going forward from the current original timestamp). If the configuration has been undone, this means redoing the undone change.
ms.assetid: bd153ea3-9148-4e65-a44e-3f9fa1855f2f
ms.tgt_platform: multiple
title: Redo method of the Control class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Control.Redo
api_type: 
- COM
api_location: 
- BEvtCol.exe
---

# Redo method of the Control class

Reset the active configuration of the collector from the later backup file (determined by going forward from the current original timestamp). If the configuration has been undone, this means redoing the undone change.

## Syntax


```mof
Uint32 Redo(
  [in]  Uint32 OldTimestampLow,
  [in]  Uint32 OldTimestampHigh,
  [out] Uint32 NewTimestampLow,
  [out] Uint32 NewTimestampHigh,
  [out] Uint32 OriginalTimestampLow,
  [out] Uint32 OriginalTimestampHigh,
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

The timestamp of when the previous configuration was set. If not 0, enables the atomicity check: the new configuration will be applied only if the timestamp of the old configuration matches (i.e. the configuration was not changed in between). This is the low part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

*OldTimestampHigh* \[in\]
</dt> <dd>

The timestamp of when the previous configuration was set. If not 0, enables the atomicity check: the new configuration will be applied only if the timestamp of the old configuration matches (i.e. the configuration was not changed in between). This is the high part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

*NewTimestampLow* \[out\]
</dt> <dd>

The timestamp of when the new configuration was set, if the call succeeds. This is the low part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

*NewTimestampHigh* \[out\]
</dt> <dd>

The timestamp of when the new configuration was set, if the call succeeds. This is the high part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

*OriginalTimestampLow* \[out\]
</dt> <dd>

The original timestamp of when the restored configuration was set for the first time. This is the low part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

*OriginalTimestampHigh* \[out\]
</dt> <dd>

The original timestamp of when the restored configuration was set for the first time. This is the high part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

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
| MOF<br/>                      | <dl> <dt>BootEventCollectorWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>BEvtCol.exe</dt> </dl>               |



## See also

<dl> <dt>

[**Control**](control.md)
</dt> </dl>

 

