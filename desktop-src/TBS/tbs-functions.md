---
title: TBS Functions
description: TBS provides the following functions.
ms.assetid: df2d3e36-0a27-4cc0-bcb2-709eb6bedeac
keywords:
- TPM Base Services TBS , functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TBS Functions

TBS provides the following functions.

## In this section



| Topic                                                                                       | Description                                                                                                                                                 |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Tbsi\_Context\_Create**](/windows/win32/Tbs/nf-tbs-tbsi_context_create?branch=master)<br/>                            | Creates a context handle that can be used to pass commands to TBS.<br/>                                                                               |
| [**Tbsi\_Create\_Attestation\_From\_Log**](/windows/win32/Tbs/?branch=master)<br/> | Creates an attestation by extracting a TrustPoint from a TCG log.<br/>                                                                                |
| [**Tbsi\_GetDeviceInfo**](/windows/win32/Tbs/nf-tbs-tbsi_getdeviceinfo?branch=master)<br/>                                | Obtains the version of the TPM on the computer.<br/>                                                                                                  |
| [**Tbsi\_Get\_OwnerAuth**](/windows/win32/Tbs/nf-tbs-tbsi_get_ownerauth?branch=master)<br/>                               | Retrieves the owner authorization of the TPM if the information is available in the local registry. <br/>                                             |
| [**Tbsi\_Get\_TCG\_Log**](/windows/win32/Tbs/nf-tbs-tbsi_get_tcg_log?branch=master)<br/>                                  | Retrieves the most recent Windows Boot Configuration Log (WBCL), also referred to as a TCG log.<br/>                                                  |
| [**Tbsi\_Get\_TCG\_Log\_Ex**](/windows/win32/Tbs/nf-tbs-tbsi_get_tcg_log_ex?branch=master)<br/>                           | Gets the Windows Boot Configuration Log (WBCL), also referred to as the TCG log, of the specified type.<br/>                                          |
| [**Tbsi\_Get\_TCG\_Logs**](/windows/win32/Tbs/?branch=master)<br/>                                | Get one or more Windows Boot Configuration Logs (WBCL), also referred to as the TCG logs.<br/>                                                        |
| [**Tbsi\_Physical\_Presence\_Command**](/windows/win32/Tbs/nf-tbs-tbsi_physical_presence_command?branch=master)<br/>     | Passes a physical presence ACPI command through TBS to the driver.<br/>                                                                               |
| [**Tbsi\_Revoke\_Attestation**](/windows/win32/Tbs/nf-tbs-tbsi_revoke_attestation?branch=master)<br/>                     | Invalidates the PCRs if the ELAM driver detects a policy-violation (a rootkit, for example).<br/>                                                     |
| [**Tbsip\_Cancel\_Commands**](/windows/win32/Tbs/nf-tbs-tbsip_cancel_commands?branch=master)<br/>                        | Cancels all outstanding commands for the specified context.<br/>                                                                                      |
| [**Tbsip\_Context\_Close**](/windows/win32/Tbs/nf-tbs-tbsip_context_close?branch=master)<br/>                            | Closes a context handle, which releases resources associated with the context in TBS and closes the binding handle used to communicate with TBS.<br/> |
| [**Tbsip\_Submit\_Command**](/windows/win32/Tbs/nf-tbs-tbsip_submit_command?branch=master)<br/>                          | Submits a Trusted Platform Module (TPM) command to TPM Base Services (TBS) for processing.<br/>                                                       |



 

 

 





