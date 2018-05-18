---
title: MDM\_SideLoader class
description: Provides methods for activating side-loading of line-of-business (LOB) applications.
ms.assetid: '13326a90-6e33-4c3b-bca0-9f0a62431be0'
keywords: ["MDM_SideLoader class MDM Settings", "MDM_SideLoader class MDM Settings , described"]
topic_type:
- apiref
api_name:
- MDM_SideLoader
- MDM_SideLoader.key
- MDM_SideLoader.ProductKeyHash
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
---

# MDM\_SideLoader class

Provides methods for activating side-loading of line-of-business (LOB) applications.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_SideLoader
{
  uint32 key;
  string ProductKeyHash;
};
```

## Members

The **MDM\_SideLoader** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_SideLoader** class has these methods.



| Method                                                              | Description                                                              |
|:--------------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**ActivateKey**](https://msdn.microsoft.com/library/dn610378)       | Activates side-loading and installs the product key.<br/>          |
| [**AddCertificate**](https://msdn.microsoft.com/library/dn610379) | Adds the package-signing certificate.<br/>                         |
| [**UnActivateLOB**](https://msdn.microsoft.com/library/dn610406)   | Disables side-loading of line-of-business (LOB) applications.<br/> |



 

### Properties

The **MDM\_SideLoader** class has these properties.

<dl> <dt>

**key**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the **MDM\_SideLoader** class instance.

</dd> <dt>

**ProductKeyHash**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A hash of the installed product key.

</dd> </dl>

## Remarks

There have been some changes that were made for App Side-loading in Windows 10.If you are had Side-loading enabled in Windows 8 or Windows 8.1 and now are experiencing issues when using WMI to enable Side-loading on Windows 10 devices using Windows 8.1 keys, please see [Enterprise app management](https://msdn.microsoft.com/library/windows/hardware/mt228170) for information including using the [EnterpriseModernAppManagement CSP](https://msdn.microsoft.com/library/windows/hardware/dn904956).

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





