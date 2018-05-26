---
title: Signature
description: Specifies the signature for the Physical Disk resource. The following table summarizes the attributes of the Signature property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7c8869f5-73ae-429f-8692-db8b518e8ccd
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Signature Failover Cluster ,for physical disks
- Signature Failover Cluster
topic_type:
- apiref
api_name:
- Signature
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Signature

\[The **Signature** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [**DiskSignature**](disksignature.md) property.\]

Specifies the signature for the [Physical Disk](physical-disk.md) resource. The following table summarizes the attributes of the **Signature** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Status<br/>    | Required<br/>                                  |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 0<br/>                                         |



 

## Remarks

The **Signature** property specifies an identifier for the disk.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Signature** can be set with the following example code.


```C++
DWORD          SignatureData = 12343;
CLUSPROP_DWORD SignatureValue;

SignatureValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
SignatureValue.cbLength  = sizeof(DWORD);
SignatureValue.dw        = SignatureData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**DiskSignature**](disksignature.md)
</dt> </dl>

 

 





