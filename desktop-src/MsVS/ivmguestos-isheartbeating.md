---
title: IVMGuestOS IsHeartbeating property
description: The IsHeartbeating property indicates whether the guest operating system appears live. The Additions will send a periodic heartbeat to Virtual Server while the guest operating system is running.
ms.assetid: 1036266b-97d7-4b52-8955-5a5a4b479e8b
keywords:
- IsHeartbeating property Virtual Server
- IsHeartbeating property Virtual Server , IVMGuestOS interface
- IVMGuestOS interface Virtual Server , IsHeartbeating property
- IsHeartbeating property Virtual Server , VMGuestOS interface
- VMGuestOS interface Virtual Server , IsHeartbeating property
topic_type:
- apiref
api_name:
- IVMGuestOS.IsHeartbeating
- IVMGuestOS.get_IsHeartbeating
- VMGuestOS.IsHeartbeating
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMGuestOS::IsHeartbeating property

The **IsHeartbeating** property indicates whether the guest operating system appears live. The Additions will send a periodic heartbeat to Virtual Server while the guest operating system is running.

This property is read-only.

## Syntax


```C++
HRESULT get_IsHeartbeating(
  [out] VARIANT_BOOL *heartBeating
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMGuestOS.IsHeartbeating( _
  ByRef heartBeating _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if a heartbeat is detected.

This property value is read-only.

## Error codes



| Name                                                                                                    | Meaning                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                        | The operation was successful.<br/>                                                                                                 |
| <dl> <dt>E\_POINTER</dt> </dl>                   | The *heartBeating* parameter is **NULL**.<br/>                                                                                     |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>           | The configuration is unknown.<br/>                                                                                                 |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> </dl>      | The virtual machine is not running.<br/>                                                                                           |
| <dl> <dt>VM\_E\_ADDITIONS\_NOT\_AVAIL</dt> </dl> | The virtual machine is not fully booted, Additions are not installed, or the installed version does not support this feature.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>           | An unexpected error has occurred.<br/>                                                                                             |



## Remarks

When Additions is installed in the guest operating system, a regular 'tick' or heartbeat is sent from the virtual machine session to Virtual Server. If the guest operating system is heavily loaded, it's possible that Virtual Server will receive fewer heartbeats than expected. If no heartbeat is detected, it is possible that the guest operating system has stopped responding or has crashed.

By default, a virtual machine produces ten heartbeat ticks per minute. If no heartbeat ticks are detected for an entire minute, Virtual Server will attempt to restart the virtual machine session once every ten seconds for up to two minutes. This behavior is controlled by the following key values in the virtual machine session's configuration file.



| Configuration key                                 | Default    | Description                                                                                                              |
|---------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------|
| integration/microsoft/heartbeat/time              | 60 seconds | Length of the block of time in seconds used to generate heartbeat ticks.                                                 |
| integration/microsoft/heartbeat/rate              | 10         | Number of ticks generated in each heartbeat time block.                                                                  |
| integration/microsoft/heartbeat/failure\_interval | 10 seconds | Number of seconds between restart attempts, once no heartbeat ticks are received within a specific heartbeat time block. |
| integration/microsoft/heartbeat/failure\_attempts | 12         | Number of restart attempts made.                                                                                         |



 

The virtual machine must be running (that is, fully booted and not shutting down) and Additions must be installed when this method is invoked.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> </dl>

 

 





