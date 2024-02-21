---
title: RemoteSessionActionType enumeration
description: Used to specify the type of remote action.
ms.assetid: C0DA0FA2-6FE0-4B40-B169-4592A1BE2AD6
ms.tgt_platform: multiple
keywords:
- RemoteSessionActionType enumeration Remote Desktop Services
topic_type:
- apiref
api_name:
- RemoteSessionActionType
api_location:
- MsTscAx.dll
api_type:
- LibDef
ms.topic: reference
ms.date: 05/31/2018
---

# RemoteSessionActionType enumeration

Used to specify the type of remote action.

## Syntax


```C++
typedef enum _RemoteSessionActionType { 
  RemoteSessionActionCharms        = 0,
  RemoteSessionActionAppbar        = 1,
  RemoteSessionActionSnap          = 2,
  RemoteSessionActionStartScreen   = 3,
  RemoteSessionActionAppSwitch     = 4,
  RemoteSessionActionActionCenter  = 5,
  RemoteSessionActionTaskManager   = 6
} RemoteSessionActionType;
```



## Constants


### RemoteSessionActionCharms

Displays the charms in the remote session.

### RemoteSessionActionAppbar

Displays the app bar in the remote session.

### RemoteSessionActionSnap

Docks the application in the remote session. This option has been deprecated and should not be used.

### RemoteSessionActionStartScreen

Causes the start screen to be displayed in the remote session.

### RemoteSessionActionAppSwitch

Causes the application switch window to be displayed in the remote session. This is the same as the user pressing Alt+Tab.

### RemoteSessionActionActionCenter

Causes the Action Center to be displayed in the remote session. This is the same as the user pressing Win+A.

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012 and Windows 8:** This value is not supported before Windows Server 2016 and Windows 10.

### RemoteSessionActionTaskManager

Causes the Task Manager to be displayed in the remote session. Introduced in Windows 11, version 24H2.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsRdpClient8::SendRemoteAction**](imsrdpclient8-sendremoteaction.md)
</dt> </dl>

 

 





