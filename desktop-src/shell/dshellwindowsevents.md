---
Description: Receives IShellWindows window registration events.
ms.assetid: c340296d-f8eb-43a1-809d-912ea7412fe2
title: DShellWindowsEvents object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DShellWindowsEvents object

Receives [**IShellWindows**](/windows/win32/Exdisp/nn-exdisp-ishellwindows?branch=master) window registration events.

## Members

The **DShellWindowsEvents** object has these types of members:

-   [Methods](#methods)

### Methods

The **DShellWindowsEvents** object has these methods.



| Method                                                           | Description                                                       |
|:-----------------------------------------------------------------|:------------------------------------------------------------------|
| [**WindowRegistered**](dshellwindowsevents-windowregistered.md) | Called when a window is registered as a Shell window. <br/> |
| [**WindowRevoked**](dshellwindowsevents-windowrevoked.md)       | Called when a Shell window's registration is revoked. <br/> |



 

## Remarks

Use **DShellWindowsEvents** to monitor when a Shell window is registered or revoked. For more information, see [**IShellWindows**](/windows/win32/Exdisp/nn-exdisp-ishellwindows?branch=master).

## Requirements



|                    |                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Product<br/> | Internet Explorer 5<br/>                                                                                           |
| Header<br/>  | <dl> <dt>Exdisp.h</dt> </dl>                                      |
| DLL<br/>     | <dl> <dt>Shdocvw.dll (version 5.00.2014.0216 or later)</dt> </dl> |
| IID<br/>     | IID\_IShellWindows<br/>                                                                                            |



## See also

<dl> <dt>

[**ShellWindows**](shellwindows.md)
</dt> </dl>

 

 




