---
title: MDM\_WirelessProfileXml class
description: Represents a wireless profile with wireless LAN XML.
ms.assetid: 88d87b61-10dc-41d3-8c53-bec846505a8c
keywords:
- MDM_WirelessProfileXml class MDM Settings
- MDM_WirelessProfileXml class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_WirelessProfileXml
- MDM_WirelessProfileXml.Name
- MDM_WirelessProfileXml.ProfileXml
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDM\_WirelessProfileXml class

Represents a wireless profile with wireless LAN XML.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[InPartition("local-user"), dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_WirelessProfileXml
{
  string Name;
  string ProfileXml;
};
```

## Members

The **MDM\_WirelessProfileXml** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_WirelessProfileXml** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of a wireless LAN profile.

</dd> <dt>

**ProfileXml**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The wireless profile XML for this connection.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





