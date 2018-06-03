---
title: System.Environment object
description: Defines the properties and methods for determining system and user environment variables.
ms.assetid: 4ec38f57-39ff-44e2-94c7-63207c9f27e7
keywords:
- System.Environment object Windows Sidebar
- System.Environment object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Environment
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# System.Environment object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties and methods for determining system and user environment variables.

## Members

The **System.Environment** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **System.Environment** object has these methods.



| Method                                                                      | Description                                                                      |
|:----------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**getEnvironmentVariable**](system-environment-getenvironmentvariable.md) | Retrieves the value of a **system** or **user** environment variable.<br/> |



 

### Properties

The **System.Environment** object has these properties.



| Property                                                         | Access type          | Description                                     |
|:-----------------------------------------------------------------|:---------------------|:------------------------------------------------|
| [**machineName**](system-environment-machinename.md)<br/> | Read-only<br/> | Gets the name of the local computer.<br/> |



 

## Remarks

System environment variables define the behavior of the global operating system environment. Local environment variables define the behavior of the environment of the current user session.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





