---
title: ITSRemoteProgram interface
description: Includes methods to set and retrieve the RemoteApp mode and the start-up parameters for a RemoteApp program, such as the path of the executable file and the working directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c9eec63b-7162-4bf8-b5d5-8cadb971ef98
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- ITSRemoteProgram interface Remote Desktop Services
- ITSRemoteProgram interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- ITSRemoteProgram
api_location:
- MsTscAx.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ITSRemoteProgram interface

Includes methods to set and retrieve the RemoteApp mode and the start-up parameters for a RemoteApp program, such as the path of the executable file and the working directory.

## Members

The **ITSRemoteProgram** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) interface. **ITSRemoteProgram** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ITSRemoteProgram** interface has these methods.



| Method                                                            | Description                                                              |
|:------------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**ServerStartProgram**](itsremoteprogram-serverstartprogram.md) | Specifies a RemoteApp program to start in the remote session.<br/> |



 

### Properties

The **ITSRemoteProgram** interface has these properties.



| Property                                                                   | Access type           | Description                    |
|:---------------------------------------------------------------------------|:----------------------|:-------------------------------|
| [**RemoteProgramMode**](itsremoteprogram-remoteprogrammode.md)<br/> | Read/write<br/> | The RemoteApp mode.<br/> |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_ITSRemoteProgram is defined as FDD029F9-467A-4c49-8529-64B521DBD1B4<br/>    |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx)
</dt> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> </dl>

 

 





