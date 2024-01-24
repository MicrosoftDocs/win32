---
title: MDM_WindowsAdvancedThreatProtection_Configuration01 class
description: The MDM\_WindowsAdvancedThreatProtection\_Configuration01 class is used to determine the configuration of Windows Defender Advanced Threat Protection (WDATP) endpoints.
ms.assetid: b4b2ff02-3836-4044-b8fa-d3405f433d8c
keywords:
- MDM_WindowsAdvancedThreatProtection_Configuration01 class
- MDM_WindowsAdvancedThreatProtection_Configuration01 class, described
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MDM_WindowsAdvancedThreatProtection_Configuration01
- MDM_WindowsAdvancedThreatProtection_Configuration01.InstanceID
- MDM_WindowsAdvancedThreatProtection_Configuration01.ParentID
- MDM_WindowsAdvancedThreatProtection_Configuration01.GroupIds
api_type: 
- DllExport
api_location: 
- Mofs\DMWmiBridgeProv.dll
---

# MDM\_WindowsAdvancedThreatProtection\_Configuration01 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_WindowsAdvancedThreatProtection\_Configuration01** class is used to determine the configuration of Windows Defender Advanced Threat Protection (WDATP) endpoints.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv1")]
class MDM_WindowsAdvancedThreatProtection_Configuration01
{
  string InstanceID;
  string ParentID;
  sint32 SampleSharing;
  string GroupIds;
  sint32 TelemetryReportingFrequency;
};
```

## Members

The **MDM\_WindowsAdvancedThreatProtection\_Configuration01** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_WindowsAdvancedThreatProtection\_Configuration01** class has these properties.

<dl> <dt>

**GroupIds**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

TBD

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "Configuration".

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/WindowsAdvancedThreatProtection"

</dd> <dt>

[SampleSharing](/windows/client-management/mdm/windowsadvancedthreatprotection-csp#configuration-samplesharing)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[TelemetryReportingFrequency](/windows/client-management/mdm/windowsadvancedthreatprotection-csp#configuration-telemetryreportingfrequency)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | None supported<br/>                                                                            |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv1.mof</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>Mofs\\DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

