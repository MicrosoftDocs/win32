---
title: MDM_Policy_Result01_System02 class
description: The MDM\_Policy\_Result01\_System02 class represents the System policies available.
ms.assetid: 9A0D9688-9062-429F-897F-75705DC8FD79
keywords:
- MDM_Policy_Result01_System02 class
- MDM_Policy_Result01_System02 class, described
topic_type:
- apiref
api_name:
- MDM_Policy_Result01_System02
- MDM_Policy_Result01_System02.InstanceID
- MDM_Policy_Result01_System02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_Policy\_Result01\_System02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_Policy\_Result01\_System02** class represents the System policies available. These policies determine System configurations that are allowed.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_Policy_Result01_System02
{
  string InstanceID;
  string ParentID;
  sint32 AllowBuildPreview;
  sint32 AllowEmbeddedMode;
  sint32 AllowExperimentation;
  sint32 AllowFontProviders;
  sint32 AllowLocation;
  sint32 AllowStorageCard;
  sint32 AllowTelemetry;
  string TelemetryProxy;
  sint32 AllowUserToResetPhone;
  string BootStartDriverInitialization;
  sint32 DisableEnterpriseAuthProxy;
  sint32 DisableOneDriveFileSync;
  string DisableSystemRestore;
  sint32 LimitEnhancedDiagnosticDataWindowsAnalytics;
  sint32 FeedbackHubAlwaysSaveDiagnosticsLocally;
};
```

## Members

The **MDM\_Policy\_Result01\_System02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Policy\_Result01\_System02** class has these properties.

<dl> <dt>

[AllowBuildPreview](/windows/client-management/mdm/policy-csp-system#system-allowbuildpreview)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowEmbeddedMode](/windows/client-management/mdm/policy-csp-system#system-allowembeddedmode)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowExperimentation](/windows/client-management/mdm/policy-csp-system#system-allowexperimentation)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowFontProviders](/windows/client-management/mdm/policy-csp-system#system-allowfontproviders)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowLocation](/windows/client-management/mdm/policy-csp-system#system-allowlocation)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowStorageCard](/windows/client-management/mdm/policy-csp-system#system-allowstoragecard)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowTelemetry](/windows/client-management/mdm/policy-csp-system#system-allowtelemetry)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowUserToResetPhone](/windows/client-management/mdm/policy-csp-system#system-allowusertoresetphone)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[BootStartDriverInitialization](/windows/client-management/mdm/policy-csp-system#system-bootstartdriverinitialization)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisableEnterpriseAuthProxy](/windows/client-management/mdm/policy-csp-system#system-disableenterpriseauthproxy)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisableOneDriveFileSync](/windows/client-management/mdm/policy-csp-system#system-disableonedrivefilesync)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisableSystemRestore](/windows/client-management/mdm/policy-csp-system#system-disablesystemrestore)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[FeedbackHubAlwaysSaveDiagnosticsLocally](/windows/client-management/mdm/policy-csp-system#system-feedbackhubalwayssavediagnosticslocally)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "System".

</dd> <dt>

[LimitEnhancedDiagnosticDataWindowsAnalytics](/windows/client-management/mdm/policy-csp-system#system-limitenhanceddiagnosticdatawindowsanalytics)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
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

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/Policy/Result"

</dd> <dt>

[TelemetryProxy](/windows/client-management/mdm/policy-csp-system#system-telemetryproxy)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM\\DMMap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

