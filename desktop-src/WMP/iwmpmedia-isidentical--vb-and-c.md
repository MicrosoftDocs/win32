---
title: IWMPMedia.isIdentical (VB and C )
description: The isIdentical property (the get\_isIdentical method in C\ ) gets a value indicating whether the specified media item is the same as the current one.
ms.assetid: 1406a0ff-2dc8-4cde-8b71-4a39b8608fb1
keywords:
- IWMPMedia.isIdentical (VB and C ) Windows Media Player
topic_type:
- apiref
api_name:
- IWMPMedia.isIdentical (VB and C )
api_location:
- Interop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMedia.isIdentical (VB and C#)

The **isIdentical** property (the **get\_isIdentical** method in C#) gets a value indicating whether the specified media item is the same as the current one.


```
[Visual Basic]
ReadOnly Property isIdentical(
  pIWMPMedia As IWMPMedia
) As System.Boolean
```




```
[C#]
System.Boolean get_isIdentical (
  IWMPMedia pIWMPMedia
);
```



## Parameters

*pIWMPMedia*

A **WMPLib.IWMPMedia** interface to the media item to be compared with the current media item.

## Property Value

A **System.Boolean** value that indicates whether the two media items are identical.

## Remarks

**IWMPMedia.isIdentical** is a property in Visual Basic that takes a parameter. In C# it is referred to as the **IWMPMedia.get\_isIdentical** method.

## Examples

The following example uses the **isIdentical** property (the **get\_isIdentical** method in C#) to check whether a media item named newMedia is the same as the current media item. If they are not the same, the new media item is played. Otherwise, the current media continues to play uninterrupted. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
if (newMedia.get_isIdentical(player.currentMedia) != true)
{
    // Change the current media to the new media item.
    player.currentMedia = newMedia;

    // Play the new media item.
    player.Ctlcontrols.play();
}
```


```VB

If (newMedia.isIdentical(player.currentMedia) <> True) Then

    &#39; Change the current media to the new media item.
    player.currentMedia = newMedia

    &#39; Play the new media item.
    player.Ctlcontrols.play()

End If
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> </dl>

 

 





