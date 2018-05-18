---
title: Client Shell API Structures and Definitions
description: The following table provides an overview of the structures and other definitions for the Windows Remote Management (WinRM) Client Shell API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b7a3c92e-6796-482f-9d70-18a48cce4ad8'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-remote-management'
ms.tgt_platform: multiple
---

# Client Shell API Structures and Definitions

The following table provides an overview of the structures and other definitions for the Windows Remote Management (WinRM) Client Shell API.



| Function                                                                      | Description                                                                                  |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**WSMAN\_SHELL\_COMPLETION\_FUNCTION**](wsman-shell-completion-function.md) | The callback function that is called for shell operations, which result in a remote request. |



 



| Structure                                                                      | Description                                                                                                                                 |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSMAN\_AUTHENTICATION\_CREDENTIALS**](wsman-authentication-credentials.md) | Defines the authentication method and the credentials used for server or proxy authentication.                                              |
| [**WSMAN\_DATA**](wsman-data.md)                                              | Stores inbound and outbound data used in the WinRM API.                                                                                     |
| [**WSMAN\_DATA\_BINARY**](wsman-data-binary.md)                               | Stores binary data for use with various WinRM API functions.                                                                                |
| [**WSMAN\_DATA\_TEXT**](wsman-data-text.md)                                   | Stores text-based data for use with various WinRM API functions.                                                                            |
| [**WSMAN\_ENVIRONMENT\_VARIABLE**](wsman-environment-variable.md)             | Defines an individual environment variable by using a name and value pair.                                                                  |
| [**WSMAN\_ENVIRONMENT\_VARIABLE\_SET**](wsman-environment-variable-set.md)    | Defines an array of environment variables.                                                                                                  |
| [**WSMAN\_ERROR**](wsman-error-struct.md)                                     | Contains error information.                                                                                                                 |
| [**WSMAN\_KEY**](wsman-key.md)                                                | Represents a key and value pair within a selector set, and is used to identify a particular resource.                                       |
| [**WSMAN\_OPTION**](wsman-option.md)                                          | Represents a specific option name and value pair.                                                                                           |
| [**WSMAN\_OPTION\_SET**](wsman-option-set.md)                                 | Represents a set of options.                                                                                                                |
| [**WSMAN\_PROXY\_INFO**](wsman-proxy-info.md)                                 | Sets the proxy information for each session.                                                                                                |
| [**WSMAN\_RECEIVE\_DATA\_RESULT**](wsman-receive-data-result.md)              | Represents the output data received from the [**WSManReceiveShellOutput**](wsmanreceiveshelloutput.md) API.                                |
| [**WSMAN\_RESPONSE\_DATA**](wsman-response-data.md)                           | Represents the output data received from a [**WSMan**](wsman.md) operation.                                                                |
| [**WSMAN\_SELECTOR\_SET**](wsman-selector-set.md)                             | Defines a set of keys that represent the identity of a resource.                                                                            |
| [**WSMAN\_SHELL\_ASYNC**](wsman-shell-async.md)                               | Defines an asynchronous structure that is passed to all shell operations.                                                                   |
| [**WSMAN\_SHELL\_DISCONNECT\_INFO**](wsman-shell-disconnect-info.md)          | TBD                                                                                                                                         |
| [**WSMAN\_SHELL\_STARTUP\_INFO**](wsman-shell-startup-info.md)                | Stores all of the shell-specific data that is needed to create a shell using the [**WSManCreateShell**](wsmancreateshell.md) plug-in call. |
| [**WSMAN\_STREAM\_ID\_SET**](wsman-stream-id-set.md)                          | Lists all the streams that are used for either input or output for the shell and commands.                                                  |
| [**WSMAN\_USERNAME\_PASSWORD\_CREDS**](wsman-username-password-creds.md)      | Defines the credentials used for authentication.                                                                                            |



 

 

 




