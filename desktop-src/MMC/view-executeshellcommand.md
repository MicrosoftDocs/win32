---
title: View ExecuteShellCommand method
description: The ExecuteShellCommand method runs a command in a window. After this method successfully starts the command in a separate process, it returns immediately (it does not wait for the command to complete).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e786df29-b9ad-4cdd-81b1-99fe73a551fb
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ExecuteShellCommand method MMC
- ExecuteShellCommand method MMC , View object
- View object MMC , ExecuteShellCommand method
- ExecuteShellCommand method MMC , View interface
- View interface MMC , ExecuteShellCommand method
topic_type:
- apiref
api_name:
- View.ExecuteShellCommand
- View.ExecuteShellCommand
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::ExecuteShellCommand method

The **ExecuteShellCommand** method runs a command in a window. After this method successfully starts the command in a separate process, it returns immediately (it does not wait for the command to complete).

## Syntax


```VB
View.ExecuteShellCommand( _
  ByVal Command As String, _
  ByVal Directory As String, _
  ByVal Parameters As String, _
  ByVal WindowState As String _
)
```



## Parameters

<dl> <dt>

*Command* 
</dt> <dd>

A value that specifies the command to execute. A fully qualified path may be specified. Any environment variables (such as "%windir%") contained in *Command* will be expanded.

</dd> <dt>

*Directory* 
</dt> <dd>

A value that specifies the name of the working directory. Any environment variables contained in *Directory* will be expanded. If *Directory* is an empty string, the current directory is used as the working directory.

</dd> <dt>

*Parameters* 
</dt> <dd>

A value that specifies parameters, if any, to be used by *Command*; the parameters must be separated by spaces. For example, specifying *Parameters* as "Param1 Param2" results in *Command* receiving Param1 and Param2 as parameters. If an individual parameter is required to be in double quotation marks, use the proper technique for your programming language. For example, in Microsoft Visual Basic, specifying *Parameters* as "Param1 ""This is Param2""" results in *Command* receiving Param1 and "This is Param2" as parameters.

</dd> <dt>

*WindowState* 
</dt> <dd>

A value that specifies the state for the window. This value can be one of the following string values or an empty string. If it's an empty string, it defaults to "Restored".

<dt>

<span id="_Maximized_"></span><span id="_maximized_"></span><span id="_MAXIMIZED_"></span>

<span id="_Maximized_"></span><span id="_maximized_"></span><span id="_MAXIMIZED_"></span>**"Maximized"**


</dt> <dd>

The command executes in a maximized window.

</dd> <dt>

<span id="_Minimized_"></span><span id="_minimized_"></span><span id="_MINIMIZED_"></span>

<span id="_Minimized_"></span><span id="_minimized_"></span><span id="_MINIMIZED_"></span>**"Minimized"**


</dt> <dd>

The command executes in a minimized window.

</dd> <dt>

<span id="_Restored_"></span><span id="_restored_"></span><span id="_RESTORED_"></span>

<span id="_Restored_"></span><span id="_restored_"></span><span id="_RESTORED_"></span>**"Restored"**


</dt> <dd>

The command executes in a restored, or normal, window.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



 

 





