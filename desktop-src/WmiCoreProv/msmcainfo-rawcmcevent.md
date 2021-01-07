---
description: Contains a Corrected Machine Check (CMC) event. This class is available only in 64-bit Windows systems.
ms.assetid: e12efbf7-7d53-415a-bc48-90d33e4ce16d
title: MSMCAInfo_RawCMCEvent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSMCAInfo_RawCMCEvent
- MSMCAInfo_RawCMCEvent.Active
- MSMCAInfo_RawCMCEvent.Count
- MSMCAInfo_RawCMCEvent.InstanceName
- MSMCAInfo_RawCMCEvent.Records
api_type: 
- DllExport
api_location: 
- Wmiprov.dll
---

# MSMCAInfo\_RawCMCEvent class

The **MSMCAInfo\_RawCMCEvent** class contains a Corrected Machine Check (CMC) event. This class is available only in 64-bit Windows systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSMCAInfo_RawCMCEvent : WMIEvent
{
  boolean         Active;
  uint32          Count;
  string          InstanceName;
  MSMCAInfo_Entry Records[];
};
```

## Members

The **MSMCAInfo\_RawCMCEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSMCAInfo\_RawCMCEvent** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TRUE, if this instance of the class is active; otherwise, **FALSE**.

</dd> <dt>

**Count**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of error records.

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Unique identifier of this instance of the class.

</dd> <dt>

**Records**
</dt> <dd> <dl> <dt>

Data type: **MSMCAInfo\_Entry** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of Machine Check Architecture (MCA) error records. The number of MCA error records in the array is specified by the **Count** property.

</dd> </dl>

## Remarks

The **MSMCAInfo\_RawCMCEvent** class is derived from [**WMIEvent**](wmievent.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>Wmicore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[MSMCA Classes](msmca-classes.md)
</dt> <dt>

[**WMIEvent**](wmievent.md)
</dt> </dl>

 

