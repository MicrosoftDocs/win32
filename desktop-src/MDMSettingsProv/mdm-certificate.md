---
title: MDM\_Certificate class
description: Provides the ability to install and delete the certificates on the device.
ms.assetid: 78b6ee97-9f67-451d-ba53-6af0d2e31800
keywords:
- MDM_Certificate class MDM Settings
- MDM_Certificate class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_Certificate
- MDM_Certificate.StoreLocation
- MDM_Certificate.StoreName
- MDM_Certificate.Thumbprint
- MDM_Certificate.IsInstalled
- MDM_Certificate.Blob
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDM\_Certificate class

Provides the ability to install and delete the certificates on the device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_Certificate
{
  uint8   StoreLocation;
  string  StoreName;
  string  Thumbprint;
  boolean IsInstalled;
  string  Blob;
};
```

## Members

The **MDM\_Certificate** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Certificate** class has these properties.

<dl> <dt>

**Blob**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Base64-encoded raw certificate blob.

</dd> <dt>

**IsInstalled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the certificate is installed.

</dd> <dt>

**StoreLocation**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The certificate store location.

Possible values are.

<dt>

<span id="1"></span>

**1** (ContextUser)


</dt> <dd></dd> <dt>

<span id="2"></span>

**2** (ContextMachine)


</dt> <dd></dd> </dl>

</dd> <dt>

**StoreName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The internal store name to install the certificate.

</dd> <dt>

**Thumbprint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The thumbprint of the certificate.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





