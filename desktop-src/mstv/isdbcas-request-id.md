---
title: ISDBCAS\_REQUEST\_ID enumeration
description: Contains command codes for conditional access system (CAS) commands for Integrated Services Digital Broadcasting (ISDB).
ms.assetid: 5c8a97bb-9d8b-4f4f-aeab-e8bf199a652e
keywords:
- ISDBCAS_REQUEST_ID enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- ISDBCAS_REQUEST_ID
api_location:
- bdatypes.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# ISDBCAS\_REQUEST\_ID enumeration

Contains command codes for conditional access system (CAS) commands for Integrated Services Digital Broadcasting (ISDB).For more information, refer to ARIB STD-B25, *Conditional Access System Specifications For Digital Broadcasting*. (This resource may not be available in some languages and countries.)

## Syntax


```C++
typedef enum ISDBCAS_REQUEST_ID { 
  ISDBCAS_REQUEST_ID_EMG  = 0x38,
  ISDBCAS_REQUEST_ID_EMD  = 0x3A
} ISDBCAS_REQUEST_ID;
```



## Constants

<dl> <dt>

<span id="ISDBCAS_REQUEST_ID_EMG"></span><span id="isdbcas_request_id_emg"></span>**ISDBCAS\_REQUEST\_ID\_EMG**
</dt> <dd>

Receive EMM individual message. The command data is a [**BDA\_ISDBCAS\_EMG\_REQ**](bda-isdbcas-emg-req.md) structure.

</dd> <dt>

<span id="ISDBCAS_REQUEST_ID_EMD"></span><span id="isdbcas_request_id_emd"></span>**ISDBCAS\_REQUEST\_ID\_EMD**
</dt> <dd>

Acquire automatic display message.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Header<br/>                   | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[**IBDA\_ISDBConditionalAccess::SetIsdbCasRequest**](/windows/desktop/api/bdaiface/nf-bdaiface-ibda_isdbconditionalaccess-setisdbcasrequest)
</dt> </dl>

 

 





