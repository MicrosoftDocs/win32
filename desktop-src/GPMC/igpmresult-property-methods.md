---
title: IGPMResult Property Methods
description: The property methods of the IGPMResult interface get the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation .
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 34b9c8da-9a5f-4415-b62e-31083578c802
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMResult Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMResult Property Methods
- IGPMResult.Result
- IGPMResult.get_Result
- IGPMResult.Status
- IGPMResult.get_Status
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IGPMResult Property Methods

The property methods of the [**IGPMResult**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmresult?branch=master) interface get the properties described in the following table. For a general discussion of property methods, see [**Interface Property Methods**](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation .

## Properties

<dl> <dt>

**Result**
</dt> <dd> <dl>

Pointer to a **VARIANT** that receives the result of various types of GPO operations. This property is the location at which an **IDispatch** interface pointer can be stored.

For calls to the [**IGPMGPO::Backup**](/windows/previous-versions/Gpmgmt/nf-gpmgmt-igpmgpo-backup?branch=master) method, the result is a pointer to an [**IGPMBackup**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmbackup?branch=master) interface. For calls to [**IGPMDomain::RestoreGPO**](/windows/previous-versions/Gpmgmt/nf-gpmgmt-igpmdomain-restoregpo?branch=master), [**IGPMGPO::Import**](/windows/previous-versions/Gpmgmt/nf-gpmgmt-igpmgpo-import?branch=master), and [**IGPMGPO::CopyTo**](/windows/previous-versions/Gpmgmt/nf-gpmgmt-igpmgpo-copyto?branch=master), the result is a pointer to an [**IGPMGPO**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmgpo?branch=master) interface.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Variant**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Result(
  [out] VARIANT* pvarResult
);
```


</dt> </dl> </dd> <dt>

**Status**
</dt> <dd> <dl>

Returns a reference to the [**GPMStatusMsgCollection**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmstatusmsgcollection?branch=master) object.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Status(
  [out] ** IGPMStatusMsgCollection,
  [out]  ppIGPMStatusMsgCollection
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
| IID<br/>                      | IID\_IGPMResult is defined as 86DFF7E9-F76F-42AB-9570-CEBC6BE8A52D<br/>         |



## See also

<dl> <dt>

[**IGPMResult**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmresult?branch=master)
</dt> <dt>

[**IGPMGPO**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmgpo?branch=master)
</dt> <dt>

[**IGPMBackup**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmbackup?branch=master)
</dt> <dt>

[**IGPMDomain**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmdomain?branch=master)
</dt> <dt>

[**IGPMStatusMsgCollection**](/windows/previous-versions/Gpmgmt/nn-gpmgmt-igpmstatusmsgcollection?branch=master)
</dt> </dl>

 

 





