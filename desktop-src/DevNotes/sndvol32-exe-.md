---
description: The SndVol32.exe program controls the volume settings for your system. To display this volume control, go to the Control Panel and start Sounds and Audio Devices. Go to Device volume and click Advanced.
ms.assetid: 20e7fb8a-d0a5-46fa-9813-567fa4f57e8f
title: SndVol32.exe
ms.topic: article
ms.date: 05/31/2018
---

# SndVol32.exe

The SndVol32.exe program controls the volume settings for your system. To display this volume control, go to the Control Panel and start Sounds and Audio Devices. Go to **Device volume** and click **Advanced**.

To execute this program with command-line arguments, go to the **Start** menu, click **Run**, and type the following command.

**SndVol32.exe \[-R \| -D** *n***\]**

<dl> <dt>

<span id="-R"></span><span id="-r"></span>-R
</dt> <dd>

Starts the application in record mode.

</dd> <dt>

<span id="-D_n"></span><span id="-d_n"></span><span id="-D_N"></span>-D *n*
</dt> <dd>

Specifies a device identifier.

</dd> </dl>

## Remarks

This program is the native audio volume and mixer control included in Windows; it is not available for download from Microsoft. The program is typically installed in the following directory: C:\\Windows\\System32.

To locate this file on your system, open Windows Explorer, click the **Search** button, and select **All files and folders**. Type the file name (SndVol32.exe) into the first available line and click the **Search** button.

For more information about using this control, start the program and select **Help**. Note that there is no way to programmatically access the functionality of this program.

## Related topics

<dl> <dt>

[SysTray and SndVol32](https://msdn.microsoft.com/library/ms790410.aspx)
</dt> </dl>

 

 



