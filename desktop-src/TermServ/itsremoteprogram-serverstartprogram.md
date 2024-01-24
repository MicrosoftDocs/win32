---
title: ITSRemoteProgram ServerStartProgram method
description: Specifies a RemoteApp program to start in the remote session.
ms.assetid: 5fb251bf-4832-4e35-b372-23418c280350
ms.tgt_platform: multiple
keywords:
- ServerStartProgram method Remote Desktop Services
- ServerStartProgram method Remote Desktop Services , ITSRemoteProgram interface
- ITSRemoteProgram interface Remote Desktop Services , ServerStartProgram method
- ServerStartProgram method Remote Desktop Services , ITSRemoteProgram2 interface
- ITSRemoteProgram2 interface Remote Desktop Services , ServerStartProgram method
- ServerStartProgram method Remote Desktop Services , ITSRemoteProgram3 interface
- ITSRemoteProgram3 interface Remote Desktop Services , ServerStartProgram method
topic_type:
- apiref
api_name:
- ITSRemoteProgram.ServerStartProgram
- ITSRemoteProgram2.ServerStartProgram
- ITSRemoteProgram3.ServerStartProgram
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITSRemoteProgram::ServerStartProgram method

Specifies a RemoteApp program to start in the remote session. This function must be invoked on a connected session (after the session connected notification is received at the client). Any number of RemoteApp programs can be started in a session. A RemoteApp session will time out if no RemoteApp program is started in the session within the time-out limit, which is two minutes for Windows Server 2008.

## Syntax


```C++
HRESULT ServerStartProgram(
  [in] BSTR         bstrExecutablePath,
  [in] BSTR         bstrFilePath,
  [in] BSTR         bstrWorkingDirectory,
  [in] VARIANT_BOOL vbExpandEnvVarInWorkingDirectoryOnServer,
  [in] BSTR         bstrArguments,
  [in] VARIANT_BOOL vbExpandEnvVarInArgumentsOnServer
);
```



## Parameters

<dl> <dt>

*bstrExecutablePath* \[in\]
</dt> <dd>

The path of the RemoteApp program executable file on the server.

</dd> <dt>

*bstrFilePath* \[in\]
</dt> <dd>

The path of a file to open on the server through a file association, for example "C:\\\\Documents\\\\MyReport.docx". If you specify *bstrFilePath*, you should not specify the *bstrExecutablePath* parameter, and vice versa. You should only specify one of the parameters.

</dd> <dt>

*bstrWorkingDirectory* \[in\]
</dt> <dd>

The working directory on the server for the RemoteApp program.

</dd> <dt>

*vbExpandEnvVarInWorkingDirectoryOnServer* \[in\]
</dt> <dd>

Indicates whether the server should expand environment variables in the working directory path. Set this parameter to **VARIANT\_TRUE** if the working directory path contains environment variables, or **VARIANT\_FALSE** if the working directory path does not contain environment variables.

</dd> <dt>

*bstrArguments* \[in\]
</dt> <dd>

The command-line arguments for the RemoteApp program that are specified in *bstrExecutablePath*. Set this to **NULL** if *bstrExecutablePath* is not specified.

</dd> <dt>

*vbExpandEnvVarInArgumentsOnServer* \[in\]
</dt> <dd>

Indicates whether the server should expand environment variables in the command-line arguments. Set this parameter to **VARIANT\_TRUE** if the arguments contain environment variables, or **VARIANT\_FALSE** if the arguments do not contain environment variables.

</dd> </dl>

## Return value

Returns **S\_OK** if successful.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_ITSRemoteProgram is defined as FDD029F9-467A-4c49-8529-64B521DBD1B4<br/>    |



## See also

<dl> <dt>

[**ITSRemoteProgram2**](itsremoteprogram2.md)
</dt> <dt>

[**ITSRemoteProgram3**](itsremoteprogram3.md)
</dt> <dt>

[**ITSRemoteProgram**](itsremoteprogram.md)
</dt> </dl>

 

 





