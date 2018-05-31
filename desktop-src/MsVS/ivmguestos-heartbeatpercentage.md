---
title: IVMGuestOS HeartbeatPercentage property
description: The HeartbeatPercentage property contains the percentage of expected heartbeats received over the past minute.
ms.assetid: 9f4c3f49-b95a-4945-ac88-83a7657326d9
keywords:
- HeartbeatPercentage property Virtual Server
- HeartbeatPercentage property Virtual Server , IVMGuestOS interface
- IVMGuestOS interface Virtual Server , HeartbeatPercentage property
- HeartbeatPercentage property Virtual Server , VMGuestOS interface
- VMGuestOS interface Virtual Server , HeartbeatPercentage property
topic_type:
- apiref
api_name:
- IVMGuestOS.HeartbeatPercentage
- IVMGuestOS.get_HeartbeatPercentage
- VMGuestOS.HeartbeatPercentage
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMGuestOS::HeartbeatPercentage property

The **HeartbeatPercentage** property contains the percentage of expected heartbeats received over the past minute.

This property is read-only.

## Syntax


```C++
HRESULT get_HeartbeatPercentage(
  [out] long *heartbeatPercentage
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
<td><pre><code>VMGuestOS.HeartbeatPercentage( _
  ByRef heartbeatPercentage _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The percentage of expected heartbeats received over the past minute.

This property value is read-only.

## Error codes



| Name                                                                                                    | Meaning                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                        | The operation was successful.<br/>                                                                                                 |
| <dl> <dt>E\_POINTER</dt> </dl>                   | *heartbeatPercentage* is **NULL**.<br/>                                                                                            |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>           | The configuration is unknown.<br/>                                                                                                 |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> </dl>      | The virtual machine is not running.<br/>                                                                                           |
| <dl> <dt>VM\_E\_ADDITIONS\_NOT\_AVAIL</dt> </dl> | The virtual machine is not fully booted, Additions are not installed, or the installed version does not support this feature.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>           | An unexpected error occurred.<br/>                                                                                                 |



## Remarks

The Additions will send a periodic heartbeat to Virtual Server while the guest operating system is running. If the guest operating system is heavily loaded, it's possible that Virtual Server will receive fewer heartbeats than expected. If the heartbeat percentage drops to zero, it's possible that the guest operating system has stopped responding or has crashed. The virtual machine must be running (that is, fully booted and not shutting down) and Additions must be installed when this property is invoked.

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

 

 





