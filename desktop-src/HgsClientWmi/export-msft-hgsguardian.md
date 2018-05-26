---
title: Export method of the MSFT\_HgsGuardian class
description: Exports a guardian to an XML file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9a1c2fc3-cd34-480a-a51e-8c12076edc40
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Export method
- Export method, MSFT_HgsGuardian class
- MSFT_HgsGuardian class, Export method
topic_type:
- apiref
api_name:
- MSFT_HgsGuardian.Export
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Export method of the MSFT\_HgsGuardian class

Exports a guardian to an XML file.

## Syntax


```mof
uint32 Export(
  [in] string           Path,
  [in] MSFT_HgsGuardian InputObject
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The path to the file to write an XML representation of the guardian.

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

A [**MSFT\_HgsGuardian**](msft-hgsguardian.md) object containing the guardian to export.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Hgs<br/>                                                    |
| MOF<br/>                      | <dl> <dt>HgsClientWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>HgsClientWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_HgsGuardian**](msft-hgsguardian.md)
</dt> </dl>

 

 





