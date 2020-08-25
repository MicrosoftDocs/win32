---
title: TBS Functions
description: TBS provides the following functions.
ms.assetid: df2d3e36-0a27-4cc0-bcb2-709eb6bedeac
keywords:
- TPM Base Services TBS , functions
ms.topic: reference
ms.date: 05/31/2018
---

# TBS Functions

TBS provides the following functions.

## In this section



| Topic                                                                                       | Description                                                                                                                                                 |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Tbsi\_Context\_Create**](/windows/desktop/api/Tbs/nf-tbs-tbsi_context_create)<br/>                            | Creates a context handle that can be used to pass commands to TBS.<br/>                                                                               |
| [**Tbsi\_Create\_Attestation\_From\_Log**](/previous-versions/windows/desktop/legacy/dn455155(v=vs.85))<br/> | Creates an attestation by extracting a TrustPoint from a TCG log.<br/>                                                                                |
| [**Tbsi\_GetDeviceInfo**](/windows/desktop/api/Tbs/nf-tbs-tbsi_getdeviceinfo)<br/>                                | Obtains the version of the TPM on the computer.<br/>                                                                                                  |
| [**Tbsi\_Get\_OwnerAuth**](/windows/desktop/api/Tbs/nf-tbs-tbsi_get_ownerauth)<br/>                               | Retrieves the owner authorization of the TPM if the information is available in the local registry. <br/>                                             |
| [**Tbsi\_Get\_TCG\_Log**](/windows/desktop/api/Tbs/nf-tbs-tbsi_get_tcg_log)<br/>                                  | Retrieves the most recent Windows Boot Configuration Log (WBCL), also referred to as a TCG log.<br/>                                                  |
| [**Tbsi\_Get\_TCG\_Log\_Ex**](/windows/desktop/api/Tbs/nf-tbs-tbsi_get_tcg_log_ex)<br/>                           | Gets the Windows Boot Configuration Log (WBCL), also referred to as the TCG log, of the specified type.<br/>                                          |
| [**Tbsi\_Get\_TCG\_Logs**](/previous-versions/windows/desktop/legacy/dn455156(v=vs.85))<br/>                                | Get one or more Windows Boot Configuration Logs (WBCL), also referred to as the TCG logs.<br/>                                                        |
| [**Tbsi\_Physical\_Presence\_Command**](/windows/desktop/api/Tbs/nf-tbs-tbsi_physical_presence_command)<br/>     | Passes a physical presence ACPI command through TBS to the driver.<br/>                                                                               |
| [**Tbsi\_Revoke\_Attestation**](/windows/desktop/api/Tbs/nf-tbs-tbsi_revoke_attestation)<br/>                     | Invalidates the PCRs if the ELAM driver detects a policy-violation (a rootkit, for example).<br/>                                                     |
| [**Tbsip\_Cancel\_Commands**](/windows/desktop/api/Tbs/nf-tbs-tbsip_cancel_commands)<br/>                        | Cancels all outstanding commands for the specified context.<br/>                                                                                      |
| [**Tbsip\_Context\_Close**](/windows/desktop/api/Tbs/nf-tbs-tbsip_context_close)<br/>                            | Closes a context handle, which releases resources associated with the context in TBS and closes the binding handle used to communicate with TBS.<br/> |
| [**Tbsip\_Submit\_Command**](/windows/desktop/api/Tbs/nf-tbs-tbsip_submit_command)<br/>                          | Submits a Trusted Platform Module (TPM) command to TPM Base Services (TBS) for processing.<br/>                                                       |



 

 

