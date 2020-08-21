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

You can use the [**mixerGetLineInfo**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetlineinfo) function to retrieve information about a specified audio line. This function fills the [**MIXERLINE**](/windows/win32/api/mmeapi/ns-mmeapi-mixerline) structure for a specified source audio line, destination audio line, or line identifier. The structure includes the destination line number, the number of channels in the audio line, as well as a short and a long name for the audio line.

The [**mixerGetLineControls**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetlinecontrols) function retrieves general information about one or more controls associated with an audio line. This function fills the [**MIXERLINECONTROLS**](/windows/win32/api/mmeapi/ns-mmeapi-mixerlinecontrols) structure with information about the specified control or controls. You can use **mixerGetLineControls** to retrieve control properties for one of the following:

-   All controls for a specified source line
-   A specified control for a specified source line
-   The first control of a specific class for a specified source line

The [**mixerGetControlDetails**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetcontroldetails) function retrieves properties of a single control associated with an audio line. This function fills the [**MIXERCONTROLDETAILS**](/windows/win32/api/mmeapi/ns-mmeapi-mixercontroldetails_listtexta) structure with the current values for a control.

The [**mixerSetControlDetails**](/windows/win32/api/mmeapi/nf-mmeapi-mixersetcontroldetails) function uses the contents of the **MIXERCONTROLDETAILS** structure to set the properties of the specified control. You must ensure that all members of this structure are filled before you call **mixerSetControlDetails**.

 

 