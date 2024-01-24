---
title: Error.item method
description: The item method retrieves an ErrorItem object from the error queue.
ms.assetid: 3aca21ff-4c6b-4c24-a85d-3d015612a496
keywords:
- item method Windows Media Player
- item method Windows Media Player , Error class
- Error class Windows Media Player , item method
topic_type:
- apiref
api_name:
- Error.item
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Error.item method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **item** method retrieves an **ErrorItem** object from the error queue.

## Syntax


```JScript
retVal = Error.item(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) containing the index of the **ErrorItem** object to be retrieved.

</dd> </dl>

## Return value

This method returns an **ErrorItem** object.

## Remarks

Windows Media Player can generate a number of errors in response to an error condition. This method allows the retrieval of a specific error in the queue by using an index number. The index numbers for the error queue begin with zero.

You should set *Settings*.**enableErrorDialogs** to false if you choose to display custom error messages.

## Examples

The following JScript example uses the *Error*.**item** object in an event handler to alert the user to the most recent error. The **Player** object was created with ID = "Player".


```JScript
<SCRIPT LANGUAGE="JScript"  FOR=Player EVENT=error()>

// Store the most recent error item number.
var max = Player.error.errorCount - 1 

// Store the most recent error in an error item object.
var errItem = Player.error.item(max);

// Use the error item object to store the error info.
errDesc = errItem.errorDescription;
errNum = errItem.errorCode;

// Display the error info.
alert(errNum + "\n" + errDesc);

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
</dt> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> </dl>

 

 





