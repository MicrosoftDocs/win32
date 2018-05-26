---
Description: Represents information on the NAP System Health Agent (SHA) which provides information about the registered SHAs on a Windows system.
ms.assetid: 9ad1451f-c56d-4324-9465-89fa62f6cd27
title: NAP\_SystemHealthAgent class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NAP\_SystemHealthAgent class

Represents information on the NAP System Health Agent (SHA) which provides information about the registered SHAs on a Windows system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class NAP_SystemHealthAgent
{
  uint32  id;
  string  friendlyName;
  string  description;
  string  version;
  string  vendorName;
  string  infoClsid;
  string  registrationDate;
  boolean isBound;
  uint32  fixupState;
  uint8   percentage;
};
```

## Members

The **NAP\_SystemHealthAgent** class has these types of members:

-   [Properties](#properties)

### Properties

The **NAP\_SystemHealthAgent** class has these properties.

<dl> <dt>

**description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the SHA.

</dd> <dt>

**fixupState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fix-up state of the SHA.

</dd> <dt>

**friendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly name for the SHA.

</dd> <dt>

**id**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The System Health Agent Id.

</dd> <dt>

**infoClsid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A GUID of the COM server implementing the [**INapComponentInfo**](https://msdn.microsoft.com/library/windows/desktop/aa369417) interface.

</dd> <dt>

**isBound**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A value that indicates if the SHA is bound to the NAP Agent service; **TRUE** if bound, otherwise **FALSE**.

</dd> <dt>

**percentage**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The percent fix-up complete value. This property is not supported.

</dd> <dt>

**registrationDate**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The registration date of the SHA.

</dd> <dt>

**vendorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The vendor name of the SHA.

</dd> <dt>

**version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version number of the SHA.

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

 

 




