---
title: MDM\_Application class
description: Retrieves information about an application on a device that is registered with the Mobile Device Management (MDM) service.
ms.assetid: '57f6f5a7-9112-4ccf-9553-3155a139807c'
keywords: ["MDM_Application class MDM App Management", "MDM_Application class MDM App Management , described"]
topic_type:
- apiref
api_name:
- MDM_Application
- MDM_Application.PackageFullName
- MDM_Application.UserSID
- MDM_Application.PackageName
- MDM_Application.PackagePublisher
- MDM_Application.PackageVersion
- MDM_Application.InstallPath
- MDM_Application.IsFramework
- MDM_Application.IsResourcePackage
- MDM_Application.IsBundle
- MDM_Application.IsDevelopmentMode
- MDM_Application.Dependencies
api_location:
- MDMAppProv.dll
api_type:
- DllExport
---

# MDM\_Application class

\[The MDM Application Provider is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [EnterpriseAppManagement Configuration Service Provider (CSP)](https://msdn.microsoft.com/library/windows/hardware/dn904955).\]

Retrieves information about an application on a device that is registered with the Mobile Device Management (MDM) service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), Deprecated("No value"), dynamic, provider("MDMAppProv"), AMENDMENT]
class MDM_Application
{
  string  PackageFullName;
  string  UserSID;
  string  PackageName;
  string  PackagePublisher;
  string  PackageVersion;
  string  InstallPath;
  boolean IsFramework;
  boolean IsResourcePackage;
  boolean IsBundle;
  boolean IsDevelopmentMode;
  string  Dependencies;
};
```

## Members

The **MDM\_Application** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Application** class has these properties.

<dl> <dt>

**Dependencies**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a comma separated list that specifies the applications dependencies of the package.

**Windows 8:** This property is not supported before Windows 8.1.

</dd> <dt>

**InstallPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the installation path of the package.

**Windows 8:** This property is not supported before Windows 8.1.

</dd> <dt>

**IsBundle**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets **TRUE** if the package contains an application bundle; otherwise **FALSE**.

**Windows 8:** This property is not supported before Windows 8.1.

</dd> <dt>

**IsDevelopmentMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets **TRUE** if the application is in development mode; otherwise **FALSE**.

**Windows 8:** This property is not supported before Windows 8.1.

</dd> <dt>

**IsFramework**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets **TRUE** if the package contains a framework; otherwise **FALSE**.

**Windows 8:** This property is not supported before Windows 8.1.

</dd> <dt>

**IsResourcePackage**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets **TRUE** if the package is a resource package; otherwise **FALSE**.

**Windows 8:** This property is not supported before Windows 8.1.

</dd> <dt>

**PackageFullName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets a key that specifies the full name of the package.

</dd> <dt>

**PackageName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the friendly name of the package.

</dd> <dt>

**PackagePublisher**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the publisher name of the package.

</dd> <dt>

**PackageVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the version of the package.

</dd> <dt>

**UserSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Get the user security identifier of the package.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                      |
| Minimum supported server<br/> | None supported<br/>                                                                 |
| Namespace<br/>                | Root\\cimv2\\mdm<br/>                                                               |
| MOF<br/>                      | <dl> <dt>MDMAppProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMAppProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Application Provider Classes](https://msdn.microsoft.com/library/dn610374)
</dt> </dl>

 

 





