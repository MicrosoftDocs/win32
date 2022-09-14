---
title: ErrorItem.errorDescription
description: The errorDescription property retrieves a description of the error.
ms.assetid: 7fd16c3d-1460-41b5-81ca-2636d7a1d0d1
keywords:
- ErrorItem.errorDescription Windows Media Player
topic_type:
- apiref
api_name:
- ErrorItem.errorDescription
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ErrorItem.errorDescription

The **errorDescription** property retrieves a description of the error.

``` syntax
player.error.item(
        index
        ).errorDescription
```

## Possible Values

This property is a read-only **String**.

## Remarks

You should set *Settings*.**enableErrorDialogs** to false if you choose to display custom error messages.

## Examples

The following JScript example uses *ErrorItem*.**errorDescription** in an event handler to display the error message to the user. The **Player** object was created with ID = "Player".


```JScript
<SCRIPT LANGUAGE = "JScript"  FOR = Player  EVENT = error()>

// Get the error description for the first error item.
errDesc = Player.error.item(0).errorDescription;

// Display the error code.
var message = "Error: " + errDesc";
message += "<BR>";
message += "Use your BACK button to return ";
message += "to the previous page.";
document.write(message);

</SCRIPT>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/>                               |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> </dl>

 

 





