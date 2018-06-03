---
title: MDM\_WebApplication class
description: Retrieves information about a web application on a device that is registered with the Mobile Device Management (MDM) service.
ms.assetid: e16bf5ef-9c7b-4136-ab06-e22876830668
keywords:
- MDM_WebApplication class MDM App Management
- MDM_WebApplication class MDM App Management , described
topic_type:
- apiref
api_name:
- MDM_WebApplication
- MDM_WebApplication.PackageName
- MDM_WebApplication.PackageUrl
- MDM_WebApplication.ShortcutFolder
- MDM_WebApplication.ShortcutFilename
api_location:
- MDMAppProv.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MDM\_WebApplication class

\[The MDM Application Provider is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [EnterpriseAppManagement Configuration Service Provider (CSP)](https://msdn.microsoft.com/library/windows/hardware/dn904955).\]

Retrieves information about a web application on a device that is registered with the Mobile Device Management (MDM) service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), Deprecated("No value"), dynamic, provider("MDMAppProv"), AMENDMENT]
class MDM_WebApplication
{
  string PackageName;
  string PackageUrl;
  string ShortcutFolder;
  string ShortcutFilename;
};
```

## Members

The **MDM\_WebApplication** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_WebApplication** class has these properties.

<dl> <dt>

**PackageName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the key that specifies the name of the web application.

</dd> <dt>

**PackageUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the URL of the package.

</dd> <dt>

**ShortcutFilename**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the file name of the shortcut to the web application.

</dd> <dt>

**ShortcutFolder**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the folder that contains the shortcut file for the web application.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                 |
| Namespace<br/>                | Root\\cimv2\\mdm<br/>                                                               |
| MOF<br/>                      | <dl> <dt>MDMAppProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMAppProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Application Provider Classes](https://msdn.microsoft.com/library/dn610374)
</dt> </dl>

 

 





