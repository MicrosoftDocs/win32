---
Description: Audio Device Messages for MIDI
ms.assetid: d3b00985-6894-41ea-b493-d0aee269d5bf
title: Audio Device Messages for MIDI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Audio Device Messages for MIDI

In Windows XP and later versions of Windows (including Windows Vista), the operating system communicates with musical instrument digital interface (MIDI) input and output drivers by using audio device messages.

Every MIDI input and output driver must have one [DriverProc](http://go.microsoft.com/fwlink/p/?linkid=142258) entry-point function to enable or disable the driver. Additionally, it must have an additional entry-point function to process messages from the Windows operating system. In the case of MIDI output drivers, the additional entry-point function is [**modMessage**](/windows/win32/mmddk/?branch=master), which must be provided by the manufacturer of the MIDI device. This function processes messages that WINMM sends to the MIDI output driver. WINMM is a Windows dynamic link library (DLL) module that contains functions that help the operating system and the MIDI output driver communicate with each other. Specifically, WINMM helps to manage 16-bit multimedia applications that run on Windows.

Each message received by the **modMessage** function comes with two pointers to DWORD variables (DWORD\_PTR). For some messages, one of these parameters points to a structure that contains additional information from the client, or it points to an empty structure for the driver to fill with information for the client. One example of such a structure is [**MIDIOPENDESC**](/windows/win32/mmddk/ns-mmddk-midiopendesc_tag?branch=master). There are two other structures used by MIDI output device drivers and they are discussed in the Windows SDK. For more information about these structures, see [MIDIHDR](http://go.microsoft.com/fwlink/p/?linkid=142406) and [MIDIOUTCAPS](http://go.microsoft.com/fwlink/p/?linkid=142347).

The following is a list of the audio device messages and the **modMessage** entry-point function that processes them for a MIDI output driver:

<dl>

[**modMessage**](/windows/win32/mmddk/?branch=master)  
[**MODM\_CACHEDRUMPATCHES**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_CACHEPATCHES**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_DATA**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_GETDEVCAPS**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_GETNUMDEVS**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_GETPOS**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_GETVOLUME**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_LONGDATA**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_OPEN**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_PAUSE**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_PREPARE**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_PROPERTIES**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_RESET**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_RESTART**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_SETVOLUME**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_STOP**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_STRMDATA**](/windows/win32/Mmddk/?branch=master)  
[**MODM\_UNPREPARE**](/windows/win32/Mmddk/?branch=master)  
[**MOM\_CLOSE**](/windows/win32/Mmddk/?branch=master)  
[**MOM\_DONE**](/windows/win32/Mmsystem/?branch=master)  
[**MOM\_OPEN**](/windows/win32/Mmddk/?branch=master)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Baudio\audio%5D:%20Audio%20Device%20Messages%20for%20MIDI%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



