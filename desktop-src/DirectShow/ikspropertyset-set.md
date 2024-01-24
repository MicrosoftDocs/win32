---
description: The Set method sets a property identified by a property set GUID and a property ID.
ms.assetid: 78f506dc-7fb4-446d-863e-cffee9da5280
title: IKsPropertySet::Set method (Ksproxy.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IKsPropertySet.Set
api_type: 
- COM
api_location: 
- Strmiids.lib
- Strmiids.dll
ms.custom: UpdateFrequency5
---

# IKsPropertySet::Set method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Set` method sets a property identified by a property set GUID and a property ID.

## Syntax


```C++
HRESULT Set(
  [in] REFGUID guidPropSet,
  [in] DWORD   dwPropID,
  [in] LPVOID  pInstanceData,
  [in] DWORD   cbInstanceData,
  [in] LPVOID  pPropData,
  [in] DWORD   cbPropData
);
```



## Parameters

<dl> <dt>

*guidPropSet* \[in\]
</dt> <dd>

Property set GUID.

</dd> <dt>

*dwPropID* \[in\]
</dt> <dd>

Identifier of the property within the property set.

</dd> <dt>

*pInstanceData* \[in\]
</dt> <dd>

Pointer to a buffer that contains instance data for the property.

</dd> <dt>

*cbInstanceData* \[in\]
</dt> <dd>

Size of the *pInstanceData* buffer, in bytes.

</dd> <dt>

*pPropData* \[in\]
</dt> <dd>

Pointer to a buffer that contains the value of the property.

</dd> <dt>

*cbPropData* \[in\]
</dt> <dd>

Sise of the *pPropData* buffer, in bytes.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                              | Description                                                                 |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | Success.<br/>                                                         |
| <dl> <dt>**E\_PROP\_SET\_UNSUPPORTED**</dt> </dl> | The property set is not supported.<br/>                               |
| <dl> <dt>**E\_PROP\_ID\_UNSUPPORTED**</dt> </dl>  | The property ID is not supported for the specified property set.<br/> |



 

## Remarks

> [!Note]  
> Another interface by this name exists in the dsound.h header file. The two interfaces are not compatible. The **IKsControl** interface, documented in the DirectShow DDK, is now the recommended interface for passing property sets between WDM drivers and user mode components.

 

You must include Ks.h before Ksproxy.h.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Ksproxy.h</dt> </dl>    |
| Library<br/>                  | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**IKsPropertySet Interface**](ikspropertyset.md)
</dt> <dt>

[Property Sets](property-sets.md)
</dt> </dl>

 

 




