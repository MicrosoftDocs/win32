---
Description: 'The SetSecurityDescriptorWMI class method sets a security descriptor to the specified structure.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '15fc56c9-9990-4d83-bb1e-92eeecb1798b'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'SetSecurityDescriptor method of the Win32\_LogicalFileSecuritySetting class'
---

# SetSecurityDescriptor method of the Win32\_LogicalFileSecuritySetting class

The **SetSecurityDescriptor**[WMI class](https://msdn.microsoft.com/library/aa393244) method sets a security descriptor to the specified structure. A security descriptor contains information about the owner of the object and the object's primary group. The security descriptor also contains the [*discretionary access control list (DACL)*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) and the [*system access control list (SACL)*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly). DACLs specify which groups and accounts have access to an object and what type of access to grant. SACLs specify who has access to the auditing entries in the Security event log.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetSecurityDescriptor(
  [in] Win32_SecurityDescriptor Descriptor
);
```



## Parameters

<dl> <dt>

*Descriptor* \[in\]
</dt> <dd>

An expression that resolves to an instance of [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md).

</dd> </dl>

## Return value

The **SetSecurityDescriptor** method can return the error codes listed in the following list. For more information, see [WMI\_Return Codes](https://msdn.microsoft.com/library/aa394574).

<dl> <dt>

**Success** (0)
</dt> <dt>

**Access denied** (2)
</dt> <dt>

**Unknown failure** (8)
</dt> <dt>

**Privilege missing** (9)
</dt> <dt>

**Invalid parameter** (21)
</dt> <dt>

**Other** (22–4294967295)
</dt> </dl>

## Remarks

The **SeSecurityPrivilege** privilege is required to execute this method. For more information, see [Executing Privileged Operations](https://msdn.microsoft.com/library/aa390428).

When a new SACL is not specified in a call to a **SetSecurityDescriptor** method, then the security descriptor SACL on the target securable object is set to **NULL** so that the previous SACL setting does not persist.

## Examples

The following script calls the [**Win32\_LogicalFileSecuritySetting::GetSecurityDescriptor**](getsecuritydescriptor-method-in-class-win32-logicalfilesecuritysetting.md) method to retrieve an instance of the [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) class for the target object, that is, C:\\TestFolder. **GetSecurityDescriptor** returns the *SecurityDescriptor* parameter with an instance of the **Win32\_SecurityDescriptor** class that corresponds to the security descriptor for the target object. The access mask for each trustee in each access control entry (ACE) in the security descriptor changes to allow read access. For more information about security entities, see [Security Descriptors](https://msdn.microsoft.com/library/windows/desktop/aa379563).


```VB
' Connect to WMI and get the file security
' object for the testfolder directory
Set wmiFileSecSetting = GetObject ( _
    "winmgmts:Win32_LogicalFileSecuritySetting." & _
    "path='c:\\testfolder'")

' Use the Win32_LogicalFileSecuritySetting Caption
' property to create a simple header before
' clearing the discretionary access control list (DACL).
Wscript.Echo wmiFileSecSetting.Caption & ":" & vbCrLf

' Obtain the existing security descriptor for folder
RetVal = wmiFileSecSetting. _
    GetSecurityDescriptor(wmiSecurityDescriptor)
If Err <> 0 Then
    WScript.Echo "GetSecurityDescriptor failed" & _
        VBCRLF & Err.Number & VBCRLF & Err.Description
    WScript.Quit
Else
    WScript.Echo "GetSecurityDescriptor suceeded"
End If

' Retrieve the content of Win32_SecurityDescriptor
' DACL property.
' The DACL is an array of Win32_ACE objects.
DACL = wmiSecurityDescriptor.DACL

' Display the control flags in the descriptor.
Wscript.Echo "Control Flags:  " & _
    wmiSecurityDescriptor.ControlFlags

' Obtain the trustee for each access
' control entry (ACE) and change the permissions
' in the AccessMask for each ACE to read, write, and delete.
For each wmiAce in DACL
    
' Get Win32_Trustee object from ACE 
       Set Trustee = wmiAce.Trustee
'    wscript.echo "Trustee Domain: "  & Trustee.Domain
    wscript.echo "Trustee Name: "    & Trustee.Name
    wscript.echo "Access Mask: "     & wmiAce.AccessMask
' Set read access to the owner, group,
' and DACL of the security descriptor (131072) 
    wmiAce.AccessMask = 131072
    wscript.echo "Access Mask: "     & wmiAce.AccessMask            
Next

' Call the Win32_LogicalFileSecuritySetting.
' SetSecurityDescriptor method 
' to write the new security descriptor.
RetVal = wmiFileSecSetting. _
    SetSecurityDescriptor(wmiSecurityDescriptor)

Wscript.Echo "ReturnValue is:  " & RetVal
```



The following PowerShell example describes how to set the owner for a specified object.


```PowerShell
function Set-Owner ($user, $Path) { 
if (!(Test-Path $Path)) {Write-Warning "Specified path is incorrect"} 
else { 
    # replace path from C:\Folder to C:\\Folder 
    $path = $path.replace("\", "\\") 

    # create SecurityDescriptor appropriated classes 
    $SD = ([WMIClass] "Win32_SecurityDescriptor").CreateInstance() 
    $Trustee = ([WMIClass] "Win32_Trustee").CreateInstance() 

    # translate user/group name to SID and write information to
    # Trustee properties 
    $SID = (new-object security.principal.ntaccount $user).translate([security.principal.securityidentifier]) 
    [byte[]] $SIDArray = ,0 * $SID.BinaryLength 
    $SID.GetBinaryForm($SIDArray,0) 
    $Trustee.Name = $user 
    $Trustee.SID = $SIDArray 
    $SD.Owner = $Trustee 

    # set control flag 
    $SD.ControlFlags="0x8000" 

    # get file or folder object 
    $wPrivilege = gwmi Win32_LogicalFileSecuritySetting -filter "path='$path'" 

    # enable SeRestorePrivilege (for Windows Vista and Windows Server 2008
    # not neccessary if running in privileged mode)
    $wPrivilege.psbase.Scope.Options.EnablePrivileges = $true 

    # Write  new SecurityDescriptor to file/folder object
    $wPrivilege.setsecuritydescriptor($SD)
}
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

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_LogicalFileSecuritySetting**](win32-logicalfilesecuritysetting.md)
</dt> <dt>

[**Win32\_SecurityDescriptor**](win32-securitydescriptor.md)
</dt> <dt>

[Maintaining WMI Security](https://msdn.microsoft.com/library/aa392291)
</dt> <dt>

[Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> </dl>

 

 




