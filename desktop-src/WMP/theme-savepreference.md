---
title: THEME.savePreference
description: The savePreference method saves a preference in the registry.
ms.assetid: 4c253d8d-15c0-4c18-bb3f-fdbcef79c999
keywords:
- THEME.savePreference Windows Media Player
topic_type:
- apiref
api_name:
- THEME.savePreference
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# THEME.savePreference

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **savePreference** method saves a preference in the registry.

``` syntax
        theme.savePreference(theKey, theValue)
```

## Parameters

<dl> <dt>

<span id="theKey"></span><span id="thekey"></span><span id="THEKEY"></span>*theKey*
</dt> <dd>

A **String** specifying the key of the preference value to save.

</dd> <dt>

<span id="theValue"></span><span id="thevalue"></span><span id="THEVALUE"></span>*theValue*
</dt> <dd>

A **String** specifying the value to save.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

A preference is a key/value pair that can be stored in the registry to retain information about the state of Windows Media Player between runs. This feature can be used, for example, to save customization settings so that they won't have to be re-entered each time Windows Media Player is started.

Preferences are not encrypted and therefore are not a secure method for persisting data. Do not use preferences to store private data.

## Examples


```JScript
<THEME>
  <VIEW 
    id="View1" 
    onclose="jscript:theme.savePreference('drawer1','open');
             theme.savePreference('drawer2','close')">
  </VIEW>
</THEME>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**THEME Element**](theme-element.md)
</dt> <dt>

[**THEME.loadPreference**](theme-loadpreference.md)
</dt> </dl>

 

 





