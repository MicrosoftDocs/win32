---
title: CreatePropertyValue method of the MSFT\_FSRMClassificationPropertyValue class
description: Creates a classification property value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 483678a6-96d5-4a6b-b8b9-60eecdb1e19b
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- CreatePropertyValue method File Server Resource Manager
- CreatePropertyValue method File Server Resource Manager , MSFT_FSRMClassificationPropertyValue class
- MSFT_FSRMClassificationPropertyValue class File Server Resource Manager , CreatePropertyValue method
topic_type:
- apiref
api_name:
- MSFT_FSRMClassificationPropertyValue.CreatePropertyValue
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreatePropertyValue method of the MSFT\_FSRMClassificationPropertyValue class

Creates a classification property value.

## Syntax


```mof
uint64 CreatePropertyValue(
  [in]  string                               Name,
  [in]  string                               Description,
  [out] MSFT_FSRMClassificationPropertyValue PropertyValue
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the property value. The *Name* parameter is used for both the **DisplayName** and **Name** properties of the returned [**MSFT\_FSRMClassificationPropertyValue**](msft-fsrmclassificationpropertyvalue.md) instance.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description of the property value.

</dd> <dt>

*PropertyValue* \[out\]
</dt> <dd>

Returns an instance of the [**MSFT\_FSRMClassificationPropertyValue**](msft-fsrmclassificationpropertyvalue.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_FSRMClassificationPropertyValue**](msft-fsrmclassificationpropertyvalue.md)
</dt> </dl>

 

 





