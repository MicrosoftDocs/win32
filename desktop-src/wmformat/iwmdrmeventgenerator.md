---
title: IWMDRMEventGenerator interface
description: The IWMDRMEventGenerator interface is an extension of the IMFMediaEventGenerator interface that provides a method to cancel asynchronous operations.
ms.assetid: 38d8db83-b8f0-4cc2-b426-cb0e46bde51d
keywords:
- IWMDRMEventGenerator interface windows Media Format
- IWMDRMEventGenerator interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMEventGenerator
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IWMDRMEventGenerator interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IWMDRMEventGenerator** interface is an extension of the **IMFMediaEventGenerator** interface that provides a method to cancel asynchronous operations.

## Members

The **IWMDRMEventGenerator** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMDRMEventGenerator** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMEventGenerator** interface has these methods.



| Method                                                                    | Description                                   |
|:--------------------------------------------------------------------------|:----------------------------------------------|
| [**CancelAsyncOperation**](iwmdrmeventgenerator-cancelasyncoperation.md) | Cancels an asynchronous operation.<br/> |



 

## See also

<dl> <dt>

[**DRM Individualization Example**](drm-individualization-example.md)
</dt> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> <dt>

[Media Foundation SDK](../medfound/microsoft-media-foundation-sdk.md)
</dt> </dl>

 

