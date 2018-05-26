---
title: CIM\_ElementSetting class
description: Represents the association between managed system elements and the setting classes defined for them.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c7dc9913-16ff-47d9-acae-170cd8f25e79
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ElementSetting class
- CIM_ElementSetting class, described
topic_type:
- apiref
api_name:
- CIM_ElementSetting
- CIM_ElementSetting.Element
- CIM_ElementSetting.Setting
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ElementSetting class

Represents the association between managed system elements and the setting classes defined for them.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, AMENDMENT]
class CIM_ElementSetting
{
  CIM_ManagedSystemElement REF Element;
  CIM_Setting              REF Setting;
};
```

## Members

The **CIM\_ElementSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The CIM\_ManagedSystemElement reference represents the role of the CIM\_ManagedSystemElement object of the CIM\_ElementSetting association. Role: The associated managed system element provides the element that implements the element setting.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Setting**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Represents the role of the CIM\_Setting object of the CIM\_ElementSetting association. Role: The associated setting provides the setting that implements the element setting.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



 

 





