---
title: Media.setItemInfo method
description: The setItemInfo method sets the value of the specified attribute for the current media item.
ms.assetid: '8c4ce954-45cb-4a67-9660-1a013ecd64c3'
keywords:
- setItemInfo method Windows Media Player
- setItemInfo method Windows Media Player , Media class
- Media class Windows Media Player , setItemInfo method
topic_type:
- apiref
api_name:
- Media.setItemInfo
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media.setItemInfo method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setItemInfo** method sets the value of the specified attribute for the current media item.

## Syntax


```JScript
Media.setItemInfo(
  attribute,
  value
)
```



## Parameters

<dl> <dt>

*attribute* \[in\]
</dt> <dd>

**String** containing the attribute name. For information about the attributes supported by Windows Media Player, see the Windows Media Player [Attribute Reference](attribute-reference.md).

</dd> <dt>

*value* \[in\]
</dt> <dd>

**String** containing the new value.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The **attributeCount** property contains the number of attributes available for a given **Media** object. Index numbers can then be used with the **getAttributeName** method to determine the names of the built-in attributes that can be used with this method.

Before using this method, use the **isReadOnlyItem** method to determine whether a particular attribute can be set.

To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

**Note**

If you embed the Windows Media Player control in your application, file attributes that you change will not be written to the digital media file until the user runs Windows Media Player. If you use the control in a remoted application written in C++, file attributes that you change will be written to the digital media file shortly after you make the changes. In either case, the changes are immediately available to your code through the library.

**Windows Media Player 10 Mobile:** This method is not implemented.

## Examples

The following JScript example uses *Media*.**setItemInfo** to change the value of the Genre attribute for the current media item. An HTML TEXT input element named genText allows the user to enter a text string, which is then used to change the attribute information. The **Player** object was created with ID = "Player".


```JScript
<!-- Create the button element. -->
<INPUT type = "BUTTON"  id = "NEWGEN"  name = "NEWGEN"  value = "Change Genre" 
onClick = "
    /* Store the current media item. */
    var cm = Player.currentMedia;

    /* Get the user input from the text box. */
    var atValue = genText.value;

    /* Test for read-only status of the attribute. */
    if(cm.isReadOnlyItem('Genre') == false){

        /* Change the attribute value. */
        cm.setItemInfo('Genre' ,atValue);
    } 
">

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Media.getItemInfo**](media-getiteminfo.md)
</dt> <dt>

[**Media.isReadOnlyItem**](media-isreadonlyitem.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





