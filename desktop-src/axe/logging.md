---
title: Logging class
description: This interface logs standard ETW events to a pre-configured ETW session maintained by the AXE engine so the solution doesn't have to configure and manage ETW itself.
ms.assetid: 9E147D51-A7B7-468E-9323-B5C96A5B146F
keywords:
- Logging class Access Execution Engine
- Logging class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Logging
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Logging class

This interface logs standard ETW events to a pre-configured ETW session maintained by the AXE engine so the solution doesn't have to configure and manage ETW itself. Use the [**Solution::CreateLogger**](solution-createlogger.md) method to retrieve a **Logging** object with the [AXE Execution Solution API](axe-execution-solution-api.md). Use the [**Support::CreateLogger**](support-createlogger.md) method to retrieve a **Logging** object with the [AXE Execution Assessment API](axe-execution-assessment-api.md).

## When to implement

Never. This is an interface implemented and exposed by the AXE Engine.

## Inheritance

The **Logging** interface inherits from [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509).

**Logging** has these types of members:

-   [Methods](#methods)

### Methods

The **Logging** class has these methods.



| Method                                                       | Description                                                                                                   |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**~Logging**](logging--logging.md)                         | Destructor method.<br/>                                                                                 |
| [**FlushLog**](logging-flushlog.md)                         | Commits all accumulated log messages to disk.<br/>                                                      |
| [**LogBeginOperation**](logging-logbeginoperation.md)       | This method logs a begin event to the AXE engine s pre-configured ETW session.<br/>                     |
| [**LogDiscreteOperation**](logging-logdiscreteoperation.md) | This method logs a discrete event to the AXE engine s pre-configured ETW session.<br/>                  |
| [**LogEndOperation**](logging-logendoperation.md)           | This method logs an end event to the AXE engine s pre-configured ETW session.<br/>                      |
| [**LogErrorCode**](logging-logerrorcode-ovl.md)             | Overloaded. This method logs an error code and custom message to AXE s pre-configured ETW session.<br/> |
| [**LogFileVersion**](logging-logfileversion.md)             | Writes the four-part version number of an executable to Axe s pre-configured ETW file.<br/>             |
| [**LogMessage**](logging-logmessage-ovl.md)                 | Overloaded. Write custom messages to Axe s pre-configured ETW file.<br/>                                |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl> |



 

 





