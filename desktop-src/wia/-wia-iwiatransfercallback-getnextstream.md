---
description: Gets a new stream for the specified item.
ms.assetid: fe25843c-2051-42fe-8737-eea39f6aeab9
title: IWiaTransferCallback::GetNextStream method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaTransferCallback.GetNextStream
api_type: 
- COM
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# IWiaTransferCallback::GetNextStream method

Gets a new stream for the specified item.

## Syntax


```C++
HRESULT GetNextStream(
  [in]  LONG    lFlags,
  [in]  BSTR    bstrItemName,
  [in]  BSTR    bstrFullItemName,
  [out] IStream **ppDestination
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Currently unused. Should be set to zero.

</dd> <dt>

*bstrItemName* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the name of the item to create stream for.

</dd> <dt>

*bstrFullItemName* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the full name of the item to create stream for.

</dd> <dt>

*ppDestination* \[out\]
</dt> <dd>

Type: **[IStream](/windows/win32/api/objidl/nn-objidl-istream)\*\***

Receives the address of a pointer to the new [IStream](/windows/win32/api/objidl/nn-objidl-istream) object.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

When this method is implemented by an image processing filter, the Windows Image Acquisition (WIA) 2.0 minidriver calls it during image acquisition to get the destination stream from the client.

A filter's **IWiaTransferCallback::GetNextStream** must delegate to the application's callback method. The filter uses the stream returned by the application callback's **IWiaTransferCallback::GetNextStream** implementation to create its own stream that it passes back to the WIA 2.0 service. The filtering is done when the filter's stream calls the [IStream::Write](/windows/win32/api/objidl/nf-objidl-isequentialstream-write) method.

The filter's stream cannot make any assumptions on the number of bytes that are written to it on each write, since the unfiltered image data may come from the WIA 2.0 Preview Component rather than the driver. The WIA 2.0 Preview Component always writes the whole unfiltered image data into the filter's stream only once, which means that the filter's stream has one source writing into it. If both the driver and the preview component write into the filter's stream, the filter's stream cannot assume, for example, that it will receive the full header the first time [IStream::Write](/windows/win32/api/objidl/nf-objidl-isequentialstream-write) is called although its corresponding driver always writes the header data first in one write. Nor can it assume that a subsequent write contains exactly one scan line. So the filtering stream may have to count the number of bytes written to it to determine, for example, where the image data starts.

The image processing filter's **IWiaTransferCallback::GetNextStream** implementation should read the properties needed for its image processing from the item for which the image is being acquired. The filter does not read the properties directly from the *pWiaItem2* passed into [**InitializeFilter**](-wia-iwiaimagefilter-initializefilter.md). Instead the filter must call [**FindItemByName**](-wia-iwiaitem2-finditembyname.md) on this WIA 2.0 item to obtain the actual WIA 2.0 item. The reason for this is that the image being acquired may actually be a child item of *pWiaItem2*. For example, during a folder acquisition the filter uses *pWiaItem2* to obtain *pWiaItem2*'s child items in **IWiaTransferCallback::GetNextStream** (during a folder acquisition the driver returns the images represented by the child items of *pWiaItem2*). The same is true when the WIA 2.0 Preview Component calls into the image processing filter passing a child WIA 2.0 item.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 
