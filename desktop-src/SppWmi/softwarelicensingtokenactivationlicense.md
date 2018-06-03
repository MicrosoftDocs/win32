---
title: SoftwareLicensingTokenActivationLicense class
description: This class exposes properties of installed token-based activation licenses.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a769725a-8cbe-462a-8ef7-6cc2fba06c7e
keywords:
- SoftwareLicensingTokenActivationLicense class Windows Management Instrumentation
- SoftwareLicensingTokenActivationLicense class Windows Management Instrumentation , described
topic_type:
- apiref
api_name:
- SoftwareLicensingTokenActivationLicense
- SoftwareLicensingTokenActivationLicense.ID
- SoftwareLicensingTokenActivationLicense.ILID
- SoftwareLicensingTokenActivationLicense.ILVID
- SoftwareLicensingTokenActivationLicense.AuthorizationStatus
- SoftwareLicensingTokenActivationLicense.ExpirationDate
- SoftwareLicensingTokenActivationLicense.Description
- SoftwareLicensingTokenActivationLicense.AdditionalInfo
api_location:
- SppWmi.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SoftwareLicensingTokenActivationLicense class

This class exposes properties of installed token-based activation licenses.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class SoftwareLicensingTokenActivationLicense
{
  string   ID;
  string   ILID;
  uint32   ILVID;
  uint32   AuthorizationStatus;
  datetime ExpirationDate;
  string   Description;
  string   AdditionalInfo;
};
```

## Members

The **SoftwareLicensingTokenActivationLicense** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SoftwareLicensingTokenActivationLicense** class has these methods.



| Method                                                                 | Description                        |
|:-----------------------------------------------------------------------|:-----------------------------------|
| [**Uninstall**](uninstall-softwarelicensingtokenactivationlicense.md) | Uninstalls the license.<br/> |



 

### Properties

The **SoftwareLicensingTokenActivationLicense** class has these properties.

<dl> <dt>

**AdditionalInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies optional text to provide additional metadata.

</dd> <dt>

**AuthorizationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies an HRESULT returned from the issuance license (IL) authorization.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies optional text provided by the customer and included in the IL.

</dd> <dt>

**ExpirationDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies a UTC datetime after which the IL cannot be used for token activation.

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Specifies a GUID that is used by the Software Licensing service to uniquely identify an XRML license.

</dd> <dt>

**ILID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies a GUID that is used to identify the IL to the customer. The ILID is not unique, unless combined with the ILVID.

</dd> <dt>

**ILVID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies a version number that is used along with the ILID to allow customers to version their licenses.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>SppWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SppWmi.dll</dt> </dl> |



 

 





