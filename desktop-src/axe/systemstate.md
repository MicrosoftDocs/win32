---
title: SystemState class
description: Provides access to specific system configuration settings and the ability to save and restore them.
ms.assetid: F206930D-98C0-40C0-BFA5-CEFAB5FF935E
keywords:
- SystemState class Access Execution Engine
- SystemState class Access Execution Engine , described
topic_type:
- apiref
api_name:
- SystemState
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

# SystemState class

Provides access to specific system configuration settings and the ability to save and restore them.

## When to implement

Never. This is an interface implemented by Axe and provided to the assessment.

## Inheritance

The **SystemState** interface inherits from [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509).

**SystemState** has these types of members:

-   [Methods](#methods)

### Methods

The **SystemState** class has these methods.



| Method                                                                             | Description                                                                                                                                     |
|:-----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**~SystemState**](systemstate--systemstate-destructor.md)                        | Destructor method.<br/>                                                                                                                   |
| [**CheckBoolean**](systemstate-checkboolean.md)                                   | Retrieves whether or not the specified system setting is enabled.<br/>                                                                    |
| [**CheckRegistryValueMultistring**](systemstate-checkregistryvaluemultistring.md) | Retrieves a multi-string (REG\_MULTI\_SZ) value from the registry.<br/>                                                                   |
| [**CheckRegistryValueString**](systemstate-checkregistryvaluestring.md)           | Retrieves an unsigned 64-bit (unsigned REG\_QWORD) value from the registry.<br/>                                                          |
| [**CheckRegistryValueUInt32**](systemstate-checkregistryvalueuint32.md)           | Retrieves an unsigned 32-bit integer (unsigned REG\_DWORD) value from the registry.<br/>                                                  |
| [**CheckRegistryValueUInt64**](systemstate-checkregistryvalueuint64.md)           | Retrieves an unsigned 64-bit (unsigned REG\_QWORD) value from the registry.<br/>                                                          |
| [**RestoreAll**](systemstate-restoreall.md)                                       | Restores all system settings originally modified through [**SetBoolean**](systemstate-setboolean.md) back to their original values.<br/> |
| [**SetBoolean**](systemstate-setboolean.md)                                       | Sets specified system settings.<br/>                                                                                                      |
| [**SetRegistryValueMultistring**](systemstate-setregistryvaluemultistring.md)     | Sets a multi-string (REG\_MULTI\_SZ) value into the registry.<br/>                                                                        |
| [**SetRegistryValueString**](systemstate-setregistryvaluestring.md)               | Sets a string (REG\_SZ) value into the registry.<br/>                                                                                     |
| [**SetRegistryValueUInt32**](systemstate-setregistryvalueuint32.md)               | Sets an unsigned 32-bit integer (unsigned REG\_DWORD) value into the registry. <br/>                                                      |
| [**SetRegistryValueUInt64**](systemstate-setregistryvalueuint64.md)               | Sets an unsigned 64-bit (unsigned REG\_QWORD) value Into the registry.<br/>                                                               |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 





