---
title: MDM\_ApplicationMinVersion class
description: Identifies an application through the minimum version of the application.
ms.assetid: 8CDCA5BF-6760-4B61-AA73-8DD9114346D1
keywords:
- MDM_ApplicationMinVersion class MDM App Management
- MDM_ApplicationMinVersion class MDM App Management , described
topic_type:
- apiref
api_name:
- MDM_ApplicationMinVersion
- MDM_ApplicationMinVersion.PackageName
- MDM_ApplicationMinVersion.MinimumPackageVersion
- MDM_ApplicationMinVersion.PackagePublisher
- MDM_ApplicationMinVersion.PackageArchitecture
- MDM_ApplicationMinVersion.PackageFullName
- MDM_ApplicationMinVersion.PackageVersion
- MDM_ApplicationMinVersion.UserSID
api_location:
- MDMAppProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDM\_ApplicationMinVersion class

\[The MDM Application Provider is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [EnterpriseAppManagement Configuration Service Provider (CSP)](https://msdn.microsoft.com/library/windows/hardware/dn904955).\]

Identifies an application through the minimum version of the application.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), Deprecated("No value"), dynamic, provider("MDMAppProv"), AMENDMENT]
class MDM_ApplicationMinVersion
{
  string PackageName;
  string MinimumPackageVersion;
  string PackagePublisher;
  string PackageArchitecture;
  string PackageFullName;
  string PackageVersion;
  string UserSID;
};
```

## Members

The **MDM\_ApplicationMinVersion** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_ApplicationMinVersion** class has these properties.

<dl> <dt>

**MinimumPackageVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the minimum version of the package.

</dd> <dt>

**PackageArchitecture**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the architecture of the package.

</dd> <dt>

**PackageFullName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the full name of the package.

</dd> <dt>

**PackageName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the name of the package used to deploy the application.

</dd> <dt>

**PackagePublisher**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the publisher of the package.

</dd> <dt>

**PackageVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the package version.

</dd> <dt>

**UserSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Get the user security identifier (SID) of the package.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | None supported<br/>                                                                 |
| Namespace<br/>                | Root\\cimv2\\mdm<br/>                                                               |
| MOF<br/>                      | <dl> <dt>MDMAppProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMAppProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Application Provider Classes](https://msdn.microsoft.com/library/dn610374)
</dt> </dl>

 

 





