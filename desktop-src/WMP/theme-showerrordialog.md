---
title: THEME.showErrorDialog
description: The showErrorDialog method displays the standard error dialog box.
ms.assetid: cec9ecfd-6665-4b0a-a09c-49120d557a80
keywords:
- THEME.showErrorDialog Windows Media Player
topic_type:
- apiref
api_name:
- THEME.showErrorDialog
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# THEME.showErrorDialog

The **showErrorDialog** method displays the standard error dialog box.

``` syntax
        theme.showErrorDialog()
```

## Parameters

This method has no parameters.

## Return Value

This method does not return a value.

## Remarks

If **Settings.enableErrorDialogs** is false, this method can be used to programmatically display the error dialog. If there are no errors in the error queue, the error dialog box is not shown.

For Windows Media Player 9 Series or later, this method must be called from the error event handler. Windows Media Player 9 Series or later clears the error queue for skins after the error event has been fired.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**THEME Element**](theme-element.md)
</dt> <dt>

[**Settings.enableErrorDialogs**](settings-enableerrordialogs.md)
</dt> </dl>

 

 





