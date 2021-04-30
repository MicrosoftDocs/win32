---
description: The Balance property sets or retrieves the speaker balance for the audio stream output.
ms.assetid: b0e6bf16-b1d1-453d-8b58-272565c3d6e6
title: Balance Property
ms.topic: reference
ms.date: 05/31/2018
---

# Balance Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Balance` property sets or retrieves the speaker balance for the audio stream output.

``` syntax
[ iBalance = ] MSWebDVD.Balance
```

## Return Value

Returns an integer value representing the balance levels. The allowable input range is -10,000 to 10,000. A value of 0 sets a neutral balance, that is both left and right speakers are given the same amplitude audio signal.

## Remarks

This property is read/write with a default value of 0, meaning that both speakers receive equivalent audio signals. As with the [**Volume**](volume-property.md) property, units correspond to .01 decibels (multiplied by -1 when


```
iBalance
```



is a positive value). For example, a value of 1000 indicates 10 dB on the right channel and 90 dB on the left channel.

 

 



