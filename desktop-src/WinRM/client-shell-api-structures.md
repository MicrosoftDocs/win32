---
title: Client Shell API Structures and Definitions
description: The following table provides an overview of the structures and other definitions for the Windows Remote Management (WinRM) Client Shell API.
ms.assetid: b7a3c92e-6796-482f-9d70-18a48cce4ad8
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Client Shell API Structures and Definitions

The following table provides an overview of the structures and other definitions for the Windows Remote Management (WinRM) Client Shell API.



| Function                                                                      | Description                                                                                  |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**WSMAN\_SHELL\_COMPLETION\_FUNCTION**](/windows/win32/api/wsman/nc-wsman-wsman_shell_completion_function) | The callback function that is called for shell operations, which result in a remote request. |



 



| Structure                                                                      | Description                                                                                                                                 |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSMAN\_AUTHENTICATION\_CREDENTIALS**](/windows/desktop/api/Wsman/ns-wsman-wsman_authentication_credentials) | Defines the authentication method and the credentials used for server or proxy authentication.                                              |
| [**WSMAN\_DATA**](/windows/desktop/api/Wsman/ns-wsman-wsman_data)                                              | Stores inbound and outbound data used in the WinRM API.                                                                                     |
| [**WSMAN\_DATA\_BINARY**](/windows/desktop/api/Wsman/ns-wsman-wsman_data_binary)                               | Stores binary data for use with various WinRM API functions.                                                                                |
| [**WSMAN\_DATA\_TEXT**](/windows/desktop/api/Wsman/ns-wsman-wsman_data_text)                                   | Stores text-based data for use with various WinRM API functions.                                                                            |
| [**WSMAN\_ENVIRONMENT\_VARIABLE**](/windows/desktop/api/Wsman/ns-wsman-wsman_environment_variable)             | Defines an individual environment variable by using a name and value pair.                                                                  |
| [**WSMAN\_ENVIRONMENT\_VARIABLE\_SET**](/windows/desktop/api/Wsman/ns-wsman-wsman_environment_variable_set)    | Defines an array of environment variables.                                                                                                  |
| [**WSMAN\_ERROR**](/windows/desktop/api/Wsman/ns-wsman-wsman_error)                                     | Contains error information.                                                                                                                 |
| [**WSMAN\_KEY**](/windows/desktop/api/Wsman/ns-wsman-wsman_key)                                                | Represents a key and value pair within a selector set, and is used to identify a particular resource.                                       |
| [**WSMAN\_OPTION**](/windows/desktop/api/Wsman/ns-wsman-wsman_option)                                          | Represents a specific option name and value pair.                                                                                           |
| [**WSMAN\_OPTION\_SET**](/windows/desktop/api/Wsman/ns-wsman-wsman_option_set)                                 | Represents a set of options.                                                                                                                |
| [**WSMAN\_PROXY\_INFO**](/windows/desktop/api/Wsman/ns-wsman-wsman_proxy_info)                                 | Sets the proxy information for each session.                                                                                                |
| [**WSMAN\_RECEIVE\_DATA\_RESULT**](/windows/desktop/api/Wsman/ns-wsman-wsman_receive_data_result)              | Represents the output data received from the [**WSManReceiveShellOutput**](/windows/desktop/api/Wsman/nf-wsman-wsmanreceiveshelloutput) API.                                |
| [**WSMAN\_RESPONSE\_DATA**](/windows/desktop/api/Wsman/ns-wsman-wsman_response_data)                           | Represents the output data received from a [**WSMan**](wsman.md) operation.                                                                |
| [**WSMAN\_SELECTOR\_SET**](/windows/desktop/api/Wsman/ns-wsman-wsman_selector_set)                             | Defines a set of keys that represent the identity of a resource.                                                                            |
| [**WSMAN\_SHELL\_ASYNC**](/windows/desktop/api/Wsman/ns-wsman-wsman_shell_async)                               | Defines an asynchronous structure that is passed to all shell operations.                                                                   |
| [**WSMAN\_SHELL\_DISCONNECT\_INFO**](/windows/desktop/api/Wsman/ns-wsman-wsman_shell_disconnect_info)          | TBD                                                                                                                                         |
| [**WSMAN\_SHELL\_STARTUP\_INFO**](/windows/desktop/api/Wsman/ns-wsman-wsman_shell_startup_info_v10)                | Stores all of the shell-specific data that is needed to create a shell using the [**WSManCreateShell**](/windows/desktop/api/Wsman/nf-wsman-wsmancreateshell) plug-in call. |
| [**WSMAN\_STREAM\_ID\_SET**](/windows/desktop/api/Wsman/ns-wsman-wsman_stream_id_set)                          | Lists all the streams that are used for either input or output for the shell and commands.                                                  |
| [**WSMAN\_USERNAME\_PASSWORD\_CREDS**](/windows/desktop/api/Wsman/ns-wsman-wsman_username_password_creds)      | Defines the credentials used for authentication.                                                                                            |



 

 

 