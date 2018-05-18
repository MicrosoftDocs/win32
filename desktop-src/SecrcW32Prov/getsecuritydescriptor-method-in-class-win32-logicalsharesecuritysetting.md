---
Description: 'Retrieves a Win32\_SecurityDescriptor representation of the Win32\_LogicalShareSecuritySetting object security descriptor.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '4d16713a-19bd-456b-b2b5-6bcf235862f6'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'GetSecurityDescriptor method of the Win32\_LogicalShareSecuritySetting class'
---

# GetSecurityDescriptor method of the Win32\_LogicalShareSecuritySetting class

The **GetSecurityDescriptor** method retrieves a [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) representation of the [**Win32\_LogicalShareSecuritySetting**](win32-logicalsharesecuritysetting.md) object security descriptor.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832) and [Retrieving a Class](https://msdn.microsoft.com/library/aa393244).

## Syntax


```mof
uint32 GetSecurityDescriptor(
  [out] Win32_SecurityDescriptor Descriptor
);
```



## Parameters

<dl> <dt>

*Descriptor* \[out\]
</dt> <dd>

Expression that resolves to an instance of [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md).

</dd> </dl>

## Return value

The **GetSecurityDescriptor** method can return the error codes listed in the following list. For more information about integer values different from those listed, see [WMI Return Codes](https://msdn.microsoft.com/library/aa394574).

<dl> <dt>

**Success**
</dt> <dd>

0

Successful completion.

</dd> <dt>

**Access denied**
</dt> <dd>

2

The user does not have access to the requested information.

</dd> <dt>

**Unknown failure**
</dt> <dd>

8

Unknown failure.

</dd> <dt>

**Privilege missing**
</dt> <dd>

9

The user does not have adequate privileges.

</dd> <dt>

**Invalid parameter**
</dt> <dd>

21

The specified parameter is not valid.

</dd> <dt>

**Other**
</dt> <dd>

22–4294967295

</dd> </dl>

## Remarks

For a VBScript code example about how to get and parse the SD, see [**GetSecurityDescriptor Method in Class Win32\_LogicalFileSecuritySetting**](getsecuritydescriptor-method-in-class-win32-logicalfilesecuritysetting.md).

Note that this method works on shares, but may not be able to retrieve retrieve hidden shares (suffixed with "$").

## Examples

The following Script Center[code example](https://Gallery.TechNet.Microsoft.Com/scriptcenter/List-Share-Permissions-83f8c419) lists all shares on a computer, and then uses **GetSecurityDescriptor** to list all the share permissions for each share.

The script calls the **Win32\_LogicalShareSecuritySetting.GetSecurityDescriptor** method to retrieve an instance of the [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) class for the target object. **GetSecurityDescriptor** returns the *SecurityDescriptor* parameter with an instance of the **Win32\_SecurityDescriptor** class that corresponds to the security descriptor for the target object. Properties provided by the **Win32\_SecurityDescriptor** class contain the DACL array of access control entries (ACEs) in the form of [**Win32\_ACE**](win32-ace.md) object references. It also contains the trustee information in the form of [**Win32\_Trustee**](win32-trustee.md) objects.


```VB
On Error Resume Next
' The Win32_LogicalShareSecuritySetting instance with
' the name = to WMILogs$ is specified 

Set wmiFileSecSetting = GetObject( _
   "winmgmts:Win32_LogicalShareSecuritySetting.Name='WMILogs$'")

RetVal = wmiFileSecSetting. _
    GetSecurityDescriptor(wmiSecurityDescriptor)
If Err <> 0 Then
    WScript.Echo "GetSecurityDescriptor failed" _
    & VBCRLF & Err.Number & VBCRLF & Err.Description
    WScript.Quit
Else
    WScript.Echo "GetSecurityDescriptor succeeded"
End If

' Retrieve the DACL array of Win32_ACE objects.
DACL = wmiSecurityDescriptor.DACL

For each wmiAce in DACL

    wscript.echo "Access Mask: "     & wmiAce.AccessMask
    wscript.echo "ACE Type: "        & wmiAce.AceType

' Get Win32_Trustee object from ACE 
       Set Trustee = wmiAce.Trustee
    wscript.echo "Trustee Domain: "  & Trustee.Domain
    wscript.echo "Trustee Name: "    & Trustee.Name

' Get SID as array from Trustee
    SID = Trustee.SID 
    strsid = join(SID, ",") 
    wscript.echo "Trustee SID: {" & strsid & "}"
        
Next
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

[**Win32\_LogicalShareSecuritySetting**](win32-logicalsharesecuritysetting.md)
</dt> </dl>

 

 




