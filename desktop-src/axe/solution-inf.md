---
title: Solution class
description: Acts as an interface factory and provides access to data applicable to the overall AXE session. This interface is the core of the AXE functionality for a solution application.
ms.assetid: '58C4668E-B8E5-4ACF-AE72-63EC348A07E3'
keywords: ["Solution class Access Execution Engine", "Solution class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- Solution
api_location:
- AxeCore.dll
api_type:
- COM
---

# Solution class

Acts as an interface factory and provides access to data applicable to the overall AXE session. This interface is the core of the AXE functionality for a solution application.

## When to implement

Never. This is an exposed interface that is already implemented.

**Solution** has these types of members:

-   [Methods](#methods)

### Methods

The **Solution** class has these methods.



| Method                                                  | Description                                                                                                |
|:--------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**CreateEngine**](solution-createengine.md)           | Create an [**Engine**](engine-if.md) object for running AXE jobs.<br/>                              |
| [**CreateJob**](solution-createjob-ovl.md)             | Overloaded. Load a job from an XML file.<br/>                                                        |
| [**CreateLogger**](solution-createlogger.md)           | Creates a [**Logging**](logging.md) object to write information into AXE’s event logging file.<br/> |
| [**CreateResults**](solution-createresults.md)         | Overloaded. Create a [**JobResults**](jobresults.md) object from a results file.<br/>               |
| [**GetErrorText**](solution-geterrortext.md)           | Retrieve the text for a specified error code.<br/>                                                   |
| [**GetSessionFolder**](solution-getsessionfolder.md)   | Retrieve the folder that contains the Axe engine state files and debugging logs.<br/>                |
| [**GetSessionLogFile**](solution-getsessionlogfile.md) | Retrieve the name of the debugging log files that contain a record of the Axe engine execution.<br/> |
| [**ReadLogFile**](solution-readlogfile.md)             | Read a log file.<br/>                                                                                |



 

## Remarks

Managed code uses an object of the [**Solution**](https://msdn.microsoft.com/library/windows/desktop/hh802973) class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>AxeCore.lib</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Execution Solution Interfaces**](execution-solution-interfaces.md)
</dt> </dl>

 

 





