---
Description: The Win32\_SessionProcess association WMI class represents an association between a logon session and the processes associated with that session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 19d4ecf9-27b5-4a0b-9c76-7d10679aaf5e
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SessionProcess class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_SessionProcess class

The **Win32\_SessionProcess** association [WMI class](https://msdn.microsoft.com/cfe4bcca-692e-45cd-a840-93ebfe4ae267) represents an association between a logon session and the processes associated with that session.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("9CD8E1CE-0D27-4a41-AADE-F8D200230FF4"), AMENDMENT]
class Win32_SessionProcess : Win32_SessionResource
{
  Win32_LogonSession REF Antecedent;
  Win32_Process      REF Dependent;
};
```

## Members

The **Win32\_SessionProcess** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SessionProcess** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogonSession**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Antecedent"), [**Key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc)
</dt> </dl>

A [**Win32\_LogonSession**](win32-logonsessionmappeddisk.md) that represents the session which is related to the process.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Process**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Dependent"), [**Key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc)
</dt> </dl>

A [**Win32\_Process**](win32-processor.md) that represents the process associated with the session.

</dd> </dl>

## Remarks

**Win32\_SessionProcess** returns all session for the administrator when logged in elevated or when run remotely. This is an extension to the behavior of the class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SessionResource**](win32-sessionresource.md)
</dt> <dt>

[Operating System Classes](https://www.bing.com/search?q=Operating+System+Classes)
</dt> </dl>

 

 




