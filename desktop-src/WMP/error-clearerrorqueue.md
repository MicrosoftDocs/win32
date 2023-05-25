---
title: Error.clearErrorQueue method
description: The clearErrorQueue method clears the errors from the error queue. | Error.clearErrorQueue method
ms.assetid: 306f0700-88b1-4433-8abb-7d225e82060a
keywords:
- clearErrorQueue method Windows Media Player
- clearErrorQueue method Windows Media Player , Error class
- Error class Windows Media Player , clearErrorQueue method
topic_type:
- apiref
api_name:
- Error.clearErrorQueue
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Error.clearErrorQueue method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **clearErrorQueue** method clears the errors from the error queue.

## Syntax


```JScript
Error.clearErrorQueue()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method is useful to clear the error queue after a series of errors has been processed.

You should set *Settings*.**enableErrorDialogs** to false if you choose to display custom error messages.

## Examples

The following JScript example uses *Error*.**clearErrorQueue** in an event handler to empty the error queue after all error descriptions are displayed. The **Player** object was created with ID = "Player".


```JScript
<SCRIPT LANGUAGE = "JScript"  FOR = Player  EVENT = error()>

// Store the number of errors in the queue.
var max = Player.error.errorCount 

// Loop through the list of errors.
for (var i = 0; i < max; i++){
    // Get the error description for this item.
    var errDesc = Player.error.item(i).errorDescription;
    
    // Display the error message.
    alert(errDesc);
}

// Clear the error queue to prepare for the next group of errors.
Player.error.clearErrorQueue();

</SCRIPT>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Error Object**](error-object.md)
</dt> </dl>

 

 





