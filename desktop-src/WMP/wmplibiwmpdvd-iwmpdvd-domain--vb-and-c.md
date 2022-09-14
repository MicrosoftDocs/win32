---
title: IWMPDVD domain property
description: The domain property gets the current domain of the DVD.
ms.assetid: 0b7b39fe-2b04-44e2-aa5e-cab7be9a06b1
keywords:
- domain property Windows Media Player
- domain property Windows Media Player , IWMPDVD interface
- IWMPDVD interface Windows Media Player , domain property
topic_type:
- apiref
api_name:
- IWMPDVD.domain
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPDVD::domain property

The **domain** property gets the current domain of the DVD.

## Syntax


```CSharp
public System.String domain {get; set;}
```


```VB

Public ReadOnly Property domain As System.String
```





## Property value

A **System.String** that is one of the following values.



| Value                                                                                        | Meaning                                                                                                                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>firstPlay</dt> </dl>         | Performing default initialization of a DVD disc.<br/>                                                                                      |
| <dl> <dt>videoManagerMenu</dt> </dl>  | Displaying menus for the entire disc. Also known as topMenu for Windows Media Player. Commonly called the title menu or the top menu.<br/> |
| <dl> <dt>videoTitleSetMenu</dt> </dl> | Displaying menus for the current title set. Also known as titleMenu for Windows Media Player. Commonly called the root menu.<br/>          |
| <dl> <dt>title</dt> </dl>             | Usually, displaying the current title.<br/>                                                                                                |
| <dl> <dt>stop</dt> </dl>              | The DVD Navigator is in the DVD Stop domain.<br/>                                                                                          |
| <dl> <dt>undefined</dt> </dl>         | Windows Media Player is not in any DVD domain.<br/>                                                                                        |



 

## Remarks

Every DVD is authored differently. Some DVDs do not contain the firstPlay, videoManagerMenu, or videoTitleSetMenu domains.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPDVD Interface (VB and C#)**](iwmpdvd--vb-and-c.md)
</dt> </dl>

 

 





