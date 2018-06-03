---
title: System.Shell.chooseFile method
description: Displays a file picker dialog box and retrieves a System.Shell.Item object that represents the selected file.
ms.assetid: 1c8cd9d2-992f-4a03-8c8f-cc5d473114b6
keywords:
- chooseFile method Windows Sidebar
- chooseFile method Windows Sidebar , System.Shell object
- System.Shell object Windows Sidebar , chooseFile method
topic_type:
- apiref
api_name:
- System.Shell.chooseFile
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Shell.chooseFile method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Displays a file picker dialog box and retrieves a [**System.Shell.Item**](system-shell-item.md) object that represents the selected file.

## Syntax


```JScript
objRetVal = System.Shell.chooseFile(
  bForOpen,
  strFilter,
  strInitialDirectory,
  strFileInit
)
```



## Parameters

<dl> <dt>

*bForOpen* \[in\]
</dt> <dd>

**Boolean** that specifies the type of file picker dialog box to display.

<dt>



 (true)


</dt> <dd>

**Open**.

</dd> <dt>



 (false)


</dt> <dd>

**Save As**.

</dd> </dl> </dd> <dt>

*strFilter* \[in\]
</dt> <dd>

**String** that specifies file descriptions and extensions. This string is in the format "Description:\*.Extension:Description:\*.Extension::".

</dd> <dt>

*strInitialDirectory* \[in\]
</dt> <dd>

**String** that specifies the root directory.

> [!Note]  
> If an empty string is specified, the root directory is set to the users desktop (%USERPROFILE%\\Desktop).

 

</dd> <dt>

*strFileInit* \[in\]
</dt> <dd>

**String** that specifies the file name.

</dd> </dl>

## Return value

A [**System.Shell.Item**](system-shell-item.md) that represents the selected file.

## Remarks

*strFilter* requires the double-colon terminator as the filter string must be terminated by two **NULL** characters.

The first string in each pair is a display string that describes the filter (for example, Text Files), and the second string specifies the filter pattern (for example, \*.TXT). To specify multiple filter patterns for a single display string, use a semicolon to separate the patterns (for example, \*.TXT;\*.DOC;\*.BAK). A pattern string can be a combination of valid file name characters and the asterisk (\*) wildcard character. Do not include spaces in the pattern string.

The system displays the filters in the order specified by *strFilter* in the **File Types** combo box.

If *strFilter* is an empty string, the dialog box does not display any filters.

The **chooseFile** Open dialog box:

![file picker 'open' dialog box.](images/reference/choosefileopen.png)

The **chooseFile** Save As dialog box:

![file picker 'save as' dialog box.](images/reference/choosefilesaveas.png)

## Examples

The following example demonstrates how to specify .txt and .reg files for the file picker dialog box.


```JScript
// Create a shell item object.
var oShellItem = System.Shell.chooseFile(true, "Text File:*.txt:Reg File:*.reg::", "C:\\", "");
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





