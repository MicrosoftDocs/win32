---
title: System.Environment.getEnvironmentVariable method
description: Retrieves the value of a system or user environment variable.
ms.assetid: 'd61555d5-3f41-4009-b295-398c12a991f1'
keywords: ["getEnvironmentVariable method Windows Sidebar", "getEnvironmentVariable method Windows Sidebar , System.Environment object", "System.Environment object Windows Sidebar , getEnvironmentVariable method"]
topic_type:
- apiref
api_name:
- System.Environment.getEnvironmentVariable
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Environment.getEnvironmentVariable method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Retrieves the value of a **system** or **user** environment variable.

## Syntax


```JScript
strRetVal = System.Environment.getEnvironmentVariable(
  strEnvVar
)
```



## Parameters

<dl> <dt>

*strEnvVar* \[in\]
</dt> <dd>

**String** that specifies the name of an environment variable.

</dd> </dl>

## Return value

The value of the specified environment variable.

## Remarks

System environment variables define the behavior of the global operating system environment. Local environment variables define the behavior of the environment of the current user session.

The following is a selection of valid environment variables:

-   ALLUSERSPROFILE=C:\\ProgramData
-   APPDATA=C:\\Users\\**user**\\AppData\\Roaming
-   HOMEPATH=\\Users\\**user**
-   LOCALAPPDATA=C:\\Users\\**user**\\AppData\\Local
-   PROGRAMDATA=C:\\ProgramData
-   PUBLIC=C:\\Users\\Public
-   TEMP=C:\\Users\\**user**\\AppData\\Local\\Temp
-   TMP=C:\\Users\\**user**\\AppData\\Local\\Temp
-   USERPROFILE=C:\\Users\\**user**

## Examples

The following example demonstrates how to retrieve the value of an environment variable.


```JScript
// --------------------------------------------------------------------
// Set the text of the gadget based on the environment variable.
// --------------------------------------------------------------------
function SetContentText()
{
    var environmentVariableValue = 
        System.Environment.getEnvironmentVariable(environmentVariableName);
    
    if (environmentVariableValue)
    {
        gadgetContent.innerHTML = environmentVariableName + 
            ": " + environmentVariableValue;
    }
    else
    {
        gadgetContent.innerHTML = defaultText;
    }
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**System.Environment**](system-environment.md)
</dt> <dt>

[**machineName**](system-environment-machinename.md)
</dt> </dl>

 

 





