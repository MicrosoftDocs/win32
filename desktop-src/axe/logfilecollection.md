---
title: LogFileCollection class
description: This interface provides a container object for assessment log files.
ms.assetid: '5ABCF721-1A7C-40FB-9E34-400E600325C3'
keywords: ["LogFileCollection class Access Execution Engine", "LogFileCollection class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- LogFileCollection
api_location:
- AxeCore.dll
api_type:
- COM
---

# LogFileCollection class

This interface provides a container object for assessment log files.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**LogFileCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **LogFileCollection** class has these methods.



| Method                                                             | Description                                                       |
|:-------------------------------------------------------------------|:------------------------------------------------------------------|
| [**~LogFileCollection**](logfilecollection--logfilecollection.md) | Destructor method.<br/>                                     |
| [**AddItem**](logfilecollection-additem.md)                       | Adds a log file to the collection.<br/>                     |
| [**Clear**](logfilecollection-clear.md)                           | Deletes all log files from the collection.<br/>             |
| [**DeleteItem**](logfilecollection-deleteitem.md)                 | Deletes a log file from the collection.<br/>                |
| [**GetCount**](logfilecollection-getcount.md)                     | Gets the count of log files in the collection.<br/>         |
| [**GetItem**](logfilecollection-getitem.md)                       | Returns the file path of a log file in the collection.<br/> |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





