---
Description: 'Converts a Win32\_SecurityDescriptor instance to a security descriptor in Security Descriptor Definition Language (SDDL) string format.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'ebf957ca-d2bb-4928-a92d-08e7db447ebd'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32SDToSDDL method of the Win32\_SecurityDescriptorHelper class'
---

# Win32SDToSDDL method of the Win32\_SecurityDescriptorHelper class

The **Win32SDToSDDL** WMI class method converts a [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) instance to a [*security descriptor*](https://msdn.microsoft.com/library/aa390836#wmi-gloss-security-descriptor) in [Security Descriptor Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa379570) (SDDL) string format.

## Syntax


```mof
uint32 Win32SDToSDDL(
  [in]  __SecurityDescriptor Descriptor,
  [out] string               SDDL
);
```



## Parameters

<dl> <dt>

*Descriptor* \[in\]
</dt> <dd>

Security descriptor in [**\_\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394673) format.

</dd> <dt>

*SDDL* \[out\]
</dt> <dd>

Security descriptor in SDDL format.

</dd> </dl>

## Return value

Returns one of the values listed in the following list.

<dl> <dt>

**S\_OK**
</dt> <dd>

0 (0x0)

The call was successful. The scripting and Visual Basic constant is **wbemNoErr**.

</dd> <dt>

**WBEM\_E\_INVALID\_PARAMETER**
</dt> <dd>

2147749896 (0x80041008)

One of the parameters to the call is not correct. The scripting and Visual Basic constant is **wbemErrInvalidParameter**.

</dd> <dt>

**WBEM\_E\_PROVIDER\_FAILURE**
</dt> <dd>

2147749892 (0x80041004)

Provider has failed at some time other than during initialization. The scripting and Visual Basic constant is **wbemErrProviderFailure**.

</dd> <dt>

**WBEM\_E\_OUT\_OF\_MEMORY**
</dt> <dd>

2147749894 (0x80041006)

Not enough memory for the operation. The scripting and Visual Basic constant is **wbemErrOutOfMemory**.

</dd> </dl>

## Examples

The following VBScript code example gets the security descriptor for a file in [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) format then converts it to SDDL format.


```VB
' Obtain argument from command line

If WScript.Arguments.Count = 0 Then
 WScript.Echo "Usage: GetFileSD <file_name>"
 WScript.Quit 1
End If

' Get the filename with path, for example C:\Users\user1\test.txt
Set objFileSystem = CreateObject( "Scripting.FileSystemObject" )
Filename = WScript.Arguments( 0 )
Set objFile = objFileSystem.GetFile( Filename )
Filename = objFile.Path
WScript.Echo Filename

' Get an instance of Win32_SecurityDescriptorHelper
Set objHelper = GetObject( _
    "winmgmts:root\cimv2:Win32_SecurityDescriptorHelper" )

' Connect to WMI on local computer and root\cimv2 namespace
Set objWMIService = GetObject( "winmgmts:root\cimv2" )

' Get the instance of Win32_LogicalFileSecuritySetting
'    associated with the file
' Replace single "\" with "\\" as escape character
Set objFile = objWMIService.Get( _
    "Win32_LogicalFileSecuritySetting=""" _
    & Replace( Filename,"\","\\") & """" )

' Get the existing security descriptor for the file
Return = objFile.GetSecurityDescriptor( objSD )
If ( return <> 0 ) Then
 WScript.Echo "Could not get security descriptor: " & Return
 wscript.Quit Return
End If

' Convert file security descriptor from 
'     Win32_SecurityDescriptor format to SDDL format
Return = objHelper.Win32SDToSDDL( objSD,SDDLstring )
If ( Return <> 0 )  Then
 WScript.Echo "Could not convert to SDDL: " & Return
 WScript.Quit Return
End If

WScript.Echo SDDLstring
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SecurityDescriptorHelper**](win32-securitydescriptorhelper.md)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> <dt>

[Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905)
</dt> </dl>

 

 




