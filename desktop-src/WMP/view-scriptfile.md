---
title: VIEW.scriptFile
description: The scriptFile attribute specifies the file names of accompanying JScript files.
ms.assetid: c285c467-5ba7-4f46-b316-977e833c3cdd
keywords:
- VIEW.scriptFile Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.scriptFile
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.scriptFile

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **scriptFile** attribute specifies the file names of accompanying JScript files.

``` syntax
        elementID.scriptFile
```

## Possible Values

This attribute is a write-only **String** with no default value. The file names of multiple JScript files are delimited with semicolons. Leading and following spaces and semicolons should not be present.

## Remarks

The code in the specified files can be used by any event handler in the View. Code that is used by event handlers in multiple Views can be placed in a file with the same name as the skin definition file but with a .js extension instead of a .wms extension. This file is loaded automatically and need not be specified in the skin definition file.

## Examples


```C++
<VIEW id="theView" scriptFile="theScript.js">
</VIEW>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> </dl>

 

 





