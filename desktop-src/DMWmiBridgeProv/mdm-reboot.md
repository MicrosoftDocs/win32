---
title: MDM_Reboot class
description: The MDM\_Rebootclass is used to configure reboot settings.
ms.assetid: 876ba854-1c26-49cf-915d-194be9f9c1d4
keywords:
- MDM_Reboot class
- MDM_Reboot class, described
topic_type:
- apiref
api_name:
- MDM_Reboot
- MDM_Reboot.InstanceID
- MDM_Reboot.ParentID
api_location:
- Mofs\DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_Reboot class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_Reboot**class is used to configure reboot settings.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv1")]
class MDM_Reboot
{
  string InstanceID;
  string ParentID;
};
```

## Members

The **MDM\_Reboot** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_Reboot** class has these methods.



| Method                                                | Description                                             |
|:------------------------------------------------------|:--------------------------------------------------------|
| [**RebootNowMethod**](mdm-reboot-rebootnowmethod.md) | This method executes a reboot of the device.<br/> |



 

### Properties

The **MDM\_Reboot** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "Reboot".

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/"

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | None supported<br/>                                                                            |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv1.mof</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>Mofs\\DMWmiBridgeProv.dll</dt> </dl> |



 

