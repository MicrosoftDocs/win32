---
title: MDM\_BrowserSecurityZones class
description: Contains configuration information about browser security zone settings on the device.
ms.assetid: 66626aa8-392b-487a-9810-6f5e9d0a8fa1
keywords:
- MDM_BrowserSecurityZones class MDM Settings
- MDM_BrowserSecurityZones class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_BrowserSecurityZones
- MDM_BrowserSecurityZones.Namespace
- MDM_BrowserSecurityZones.Zone
- MDM_BrowserSecurityZones.Exists
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

# MDM\_BrowserSecurityZones class

Contains configuration information about browser security zone settings on the device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_BrowserSecurityZones
{
  string  Namespace;
  Uint32  Zone;
  boolean Exists;
};
```

## Members

The **MDM\_BrowserSecurityZones** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_BrowserSecurityZones** class has these properties.

<dl> <dt>

**Exists**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the namespace exists in the specified security zone.

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The namespace.

</dd> <dt>

**Zone**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The security zone.

<dt>

<span id="Intranet"></span><span id="intranet"></span><span id="INTRANET"></span>

**Intranet** (1)


</dt> <dd></dd> <dt>

<span id="Trusted"></span><span id="trusted"></span><span id="TRUSTED"></span>

**Trusted** (2)


</dt> <dd></dd> <dt>

<span id="Internet"></span><span id="internet"></span><span id="INTERNET"></span>

**Internet** (3)


</dt> <dd></dd> <dt>

<span id="Untrusted"></span><span id="untrusted"></span><span id="UNTRUSTED"></span>

**Untrusted** (4)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





