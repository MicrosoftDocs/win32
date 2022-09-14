---
description: The WPD\_OPERATION\_STATES enumeration values describe the current state of an operation in progress.
ms.assetid: a002f735-e385-4c7c-b734-e70a9c6842ca
title: WPD_OPERATION_STATES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_OPERATION_STATES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_OPERATION\_STATES enumeration

The **WPD\_OPERATION\_STATES** enumeration values describe the current state of an operation in progress.

## Syntax


```C++
typedef enum tagWPD_OPERATION_STATES { 
  WPD_OPERATION_STATE_UNSPECIFIED  = 0,
  WPD_OPERATION_STATE_STARTED      = 1,
  WPD_OPERATION_STATE_RUNNING      = 2,
  WPD_OPERATION_STATE_PAUSED       = 3,
  WPD_OPERATION_STATE_CANCELLED    = 4,
  WPD_OPERATION_STATE_FINISHED     = 5,
  WPD_OPERATION_STATE_ABORTED      = 6
} WPD_OPERATION_STATES;
```



## Constants

<dl> <dt>

<span id="WPD_OPERATION_STATE_UNSPECIFIED"></span><span id="wpd_operation_state_unspecified"></span>**WPD\_OPERATION\_STATE\_UNSPECIFIED**
</dt> <dd>

The current operation is in an unspecified state (not set) and unknown.

</dd> <dt>

<span id="WPD_OPERATION_STATE_STARTED"></span><span id="wpd_operation_state_started"></span>**WPD\_OPERATION\_STATE\_STARTED**
</dt> <dd>

The operation is started.

</dd> <dt>

<span id="WPD_OPERATION_STATE_RUNNING"></span><span id="wpd_operation_state_running"></span>**WPD\_OPERATION\_STATE\_RUNNING**
</dt> <dd>

The operation is running.

</dd> <dt>

<span id="WPD_OPERATION_STATE_PAUSED"></span><span id="wpd_operation_state_paused"></span>**WPD\_OPERATION\_STATE\_PAUSED**
</dt> <dd>

The operation is paused.

</dd> <dt>

<span id="WPD_OPERATION_STATE_CANCELLED"></span><span id="wpd_operation_state_cancelled"></span>**WPD\_OPERATION\_STATE\_CANCELLED**
</dt> <dd>

The operation is canceled.

</dd> <dt>

<span id="WPD_OPERATION_STATE_FINISHED"></span><span id="wpd_operation_state_finished"></span>**WPD\_OPERATION\_STATE\_FINISHED**
</dt> <dd>

The operation is finished.

</dd> <dt>

<span id="WPD_OPERATION_STATE_ABORTED"></span><span id="wpd_operation_state_aborted"></span>**WPD\_OPERATION\_STATE\_ABORTED**
</dt> <dd>

The operation is aborted.

</dd> </dl>

## Remarks

These values are received in the application-defined callback ([**IPortableDeviceEventCallback**](/windows/desktop/api/PortableDeviceApi/nn-portabledeviceapi-iportabledeviceeventcallback)).

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




