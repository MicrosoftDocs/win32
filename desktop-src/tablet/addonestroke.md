---
Description: Adds a new IInkStrokeDisp object to the InkDivider object that was passed in.
ms.assetid: d5b82244-68d5-4137-aaf4-d3232f7c0779
title: AddOneStroke function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AddOneStroke function

Adds a new [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) object to the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object that was passed in.

This function is not intended to be used by application code.

## Syntax


```C++
HRESULT WINAPI AddOneStroke(
  _In_ INT_PTR hDivider,
  _In_ int     strokeId,
  _In_ int     cPoints,
  _In_ POINT   *aPoints
);
```



## Parameters

<dl> <dt>

*hDivider* \[in\]
</dt> <dd>

A handle to the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object.

</dd> <dt>

*strokeId* \[in\]
</dt> <dd>

The [**Id**](/windows/win32/msinkaut/nf-msinkaut-iinkstrokedisp-get_id?branch=master) of the [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) object to be added to the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object.

</dd> <dt>

*cPoints* \[in\]
</dt> <dd>

The number of packets that make up the new [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) object.

</dd> <dt>

*aPoints* \[in\]
</dt> <dd>

The array of packets that make up the [**IInkStrokeDisp**](/windows/win32/msinkaut/nn-msinkaut-iinkstrokedisp?branch=master) object in *strokeId*.

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
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkDiv.dll</dt> </dl> |



 

 




