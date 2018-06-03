---
Description: Replaces an existing resource with a new one of the same type.
ms.assetid: DD2066B0-C91E-4299-AFD3-13E74E75E94B
title: IVisualTreeService2::ReplaceResource method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

[**IVisualTreeService2**](/previous-versions/windows/desktop/api/xamlom/nn-xamlom-ivisualtreeservice2)
</dt> <dt>

[**IVisualTreeService3::AddDictionaryItem**](/previous-versions/windows/desktop/api/xamlom/nf-xamlom-ivisualtreeservice3-adddictionaryitem)
</dt> <dt>

[**IVisualTreeService3::RemoveDictionaryItem**](/previous-versions/windows/desktop/api/xamlom/nf-xamlom-ivisualtreeservice3-removedictionaryitem)
</dt> </dl>

 

 



