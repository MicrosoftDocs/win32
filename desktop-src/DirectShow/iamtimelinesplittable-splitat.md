---
description: The SplitAt method splits the object at the specified time.
ms.assetid: 37870c6f-a35e-4c08-8188-1c4c7b25ff88
title: IAMTimelineSplittable::SplitAt method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSplittable.SplitAt
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineSplittable::SplitAt method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SplitAt` method splits the object at the specified time.

## Syntax


```C++
HRESULT SplitAt(
   REFERENCE_TIME Time
);
```



## Parameters

<dl> <dt>

*Time* 
</dt> <dd>

Time at which to split the object, relative to the start of the timeline, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following:



| Return code                                                                                   | Description                                        |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Nothing to split.<br/>                       |
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The object does not exist at this time.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory.<br/>                    |



 

## Remarks

If you split a source, effect, or transition, this method creates a second object of the same type. The original object is truncated at the specified split time, and the new object replaces the truncated portion. The new object inherits all of the same properties. In a source object, the method also splits any effects that fall on the split time.

Calling this method on a track splits all the sources, effects, and transitions that are contained in the track at the specified split time. It does not create a second track. (A track begins at time zero and extends to infinity.)

For a track, if the split time is later than everything in the track, the method returns S\_FALSE. For any other object, if the split time does not fall anywhere within the object, the method returns E\_INVALIDARG.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineSplittable Interface**](iamtimelinesplittable.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




