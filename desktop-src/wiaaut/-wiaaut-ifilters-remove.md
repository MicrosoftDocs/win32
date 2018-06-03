---
title: Filters.Remove method
description: Removes the designated filter.
ms.assetid: f00bfeac-a043-4146-965c-31cd12749a9f
keywords:
- Remove method WIA Automation
- Remove method WIA Automation , Filters object
- Filters object WIA Automation , Remove method
topic_type:
- apiref
api_name:
- Filters.Remove
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

# Filters.Remove method

Removes the designated filter.

## Syntax


```VB
Filters.Remove( _
  ByVal Index As LONG _
) As HRESULT
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **LONG**

Required. **Long** value.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example code, see [Create an ImageProcess Object and Create one of Each Available Filter](https://www.bing.com/search?q=Create an ImageProcess Object and Create one of Each Available Filter) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Filters**](-wiaaut-filters.md)
</dt> </dl>

 

 





