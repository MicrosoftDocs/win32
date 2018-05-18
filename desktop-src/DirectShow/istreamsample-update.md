---
Description: 'Note  This interface is deprecated. New applications should not use it. Performs a synchronous or an asynchronous update on the current sample.'
ms.assetid: '5f56e3f9-443b-4d67-bfed-3210e691ad4b'
title: 'IStreamSample::Update method'
---

# IStreamSample::Update method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Performs a synchronous or an asynchronous update on the current sample.

## Syntax


```C++
HRESULT Update(
  [in] DWORD     dwFlags,
  [in] HANDLE    hEvent,
  [in] PAPCFUNC  pfnAPC,
  [in] DWORD_PTR dwAPCData
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flag that specifies whether the update is synchronous or asynchronous. The SSUPDATE\_ASYNC flag specifies an asynchronous update, which you can set if both *hEvent* and *pfnAPC* are **NULL**. Use SSUPDATE\_CONTINUOUS to continuously update the sample until you call the [**IStreamSample::CompletionStatus**](istreamsample-completionstatus.md) method.

</dd> <dt>

*hEvent* \[in\]
</dt> <dd>

Handle to an event that this method will trigger when the update is complete.

</dd> <dt>

*pfnAPC* \[in\]
</dt> <dd>

Pointer to a Win32 asynchronous procedure call (APC) function that this method will call after it completes the sample update.

</dd> <dt>

*dwAPCData* \[in\]
</dt> <dd>

Value that this method passes to the function specified by the *pfnAPC* parameter.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                           | Description                                                                 |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**E\_ABORT**</dt> </dl>               | The update aborted.<br/>                                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>          | One of the parameters is invalid.<br/>                                |
| <dl> <dt>**E\_POINTER**</dt> </dl>             | One of the parameters is invalid.<br/>                                |
| <dl> <dt>**MS\_E\_BUSY**</dt> </dl>            | This sample already has a pending update.<br/>                        |
| <dl> <dt>**MS\_S\_ENDOFSTREAM**</dt> </dl>     | Reached the end of the stream; the sample wasn't updated.<br/>        |
| <dl> <dt>**MS\_S\_PENDING**</dt> </dl>         | The asynchronous update is pending.<br/>                              |
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                                                         |
| <dl> <dt>**VFW\_E\_NOT\_COMMITTED**</dt> </dl> | Cannot allocate a sample because the allocator is not committed.<br/> |



 

## Remarks

This method can be used to perform a synchronous or asynchronous update of a sample. If both *hEvent* and *pfnAPC* are **NULL** then the update will be synchronous unless either of the SSUPDATE\_ASYNC or SSUPDATE\_CONTINUOUS flags is specified. When a synchronous update returns, the result of the function contains the I/O completion status.

You can't specify values for both *hEvent* and *pfnAPC*; the method will fail.

Asynchronous updates might complete before the update returns; in that case, the return value is S\_OK. If you specify an event and the update returns S\_OK, this method sets the event on return. If you specify an APC function and the update returns S\_OK, the APC will not be queued and the function will not be called.

Asynchronous updates that don't complete prior to returning will return a value of MS\_S\_PENDING.

If an application creates multiple streams, it must perform an asynchronous update on each stream. Call **WaitForMultipleObjects** to wait for each stream update to complete, before making the next update. Otherwise, the application might block.

## See also

<dl> <dt>

[**IStreamSample Interface**](istreamsample.md)
</dt> </dl>

 

 




