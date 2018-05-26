---
Description: Replaces an existing resource with a new one of the same type.
ms.assetid: DD2066B0-C91E-4299-AFD3-13E74E75E94B
title: IVisualTreeService2ReplaceResource method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVisualTreeService2::ReplaceResource method

Replaces an existing resource with a new one of the same type.

## Syntax


```C++
virtual HRESULT ReplaceResource(
  [in] InstanceHandle resourceDictionary,
  [in] InstanceHandle key,
  [in] InstanceHandle newValue
) = 0;
```



## Parameters

<dl> <dt>

*resourceDictionary* \[in\]
</dt> <dd>

The dictionary that contains the resource to replace.

</dd> <dt>

*key* \[in\]
</dt> <dd>

The key of the resource to replace.

</dd> <dt>

*newValue* \[in\]
</dt> <dd>

The value to replace the resource with.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## See also

<dl> <dt>

[**IVisualTreeService2**](/windows/previous-versions/xamlom/nn-xamlom-ivisualtreeservice2?branch=master)
</dt> <dt>

[**IVisualTreeService3::AddDictionaryItem**](/windows/previous-versions/xamlom/nf-xamlom-ivisualtreeservice3-adddictionaryitem?branch=master)
</dt> <dt>

[**IVisualTreeService3::RemoveDictionaryItem**](/windows/previous-versions/xamlom/nf-xamlom-ivisualtreeservice3-removedictionaryitem?branch=master)
</dt> </dl>

 

 



