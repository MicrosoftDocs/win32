---
Description: Convert a security descriptor between the Win32\_SecurityDescriptor, Security Descriptor Definition Language (SDDL), and binary byte array formats.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b9454a2d-5bcc-4e8b-aca8-4294698480e3
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SecurityDescriptorHelper class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_SecurityDescriptorHelper class

The methods of the **Win32\_SecurityDescriptorHelper** WMI class convert a security descriptor between the [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md), Security Descriptor Definition Language (SDDL), and binary byte array formats. Because many WMI methods for manipulating security descriptors require a binary format, use this method to convert the more easily manipulated [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) form to and from binary. For more information, see [WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577).

## Syntax

``` syntax
[Dynamic, Provider("SECRCW32"), UUID("{A502B5A5-B91A-41d1-83D6-BBFA55076333}"), AMENDMENT]
class Win32_SecurityDescriptorHelper
{
};
```

## Members

The **Win32\_SecurityDescriptorHelper** class has these types of members:

-   [Methods](#methods)

### Methods

The **Win32\_SecurityDescriptorHelper** class has these methods.



| Method                                                                                        | Description                                                                                                                                                                                                                       |
|:----------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BinarySDToSDDL**](binarysdtosddl-method-in-class-win32-securitydescriptorhelper.md)       | Converts a binary byte array security descriptor format to a [Security Descriptor Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa379570) (SDDL) string security descriptor format.<br/>                           |
| [**BinarySDToWin32SD**](binarysdtowin32sd-method-in-class-win32-securitydescriptorhelper.md) | Converts a binary byte array security descriptor format to a [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) instance.<br/>                                                                                   |
| [**SDDLToBinarySD**](sddltobinarysd-method-in-class-win32-securitydescriptorhelper.md)       | Converts a [Security Descriptor Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa379570) (SDDL) string security descriptor format to a binary byte array security descriptor format.<br/>                           |
| [**SDDLToWin32SD**](sddltowin32sd-method-in-class-win32-securitydescriptorhelper.md)         | Converts a [Security Descriptor Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa379570) (SDDL) string security descriptor format to a [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) instance.<br/> |
| [**Win32SDToBinarySD**](win32sdtobinarysd-method-in-class-win32-securitydescriptorhelper.md) | Converts a [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) instance to a binary byte array security descriptor format.<br/>                                                                                   |
| [**Win32SDToSDDL**](win32sdtosddl-method-in-class-win32-securitydescriptorhelper.md)         | Converts a [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) instance to [Security Descriptor Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa379570) (SDDL) string format.<br/>                       |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Security Descriptor Helper Class](win32-securitydescriptorhelper.md)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> <dt>

[Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905)
</dt> <dt>

[Access to WMI Namespaces](https://msdn.microsoft.com/library/aa822575)
</dt> </dl>

 

 




