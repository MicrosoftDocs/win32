---
title: LogReaderCallbackData structure
description: This structure defines the data from a single event that was logged to an .ETL file.
ms.assetid: 'C27EB327-F7D6-4727-AEF9-56BAF2AD9148'
keywords: ["LogReaderCallbackData structure Access Execution Engine"]
topic_type:
- apiref
api_name:
- LogReaderCallbackData
api_location:
- AxeHosting.h
api_type:
- HeaderDef
---

# LogReaderCallbackData structure

This structure defines the data from a single event that was logged to an .ETL file.

## Syntax


```C++
struct LogReaderCallbackData {
  FILETIME Timestamp;
  LPCWSTR  LogDate;
  LPCWSTR  LogTime;
  LPCWSTR  LogText;
  LPCWSTR  LogError;
};
```



## Members

<dl> <dt>

**Timestamp**
</dt> <dd>

The time when the ETL file started logging information.

</dd> <dt>

**LogDate**
</dt> <dd>

The date the current event was logged.

</dd> <dt>

**LogTime**
</dt> <dd>

The local time the current event was logged.

</dd> <dt>

**LogText**
</dt> <dd>

The text describing the current event.

</dd> <dt>

**LogError**
</dt> <dd>

The error text for any additional error information that was logged for the current event.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





