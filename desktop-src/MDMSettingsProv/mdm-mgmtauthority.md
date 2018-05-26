---
title: MDM\_MgmtAuthority class
description: Represents a management authority and provides a method to create new authorities.
ms.assetid: 910983f3-107e-467e-8aa6-7ac1b3e73f33
keywords:
- MDM_MgmtAuthority class MDM Settings
- MDM_MgmtAuthority class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_MgmtAuthority
- MDM_MgmtAuthority.AuthorityName
- MDM_MgmtAuthority.RootThumbprint
- MDM_MgmtAuthority.ProvisionedCertThumbprint
- MDM_MgmtAuthority.ClientSearchCriteria
- MDM_MgmtAuthority.ServerList
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

# MDM\_MgmtAuthority class

Represents a management authority and provides a method to create new authorities.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_MgmtAuthority
{
  string AuthorityName;
  string RootThumbprint;
  string ProvisionedCertThumbprint;
  string ClientSearchCriteria;
  string ServerList;
};
```

## Members

The **MDM\_MgmtAuthority** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_MgmtAuthority** class has these methods.



| Method                                                                         | Description                                    |
|:-------------------------------------------------------------------------------|:-----------------------------------------------|
| [**CreateNewAuthority**](https://msdn.microsoft.com/library/dn610380) | Creates a new management authority.<br/> |



 

### Properties

The **MDM\_MgmtAuthority** class has these properties.

<dl> <dt>

**AuthorityName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the **MDM\_MgmtAuthority** class instance.

</dd> <dt>

**ClientSearchCriteria**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The certificate search criteria. For example, *Thumbprint*=*122344*&store=*my\\\\system*.

</dd> <dt>

**ProvisionedCertThumbprint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A thumb print of the certificate for this authority.

</dd> <dt>

**RootThumbprint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A thumb print of the trusted root certificate for this authority.

</dd> <dt>

**ServerList**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of the management server URLs that are associated with this authority.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





