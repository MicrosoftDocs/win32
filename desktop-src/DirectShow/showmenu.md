---
Description: 'The ShowMenu event is sent when the disc enables or disables the showing of a menu.'
ms.assetid: '7427ff6c-875b-40ce-aa96-3d32b607dc56'
title: ShowMenu
---

# ShowMenu

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ShowMenu` event is sent when the disc enables or disables the showing of a menu.

``` syntax
ShowMenu(DVDMenuIDConstants, bEnabled)
```

## Parameters

<dl> <dt>

<span id="DVDMenuIDConstants"></span><span id="dvdmenuidconstants"></span><span id="DVDMENUIDCONSTANTS"></span>*DVDMenuIDConstants*
</dt> <dd>

Specifies which menu has been enabled or disabled as a Number value.



| Value | Description |
|-------|-------------|
| 2     | Title       |
| 3     | Root        |
| 4     | Subpicture  |
| 5     | Audio       |
| 6     | Angle       |
| 7     | Chapter     |



 

</dd> <dt>

<span id="bEnabled"></span><span id="benabled"></span><span id="BENABLED"></span>*bEnabled*
</dt> <dd>

Specifies whether the operation is enabled or disabled as a Boolean.

</dd> </dl>

 

 



