---
description: A callback function used to notify the host when a texture slice load has been completed.
MS-HAID: vspixengine.IPixEngine5Callbacks\_LoadTextureSliceComplete\_PixEngineTextureSliceDescriptor\_PixEngineHistogram\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine5Callbacks::LoadTextureSliceComplete method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: CEEAB77F-0856-4DEC-991A-7CEB921C84BB
api_name: 
 - IPixEngine5Callbacks.LoadTextureSliceComplete
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixengine5callbacks_loadtextureslicecomplete_pixenginetextureslicedescriptor_pixenginehistogram_ptr"></span>IPixEngine5Callbacks::LoadTextureSliceComplete method

A callback function used to notify the host when a texture slice load has been completed.

## Syntax


```C++
HRESULT LoadTextureSliceComplete(
   PixEngineTextureSliceDescriptor sliceDesc,
   PixEngineHistogram*             histogram
);
```

## Parameters

*sliceDesc*   
A descriptor of the loaded slice.

*histogram*   
The address of histogram data for the loaded slice.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixEngine5Callbacks**](/windows/desktop/direct3dtools/ipixengine5callbacks)

 

 
