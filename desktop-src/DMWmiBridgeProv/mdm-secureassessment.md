---
title: MDM_SecureAssessment class
description: The MDM\_SecureAssessmentclass is used to provide configuration information for the secure assessment browser.
ms.assetid: ad456f01-c77d-428b-a8bf-03e9ae106e60
keywords:
- MDM_SecureAssessment class
- MDM_SecureAssessment class, described
topic_type:
- apiref
api_name:
- MDM_SecureAssessment
- MDM_SecureAssessment.InstanceID
- MDM_SecureAssessment.ParentID
api_location:
- Mofs\DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_SecureAssessment class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_SecureAssessment**class is used to provide configuration information for the secure assessment browser.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv1")]
class MDM_SecureAssessment
{
  string  InstanceID;
  string  ParentID;
  string  LaunchURI;
  string  TesterAccount;
  boolean AllowTextSuggestions;
  boolean RequirePrinting;
  boolean AllowScreenMonitoring;
};
```

## Members

The **MDM\_SecureAssessment** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_SecureAssessment** class has these properties.

<dl> <dt>

[AllowScreenMonitoring](/windows/client-management/mdm/secureassessment-csp#allowscreenmonitoring)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowTextSuggestions](/windows/client-management/mdm/secureassessment-csp#AllowTextSuggestions)
</dt> <dd> <dl> <dt>

Data type: **boolean**
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

Identifies the name of the parent node. For this class, the string is "SecureAssessment".

</dd> <dt>

[LaunchURI](/windows/client-management/mdm/secureassessment-csp#launchuri)
</dt> <dd> <dl> <dt>

Data type: **string**
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

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/"

</dd> <dt>

[RequirePrinting](/windows/client-management/mdm/secureassessment-csp#requireprinting)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[TesterAccount](/windows/client-management/mdm/secureassessment-csp#testeraccount)
</dt> <dd> <dl> <dt>

Data type: **string**
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



 

