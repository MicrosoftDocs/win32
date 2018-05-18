---
title: System.Debug.outputString method
description: Writes a string to the console.
ms.assetid: 'b74fa757-3368-4395-bb39-6bb45d962e98'
keywords: ["outputString method Windows Sidebar", "outputString method Windows Sidebar , System.Debug object", "System.Debug object Windows Sidebar , outputString method"]
topic_type:
- apiref
api_name:
- System.Debug.outputString
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Debug.outputString method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Writes a string to the console.

## Syntax


```JScript
System.Debug.outputString(
  strOutputString
)
```



## Parameters

<dl> <dt>

*strOutputString* \[in\]
</dt> <dd>

**String** to write to the console.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Useful for sending variable values, gadget state, or function names to the console for debugging.

The value of `strOutputString` can only be viewed with a script debugger while the gadget is running.

## Examples

The following example demonstrates how to throw an error and use **outputString** to display it in a debugger console.


```JScript
// --------------------------------------------------------------------
// Attempt to save the file and throw an error if the file name does 
// not include a file name extension.
// --------------------------------------------------------------------
function SaveFile()
{
    var fso = new ActiveXObject( "Scripting.FileSystemObject" );
    // Throw an arbitrary error to demonstrate the outputString method.
    try
    {
        if (sFilename.indexOf(".") == -1)
        {            
            throw "'File name' does not specify a file name extension.";
        }
        var file = 
            fso.OpenTextFile(sFilePath + sFilename, 
            FOR_WRITING, CREATE_NEW);
        file.Write(sContent);
        file.Close();
        fso = file = null;
    }
    catch(e)
    {
        System.Debug.outputString(e);
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

[**System.Debug**](system-debug.md)
</dt> </dl>

 

 





