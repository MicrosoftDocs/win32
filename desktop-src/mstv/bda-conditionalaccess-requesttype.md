---
title: BDA\_CONDITIONALACCESS\_REQUESTTYPE enumeration
description: Specifies the type of content access that a media sink device (MSD) is requesting.
ms.assetid: b21bca45-e219-4670-b209-9d7a63fbd65c
keywords:
- BDA_CONDITIONALACCESS_REQUESTTYPE enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- BDA_CONDITIONALACCESS_REQUESTTYPE
api_location:
- bdatypes.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BDA\_CONDITIONALACCESS\_REQUESTTYPE enumeration

Specifies the type of content access that a media sink device (MSD) is requesting.

## Syntax


```C++
typedef enum BDA_CONDITIONALACCESS_REQUESTTYPE { 
  CONDITIONALACCESS_ACCESS_UNSPECIFIED                       = 0,
  CONDITIONALACCESS_ACCESS_NOT_POSSIBLE,
  CONDITIONALACCESS_ACCESS_POSSIBLE,
  CONDITIONALACCESS_ACCESS_POSSIBLE_NO_STREAMING_DISRUPTION
} BDA_CONDITIONALACCESS_REQUESTTYPE;
```



## Constants

<dl> <dt>

<span id="CONDITIONALACCESS_ACCESS_UNSPECIFIED"></span><span id="conditionalaccess_access_unspecified"></span>**CONDITIONALACCESS\_ACCESS\_UNSPECIFIED**
</dt> <dd>

Unspecified.

</dd> <dt>

<span id="CONDITIONALACCESS_ACCESS_NOT_POSSIBLE"></span><span id="conditionalaccess_access_not_possible"></span>**CONDITIONALACCESS\_ACCESS\_NOT\_POSSIBLE**
</dt> <dd>

The MSD cannot provide access to the content.

</dd> <dt>

<span id="CONDITIONALACCESS_ACCESS_POSSIBLE"></span><span id="conditionalaccess_access_possible"></span>**CONDITIONALACCESS\_ACCESS\_POSSIBLE**
</dt> <dd>

The MSD can provide access to the content.

</dd> <dt>

<span id="CONDITIONALACCESS_ACCESS_POSSIBLE_NO_STREAMING_DISRUPTION"></span><span id="conditionalaccess_access_possible_no_streaming_disruption"></span>**CONDITIONALACCESS\_ACCESS\_POSSIBLE\_NO\_STREAMING\_DISRUPTION**
</dt> <dd>

The MSD can provide access to the content; however, the media transform device (MTD) should not disrupt streaming.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[**IBDA\_ConditionalAccessEx::CheckEntitlementToken**](/windows/win32/bdaiface/nf-bdaiface-ibda_conditionalaccessex-checkentitlementtoken?branch=master)
</dt> </dl>

 

 





