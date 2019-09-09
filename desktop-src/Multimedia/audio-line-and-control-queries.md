---
title: Audio Line and Control Queries
description: Audio Line and Control Queries
ms.assetid: f0954fc7-9961-410a-a638-a7025fb2616a
keywords:
- multimedia audio,mixer controls
- audio,mixer controls
- audio mixers,audio lines
- audio lines
- audio mixers,controls
- mixers,controls
- mixers,audio lines
ms.topic: article
ms.date: 05/31/2018
---

# Audio Line and Control Queries

The mixer services provide functions for determining information about audio lines, audio-line controls, and control details. The services also provide functions for setting control details.

You can use the [**mixerGetLineInfo**](https://msdn.microsoft.com/en-us/library/Dd757303(v=VS.85).aspx) function to retrieve information about a specified audio line. This function fills the [**MIXERLINE**](https://msdn.microsoft.com/en-us/library/Dd757305(v=VS.85).aspx) structure for a specified source audio line, destination audio line, or line identifier. The structure includes the destination line number, the number of channels in the audio line, as well as a short and a long name for the audio line.

The [**mixerGetLineControls**](https://msdn.microsoft.com/en-us/library/Dd757302(v=VS.85).aspx) function retrieves general information about one or more controls associated with an audio line. This function fills the [**MIXERLINECONTROLS**](https://msdn.microsoft.com/en-us/library/Dd757306(v=VS.85).aspx) structure with information about the specified control or controls. You can use **mixerGetLineControls** to retrieve control properties for one of the following:

-   All controls for a specified source line
-   A specified control for a specified source line
-   The first control of a specific class for a specified source line

The [**mixerGetControlDetails**](https://msdn.microsoft.com/en-us/library/Dd757299(v=VS.85).aspx) function retrieves properties of a single control associated with an audio line. This function fills the [**MIXERCONTROLDETAILS**](/windows/win32/api/mmeapi/ns-mmeapi-mixercontroldetails_listtexta) structure with the current values for a control.

The [**mixerSetControlDetails**](https://msdn.microsoft.com/en-us/library/Dd757309(v=VS.85).aspx) function uses the contents of the **MIXERCONTROLDETAILS** structure to set the properties of the specified control. You must ensure that all members of this structure are filled before you call **mixerSetControlDetails**.

 

 




