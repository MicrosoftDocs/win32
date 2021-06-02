---
description: Returns the list of the saved backup configuration files that can be restored.
ms.assetid: 9487c50e-ef3b-425f-92ef-0614290e9af4
ms.tgt_platform: multiple
title: ListBackups method of the Control class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Control.ListBackups
api_type: 
- COM
api_location: 
- BEvtCol.exe
---

# ListBackups method of the Control class

Returns the list of the saved backup configuration files that can be restored.

## Syntax


```mof
void ListBackups(
  [out] Uint32 OriginalTimestampLow,
  [out] Uint32 OriginalTimestampHigh,
  [out] string Files[],
  [out] Uint32 FilesTimestampLow[],
  [out] Uint32 FilesTimestampHigh[]
);
```



## Parameters

<dl> <dt>

*OriginalTimestampLow* \[out\]
</dt> <dd>

The timestamp of when the current configuration was set (if restored from backup, will contain the original timestamp). This is the low part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

*OriginalTimestampHigh* \[out\]
</dt> <dd>

The timestamp of when the current configuration was set (if restored from backup, will contain the original timestamp). This is the high part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

*Files* \[out\]
</dt> <dd>

The list of available backup files, in order from the newest to the oldest.

</dd> <dt>

*FilesTimestampLow* \[out\]
</dt> <dd>

For each backup file, the timestamp of when its configuration was set. This is the low part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

*FilesTimestampHigh* \[out\]
</dt> <dd>

For each backup file, the timestamp of when its configuration was set. This is the high part of [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime).

</dd> </dl>

## Return value

This method does not return a value.

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

 

