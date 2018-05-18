---
title: Video Classes
description: All virtual machines reflect the presence of an emulated S3 video controller and an accelerated, synthetic video controller.
ms.assetid: '0a02f8f5-f117-46e2-b4c8-822033d40523'
---

# Video Classes

All virtual machines reflect the presence of an emulated S3 video controller and an accelerated, synthetic video controller.

Each display controller has a video head object associated with it. Only one display controller can be active in a virtual machine at any time.

A terminal connection is present for every active remote session connected to a virtual machine.

The following are virtualization WMI classes related to video.

## In this section



| Class                                                                                  | Description                                                                                                                |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**Msvm\_S3DisplayController**](msvm-s3displaycontroller.md)<br/>               | Represents the state of the emulated S3 controller that is present in each virtual machine configuration.<br/>       |
| [**Msvm\_SyntheticDisplayController**](msvm-syntheticdisplaycontroller.md)<br/> | Represents the state of the synthetic display controller that is present in each virtual machine configuration.<br/> |
| [**Msvm\_SystemTerminalConnection**](msvm-systemterminalconnection.md)<br/>     | Associates a virtual computer system with a terminal connection.<br/>                                                |
| [**Msvm\_TerminalConnection**](msvm-terminalconnection.md)<br/>                 | Indicates the state of an active remote session interacting with a virtual computer system.<br/>                     |
| [**Msvm\_TerminalService**](msvm-terminalservice.md)<br/>                       | Manages all remote terminal connections to a particular host.<br/>                                                   |
| [**Msvm\_VideoHead**](msvm-videohead.md)<br/>                                   | Describes the primary drawing surface on a display controller.<br/>                                                  |
| [**Msvm\_VideoHeadOnController**](msvm-videoheadoncontroller.md)<br/>           | Associates a video head with the video controller that includes it.<br/>                                             |



 

## Related topics

<dl> <dt>

[Virtualization WMI Classes](virtualization-wmi-classes.md)
</dt> </dl>

 

 





