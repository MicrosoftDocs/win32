---
title: MSFT\_StorageAlertEvent class
description: Represents a storage alert event.
ms.assetid: 3DB2E42D-28BA-418C-8494-1C6FDCF44B98
keywords:
- MSFT_StorageAlertEvent class Windows Storage Management API
- MSFT_StorageAlertEvent class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageAlertEvent
- MSFT_StorageAlertEvent.AlertType
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageAlertEvent class

Represents a storage alert event.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Indication]
class MSFT_StorageAlertEvent : MSFT_StorageEvent
{
  UInt16 AlertType;
};
```

## Members

The **MSFT\_StorageAlertEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageAlertEvent** class has these properties.

<dl> <dt>

**AlertType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The alert type.



| Value                                                                                                                                         | Meaning                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl>                                          | Thin provisioning threshold reached<br/> |
| <span id="..."></span><dl> <dt>**...**</dt> </dl>                                      | Microsoft Reserved<br/>                  |
| <span id="0x8000.."></span><span id="0X8000.."></span><dl> <dt>**0x8000..**</dt> </dl> | Vendor Specific<br/>                     |



 

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageEvent**](msft-storageevent.md)
</dt> </dl>

 

 





