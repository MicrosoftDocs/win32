---
description: An identifier that can be set on an IMFOutputPolicy.
ms.assetid: 89da33c8-97af-4c56-8bdb-2ac588810d77
title: MF_POLICY_ID (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_POLICY\_ID attribute

An identifier that can be set on an [IMFOutputPolicy](/windows/win32/api/mfidl/nn-mfidl-imfoutputpolicy).

## Data type

**UINT32** (treated as **BOOL**)

## Remarks

The value can be recieved from the [MEPolicySet](./mepolicyset.md) media event. It is stored as a **VT_UI4** type payload in the **MEPolicySet** event.


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 April 2020 Update   <br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>



 

 
