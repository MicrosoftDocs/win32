---
Description: 'Adds a new IInkStrokeDisp object to the InkDivider object that was passed in.'
ms.assetid: 'd5b82244-68d5-4137-aaf4-d3232f7c0779'
title: AddOneStroke function
---

# AddOneStroke function

Adds a new [**IInkStrokeDisp**](iinkstrokedisp.md) object to the [**InkDivider**](inkdivider-class.md) object that was passed in.

This function is not intended to be used by application code.

## Syntax


```C++
HRESULT WINAPI AddOneStroke(
  _In_ INT_PTR hDivider,
  _In_ int     strokeId,
  _In_ int     cPoints,
  _In_ POINT   *aPoints
);
```



## Parameters

<dl> <dt>

*hDivider* \[in\]
</dt> <dd>

A handle to the [**InkDivider**](inkdivider-class.md) object.

</dd> <dt>

*strokeId* \[in\]
</dt> <dd>

The [**Id**](iinkstrokedisp-id.md) of the [**IInkStrokeDisp**](iinkstrokedisp.md) object to be added to the [**InkDivider**](inkdivider-class.md) object.

</dd> <dt>

*cPoints* \[in\]
</dt> <dd>

The number of packets that make up the new [**IInkStrokeDisp**](iinkstrokedisp.md) object.

</dd> <dt>

*aPoints* \[in\]
</dt> <dd>

The array of packets that make up the [**IInkStrokeDisp**](iinkstrokedisp.md) object in *strokeId*.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                  | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The function succeeded.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *hDivider* parameter is invalid.<br/> |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkDiv.dll</dt> </dl> |



 

 




