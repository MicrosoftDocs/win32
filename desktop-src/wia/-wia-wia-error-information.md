---
description: The Windows Image Acquisition (WIA)APIs return their completion status in an HRESULT return value.
ms.assetid: 4f3b4292-7aad-4a0a-9cd7-ef8438e57ab3
title: WIA Error Information
ms.topic: article
ms.date: 05/31/2018
---

# WIA Error Information

The Windows Image Acquisition (WIA)APIs return their completion status in an HRESULT return value. Applications check these return values against the FACILITY\_WIA constant to determine whether the error requires user intervention to clear, such as a jammed paper path, and report them to the user. In addition, all driver-level errors are logged in detail to the event log, using error strings provided by the device minidriver. For a listing of WIA-specific error codes, see [Error Codes](-wia-error-codes.md).

 

 



