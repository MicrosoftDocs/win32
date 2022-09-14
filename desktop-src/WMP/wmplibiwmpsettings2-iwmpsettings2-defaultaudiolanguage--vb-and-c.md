---
title: IWMPSettings2 defaultAudioLanguage property
description: The defaultAudioLanguage property gets the locale identifier (LCID) of the default audio language specified in Windows Media Player.
ms.assetid: 4b7c9639-9d9f-4ed7-bb70-12cc608dd57a
keywords:
- defaultAudioLanguage property Windows Media Player
- defaultAudioLanguage property Windows Media Player , IWMPSettings2 interface
- IWMPSettings2 interface Windows Media Player , defaultAudioLanguage property
topic_type:
- apiref
api_name:
- IWMPSettings2.defaultAudioLanguage
- IWMPSettings2.get_defaultAudioLanguage
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPSettings2::defaultAudioLanguage property

The **defaultAudioLanguage** property gets the locale identifier (LCID) of the default audio language specified in Windows Media Player.

This property is read-only.

## Syntax


```CSharp
public System.Int32 defaultAudioLanguage {get;}
```


```VB

Public ReadOnly Property defaultAudioLanguage As System.Int32
```





## Property value

A **System.Int32** that is the LCID.

## Remarks

An LCID uniquely identifies a particular language dialect, called a locale.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPControls3.currentAudioLanguage (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-currentaudiolanguage--vb-and-c.md)
</dt> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2 Interface (VB and C#)**](iwmpsettings2--vb-and-c.md)
</dt> </dl>

 

 





