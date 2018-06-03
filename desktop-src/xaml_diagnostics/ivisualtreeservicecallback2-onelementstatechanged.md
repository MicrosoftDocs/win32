---
Description: Communicates the state of an element in the visual tree when it changes.
ms.assetid: A832FDC6-1485-432C-9A87-A3C94D0AF8CA
title: IVisualTreeServiceCallback2::OnElementStateChanged method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVisualTreeServiceCallback2::OnElementStateChanged method

Communicates the state of an element in the visual tree when it changes.

## Syntax


```C++
virtual HRESULT OnElementStateChanged(
   InstanceHandle     element,
   VisualElementState elementState,
   LPCWSTR            context
) = 0;
```



## Parameters

<dl> <dt>

*element* 
</dt> <dd>

The XAML element in the visual tree.

</dd> <dt>

*elementState* 
</dt> <dd>

The state of the element.

</dd> <dt>

*context* 
</dt> <dd>

The path to the element.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

When any XAML diagnostics API results in a resource reference becoming invalid, this callback will be notified of the invalid reference. An instance handle will be given that corresponds to an element in the tree, and a string representation of the path to the invalid reference. The grammar for the syntax is: PropertyName:Full.Dotted.TypeName\[Indexer\] and paths can be separated with a forward slash ("/") to be chained together.

## See also

<dl> <dt>

[**IVisualTreeServiceCallback2**](/previous-versions/windows/desktop/api/xamlom/nn-xamlom-ivisualtreeservicecallback2)
</dt> </dl>

 

 



