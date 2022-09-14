---
description: Represents the raw data from a Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) structure.
ms.assetid: a51b73bb-a5f7-4e01-9c88-780105e9952b
title: WmiMonitorRawEEdidV1Block class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorRawEEdidV1Block
- WmiMonitorRawEEdidV1Block.Active
- WmiMonitorRawEEdidV1Block.InstanceName
- WmiMonitorRawEEdidV1Block.Id
- WmiMonitorRawEEdidV1Block.Type
- WmiMonitorRawEEdidV1Block.Content
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# WmiMonitorRawEEdidV1Block class

The **WmiMonitorRawEEdidV1Block** WMI class represents the raw data from a Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) structure. This 128-byte data structure contains information that describes the optimal configuration for a display.

## Syntax

``` syntax
class WmiMonitorRawEEdidV1Block : MSMonitorClass
{
  boolean Active;
  string  InstanceName;
  uint8   Id;
  uint8   Type;
  uint8   Content[];
};
```

## Members

The **WmiMonitorRawEEdidV1Block** class has these types of members:

-   [Properties](#properties)

### Properties

The **WmiMonitorRawEEdidV1Block** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the active monitor.

</dd> <dt>

**Content**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

128 byte array that contains the raw block content.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identity of the data block.

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Name of the specific monitor instance.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of data block. The following table lists possible values that can be returned.



| Value                                                                                 | Meaning                    |
|---------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0 (0x0)</dt> </dl>    | Uninitialized<br/>   |
| <dl> <dt>1 (0x1)</dt> </dl>    | EDID base block<br/> |
| <dl> <dt>2 (0x2)</dt> </dl>    | EDID block map<br/>  |
| <dl> <dt>255 (0xFF)</dt> </dl> | Other<br/>           |



 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>WmiCore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSMonitorClass**](msmonitorclass.md)
</dt> <dt>

[**WmiGetMonitorRawEEdidV1Block**](wmigetmonitorraweedidv1block-wmimonitordescriptormethods.md)
</dt> </dl>

 

 




