---
description: All virtual machines reflect the presence of an emulated S3 video controller and an accelerated, synthetic video controller.
ms.assetid: 93BDC827-E84A-4460-A2DD-18EE87254426
title: Video classes
ms.topic: reference
ms.date: 05/31/2018
---

# Video classes

All virtual machines reflect the presence of an emulated S3 video controller and an accelerated, synthetic video controller.

Each display controller has a video head object associated with it. Only one display controller can be active in a virtual machine at any time.

A terminal connection is present for every active remote session connected to a virtual machine.

The following are virtualization WMI classes related to video.

## In this section



| Topic                                                                                  | Description                                                                                                                |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**Msvm\_S3DisplayController**](msvm-s3displaycontroller.md)<br/>               | Represents the state of the emulated S3 controller that is present in each virtual machine configuration.<br/>       |
| [**Msvm\_SyntheticDisplayController**](msvm-syntheticdisplaycontroller.md)<br/> | Represents the state of the synthetic display controller that is present in each virtual machine configuration.<br/> |
| [**Msvm\_SystemTerminalConnection**](msvm-systemterminalconnection.md)<br/>     | Associates a virtual machine with a terminal connection.<br/>                                                        |
| [**Msvm\_TerminalConnection**](msvm-terminalconnection.md)<br/>                 | Indicates the state of an active remote session interacting with a virtual machine.<br/>                             |
| [**Msvm\_VideoHead**](msvm-videohead.md)<br/>                                   | Describes the primary drawing surface on a display controller.<br/>                                                  |
| [**Msvm\_VideoHeadOnController**](msvm-videoheadoncontroller.md)<br/>           | Associates a video head with the video controller that includes it.<br/>                                             |



 

 

 




