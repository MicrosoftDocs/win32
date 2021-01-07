---
description: Gets the security descriptor for the namespace to which the user is connected. This method returns a security descriptor in binary byte array format. If you are writing a script, use the GetSecurityDescriptor method.
ms.assetid: aeac1e7b-fcb8-4880-afd1-4950da37602b
ms.tgt_platform: multiple
title: GetSD method of the __SystemSecurity class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- __SystemSecurity.GetSD
api_type:
- COM
api_location:
- All
---

# GetSD method of the \_\_SystemSecurity class

The **GetSD** method gets the security descriptor for the namespace to which the user is connected. This method returns a security descriptor in binary byte array format. If you are writing a script, use the [**GetSecurityDescriptor**](getsecuritydescriptor-method-in-class---systemsecurity-.md) method. For more information, see [Securing WMI Namespaces](securing-wmi-namespaces.md) and [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md).

The user must have the **READ\_CONTROL** permission. By default, administrators have that permission. The only part of the security descriptor that is actually used is the discretionary access control list (DACL). The DACL can contain both inherited and non-inherited ACEs. Both deny and allow ACEs are permitted.

If you are programming in C++, you can manipulate the binary security descriptor using [SDDL](/windows/desktop/SecAuthZ/security-descriptor-definition-language), and the conversion methods [**ConvertSecurityDescriptorToStringSecurityDescriptor**](/windows/desktop/api/sddl/nf-sddl-convertsecuritydescriptortostringsecuritydescriptora) and [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora).

## Syntax


```mof
HRESULT GetSD(
  [out] uint8 SD[]
);
```



## Parameters

<dl> <dt>

*SD* \[out\]
</dt> <dd>

Security descriptor in binary byte array format.

</dd> </dl>

## Return value

This method returns an **HRESULT** indicating the status of the method call. The following list lists the return values that are of significance to **GetSD**. For scripting and Visual Basic applications, the result can be obtained from [OutParameters.ReturnValue](parsing-outparameters-objects.md). For more information, see [Constructing InParameters Objects and Parsing OutParameters Objects](constructing-inparameters-objects-and-parsing-outparameters-objects.md).

<dl> <dt>

**S\_OK**
</dt> <dd>

Method executed successfully.

</dd> <dt>

**WBEM\_E\_ACCESS\_DENIED**
</dt> <dd>

Caller does not have sufficient rights to call this method.

</dd> <dt>

**WBEM\_E\_METHOD\_DISABLED**
</dt> <dd>

Attempted to run this method on an unsupported system.

</dd> </dl>

## Remarks

For more information about modifying namespace security programmatically or manually, see [Securing WMI Namespaces](securing-wmi-namespaces.md).

## Examples

The following script shows you how to use **GetSD** to obtain the current security descriptor for the Root\\Cimv2 namespace and change it to the byte array shown in **DisplaySD**.


```VB
Set objServices = GetObject("winmgmts:root\cimv2")
Set CimV2 = objServices.Get("__SystemSecurity=@")
ReturnValue = Cimv2.GetSD(arrSD)

If Err <> 0 Then
   WScript.Echo "Method returned error " & ReturnValue
End If

DisplaySD = "SD = {"
For I = Lbound(arrSD) To Ubound(arrSD)

   DisplaySD = DisplaySD & arrSD(I)

   If I <> Ubound(arrSD) Then
      DisplaySD = DisplaySD & ","
   End If

Next

DisplaySD = DisplaySD & "}"

WScript.Echo DisplaySD
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[**\_\_SystemSecurity**](--systemsecurity.md)
</dt> <dt>

[WMI Security Constants](wmi-security-constants.md)
</dt> <dt>

[**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace)
</dt> <dt>

[**\_\_SystemSecurity::SetSD**](--systemsecurity-setsd.md)
</dt> <dt>

[**Security\_Descriptor**](/windows/desktop/api/winnt/ns-winnt-security_descriptor)
</dt> <dt>

[**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor)
</dt> <dt>

[Securing WMI Namespaces](securing-wmi-namespaces.md)
</dt> </dl>

 

