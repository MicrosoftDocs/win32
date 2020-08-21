---
title: Opening a Device
description: Opening a Device
ms.assetid: d4881d32-e8b7-45e6-b00b-b4cd69b738f1
keywords:
- MCI_OPEN command
ms.topic: article
ms.date: 05/31/2018
---

# Opening a Device

Before using a device, you must initialize it by using the [**open**](open.md) ([**MCI\_OPEN**](mci-open.md)) command. This command loads the driver into memory (if it isn't already loaded) and retrieves the device identifier you will use to identify the device in subsequent MCI commands. You should check the return value of the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) or [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function before using a new device identifier to ensure that the identifier is valid. (You can also retrieve a device identifier by using the [**mciGetDeviceID**](/previous-versions//dd757156(v=vs.85)) function.)

Like all MCI command messages, **MCI\_OPEN** has an associated structure. These structures are sometimes called *parameter blocks*. The default structure for **MCI\_OPEN** is [**MCI\_OPEN\_PARMS**](mci-open-parms.md). Certain devices (such as *waveform* and *overlay*) have extended structures (such as [**MCI\_WAVE\_OPEN\_PARMS**](mci-wave-open-parms.md) and [**MCI\_OVLY\_OPEN\_PARMS**](mci-ovly-open-parms.md)) to accommodate additional optional parameters. Unless you need to use these additional parameters, you can use the **MCI\_OPEN\_PARMS** structure with any MCI device.

The number of devices you can have open is limited only by the amount of available memory.

## Using an Alias

When you open a device, you can use the "alias" flag to specify a device identifier for the device. This flag lets you assign a short device identifier for compound devices with lengthy filenames, and it lets you open multiple instances of the same file or device.

For example, the following command assigns the device identifier "birdcall" to the lengthy filename C:\\NABIRDS\\SOUNDS\\MOCKMTNG.WAV:


```C++
mciSendString(
    "open c:\nabirds\sounds\mockmtng.wav type waveaudio alias birdcall", 
    lpszReturnString, lstrlen(lpszReturnString), NULL);
```



In the command-message interface, you specify an alias by using the **lpstrAlias** member of the [**MCI\_OPEN\_PARMS**](mci-open-parms.md) structure.

## Specifying a Device Type

When you open a device, you can use the "type" flag to refer to a device type, rather than to a specific device driver. The following example opens the waveform-audio file C:\\WINDOWS\\CHIMES.WAV (using the "type" flag to specify the **waveaudio** device type) and assigns the alias "chimes":


```C++
mciSendString(
    "open c:\windows\chimes.wav type waveaudio alias chimes", 
    lpszReturnString, lstrlen(lpszReturnString), NULL);
```



In the command-message interface, the functionality of the "type" flag is supplied by the **lpstrDeviceType** member of the [**MCI\_OPEN\_PARMS**](mci-open-parms.md) structure.

## Simple and Compound Devices

MCI classifies device drivers as *compound* or *simple*. Drivers for compound devices require the name of a data file for playback; drivers for simple devices do not.

Simple devices include **cdaudio** and **videodisc** devices. There are two ways to open simple devices:

-   Specify a pointer to a null-terminated string containing the device name from the registry or the SYSTEM.INI file.

    For example, you can open a **videodisc** device by using the following command:


```C++
    mciSendString("open videodisc", lpszReturnString, 
        lstrlen(lpszReturnString), NULL);
```



In this case, "videodisc" is the device name from the registry or the \[mci\] section of SYSTEM.INI.

-   Specify the actual name of the device driver. Opening a device using the device-driver filename, however, makes the application device-specific and can prevent the application from running if the system configuration changes. If you use a filename, you do not need to specify the complete path or the filename extension; MCI assumes drivers are located in a system directory and have the .DRV filename extension.

Compound devices include **waveaudio** and **sequencer** devices. The data for a compound device is sometimes called a *device element*. This document, however, generally refers to this data as a file, even though in some cases the data might not be stored as a file.

There are three ways to open a compound device:

-   Specify only the device name. This lets you open a compound device without associating a filename. Most compound devices process only the [**capability**](capability.md) ([**MCI\_GETDEVCAPS**](mci-getdevcaps.md)) and [**close**](close.md) ([**MCI\_CLOSE**](mci-close.md)) commands when they are opened this way.
-   Specify only the filename. The device name is determined from the associations in the registry.
-   Specify the filename and the device name. MCI ignores the entries in the registry and opens the specified device name.

To associate a data file with a particular device, you can specify the filename and device name. For example, the following command opens the **waveaudio** device with the filename MYVOICE.SND:


```C++
mciSendString("open myvoice.snd type waveaudio", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
```



In the command-string interface, you can also abbreviate the device name specification by using the alternative exclamation-point format, as documented with the [**open**](open.md) command.

## Opening a Device Using the Filename Extension

If the [**open**](open.md) ([**MCI\_OPEN**](mci-open.md)) command specifies only the filename, MCI uses the filename extension to select the appropriate device from the list in the registry or the \[mci extensions\] section of the SYSTEM.INI file. The entries in the \[mci extensions\] section use the following form:

*filename\_extension* = *device\_name*

MCI implicitly uses *device\_name* if the extension is found and if a device name has not been specified in the **open** command.

The following example shows a typical \[mci extensions\] section:


```C++
[mci extensions]
wav=waveaudio
mid=sequencer
rmi=sequencer
```



Using these definitions, MCI opens the **waveaudio** device if the following command is issued:


```C++
mciSendString("open train.wav", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
```



## New Data Files

To create a new data file, simply specify a blank filename. MCI does not save a new file until you save it by using the [**save**](save.md) ([**MCI\_SAVE**](mci-save.md)) command. When creating a new file, you must include a device alias with the [**open**](open.md) ([**MCI\_OPEN**](mci-open.md)) command.

The following example opens a new **waveaudio** file, starts and stops recording, then saves and closes the file:


```C++
mciSendString("open new type waveaudio alias capture", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
mciSendString("record capture", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
mciSendString("stop capture", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
mciSendString("save capture orca.wav", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
mciSendString("close capture", lpszReturnString, 
    lstrlen(lpszReturnString), NULL);
```



## Sharable Devices

The "sharable" (MCI\_OPEN\_SHAREABLE) flag of the [**open**](open.md) ([**MCI\_OPEN**](mci-open.md)) command lets multiple applications access the same device (or file) and device instance simultaneously. If your application opens a device or file as sharable, other applications can also access it by opening it as sharable. The shared device or file gives each application the ability to change the parameters governing its operating state. Each time a device or file is opened as sharable, MCI returns a unique device identifier, even though the identifiers refer to the same instance.

If your application opens a device or file without specifying that it is sharable, no other application can access it until your application closes it. Also, if a device supports only one open instance, the **open** command will fail if you specify the sharable flag.

If your application opens a device and specifies that it is sharable, your application should not make any assumptions about the state of this device. Your application might need to compensate for changes made by other applications accessing the device.

Most compound files are not sharable; however, you can open multiple files, or you can open a single file multiple times. If you open a single file multiple times, MCI creates an independent instance for each, with each instance having a unique operating status.

If you open multiple instances of a file, you must assign a unique device identifier to each. You can use an alias, as described in the following section, to assign a unique name for each file.

 

 