---
Description: 'Note  The ICaptureGraphBuilder interface is deprecated. Use ICaptureGraphBuilder2 instead. Creates the rendering section of the filter graph, which will save bits to disk with the specified file name.'
ms.assetid: 'f410465f-c560-49ab-9194-66d708274f77'
title: 'ICaptureGraphBuilder::SetOutputFileName method'
---

# ICaptureGraphBuilder::SetOutputFileName method

> [!Note]  
> The **ICaptureGraphBuilder** interface is deprecated. Use [**ICaptureGraphBuilder2**](icapturegraphbuilder2.md) instead.

 

Creates the rendering section of the filter graph, which will save bits to disk with the specified file name.

## Syntax


```C++
HRESULT SetOutputFileName(
  [in]  const GUID            *pType,
  [in]        LPCOLESTR       lpwstrFile,
  [out]       IBaseFilter     **ppf,
  [out]       IFileSinkFilter **pSink
);
```



## Parameters

<dl> <dt>

*pType* \[in\]
</dt> <dd>

Pointer to a **GUID** representing the media subtype. Must be `&MEDIASUBTYPE_Avi`.

</dd> <dt>

*lpwstrFile* \[in\]
</dt> <dd>

Pointer to a wide-character string containing the output file name.

</dd> <dt>

*ppf* \[out\]
</dt> <dd>

Address of a pointer to an [**IBaseFilter**](ibasefilter.md) interface representing the multiplexer filter. This method increments the reference count on the **IBaseFilter** interface so you must decrement the reference count by using the **Release** method on this parameter when done using the filter.

</dd> <dt>

*pSink* \[out\]
</dt> <dd>

Address of a pointer to an [**IFileSinkFilter**](ifilesinkfilter.md) interface representing the file writer. This method increments the reference count on the IFileSinkFilter interface so you must decrement the reference count using **Release** when done using the filter.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                   | Description                                                                                     |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Failure.<br/>                                                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid argument. Audio-Video Interleaved (AVI) is the only supported output format.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                                                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument.<br/>                                                           |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | Unexpected error occurred.<br/>                                                           |
| <dl> <dt>**NOERROR**</dt> </dl>        | Success.<br/>                                                                             |
| <dl> <dt>**S\_OK**</dt> </dl>          | Instance of the AVI multiplexer filter was successfully created.<br/>                     |



 

## Remarks

This method inserts the multiplexer and the file writer into the filter graph and calls [**IFileSinkFilter::SetFileName**](ifilesinkfilter-setfilename.md) to set the output file name.

You can use the *ppf* parameter returned by this method as the *pfRenderer* parameter in calls to [**RenderStream**](icapturegraphbuilder-renderstream.md).

You can use the *pSink* parameter from this method in a call to [**SetFileName**](ifilesinkfilter-setfilename.md) to change the file name set by `ICaptureGraphBuilder::SetOutputFileName`.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Version<br/> | Reference: Dshowh<br/>                                                          |
| DLL<br/>     | <dl> <dt>Quartz.dll</dt> </dl> |



## See also

<dl> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**ICaptureGraphBuilder Interface**](icapturegraphbuilder.md)
</dt> </dl>

 

 




