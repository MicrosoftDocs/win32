---
title: System.Shell.saveFileDialog method
description: Displays a standard Windows File Save dialog box.
ms.assetid: 'e3fd8e4c-e4a9-401f-b6e7-a6bd71aedfe4'
keywords: ["saveFileDialog method Windows Sidebar", "saveFileDialog method Windows Sidebar , System.Shell object", "System.Shell object Windows Sidebar , saveFileDialog method"]
topic_type:
- apiref
api_name:
- System.Shell.saveFileDialog
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.saveFileDialog method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Displays a standard Windows **File Save** dialog box.

## Syntax


```JScript
strRetVal = System.Shell.saveFileDialog(
  strPath,
  strFilter
)
```



## Parameters

<dl> <dt>

*strPath* \[in\]
</dt> <dd>

**String** that specifies the root directory.

> [!Note]  
> If an empty string is specified, the root directory is set to the users desktop (%USERPROFILE%\\Desktop).

 

</dd> <dt>

*strFilter* \[in\]
</dt> <dd>

**String** that specifies file description and extension. This string is in the format "Description:\*.Extension:Description:\*.Extension::".

> [!Note]  
> It may be necessary to substitute the '`:`' seperator with '`\0`' for the **Save as type:** listbox to function correctly.

 

</dd> </dl>

## Return value

**String** that specifies the UNC path to the saved object.

## Remarks

Displays the standard Windows File Save dialog box in order to save data to a file.

*strFilter* requires that the double-colon terminator as the filter string must be terminated by two **NULL** characters.

The first string in each pair is a display string that describes the filter (for example, Text Files), and the second string specifies the filter pattern (for example, \*.TXT). To specify multiple filter patterns for a single display string, use a semicolon to separate the patterns (for example, \*.TXT;\*.DOC;\*.BAK). A pattern string can be a combination of valid file name characters and the asterisk (\*) wildcard character. Do not include spaces in the pattern string.

The system displays the filters in the order specified by *strFilter* in the **File Types** combo box.

If *strFilter* is an empty string, the dialog box does not display any filters.

## Examples

The following example demonstrates how to save user input to a text file.


```JScript
// --------------------------------------------------------------------
// Save user input to a text file.
// txtToSave: user input.
// --------------------------------------------------------------------
function SaveTextToFile(txtToSave)
{
    var sPath = System.Shell.saveFileDialog(System.Gadget.path,"Text File\0*.txt\0XML File\0*.xml\0\0");
    if (sPath != "")
    {
        spFeedback.innerHTML = sPath;
        
        // Initialize the Stream object enums.
        // Sets or returns the type of data in a Stream object. 
        // 2 = text data.
        var adTypeText = 2; 
        // Sets whether a file should be created if it does not exist or overwritten if it does.
        // 2 = overwrites the file with the data from a Stream object.
        var adSaveCreateOverWrite = 2;
        // Sets or returns the available permissions for modifying data.
        // 3 = read/write.
        var adModeReadWrite = 3;
    
        var oStream = new ActiveXObject("ADODB.Stream");
        with(oStream)
        {
            Mode = adModeReadWrite;
            Type = adTypeText;
            Open();
            WriteText(txtToSave);
            SaveToFile(sPath,adSaveCreateOverWrite);
            Close();
        }
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



 

 





