---
Description: Audio Device Messages for MIDI
ms.assetid: d3b00985-6894-41ea-b493-d0aee269d5bf
title: Audio Device Messages for MIDI
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Audio Device Messages for MIDI

In Windows XP and later versions of Windows (including Windows Vista), the operating system communicates with musical instrument digital interface (MIDI) input and output drivers by using audio device messages.

Every MIDI input and output driver must have one [DriverProc](http://go.microsoft.com/fwlink/p/?linkid=142258) entry-point function to enable or disable the driver. Additionally, it must have an additional entry-point function to process messages from the Windows operating system. In the case of MIDI output drivers, the additional entry-point function is [**modMessage**](/windows/desktop/api/mmddk/), which must be provided by the manufacturer of the MIDI device. This function processes messages that WINMM sends to the MIDI output driver. WINMM is a Windows dynamic link library (DLL) module that contains functions that help the operating system and the MIDI output driver communicate with each other. Specifically, WINMM helps to manage 16-bit multimedia applications that run on Windows.

Each message received by the **modMessage** function comes with two pointers to DWORD variables (DWORD\_PTR). For some messages, one of these parameters points to a structure that contains additional information from the client, or it points to an empty structure for the driver to fill with information for the client. One example of such a structure is [**MIDIOPENDESC**](/windows/desktop/api/mmddk/ns-mmddk-midiopendesc_tag). There are two other structures used by MIDI output device drivers and they are discussed in the Windows SDK. For more information about these structures, see [MIDIHDR](http://go.microsoft.com/fwlink/p/?linkid=142406) and [MIDIOUTCAPS](http://go.microsoft.com/fwlink/p/?linkid=142347).

The following is a list of the audio device messages and the **modMessage** entry-point function that processes them for a MIDI output driver:

<dl>

[**modMessage**](/windows/desktop/api/mmddk/)  
[**MODM\_CACHEDRUMPATCHES**](/windows/desktop/api/Mmddk/)  
[**MODM\_CACHEPATCHES**](/windows/desktop/api/Mmddk/)  
[**MODM\_DATA**](/windows/desktop/api/Mmddk/)  
[**MODM\_GETDEVCAPS**](/windows/desktop/api/Mmddk/)  
[**MODM\_GETNUMDEVS**](/windows/desktop/api/Mmddk/)  
[**MODM\_GETPOS**](/windows/desktop/api/Mmddk/)  
[**MODM\_GETVOLUME**](/windows/desktop/api/Mmddk/)  
[**MODM\_LONGDATA**](/windows/desktop/api/Mmddk/)  
[**MODM\_OPEN**](/windows/desktop/api/Mmddk/)  
[**MODM\_PAUSE**](/windows/desktop/api/Mmddk/)  
[**MODM\_PREPARE**](/windows/desktop/api/Mmddk/)  
[**MODM\_PROPERTIES**](/windows/desktop/api/Mmddk/)  
[**MODM\_RESET**](/windows/desktop/api/Mmddk/)  
[**MODM\_RESTART**](/windows/desktop/api/Mmddk/)  
[**MODM\_SETVOLUME**](/windows/desktop/api/Mmddk/)  
[**MODM\_STOP**](/windows/desktop/api/Mmddk/)  
[**MODM\_STRMDATA**](/windows/desktop/api/Mmddk/)  
[**MODM\_UNPREPARE**](/windows/desktop/api/Mmddk/)  
[**MOM\_CLOSE**](/windows/desktop/api/Mmddk/)  
[**MOM\_DONE**](/windows/desktop/api/Mmsystem/)  
[**MOM\_OPEN**](/windows/desktop/api/Mmddk/)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Baudio\audio%5D:%20Audio%20Device%20Messages%20for%20MIDI%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



