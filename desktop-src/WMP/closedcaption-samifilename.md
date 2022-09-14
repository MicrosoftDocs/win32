---
title: ClosedCaption.SAMIFileName
description: The SAMIFileName property specifies or retrieves the name of the file containing the information needed for closed captioning.
ms.assetid: f2090500-6c9f-4d2d-9855-a9c193b00a41
keywords:
- ClosedCaption.SAMIFileName Windows Media Player
topic_type:
- apiref
api_name:
- ClosedCaption.SAMIFileName
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ClosedCaption.SAMIFileName

The **SAMIFileName** property specifies or retrieves the name of the file containing the information needed for closed captioning.

``` syntax
player.closedCaption.SAMIFileName
```

## Possible Values

This property is a read/write **String**.

## Remarks

The Synchronized Accessible Media Interchange (SAMI) file must use an .smi or .sami file name extension.

If you don't specify a value for **SAMIFileName**, this property retrieves a string containing the file name or URL associated with the current media item. This association can occur when a SAMI file is specified using the *sami* URL parameter, or automatically when the SAMI file has the same name as the digital media file name (except for the file name extension). If there is no SAMI file associated with the current media, this property retrieves an empty string ("").

Once you specify a value for **SAMIFileName**, that value persists until you specify a new value (or until a new media item is opened using the *sami* URL parameter). Therefore, you must specify a new value for this property before you play each new media item. That way, the new value for **SAMIFileName** will take effect when the next media item is opened (or when *Player*.**close** is called). Specifying a new value for **SAMIFileName** has no effect for the current media.

To cause Windows Media Player to return to using the SAMI file associated with a particular media item, specify a value for **SAMIFileName** equal to an empty string ("") before you play the next media item.

**Windows Media Player 10 Mobile:** This property is read only, and always returns an empty string.

## Examples

The following three JScript examples use *ClosedCaption*.**SAMIFileName** to specify the name of a closed caption text file. The **Player** object was created with ID = "Player".


```JScript
// Display the closed captions from a website.
Player.closedCaption.SAMIFileName="https://www.proseware.com/ccsample.smi";

// Display the closed captions from a local network.
// You must add an escape sequence of a backslash for every original backslash.
Player.closedCaption.SAMIFileName="\\\\yourservername\\Public\\ccsample.smi";

// Display the closed captions from a file on a local drive.
// Be sure to add the appropriate escape sequences.
Player.closedCaption.SAMIFileName="C:\\WMSDK\\WMPSDK9\\samples\\media\\ccsample.smi";

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> <dt>

[**ClosedCaption Object**](closedcaption-object.md)
</dt> <dt>

[**Player.close**](player-close.md)
</dt> </dl>

 

 





