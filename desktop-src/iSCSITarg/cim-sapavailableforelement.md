---
title: CIM\_SAPAvailableForElement class
description: CIM\_SAPAvailableForElement conveys the semantics of a Service Access Point that is available for a ManagedElement.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f922a72f-96a1-4998-b4f4-25a30a790b2e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_SAPAvailableForElement class iSCSI Software Target API", "CIM_SAPAvailableForElement class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_SAPAvailableForElement
- CIM_SAPAvailableForElement.AvailableSAP
- CIM_SAPAvailableForElement.ManagedElement
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_SAPAvailableForElement class

CIM\_SAPAvailableForElement conveys the semantics of a Service Access Point that is available for a ManagedElement. When CIM\_SAPAvailableForElement is not instantiated, then the SAP is assumed to be generally available. If instantiated, the SAP is available only for the associated ManagedElements. For example, a device might provide management access through a URL. This association allows the URL to be advertised for the device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Service")]
class CIM_SAPAvailableForElement
{
  CIM_ServiceAccessPoint REF AvailableSAP;
  CIM_ManagedElement     REF ManagedElement;
};
```

## Members

The **CIM\_SAPAvailableForElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SAPAvailableForElement** class has these properties.

<dl> <dt>

**AvailableSAP**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The Service Access Point that is available.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ManagedElement for which the SAP is available.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



 

 





