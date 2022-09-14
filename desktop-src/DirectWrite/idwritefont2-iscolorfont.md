---
title: IDWriteFont2 IsColorFont method
description: Enables determining if a color rendering path is potentially necessary.
ms.assetid: E21BB773-923E-461B-B966-A186ACD0164A
keywords:
- IsColorFont method Direct Write
- IsColorFont method Direct Write , IDWriteFont2 interface
- IDWriteFont2 interface Direct Write , IsColorFont method
topic_type:
- apiref
api_name:
- IDWriteFont2.IsColorFont
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteFont2::IsColorFont method

Enables determining if a color rendering path is potentially necessary.

## Syntax


```C++
BOOL IsColorFont();
```



## Parameters

This method has no parameters.

## Return value

Type: **BOOL**

Returns **TRUE** if the font has color information (COLR and CPAL tables); otherwise **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



## See also

<dl> <dt>

[**IDWriteFont2**](idwritefont2.md)
</dt> </dl>

 

 





