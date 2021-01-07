---
description: Returns the requested frame from a loaded capture.
ms.assetid: efd1cff5-a3a1-4910-b003-25b6e10dad6e
title: ExpertGetFrame function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExpertGetFrame
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# ExpertGetFrame function

The **ExpertGetFrame** function returns the requested frame from a loaded capture.

## Syntax


```C++
DWORD WINAPI ExpertGetFrame(
  _In_  HEXPERTKEY              hExpertKey,
  _In_  DWORD                   Direction,
  _In_  DWORD                   RequestFlags,
  _In_  DWORD                   RequestedFrameNumber,
  _In_  HFILTER                 hFilter,
  _Out_ LPEXPERTFRAMEDESCRIPTOR pEFrameDescriptor
);
```



## Parameters

<dl> <dt>

*hExpertKey* \[in\]
</dt> <dd>

A unique expert identifier. Network Monitor passes the *hExpertKey* identifier to the expert when it calls the [**Run**](run.md) function.

</dd> <dt>

*Direction* \[in\]
</dt> <dd>

A value that identifies how Network Monitor searches for the frame.



| Value                                                                                                                                                                                         | Meaning                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="GET_SPECIFIED_FRAME"></span><span id="get_specified_frame"></span><dl> <dt>**GET\_SPECIFIED\_FRAME**</dt> </dl>              | Return the requested frame.<br/> |
| <span id="GET_FRAME_NEXT_FORWARD"></span><span id="get_frame_next_forward"></span><dl> <dt>**GET\_FRAME\_NEXT\_FORWARD**</dt> </dl>    | Return the next frame.<br/>      |
| <span id="GET_FRAME_NEXT_BACKWARD"></span><span id="get_frame_next_backward"></span><dl> <dt>**GET\_FRAME\_NEXT\_BACKWARD**</dt> </dl> | Return the previous frame.<br/>  |



 

</dd> <dt>

*RequestFlags* \[in\]
</dt> <dd>

The flags that specify how Network Monitor should handle the request. Specify one or more of the following flags.



| Value                                                                                                                                                                                             | Meaning                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FLAGS_DEFER_TO_UI_FILTER"></span><span id="flags_defer_to_ui_filter"></span><dl> <dt>**FLAGS\_DEFER\_TO\_UI\_FILTER**</dt> </dl> | Before applying the display filter parameter of the expert which is specified in *hFilter*, apply the display filter that Network Monitor is using when the expert starts.<br/>                                                                                                                              |
| <span id="FLAGS_ATTACH_PROPERTIES"></span><span id="flags_attach_properties"></span><dl> <dt>**FLAGS\_ATTACH\_PROPERTIES**</dt> </dl>      | The properties that all protocol parsers find with claimed sections of this frame are attached to the frame. If the flag is not set, the **lpPropertyTable** field of the [**EXPERTFRAMEDESCRIPTOR**](expertframedescriptor.md) structure (returned by **pEFrameDescriptor**) will be set to **NULL**.<br/> |



 

</dd> <dt>

*RequestedFrameNumber* \[in\]
</dt> <dd>

The number of the requested frame.

</dd> <dt>

*hFilter* \[in\]
</dt> <dd>

A handle to the expert display filter. If the expert does not have a display filter, set the parameter to **NULL**.

</dd> <dt>

*pEFrameDescriptor* \[out\]
</dt> <dd>

The [**EXPERTFRAMEDESCRIPTOR**](expertframedescriptor.md) structure that, on return, describes the frame. The expert must allocate and free the memory that this structure uses.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value indicates the reason for the failure. If the return value is NMERR\_EXPERT\_TERMINATE, the expert must immediately clean up and return; the user has aborted the expert run.

## Remarks

If you set FLAGS\_ATTACH\_PROPERTIES, the call requires more resources than if you do not set the flag. If the flag is not set, a pointer points to the raw frame and to data about the frame. If this flag is set, Network Monitor attaches all properties to the frame by calling every parser that claims a portion of the frame. This can be a slow process.

Experts should not set the FLAGS\_ATTACH\_PROPERTIES flag unless the experts require the properties that parsers attach to the frame. If possible, experts should call the **ExpertGetFrame** function without the flag, and then extract the required data directly from the frame.

If the expert calls **ExpertGetFrame** without the FLAGS\_ATTACH\_PROPERTIES flag and requires the properties associated with that frame (an event, for example), the expert calls **ExpertGetFrame** with the same parameters except for the following:

``` syntax
Direction = EXPERT_GET_SPECIFIED_FRAME;
RequestFlags &= (~EXPERT_DEFER_TO_UI_FILTER) | EXPERT_ATTACH_PROPERTIES;
RequestedFrameNumber= (The actual frame number you want);
hFilter = NULL;
pEFrameDescriptor = (The same one as last time);
```

Using the preceding code ensures that the expert gets the required frame without having to call filter code again.

You can set the *hFilter* parameter as an **LPVOID**. If it exists, the returned frame passes this filter. If the expert does not have a display filter to pass to the function (if *hFilter* is **NULL** ), then the frame returned is not filtered.

The **ExpertGetFrame** function can only be called by experts that implement the [**Run**](run.md) or [**Configure**](configure.md) export function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




