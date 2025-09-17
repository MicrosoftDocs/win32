---
title: IRdsCursorRedirector interface
description: Remote desktop cursor image changed presenter.
ms.assetid: 54ee23c4-8d8b-4911-9f24-db0d4ac1fec4
ms.tgt_platform: multiple
keywords:
- IRdsCursorRedirector interface Remote Desktop Services
topic_type:
- apiref
api_name:
- IRdsCursorRedirector
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/31/2025
---

# IRdsCursorRedirector interface

Remote desktop client interface to get updates to the cursor image (HCURSOR) when it changes.

### Methods

The **IRdsCursorRedirector** interface has these methods.


| Method                                                               | Description                          |
|:---------------------------------------------------------------------|:-------------------------------------|
| [**OnCursorChanged**](irdscursorredirector-oncursorchanged.md)  | Called when frame buffer changes with updated byte array.<br/>  |


## Requirements


| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11<br/>                                                                 |
| Minimum supported server<br/> | <br/>                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpInputSink is defined as 54ee23c4-8d8b-4911-9f24-db0d4ac1fec4<br/>     |



 

