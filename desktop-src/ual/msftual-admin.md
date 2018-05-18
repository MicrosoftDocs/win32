---
title: MsftUal\_Admin class
description: This is a class of methods for enabling and disabling the User Access Logging feature.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8a692693-b9a2-4c03-b2ee-1727f96cede4'
ms.prod: 'windows-server-dev'
ms.technology: 'user-access-logging'
ms.tgt_platform: multiple
keywords: ["MsftUal_Admin class User Access Logging", "MsftUal_Admin class User Access Logging , described"]
topic_type:
- apiref
api_name:
- MsftUal_Admin
- MsftUal_Admin.Enabled
api_location:
- UALProv.dll
api_type:
- DllExport
---

# MsftUal\_Admin class

This is a class of methods for enabling and disabling the User Access Logging feature.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1"), dynamic, provider("UAL")]
class MsftUal_Admin
{
  boolean Enabled;
};
```

## Members

The **MsftUal\_Admin** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MsftUal\_Admin** class has these methods.



| Method                                   | Description                                            |
|:-----------------------------------------|:-------------------------------------------------------|
| [**Disable**](disable-msftual-admin.md) | Disables User Access Logging on the system.<br/> |
| [**Enable**](enable-msftual-admin.md)   | Enables User Access Logging on the system.<br/>  |



 

### Properties

The **MsftUal\_Admin** class has these properties.

<dl> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\AccessLogging<br/>                                                         |
| MOF<br/>                      | <dl> <dt>Sum.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>UALProv.dll</dt> </dl> |



 

 





