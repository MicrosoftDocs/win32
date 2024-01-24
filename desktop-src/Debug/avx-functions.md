---
description: Intel AVX functions.
ms.assetid: 237f356a-9ee8-4c52-b08c-a6695c52713a
title: AVX Functions
ms.topic: article
ms.date: 05/31/2018
---

# AVX Functions

The following are the Intel AVX functions.

## In this section



| Topic                                                                   | Description                                                                                                                    |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**CopyContext**](/windows/desktop/api/WinBase/nf-winbase-copycontext)<br/>                           | Copies a source context structure (including any XState) onto an initialized destination context structure.<br/>         |
| [**GetEnabledXStateFeatures**](/windows/desktop/api/WinBase/nf-winbase-getenabledxstatefeatures)<br/> | Gets a mask of enabled XState features on x86 or x64 processors.<br/>                                                    |
| [**GetXStateFeaturesMask**](/windows/desktop/api/WinBase/nf-winbase-getxstatefeaturesmask)<br/>       | Returns the mask of XState features set within a [**CONTEXT**](/windows/desktop/api/WinNT/ns-winnt-wow64_context) structure.<br/>                        |
| [**InitializeContext**](/windows/desktop/api/WinBase/nf-winbase-initializecontext)<br/>               | Initializes a [**CONTEXT**](/windows/desktop/api/WinNT/ns-winnt-arm64_nt_context) structure inside a buffer with the necessary size and alignment.<br/>       |
| [**LocateXStateFeature**](/windows/desktop/api/WinBase/nf-winbase-locatexstatefeature)<br/>           | Retrieves a pointer to the processor state for an XState feature within a [**CONTEXT**](/windows/desktop/api/WinNT/ns-winnt-arm64_nt_context) structure.<br/> |
| [**SetXStateFeaturesMask**](/windows/desktop/api/WinBase/nf-winbase-setxstatefeaturesmask)<br/>       | Sets the mask of XState features set within a [**CONTEXT**](/windows/desktop/api/WinNT/ns-winnt-arm64_nt_context) structure.<br/>                             |



 

 

 




