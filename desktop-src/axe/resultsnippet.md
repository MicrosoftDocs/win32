---
title: ResultSnippet class
description: This interface provides the ability to store and query assessment results information.
ms.assetid: B0D6A0DB-CBB5-432A-BBB7-36460944E008
keywords:
- ResultSnippet class Access Execution Engine
- ResultSnippet class Access Execution Engine , described
topic_type:
- apiref
api_name:
- ResultSnippet
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ResultSnippet class

This interface provides the ability to store and query assessment results information.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

## Inheritance

The **ResultSnippet** interface inherits from [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509).

**ResultSnippet** has these types of members:

-   [Methods](#methods)

### Methods

The **ResultSnippet** class has these methods.



| Method                                                             | Description                                                                                                                                                                               |
|:-------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**~ResultSnippet**](resultsnippet--resultsnippet.md)             | Destructor object.<br/>                                                                                                                                                             |
| [**AddError**](resultsnippet-adderror-overl.md)                   | Overloaded. Creates an [**ErrorWarning**](errorwarning.md) error object for use by the **ResultSnippet** object.<br/>                                                              |
| [**AddIteration**](resultsnippet-additeration.md)                 | Creates and returns an [**Iteration**](iteration.md) for use by this **ResultSnippet** object.<br/>                                                                                |
| [**AddLogFile**](resultsnippet-addlogfile.md)                     | Adds a log file to this **ResultSnippet**.<br/>                                                                                                                                     |
| [**AddWarning**](resultsnippet-addwarning-overl.md)               | Overloaded. Creates an [**ErrorWarning**](errorwarning.md) object for use by the **ResultSnippet** object.<br/>                                                                    |
| [**GetErrorsAndWarnings**](resultsnippet-geterrorsandwarnings.md) | Returns an [**ErrorWarningsCollection**](errorwarningcollection.md) object that contains the errors and warnings for this ResultsSnippet.<br/>                                     |
| [**GetIterations**](resultsnippet-getiterations.md)               | Returns a pointer to the [**IterationCollection**](iterationcollection.md) object that contains the [**Iteration**](iteration-struct.md)s for this **ResultSnippet** object.<br/> |
| [**GetLogFiles**](resultsnippet-getlogfiles.md)                   | Returns a [**LogFileCollection**](logfilecollection.md) object that contains the log files for this **ResultSnippet**.<br/>                                                        |
| [**GetXmlText**](resultsnippet-getxmltext.md)                     | Gets the XML text.<br/>                                                                                                                                                             |
| [**Save**](resultsnippet-save.md)                                 | Saves this **ResultSnippet** object to a file.<br/>                                                                                                                                 |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





