---
title: IWMPClosedCaption2 getSAMILangID method
description: The getSAMILangID method returns the locale identifier (LCID) of a language supported by the current SAMI file.
ms.assetid: 41aca317-6182-47c3-8bd9-ba42b92b10f4
keywords:
- getSAMILangID method Windows Media Player
- getSAMILangID method Windows Media Player , IWMPClosedCaption2 interface
- IWMPClosedCaption2 interface Windows Media Player , getSAMILangID method
topic_type:
- apiref
api_name:
- IWMPClosedCaption2.getSAMILangID
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPClosedCaption2::getSAMILangID method

The **getSAMILangID** method returns the locale identifier (LCID) of a language supported by the current SAMI file.

## Syntax


```CSharp
public System.Int32 getSAMILangID(
  System.Int32 nIndex
);
```


```VB

Public Function getSAMILangID( _
  ByVal nIndex As System.Int32 _
) As System.Int32
Implements IWMPClosedCaption2.getSAMILangID
```





## Parameters

<dl> <dt>

*nIndex* \[in\]
</dt> <dd>

A **System.Int32** that is the zero-based index of the LCID to retrieve.

</dd> </dl>

## Return value

A **System.Int32** that is the LCID of the language with the specified index.

## Remarks

The languages in a SAMI file are indexed in the order shown in the file, starting with zero.

This method returns 0 unless a digital media file is open (AxWindowsMediaPlayer.openState is equal to 13).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> <dt>

[**IWMPClosedCaption Interface (VB and C#)**](iwmpclosedcaption--vb-and-c.md)
</dt> <dt>

[**IWMPClosedCaption2 Interface (VB and C#)**](iwmpclosedcaption2--vb-and-c.md)
</dt> </dl>

 

 





