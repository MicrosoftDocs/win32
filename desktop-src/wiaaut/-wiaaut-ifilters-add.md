---
title: Filters.Add method
description: Appends or inserts a new Filter of the specified FilterID into a Filters collection.
ms.assetid: 506a555c-cdc1-4852-a398-f3cdc77e3214
keywords:
- Add method WIA Automation
- Add method WIA Automation , Filters object
- Filters object WIA Automation , Add method
topic_type:
- apiref
api_name:
- Filters.Add
api_location:
- Wiaaut.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Filters.Add method

Appends or inserts a new [**Filter**](-wiaaut-filter.md) of the specified *FilterID* into a [**Filters**](-wiaaut-filters.md) collection.

## Syntax


```VB
Filters.Add( _
  ByVal FilterID As BSTR, _
  [ ByVal Index As LONG ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*FilterID* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> <dt>

*Index* \[in, optional\]
</dt> <dd>

Type: **LONG**

**Long** value.



| Value                                                                                                                              | Meaning              |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| <dl> <dt></dt> <dt>0</dt> </dl> | Default. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example code, see [Display all the Properties for the Selected Device](https://www.bing.com/search?q=Display all the Properties for the Selected Device) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**FilterID (Filter)**](-wiaaut-ifilter-filterid.md)
</dt> <dt>

[**FilterID (FilterInfo)**](-wiaaut-ifilterinfo-filterid.md)
</dt> <dt>

[**Filters**](-wiaaut-filters.md)
</dt> </dl>

 

 





