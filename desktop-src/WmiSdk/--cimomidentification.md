---
description: Describes the local installation of WMI.
ms.assetid: 907b65b2-a853-40f4-8b36-5a05a2b1cf85
ms.tgt_platform: multiple
title: '__CIMOMIdentification class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __CIMOMIdentification
- Root.__CIMOMIdentification.SetupDateTime
- Root.__CIMOMIdentification.VersionCurrentlyRunning
- Root.__CIMOMIdentification.VersionUsedToCreateDB
- Root.__CIMOMIdentification.WorkingDirectory
api_type: 
- Schema
api_location: 
- Root
---

# \_\_CIMOMIdentification class

The **\_\_CIMOMIdentification** system class describes the local installation of WMI. This is a singleton class; there is only one instance. The **\_\_CIMOMIdentification** class is available only in the **Root** and **Root\\Default** namespaces. Users query for the instance to obtain information about the WMI installation.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[singleton]
class __CIMOMIdentification : __SystemClass
{
  string SetupDateTime;
  string VersionCurrentlyRunning;
  string VersionUsedToCreateDB;
  string WorkingDirectory;
};
```

## Members

The **\_\_CIMOMIdentification** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_CIMOMIdentification** class has these properties.

<dl> <dt>

**SetupDateTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time of installation. This property is empty after the operating system is installed for the first time.

If the WMI repository has been deleted and then created again, this property contains the date and time that the repository is created again.

</dd> <dt>

**VersionCurrentlyRunning**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the version of the actual image containing the WMI service that created the Common Information Model (CIM) repository. Because the repository format may change between versions of WMI, this property allows future WMI upgrades to determine whether the database must be upgraded. The format is:

"1.00.183.0000"

where the first digit is the major version, the next two digits are minor versions, and the next three digits are the build number. The remaining digits are not used.

</dd> <dt>

**VersionUsedToCreateDB**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the version of the actual image containing the WMI service that created the CIM repository. Because the repository format may change between versions of WMI, this property allows future WMI upgrades to determine whether the database must be upgraded. The format is:

"1.00.183.0000"

where the first digit is the major version, the next two digits are minor versions, and the next three digits are the build number. The remaining digits are not used.

</dd> <dt>

**WorkingDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Installation directory.

</dd> </dl>

## Remarks

The **\_\_CIMOMIdentification** class is derived from [**\_\_SystemClass**](--systemclass.md), which has no properties.

## Examples

The following VBScript code sample describes how to display CIM object model identification information, and was taken from the sample directory at \\\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\sysmgmt\\wmi\\scripting.


```VB
on error resume next 
set cimomid = GetObject("winmgmts:root\default:__cimomidentification=@")

if err <> 0 then
 WScript.Echo ErrNumber, Err.Source, Err.Description
else
 WScript.Echo cimomid.path_.displayname
 WScript.Echo cimomid.versionusedtocreatedb
end if
```



The following Perl code sample describes how to display CIM object model identification information, and was taken from the sample directory at \\\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\sysmgmt\\wmi\\scripting.


```Perl
use strict;
use Win32::OLE;

my ($Cimomid, $locator, $services);

eval { $Cimomid = Win32::OLE->GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\default")->
 Get("__CIMOMIdentification=@"); };

unless ($@)
{
 print "\n", $Cimomid->Path_()->{displayname}, "\n";
 print $Cimomid->{versionusedtocreatedb}, "\n";
}
else
{ 
 print STDERR "\n", Win32::OLE->LastError, "\n";
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | Root<br/>                |



## See also

<dl> <dt>

[**\_\_SystemClass**](/windows/desktop/WmiSdk/--systemclass)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

