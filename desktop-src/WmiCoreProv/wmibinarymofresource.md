---
description: The WDM class provider defines the WMIBinaryMofResource class in the \\root\\wmi namespace to support the task of keeping track of the status of data in the WMI repository.
ms.assetid: 57416a36-5b3a-4d04-808c-09adc597c47a
title: WMIBinaryMofResource class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WMIBinaryMofResource
- WMIBinaryMofResource.HighDateTime
- WMIBinaryMofResource.LowDateTime
- WMIBinaryMofResource.MofProcessed
- WMIBinaryMofResource.Name
api_type: 
- Schema
api_location: 
- Root\WMI
---

# WMIBinaryMofResource class

The WDM class provider defines the **WMIBinaryMofResource** class in the \\root\\wmi namespace to support the task of keeping track of the status of data in the WMI repository.

## Syntax

``` syntax
class WMIBinaryMofResource
{
  uint32  HighDateTime;
  uint32  LowDateTime;
  boolean MofProcessed;
  string  Name;
};
```

## Members

The **WMIBinaryMofResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **WMIBinaryMofResource** class has these properties.

<dl> <dt>

**HighDateTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

High half of the date-time stamp.

</dd> <dt>

**LowDateTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Low half of the date-time stamp.

</dd> <dt>

**MofProcessed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Flag indicating whether the .mof file was fully processed.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Name of the WDM enabled driver that has a binary MOF file successfully compiled in the WMI repository.

</dd> </dl>

## Remarks

The WDM class provider creates an instance of **WMIBinaryMofResource** for each WDM driver that supplies a binary MOF file.

Whenever WMI initializes the provider, the provider compares the timestamp with the timestamp of the driver image file. If the timestamps differ, WMI re-compiles the MOF file.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                     |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Wmi.mof</dt> </dl> |



## See also

<dl> <dt>

[WDM Provider](wdm-provider.md)
</dt> </dl>

 

