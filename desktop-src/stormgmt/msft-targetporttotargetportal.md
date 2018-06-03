---
title: MSFT\_TargetPortToTargetPortal class
description: Association between TargetPort and TargetPortal.
ms.assetid: 83174B58-7A06-4431-8453-CA948CD900D4
keywords:
- MSFT_TargetPortToTargetPortal class Windows Storage Management API
- MSFT_TargetPortToTargetPortal class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_TargetPortToTargetPortal
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

# MSFT\_TargetPortToTargetPortal class

Association between [**TargetPort**](msft-targetport.md) and [**TargetPortal**](msft-targetportal.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_TargetPortToTargetPortal
{
  MSFT_TargetPort   REF TargetPort;
  MSFT_TargetPortal REF TargetPortal;
};
```

## Members

The **MSFT\_TargetPortToTargetPortal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_TargetPortToTargetPortal** class has these properties.

<dl> <dt>

[**TargetPort**](msft-targetport.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_TargetPort**](msft-targetport.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

[**TargetPortal**](msft-targetportal.md)
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_TargetPortal**](msft-targetportal.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

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

[**MSFT\_TargetPort**](msft-targetport.md)
</dt> <dt>

[**MSFT\_TargetPortal**](msft-targetportal.md)
</dt> </dl>

 

 





