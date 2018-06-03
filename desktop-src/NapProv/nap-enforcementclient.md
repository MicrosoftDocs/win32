---
Description: Represents information on the NAP Enforcement Client (EC) and registered enforcers on a Windows system.
ms.assetid: bac64788-2dc1-4a91-a287-1513a2d9aaa0
title: NAP\_EnforcementClient class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NAP\_EnforcementClient class

Represents information on the NAP Enforcement Client (EC) and registered enforcers on a Windows system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class NAP_EnforcementClient
{
  uint32  id;
  string  friendlyName;
  string  description;
  string  version;
  string  vendorName;
  string  infoClsid;
  string  registrationDate;
  boolean isBound;
};
```

## Members

The **NAP\_EnforcementClient** class has these types of members:

-   [Properties](#properties)

### Properties

The **NAP\_EnforcementClient** class has these properties.

<dl> <dt>

**description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the EC.

</dd> <dt>

**friendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly name for the EC.

</dd> <dt>

**id**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The Enforcement Client entity Id.

</dd> <dt>

**infoClsid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The GUID of the COM server implementing [**INapComponentInfo**](https://msdn.microsoft.com/library/windows/desktop/aa369417) interface.

</dd> <dt>

**isBound**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A value that indicates if the Nap EC is bound to NAP Agent service; **TRUE** if bound, otherwise **FALSE**.

</dd> <dt>

**registrationDate**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The registration date of the EC.

</dd> <dt>

**vendorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The vendor name of the EC.

</dd> <dt>

**version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version number of the EC.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                           |
| Namespace<br/>                | Root\\NAP<br/>                                                                           |
| MOF<br/>                      | <dl> <dt>Napclientschema.mof</dt> </dl> |



## See also

<dl> <dt>

[**INapComponentInfo**](https://msdn.microsoft.com/library/windows/desktop/aa369417)
</dt> <dt>

[Network Access Protection](https://msdn.microsoft.com/library/windows/desktop/aa369712)
</dt> </dl>

 

 




