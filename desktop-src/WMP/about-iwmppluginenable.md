---
title: About IWMPPluginEnable
description: About IWMPPluginEnable
ms.assetid: 7611a197-f404-4cfb-88b0-05348a41ac42
keywords:
- Windows Media Player plug-ins,interfaces
- plug-ins,interfaces
- digital signal processing plug-ins,interfaces
- DSP plug-ins,interfaces
- interfaces,DSP plug-ins
- Windows Media Player plug-ins,IWMPPluginEnable interface
- plug-ins,IWMPPluginEnable interface
- digital signal processing plug-ins,IWMPPluginEnable interface
- DSP plug-ins,IWMPPluginEnable interface
- IWMPPluginEnable interface
ms.topic: article
ms.date: 05/31/2018
---

# About IWMPPluginEnable

The **IWMPPluginEnable** interface is required for Windows Media Player DSP plug-ins. **IWMPPluginEnable** contains two methods that store whether Windows Media Player has enabled the DSP plug-in. Windows Media Player calls **IWMPPluginEnable::SetEnable** when it creates an instance of the DSP plug-in, passing a value of **TRUE** if it has enabled the plug-in or **FALSE** otherwise.

DSP plug-ins may remain loaded even when the user chooses to disable them. When disabled, a plug-in must copy data from the input buffer to the output buffer, performing only format conversion processing, if applicable.

Windows Media Player also calls this method before it releases an instance of the DSP plug-in. This is useful to allow clients of the plug-in to check whether the plug-in is currently enabled. For instance, a user interface plug-in might change the appearance of its controls to alert the user that the DSP plug-in is not connected.

## Related topics

<dl> <dt>

[**Required Interfaces**](required-interfaces.md)
</dt> </dl>

 

 




