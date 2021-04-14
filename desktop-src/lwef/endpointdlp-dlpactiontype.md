---
description: Specifies the action type of an endpoint Data Loss Prevention (DLP) operation.
title: DlpActionType enumeration (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpActionType
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# DlpActionType enumeration

Specifies the action type of an endpoint Data Loss Prevention (DLP) operation.

## Syntax


```C++
typedef enum  
{
    DlpActionTypeCopyToRemovableMedia = 0,
    DlpActionTypeCopyToNetworkShare = 1,
    DlpActionTypeCopyToClipboard = 2,
    DlpActionTypePrint = 3,
    DlpActionTypeScreenClip = 4,
    DlpActionTypeAccessByUnallowedApp = 5,
    DlpActionTypeCloudAppEgress = 6,
    DlpActionTypeAccessByBluetoothApp = 7,
    DlpActionTypeAccessByRDPApp = 8,
    DlpActionTypeCount = 9
} DlpActionType;
```


## Constants

<dl> <dt>

*DlpActionTypeCopyToRemovableMedia*
</dt> <dd>

A copy operation to removable media.

</dd> </dl>

<dl> <dt>

*DlpActionTypeCopyToNetworkShare*
</dt> <dd>

A copy operation to a shared network folder.

</dd> </dl>

<dl> <dt>

*DlpActionTypeCopyToClipboard*
</dt> <dd>

A copy operation to the clipboard.

</dd> </dl>

<dl> <dt>

*DlpActionTypePrint*
</dt> <dd>

A print operation.

</dd> </dl>


<dl> <dt>

*DlpActionTypeScreenClip*
</dt> <dd>

A screen capture operation.

</dd> </dl>

<dl> <dt>

*DlpActionTypeAccessByUnallowedApp*
</dt> <dd>

An operation performed by an unallowed app.

</dd> </dl>


<dl> <dt>

*DlpActionTypeCloudAppEgress*
</dt> <dd>

An operation targeted to a cloud location.

</dd> </dl>

<dl> <dt>

*DlpActionTypeAccessByBluetoothApp*
</dt> <dd>

An operation that includes access by a bluetooth app.

</dd> </dl>

<dl> <dt>

*DlpActionTypeAccessByRDPApp*
</dt> <dd>

An operation that includes access by a remote desktop.

</dd> </dl>

<dl> <dt>

*DlpActionTypeCount*
</dt> <dd>

The maximum value of the enumeration.

</dd> </dl>
 

## Remarks

Values from this enumeration are used by the [DLP_APP_OP_ENLIGHTENED_LEVEL](endpointdlp-dlp_app_op_enlightened_level.md) structure.

## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |

