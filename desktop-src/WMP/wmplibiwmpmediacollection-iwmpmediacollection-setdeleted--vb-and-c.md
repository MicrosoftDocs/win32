---
title: IWMPMediaCollection setDeleted method
description: The setDeleted method moves the specified media item to the deleted items folder. | IWMPMediaCollection setDeleted method
ms.assetid: 3fa7989e-8b98-44e1-93ca-8136aba358ea
keywords:
- setDeleted method Windows Media Player
- setDeleted method Windows Media Player , IWMPMediaCollection interface
- IWMPMediaCollection interface Windows Media Player , setDeleted method
topic_type:
- apiref
api_name:
- IWMPMediaCollection.setDeleted
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMediaCollection::setDeleted method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `setDeleted` method moves the specified media item to the deleted items folder.

## Syntax


```CSharp
public void setDeleted(
  IWMPMedia pItem,
  System.Boolean varfIsDeleted
);
```


```VB

Public Sub setDeleted( _
  ByVal pItem As IWMPMedia, _
  ByVal varfIsDeleted As System.Boolean _
)
Implements IWMPMediaCollection.setDeleted
```





## Parameters

<dl> <dt>

*pItem* \[in\]
</dt> <dd>

A **WMPLib.IWMPMedia** interface for the item to be moved.

</dd> <dt>

*varfIsDeleted* \[in\]
</dt> <dd>

A **System.Boolean** value that specifies whether the item should be moved to the deleted items folder. This value must always be **true**.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method does not remove files from the user's computer, it just moves them to the deleted items folder.

Before calling this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Examples

The following example uses `setDeleted` to move a particular media item to the deleted items folder. The **isDeleted** method first tests whether the item has already been deleted. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Test whether the media item has already been deleted.
if (!player.mediaCollection.isDeleted(media))
{
    // The item is available to be deleted; move it to the deleted items folder.
    player.mediaCollection.setDeleted(media, true);

    // Inform the user that the operation succeeded.
    System.Windows.Forms.MessageBox.Show("Item moved to deleted items folder.");
}
else
{
    // Tell the user the operation is unnecessary.
    System.Windows.Forms.MessageBox.Show("Item is already deleted!");
}
```


```VB

' Test whether the media item has already been deleted.
If (Not player.mediaCollection.isDeleted(media)) Then

    &#39; The item is available to be deleted move it to the deleted items folder.
    player.mediaCollection.setDeleted(media, True)

    &#39; Inform the user that the operation succeeded.
    System.Windows.Forms.MessageBox.Show(&quot;Item moved to deleted items folder.&quot;)

Else

    &#39; Tell the user the operation is unnecessary.
    System.Windows.Forms.MessageBox.Show(&quot;Item is already deleted!&quot;)

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
</dt> <dt>

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> </dl>

 

 





