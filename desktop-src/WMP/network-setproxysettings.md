---
title: Network.setProxySettings method
description: The setProxySettings method specifies the proxy setting for a given protocol.
ms.assetid: '473501c9-27ea-47ec-bc82-691804fbfb89'
keywords:
- setProxySettings method Windows Media Player
- setProxySettings method Windows Media Player , Network class
- Network class Windows Media Player , setProxySettings method
topic_type:
- apiref
api_name:
- Network.setProxySettings
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Network.setProxySettings method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setProxySettings** method specifies the proxy setting for a given protocol.

## Syntax


```JScript
Network.setProxySettings(
  protocol,
  setting
)
```



## Parameters

<dl> <dt>

*protocol* \[in\]
</dt> <dd>

**String** specifying the protocol name. For a list of supported protocols, see [Supported Protocols and File Types](supported-protocols-and-file-types.md).

</dd> <dt>

*setting* \[in\]
</dt> <dd>

**Number** (**long**) containing one of the following values.



| Value | Description                                                          |
|-------|----------------------------------------------------------------------|
| 0     | Do not use a proxy server.                                           |
| 1     | Use the proxy settings of the current browser (only valid for HTTP). |
| 2     | Use the manually specified proxy settings.                           |
| 3     | Auto-detect the proxy settings.                                      |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method fails unless the calling application is running on the local computer or intranet.

**Windows Media Player 10 Mobile:** This method is not supported.

## Examples

The following example uses JScript with an HTML SELECT **element to allow the user to specify the Windows Media Player proxy setting for the HTTP protocol. The Player** object was created with ID = "Player".


```JScript
<SELECT ID = HTTPsetproxy  NAME = "HTTPsetproxy"  LANGUAGE="JScript"
        onChange = "
                      /* Store the current selection.*/
                      var setting = this.value;

                      /* Change the proxy setting. */
                      Player.network.setProxySettings('HTTP', setting);
">

<OPTION VALUE=0>Do not use a proxy server
<OPTION VALUE=1>Use the browser settings
<OPTION VALUE=2>Use manual settings
<OPTION VALUE=3>Auto-detect settings

</SELECT>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Network Object**](network-object.md)
</dt> </dl>

 

 





