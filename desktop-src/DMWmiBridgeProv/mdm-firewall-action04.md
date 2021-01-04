---
title: MDM_Firewall_Action04 class
description: The MDM\_Firewall\_Action04 class is used to configure the Windows Defender Firewall settings.
ms.assetid: d0704662-ac2b-4ff5-a2c1-8f2bc7835488
keywords:
- MDM_Firewall_Action04 class
- MDM_Firewall_Action04 class, described
topic_type:
- apiref
api_name:
- MDM_Firewall_Action04
- MDM_Firewall_Action04.InstanceID
- MDM_Firewall_Action04.ParentID
- MDM_Firewall_Action04.Type
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_Firewall\_Action04 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The MDM\_Firewall\_Action04 class is used to configure the Windows Defender Firewall settings.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv1")]
class MDM_Firewall_Action04
{
  string InstanceID;
  string ParentID;
  sint32 Type;
};
```

## Members

The **MDM\_Firewall\_Action04** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Firewall\_Action04** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | None supported<br/>                                                                       |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                              |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv1.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl>  |



 

