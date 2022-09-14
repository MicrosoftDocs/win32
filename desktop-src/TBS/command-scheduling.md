---
title: Command Scheduling
description: Each command has a priority associated with it.
ms.assetid: 63f6ba9d-0b87-403b-916b-aa8550f98a11
ms.topic: article
ms.date: 05/31/2018
---

# Command Scheduling

## Command Scheduling

Commands can be submitted to the TBS from multiple contexts at any time. However, a physical TPM can only process one command at a time, and some commands can run for a significant period of time. When multiple commands are pending, the TBS decides which command to send to the TPM. When a command is submitted, each command has a priority associated with it. The TBS uses these priorities to determine which pending command to submit whenever the TPM is free. The four levels of priority are low, normal, high, and system. Applications should use low, normal, or high priority. Although high-priority commands are usually executed before low-priority commands, the TBS command scheduler has an aging policy that eventually gives very high priority to commands that have been blocked for significant periods of time.

## Context Management

When a TPM\_SaveContext or TPM2 ContextSave command is submitted with a virtual handle to a resource that the TBS is managing, the TBS executes the appropriate command on the physical resource and returns the result to the caller if the resource is physically present in the TPM. If the resource is not physically present in the TPM, the preprocessing of the TPM\_SaveContext or TPM2\_ContextSave command causes the resource to be reloaded, at which point the context will be saved and returned to the caller. If the resource being saved is of a type that is normally flushed automatically from the TPM after saving, the TBS invalidates the virtual resource upon completion of this command. When a TPM\_LoadContext or TPM2\_ContextLoad command is submitted to the TBS, the TBS executes the command immediately. If the command completes successfully, the TBS virtualizes the resource handle and passes the resulting TPM byte stream to the caller. When a TPM\_FlushSpecific or TPM2\_FlushContext command is submitted with a virtual handle to a resource that the TBS is managing, the TBS executes a TPM\_FlushSpecific or TPM2\_FlushContext command to evict the resource from the TPM if it is physically present. In this case, the TBS invalidates the virtual resource and returns the result of the flush command to the caller. If the resource is not physically present in the TPM, the preprocessing of the TPM\_FlushSpecific or TPM2\_FlushContext command will load the resource that corresponds to the virtual handle, but it will then be flushed when the command is actually processed. The TBS does not support the TPM\_KeyControlOwner bit or the keepHandle functionality of the TPM\_LoadContext operation, so it will not give a resource the same handle it had before the context was saved.

## Other Commands

Commands that are not mentioned in this documentation are processed by replacing virtual key handles with physical key handles (if necessary) and submitting them to the TPM. This is done after performing the appropriate operations to ensure that resources being used are physically present on the TPM. No additional special processing is performed. The TBS does not attempt to improve the fidelity of the virtualization by modifying data passed back from the TPM as part of a TPM\_GetCapabilities or TPM2\_GetCapability query. The TBS also supports TCG Physical Presence commands. The TBS acts as a pass-through for Physical Presence commands; no special processing is performed by the TBS itself.

## Cleanup

When a context exits, all physical and virtual resources associated with it are cleaned up so they no longer consume system resources.

 

 




