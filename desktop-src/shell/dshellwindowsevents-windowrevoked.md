---
Description: 'Called when a Shell window''s registration is revoked.'
title: 'DShellWindowsEvents.WindowRevoked method'
---

# DShellWindowsEvents.WindowRevoked method

Called when a Shell window's registration is revoked.

## Syntax


```JScript
DShellWindowsEvents.WindowRevoked(
  lCookie
)
```



## Parameters

<dl> <dt>

*lCookie* \[in\]
</dt> <dd>

Type: **Integer**

The cookie that identifies the window that was revoked.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

A window is granted a cookie when it is registered as a Shell window. For more information, see [**Register**](ishellwindows-register.md).

## Requirements



|                    |                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | Internet Explorer 5<br/>                                                                                           |
| DLL<br/>     | <dl> <dt>Shdocvw.dll (version 5.00.2014.0216 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DShellWindowsEvents**](dshellwindowsevents.md)
</dt> <dt>

[**WindowRegistered**](dshellwindowsevents-windowregistered.md)
</dt> <dt>

[**Revoke**](ishellwindows-revoke.md)
</dt> </dl>

 

 




