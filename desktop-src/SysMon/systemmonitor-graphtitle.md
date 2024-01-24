---
title: SystemMonitor.GraphTitle property
description: Retrieves or sets the title of the graph.
ms.assetid: 10a91b38-6963-4ef6-8b4f-9ecd1341f471
keywords:
- GraphTitle property SysMon
- GraphTitle property SysMon , SystemMonitor class
- SystemMonitor class SysMon , GraphTitle property
topic_type:
- apiref
api_name:
- SystemMonitor.GraphTitle
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.GraphTitle property

Retrieves or sets the title of the graph.

This property is read-only.

## Syntax


```VB
Property GraphTitle As String
```



## Property value

Title of the graph. The maximum length of the title is 128 characters. If the title exceeds 128 characters, the title is truncated.

**Windows XP and Windows 2000:** There is no limit to the length of the title.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> </dl>

 

 





