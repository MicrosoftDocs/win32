---
title: MSISCSITARGET\_ElementSettingData class
description: Represents the association between managed elements and applicable setting data. This association also describes whether this is a default or current setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'db69c0da-5c19-4790-96f7-9bc3b36e80a2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_ElementSettingData class iSCSI Software Target API", "MSISCSITARGET_ElementSettingData class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ElementSettingData
- MSISCSITARGET_ElementSettingData.ManagedElement
- MSISCSITARGET_ElementSettingData.SettingData
- MSISCSITARGET_ElementSettingData.IsDefault
- MSISCSITARGET_ElementSettingData.IsCurrent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_ElementSettingData class

Represents the association between managed elements and applicable setting data. This association also describes whether this is a default or current setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_ElementSettingData : CIM_ElementSettingData
{
  CIM_ManagedElement REF ManagedElement;
  CIM_SettingData    REF SettingData;
  uint16                 IsDefault;
  uint16                 IsCurrent;
};
```

## Members

The **MSISCSITARGET\_ElementSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_ElementSettingData** class has these properties.

<dl> <dt>

**IsCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumerated integer indicating that the referenced setting is currently being used in the operation of the element, or that this information is unknown.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Is_Current"></span><span id="is_current"></span><span id="IS_CURRENT"></span>

**Is Current** (1)


</dt> <dd></dd> <dt>

<span id="Is_Not_Current"></span><span id="is_not_current"></span><span id="IS_NOT_CURRENT"></span>

**Is Not Current** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**IsDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumerated integer indicating that the referenced setting is a default setting for the element, or that this information is unknown.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Is_Default"></span><span id="is_default"></span><span id="IS_DEFAULT"></span>

**Is Default** (1)


</dt> <dd></dd> <dt>

<span id="Is_Not_Default"></span><span id="is_not_default"></span><span id="IS_NOT_DEFAULT"></span>

**Is Not Default** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The managed element.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The SettingData object associated with the element.

This property is inherited from [**CIM\_ElementSettingData**](cim-elementsettingdata.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementSettingData**](cim-elementsettingdata.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**CIM\_ElementSettingData**](https://msdn.microsoft.com/library/mt446053)
</dt> <dt>

[**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911)
</dt> </dl>

 

 





