---
Description: Retrieves a Win32\_SecurityDescriptor representation of the Win32\_LogicalFileSecuritySetting object security descriptor in the form of a Win32\_SecurityDescriptor object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c6736acd-5ef1-4f18-b32a-fca13142db9c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: GetSecurityDescriptor method of the Win32\_LogicalFileSecuritySetting class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSecurityDescriptor method of the Win32\_LogicalFileSecuritySetting class

The **GetSecurityDescriptor** [WMI class](https://msdn.microsoft.com/library/aa393244) method retrieves a [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) representation of the [**Win32\_LogicalFileSecuritySetting**](win32-logicalfilesecuritysetting.md) object security descriptor in the form of a **Win32\_SecurityDescriptor** object. A security descriptor contains information about the owner of the object, and the primary group of an object. The security descriptor also contains two access control lists (ACL). The first list is called the discretionary access control lists (DACL), and describes who should have access to an object and what type of access to grant. The second list is called the system access control lists (SACL) and defines what type of auditing to record for an object.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetSecurityDescriptor(
  [out] Win32_SecurityDescriptor Descriptor
);
```



## Parameters

<dl> <dt>

*Descriptor* \[out\]
</dt> <dd>

Expression that resolves to an instance of [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md).

</dd> </dl>

## Return value

The **GetSecurityDescriptor** method can return the error codes listed in the following list. For more information about integer values other than those listed, see [WMI\_Return Codes](https://msdn.microsoft.com/library/aa394574).

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

**Other** (22 4294967295)
</dt> </dl>

## Examples

In the following VBScript code example the assumption is that a folder named \\testfolder exists on C:\\. The example obtains the folder security and dissects it into the security components: ACEs, Trustees, and SIDs. For more information about security entities, see [Security Descriptors](https://msdn.microsoft.com/library/windows/desktop/aa379563).

The script calls the **Win32\_LogicalFileSecuritySetting::GetSecurityDescriptor** method to retrieve an instance of the [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) class for the target object, that is, C:\\TestFolder. **GetSecurityDescriptor** returns the *wmiSecurityDescriptor* parameter with an instance of the **Win32\_SecurityDescriptor** class that corresponds to the security descriptor for the target object. Properties provided by the **Win32\_SecurityDescriptor** class contain the DACL array of access control entries (ACEs) in the form of [**Win32\_ACE**](win32-ace.md) object references. It also contains the trustee information in the form of Win32\_Trustee objects.


```VB
On Error Resume Next
' The folder named "testfolder" must exist on the C:\ drive.

Set wmiFileSecSetting = GetObject( _
   "winmgmts:Win32_LogicalFileSecuritySetting.path='c:\\testfolder'")

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
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
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

[Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> </dl>

 

 




