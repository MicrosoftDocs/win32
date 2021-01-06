---
description: Writes an updated version of the security descriptor that controls access to the printer.
ms.assetid: 6a709043-473e-4b24-8b52-6c68b670ebcf
ms.tgt_platform: multiple
title: SetSecurityDescriptor method of the Win32_Printer class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Printer.SetSecurityDescriptor
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# SetSecurityDescriptor method of the Win32\_Printer class

The **SetSecurityDescriptor** method writes an updated version of the security descriptor that controls access to the printer. The security descriptor is an instance of the [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) class. For more information, see [Changing Access Security on Securable Objects](/windows/desktop/WmiSdk/changing-access-security-on-securable-objects).

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 SetSecurityDescriptor(
  [in] Win32_SecurityDescriptor Descriptor
);
```



## Parameters

<dl> <dt>

*Descriptor* \[in\]
</dt> <dd>

The security descriptor that is associated with the printer.

</dd> </dl>

## Return value

Returns one of the values listed in the following list, or a different value to indicate an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**0**
</dt> <dd>

Successful completion.

</dd> <dt>

**2**
</dt> <dd>

The user does not have access to the requested information.

</dd> <dt>

**8**
</dt> <dd>

Unknown failure.

</dd> <dt>

**9**
</dt> <dd>

The user does not have adequate privileges to execute the method.

</dd> <dt>

**21**
</dt> <dd>

A parameter specified in the method call is not valid.

</dd> </dl>

## Remarks

The [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) instance represents a [**SECURITY\_DESCRIPTOR\_CONTROL**](/windows/desktop/SecAuthZ/security-descriptor-control) data type and contains a [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) and a [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL). For more information, see [Access Control Lists](/windows/desktop/SecAuthZ/access-control-lists).

If the **SeSecurityPrivilege** is not granted or enabled when getting a security descriptor, then only the DACL is returned in the returned security descriptor. For more information, see [**Privilege Constants**](/windows/desktop/WmiSdk/privilege-constants) and [Executing Privileged Operations](/windows/desktop/WmiSdk/executing-privileged-operations).

You can update both the DACL and the SACL in the [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) instance when calling this method, but you can also update only the DACL or only the SACL.

The following values in [**SECURITY\_DESCRIPTOR\_CONTROL**](/windows/desktop/SecAuthZ/security-descriptor-control) determine whether the DACL, the SACL, or both are updated.

-   **SE\_DACL\_PRESENT**

    Indicates that the DACL should be updated. If this is not set then WMI preserves the original value of the DACL.

-   **SE\_SACL\_PRESENT**

    Indicates that the SACL should be updated. If this is not set, then WMI preserves the original value of the SACL. To update the SACL, the account must have the **SeSecurityPrivilege** privilege enabled. For scripting, the privilege name is **SeSecurityPrivilege**. For more information, see [**Privilege Constants**](/windows/desktop/WmiSdk/privilege-constants).

If the Group trustee and the Owner trustee properties are not **NULL**, then they are updated. Otherwise, WMI preserves the original values. For more information, see [WMI Security Descriptor Objects](/windows/desktop/WmiSdk/wmi-security-descriptor-objects).

When a new SACL is **NULL** in a call to this method, then the security descriptor SACL on the target securable object is left unchanged.

## Examples

The [Copy-ACLToPrinter](https://Gallery.TechNet.Microsoft.Com/Copy-ACLToPrinter-2d66ce19) PowerShell sample Replace the permissions (ACL) from one printer to another.

The following PowerShell code sample describes how to set the security descriptor for a printer.


```PowerShell
# Specify the user or group
$user = "everyone"

# create instances of necessary classes
$SD = ([WMIClass] "Win32_SecurityDescriptor").CreateInstance()
$ace = ([WMIClass] "Win32_Ace").CreateInstance()
$Trustee = ([WMIClass] "Win32_Trustee").CreateInstance()

# Translate a name of user or group to SID
$SID = (new-object security.principal.ntaccount $user).translate([security.principal.securityidentifier])

# Get binary form from SID and byte Array
[byte[]] $SIDArray = ,0 * $SID.BinaryLength
$SID.GetBinaryForm($SIDArray,0)

# Fill Trustee object parameters
$Trustee.Name = $user
$Trustee.SID = $SIDArray

# Set AccessMask which can contain following values:
# Takeownership - 524288
# ReadPermissions - 131072
# ChangePermissions - 262144
# ManageDocuments - 983088
# ManagePrinters - 983052
# Print + ReadPermissions - 131080
$ace.AccessMask = 983052

# Set AceType. Can be 0 (Allow), or 1 (Deny), or 2 (System Audit)
$ace.AceType = 0
$ace.AceFlags = 0  

# Write Win32_Trustee object to Win32_Ace Trustee property
$ace.Trustee = $Trustee

# Write Win32_Ace and Win32_Trustee objects to SecurityDescriptor object
$SD.DACL = $ace

# Set SE_DACL_PRESENT control flag
$SD.ControlFlags = 0x0004

# Get printer object. For example 'CutePDF Writer' printer object
$Printer = gwmi win32_printer -filter "name = 'CutePDF Writer'"

# Enable SeSecurityPrivilege privilegies
$Printer.psbase.Scope.Options.EnablePrivileges = $true

# Invoke SetSecurityDescriptor method and write new ACE to specified
# printer ACL.
$Printer.SetSecurityDescriptor($SD)
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>Win32\_Printer.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl>       |



## See also

<dl> <dt>

[**Win32\_Printer**](win32-printer.md)
</dt> <dt>

[**Privilege Constants**](/windows/desktop/WmiSdk/privilege-constants)
</dt> <dt>

[WMI Security Descriptor Objects](/windows/desktop/WmiSdk/wmi-security-descriptor-objects)
</dt> <dt>

[Changing Access Security on Securable Objects](/windows/desktop/WmiSdk/changing-access-security-on-securable-objects)
</dt> </dl>

 

