---
description: CBaseDispatch.GetTypeInfo method - The GetTypeInfo method retrieves the type information for the object, which can then be used to get the type information for an interface.
ms.assetid: aa06b97c-541b-44fc-bdef-97fd1f014e85
title: CBaseDispatch.GetTypeInfo method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseDispatch.GetTypeInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseDispatch.GetTypeInfo method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetTypeInfo` method retrieves the type information for the object, which can then be used to get the type information for an interface.

## Syntax


```C++
HRESULT GetTypeInfo(
   REFIID    riid,
   UINT      itinfo,
   LCID      lcid,
   ITypeInfo **pptinfo
);
```



## Parameters

<dl> <dt>

*riid* 
</dt> <dd>

Reference to an interface identifier (IID) that specifies the interface.

</dd> <dt>

*itinfo* 
</dt> <dd>

Type information to return. Must be zero.

</dd> <dt>

*lcid* 
</dt> <dd>

Locale identifier.

</dd> <dt>

*pptinfo* 
</dt> <dd>

Address of a variable that receives an **ITypeInfo** pointer.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                             | Description                                    |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                            |
| <dl> <dt>**E\_POINTER**</dt> </dl>               | **NULL** pointer argument.<br/>          |
| <dl> <dt>**TYPE\_E\_ELEMENTNOTFOUND**</dt> </dl> | The *itinfo* parameter is not zero.<br/> |



 

## Remarks

This method behaves like the **IDispatch::GetTypeInfo** method. However, it includes an additional parameter, *riid*, which specifies the interface for which to retrieve type information.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseDispatch Class**](cbasedispatch.md)
</dt> </dl>

 

 




