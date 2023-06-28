---
title: IDRMStatusCallback interface
description: The IDRMStatusCallback interface provides a method for receiving status on asynchronous DRM calls.
ms.assetid: d036e259-2451-4020-9516-9631f0ff4095
keywords:
- IDRMStatusCallback interface windows Media Format
- IDRMStatusCallback interface windows Media Format , described
topic_type:
- apiref
api_name:
- IDRMStatusCallback
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IDRMStatusCallback interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IDRMStatusCallback** interface provides a method for receiving status on asynchronous DRM calls.

## Members

The **IDRMStatusCallback** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IDRMStatusCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDRMStatusCallback** interface has these methods.



| Method                                          | Description                                                      |
|:------------------------------------------------|:-----------------------------------------------------------------|
| [**OnStatus**](idrmstatuscallback-onstatus.md) | Receives status messages from asynchronous processes.<br/> |



 

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> </dl>

 

