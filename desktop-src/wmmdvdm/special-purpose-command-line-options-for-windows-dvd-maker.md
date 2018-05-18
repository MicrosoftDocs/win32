---
title: Special-Purpose Command-line Options for Windows DVD Maker
description: Special-Purpose Command-line Options for Windows DVD Maker
ms.assetid: 'fce18bf7-88bd-4305-bf7d-48b579fc11f2'
keywords: ["Windows DVD Maker,Windows Import Video Wizard", "DVD Maker,Windows Import Video Wizard", "programming reference,Windows Import Video Wizard", "reference for Windows DVD Maker,Windows Import Video Wizard", "command-line options for Windows DVD Maker,Windows Import Video Wizard", "Windows Import Video Wizard", "Windows DVD Maker,crash recovery scenarios", "DVD Maker,crash recovery scenarios", "programming reference,crash recovery scenarios", "reference for Windows DVD Maker,crash recovery scenarios", "command-line options for Windows DVD Maker,crash recovery scenarios"]
---

# Special-Purpose Command-line Options for Windows DVD Maker

Windows DVD Maker also supports the following command-line options.

## -clickonce

The -clickonce option is used only in connection with the Windows Import Video Wizard.

**Syntax**


```C++
dvdmaker -clickonce
```



## /AppRestart

The /AppRestart option is used only in crash recovery scenarios.

**Syntax**


```C++
dvdmaker /AppRestart
```



## Remarks

This option is used when Windows DVD Maker is started from the Windows Import Video Wizard. It should not be used in other situations.

This option is passed to Windows DVD Maker in certain crash recovery scenarios. Windows DVD Maker ignores this option.

## Related topics

<dl> <dt>

[**Command-line Options for Windows DVD Maker**](command-line-options-for-windows-dvd-maker.md)
</dt> </dl>

 

 




