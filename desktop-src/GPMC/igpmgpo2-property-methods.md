---
title: IGPMGPO2 Property Methods
description: The property methods of the IGPMGPO2 interface get and set the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6626e709-a78d-4df8-844b-aa1254d5ec0f
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMGPO2 Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMGPO2 Property Methods
- IGPMGPO.Description
- IGPMGPO.put_Description
- IGPMGPO.get_Description
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IGPMGPO2 Property Methods

The property methods of the **IGPMGPO2** interface get and set the properties described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation.

## Properties

<dl> <dt>

**Description**
</dt> <dd> <dl>

GPO comment or description.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_Description(
  [in] BSTR newVal
);
HRESULT get_Description(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMGPO2 is defined as 8A66A210-B78B-4d99-88E2-C306A817C925<br/>           |



## See also

<dl> <dt>

[**IGPMGPO**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmgpo?branch=master)
</dt> <dt>

[**IGPMGPOCollection**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmgpocollection?branch=master)
</dt> </dl>

 

 





