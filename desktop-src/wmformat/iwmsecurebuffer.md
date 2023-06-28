---
title: IWMSecureBuffer interface
description: The IWMSecureBuffer interface encrypts and decrypts data pointers.
ms.assetid: 6b8ce694-15ec-4177-ba17-88fcd6517bdb
keywords:
- IWMSecureBuffer interface windows Media Format
- IWMSecureBuffer interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMSecureBuffer
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IWMSecureBuffer interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IWMSecureBuffer** interface encrypts and decrypts data pointers.

## Members

The **IWMSecureBuffer** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMSecureBuffer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMSecureBuffer** interface has these methods.



| Method                                     | Description                         |
|:-------------------------------------------|:------------------------------------|
| [**Decrypt**](iwmsecurebuffer-decrypt.md) | Decrypts a data pointer.<br/> |
| [**Encrypt**](iwmsecurebuffer-encrypt.md) | Encrypts a data pointer.<br/> |



 

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> </dl>

 

