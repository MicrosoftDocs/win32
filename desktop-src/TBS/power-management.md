---
title: Power Management (TPM Base Services)
description: The TBS receives power management events.
ms.assetid: 21f76bea-a313-46b7-99b3-422f17376a5a
ms.topic: article
ms.date: 05/31/2018
---

# Power Management (TPM Base Services)

The TBS receives power management events. When an indication is received that the TPM or other parts of the platform are about to enter a power state in which execution will be interrupted or TPM state will be lost, the TBS checks to determine whether the currently executing command is likely to finish before the system powers down. In general, the TBS allows short and medium duration commands to finish, but cancels long duration commands. After the command has returned, the TBS stops sending new commands to the TPM and prepares itself for hibernation. When power is restored, the TBS returns the result of the command to the caller, and then proceeds with processing pending TBS commands. The TBS power management code runs asynchronously, so it can handle power management requests even if the TPM is processing a long command.

When a computer enters sleep states, including S3 (sleep) and S4 (hibernation), the TPM is powered off. Thus, all nonpersistent TPM states are lost. Before entering these states, application software is expected to prepare for the loss of volatile TPM states. When the system returns from a sleep state, the TBS synchronizes with the TPM so that the TBS state is consistent with the TPM state. Application software may need to reissue commands that were interrupted.

 

 




