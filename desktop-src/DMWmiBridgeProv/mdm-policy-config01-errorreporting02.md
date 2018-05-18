---
title: MDM\_Policy\_Config01\_ErrorReporting02 class
description: The MDM\_Policy\_Config01\_ErrorReporting02 class configures the error reporting policies.
ms.assetid: '41067b5e-0db5-43b3-b1d5-2d6c54c35388'
keywords: ["MDM_Policy_Config01_ErrorReporting02 class", "MDM_Policy_Config01_ErrorReporting02 class, described"]
topic_type:
- apiref
api_name:
- MDM_Policy_Config01_ErrorReporting02
- MDM_Policy_Config01_ErrorReporting02.InstanceID
- MDM_Policy_Config01_ErrorReporting02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
---

# MDM\_Policy\_Config01\_ErrorReporting02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The MDM\_Policy\_Config01\_ErrorReporting02 class configures the error reporting policies.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_Policy_Config01_ErrorReporting02
{
  string InstanceID;
  string ParentID;
  string CustomizeConsentSettings;
  string DisableWindowsErrorReporting;
  string DisplayErrorNotification;
  string DoNotSendAdditionalData;
  string PreventCriticalErrorDisplay;
};
```

## Members

The **MDM\_Policy\_Config01\_ErrorReporting02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Policy\_Config01\_ErrorReporting02** class has these properties.

<dl> <dt>

[CustomizeConsentSettings](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-errorreporting#errorreporting-customizeconsentsettings)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisableWindowsErrorReporting](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-errorreporting#errorreporting-disablewindowserrorreporting)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisplayErrorNotification](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-errorreporting#errorreporting-displayerrornotification)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DoNotSendAdditionalData](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-errorreporting#errorreporting-donotsendadditionaldata)
</dt> <dd> <dl> <dt>

Data type: **string**
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

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

</dd> <dt>

[PreventCriticalErrorDisplay](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-errorreporting#errorreporting-preventcriticalerrordisplay)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



 

 





