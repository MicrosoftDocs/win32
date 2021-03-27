---
title: ErrorItem.errorCode
description: The errorCode property retrieves the current error code.
ms.assetid: 1495ec34-0995-40c6-bfd0-f3695784e057
keywords:
- ErrorItem.errorCode Windows Media Player
topic_type:
- apiref
api_name:
- ErrorItem.errorCode
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ErrorItem.errorCode

The **errorCode** property retrieves the current error code.

``` syntax
player.error.item(
        index
        ).errorCode
```

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

You should set *Settings*.**enableErrorDialogs** to false if you choose to display custom error messages.

## Examples

The following JScript example uses *ErrorItem*.**errorCode** in an event handler to display the error code to the user. The **Player** object was created with ID = "Player".


```JScript
<SCRIPT LANGUAGE = "JScript"  FOR = Player  EVENT = error()>

// Get the error code for the first error item.
errNum = Player.error.item(0).errorCode;

// Display the error information.
var message = "Error number: " + errNum);
message += "<BR>";
message += "Use your BACK button to return ";
message += "to the previous page.";
document.write(message);

</SCRIPT>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> <dt>

[**ErrorItem.errorDescription**](erroritem-errordescription.md)
</dt> </dl>

 

 





