---
title: Player.launchURL method
description: The launchURL method sends a URL to the user's default browser to be rendered. | Player.launchURL method
ms.assetid: '2b445e59-f884-4519-9acb-f349319429d2'
keywords:
- launchURL method Windows Media Player
- launchURL method Windows Media Player , Player class
- Player class Windows Media Player , launchURL method
topic_type:
- apiref
api_name:
- Player.launchURL
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.launchURL method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **launchURL** method sends a URL to the user's default browser to be rendered.

## Syntax


```JScript
Player.launchURL(
  URL
)
```



## Parameters

<dl> <dt>

*URL* \[in\]
</dt> <dd>

**String** value representing the URL to launch.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method only opens webpages using the HTTP or HTTPS protocols.

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following example creates an HTML BUTTON element that, when clicked, displays the Microsoft website in a new browser window. The **Player** element was created with ID = "Player".


```JScript
<INPUT  TYPE = "BUTTON"  ID = "GOTOMS"  VALUE = "Microsoft.com"  onClick = "

    /* Open the Microsoft website. */
    Player.launchURL('https://www.microsoft.com');
">

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





