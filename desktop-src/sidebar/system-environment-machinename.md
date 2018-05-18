---
title: System.Environment.machineName property
description: Gets the name of the local computer.
ms.assetid: '8e3b2103-942a-4d47-ad54-f181ee7866e1'
keywords: ["machineName property Windows Sidebar", "machineName property Windows Sidebar , System.Environment object", "System.Environment object Windows Sidebar , machineName property"]
topic_type:
- apiref
api_name:
- System.Environment.machineName
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Environment.machineName property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the name of the local computer.

This property is read-only.

## Syntax


```JScript
strmachineName = System.Environment.machineName
```



## Property value

A **String** that receives the name of the local computer.

## Remarks

The value of `strMachineName` is the same as the value of the **COMPUTERNAME** environment variable.

## Examples

The following example demonstrates how to get the value of the **COMPUTERNAME** environment variable.


```JScript
// --------------------------------------------------------------------
// Set the text of the gadget based on the environment variable.
// --------------------------------------------------------------------
function SetContentText()
{
    txtMachineName.innerHTML = System.Environment.machineName;
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

[**getEnvironmentVariable**](system-environment-getenvironmentvariable.md)
</dt> </dl>

 

 





