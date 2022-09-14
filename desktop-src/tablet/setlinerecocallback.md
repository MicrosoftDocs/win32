---
description: Sets a callback function to be used during line recognition.
ms.assetid: 0b07ec80-328a-471b-b554-fa66f56a2871
title: SetLineRecoCallback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetLineRecoCallback
api_type: 
- LibDef
api_location: 
- InkDiv.dll
- InkDiv.dll.dll
---

# SetLineRecoCallback function

Sets a callback function to be used during line recognition.

This helper function is not intended to be used by application code.

## Syntax


```C++
HRESULT WINAPI SetLineRecoCallback(
  _In_ INT_PTR        hDivider,
       GetLineRecoDef pfn
);
```



## Parameters

<dl> <dt>

*hDivider* \[in\]
</dt> <dd>

A handle to the [**InkDivider**](inkdivider-class.md) object.

</dd> <dt>

*pfn* 
</dt> <dd>

A pointer to a function that is called when recognition occurs on the [**InkDivider**](inkdivider-class.md) passed in.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                  | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The function succeeded.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *pDivider* parameter is invalid.<br/> |



 

## Remarks

The following is the syntax for the callback function.

``` syntax
public delegate void GetLineRecoDef(
        int cStrokes, 
        [MarshalAs(UnmanagedType.LPArray, ArraySubType = UnmanagedType.I4, SizeParamIndex = 0)]int [] aStrokeIds, 
        float degrees, 
        Point point, 
        [MarshalAs(UnmanagedType.BStr)] out string lineString, 
        out int cSegment, 
        out int[] strokeIdOrdered, 
        out int[] segmentStrokes,
        [MarshalAs(UnmanagedType.LPArray, ArraySubType = UnmanagedType.BStr)] out string [] aSegmentString
    );
```

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkDiv.dll</dt> </dl> |



 

 




