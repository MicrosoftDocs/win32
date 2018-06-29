---
Description: Restore the active configuration of the collector from the previous backup file (determined by going back from the current original timestamp).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 150fa554-9efd-483e-a177-5fc7766a6a6c
ms.prod: windows-server-dev
ms.technology:
- boot-event-collector
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Undo method of the Control class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Control.Undo
api_type: 
- COM
api_location: 
- BEvtCol.exe
---

# Undo method of the Control class

Restore the active configuration of the collector from the previous backup file (determined by going back from the current original timestamp). If the configuration has been just set, this means undoing that change. The consecutive calls will undo to the earlier and earlier configurations. Returns 1 on success, 0 on error.

## Syntax


```mof
Uint32 Undo(
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

The timestamp of when the previous configuration was set. If not 0, enables the atomicity check: the new configuration will be applied only if the timestamp of the old configuration matches (i.e. the configuration was not changed in between). This is the low part of [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284).

</dd> <dt>

*OldTimestampHigh* \[in\]
</dt> <dd>

The timestamp of when the previous configuration was set. If not 0, enables the atomicity check: the new configuration will be applied only if the timestamp of the old configuration matches (i.e. the configuration was not changed in between). This is the high part of [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284).

</dd> <dt>

*NewTimestampLow* \[out\]
</dt> <dd>

The timestamp of when the new configuration was set, if the call succeeds. This is the low part of [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284).

</dd> <dt>

*NewTimestampHigh* \[out\]
</dt> <dd>

The timestamp of when the new configuration was set, if the call succeeds. This is the high part of [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284).

</dd> <dt>

*OriginalTimestampLow* \[out\]
</dt> <dd>

The original timestamp of when the restored configuration was set for the first time. This is the low part of [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284).

</dd> <dt>

*OriginalTimestampHigh* \[out\]
</dt> <dd>

The original timestamp of when the restored configuration was set for the first time. This is the high part of [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284).

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

The type of the error: note that 0 or absent indicates success.

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



|                                     |                                                                                                      |
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

 

 




