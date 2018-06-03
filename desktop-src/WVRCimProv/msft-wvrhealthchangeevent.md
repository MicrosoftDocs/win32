---
title: MSFT\_WvrHealthChangeEvent class
description: Represents health events on Storage Replica objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8dc9776e-c98c-4aa8-8e99-32c0633bcbce
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WvrHealthChangeEvent class
- MSFT_WvrHealthChangeEvent class, described
topic_type:
- apiref
api_name:
- MSFT_WvrHealthChangeEvent
- MSFT_WvrHealthChangeEvent.HealthInformation
api_location:
- wvrcimprov.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WvrHealthChangeEvent class

Represents health events on Storage Replica objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Indication, dynamic, provider("wvrcimprov"), AMENDMENT]
class MSFT_WvrHealthChangeEvent
{
  MSFT_WvrHealth HealthInformation;
};
```

## Members

The **MSFT\_WvrHealthChangeEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WvrHealthChangeEvent** class has these properties.

<dl> <dt>

**HealthInformation**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_WvrHealth**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_WvrHealth**](msft-wvrhealth.md)")
</dt> </dl>

An embedded instance of a [**MSFT\_WvrHealth**](msft-wvrhealth.md) object containing health information.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



 

 





