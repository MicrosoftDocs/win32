---
title: System.Shell.execute method
description: Launches an application.
ms.assetid: 'a2e4f759-e845-4f34-84c0-a1bab5e39f04'
keywords: ["execute method Windows Sidebar", "execute method Windows Sidebar , System.Shell object", "System.Shell object Windows Sidebar , execute method"]
topic_type:
- apiref
api_name:
- System.Shell.execute
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.execute method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Launches an application.

## Syntax


```JScript
iRetVal = System.Shell.execute(
  strFile,
  [ strArgs ],
  [ strDir ],
  [ strOperation ]
)
```



## Parameters

<dl> <dt>

*strFile* \[in\]
</dt> <dd>

**String** that specifies a UNC path to an executable file, a file name, or a URL.

</dd> <dt>

*strArgs* \[in, optional\]
</dt> <dd>

If *strFile* specifies an executable file then **String** specifies the parameters to be passed to the application. For example, a UNC path such as `System.Gadget.path + "\\MyFile.Txt"`.

> [!Note]  
> If *strFile* specifies a file name or URL, *strArgs* is unneccessary and should be blank, null, or an empty string.

 

</dd> <dt>

*strDir* \[in, optional\]
</dt> <dd>

**String** that specifies the UNC path for the default (working) directory of the executable file.

</dd> <dt>

*strOperation* \[in, optional\]
</dt> <dd>

**String** that specifies the action (or Windows Shell verb) to be performed. The set of available verbs depends on the particular file or folder.

<dt>



 (edit)


</dt> <dd>

Opens the file specified by *strArgs* for editing.

</dd> <dt>



 (explore)


</dt> <dd>

Opens the folder specified by *strDir* for exploring.

</dd> <dt>



 (find)


</dt> <dd>

Opens the folder specified by *strDir* for searching.

</dd> <dt>



 (open)


</dt> <dd>

Opens the file specified by *strArgs*.

</dd> <dt>



 (print)


</dt> <dd>

Prints the file specified by *strArgs* on the default printer.

</dd> </dl> </dd> </dl>

## Remarks

Supplying a path to a file name (with extension) or a URL for *strFile* will launch the default application associated with that file name extension and load the file name specified.

> [!Note]  
> Alternatively, a path to a known application .exe can by supplied for *strFile* while *strArgs*, *strDir*, and *strOperation* are used to specify the rest of the file information.

 

*strArgs*, *strDir*, and *strOperation* can be assigned values in combination as required.

UNC paths should escape special characters with a '\\'.

## Examples

The following example demonstrates how to launch a URL.


```JScript
System.Shell.execute("http://www.microsoft.com");
```



The following example demonstrates how to open a text file in the default application and in Notepad.


```JScript
System.Shell.execute(System.Gadget.path + "\\MyFile.txt");
System.Shell.execute("Notepad.exe", "MyFile.Txt", "C:\\Users\\MyName\\", "open");
```



The following example demonstrates how to print a text file.


```JScript
System.Shell.execute(System.Gadget.path + "\\MyFile.txt", null, null, "print");
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



 

 





