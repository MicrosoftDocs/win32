---
title: MSFT\_StorageFaultDomainToStorageFaultDomain class
description: Association between an MSFT\_StorageFaultDomain object and its ancestor or descendent MSFT\_StorageFaultDomain objects.
ms.assetid: A45632F0-7607-49F8-BB6C-FF1043A9E173
keywords:
- MSFT_StorageFaultDomainToStorageFaultDomain class Windows Storage Management API
- MSFT_StorageFaultDomainToStorageFaultDomain class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageFaultDomainToStorageFaultDomain
- MSFT_StorageFaultDomainToStorageFaultDomain.SourceStorageFaultDomain
- MSFT_StorageFaultDomainToStorageFaultDomain.TargetStorageFaultDomain
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_StorageFaultDomainToStorageFaultDomain class

Association between an [**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md) object and its ancestor or descendent **MSFT\_StorageFaultDomain** objects.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageFaultDomainToStorageFaultDomain
{
  MSFT_StorageFaultDomain REF SourceStorageFaultDomain;
  MSFT_StorageFaultDomain REF TargetStorageFaultDomain;
};
```

## Members

The **MSFT\_StorageFaultDomainToStorageFaultDomain** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageFaultDomainToStorageFaultDomain** class has these properties.

<dl> <dt>

**SourceStorageFaultDomain**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**TargetStorageFaultDomain**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)
</dt> </dl>

 

 





