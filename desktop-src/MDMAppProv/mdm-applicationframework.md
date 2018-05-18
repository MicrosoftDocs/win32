---
title: MDM\_ApplicationFramework class
description: Retrieves information about an application framework on a device that is registered with the Mobile Device Management (MDM) service.
ms.assetid: '9f418156-91c3-477b-9467-9697c2951dc0'
keywords: ["MDM_ApplicationFramework class MDM App Management", "MDM_ApplicationFramework class MDM App Management , described"]
topic_type:
- apiref
api_name:
- MDM_ApplicationFramework
- MDM_ApplicationFramework.PackageName
- MDM_ApplicationFramework.MinimumPackageVersion
- MDM_ApplicationFramework.PackagePublisher
- MDM_ApplicationFramework.PackageArchitecture
- MDM_ApplicationFramework.PackageFullName
- MDM_ApplicationFramework.PackageVersion
- MDM_ApplicationFramework.UserSID
api_location:
- MDMAppProv.dll
api_type:
- DllExport
---

# MDM\_ApplicationFramework class

\[The MDM Application Provider is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [EnterpriseAppManagement Configuration Service Provider (CSP)](https://msdn.microsoft.com/library/windows/hardware/dn904955).\]

Retrieves information about an application framework on a device that is registered with the Mobile Device Management (MDM) service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), Deprecated("No value"), dynamic, provider("MDMAppProv"), AMENDMENT]
class MDM_ApplicationFramework
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

The **MDM\_ApplicationFramework** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_ApplicationFramework** class has these properties.

<dl> <dt>

**MinimumPackageVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets a key that specifies the minimum package version that is supported by the dependent framework.

</dd> <dt>

**PackageArchitecture**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets a key that specifies the architecture of the package.

**Windows 8 and Windows 8.1:** This property is not supported before Windows 8.1 Update.

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

Gets a key that specifies the name of the package.

</dd> <dt>

**PackagePublisher**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets a key that specifies the publisher name of the package.

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

Gets the user security identifier of the package.

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

 

 





