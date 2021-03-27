---
title: IWMPClosedCaption2 getSAMIStyleName method
description: The getSAMIStyleName method returns the name of a style supported by the current SAMI file.
ms.assetid: e7678ca6-f52f-45f4-bd1c-7fbcdf1cc47c
keywords:
- getSAMIStyleName method Windows Media Player
- getSAMIStyleName method Windows Media Player , IWMPClosedCaption2 interface
- IWMPClosedCaption2 interface Windows Media Player , getSAMIStyleName method
topic_type:
- apiref
api_name:
- IWMPClosedCaption2.getSAMIStyleName
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPClosedCaption2::getSAMIStyleName method

The **getSAMIStyleName** method returns the name of a style supported by the current SAMI file.

## Syntax


```CSharp
public System.String getSAMIStyleName(
  System.Int32 nIndex
);
```


```VB

Public Function getSAMIStyleName( _
  ByVal nIndex As System.Int32 _
) As System.String
Implements IWMPClosedCaption2.getSAMIStyleName
```





## Parameters

<dl> <dt>

*nIndex* \[in\]
</dt> <dd>

A **System.Int32** that is the zero-based index of the style name to retrieve

</dd> </dl>

## Return value

A **System.String** that is the name of the style as specified in the SAMI file.

## Remarks

The styles in a SAMI file are indexed in the order shown in the file, starting with zero.

This method returns a zero-length string ("") unless a digital media file is open (AxWindowsMediaPlayer.openState is equal to 13).

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

[**IWMPClosedCaption.SAMIStyle (VB and C#)**](wmplibiwmpclosedcaption-iwmpclosedcaption-samistyle--vb-and-c.md)
</dt> <dt>

[**IWMPClosedCaption2 Interface (VB and C#)**](iwmpclosedcaption2--vb-and-c.md)
</dt> </dl>

 

 





