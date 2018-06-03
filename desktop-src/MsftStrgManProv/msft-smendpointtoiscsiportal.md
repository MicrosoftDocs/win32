---
title: MSFT\_SMEndpointToiSCSIPortal class
description: Represents a relationship between an endpoint and an iSCSI portal.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c5bd7892-8eae-4e8e-a719-2a60995b8d0c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMEndpointToiSCSIPortal class
- MSFT_SMEndpointToiSCSIPortal class, described
topic_type:
- apiref
api_name:
- MSFT_SMEndpointToiSCSIPortal
- MSFT_SMEndpointToiSCSIPortal.Parent
- MSFT_SMEndpointToiSCSIPortal.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMEndpointToiSCSIPortal class

Represents a relationship between an endpoint and an iSCSI portal.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMEndpointToiSCSIPortal
{
  MSFT_SMEndpoint            REF Parent;
  MSFT_SMiSCSIPortalEndpoint REF Child;
};
```

## Members

The **MSFT\_SMEndpointToiSCSIPortal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMEndpointToiSCSIPortal** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMiSCSIPortalEndpoint**](msft-smiscsiportalendpoint.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMiSCSIPortalEndpoint**](msft-smiscsiportalendpoint.md) object that represents the iSCSI portal in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMEndpoint**](msft-smendpoint.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMEndpoint**](msft-smendpoint.md) object that represents the endpoint in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





