---
title: Client Shell API Structures and Definitions
description: The following table provides an overview of the structures and other definitions for the Windows Remote Management (WinRM) Client Shell API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b7a3c92e-6796-482f-9d70-18a48cce4ad8
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Client Shell API Structures and Definitions

The following table provides an overview of the structures and other definitions for the Windows Remote Management (WinRM) Client Shell API.



| Function                                                                      | Description                                                                                  |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**WSMAN\_SHELL\_COMPLETION\_FUNCTION**](/windows/win32/Wsman/nc-wsman-wsman_shell_completion_function?branch=master) | The callback function that is called for shell operations, which result in a remote request. |



 



| Structure                                                                      | Description                                                                                                                                 |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSMAN\_AUTHENTICATION\_CREDENTIALS**](/windows/win32/Wsman/ns-wsman-_wsman_authentication_credentials?branch=master) | Defines the authentication method and the credentials used for server or proxy authentication.                                              |
| [**WSMAN\_DATA**](/windows/win32/Wsman/ns-wsman-_wsman_data?branch=master)                                              | Stores inbound and outbound data used in the WinRM API.                                                                                     |
| [**WSMAN\_DATA\_BINARY**](/windows/win32/Wsman/ns-wsman-_wsman_data_binary?branch=master)                               | Stores binary data for use with various WinRM API functions.                                                                                |
| [**WSMAN\_DATA\_TEXT**](/windows/win32/Wsman/ns-wsman-_wsman_data_text?branch=master)                                   | Stores text-based data for use with various WinRM API functions.                                                                            |
| [**WSMAN\_ENVIRONMENT\_VARIABLE**](/windows/win32/Wsman/ns-wsman-_wsman_environment_variable?branch=master)             | Defines an individual environment variable by using a name and value pair.                                                                  |
| [**WSMAN\_ENVIRONMENT\_VARIABLE\_SET**](/windows/win32/Wsman/ns-wsman-_wsman_environment_variable_set?branch=master)    | Defines an array of environment variables.                                                                                                  |
| [**WSMAN\_ERROR**](/windows/win32/Wsman/ns-wsman-_wsman_error?branch=master)                                     | Contains error information.                                                                                                                 |
| [**WSMAN\_KEY**](/windows/win32/Wsman/ns-wsman-_wsman_key?branch=master)                                                | Represents a key and value pair within a selector set, and is used to identify a particular resource.                                       |
| [**WSMAN\_OPTION**](/windows/win32/Wsman/ns-wsman-_wsman_option?branch=master)                                          | Represents a specific option name and value pair.                                                                                           |
| [**WSMAN\_OPTION\_SET**](/windows/win32/Wsman/ns-wsman-_wsman_option_set?branch=master)                                 | Represents a set of options.                                                                                                                |
| [**WSMAN\_PROXY\_INFO**](/windows/win32/Wsman/ns-wsman-_wsman_proxy_info?branch=master)                                 | Sets the proxy information for each session.                                                                                                |
| [**WSMAN\_RECEIVE\_DATA\_RESULT**](/windows/win32/Wsman/ns-wsman-_wsman_receive_data_result?branch=master)              | Represents the output data received from the [**WSManReceiveShellOutput**](/windows/win32/Wsman/nf-wsman-wsmanreceiveshelloutput?branch=master) API.                                |
| [**WSMAN\_RESPONSE\_DATA**](/windows/win32/Wsman/ns-wsman-_wsman_response_data?branch=master)                           | Represents the output data received from a [**WSMan**](wsman.md) operation.                                                                |
| [**WSMAN\_SELECTOR\_SET**](/windows/win32/Wsman/ns-wsman-_wsman_selector_set?branch=master)                             | Defines a set of keys that represent the identity of a resource.                                                                            |
| [**WSMAN\_SHELL\_ASYNC**](/windows/win32/Wsman/ns-wsman-_wsman_shell_async?branch=master)                               | Defines an asynchronous structure that is passed to all shell operations.                                                                   |
| [**WSMAN\_SHELL\_DISCONNECT\_INFO**](/windows/win32/Wsman/ns-wsman-_wsman_shell_disconnect_info?branch=master)          | TBD                                                                                                                                         |
| [**WSMAN\_SHELL\_STARTUP\_INFO**](/windows/win32/Wsman/ns-wsman-_wsman_shell_startup_info_v10?branch=master)                | Stores all of the shell-specific data that is needed to create a shell using the [**WSManCreateShell**](/windows/win32/Wsman/nf-wsman-wsmancreateshell?branch=master) plug-in call. |
| [**WSMAN\_STREAM\_ID\_SET**](/windows/win32/Wsman/ns-wsman-_wsman_stream_id_set?branch=master)                          | Lists all the streams that are used for either input or output for the shell and commands.                                                  |
| [**WSMAN\_USERNAME\_PASSWORD\_CREDS**](/windows/win32/Wsman/ns-wsman-_wsman_username_password_creds?branch=master)      | Defines the credentials used for authentication.                                                                                            |



 

 

 




