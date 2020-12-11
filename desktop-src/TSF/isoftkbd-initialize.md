---
title: ISoftKbd Initialize method (Softkbdc.h)
description: The ISoftKbd Initialize method initializes all necessary fields for a soft keyboard and generates standard soft keyboard layouts.
ms.assetid: c997864c-2596-4086-8062-cd30f371c38f
keywords:
- Initialize method Text Services Framework
- Initialize method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , Initialize method
topic_type:
- apiref
api_name:
- ISoftKbd.Initialize
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::Initialize method

The **ISoftKbd::Initialize** method initializes all necessary fields for a soft keyboard and generates standard soft keyboard layouts.

## Syntax


```C++
HRESULT Initialize();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Value                                                                                | Description                           |
|--------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method was successful.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Softkbd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ISoftKbd**](isoftkbd.md)
</dt> </dl>

 

 





