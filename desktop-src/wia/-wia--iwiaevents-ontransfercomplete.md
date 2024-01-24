---
description: Event that occurs when a data transfer is completed successfully.
ms.assetid: 6110867b-21e2-48ab-97ad-0e084a0ccf07
title: Wia.OnTransferComplete event
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Wia.OnTransferComplete
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Wia.OnTransferComplete event

Event that occurs when a data transfer is completed successfully.

## Syntax


```JScript
Wia.OnTransferComplete(
  Item,
  Path
)
```



## Parameters

<dl> <dt>

*Item* 
</dt> <dd>

The [**Item**](-wia-item.md) object transferred.

</dd> <dt>

*Path* 
</dt> <dd>

The path and file name of the transferred image.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

WIA notifies the script or application when a data transfer, image or sound, completes successfully. Implement the **objWia**\_**OnTransferComplete()** subroutine to allow your script or application to respond to the completion of the data transfer.

For example, you might want a script to display an image after it is transferred.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




