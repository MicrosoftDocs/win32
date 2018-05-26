---
title: MSISCSITARGET\_SAPAvailableForElement class
description: Associates a Service Access Point (SAP) with a managed element, which indicates that the SAP is available for only the associated managed element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1eec3130-9454-4599-a08d-36d89c5a5550
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_SAPAvailableForElement class iSCSI Software Target API
- MSISCSITARGET_SAPAvailableForElement class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_SAPAvailableForElement
- MSISCSITARGET_SAPAvailableForElement.AvailableSAP
- MSISCSITARGET_SAPAvailableForElement.ManagedElement
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSISCSITARGET\_SAPAvailableForElement class

Associates a Service Access Point (SAP) with a managed element, which indicates that the SAP is available for only the associated managed element. An SAP that is not associated in an instance of this class is assumed to be generally available.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_SAPAvailableForElement : CIM_SAPAvailableForElement
{
  CIM_ServiceAccessPoint REF AvailableSAP;
  CIM_ManagedElement     REF ManagedElement;
};
```

## Members

The **MSISCSITARGET\_SAPAvailableForElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_SAPAvailableForElement** class has these properties.

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

This property is inherited from [**CIM\_SAPAvailableForElement**](cim-sapavailableforelement.md).

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

This property is inherited from [**CIM\_SAPAvailableForElement**](cim-sapavailableforelement.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SAPAvailableForElement**](cim-sapavailableforelement.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





