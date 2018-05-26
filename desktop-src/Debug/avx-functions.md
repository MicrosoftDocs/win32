---
Description: Intel AVX functions.
ms.assetid: 237f356a-9ee8-4c52-b08c-a6695c52713a
title: AVX Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVX Functions

The following are the Intel AVX functions.

## In this section



| Topic                                                                   | Description                                                                                                                    |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**CopyContext**](/windows/win32/WinBase/nf-winbase-copycontext?branch=master)<br/>                           | Copies a source context structure (including any XState) onto an initialized destination context structure.<br/>         |
| [**GetEnabledXStateFeatures**](/windows/win32/WinBase/nf-winbase-getenabledxstatefeatures?branch=master)<br/> | Gets a mask of enabled XState features on x86 or x64 processors.<br/>                                                    |
| [**GetXStateFeaturesMask**](/windows/win32/WinBase/nf-winbase-getxstatefeaturesmask?branch=master)<br/>       | Returns the mask of XState features set within a [**CONTEXT**](/windows/win32/WinNT/ns-winnt-_wow64_context?branch=master) structure.<br/>                        |
| [**InitializeContext**](/windows/win32/WinBase/nf-winbase-initializecontext?branch=master)<br/>               | Initializes a [**CONTEXT**](/windows/win32/WinNT/ns-winnt-_arm64_nt_context?branch=master) structure inside a buffer with the necessary size and alignment.<br/>       |
| [**LocateXStateFeature**](/windows/win32/WinBase/nf-winbase-locatexstatefeature?branch=master)<br/>           | Retrieves a pointer to the processor state for an XState feature within a [**CONTEXT**](/windows/win32/WinNT/ns-winnt-_arm64_nt_context?branch=master) structure.<br/> |
| [**SetXStateFeaturesMask**](/windows/win32/WinBase/nf-winbase-setxstatefeaturesmask?branch=master)<br/>       | Sets the mask of XState features set within a [**CONTEXT**](/windows/win32/WinNT/ns-winnt-_arm64_nt_context?branch=master) structure.<br/>                             |



 

 

 




