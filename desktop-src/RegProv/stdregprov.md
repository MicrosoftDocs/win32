---
title: StdRegProv class
description: Contains methods that manipulate system registry keys and values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fa157559-40f0-4363-b43a-1571885a3152
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StdRegProv class
- StdRegProv class, described
topic_type:
- apiref
api_name:
- StdRegProv
api_location:
- Stdprov.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StdRegProv class

The **StdRegProv** class contains methods that manipulate system registry keys and values. **StdRegProv** is preinstalled in the WMI namespaces root\\default and root\\cimv2.

## Syntax

``` syntax
[dynamic, provider("RegProv"), AMENDMENT]
class StdRegProv
{
};
```

## Members

The **StdRegProv** class has these types of members:

-   [Methods](#methods)

### Methods

The **StdRegProv** class has these methods.



| Method                                                                              | Description                                                             |
|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [**CheckAccess**](checkaccess-method-in-class-stdregprov.md)                       | Verifies that the user has the specified access permissions.<br/> |
| [**CreateKey**](createkey-method-in-class-stdregprov.md)                           | Creates a subkey.<br/>                                            |
| [**DeleteKey**](deletekey-method-in-class-stdregprov.md)                           | Deletes a subkey.<br/>                                            |
| [**DeleteValue**](deletevalue-method-in-class-stdregprov.md)                       | Deletes a named value.<br/>                                       |
| [**EnumKey**](enumkey-method-in-class-stdregprov.md)                               | Enumerates subkeys.<br/>                                          |
| [**EnumValues**](enumvalues-method-in-class-stdregprov.md)                         | Enumerates the named values of a key.<br/>                        |
| [**GetBinaryValue**](getbinaryvalue-method-in-class-stdregprov.md)                 | Gets the binary data value of a named value.<br/>                 |
| [**GetDWORDValue**](getdwordvalue-method-in-class-stdregprov.md)                   | Gets the **DWORD** data value of a named value.<br/>              |
| [**GetExpandedStringValue**](getexpandedstringvalue-method-in-class-stdregprov.md) | Gets the expanded string data value of a named value.<br/>        |
| [**GetMultiStringValue**](getmultistringvalue-method-in-class-stdregprov.md)       | Gets the multiple string data values of a named value.<br/>       |
| [**GetQWORDValue**](getqwordvalue-method-in-class-stdregprov.md)                   | Gets the **QWORD** data values of a named value.<br/>             |
| [**GetSecurityDescriptor**](getsecuritydescriptor-method-in-class-stdregprov.md)   | Gets the security descriptor for a key.<br/>                      |
| [**GetStringValue**](getstringvalue-method-in-class-stdregprov.md)                 | Gets the string data value of a named value.<br/>                 |
| [**SetBinaryValue**](setbinaryvalue-method-in-class-stdregprov.md)                 | Sets the binary data value of a named value.<br/>                 |
| [**SetDWORDValue**](setdwordvalue-method-in-class-stdregprov.md)                   | Sets the **DWORD** data value of a named value.<br/>              |
| [**SetExpandedStringValue**](setexpandedstringvalue-method-in-class-stdregprov.md) | Sets the expanded string data value of a named value.<br/>        |
| [**SetMultiStringValue**](setmultistringvalue-method-in-class-stdregprov.md)       | Sets the multiple string values of a named value.<br/>            |
| [**SetQWORDValue**](setqwordvalue-method-in-class-stdregprov.md)                   | Sets the **QWORD** data values of a named value.<br/>             |
| [**SetSecurityDescriptor**](setsecuritydescriptor-method-in-class-stdregprov.md)   | Sets the security descriptor for a key.<br/>                      |
| [**SetStringValue**](setstringvalue-method-in-class-stdregprov.md)                 | Sets the string value of a named value.<br/>                      |



 

## Remarks

You can use the methods to perform the following tasks:

-   Verify the access permissions for a user.
-   Create, enumerate, and delete registry keys.
-   Create, enumerate, and delete named values.
-   Read, write, and delete data values.
-   Obtain or update the security descriptors for registry keys in scripts using [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) objects.

The RegProv registry provider is hosted in LocalService not the LocalSystem. Therefore, you cannot obtain information remotely from **HKEY\_CURRENT\_USER**, but you can run scripts locally. You can set the hosting model to LocalSystem on a remote machine, but the remote machine registry is vulnerable to hostile access, which is a security risk.

If your application uses a different namespace and requires access to the registry through WMI, you can compile the Managed Object Format (MOF) file that defines **StdRegProv**, RegEvent.mof, into that namespace for use by your application.

Although **StdRegProv** supplies only methods, a script or application can define a new class with properties that represent registry data for particular keys and store the classes in the [*WMI repository*](https://msdn.microsoft.com/library/aa390843#wmi-gloss-wmi-repository). Define the class as described in topics under [Programming with the System Registry Provider](https://msdn.microsoft.com/library/aa392759).

While **StdRegProv** does not have methods to detect registry events, you can call methods like [**SWbemServices.ExecNotificationQuery**](https://msdn.microsoft.com/library/aa393864) or [**IWbemServices::ExecNotificationQuery**](https://msdn.microsoft.com/library/aa392105) with one of the following WMI registry event classes as TargetInstance in the query:

<dl>

[**RegistryKeyChangeEvent**](registrykeychangeevent.md)  
[**RegistryTreeChangeEvent**](registrytreechangeevent.md)  
[**RegistryValueChangeEvent**](registryvaluechangeevent.md)  
</dl>

## Examples

The [Get-Registry via StdRegProv](https://Gallery.TechNet.Microsoft.Com/Get-Registry-via-StdRegProv-f0a04375) PowerShell example retrieves values from the registry via the **StdRegProv** WMI class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\default, Root\\CIMv2<br/>                                                   |
| MOF<br/>                      | <dl> <dt>RegEvent.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Stdprov.dll</dt> </dl>  |



## See also

<dl> <dt>

[Modifying the System Registry](https://msdn.microsoft.com/library/aa392388)
</dt> <dt>

[System Registry Provider](system-registry-provider.md)
</dt> <dt>

[WMI Tasks: Registry](https://msdn.microsoft.com/library/aa394600)
</dt> </dl>

 

 





