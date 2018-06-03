---
title: GetExpandedStringValue method of the StdRegProv class
description: The GetExpandedStringValue method returns the data value for a named value whose data type is REG\_EXPAND\_SZ.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 67d641cf-b648-4c22-9308-a2c9a380f638
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetExpandedStringValue method
- GetExpandedStringValue method, StdRegProv class
- StdRegProv class, GetExpandedStringValue method
topic_type:
- apiref
api_name:
- StdRegProv.GetExpandedStringValue
api_location:
- Stdprov.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetExpandedStringValue method of the StdRegProv class

The **GetExpandedStringValue** method returns the data value for a named value whose data type is **REG\_EXPAND\_SZ**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetExpandedStringValue(
  [in]  uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in]  string sSubKeyName,
  [in]  string sValueName,
  [out] string sValue
);
```



## Parameters

<dl> <dt>

*hDefKey* \[in\]
</dt> <dd>

A registry tree, also known as a hive, that contains the *sSubKeyName* path. The default value is **HKEY\_LOCAL\_MACHINE**.

The following trees are defined in WinReg.h.

<dt>

<span id="HKEY_CLASSES_ROOT"></span><span id="hkey_classes_root"></span>

**HKEY\_CLASSES\_ROOT** (2147483648)


</dt> <dd></dd> <dt>

<span id="HKEY_CURRENT_USER"></span><span id="hkey_current_user"></span>

**HKEY\_CURRENT\_USER** (2147483649)


</dt> <dd></dd> <dt>

<span id="HKEY_LOCAL_MACHINE"></span><span id="hkey_local_machine"></span>

**HKEY\_LOCAL\_MACHINE** (2147483650)


</dt> <dd></dd> <dt>

<span id="HKEY_USERS"></span><span id="hkey_users"></span>

**HKEY\_USERS** (2147483651)


</dt> <dd></dd> <dt>

<span id="HKEY_CURRENT_CONFIG"></span><span id="hkey_current_config"></span>

**HKEY\_CURRENT\_CONFIG** (2147483653)


</dt> <dd></dd> </dl> </dd> <dt>

*sSubKeyName* \[in\]
</dt> <dd>

\[in\] A path that contains the named values.

</dd> <dt>

*sValueName* \[in\]
</dt> <dd>

\[in\] A named value whose data value you are retrieving. Specify an empty string to get the default named value.

</dd> <dt>

*sValue* \[out\]
</dt> <dd>

\[out\] An expanded string data value for the named value. The string is only expanded if the environment variable (for example, *%Path%*) is defined.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

Registry values of the expanded string type are strings that include items that are evaluated only when the string value is actually used. For instance, a typical expanded string value is the one that holds the location of the TEMP directory:

**%USERPROFILE%\\Local Settings\\Temp**

The \\Local Settings\\Temp component of the string is treated literally, but the value of the *%USERPROFILE%* component can be determined only when it is actually accessed. This is because the value is dependent upon the user accessing the entry. If you look at the registry entry in Regedit.exe, you will see the value %USERPROFILE%\\Local Settings\\Temp. However, when you retrieve the value of the entry, the value will be something like this: C:\\Documents and Settings\\jsmith.REDMOND\\Local Settings\\Temp. In other words, the environment variable *%USERPROFILE%* is replaced with the folder (in this case, C:\\Documents and Settings\\jsmith.REDMOND) that contains the user profile.

The components of expanded string types that appear between percent symbols (%) correspond to environment variables and are dependent either on the aspects of the particular user or the current configuration of the computer.

You use the **GetExpandedStringValue** method to retrieve expanded string values. The method takes, as one of its parameters, a variable in which the retrieved value is stored. In the retrieved value, the components of the string that appear between percent symbols are automatically evaluated. This means your script will echo a value similar to "C:\\Documents and Settings\\jsmith.REDMOND\\Local Settings\\Temp" rather than a value like "%USERPROFILE%\\Local Settings\\Temp".

## Examples

The [Add a Folder to Your Windows Path](https://Gallery.TechNet.Microsoft.Com/dd4f01a6-8850-49ba-b4e5-d2c3df60a69f) VBScript sample adds a new folder to your Windows path.

The [Collect userprofile, recycle bin and selective folder size for remote servers](https://Gallery.TechNet.Microsoft.Com/f1634012-59e2-4f7e-9a3e-75e522fc0511) PowerShell sample generates a report for all user profiles, user specified folders, and user recycle bin that are more than a specified size.

The following VBScript code example shows how to read the **REG\_EXPAND\_SZ** value that is located in **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**WinLogon**. You can save the script as a file with a .vbs extension and send the output to a file by executing the command line in the folder that contains the script:

**cscript Filename.vbs &gt;** *output.txt*


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
strComputer = "."
Set objReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\"&amp;_
    strComputer & "\root\default:StdRegProv")
strKeyPath = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\WinLogon"
strValueName = "UIHost"
Return = objReg.GetExpandedStringValue(HKEY_LOCAL_MACHINE,_
    strKeyPath,strValueName,strValue)
If (Return = 0) And (Err.Number = 0) Then   
    WScript.Echo  "The Windows logon UI host is: " & strValue
Else
    Wscript.Echo _
        "GetExpandedStringValue failed. Error = " & Err.Number
End If
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\default<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RegEvent.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Stdprov.dll</dt> </dl>  |



 

 





