---
title: GetInt32Property method of the Win32_RDMSVirtualDesktopCollection class
description: Retrieves an integer property from a virtual desktop collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 18ffca65-e7c0-4b17-902f-d74b2a81aba2
ms.tgt_platform: multiple
keywords:
- GetInt32Property method Remote Desktop Services
- GetInt32Property method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection class
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , GetInt32Property method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.GetInt32Property
api_location:
- RDMS.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetInt32Property method of the Win32\_RDMSVirtualDesktopCollection class

Retrieves an integer property from a virtual desktop collection.

## Syntax


```mof
uint32 GetInt32Property(
  [in]  string Key,
  [out] sint32 Value
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

A key that identifies the property to retrieve.

</dd> <dt>

*Value* \[out\]
</dt> <dd>

An integer that receives the retrieved value.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                      |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                 |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                                   |
| Header<br/>                   | <dl> <dt>Microsoft.diagnostics.appanalysis.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>                            |



## See also

<dl> <dt>

[**Win32\_RDMSVirtualDesktopCollection**](win32-rdmsvirtualdesktopcollection.md)
</dt> </dl>

 

 





