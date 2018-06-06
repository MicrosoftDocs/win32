---
Description: The Win32\_PageFileSetting&\#8194;WMI class represents the settings of a page file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 22190ede-1db6-4d69-ae74-63d10977cc78
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_PageFileSetting class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_PageFileSetting class

The **Win32\_PageFileSetting** [WMI class](https://msdn.microsoft.com/cfe4bcca-692e-45cd-a840-93ebfe4ae267) represents the settings of a page file. Information contained within objects instantiated from this class specify the page file parameters used when the file is created at system startup. The properties in this class can be modified and deferred until startup. These settings are different from the run-time state of a page file expressed through the associated class [**Win32\_PageFileUsage**](win32-pagefileusage.md).

To create an instance of this class, enable the **SeCreatePagefilePrivilege** privilege. For more information, see [**Privilege Constants**](https://msdn.microsoft.com/f9400597-81bb-44a8-80dc-aba0160aea26) and [Executing Privileged Operations](https://msdn.microsoft.com/11bb8723-f329-4083-8219-2256ce44a5e3).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), Privileges("SeCreatePagefilePrivilege"), UUID("{514A9270-C856-11D2-B364-00105A1f77A1}"), SupportsCreate, CreateBy("PutInstance"), SupportsDelete, DeleteBy("DeleteInstance"), SupportsUpdate, AMENDMENT]
class Win32_PageFileSetting : CIM_Setting
{
  string Caption;
  string Description;
  string SettingID;
  uint32 InitialSize;
  uint32 MaximumSize;
  string Name;
};
```

## Members

The **Win32\_PageFileSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PageFileSetting** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) (64)
</dt> </dl>

Short textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**InitialSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|System\\\\CurrentControlSet\\\\Control\\\\Session Manager\\\\Memory Management\|PagingFiles"), [**Units**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("megabytes")
</dt> </dl>

Initial size of the page file.

Example: 139

</dd> <dt>

**MaximumSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|System\\\\CurrentControlSet\\\\Control\\\\Session Manager\\\\Memory Management\|PagingFiles"), [**Units**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("megabytes")
</dt> </dl>

Maximum size of the page file.

Example: 178

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI")
</dt> </dl>

Path and file name of the page file.

Example: "C:\\PAGEFILE.SYS"

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) (256)
</dt> </dl>

Identifier by which the current object is known.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> </dl>

## Remarks

The **Win32\_PageFileSetting** class is derived from [**CIM\_Setting**](cim-setting.md).

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

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[Operating System Classes](https://www.bing.com/search?q=Operating+System+Classes)
</dt> </dl>

 

 




