---
title: Handling Errors with MIDI Functions
description: Handling Errors with MIDI Functions
ms.assetid: 7ea5db5e-34d7-4506-8157-c24adf5bcdda
keywords:
- Musical Instrument Digital Interface (MIDI),errors
- MIDI (Musical Instrument Digital Interface),errors
- MIDI services,errors
- MIDI errors
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Handling Errors with MIDI Functions

MIDI audio functions return a nonzero error code. For MIDI-associated errors, the [**midiInGetErrorText**](https://msdn.microsoft.com/en-us/library/Dd798454(v=VS.85).aspx) and [**midiOutGetErrorText**](https://msdn.microsoft.com/en-us/library/Dd798470(v=VS.85).aspx) functions retrieve textual descriptions for the error codes. The application must still look at the error value itself to determine how to proceed, but it can use the error descriptions in dialog boxes to inform users of the error conditions.

The only MIDI functions that do not return error codes are the [**midiInGetNumDevs**](https://msdn.microsoft.com/en-us/library/Dd798456(v=VS.85).aspx) and [**midiOutGetNumDevs**](https://msdn.microsoft.com/en-us/library/Dd798472(v=VS.85).aspx) functions. These functions return a value of zero if no devices are present in a system or if any errors are encountered by the function.

## Related topics

<dl> <dt>

[MIDI Services](midi-services.md)
</dt> </dl>

 

 




